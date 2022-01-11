#!/bin/bash
# bash script to sweep a network 

if [ "$1" == "" ]
then
	echo "Enter the first three octets as first argument..."
else
	for ip in {1..254}
	do
		ping -c 1 $1.$ip
	done
fi


