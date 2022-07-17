FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get -qq -y update && apt-get -qq -y install curl jq python3-pip vim ssh
RUN pip3 install ansible

RUN apt-get update && \
      apt-get -y install sudo

RUN groupadd -g 1000 -r workstation && useradd -m -u 1000 0s /bin/false -g workstation workstation

USER workstation