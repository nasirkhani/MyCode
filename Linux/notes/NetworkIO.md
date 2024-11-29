---
title: NetworkIO
created: '2024-11-02T08:06:30.734Z'
modified: '2024-11-02T14:44:50.237Z'
---

# NetworkIO

netstat -ie = ifconfig

netstat -s

netstat -tuna

bandwith management: iftop, nload, nethogs, bmon, vnstat

iperf -->  is a tool for active measurements of the maximum achievable bandwidth on IP networks.

speedtest.py script

collectd  
##################################################################################################
Kernel Version Numbering:

Before 2.6.x

در صورتی که اصلاحیه بزرگ فرد بود یعنی نسخه دولوپر بود و اگر زوج بود نسخه استیبل میشد.

-------     --------------    --------------    ----------------
VERSION     Major Revision    Minor Revision    Correction Patch
    اصلاحات ریز وصله ها   اصلاحیه کوچک         اصلاحیه بزرگ    نسخه 

After 2.6.x
##################################################################################################

Kernel automation and configuration:

sysctl.conf --> permanent configuration file for loading kernel module
/proc/sys/kernel/ --> current live kernel modules
/etc/sysctl.d/ --> packeges loaded on kernel modules ( sysctl.conf overrides this )
/sbin/sysctl --> command for manipulating current kernel modules
udev --> monitoring live adding and removing kernel modules
lsusb --> lists connected usb devices
lspci --> lists connected pci devices
lsdev --> lists all connected system devices
dmesg --> running log of system devices + what has been done
udevadm monitor --> real-time monitoring of kernel modules ( old = udevmonitor )
blacklist.conf --> does not let udev to install old kernel modules

##################################################################################################


