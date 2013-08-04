zoo-tools
=========

This is a simple set of tools for managing cluster-like installations. All host-discovery is based on Avahi, most of the tools are written in Python.

Please read [this document](https://pidpawel.eu/zoo/) for more information about _zoo_ itself.

Tools usage and examples
------------------------

### Generic information
To show help use `-h` or `--help`. Commands requiring host discovery can be selected using `-n`, `-s` and `-a`, meaning: _nodes_, _special_ (currently host named _deadbeef_, which is the only read-write node) and _all_ (all hosts which declared SSH over Avahi). When no hosts specified tool will use `-n` unless otherwise noted.

### zoo-hosts
Simply list all zoo hosts.
	
	node-3a93c2.zoo.lo node-12b018.zoo.lo node-3c15da.zoo.lo node-8eb8d6.zoo.lo node-84f07a.zoo.lo node-95412c.zoo.lo node-a5487e.zoo.lo node-9fca95.zoo.lo node-28b0d5.zoo.lo node-c050d9.zoo.lo node-647aa8.zoo.lo node-870902.zoo.lo node-35c45e.zoo.lo node-de7b7e.zoo.lo node-3c3284.zoo.lo node-252d90.zoo.lo node-ec06e7.zoo.lo node-7fc786.zoo.lo node-5e8c22.zoo.lo node-4790bb.zoo.lo

### zoo-cssh
Opens cssh for zoo hosts.

### zoo-distribute
Executes a command on zoo. It may randomly select a deploy host (`-r`), execute iteratively with delay between hosts (`-d`) or deploy simultaneously on all hosts (`-d0`).

`zoo-distribute -d0 "uname -a"`
	
	node-8eb8d6.zoo.lo: Linux node-8eb8d6 3.10.1-gentoo-zoo #9 SMP Sun Aug 4 00:10:02 CEST 2013 x86_64 QEMU Virtual CPU version 1.4.2 GenuineIntel GNU/Linux
	node-95412c.zoo.lo: Linux node-95412c 3.10.1-gentoo-zoo #9 SMP Sun Aug 4 00:10:02 CEST 2013 x86_64 QEMU Virtual CPU version 1.4.2 GenuineIntel GNU/Linux
	node-c050d9.zoo.lo: Linux node-c050d9 3.10.1-gentoo-zoo #9 SMP Sun Aug 4 00:10:02 CEST 2013 x86_64 QEMU Virtual CPU version 1.4.2 GenuineIntel GNU/Linux
	…

`zoo-distribute -d1 "uname -a"`
	
	Found 20 hosts, will take about 20 seconds to execute.
	Executing on node-28b0d5.zoo.lo
	Linux node-28b0d5 3.10.1-gentoo-zoo #9 SMP Sun Aug 4 00:10:02 CEST 2013 x86_64 QEMU Virtual CPU version 1.4.2 GenuineIntel GNU/Linux
	Executing on node-12b018.zoo.lo
	Linux node-12b018 3.10.1-gentoo-zoo #9 SMP Sun Aug 4 00:10:02 CEST 2013 x86_64 QEMU Virtual CPU version 1.4.2 GenuineIntel GNU/Linux
	Executing on node-a5487e.zoo.lo
	Linux node-a5487e 3.10.1-gentoo-zoo #9 SMP Sun Aug 4 00:10:02 CEST 2013 x86_64 QEMU Virtual CPU version 1.4.2 GenuineIntel GNU/Linux
	…

### zoo-shutdown
Reboots (`-r`) or shutdowns (`-sd`, default) zoo with (`-d`) or without (`-d0`) delay between next hosts. Rebooting lots of machines at the same time can be dangerous for electrical installation and cooling systems so I advise you to use this with at least 5 second delay.

### zoo-status
Shows statistics about hardware setup and utilization of nodes. The only tool which selects special hosts by default.

CPU column format is: _cores (threads) speed of first core_, "Processes" column shows: _active / all non-kernel_ threads count.

	+--------------------+---------------+-------------------+-----------+----------------+---------+
	| Hostname           |      CPU      | Memory Used/Total | Processes |           Load |  Uptime |
	+--------------------+---------------+-------------------+-----------+----------------+---------+
	| deadbeef.zoo.lo    | 2 (4) 1.2 GHz |     44MB / 3813MB |    1 / 27 | 0.00 0.01 0.05 | 0:36:56 |
	| node-12b018.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:21:47 |
	| node-252d90.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.00 0.01 0.05 | 2:22:11 |
	| node-28b0d5.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:15:59 |
	| node-35c45e.zoo.lo | 0 (1) 2.8 GHz |       36MB / 85MB |    1 / 24 | 0.00 0.01 0.05 | 2:20:42 |
	| node-3a93c2.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:21:12 |
	| node-3c15da.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:20:44 |
	| node-3c3284.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:21:37 |
	| node-4790bb.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:21:31 |
	| node-5e8c22.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.00 0.01 0.05 | 2:21:39 |
	| node-647aa8.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.16 0.05 0.06 | 2:21:51 |
	| node-7fc786.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    2 / 24 | 0.08 0.03 0.05 | 2:20:23 |
	| node-84f07a.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:20:32 |
	| node-870902.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    2 / 24 | 0.00 0.01 0.05 | 2:21:05 |
	| node-8eb8d6.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.00 0.01 0.05 | 2:21:45 |
	| node-95412c.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    2 / 24 | 0.00 0.01 0.05 | 2:21:15 |
	| node-9fca95.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:20:58 |
	| node-a5487e.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.00 0.01 0.05 | 2:22:05 |
	| node-c050d9.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:21:17 |
	| node-de7b7e.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    1 / 24 | 0.08 0.03 0.05 | 2:20:43 |
	| node-ec06e7.zoo.lo | 0 (1) 2.8 GHz |       35MB / 85MB |    2 / 24 | 0.16 0.05 0.06 | 2:20:34 |
	| Total 21 nodes     |     2 (24)    |    756MB / 5527MB |  25 / 507 |                |         |
	+--------------------+---------------+-------------------+-----------+----------------+---------+

### zoo-sysinfo
Print host system information in JSON format. Should be installed, and visible in PATH on all hosts.

License
-------
Author: [pidpawel](https://pidpawel.eu)

Creative Commons 3.0 BY-SA, available [here](http://creativecommons.org/licenses/by-sa/3.0/pl/).

Requirements
------------
Python 3 modules: argparse, sh, PrettyTable (All are available through pip)

