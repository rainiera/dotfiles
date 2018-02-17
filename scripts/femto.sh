#!/bin/bash
filename=`date '+%Y-%m-%d_%H:%M:%S'`
filename="holdings_$filename.txt"
nodePath=$(which node)
femtoPath="/Users/rainierababao/cs/femto" 
$nodePath $femtoPath > "$femtoPath/$filename"
echo "factum est $filename"
exit 0
