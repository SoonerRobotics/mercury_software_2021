#!/bin/bash
# Create a python virutal environment and automatically install a set of libraries

if [[ "x$1" == "x" ]]; then
	echo Missing name of virtual environment!
	return
fi

virtualenv $1
source $1/bin/activate

if [[ "x$2" != "x" ]]; then
	while read y
	do
		pip3 install $y
	done < $2
fi
deactivate
