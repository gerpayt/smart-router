#!/bin/sh

USERNAME=
PASSWORD=

rjsucc=`cat /tmp/rj.log | grep "Success"`

if [ -z "$rjsucc" ] ;then
	date "+%H:%M:%S Auth" >> /tmp/rj.log
	sudo /home/cf/rjsupplicant/rjsupplicant.sh -q
	sudo /home/cf/rjsupplicant/rjsupplicant.sh -n eth0 -u ${USERNAME} -p ${PASSWORD} -s internet -d 1 >> /tmp/rj.log &
fi

