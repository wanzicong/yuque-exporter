

框架 springcloud stream 接入 rabbitmq + tonghtp



本地 jar 包安装 （看群）

```plain


mvn install:install-file -DgroupId=com.tongtech.client -DartifactId=tongtech-client -Dversion=2.0.2.2  -Dfile=（jar包地址）htpclient-2.0.2.2.jar -Dpackaging=jar
mvn install:install-file -DgroupId=com.tongtech.cloud -DartifactId=htp-spring-cloud-starter-stream -Dversion=2.0.2.2 -Dfile=（jar包地址） htp-spring-cloud-starter-stream-2.0.2.2.jar -Dpackaging=jar


```

1. 引入配置

```plain

        <dependency>
            <groupId>com.tongtech.cloud</groupId>
            <artifactId>htp-spring-cloud-starter-stream</artifactId>
            <version>2.0.2.2</version>
        </dependency>

        <dependency>
            <groupId>com.tongtech.client</groupId>
            <artifactId>tongtech-client</artifactId>
            <version>2.0.2.2</version>
        </dependency>


        <!-- Spring Cloud Stream -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-stream-rabbit</artifactId>
        </dependency>




```





2. 配置文件

```plain
server:
  port: 8080
spring:
  rabbitmq:
    host: 10.100.21.61
    port: 5672
    username: zlmq
    password: zhiling888mq
    virtual-host: /
  cloud:
    function:
      definition: clusterMessage0
    stream:
      default-binder: htp #默认binder名称，此处为htp
      bindings:
        producerMessage-out-0:
          destination: topic22
        clusterMessage0-in-0:
          destination: topic22
      htp:
        binder:
          name-server: tcp://10.17.7.171:9888 #NameServer地址,多个地址用,分隔
          namespace: ns1 #命名空间
          cluster: defaultCluster #集群名称
          enabled: true #是否启用binder
          heartbeat-broker-interval: 45000 #客户端与broker心跳间隔时间,单位为毫秒
        bindings:
          clusterMessage0-in-0:
            consumer:
              group: consumer1  #消费者组名称
              messageModel: CLUSTERING  #消息模型定: CLUSTERING-集群, BROADCASTING--广播
              #              subscription: tag1 || tag2 #订阅的标签,多个用||分隔,模糊匹配:tag1.*,支持*:一个单词; #:0个或多个单词,以.为层级符,与topic模糊匹配规则相同
              pullTimeDelayMillsWhenException: 1000 #消费异常时，下一次拉取时间延迟毫秒数
              consumeFromWhere: LocalOffset #重启时消费开始位置.(LocalOffset-从本地读取offset; RemoteOffset-从Broker读取offset，即从最新消息消费)
              pullBatchSize: 1  #一次拉取多少条消息
              maxCachedMessageCount: 1000 #最大缓存的消息数量,[1, 65535]
              maxCachedBufferSize: 50 #最大缓存的消息大小，单位为MB,[1, 1024]
              concurrentlyMaxSpan: 2000 #无序并发消费最大跨度偏移量
              suspendTime: 1000 #对于需要缓慢拉动的情况，暂停拉动时间，如流量控制场景
              persistConsumerOffsetInterval: 5000 #持久化消费者偏移量间隔时间，单位为毫秒
              allowCreateTopicDelayed: true #是否支持模糊匹配延时创建主题
              initialDelay: 2000 #设置重平衡初始延迟时间,单位为毫秒
              pullType: PullContinue #拉取类型,(PullLatest-拉取最新消息; PullContinue-使用服务端的消费历史记录; PullOffset-使用客户端传递的offset获取消息(也可以回溯消息);PullEndContinue--3与-1都使用历史记录，拉取消费偏移顺序递增 ；不同之处是首次消费偏移位置不同，-3是末尾，-1的首次消费偏移是0.)
              rebalanceStrategy: ShareCircle  #消费者负载均衡策略(ExclusiveCircle:独占轮询 一个broker只能有一个消费者,ShareCircle:共享轮询,ShareAll:共享全连模式)
              push:
                orderly: true #如果 orderly 为 true，则使用 {@link MessageListenerOrderly} 否则， 如果 orderly 为 false，则使用 {@link MessageListenerConcurrently}.
                suspendCurrentQueueTimeMillis: -1 #重新提交消费间隔时间
                maxReconsumeTimes: 2 #当消费者顺序消费消息失败后，消息队列 会自动不断地进行消息重试
                delayLevel: 0 #延迟级别,默认为0
                pullInterval: 0 #两次拉取之间的间隔时间
                longPollingTime: 2000 #响应no_msg，拉取长轮询时间，单位为毫秒
                updateSubscriptionInterval: 30000 #更新订阅主题（管理节点）默认30秒，单位毫秒

          producerMessage-out-0:
            producer:
              group: producer1 #生产者组名称
              sendMsgTimeout: 30000 #消息发送超时时间，单位为毫秒
              retryTimesWhenSendFailed: 2 #消息发送失败重试次数
              maxMessageSize: 4194304 #最大消息大小，单位为字节,默认4MB
              sendType: Sync #同步--Sync,单向--OneWay,单向--selectBroker
              #              brokerName: bro1 #当sendType为selectBroker时，需要配置brokerName
              selectStrategy: POLLING #轮询--POLLING,hash取模--HASH,随机--RANDOM
      rabbit:
        bindings:
          producerMessage-out-0:
            producer:
              auto-bind-dlq: true
          clusterMessage0-in-0:
            consumer:
              durableSubscription: true


```







