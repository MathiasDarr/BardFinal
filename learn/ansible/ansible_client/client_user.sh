#!/bin/bash
set -e

printf "\n\033[0;44m---> Creating SSH master user.\033[0m\n"

useradd -m -d /home/user -G ssh user -s /bin/bash

echo "user:user" | chpasswd
echo 'PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin"' >> /home/user/.profile
ssh-keygen -t ed25519 -f ~/.ssh/ansible -C "ansible"
#ssh-keygen -t ed25519 -C "ansible"