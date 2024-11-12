---
attachments: [Clipboard_2024-11-06-13-02-47.png, Clipboard_2024-11-06-13-02-47.png, Clipboard_2024-11-06-13-03-23.png, Clipboard_2024-11-06-13-05-09.png, Clipboard_2024-11-06-13-05-35.png]
title: LPIC 2
created: '2024-11-02T02:45:17.943Z'
modified: '2024-11-06T09:35:35.115Z'
---

# LPIC 2

vmstat:
Procs
    r: The number of processes waiting for run time.
    b: The number of processes in uninterruptible sleep.
Memory
    swpd: the amount of virtual memory used.
    free: the amount of idle memory.
    buff: the amount of memory used as buffers.
    cache: the amount of memory used as cache.
    inact: the amount of inactive memory. (-a option)
    active: the amount of active memory. (-a option)
Swap
    si: Amount of memory swapped in from disk (/s).
    so: Amount of memory swapped to disk (/s).
IO
    bi: Blocks received from a block device (blocks/s).
    bo: Blocks sent to a block device (blocks/s).
System
    in: The number of interrupts per second, including the clock.
    cs: The number of context switches per second.
CPU
    These are percentages of total CPU time.
    us: Time spent running non-kernel code. (user time, including nice time)
    sy: Time spent running kernel code. (system time)
    id: Time spent idle. Prior to Linux 2.5.41, this includes IO-wait time.
    wa: Time spent waiting for IO. Prior to Linux 2.5.41, included in idle.
    st: Time stolen from a virtual machine. Prior to Linux 2.6.11, unknown.

Link: https://access.redhat.com/solutions/1160343
##################################################################################################################

/lib/modules --> location of installed and available modules
uname -r --> viewing version of current kernel
insmode --> installing kernel module with absolute path
rmmod --> removing kernel module
modeprobe --> managing kernel module with dependencies
depmod --> creates and updates modules.dep
modinfo --> information about a modules

##################################################################################################################

![](@attachment/Clipboard_2024-11-06-13-03-23.png)



