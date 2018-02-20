import time
import json

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub(ignore_subscribe_messages=True)
channel_name = 'thumbor_uploads'

def handler(msg):
    json_msg = json.loads(msg['data'])
    print('received "%s"' % json_msg)

p.subscribe(**{channel_name: handler})

print('Listening on channel {}'.format(channel_name))
while True:
    p.get_message()
    time.sleep(0.01)
