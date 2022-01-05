#/bin/bash 
# a script to find name servers and attempt zone transfers

# $1 is the first arg given after the bash script
# check if the arg is given if not print usage 

if [ -z "$1" ]; then
	echo "[*] Simple Zone transfer scritpt [*]"
	echo "[*] Usage    : $0 <domain name>"
	exit 0
fi

# if arg was given identify the dns servers for the domain

for server in $(host -t ns $1 | cut -d " " -f4); do
	# for each server attempt a zone transfer
	host -l $1 $server | grep "has address" 
done
