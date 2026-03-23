# 依赖软件环境
资源配置: 内存 64G

## docker 
[docker-ce | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)

```sql
# 基础命令
docker run
docker ps 
docker logs 
```

## docker compose 
[linux安装docker-compose（官网教程）_linux 安装docker-compose-CSDN博客](https://blog.csdn.net/weixin_51311218/article/details/131376823)

```sql
version: '3'
services:
  activemq:
    image: webcenter/activemq                    # 镜像`webcenter/activemq`
    container_name: activemq                     # 容器名为'activemq'
    hostname: myActivemq                         # 定义主机名
    restart: unless-stopped                              # 指定容器退出后的重启策略为始终重启，但是不考虑在Docker守护进程启动时就已经停止了的容器
    #容器的映射端口
    ports:
      - 61613:61613
      - 61616:61616
      - 8161:8161
    volumes:                                    # 数据卷挂载路径设置,将本机目录映射到容器目录
      - /etc/localtime:/etc/localtime:ro
      - ./activemq/data/activemq:/data/activemq
      - ./activemq/var/log/activemq:/var/log/activemq
    environment:                                # 设置环境变量,相当于docker run命令中的-e
      TZ: Asia/Shanghai
      LANG: en_US.UTF-8
      ACTIVEMQ_ADMIN_LOGIN: admin      # 登录账号
      ACTIVEMQ_ADMIN_PASSWORD: admin   # 登录密码
      ACTIVEMQ_CONFIG_MINMEMORY: 512
      ACTIVEMQ_CONFIG_MAXMEMORY: 2048

```

## docker file 
```sql
FROM registry.cn-hangzhou.aliyuncs.com/zhengqing/openjdk:8-jdk-alpine

# 维护者信息
MAINTAINER zhengqingya

# 设置环境变量-运行时也可传参进来耍哈
ENV JAVA_OPTS ""

# 添加jar包到容器中 -- tips: xx.jar 和 Dockerfile 在同一级
ADD *.jar /home/app.jar

# 对外暴漏的端口号
# [注：EXPOSE指令只是声明容器运行时提供的服务端口，给读者看有哪些端口，在运行时只会开启程序自身的端口！！]
EXPOSE 8080

# 以exec格式的CMD指令 -- 可实现优雅停止容器服务
# "sh", "-c" : 可通过exec模式执行shell  =》 获得环境变量
CMD ["sh", "-c", "echo \"****** 运行命令：java -jar ${JAVA_OPTS} /home/app.jar\"   &   java -jar ${JAVA_OPTS} /home/app.jar"]

```





# 日志环境搭建
elfk 体系

elasticsearch 日志存储引擎【比较消耗内存，最低1G】

kibana 【ui 客户端】

<font style="color:#080808;background-color:#ffffff;">logstash 【日志清洗， 日志输入采集，日志输出】</font>

<font style="color:#080808;background-color:#ffffff;">filebeat 【日志源收集-文件】</font>



```sql
version: '3'

# 网桥 -> 方便相互通讯
networks:
  elkf:

services:
  elasticsearch:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/elasticsearch:7.14.1      # 原镜像`elasticsearch:7.14.1`
    container_name: elkf_elasticsearch         # 容器名为'elkf_elasticsearch'
    restart: unless-stopped                   # 指定容器退出后的重启策略为始终重启，但是不考虑在Docker守护进程启动时就已经停止了的容器
    volumes:                                  # 数据卷挂载路径设置,将本机目录映射到容器目录
      - "./app/elasticsearch/data:/usr/share/elasticsearch/data"
      - "./app/elasticsearch/logs:/usr/share/elasticsearch/logs"
      - "./app/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml"
#      - "./app/elasticsearch/config/jvm.options:/usr/share/elasticsearch/config/jvm.options"
    environment:                              # 设置环境变量,相当于docker run命令中的-e
      TZ: Asia/Shanghai
      LANG: en_US.UTF-8
      TAKE_FILE_OWNERSHIP: "true"  # 权限
      discovery.type: single-node
      ES_JAVA_OPTS: "-Xmx512m -Xms512m"
      ELASTIC_PASSWORD: "123456" # elastic账号密码
    ports:
      - "9200:9200"
      - "9300:9300"
    networks:
      - elkf

  kibana:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/kibana:7.14.1       # 原镜像`kibana:7.14.1`
    container_name: elkf_kibana
    restart: unless-stopped
    volumes:
      - "./app/kibana/config/kibana.yml:/usr/share/kibana/config/kibana.yml"
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
    links:
      - elasticsearch
    networks:
      - elkf

  logstash:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/logstash:7.14.1     # 原镜像`logstash:7.14.1`
    container_name: elkf_logstash
    restart: unless-stopped
    environment:
      LS_JAVA_OPTS: "-Xmx512m -Xms512m"
    volumes:
      - "./app/logstash/data:/usr/share/logstash/data"
      - "./app/logstash/config/logstash.yml:/usr/share/logstash/config/logstash.yml"
#      - "./app/logstash/config/logstash.conf:/usr/share/logstash/config/logstash.conf"
      - "./app/logstash/config/test:/usr/share/logstash/config/test"
#    command: logstash -f /usr/share/logstash/config/logstash.conf    # 指定logstash启动时使用的配置文件 - 指定单个文件
    command: logstash -f /usr/share/logstash/config/test       # 指定logstash启动时使用的配置文件 - 指定目录夹（系统会自动读取文件夹下所有配置文件，并在内存中整合）
    ports:
      - "9600:9600"
#      - "10001-10010:10001-10010"
      - "5044:5044"
    depends_on:
      - elasticsearch
    networks:
      - elkf

  filebeat:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/filebeat:7.14.1      # 原镜像`elastic/filebeat:7.14.1`
    container_name: elkf_filebeat
    restart: unless-stopped                   # 指定容器退出后的重启策略为始终重启，但是不考虑在Docker守护进程启动时就已经停止了的容器
    volumes:                                  # 数据卷挂载路径设置,将本机目录映射到容器目录
      - "./app/filebeat/filebeat.yml:/usr/share/filebeat/filebeat.yml"
      - "./app/filebeat/logs:/usr/share/filebeat/logs"
      - "./app/filebeat/my-log:/usr/share/filebeat/my-log"
    environment:          # 设置环境变量,相当于docker run命令中的-e
      TZ: Asia/Shanghai
      LANG: en_US.UTF-8
    depends_on:
      - elasticsearch
      - logstash
    networks:
      - elkf
```



# 链路追踪SkyWalking
依赖: skywalking-jar , mysql , skywalking-server



```sql
# 可参考 https://github.com/apache/skywalking/blob/master/docker/docker-compose.yml
version: '3'

# 网桥 -> 方便相互通讯
networks:
  skywalking:
    ipam:
      driver: default
      config:
        - subnet: "172.24.0.0/24"

services:
  # 应用性能分析 -- 不使用docker的话可下载 https://dlcdn.apache.org/skywalking/9.3.0/apache-skywalking-apm-9.3.0.tar.gz 进行测试
  oap:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/skywalking-oap-server:9.3.0 # 原镜像`apache/skywalking-oap-server:9.3.0`
    container_name: oap
    restart: unless-stopped
    environment:
      TZ: Asia/Shanghai
      JAVA_OPTS: "-Xmx2048M -Xms2048M"
      SW_STORAGE: mysql
      # 需等待自动创建476张表...
      SW_JDBC_URL: "jdbc:mysql://172.24.0.83:3306/skywalking?rewriteBatchedStatements=true&allowMultiQueries=true&useSSL=false"
      SW_DATA_SOURCE_USER: root
      SW_DATA_SOURCE_PASSWORD: root
    volumes:
      # 驱动获取 https://mvnrepository.com/artifact/mysql/mysql-connector-java/8.0.28
#      - "./skywalking/mysql-connector-java-8.0.28.jar:/skywalking/oap-libs/mysql-connector-java-8.0.28.jar"
      - "./skywalking/mysql-connector-java-8.0.28.jar:/skywalking/ext-libs/mysql-connector-java-8.0.28.jar"
    ports:
      - "11800:11800" # agent 上报数据的端口，这是 gRPC 端口
      - "12800:12800" # ui 读取数据的端口， 这是 http 端口
    depends_on:
      - mysql
    networks:
      skywalking:
        ipv4_address: 172.24.0.81

  # 可视化界面
  oap-ui:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/skywalking-ui:9.3.0 # 原镜像`apache/skywalking-ui:9.3.0`
    container_name: oap-ui
    restart: unless-stopped
    depends_on:
      - oap
    links:
      - oap
    ports:
      - "8888:8080"
    environment:
      SW_OAP_ADDRESS: http://172.24.0.81:12800
      TZ: Asia/Shanghai
    networks:
      skywalking:
        ipv4_address: 172.24.0.82

  # mysql存储
  mysql:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/mysql:5.7  # 原镜像`mysql:5.7`
    container_name: oap-mysql                                    # 容器名为'oap-mysql'
    restart: unless-stopped
    volumes:                                                      # 数据卷挂载路径设置,将本机目录映射到容器目录
      - "./skywalking/mysql/my.cnf:/etc/mysql/my.cnf"
      - "./skywalking/mysql/data:/var/lib/mysql"
      #      - "./skywalking/mysql/conf.d:/etc/mysql/conf.d"
      - "./skywalking/mysql/log/mysql/error.log:/var/log/mysql/error.log"
      - "./skywalking/mysql/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d" # 可执行初始化sql脚本的目录 -- tips:`/var/lib/mysql`目录下无数据的时候才会执行(即第一次启动的时候才会执行)
    environment:                        # 设置环境变量,相当于docker run命令中的-e
      TZ: Asia/Shanghai
      LANG: en_US.UTF-8
      MYSQL_ROOT_PASSWORD: root         # 设置root用户密码
      MYSQL_DATABASE: skywalking        # 初始化的数据库名称
    ports:                              # 映射端口
      - "3308:3306"
    networks:
      skywalking:
        ipv4_address: 172.24.0.83

```

 

# mysql 慢查询监控
依赖： 

mysql 配置开启慢查询

prometheus 监控信息采集

mysql-exporter mysql日志采集

grafana 监控报表展示

```sql
# 镜像版本请自行选择 https://hub.docker.com/search?q=&type=image
version: "3"

# 网桥 -> 方便相互通讯
networks:
  prometheus:
    ipam:
      driver: default
      config:
        - subnet: "172.22.0.0/24"

services:
  # 开源的系统监控和报警系统
  prometheus:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/prometheus:v2.34.0             # 原镜像`prom/prometheus:v2.34.0`
    container_name: prometheus
    restart: unless-stopped
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    command: "--config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/prometheus"
    ports:
      - "9090:9090"
    depends_on:
      - node-exporter
    networks:
      prometheus:
        ipv4_address: 172.22.0.11

  # 采集服务器层面的运行指标
  node-exporter:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/node-exporter:v1.3.1           # 原镜像`prom/node-exporter:v1.3.1`
    container_name: prometheus-node-exporter
    restart: unless-stopped
    ports:
      - "9100:9100"
    networks:
      prometheus:
        ipv4_address: 172.22.0.22

  # 用于UI展示
  # https://grafana.com/docs/grafana/latest/installation/docker
  grafana:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/grafana:8.0.0               # 原镜像`grafana/grafana:8.0.0`
    container_name: prometheus-grafana
    restart: unless-stopped
    ports:
      - "3000:3000"
    volumes:
      - "./prometheus/grafana/grafana.ini:/etc/grafana/grafana.ini" # 邮箱配置
#      - "./prometheus/grafana/grafana-storage:/var/lib/grafana"
#      - "./prometheus/grafana/public:/usr/share/grafana/public" # 这里面可处理汉化包 可参考 https://github.com/WangHL0927/grafana-chinese
#      - "./prometheus/grafana/conf:/usr/share/grafana/conf"
#      - "./prometheus/grafana/log:/var/log/grafana"
#      - "/etc/localtime:/etc/localtime"
    environment:
      GF_EXPLORE_ENABLED: "true"
      GF_SECURITY_ADMIN_PASSWORD: "admin"
      GF_INSTALL_PLUGINS: "grafana-clock-panel,grafana-simple-json-datasource,alexanderzobnin-zabbix-app"
      # 持久化到mysql数据库
      GF_DATABASE_URL: "mysql://root:root@www.zhengqingya.com:3306/grafana" # TODO 修改
    depends_on:
      - prometheus
    networks:
      prometheus:
        ipv4_address: 172.22.0.33

  # mysql数据库 => 用于grafana持久化数据
#  mysql:
#    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/mysql:5.7
#    container_name: prometheus-mysql
#    restart: unless-stopped
#    volumes:
#      - "./prometheus/mysql5.7/my.cnf:/etc/mysql/my.cnf"
#      - "./prometheus/mysql5.7/data:/var/lib/mysql"
#      - "./prometheus/mysql5.7/log/mysql/error.log:/var/log/mysql/error.log"
#    environment:
#      TZ: Asia/Shanghai
#      LANG: en_US.UTF-8
#      MYSQL_ROOT_PASSWORD: root         # 设置root用户密码
#      MYSQL_DATABASE: grafana           # 初始化数据库grafana
#    ports:
#      - "3306:3306"

```





# 代码质量监控
sonarqube

gitlab

```sql
# https://hub.docker.com/_/sonarqube
version: '3'

# 网桥elk -> 方便相互通讯
networks:
  sonarqube:

services:
  sonarqube:
    image: registry.cn-hangzhou.aliyuncs.com/zhengqing/sonarqube:6.7.1      # 原镜像`sonarqube:6.7.1`
    container_name: sonarqube
    restart: unless-stopped        # 指定容器退出后的重启策略为始终重启，但是不考虑在Docker守护进程启动时就已经停止了的容器
    volumes:
      - "./sonarqube/data:/opt/sonarqube/data"
      - "./sonarqube/logs:/opt/sonarqube/logs"
      - "./sonarqube/extensions/plugins/sonar-l10n-zh-plugin-1.19.jar:/opt/sonarqube/extensions/plugins/sonar-l10n-zh-plugin-1.19.jar"
#      - "./sonarqube/conf:/opt/sonarqube/conf"
    environment:
      SONARQUBE_JDBC_USERNAME: root
      SONARQUBE_JDBC_PASSWORD: root
      SONARQUBE_JDBC_URL: "jdbc:mysql://www.zhengqingya.com:3306/sonarqube?useUnicode=true&characterEncoding=utf8&rewriteBatchedStatements=true&useConfigs=maxPerformance"
    ports:
      - "9005:9000"
    networks:
      - sonarqube

```



# CI/CD/Docker
使用流程

1. springboot 打包生成jar包
2. 配置 docker file 文件
3. 基于docker file 生成docker 镜像
4. 上传镜像到 docker hub 制品仓库
5. 基于 配置信息 启动 docker 容器



Docker FIle 演示

```plain
# jre基础环境
FROM openjdk:8-jre-alpine

# 维护者信息
MAINTAINER zhengqingya

# 添加jar包到容器中 -- tips: app.jar 和 Dockerfile 在同一级
ADD app.jar /home/

# 对外暴漏的端口号
# [注：EXPOSE指令只是声明容器运行时提供的服务端口，给读者看有哪些端口，在运行时只会开启程序自身的端口！！]
EXPOSE 8080

# RUN🏃🏃
CMD nohup java -jar /home/app.jar >> /home/app.log 2>&1 & \
    echo "****** 查看日志..." & \
    tail -f /home/app.log
```





```plain
# 拉取nginx基础镜像
FROM nginx:1.21.1

# 维护者信息
MAINTAINER zhengqingya

# 将dist文件中的内容复制到 `/usr/share/nginx/html/` 这个目录下面
COPY dist/  /usr/share/nginx/html/
# 用本地配置文件来替换nginx镜像里的默认配置
COPY Docker/nginx/nginx.conf /etc/nginx/nginx.conf

# 对外暴漏的端口号
# [注：EXPOSE指令只是声明容器运行时提供的服务端口，给读者看有哪些端口，在运行时只会开启程序自身的端口！！]
EXPOSE 80

# 启动nginx容器
CMD ["nginx", "-g", "daemon off;"]
```



基于docker 使用流程

```shell
# 构建镜像
# -f：指定Dockerfile文件路径
# -t：镜像命名
# --no-cache：构建镜像时不使用缓存
# 最后有一个点 “.”：当构建的时候，由用户指定构建镜像的上下文环境路径，然后将此路径下的所有文件打包上传给Docker引擎，引擎内将这些内容展开后，就能获取到所有指定上下文中的文件了。
# ex: Dockerfile中`COPY dist/  /usr/share/nginx/html/` => 其实拷贝的并不是本机目录下的dist文件内容，而是Docker引擎中展开的构建上下文中的文件
docker build -f ./Docker/Dockerfile -t "registry.cn-hangzhou.aliyuncs.com/zhengqing/small-tools-web:prod" . --no-cache

# 推送镜像
docker push registry.cn-hangzhou.aliyuncs.com/zhengqing/small-tools-web:prod

# 拉取镜像
registry.cn-hangzhou.aliyuncs.com/zhengqing/small-tools-web:prod

# 运行
docker run -d --name small-tools-web -p 80:80 --restart=always registry.cn-hangzhou.aliyuncs.com/zhengqing/small-tools-web:prod

# 删除旧容器
docker ps -a | grep small-tools-web | grep prod | awk '{print $1}' | xargs -i docker stop {} | xargs -I docker rm {}

# 删除旧镜像
docker images | grep -E small-tools-web | grep prod | awk '{print $3}' | uniq | xargs -I {} docker rmi --force {}
```



