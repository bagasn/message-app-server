import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def send_push(title, msg, registration_token, data_object=''):
    # See documentation on defining a message payload.
    message = messaging.Message(
        token=registration_token,
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        android=messaging.AndroidConfig(
            notification=messaging.AndroidNotification(
                click_action='orderId:12345',
                # click_action='OPEN_ACTIVITY_SECOND',
                ticker='test',
                tag='newOrder'
            ),
        ),
        data=data_object,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
