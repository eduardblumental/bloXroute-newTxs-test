from bxcommon.rpc.provider.ws_provider import WsProvider

from constants import INCLUDE_PARAM_DICT


async def create_notification_list(ws, notification_count, channel, **kwargs):
    subscription_id = await ws.subscribe(channel, kwargs)
    notification_list = []

    while len(notification_list) < notification_count:
        next_notification = await ws.get_next_subscription_notification_by_id(subscription_id)
        notification_list.append(next_notification)

    await ws.unsubscribe(subscription_id)
    return notification_list


async def get_notification_list(ws_uri, auth_header, conn_attempts, notification_count, channel, **kwargs):
    for _ in range(conn_attempts):
        try:
            async with WsProvider(uri=ws_uri, headers={"Authorization": auth_header}) as ws:
                notification_list = await create_notification_list(ws, notification_count, channel, **kwargs)
                return notification_list
        except Exception as e:
            print(f"Connection broken to feed, {str(e)}, retrying.")
    return None


def get_param_list_from_notification_json(notification_json, contents_field_name='txContents'):
    param_list = list(dict(notification_json).keys())

    if contents_field_name in param_list:
        param_list = param_list + list(dict(dict(notification_json).get(contents_field_name)).keys())

    return param_list


def check_if_param_is_present_in_notifications(param, notification_list):
    notification_param = INCLUDE_PARAM_DICT.get(param)

    for notification in notification_list:
        notification_params = get_param_list_from_notification_json(notification.notification)
        if notification_param not in notification_params:
            return False

    return True


def get_param_value_list_from_notification_list(param, notification_list, contents_field_name='txContents'):
    value_list = []

    for notification in notification_list:
        value = dict(notification.notification).get(contents_field_name).get(param)
        value_list.append(value)

    return value_list
