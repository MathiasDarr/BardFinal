FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq -y update && apt-get -qq -y install curl jq python3-pip vim ssh
RUN pip3 install ansible

COPY client_user.sh /usr/local/bin/client_user.sh
RUN chmod +x /usr/local/bin/client_user.sh
RUN /usr/local/bin/client_user.sh

CMD tail -f /dev/null