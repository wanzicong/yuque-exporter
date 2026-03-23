资源参考: 

[09-SpringBoot面试题.pdf](https://www.yuque.com/attachments/yuque/0/2024/pdf/21382055/1722255522499-8bae1b0d-acd5-4308-9447-ca1ca4404728.pdf)



[Spring面试题，39道Spring八股文（1.3万字63张手绘图），面渣逆袭必看👍 | 二哥的Java进阶之路 (javabetter.cn)](https://javabetter.cn/sidebar/sanfene/spring.html#spring-boot)



SpringBoot 有哪些优点

SpringBoot 自动装配原理

SpringBoot 启动原理了解吗

SpringBoot Starter 如何自己实现一个

SpringBoot 和 Spring有什么区别

SpringBoot 和 SpringMvc 有什么区别



spring boot 在实际面试中可问的点不多，因为springboot 本身是一个脚手架框架， 在实际开发中可以省去很多没有必要的配置。

spring boot 提供自动装配的能力， 底层依赖的还是spring 的核心功能， 相当于对spring 的核心功能提供了一层自动化的封装

spring 是整个spring 全家桶的基石，spring boot是在spring的基础上做的扩展和延伸



回答问题最好带上一些关键的类 和 方法

核心点: EnableAutoConfiguration  @Import 注解  Selector 类， spring.factory 配置文件

SpringFactoryLoader 类 加载spring.factory 文件



## 谈谈你对SpringBoot 自动装配理解？
背景了解: 

springboot 初始化: 

解析类路径下面的 spring.factory 文件

设置初始化器， 设置监听器

通过事件多播器进行广播 

通过发布事件的发布进行 具体的操作， 包含容器的启动 bean 信息的加载 ioc 容器的启动， bean 生命周期的管理，扩展点的执行

spring boot 用了很多监听器， 设置了很多模板， 通过事件发布和事件监听的方式进行逻辑的解耦和灵活管理



解析spring boot 主类， 进行beandefination 的扫描 ，里面包含了很多自动装配的类配置类信息， 里面通过 @componentScan @Config  和 @Bean 的方式 将bean 信息加载进ioc 容器中

其中使用到了 BeanFactoryPostProcessor  和 BeanPostProcessor ， 解析具体的beandefination 使用到的是具体的beandefinitionregistrypostprocessor

最终会调用到 spring 核心方法 refresh 方法 进行 容器的启动 和 管理



具体回答： 

<font style="color:rgb(51, 51, 51);">BFPP：BeanFactoryPostProcessor</font>

<font style="color:rgb(51, 51, 51);">BPP：BeanPostProcessor</font>

<font style="color:rgb(51, 51, 51);">BDRPP:BeanDefinitionRegistryPostProcessor</font>

<font style="color:rgb(51, 51, 51);">表达的总体思路是：总-分-总</font>

<font style="color:rgb(51, 51, 51);">1、springboot自动装配是什么，解决了什么问题</font>

因为springboot 本身是一个脚手架框架， 在实际开发中可以省去很多没有必要的配置。<font style="color:rgb(51, 51, 51);">spring boot 提供自动装配的能力， 底层依赖的还是spring 的核心功能，</font>

<font style="color:rgb(51, 51, 51);">2、自动装配实现的原理：</font>

<font style="color:rgb(51, 51, 51);">1、当启动springboot应用程序的时候， 会先创建SpringApplication的对象，在对象的构造方法中会进行某些参数的初始化工作，最主要的是判断当前应用程序的类型以及初始化器和监听器，在这个过程中会加载整个应用程序中的spring.factories文件，将文件的内容放到缓存对象中，方便后续获取。</font>

<font style="color:rgb(51, 51, 51);">2、SpringApplication对象创建完成之后，开始执行run方法，来完成整个启动，启动过程中最主要的有两个方法，第一个叫做prepareContext，第二个叫做refreshContext,在这两个关键步骤中完整了自动装配的核心功能，前面的处理逻辑包含了上下文对象的创建，banner的打印，异常报告期的准备等各个准备工作，方便后续来进行调用。</font>

<font style="color:rgb(51, 51, 51);">3、在prepareContext方法中主要完成的是对上下文对象的初始化操作，包括了属性值的设置，比如环境对象，在整个过程中有一个非常重要的方法，叫做load，load主要完成一件事，将当前启动类做为一个beanDefinition注册到registry中，方便后续在进行BeanFactoryPostProcessor调用执行的时候，找到对应的主类，来完成@SpringBootApplicaiton,@EnableAutoConfiguration等注解的解析工作</font>

<font style="color:rgb(51, 51, 51);">4、在refreshContext方法中会进行整个容器刷新过程，会调用中spring中的refresh方法，refresh中有13个非常关键的方法，来完成整个spring应用程序的启动，在自动装配过程中，会调用invokeBeanFactoryPostProcessor方法，在此方法中主要是对ConfigurationClassPostProcessor类的处理，这次是BFPP的子类也是BDRPP的子类，在调用的时候会先调用BDRPP中的postProcessBeanDefinitionRegistry方法，然后调用postProcessBeanFactory方法，在执行postProcessBeanDefinitionRegistry的时候回解析处理各种注解，包含@PropertySource,@ComponentScan,@ComponentScans，@Bean,@Import等注解，最主要的是@Import注解的解析</font>

<font style="color:rgb(51, 51, 51);">5、在解析@Import注解的时候，会有一个getImports的方法，从主类开始递归解析注解，把所有包含@Import的注解都解析到，然后在processImport方法中对Import的类进行分类，此处主要识别的时候AutoConfigurationImportSelect归属于ImportSelect的子类，在后续过程中会调用deferredImportSelectorHandler中的process方法，来完整EnableAutoConfiguration的加载。</font>

<font style="color:rgb(51, 51, 51);">6、上面是我对springboot自动装配的简单理解，面试官您看一下，我回答有没有问题，帮我指点一下！</font>









<font style="color:rgb(6, 6, 7);">这位面试官提供的回答基本上涵盖了Spring Boot自动装配的核心概念和实现原理，以下是一些补充和澄清：</font>

1. **<font style="color:rgb(6, 6, 7);">自动装配的目的</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">Spring Boot的自动装配旨在简化Spring应用的配置。通过自动装配，开发者可以减少显式的配置代码，使得应用更加简洁和易于维护。</font>
2. **<font style="color:rgb(6, 6, 7);">自动装配的实现原理</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">回答中提到了Spring Boot启动时会加载</font>`spring.factories`<font style="color:rgb(6, 6, 7);">文件，这是正确的。</font>`spring.factories`<font style="color:rgb(6, 6, 7);">文件通常包含自动配置类和监听器的配置，这些配置会被Spring Boot在启动时加载和处理。</font>
3. **<font style="color:rgb(6, 6, 7);">BeanFactoryPostProcessor和BeanDefinitionRegistryPostProcessor的作用</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">回答中提到了</font>`BeanFactoryPostProcessor`<font style="color:rgb(6, 6, 7);">和</font>`BeanDefinitionRegistryPostProcessor`<font style="color:rgb(6, 6, 7);">在自动装配中的作用。</font>`BeanFactoryPostProcessor`<font style="color:rgb(6, 6, 7);">允许在Bean实例化之前修改Bean的定义，而</font>`BeanDefinitionRegistryPostProcessor`<font style="color:rgb(6, 6, 7);">则允许在Bean定义注册到容器之前进行修改。</font>
4. **<font style="color:rgb(6, 6, 7);">@EnableAutoConfiguration的作用</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - `@EnableAutoConfiguration`<font style="color:rgb(6, 6, 7);">是一个关键的注解，它告诉Spring Boot根据应用所依赖的库和类路径下的</font>`spring.factories`<font style="color:rgb(6, 6, 7);">文件自动配置Bean。这是自动装配的核心机制之一。</font>
5. **<font style="color:rgb(6, 6, 7);">@Import注解的处理</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">回答中提到了</font>`@Import`<font style="color:rgb(6, 6, 7);">注解的处理，这是正确的。</font>`@Import`<font style="color:rgb(6, 6, 7);">注解可以导入其他配置类，Spring Boot会递归解析这些注解，从而加载更多的自动配置类。</font>
6. **<font style="color:rgb(6, 6, 7);">自动配置的加载过程</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">回答中提到了</font>`deferredImportSelectorHandler`<font style="color:rgb(6, 6, 7);">和</font>`processImport`<font style="color:rgb(6, 6, 7);">方法，这些是处理自动配置导入选择器的关键步骤。Spring Boot会根据条件判断哪些自动配置类应该被加载。</font>
7. **<font style="color:rgb(6, 6, 7);">总结</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">回答中对Spring Boot自动装配的描述较为详细，涵盖了从启动到自动配置加载的整个流程。不过，可以进一步强调自动装配是如何根据应用的依赖和环境自动选择配置的，以及如何通过</font>`application.properties`<font style="color:rgb(6, 6, 7);">或</font>`application.yml`<font style="color:rgb(6, 6, 7);">文件来覆盖自动配置的默认行为。</font>

<font style="color:rgb(6, 6, 7);">总的来说，这位面试官的回答是相当全面和准确的，涵盖了Spring Boot自动装配的主要方面。如果需要进一步的深入讨论，可以探讨一些具体的自动配置类是如何实现的，以及它们是如何与Spring Boot的启动流程和事件监听机制相互作用的。</font>



## 你觉得springboot 作为一个成熟的产品， 他有哪些优势，谈谈你的理解？
Spring Boot是一个开源的Java框架，用于创建独立、生产级的基于Spring框架的应用程序。它简化了基于Spring的应用开发，提供了快速启动和运行Spring项目的能力。以下是Spring Boot的一些主要优势：

1. **简化配置**：
    - Spring Boot提供了大量的自动配置，减少了传统Spring应用中需要的XML和Java配置代码。
1. **独立运行**：
    - Spring Boot应用包含内嵌的HTTP服务器（如Tomcat、Jetty或Undertow），可以打包成一个独立的JAR文件，通过简单的`java -jar`命令运行。
1. **社区和插件生态**：
    - Spring Boot拥有一个活跃的社区和丰富的插件生态，提供了大量的Starters，使得添加新功能变得非常容易。
1. **微服务支持**：
    - Spring Boot非常适合微服务架构，它与Spring Cloud等项目紧密集成，简化了分布式系统的开发。
1. **监控和管理**：
    - 内置了多种监控和管理功能，如健康检查、度量信息收集等，这些功能可以通过actuator模块轻松访问。
1. **无需XML配置**：
    - 虽然Spring Boot支持XML配置，但它鼓励使用基于Java的配置，这使得配置更加简洁和易于理解。
1. **自动装配**：
    - Spring Boot的自动装配功能可以自动配置应用程序的大部分需求，减少了样板代码。
1. **快速开发**：
    - 开发者可以快速搭建项目骨架，通过Spring Initializr快速生成项目结构。
1. **兼容性**：
    - Spring Boot与Spring框架的其他部分以及第三方库高度兼容。
1. **安全性**：
    - 提供了对安全性的内置支持，例如Spring Security的自动配置。
1. **性能优化**：
    - 通过内嵌的服务器和优化的类加载机制，Spring Boot应用通常具有较好的性能。
1. **易于部署**：
    - 由于应用是独立的，部署变得非常简单，可以很容易地在多种环境中运行。
1. **环境无关性**：
    - Spring Boot应用不依赖于特定的外部XML配置或库，这使得它们更加灵活和可移植。
1. **配置外部化**：
    - 支持配置外部化，可以很容易地根据不同环境调整配置。
1. **RESTful服务开发**：
    - 通过Spring MVC和Spring WebFlux，Spring Boot简化了RESTful服务的开发。

Spring Boot的这些优势使其成为现代Java企业应用开发的一个非常受欢迎的选择，尤其适合快速开发和微服务架构。

























