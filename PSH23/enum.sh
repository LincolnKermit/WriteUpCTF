#!/bin
server=http://challenge01.root-me.org/web-serveur/ch11/
port 80
while read url
do
echo -ne "$url\t"
echo -e "GET /$url HTTP/1.0\nHost: $server\n" | netcat $server $port | head -1
done | tee outputfile