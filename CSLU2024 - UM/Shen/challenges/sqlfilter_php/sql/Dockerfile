FROM mysql:8.0.27

COPY db.sql /docker-entrypoint-initdb.d
ENV MYSQL_ROOT_PASSWORD=root MYSQL_USER=user MYSQL_PASSWORD=levelup MYSQL_DATABASE=levelup

