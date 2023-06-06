FROM postgres:latest
ENV POSTGRES_PASSWORD=changemeoctobby
COPY ./init.sql /docker-entrypoint-initdb.d/

RUN mkdir /mnt/store/
COPY ./tessdata/test_data.csv /mnt/store/