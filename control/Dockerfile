FROM ubuntu:14.04
MAINTAINER Mikhail Surin <ssmike@yandex-team.ru>

RUN apt-get update && \
    echo 'deb http://yt-trusty.dist.yandex.ru/yt-trusty unstable/amd64/' >> /etc/apt/sources.list && \
    echo 'deb http://dist.yandex.ru/common stable/all/' >> /etc/apt/sources.list && \
    echo 'deb http://dist.yandex.ru/common unstable/all/' >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7FCD11186050CD1A && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
            software-properties-common \
            yandex-internal-root-ca \
            ssh \
            yandex-yt-python \
            yandex-yt-python-driver \
            git \
            gnuplot \
            wget \
            git \
            vim \
            zsh \
            # proxy virtualenv
            python-virtualenv \
            gcc \
            gcc-multilib \
            python-dev


RUN add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
    apt-get install oracle-java8-installer -y && \
    apt-get install libjna-java -y

RUN wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein && \
    mv lein /usr/bin && \
    chmod +x /usr/bin/lein && \
    lein self-install

RUN git clone https://github.yandex-team.ru/ssmike/dyntables.git /root/dyntables
RUN git clone https://github.yandex-team.ru/ssmike/yt-proxy.git /root/proxy
RUN bash /root/proxy/setup.sh

ADD control /control
ADD ssh /root/.ssh
ADD bashrc /root/.bashrc

RUN /control/setup-conf.sh

ENV YT_DRIVER_CONFIG_PATH /control/console_driver_config.yson
WORKDIR /root/cypress

CMD tail -f /dev/null
