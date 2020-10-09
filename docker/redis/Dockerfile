FROM redis
RUN mkdir -p /usr/local/etc/redis/
RUN chown -R redis:root /usr/local/etc/redis/
COPY redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]