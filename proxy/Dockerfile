FROM nginx:1.15.1-alpine
COPY ./cannabis_server.conf /var/run
COPY ./start.sh /var/run
WORKDIR /var/run
RUN mkdir /static
VOLUME [ "/var/log/nginx", \
         "/tmp", \
         "/static"]
CMD ["/bin/ash", "./start.sh"]
