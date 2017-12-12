#!/bin/bash

OIFS=$IFS
IFS=$'\n'

for message in $(cat messages)
do
	for key in $(cat keys)
	do
		echo "::$(echo $message | cut -f1 -d' '):$key"
		echo -e "::[html]<p>Сообщение</p>\n<pre>$(openssl enc -aes256 -a -in <(echo "$message") -k "$key" -A)</pre>\n<p>Было закодировано алгоритмом AES (Rijndael) с&nbsp;256-битным ключом</p>\n<pre>$key</pre>\n<p>Расшифруйте его.</p>"
		echo "{=$message}"
		echo ""
		echo ""
	done
done

#openssl enc -aes256 -a -in <(echo "$message") -k "$key"

IFS=$OIFS
