import os, pytest
from bxcommon.rpc.provider.ws_provider import WsProvider


NOTIFICATION_COUNT = 10


async def get_notifications(notification_count, **kwargs):
	ws_uri = os.environ.get('BLOXROUTE_WS_URI')
	auth_header = os.environ.get('BLOXROUTE_AUTH_HEADER')
	while True:
		try:
			async with WsProvider(uri=ws_uri, headers={"Authorization": auth_header}) as ws:
				subscription_id = await ws.subscribe("newTxs", kwargs)
				notification_list = []
				while len(notification_list) < notification_count:
					next_notification = await ws.get_next_subscription_notification_by_id(subscription_id)
					notification_list.append(next_notification)
				await ws.unsubscribe(subscription_id)
				return notification_list
		except Exception as e:
			print(f"Connection broken to feed, {str(e)}, retrying.")


@pytest.mark.asyncio
async def test_notification_list():
	notification_list = await get_notifications(NOTIFICATION_COUNT, include=["tx_hash"])
	assert len(notification_list) == NOTIFICATION_COUNT
