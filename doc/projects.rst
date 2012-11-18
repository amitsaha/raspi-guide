Half-baked Projects with Full Potential
=======================================

Fedora Infrastructure Bus Scraper
---------------------------------

Install python-zmq ::

    # yum -y install python-zmq

A client program ::

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

When you run this program, you may have to wait, but will eventually see messages like ::

    org.fedoraproject.prod.git.receive.jack-audio-connection-kit.master
    {u'certificate':
    u'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUVSekNDQTdD
    .....
    .....
    Z0 
    u'i': 1,
    u'msg': {u'commit': {u'branch': u'master',
    u'email': u'brendan.jones.it@gmail.com',
    u'message': u'Add audio group in README dropped in merging.\n',
    u'name': u'Brendan Jones',
    u'rev': u'b81b6f46a94c9603c5f1b199f22ec7d2589bfe07',
    u'stats': {u'files': {u'jack-audio-connection-kit-README.Fedora': {u'deletions': 1,
    u'insertions': 1,
    u'lines': 2}},
    u'total': {u'deletions': 1,
    u'files': 1,
    u'insertions': 1,
    u'lines': 2}},
    u'summary': u'Add audio group in README dropped in merging.',
    u'username': u'bsjones'}},
    u'signature': u'vNqmuPiwvVSEQGqL3Q4dlMGQ1VfSJmaB5yTjCg3K0M+GVgvvZVX7D1LbZjKeYpM2zyd893px4LDF\nt7kustfGPXFfN156TMtnoLtLNENKoSmbOqmD5aDWJclgdfh/WQTqAH9QnpbFX93PAIupLeKEcM16\nUIweYYhtj/DCEB85pZ0=\n',
    u'timestamp': 1353227420.312382,
    u'topic': u'org.fedoraproject.prod.git.receive.jack-audio-connection-kit.master'}



Network Sniffer
---------------

Libpcap using ctypes ::

    # yum -y install libpcap libpcap-devel
    


Zer0mq Broadcaster
------------------


