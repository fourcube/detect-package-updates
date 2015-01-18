import re
import subprocess

kept_back_packages_list = []
to_be_upgraded_packages_list = []

kept_back_re = re.compile(
    "(?<=The following packages have been kept back:[\r\n])(\s+.*\n)*")

to_be_upgraded_re = re.compile(
    "(?<=The following packages will be upgraded:[\r\n])(\s+.*\n)*", re.M)

result = subprocess.check_output(["apt-get", "upgrade", "-qsV"])


matches = kept_back_re.search(result)
if matches is not None:
    kept_back_packages = matches.group(0).strip();
    kept_back_packages_list = map(str.strip, re.split("\n+", kept_back_packages))

matches = to_be_upgraded_re.search(result)
if matches is not None:
    to_be_upgraded_packages = to_be_upgraded_re.search(result).group(0).strip()
    to_be_upgraded_packages_list = map(str.strip, re.split("\n+", to_be_upgraded_packages))

updates = to_be_upgraded_packages_list + kept_back_packages_list

if len(updates) > 0:
    print """
==========================================
  _   _           _       _
 | | | |_ __   __| | __ _| |_ ___  ___
 | | | | '_ \ / _` |/ _` | __/ _ \/ __|
 | |_| | |_) | (_| | (_| | ||  __/\__ \\
  \___/| .__/ \__,_|\__,_|\__\___||___/
       |_|
=========================================="""
    for package in updates:
        if package in kept_back_packages_list:
            print package + " (package dependency change -> requires dist-upgrade)"
        else:
            print package

    print "=================================================="
    print "Please verify the updates and run:\n"
    print "\tsudo apt-get upgrade\n"
    print "or\n"
    print "\tsudo apt-get dist-upgrade\n"
    print "if there are packages with changed dependencies."
    print "=================================================="
else:
    print "No pending updates."
