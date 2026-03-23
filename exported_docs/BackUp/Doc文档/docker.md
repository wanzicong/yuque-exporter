<font style="color:#000000;"># dev 环境</font>

<font style="color:#000000;">elasticsearch.hosts: ["http://es-cn-0pp1lyas2000m69gj.elasticsearch.aliyuncs.com:9200"]</font>

<font style="color:#000000;">elasticsearch.username: "elastic"</font>

<font style="color:#000000;">elasticsearch.password: "elas88ticDevDEVM"</font>

<font style="color:#000000;">  
</font>

<font style="color:#000000;"># daily 环境</font>

<font style="color:#000000;"># elasticsearch.hosts: ["http://es-cn-4591lab380018c6ek.elasticsearch.aliyuncs.com:9200"]</font>

<font style="color:#000000;"># elasticsearch.username: "elastic"</font>

<font style="color:#000000;"># elasticsearch.password: "eSlGasM1ti3c6D8M"</font>

```json
# 网桥es -> 方便相互通讯
networks:
  es:

services:
  kibana:
    image: kibana:6.7.0       # 原镜像`kibana:7.14.1`
    container_name: kibana_dev
    restart: unless-stopped
    volumes:
      - ./config/kibana.yml:/usr/share/kibana/config/kibana.yml
    ports:
      - "5602:5601"
    networks:
      - es

```







