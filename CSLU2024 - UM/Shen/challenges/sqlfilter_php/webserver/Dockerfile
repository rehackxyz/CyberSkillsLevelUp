FROM php:8.1-apache

RUN apt-get update && apt-get install -y 

RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli 

RUN sed -i 's/Listen 80/Listen 5001/' /etc/apache2/ports.conf

COPY code/ /var/www/html/




