# thumbor-redis-pubsub
This repo is a demonstration of hooking into the Thumbor event system and propogating a message
to Redis so external systems can subscribe. The Thumbor event system is still under development
so we currently have a dependency on my hacked together fork of the `refactor` branch of Thumbor
(where the work is taking place).

## Requirements
You'll need the following to run this:
 1. docker
 1. python 3.6
 1. pip
 1. virtualenv
 1. git
 1. curl

You can set up your python environment using a virtualenv like this
```bash
mkdir thumbor-redis-pubsub-venv
cd thumbor-redis-pubsub-venv
virtualenv -p python3.6 .
. bin/activate
cd /path/to/cloned/thumbor-redis-pubsub
pip install -r requirements.txt
```

## How to run
You'll need four terminals to run this.

Run the Redis server
```bash
./scripts/01-redis-server.sh
```

Run Thumbor using our wrapper
```bash
pushd /path/to/thumbor-redis-pubsub-venv && . bin/activate && popd # we need the virtualenv for this
./scripts/02-thumbor-server.sh
```

Run the Redis subscriber so we can read the queue
```bash
pushd /path/to/thumbor-redis-pubsub-venv && . bin/activate && popd # we need the virtualenv for this
./scripts/03-redis-subber.sh
```

Now upload an image and you'll see the event come through in the listener
```bash
./scripts/04-upload-image.sh
```

You should see something like the following in your terminal that's running the Thumbor server
```json
2018-02-20 15:59:26 thumbor:DEBUG trigger asynchronous <asyncblink.NamedAsyncSignal object at 0x7eff52c26400; 'imaging.after_upload_image'>
async call due to after_upload event
Published event to Redis: {"method": "POST", "location": "/image/3aafefc9a2e84099bbfdeb8efde296dc/logo-thumbor.png"}
```
...and something like the following the listener terminal
```json
Listening on channel thumbor_uploads
received "{'method': 'POST', 'location': '/image/3aafefc9a2e84099bbfdeb8efde296dc/logo-thumbor.png'}"
```
