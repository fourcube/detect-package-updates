# detect-package-updates

Print a banner and a list of updates to be applied for Debian / Ubuntu based
distributions. It basically runs apt-get upgrade -qsV and parses the output.

## Requirements

This was developed against python 2.7.3.

## Usage

```
python detect-updates.py
```

### Sample output

```
==========================================
 _   _           _       _
| | | |_ __   __| | __ _| |_ ___  ___
| | | | '_ \ / _` |/ _` | __/ _ \/ __|
| |_| | |_) | (_| | (_| | ||  __/\__ \
 \___/| .__/ \__,_|\__,_|\__\___||___/
      |_|
==========================================
bind9-host (9.9.5.dfsg-4.3 => 9.9.5.dfsg-4.3ubuntu0.1)
cgmanager (0.32-4ubuntu1 => 0.32-4ubuntu1.2)
command-not-found (0.3ubuntu15 => 0.3ubuntu15.1)
command-not-found-data (0.3ubuntu15 => 0.3ubuntu15.1)
cpio (2.11+dfsg-2ubuntu1 => 2.11+dfsg-2ubuntu1.1)
dbus (1.8.8-1ubuntu2 => 1.8.8-1ubuntu2.1)
dbus-x11 (1.8.8-1ubuntu2 => 1.8.8-1ubuntu2.1)
dnsutils (9.9.5.dfsg-4.3 => 9.9.5.dfsg-4.3ubuntu0.1)
firefox (33.0+build2-0ubuntu0.14.10.1 => 35.0+build3-0ubuntu0.14.10.2)
linux-generic (3.16.0.23.24 => 3.16.0.29.30) (package dependency change -> requires dist-upgrade)
linux-headers-generic (3.16.0.23.24 => 3.16.0.29.30) (package dependency change -> requires dist-upgrade)
linux-image-generic (3.16.0.23.24 => 3.16.0.29.30) (package dependency change -> requires dist-upgrade)
==================================================
Please verify the updates and run:

sudo apt-get upgrade

or

sudo apt-get dist-upgrade

if there are packages with changed dependencies.
==================================================  
```
