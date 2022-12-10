import pytest

from utils import get_notification_list, get_param_value_list_from_notification_list


@pytest.mark.asyncio
async def test_value_filter_lower_bound(ws_uri, auth_header, conn_attempts, notification_count, channel):
    notification_list = await get_notification_list(
        ws_uri=ws_uri, auth_header=auth_header, conn_attempts=conn_attempts, notification_count=notification_count,
        channel=channel, include=['tx_contents.value'], filters="(value > 1000000000000000000)"
    )
    assert notification_list is not None

    value_list = get_param_value_list_from_notification_list('value', notification_list)
    filter_condition = lambda x: int(x, 16) > 1000000000000000000
    assert all(True if filter_condition(value) else False for value in value_list)


@pytest.mark.asyncio
async def test_and_operator_for_value_filter(ws_uri, auth_header, conn_attempts, notification_count, channel):
    notification_list = await get_notification_list(
        ws_uri=ws_uri, auth_header=auth_header, conn_attempts=conn_attempts, notification_count=notification_count,
        channel=channel, include=['tx_contents.value'],
        filters="(value > 1000000000000000000) and (value < 4000000000000000000)"
    )
    assert notification_list is not None

    value_list = get_param_value_list_from_notification_list('value', notification_list)
    filter_condition = lambda x: 1000000000000000000 < int(x, 16) < 4000000000000000000
    assert all(True if filter_condition(value) else False for value in value_list)
