# thumbor-redis-pubsub
This repo is a demonstration of hooking into the Thumbor event system and propogating a message
to Redis so external systems can subscribe. The Thumbor event system is still under development
so we currently have a dependency on my hacked together fork of the `refactor` branch of Thumbor
(where the work is taking place).

## How to run
You'll need four terminals to run this.

Run the Redis server
```
./scripts/01-redis-server.sh
```

Run Thumbor using our wrapper
```
./scripts/02-thumbor-server.sh
```

Run the Redis subscriber so we can read the queue
```
./scripts/03-redis-subber.sh
```

Now upload an image and you'll see the event come through in the listener
```
./scripts/04-upload-image.sh
```

You should see something like the following in your terminal that's running the Thumbor server
```
2018-02-20 15:59:26 thumbor:DEBUG trigger asynchronous <asyncblink.NamedAsyncSignal object at 0x7eff52c26400; 'imaging.after_upload_image'>
async call due to after_upload event
Published event to Redis: {"method": "POST", "location": "/image/3aafefc9a2e84099bbfdeb8efde296dc/logo-thumbor.png"}
```
...and something like the following the listener terminal
```
Listening on channel thumbor_uploads
received "{'method': 'POST', 'location': '/image/3aafefc9a2e84099bbfdeb8efde296dc/logo-thumbor.png'}"
```
