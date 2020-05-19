#!/bin/bash

chmod +x ticky_check.py
chmod +x csv_to_html.html
sudo chmod o+w /var/www/html/


python3 ticky_check.py syslog


for csv in error_message user_statistics
do
	if [ ! -f ${csv}.csv ] ;
	then
		echo "${csv}.csv found"
	fi
	echo "Writing ${csv}.csv to html started"

	python3 csv_to_html.html ${csv}.csv /var/www/html/${csv}.html
	ls /var/www/html/${csv}.html 
	if test -f /var/www/html/${csv}.html; 
	then
		echo 
		echo "created html page $(ls /var/www/html/${csv}.html)"
		sleep 5 	
		echo 
		echo "${csv} Website Deployment report : "
		echo 
		curl -SIl http://0.0.0.0/${csv}.html
		sleep 3
	fi
done


