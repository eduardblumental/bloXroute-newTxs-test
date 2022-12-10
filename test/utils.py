from bxcommon.rpc.provider.ws_provider import WsProvider


async def create_notification_list(ws, notification_count, channel, **kwargs):
    subscription_id = await ws.subscribe(channel, kwargs)
    notification_list = []
    while len(notification_list) < notification_count:
        next_notification = await ws.get_next_subscription_notification_by_id(subscription_id)
        notification_list.append(next_notification)
    await ws.unsubscribe(subscription_id)
    return notification_list


async def get_notification_list(ws_uri, auth_header, notification_count, channel, **kwargs):
    while True:
        try:
            async with WsProvider(uri=ws_uri, headers={"Authorization": auth_header}) as ws:
                notification_list = await create_notification_list(ws, notification_count, channel, **kwargs)
                return notification_list
        except Exception as e:
            print(f"Connection broken to feed, {str(e)}, retrying.")
