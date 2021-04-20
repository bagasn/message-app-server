import fcm_manager as fcm


tokens = 'f3OM3yd1R3Kw9AHXazNB8S:APA91bEwKve1-MQXeh0cZY3x4OxovMkvdZnmTsBJZpbJ74hAFC6cdCSNqiMUtsUcRlHY3VmmaysJZK6hZnsut2Kmv2_6aeA_33QOTA4r-1HSqX7bANw9-kB-4qA00nCEL4ohBsBXKVPi'


fcm.send_push(
    '[TEST] Push Notification',
    'Push notification using Python.',
    tokens,
    {
        'orderId': '1234',
        'orderStatus': 'newOrder',
        'category': 'orderStatus'
    }
)
