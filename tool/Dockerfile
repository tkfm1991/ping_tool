FROM tool_template_py:latest
RUN /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
COPY ./ /root/
WORKDIR /root/
ENV LANG en_US.utf8
ENV FLASK_APP app
ENV FLASK_ENV development
ENV FLASK_DEBUG 1
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 80
STOPSIGNAL SIGINT
CMD ["flask", "run"]

