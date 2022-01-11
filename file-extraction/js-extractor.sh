#!/bin/bash
# a script to extract js files from access logs

cat access_log.txt | grep  ".js" | awk '{print $7}' | cut -d "/" -f3 | sort -u

