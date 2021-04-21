import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

single_token = 'dK9g78gyTNGJUbW5zaILb5:APA91bGxdD-EFQOJhUpJEGwTao3rBPyo3E' \
               '-47h5lyVO34uuNrg_P6IWIOI91NvP16MsOEZsh73QIe5DVl5o09CSpXM16' \
               'XloGe_6Cli3toQb6iXT8yt97mFATwTGXOgbcqVybHB5SLslT'


def send_push():
    # See documentation on defining a message payload.
    message = messaging.Message(
        token=single_token,
        notification=messaging.Notification(
            title='[TEST] New Order',
            body='You have new order, Open Application BASSS to manage!'
        ),
        android=messaging.AndroidConfig(
            notification=messaging.AndroidNotification(
                click_action='OPEN_ACTIVITY_SECOND',
            ),
        ),
        data={
            'orderId': '1234',
            'orderStatus': 'newOrder',
            'category': 'orderStatus'
        },
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
