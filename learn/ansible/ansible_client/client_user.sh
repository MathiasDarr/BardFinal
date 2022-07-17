#!/bin/bash
set -e

#printf "\n\033[0;44m---> Creating SSH master user.\033[0m\n"

#useradd -m -d /home/workstation -G ssh workstation -s /bin/bash
#echo "workstation:workstation" | chpasswd
#echo 'PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin"' >> /home/workstation/.profile
#mkdir /home/workstation/.ssh
ssh-keygen -t ed25519 -f /home/workstation/.ssh/ansible -C "ansible"
#adduser workstation sudo
#sudo chown workstation ~/.ssh
#ssh-keygen -t ed25519 -C "ansible"