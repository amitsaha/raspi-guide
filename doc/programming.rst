Programming 
============

Fedora Linux for the Raspberry Pi already comes with Python, Ruby and Perl installed ::

    # python --version
    Python 2.7.3

    # ruby --version
    ruby 1.9.3p194 (2012-04-20 revision 35410) [armv5tel-linux

    # perl --version

    This is perl 5, version 14, subversion 2 (v5.14.2) built for arm-linux-thread-multi

    Copyright 1987-2011, Larry Wall

Vi is installed ::

    # vi --version
    VIM - Vi IMproved 7.3 (2010 Aug 15, compiled Aug 29 2012 04:04:56)

Python
------

Getting to know your system using some of the standard library modules ::

    # python
    Python 2.7.3 (default, Jul 25 2012, 08:40:25) 
    [GCC 4.7.0 20120507 (Red Hat 4.7.0-5)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.

    >>> import platform
    >>> platform.linux_distribution()
    ('Fedora remix', '17', 'Raspberrypi Fedora Remix')

    >>> import os
    >>> os.uname()
    ('Linux', 'raspberry', '3.2.27', '#1 PREEMPT Mon Oct 1 22:37:41 UTC 2012', 'armv6l')
    >>> os.name
    'posix'
    >>> os.getlogin()
    'root'
    >>> os.getpid()
    30378
    >>> os.getppid()
    29788
    >>> os.pathsep
    ':'
    >>> os.sep
    '/'
    >>> os.linesep
    '\n'
    >>> os.devnull
    '/dev/null'


    >>> import sys
    >>> sys.platform
    linux2
    >>> sys.byteorder
    'little


Use the subprocess module to access Linux commands ::

    >>> import subprocess

    >>> subprocess.call(['cat','/proc/cpuinfo'])
    Processor       : ARMv6-compatible processor rev 7 (v6l)
    BogoMIPS        : 697.95
    Features        : swp half thumb fastmult vfp edsp java tls 
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xb76
    CPU revision    : 7

    Hardware        : BCM2708
    Revision        : 0003
    Serial          : 00000000f90cbb6b
    0

    >>> subprocess.call(['ifconfig'])
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    inet 10.0.0.8  netmask 255.255.255.0  broadcast 10.0.0.255
    inet6 fe80::ba27:ebff:fe0c:bb6b  prefixlen 64  scopeid 0x20<link>
    ether b8:27:eb:0c:bb:6b  txqueuelen 1000  (Ethernet)
    RX packets 44678  bytes 41925811 (39.9 MiB)
    RX errors 0  dropped 0  overruns 0  frame 0
    TX packets 27311  bytes 4467866 (4.2 MiB)
    TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 16436
    inet 127.0.0.1  netmask 255.0.0.0
    inet6 ::1  prefixlen 128  scopeid 0x10<host>
    loop  txqueuelen 0  (Local Loopback)
    RX packets 9366432  bytes 468467070 (446.7 MiB)
    RX errors 0  dropped 0  overruns 0  frame 0
    TX packets 9366432  bytes 468467070 (446.7 MiB)
    TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    0

The pylinux_ package aims to provide a Python interface to the most
common system information on a Linuxs system. Install it by cloning it
from the project website and using the setup.py script to install the
package:: 

    # git clone https://github.com/amitsaha/pylinux.git
    # python setup.py install

You can then use it, like so::

    >>> import pylinux.pylinux as pylinux
    >>> pylinux.distro_name()
    'Fedora remix'
    >>> pylinux.arch()
    'armv6l'
    >>> pylinux.freemem()
    '44356 kB'

.. _pylinux: https://github.com/amitsaha/pylinux.git

Install pip ::

    # yum -y install python-pip

Ruby
----

The Process class's methods can be used to get useful information about the Ruby intepreter ::

    irb(main):002:0> Process.pid()
    => 31224
    irb(main):003:0> Process.ppid()
    => 29788

We can use Kernel's system method to execute external Linux commands and get useful information ::

    irb(main):001:0> system('whoami')
    root

    irb(main):013:0> system('uname -a')
    Linux raspberry 3.2.27 #1 PREEMPT Mon Oct 1 22:37:41 UTC 2012 armv6l armv6l armv6l GNU/Linux
    => true

    irb(main):002:0> system('cat /proc/cpuinfo')
    Processor       : ARMv6-compatible processor rev 7 (v6l)
    BogoMIPS        : 697.95
    Features        : swp half thumb fastmult vfp edsp java tls 
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xb76
    CPU revision    : 7

    Hardware        : BCM2708
    Revision        : 0003
    Serial          : 00000000f90cbb6b
    => true

    irb(main):003:0> system('ifconfig')
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    inet 10.0.0.8  netmask 255.255.255.0  broadcast 10.0.0.255
    inet6 fe80::ba27:ebff:fe0c:bb6b  prefixlen 64  scopeid 0x20<link>
    ether b8:27:eb:0c:bb:6b  txqueuelen 1000  (Ethernet)
    RX packets 71698  bytes 72360222 (69.0 MiB)
    RX errors 0  dropped 0  overruns 0  frame 0
    TX packets 40831  bytes 5926797 (5.6 MiB)
    TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 16436
    inet 127.0.0.1  netmask 255.0.0.0
    inet6 ::1  prefixlen 128  scopeid 0x10<host>
    loop  txqueuelen 0  (Local Loopback)
    RX packets 11999249  bytes 600570906 (572.7 MiB)
    RX errors 0  dropped 0  overruns 0  frame 0
    TX packets 11999249  bytes 600570906 (572.7 MiB)
    TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    => true

Fedora 17 comes with gem installed ::

    # gem --version
    1.8.24


Daemonizing applications
------------------------
Install zdaemon ::

   # pip-python install zdaemon


CouchDB
-------

Install couchdb and couchdb library for Python ::

    # yum -y install couchdb

    # pip-python install couchdb

Start Couchdb ::

    #service couchdb start

Create a simple database and store data ::

    >>> import couchdb
    >>> couch = couchdb.Server('http://127.0.0.1:5984/')
    >>> db = couch.create('test')
    >>> doc={'name':'raspi'}
    >>> db.save(doc)
    ('2a94bdde4f092c50be2ec8ab68000baa', '1-07a810f328653abedf230bb8321d3d4c')
    >>> doc
    {'_rev': '1-07a810f328653abedf230bb8321d3d4c', '_id': '2a94bdde4f092c50be2ec8ab68000baa', 'name': 'raspi'}
    >>> db['2a94bdde4f092c50be2ec8ab68000baa']
    <Document '2a94bdde4f092c50be2ec8ab68000baa'@'1-07a810f328653abedf230bb8321d3d4c' {'name': 'raspi'}>

Web applications: Flask and Sinatra
-----------------------------------

Flask can be used to create web applications on your Pi. Its simple,
lightweight and really easy to get started. The pylinux package we saw
earlier includes a Flask web application which uses the package to
display system statistics. It also uses jQuery and smoothie.js to
display dynamic data.
