

```plain
ChatClient 
ChatClient.Builder
Prompt
ChatResponse
ChatOptions 
Advisor
AdvisorSpec

1. 如何创建一个ChatClient ？
A_1: 使用自动装配
public MyController(ChatClient.Builder chatClientBuilder) {
      this.chatClient = chatClientBuilder.build();
}

A_2: 使用编程的方式创建
spring.ai.chat.client.enabled=false // 核心
ChatModel myChatModel = ... // usually autowired
ChatClient.Builder builder = ChatClient.builder(this.myChatModel);
// or create a ChatClient with the default builder settings:
ChatClient chatClient = ChatClient.create(this.myChatModel);


OpenAiChatOptions
OpenAiChatModel


2 如何创建一个ChatModel？
A_1:通过starter 自动装配

A_2:通过编程的方式
var openAiApi = new OpenAiApi(System.getenv("OPENAI_API_KEY"));
var openAiChatOptions = OpenAiChatOptions.builder()
            .model("gpt-3.5-turbo")
            .temperature(0.4)
            .maxTokens(200)
            .build();
var chatModel = new OpenAiChatModel(this.openAiApi, this.openAiChatOptions);



ApiKey
OpenAiApi openAiApi = OpenAiApi.builder()
    .apiKey(customApiKey)
    .build();

// Create a chat client with the custom OpenAiApi instance
OpenAiChatClient chatClient = new OpenAiChatClient(openAiApi);

```



多种方式使用 SpringAI

使用最简单的方式-通过自动注入的方式

```java
    private final ChatClient dashScopeChatClient;

	 // 自动注入 bean ChatClient.Builder chatClientBuilder
	 public HelloworldController(ChatClient.Builder chatClientBuilder) {
        // 调用方法
	  	this.dashScopeChatClient = chatClientBuilder.build();
	 }


```



手动构建

client

```java

// usually autowired 【要么容器中有， 要么手动创建】【bean 的方式参考 不同厂商的autoconfig】
ChatModel myChatModel = ... 
ChatClient.Builder builder = ChatClient.builder(this.myChatModel);
ChatClient client = builder.build(); // 创建方式1
ChatClient chatClient = ChatClient.create(this.myChatModel); // 创建方式2 
```

model

```java
OpenAiApi openAiApi = new OpenAiApi(System.getenv("OPENAI_API_KEY")); // 创建一个api对象

OpenAiChatOptions openAiChatOptions = OpenAiChatOptions.builder()
            .model("gpt-3.5-turbo")
            .temperature(0.4)
            .maxTokens(200)
            .build(); // 创建一个 option 对象

OpenAiChatModel chatModel = new OpenAiChatModel(this.openAiApi, this.openAiChatOptions);
```



bean 对象创建 + 手动创建

```java

    // 一个平台多个model
    public MoreModelCallController( 
        @Qualifier("dashscopeChatModel") ChatModel dashScopeChatModel) {
        // 指定容器中的 chatModel
        this.dashScopeChatModel = dashScopeChatModel;
    }

    // 多个平台 多个model对象
    // 一个容器中可以存在多个 chatmode 对象
    public MorePlatformController(
            @Qualifier("dashscopeChatModel") ChatModel dashScopeChatModel,
            @Qualifier("ollamaChatModel") ChatModel OllamaChatModel,
            @Qualifier("openAiChatModel") ChatModel openAIChatModel) {
        this.dashScopeChatModel = dashScopeChatModel;
        this.ollamaChatModel = OllamaChatModel;
        this.openAIChatModel = openAIChatModel;
    }

    // 如果没有指定 model 模型 会是使用start中的默认模型
    // 使用这些chat model
    ChatOptions runtimeOptions = ChatOptions.builder().model(model).build();
    // 使用这个 model对象
    String text = dashScopeChatModel.call(new Prompt(prompt, runtimeOptions)).getResult().getOutput().getText();
    



```



```java
// 使用client 进行大模型通讯
ChatClient chatClient = ChatClient.builder(chatModel).build();

String content = chatClient.prompt("模板提示词")
				.options(DashScopeChatOptions.builder()
						.withModel(models) // 使用不同的模型
						.build()
				).call().content();


```

