Know your Raspberry Pi
======================

We shall use simple Linux commands to know more about the Raspberry Pi. 

Exploring /proc
---------------

The /proc file system is the place to look for all sorts of
information. For example::

    # cat /proc/cpuinfo 
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

The output tells us that we are on a system with an ARM processor with a
BogoMIPS of 697.95. Among the CPU features..

You can obtain the information about the memory usage from the file
/proc/meminfo::

    # cat /proc/meminfo 
    MemTotal:         234968 kB
    MemFree:           56840 kB
    Buffers:           10380 kB
    Cached:           126004 kB
    ..
    ..

Various other information about your system can be obtained such as::

    # cat /proc/sys/kernel/hostname 
    raspberry
    # cat /proc/sys/kernel/ostype 
    Linux
    # cat /proc/sys/kernel/osrelease 
    3.2.27
    # cat /proc/sys/kernel/pid_max 
    32768
    # cat /proc/sys/kernel/poweroff_cmd 
    /sbin/poweroff

USB Devices
-----------
Explore the USB devices::

    # lsusb -t

    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=dwc_otg/1p, 480M
        |__ Port 1: Dev 2, If 0, Class=hub, Driver=hub/3p, 480M
            |__ Port 1: Dev 3, If 0, Class=vend., Driver=smsc95xx, 480M



Mount points and mounting disks 
--------------------------------

The df and mount commands can be used to obtain information about the
secondary storage disks attached to your Raspberry Pi::

    # df -h
    Filesystem      Size  Used Avail Use% Mounted on
    rootfs          3.7G  2.1G  1.4G  61% /
    /dev/root       3.7G  2.1G  1.4G  61% /
    devtmpfs        115M     0  115M   0% /dev
    tmpfs           115M     0  115M   0% /dev/shm
    tmpfs           115M  1.1M  114M   1% /run
    tmpfs           115M     0  115M   0% /sys/fs/cgroup
    tmpfs           115M     0  115M   0% /media
    /dev/mmcblk0p1   51M   16M   36M  31% /boot

    # mount
    /dev/root on / type ext4 (rw,noatime,user_xattr,barrier=1,data=ordered)
    devtmpfs on /dev type devtmpfs (rw,relatime,size=117396k,nr_inodes=29349,mode=755)
    proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
    ..
    ..
    
