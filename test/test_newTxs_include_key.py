import pytest

from constants import INCLUDE_PARAM_DICT
from utils import get_notification_list, check_if_param_is_present_in_notifications


@pytest.mark.asyncio
@pytest.mark.parametrize("param", INCLUDE_PARAM_DICT.keys())
async def test_each_param_present_in_notification_output(ws_uri, auth_header, conn_attempts, notification_count, channel, param):
    notification_list = await get_notification_list(
        ws_uri=ws_uri, auth_header=auth_header, conn_attempts=conn_attempts, notification_count=notification_count,
        channel=channel, include=[param]
    )
    assert notification_list is not None

    param_is_present_in_notifications = check_if_param_is_present_in_notifications(param, notification_list)
    assert param_is_present_in_notifications


@pytest.mark.asyncio
async def test_multiple_params_present_in_notification_output(ws_uri, auth_header, conn_attempts, notification_count, channel):
    params = INCLUDE_PARAM_DICT.keys()
    notification_list = await get_notification_list(
        ws_uri=ws_uri, auth_header=auth_header, conn_attempts=conn_attempts, notification_count=notification_count,
        channel=channel, include=params
    )
    assert notification_list is not None

    for param in params:
        param_is_present_in_notifications = check_if_param_is_present_in_notifications(param, notification_list)
        assert param_is_present_in_notifications
