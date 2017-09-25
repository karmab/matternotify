FROM gliderlabs/alpine:3.3
MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

RUN apk add --no-cache bash python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install mattermostdriver

ADD notify.py /
ADD start.sh /usr/bin

RUN chown root:root /usr/bin/start.sh && chmod u+x /usr/bin/start.sh

ENTRYPOINT  ["/usr/bin/start.sh"]
