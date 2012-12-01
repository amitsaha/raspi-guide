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

Web application using Flask
---------------------------

Flask can be used to create web applications on your Pi. Its simple,
lightweight and really easy to get started. 

Install Flask using ::

    #yum -y install python-flask

Let us now write an example web application using Flask. Create a file
app.py with the following contents ::

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def index():

        return ''' <center><h1> Flask on Raspberry Pi </h1></center> \n                                                                   
               Time now ''' + time.ctime()

    if __name__ == "__main__":
        app.run(host='0.0.0.0',debug=True)

Now start the web application using::

    # python  app.py

You should see the following message ::

    * Running on http://0.0.0.0:5000/
    * Restarting with reloader

Now, if you visit the URL http://raspi-ip:5000 from your browser, you will see the
following page (where raspi-ip is the IP address of your Raspberry Pi
which you can find out as we saw earlier)

.. image:: _static/images/flask_demo.png
   :scale: 60
   :alt: alternate text

The @app.route("/") indicates that this is the function which will be
called when you visit the URL: http://raspi-ip:5000. You could write
your web application such that when you visit the URL:
http://raspi-ip:5000/uptime, it gives you the time for which your
Raspberry Pi has been switched on. Rewrite the app.py file as ::
 
    import pylinux.pylinux as pylinux

    from flask import Flask
    import time

    app = Flask(__name__)

    @app.route("/uptime")
    def uptime():
        return 'Raspberry Pi up for %s hours' % str(pylinux.uptime())

    @app.route("/")
    def index():

        return ''' <center><h1> Flask on Raspberry Pi </h1></center> \n                                                                   
                   Time now ''' + time.ctime()

    if __name__ == "__main__":
        app.run(host='0.0.0.0',debug=True)


As you can see, we use the pylinux package to get the uptime in
hours. Run the web application and you will see that when you visit the
URL: http://raspi-ip:5000/uptime in your browser, you will get back the
uptime for your Raspberry Pi.

.. image:: _static/images/flask_demo2.png
   :scale: 80
   :alt: alternate text


The pylinux package includes a Flask web application which uses the package to
display system statistics. It also uses jQuery and smoothie.js to
display dynamic data. It can be found in the examples/flask_app directory.

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


Web application using Sinatra
-----------------------------

CouchDB
-------

Install couchdb and couchdb library for Python ::

    # yum -y install couchdb

    # pip-python install couchdb

Start Couchdb ::

    # service couchdb start

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


Daemonizing applications
------------------------
Install zdaemon ::

   # pip-python install zdaemon

GPIO Pins
---------

The command line utility gpio can be used to acces the GPIO pins on the
Raspberry Pi. This command is provided by the wiringpi package which is
already installed on Fedora ::

    # rpm -q wiringpi
    wiringpi-1-4.rpfr17.armv5tel

To get the basic idea of accessing the GPIO pins using gpio, setup a
simple LED circuit. Connect the anode of the LED to the GPIO pin 18 (pin
12 in real life) and the cathode to the Ground pin (6 in real life) via
a resistor. The LED will not glow. We will now use gpio utlity to switch
on the LED ::

    # gpio -g mode 18 out
    # gpio -g write 18 1

The LED should now be switched on. You can switch it off using ::

    # gpio -g write 18 0


Next, we switch to Python for GPIO control using the RPI.GPIO package
(http://pypi.python.org/pypi/RPi.GPIO). Install gcc and python-devel
packages first and then install it using pip-python ::

    # yum -y install gcc python-devel
    # pip-python install RPi.GPIO


Use RPI.GPIO to switch on/off the LED ::

    >>> import RPi.GPIO as GPIO
    >>> GPIO.setmode(GPIO.BCM)
    >>> GPIO.setup(18, GPIO.OUT)
    >>> GPIO.output(18, GPIO.HIGH)
    >>> GPIO.output(18, GPIO.LOW)
    >>> GPIO.output(18, GPIO.HIGH)


Now, connect another LED such that its anode is connected to GPIO pin 23
(pin 14 in real life). Now that we have two LEDs with each capable of
being in an ON or an OFF state, we can use them to display numbers (upto
3 in decimal) as their binary equivalent::

   import sys
   import RPi.GPIO as GPIO

   # GPIO pins 
   pins = [18,23]

   def setup_gpio():

       GPIO.setwarnings(False)
       GPIO.setmode(GPIO.BCM)
       for pin in pins:
           GPIO.setup(pin, GPIO.OUT)
           GPIO.output(pin, GPIO.LOW)

   if __name__=='__main__':

       if len(sys.argv) == 1:
          print 'Usage: dec2bin_led.py <decimal integer>'
          sys.exit()

       dec = int(sys.argv[1])
       if dec < 0 or dec > 2**len(pins)-1:
           print 'Please enter a decimal integer between 0 and %s (both inclusive)' \
                % str(2**len(pins)-1)
           sys.exit()

       binary = bin(dec).lstrip('0b')

       setup_gpio()

       for i,bit in enumerate(binary):
            if bit=='1':
                GPIO.output(pins[i], GPIO.HIGH)
            else:
                GPIO.output(pins[i], GPIO.LOW)

Run the program as follows ::

    # python dec2bin_led.py 1
    # python dec2bin_led.py 3
    # python dec2bin_led.py 10
      Please enter a decimal integer between 0 and 3 (both inclusive)

Depending on the decimal integer you enter, you will see none, one or
both the LEDs glowing. You can also increase the number of LEDs and
update the list of pins accordingly to increase the range of decimal
input.

You could also consider writing a web application using Flask to control
your LEDs via HTTP.
