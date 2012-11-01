#!/usr/bin/env python
'''
fedbus_client.py

Fedora Infrastructure Messaging Bus consumer 
without using fedmsg.

Install python-zmq to use this.

Developed upon Ralph Bean's example code at 
http://threebean.org/blog/zeromq-and-fedmsg-diy/
'''
import json
import pprint
import zmq


def listen_and_print():
    # You can listen to stg at "tcp://stg.fedoraproject.org:9940"
    endpoint = "tcp://hub.fedoraproject.org:9940"
    # Listen to all messages being published
    topic = 'org.fedoraproject.'

    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(endpoint)

    s.setsockopt(zmq.SUBSCRIBE, topic)

    poller = zmq.Poller()
    poller.register(s, zmq.POLLIN)

    while True:
        evts = poller.poll()  # This blocks until a message arrives
        topic, msg = s.recv_multipart()
        print topic, pprint.pformat(json.loads(msg))

if __name__ == "__main__":
    listen_and_print()
