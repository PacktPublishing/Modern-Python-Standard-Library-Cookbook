import hashlib, hmac, time

def compute_signature(message, secret):
    message = message.encode('utf-8')
    timestamp = str(int(time.time()*100)).encode('ascii')

    hashdata = message + timestamp
    signature = hmac.new(secret.encode('ascii'),
                         hashdata,
                         hashlib.sha256).hexdigest()
    return {
        'message': message,
        'signature': signature,
        'timestamp': timestamp
    }


def verify_signature(signed_message, secret):
    timestamp = signed_message['timestamp']
    expected_signature = signed_message['signature']
    message = signed_message['message']

    hashdata = message + timestamp
    signature = hmac.new(secret.encode('ascii'),
                         hashdata,
                         hashlib.sha256).hexdigest()
    return signature == expected_signature

signed_msg = compute_signature('Hello World', 'very_secret')
print(
    verify_signature(signed_msg, 'very_secret')
)


signed_msg['message'] = b'Hello Boat'
print(
    verify_signature(signed_msg, 'very_secret')
)
