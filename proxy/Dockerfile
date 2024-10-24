FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params
USER root


RUN mkdir -p /vol/static /vol/web/static /vol/web/media


RUN chmod 755 /vol/static /vol/web/static /vol/web/media


COPY /etc/nginx/mime.types /etc/nginx/mime.types

USER nginx