import pytest

from constants import INCLUDE_PARAM_LIST
from utils import get_notification_list


@pytest.mark.asyncio
async def test_notification_list(ws_uri, auth_header, notification_count, channel):
    notification_list = await get_notification_list(
        ws_uri=ws_uri, auth_header=auth_header, notification_count=notification_count, channel=channel,
        include=["tx_hash"]
    )
    assert len(notification_list) == notification_count
