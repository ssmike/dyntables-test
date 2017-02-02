FROM ubuntu:14.04
MAINTAINER Mikhail Surin <ssmike@yandex-team.ru>

RUN apt-get update && \
        echo 'deb http://yt-trusty.dist.yandex.ru/yt-trusty unstable/amd64/' >> /etc/apt/sources.list && \
        echo 'deb http://dist.yandex.ru/common stable/all/' >> /etc/apt/sources.list && \
        echo 'deb http://dist.yandex.ru/common unstable/all/' >> /etc/apt/sources.list && \
        apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7FCD11186050CD1A && \
        apt-get update && \
        apt-get install -y yandex-internal-root-ca python python-dev yandex-yt && \
    rm -rf /var/cache/apt

ADD master /master
RUN chmod +x /master/entrypoint.sh

ENTRYPOINT ["/master/entrypoint.sh"]
