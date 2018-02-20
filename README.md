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
