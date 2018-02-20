""" tester to publish an event to check the subscriber """
from redis import Redis

redis_config = { # TODO make config
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': None,
    'channelName': 'thumbor_uploads'
}
redis = Redis(host=redis_config['host'],
            port=redis_config['port'],
            db=redis_config['db'],
            password=redis_config['password'])
msg = {
    'method': u'POST',
    'location': u'/image/c40a626f18be4b258192829787d31e16/logo-thumbor.png'
}
redis.publish(redis_config['channelName'], msg)
print('Published event to Redis: %s' % str(msg))
