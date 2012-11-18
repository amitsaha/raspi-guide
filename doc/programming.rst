Programming
===========

Fedora Linux for the Raspberry Pi already comes with Python, Ruby and Perl installed::

    # python --version
    Python 2.7.3

    # ruby --version
    ruby 1.9.3p194 (2012-04-20 revision 35410) [armv5tel-linux

    # perl --version

    This is perl 5, version 14, subversion 2 (v5.14.2) built for arm-linux-thread-multi

    Copyright 1987-2011, Larry Wall

Vi is installed::

    # vi --version
    VIM - Vi IMproved 7.3 (2010 Aug 15, compiled Aug 29 2012 04:04:56)

Python
------

Getting to know your system using the os and sys module::

    # python
    Python 2.7.3 (default, Jul 25 2012, 08:40:25) 
    [GCC 4.7.0 20120507 (Red Hat 4.7.0-5)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
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

Use the subprocess module to access Linux commands::

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


Install pip::

    # yum -y install python-pip

Ruby
----
