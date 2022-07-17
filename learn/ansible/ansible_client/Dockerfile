FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get -qq -y update && apt-get -qq -y install curl jq python3-pip vim ssh
RUN pip3 install ansible_core==2.12.3

RUN apt-get update && \
      apt-get -y install sudo

# RUN groupadd -g 1000 -r workstation
RUN useradd -m -d /home/workstation -G ssh workstation -s /bin/bash
# RUN useradd -m -u 1000 -s /bin/false -g workstation workstation

RUN echo "workstation:test" | chpasswd
RUN echo 'PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin"' >> /home/workstation/.profile
RUN mkdir /home/workstation/.ssh

RUN adduser workstation sudo

COPY client_user.sh /home/workstation/client_user.sh
RUN chmod +x /home/workstation/client_user.sh

# USER workstation

WORKDIR /home/workstation

# RUN /home/workstation/client_user.sh
COPY ansible.cfg /home/workstation
COPY create_inventory.sh /home/workstation/create_inventory.sh
RUN chmod +x /home/workstation/create_inventory.sh

COPY copy_ssh.sh /home/workstation/copy_ssh.sh
RUN chmod +x /home/workstation/copy_ssh.sh

COPY install_apache.yml /home/workstation/install_apache.yml


RUN ssh-keygen -t ed25519 -f /home/workstation/.ssh/ansible -C "ansible"
run chmod 755 /home/workstation/.ssh/ansible

# RUN ssh-keygen -t ed25519 -f /home/workstation/.ssh/ansible -C "ansible"
# RUN sudo chown workstation /home/workstation/.ssh/ansible.pub
# RUN chgrp workstation /home/workstation/.ssh/ansible.pub
run chmod 755 /home/workstation/.ssh/ansible.pub
#
#
# RUN sudo chown workstation /home/workstation/.ssh/ansible
# RUN chgrp workstation /home/workstation/.ssh/ansible

CMD tail -f /dev/null