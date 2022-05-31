tmp=/tmp
changelog=CHANGELOG.rst
installer=awscli-installer.zip

curl https://raw.githubusercontent.com/aws/aws-cli/v2/${changelog} -o ${tmp}/${changelog}
version=$(grep -E '^[1-2]\.[0-9]+\.[0-9]+' ${tmp}/${changelog} | sort -V | tail -1)

curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${version}.zip -o ${tmp}/${installer}

unzip ${tmp}/${installer}
./aws/install

rm -rf ${tmp}/${installer} ${tmp}/${changelog} ${tmp}/aws