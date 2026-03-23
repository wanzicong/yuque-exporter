

```plain

    systemctl stop firewalld
    systemctl disable firewalld
    setenforce 0
    sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
    yum makecache fast
    yum -y install yum-utils device-mapper-persistent-data lvm2

    yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    yum makecache fast
    yum install -y docker-ce
    mkdir -p /etc/docker
    sudo tee /etc/docker/daemon.json <<-'EOF'
    {
    "registry-mirrors": ["https://hnkfbj7x.mirror.aliyuncs.com"],
    "exec-opts": ["native.cgroupdriver=systemd"]
    }
		EOF
    systemctl daemon-reload
    systemctl restart docker
    systemctl enable docker
```