3. 发送消息

```plain
package org.example.mqstream.demos.htp;


import com.alibaba.fastjson.JSONObject;
import com.tongtech.cloud.stream.binder.htp.constant.TongHTPConst;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.stream.function.StreamBridge;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.GenericMessage;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.stream.Collectors;

/**
 * @author tongtech
 */
@RestController
@RequestMapping("/htpStream")
public class TongHTPTestController {
    private final String outputChannelName = "producerMessage-out-0";
    private final StreamBridge streamBridge;


    @Autowired
    public TongHTPTestController(StreamBridge streamBridge) {
        this.streamBridge = streamBridge;
    }

    @RequestMapping("/testSend")
    public void testSend() {
        Map<String, Object> headers = new HashMap<>();
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("msg","test");
        headers.put(TongHTPConst.PROPERTY_KEYS,"keys");
        Message<JSONObject> message = new GenericMessage<>(jsonObject, headers);
        streamBridge.send(outputChannelName, message);
    }

    @RequestMapping("/testPerf")
    public void testPerf() {
        long startTime = System.currentTimeMillis();
        System.out.println("发送消息开始时间：" + startTime);

        String alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        for (int i = 0; i < 1000000; i++) {
            String content = new Random().ints(1024, 0, alpha.length())
                    .mapToObj(alpha::charAt)
                    .map(Object::toString)
                    .collect(Collectors.joining());
            JSONObject jsonObject = new JSONObject();
            jsonObject.put("msg",content);
            Map<String, Object> headers = new HashMap<>();
            Message<JSONObject> message = new GenericMessage<>(jsonObject, headers);
            streamBridge.send(outputChannelName, message);
            if (i % 100000 == 0) {
                long end10 = System.currentTimeMillis();
                System.out.println("已发送消息数: " + i+"   时间:"+(end10-startTime));
            }
        }
        long endTime = System.currentTimeMillis();
        System.out.println("发送消息结束时间：" + endTime);
        System.out.println("耗时：" + (endTime - startTime) + " ms");
    }

}

```



4. 消费消息

```plain
package org.example.mqstream.demos.htp;


import org.springframework.context.annotation.Bean;
import org.springframework.messaging.Message;
import org.springframework.messaging.MessageHeaders;
import org.springframework.stereotype.Component;

import java.util.function.Consumer;

@Component
public class TestSpringCloudStreamHtpApplication {

    @Bean
    public Consumer<Message<String>> clusterMessage0() {
        return (msg) -> {
//            String str = new String(msg.getPayload(), StandardCharsets.UTF_8);
            String payload = msg.getPayload();
            System.out.println(Thread.currentThread().getName() + " Consumer0 Receive New Messages: " + payload);
            MessageHeaders headers = msg.getHeaders();
            System.out.println("headers:");
            // 使用 forEach 遍历
            headers.forEach((key, value) -> {
                System.out.println("Key: " + key + ", Value: " + value);
            });
        };
    }

}

```

