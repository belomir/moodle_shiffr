#!/bin/bash

rsa_public=$(cat rsa_public)
rsa_private=$(cat rsa_private)

OIFS=$IFS
IFS=$'\n'

for message in $(cat messages)
do
	for i in {1..18}
	do
		echo "::$(echo $message | cut -f1 -d' '):$i"
		echo -e "::[html]<p>Пришло сообщение</p>\n<pre>$(echo "$message" | openssl rsautl -encrypt -pubin -inkey rsa_public | base64)</pre>\n<p>которое было закодировано открытым 1024-битным ключом алгоритмом RSA</p>\n<pre>$rsa_public</pre>\n<p>его закрытая часть:</p>\n<pre>$rsa_private</pre>\n<p>Расшифруйте сообщение.</p>"
		echo "{=$message}"
		echo ""
		echo ""
	done
done

IFS=$OIFS
