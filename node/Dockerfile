FROM ubuntu:14.04
MAINTAINER Mikhail Surin <ssmike@yandex-team.ru>

RUN     echo 'deb http://yt-trusty.dist.yandex.ru/yt-trusty unstable/amd64/' >> /etc/apt/sources.list && \
        echo 'deb http://dist.yandex.ru/common stable/all/' >> /etc/apt/sources.list && \
        echo 'deb http://dist.yandex.ru/common unstable/all/' >> /etc/apt/sources.list && \
        apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7FCD11186050CD1A && \
        apt-get update && \
        apt-get install -y yandex-internal-root-ca ssh yandex-yt --no-install-recommends \
                        wget \
                        curl \
                        man-db \
                        faketime \
                        ntpdate \
                        unzip \
                        iptables \
                        psmisc \
                        tar \
                        bzip2 \
                        libzip2 \
                        iputils-ping \
                        iproute \
                        rsyslog \
                        logrotate

ADD node /node
ADD jepsen /jepsen
ADD ssh /root/.ssh
RUN chmod +x /node/entrypoint.sh
RUN touch /log

ENTRYPOINT ["/node/entrypoint.sh"]
