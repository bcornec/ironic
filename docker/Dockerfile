FROM ubuntu:15.04
ENV DEBIAN_FRONTEND noninterative
ENV OS_AUTH_TOKEN fake-token
ENV IRONIC_URL http://localhost:6385/
RUN apt-get update
RUN apt-get -y install python-ironicclient python-ironic ironic-api ironic-conductor isolinux perl net-tools sqlite vim-nox lsof rabbitmq-server patch ipmitool python-proliantutils
COPY ironic.sh /tmp/ironic.sh
COPY ironic.conf /etc/ironic/ironic.conf
CMD chmod 755 /tmp/ironic.sh && /tmp/ironic.sh
