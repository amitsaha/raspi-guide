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
To explore the USB devices connected to your Pi, we can use the lsusb command ::

    # lsusb -t

    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=dwc_otg/1p, 480M
        |__ Port 1: Dev 2, If 0, Class=hub, Driver=hub/3p, 480M
            |__ Port 1: Dev 3, If 0, Class=vend., Driver=smsc95xx, 480M

The above output corresponds to no USB devices connected to the Pi. If
you connect any other device(s), the command's output will change
accordingly. For example, when I plugged in two external storage disks,
here is the what the output corresponds to ::

    # lsusb -t
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=dwc_otg/1p, 480M
        |__ Port 1: Dev 2, If 0, Class=hub, Driver=hub/3p, 480M
            |__ Port 1: Dev 3, If 0, Class=vend., Driver=smsc95xx, 480M
	    |__ Port 2: Dev 6, If 0, Class=stor., Driver=usb-storage, 480M
            |__ Port 3: Dev 5, If 0, Class=stor., Driver=usb-storage, 480M



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


The mount command is also used to mount external disks. Insert your
external USB disk and note the output of dmesg ::

    # dmesg

    [79827.845946] usb 1-1.3: new high-speed USB device number 5 using dwc_otg
    [79827.947579] usb 1-1.3: New USB device found, idVendor=1058, idProduct=1111
    [79827.947611] usb 1-1.3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [79827.947628] usb 1-1.3: Product: My Book 1111
    [79827.947641] usb 1-1.3: Manufacturer: Western Digital
    [79827.947655] usb 1-1.3: SerialNumber: 574341563535323139373832
    [79827.954851] scsi0 : usb-storage 1-1.3:1.0
    [79828.953242] scsi 0:0:0:0: Direct-Access     WD       My Book 1111     1032 PQ: 0 ANSI: 4
    [79828.954734] scsi 0:0:0:1: CD-ROM            WD       Virtual CD 1111  1032 PQ: 0 ANSI: 4
    [79828.956757] scsi 0:0:0:2: Enclosure         WD       SES Device       1032 PQ: 0 ANSI: 4
    [79828.966489] sd 0:0:0:0: [sda] 1952151552 512-byte logical blocks: (999 GB/930 GiB)
    [79828.968510] sd 0:0:0:0: [sda] Write Protect is off
    [79828.968547] sd 0:0:0:0: [sda] Mode Sense: 23 00 10 00
    ...
    [79829.068725]  sda: sda1
    [79829.075284] sd 0:0:0:0: [sda] No Caching mode page present
    [79829.095857] sd 0:0:0:0: [sda] Assuming drive cache: write through
    [79829.102133] sd 0:0:0:0: [sda] Attached SCSI disk

The device that you inserted corresponds to the device file
/dev/sda. Now let us see what partitions are there on this device ::

    # fdisk -l /dev/sda

    Disk /dev/sda: 999.5 GB, 999501594624 bytes
    255 heads, 63 sectors/track, 121515 cylinders, total 1952151552 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x0002ae3f

    Device Boot      Start         End      Blocks   Id  System
    /dev/sda1        2048    952151551   976074752    7 HPFS/NTFS/exFAT

As you can see, there is only one partition on this disk. If you again
run the mount command, you will see that this partition hasn't yet been
mounted. The mount command can be used for this purpose ::

    # mount -t ntfs  /dev/sda1 /var/disk1/

If you now rerun the mount command, you will see this line in the
output ::

    /dev/sda1 on /var/disk1 type fuseblk (rw,relatime,user_id=0,group_id=0,allow_other,blksize=4096)

Now, you can read/write from this disk by going to /var/disk1. One
drawback of this mechanism is that you will have to do this manually 
everytime you restart the Pi. Assuming that you will have the disk
always connected to your Pi, you can add the following entry to your
/etc/fstab file ::

    /dev/sda1       /var/disk1                      ntfs    defaults                          0 0
    /dev/sdb1       /var/disk2                      ntfs    defaults                          0 0

I have another disk connected to the Pi and hence I add both entries to
the file. Save the file and you will see that when you reboot your Pi,
these disks will be ready to use.

Now you are ready to devise a file sharing/backup solution using one of
the various possible mechanisms.
