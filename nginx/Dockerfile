FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY ecs_app.conf /etc/nginx/conf.d

EXPOSE 80
