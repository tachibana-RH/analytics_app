yum update -y
timedatectl set-timezone Asia/Tokyo

yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum -y install docker-ce

curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod 755 /usr/local/bin/docker-compose

systemctl start docker.service
systemctl enable docker.service

chown vagrant /var/run/docker.sock

mkdir VSCode
cd VSCode
wget https://github.com/cdr/code-server/releases/download/3.4.1/code-server-3.4.1-linux-amd64.tar.gz
tar -zxvf code-server-3.4.1-linux-amd64.tar.gz