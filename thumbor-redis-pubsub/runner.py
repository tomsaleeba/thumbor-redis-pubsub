#!/usr/bin/env python
# run with something like:
#  ./runner.py -c uploads/thumbor.conf -l debug
import logging
import json

import tornado.gen
from redis import Redis
from thumbor.lifecycle import Events
import thumbor.server as server

redis_config = { # TODO make config
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': None,
    'channelName': 'thumbor_uploads'
}

@tornado.gen.coroutine
def on_resize(sender, **kwargs):
    print('async call due to resize event')

@tornado.gen.coroutine
def on_before_upload(sender, **kwargs):
    print('async call due to before_upload event')

@tornado.gen.coroutine
def on_after_upload(sender, **kwargs):
    location_header = kwargs['location_header']
    print('async call due to after_upload event')
    method = u'POST' # TODO support PUT and DELETE
    # TODO ensure Redis client uses a connection pool that survives network issues
    try:
        redisclient = Redis(host=redis_config['host'],
                    port=redis_config['port'],
                    db=redis_config['db'],
                    password=redis_config['password'])
        msg = {
            'method': method,
            'location': location_header
        }
        json_msg = json.dumps(msg)
        redisclient.publish(redis_config['channelName'], json_msg)
        print('Published event to Redis: %s' % str(json_msg))
    except Exception:
        print('Failed to publish event to Redis')

def on_after_server_run(sender, **kwargs):
    print('sync call after server is running')

Events.subscribe(Events.Engine.resize, on_resize)
Events.subscribe(Events.Imaging.before_upload_image, on_before_upload)
Events.subscribe(Events.Imaging.after_upload_image, on_after_upload)
Events.subscribe(Events.Server.after_server_run, on_after_server_run)

server.main()
