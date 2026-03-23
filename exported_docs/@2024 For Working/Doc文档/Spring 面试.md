参考资料: 

[Spring面试题.pdf](https://www.yuque.com/attachments/yuque/0/2024/pdf/21382055/1722234469639-2d4a2f67-b404-49f3-bb5c-933f4a970ca0.pdf)



```plain
谈谈你对SpringIOC的理解，原理和实现两方面
谈谈你对Spring底层实现原理的理解
谈谈你对Spring中Bean对象生命周期的理解
谈谈你对Spring中解决循环依赖的理解
谈谈你对Spring中三级缓存和二级缓存的理解
谈谈你对Bean Factory和FactoryBean的理解
Spring中用到了哪些设计模式?
谈谈你对Spring中AOP的理解
谈谈你对Spring中事务这块的理解
具体谈谈你对Spring中事务传播行为的理解


核心点: 容器，IOC，控制翻转，bean的生命周期，依赖注入，扩展点，设计模式，事务传播属性



```



## 谈谈你对spring 容器的理解，如果让你设计一个容器你会如何设计？
<font style="color:rgb(6, 6, 7);">Spring 容器是Spring框架的核心组件之一，它负责管理应用中的各种对象，包括它们的创建、配置、初始化、销毁等生命周期管理。Spring 容器主要有两种类型：BeanFactory和ApplicationContext。</font>

1. **<font style="color:rgb(6, 6, 7);">BeanFactory</font>**<font style="color:rgb(6, 6, 7);">：它是最基本的Spring容器，提供了基本的依赖注入功能。BeanFactory是单例的，并且不支持懒加载，也就是说，所有的bean在容器启动时都会创建。</font>
2. **<font style="color:rgb(6, 6, 7);">ApplicationContext</font>**<font style="color:rgb(6, 6, 7);">：是BeanFactory的扩展，提供了更多的高级功能，如事件发布、国际化支持、资源访问等。ApplicationContext支持懒加载，即bean只有在需要时才会被创建。</font>

### <font style="color:rgb(6, 6, 7);">设计一个容器的考虑因素：</font>
1. **<font style="color:rgb(6, 6, 7);">依赖注入（DI）</font>**<font style="color:rgb(6, 6, 7);">：容器需要能够管理组件之间的依赖关系，自动注入所需的依赖。</font>
2. **<font style="color:rgb(6, 6, 7);">生命周期管理</font>**<font style="color:rgb(6, 6, 7);">：容器需要能够控制组件的创建、初始化、使用和销毁过程。</font>
3. **<font style="color:rgb(6, 6, 7);">配置方式</font>**<font style="color:rgb(6, 6, 7);">：提供灵活的配置方式，如XML、注解、Java配置等。</font>
4. **<font style="color:rgb(6, 6, 7);">扩展性</font>**<font style="color:rgb(6, 6, 7);">：容器设计应支持扩展，允许用户添加自定义的扩展点。</font>
5. **<font style="color:rgb(6, 6, 7);">性能</font>**<font style="color:rgb(6, 6, 7);">：容器的设计应考虑性能，避免不必要的资源消耗。</font>
6. **<font style="color:rgb(6, 6, 7);">线程安全</font>**<font style="color:rgb(6, 6, 7);">：在多线程环境下，容器需要保证线程安全。</font>
7. **<font style="color:rgb(6, 6, 7);">事件机制</font>**<font style="color:rgb(6, 6, 7);">：提供事件发布和监听机制，允许组件之间进行交互。</font>
8. **<font style="color:rgb(6, 6, 7);">资源管理</font>**<font style="color:rgb(6, 6, 7);">：容器应能够管理资源，如数据库连接、文件等。</font>
9. **<font style="color:rgb(6, 6, 7);">国际化</font>**<font style="color:rgb(6, 6, 7);">：支持国际化，能够根据不同的语言环境提供不同的资源。</font>
10. **<font style="color:rgb(6, 6, 7);">安全性</font>**<font style="color:rgb(6, 6, 7);">：容器设计应考虑到安全性，防止潜在的安全问题。</font>

### <font style="color:rgb(6, 6, 7);">设计步骤：</font>
1. **<font style="color:rgb(6, 6, 7);">定义组件模型</font>**<font style="color:rgb(6, 6, 7);">：确定组件的属性、方法和生命周期。</font>
2. **<font style="color:rgb(6, 6, 7);">实现依赖注入</font>**<font style="color:rgb(6, 6, 7);">：设计依赖注入机制，包括自动注入和手动注入。</font>
3. **<font style="color:rgb(6, 6, 7);">配置解析</font>**<font style="color:rgb(6, 6, 7);">：实现配置文件的解析，支持多种配置方式。</font>
4. **<font style="color:rgb(6, 6, 7);">生命周期管理</font>**<font style="color:rgb(6, 6, 7);">：实现组件的创建、初始化、销毁等生命周期管理。</font>
5. **<font style="color:rgb(6, 6, 7);">扩展机制</font>**<font style="color:rgb(6, 6, 7);">：设计扩展点，允许用户添加自定义的扩展。</font>
6. **<font style="color:rgb(6, 6, 7);">实现事件机制</font>**<font style="color:rgb(6, 6, 7);">：设计事件发布和监听机制。</font>
7. **<font style="color:rgb(6, 6, 7);">资源管理</font>**<font style="color:rgb(6, 6, 7);">：实现资源的获取、使用和释放。</font>
8. **<font style="color:rgb(6, 6, 7);">国际化支持</font>**<font style="color:rgb(6, 6, 7);">：实现根据语言环境加载不同资源的功能。</font>
9. **<font style="color:rgb(6, 6, 7);">线程安全</font>**<font style="color:rgb(6, 6, 7);">：确保容器在多线程环境下的线程安全。</font>
10. **<font style="color:rgb(6, 6, 7);">安全性考虑</font>**<font style="color:rgb(6, 6, 7);">：设计安全机制，防止安全漏洞。</font>
11. **<font style="color:rgb(6, 6, 7);">性能优化</font>**<font style="color:rgb(6, 6, 7);">：优化容器的性能，减少资源消耗。</font>
12. **<font style="color:rgb(6, 6, 7);">测试和验证</font>**<font style="color:rgb(6, 6, 7);">：对容器的各个部分进行测试，确保其正确性和稳定性。</font>

<font style="color:rgb(6, 6, 7);">设计一个容器是一个复杂的过程，需要考虑多方面的因素，以确保容器的灵活性、可扩展性和稳定性。</font>

##  Spring 容器启动核心流程都有那些？
<font style="color:rgb(6, 6, 7);">Spring 容器的启动流程是Spring框架初始化和运行的基础。以下是Spring容器启动的核心流程：</font>

**<font style="color:rgb(6, 6, 7);">总:</font>**

初始化容器，

加载配置，

资源定位并解析Bean 定义信息，

BeanFactory初始化，

ApplicationContext初始化，



事件发布，

注册和初始化回调，

注册和调用bean生命周期回调，

注册和调用销毁回调，

容器就绪，bean的懒加载，





<font style="color:rgb(6, 6, 7);"></font>

1. **<font style="color:rgb(6, 6, 7);">初始化Spring容器</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">创建Spring容器的实例，如</font>`ClassPathXmlApplicationContext`<font style="color:rgb(6, 6, 7);">或</font>`AnnotationConfigApplicationContext`<font style="color:rgb(6, 6, 7);">等。</font>
2. **<font style="color:rgb(6, 6, 7);">加载配置</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">根据指定的配置文件（XML或注解）加载配置信息。对于XML配置，容器会解析XML文件；对于注解配置，容器会扫描指定的包或类路径。</font>
3. **<font style="color:rgb(6, 6, 7);">注册Bean定义</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">将解析得到的Bean定义信息注册到容器中，形成一个Bean定义的注册表。</font>
4. **<font style="color:rgb(6, 6, 7);">BeanFactory的初始化</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">如果使用的是</font>`BeanFactory`<font style="color:rgb(6, 6, 7);">，容器会初始化所有非懒加载的单例Bean。</font>
5. **<font style="color:rgb(6, 6, 7);">ApplicationContext的初始化</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">如果使用的是</font>`ApplicationContext`<font style="color:rgb(6, 6, 7);">，它除了执行BeanFactory的初始化外，还会执行以下步骤：</font>
        * <font style="color:rgb(6, 6, 7);">调用所有Bean的</font>`BeanNameAware`<font style="color:rgb(6, 6, 7);">、</font>`BeanClassLoaderAware`<font style="color:rgb(6, 6, 7);">、</font>`BeanFactoryAware`<font style="color:rgb(6, 6, 7);">等接口的方法。</font>
        * <font style="color:rgb(6, 6, 7);">调用</font>`BeanPostProcessor`<font style="color:rgb(6, 6, 7);">的</font>`postProcessBeforeInitialization`<font style="color:rgb(6, 6, 7);">方法。</font>
        * <font style="color:rgb(6, 6, 7);">调用Bean的初始化方法（如</font>`init-method`<font style="color:rgb(6, 6, 7);">指定的方法）。</font>
        * <font style="color:rgb(6, 6, 7);">调用</font>`BeanPostProcessor`<font style="color:rgb(6, 6, 7);">的</font>`postProcessAfterInitialization`<font style="color:rgb(6, 6, 7);">方法。</font>
6. **<font style="color:rgb(6, 6, 7);">事件发布</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">容器初始化完成后，可能会发布一些事件，如</font>`ContextRefreshedEvent`<font style="color:rgb(6, 6, 7);">。</font>
7. **<font style="color:rgb(6, 6, 7);">注册和调用初始化回调</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">对所有实现了</font>`InitializingBean`<font style="color:rgb(6, 6, 7);">接口的Bean调用</font>`afterPropertiesSet`<font style="color:rgb(6, 6, 7);">方法。</font>
8. **<font style="color:rgb(6, 6, 7);">注册和调用生命周期回调</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">如果Bean定义中指定了</font>`init-method`<font style="color:rgb(6, 6, 7);">，容器会调用该方法。</font>
9. **<font style="color:rgb(6, 6, 7);">注册和调用销毁回调</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">容器在关闭时，会注册和调用Bean的销毁回调，如</font>`DisposableBean`<font style="color:rgb(6, 6, 7);">接口的</font>`destroy`<font style="color:rgb(6, 6, 7);">方法或指定的</font>`destroy-method`<font style="color:rgb(6, 6, 7);">。</font>
10. **<font style="color:rgb(6, 6, 7);">容器就绪</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">完成以上步骤后，Spring容器就完全启动并准备好提供服务了。</font>
11. **<font style="color:rgb(6, 6, 7);">懒加载Bean的创建</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">对于设置了懒加载的Bean，在首次请求时才会被创建和初始化。</font>

<font style="color:rgb(6, 6, 7);">这个流程确保了Spring容器能够正确地加载配置、创建和管理Bean，并且提供了足够的扩展点，如BeanPostProcessor和BeanFactoryPostProcessor，允许开发者自定义容器的行为。</font>





## Spring 加载Java对象到容器中的方式有哪些？
1. **<font style="color:rgb(6, 6, 7);">基于XML的配置</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">使用XML文件定义Bean，通过</font>`<bean>`<font style="color:rgb(6, 6, 7);">标签声明Bean的类、属性、依赖等。</font>
2. **<font style="color:rgb(6, 6, 7);">注解</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">使用Spring的注解来标注Java类和方法，例如</font>`@Component`<font style="color:rgb(6, 6, 7);">,</font><font style="color:rgb(6, 6, 7);"> </font>`@Service`<font style="color:rgb(6, 6, 7);">,</font><font style="color:rgb(6, 6, 7);"> </font>`@Repository`<font style="color:rgb(6, 6, 7);">,</font><font style="color:rgb(6, 6, 7);"> </font>`@Controller`<font style="color:rgb(6, 6, 7);">等，来声明一个类为Spring管理的Bean。</font>
    - <font style="color:rgb(6, 6, 7);">使用</font>`@Autowired`<font style="color:rgb(6, 6, 7);">注解自动注入依赖。</font>
3. **<font style="color:rgb(6, 6, 7);">Java配置类</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">使用</font>`@Configuration`<font style="color:rgb(6, 6, 7);">注解的类来定义Bean，通过</font>`@Bean`<font style="color:rgb(6, 6, 7);">注解的方法来声明Bean。</font>
4. **<font style="color:rgb(6, 6, 7);">组件扫描</font>**<font style="color:rgb(6, 6, 7);">（Component Scanning）：</font>
    - <font style="color:rgb(6, 6, 7);">通过</font>`@ComponentScan`<font style="color:rgb(6, 6, 7);">注解指定要扫描的包，Spring会自动扫描这些包下标记了</font>`@Component`<font style="color:rgb(6, 6, 7);">或其派生注解的类，并注册为Bean。</font>
5. **<font style="color:rgb(6, 6, 7);">自动装配</font>**<font style="color:rgb(6, 6, 7);">（Autowiring）：</font>
    - <font style="color:rgb(6, 6, 7);">通过</font>`@Autowired`<font style="color:rgb(6, 6, 7);">,</font><font style="color:rgb(6, 6, 7);"> </font>`@Inject`<font style="color:rgb(6, 6, 7);">等注解自动装配Bean的依赖。</font>
6. **<font style="color:rgb(6, 6, 7);">Java配置的自动装配</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">在Java配置类中，使用</font>`@Autowired`<font style="color:rgb(6, 6, 7);">注解自动装配其他Bean作为配置类的依赖。</font>
7. **<font style="color:rgb(6, 6, 7);">使用</font>**`**@Bean**`**<font style="color:rgb(6, 6, 7);">注解的方法参数</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">在配置类中，</font>`@Bean`<font style="color:rgb(6, 6, 7);">注解的方法可以有参数，Spring容器会自动解析这些参数，实现依赖注入。</font>
8. **<font style="color:rgb(6, 6, 7);">FactoryBean</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">实现</font>`FactoryBean`<font style="color:rgb(6, 6, 7);">接口的类可以自定义Bean的创建过程，Spring容器会调用</font>`FactoryBean`<font style="color:rgb(6, 6, 7);">的</font>`getObject()`<font style="color:rgb(6, 6, 7);">方法来获取Bean实例。</font>
9. `**@Import**`**<font style="color:rgb(6, 6, 7);">注解</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">使用</font>`@Import`<font style="color:rgb(6, 6, 7);">注解来导入其他配置类，合并多个配置类中的Bean定义。</font>
10. `**@Profile**`**<font style="color:rgb(6, 6, 7);">注解</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">使用</font>`@Profile`<font style="color:rgb(6, 6, 7);">注解来根据环境条件控制Bean的创建。</font>
11. `**@DependsOn**`**<font style="color:rgb(6, 6, 7);">注解</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">使用</font>`@DependsOn`<font style="color:rgb(6, 6, 7);">注解来指定Bean初始化的顺序。</font>
12. `**@Lazy**`**<font style="color:rgb(6, 6, 7);">注解</font>**<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">使用</font>`@Lazy`<font style="color:rgb(6, 6, 7);">注解来控制Bean的懒加载。</font>
13. **<font style="color:rgb(6, 6, 7);">注册</font>**`**BeanDefinition**`<font style="color:rgb(6, 6, 7);">：</font>
    - <font style="color:rgb(6, 6, 7);">通过编程方式使用</font>`BeanDefinition`<font style="color:rgb(6, 6, 7);">注册Bean定义到</font>`BeanDefinitionRegistry`<font style="color:rgb(6, 6, 7);">。</font>

<font style="color:rgb(6, 6, 7);">这些方法可以单独使用，也可以组合使用，以满足不同的配置需求。Spring的灵活性允许开发者根据自己的喜好和项目需求选择合适的方式来加载和管理Bean。</font>





## 谈谈你对SpringIOC的理解，原理和实现两方面
**<font style="color:rgb(51, 51, 51);">总：</font>**

<font style="color:rgb(51, 51, 51);">控制反转：理论思想，原来的对象是由使用者来进行控制，有了spring之后，可以把整个对象交给spring来帮我们进行管理</font>

<font style="color:rgb(51, 51, 51);">				</font><font style="color:rgb(51, 51, 51);">DI：依赖注入，把对应的属性的值注入到具体的对象中，@Autowired，populateBean完成属性值的注入</font>

<font style="color:rgb(51, 51, 51);">容器：存储对象，使用map结构来存储，在spring中一般存在三级缓存，singletonObjects存放完整的bean对象,</font>

<font style="color:rgb(51, 51, 51);">			整个bean的生命周期，从创建到使用到销毁的过程全部都是由容器来管理（bean的生命周期）</font>



**<font style="color:rgb(51, 51, 51);">分：</font>**

<font style="color:rgb(51, 51, 51);">1、一般聊ioc容器的时候要涉及到容器的创建过程（beanFactory,DefaultListableBeanFactory）,向bean工厂中设置一些参数（BeanPostProcessor,Aware接口的子类）等等属性</font>

<font style="color:rgb(51, 51, 51);">2、加载解析bean对象，准备要创建的bean对象的定义对象beanDefinition,(xml或者注解的解析过程)</font>

<font style="color:rgb(51, 51, 51);">3、beanFactoryPostProcessor的处理，此处是扩展点，PlaceHolderConfigurSupport,ConfigurationClassPostProcessor</font>

<font style="color:rgb(51, 51, 51);">4、BeanPostProcessor的注册功能，方便后续对bean对象完成具体的扩展功能</font>

<font style="color:rgb(51, 51, 51);">5、通过反射的方式讲BeanDefinition对象实例化成具体的bean对象，</font>

<font style="color:rgb(51, 51, 51);">6、bean对象的初始化过程（填充属性，调用aware子类的方法，调用BeanPostProcessor前置处理方法，调用init-mehtod方法，调用BeanPostProcessor的后置处理方法）</font>

<font style="color:rgb(51, 51, 51);">7、生成完整的bean对象，通过getBean方法可以直接获取</font>

<font style="color:rgb(51, 51, 51);">8、销毁过程</font>

<font style="color:rgb(51, 51, 51);">面试官，这是我对ioc容器的整体理解，包含了一些详细的处理过程，您看一下有什么问题，可以指点我一下（允许你把整个流程说完）</font>

<font style="color:rgb(51, 51, 51);">您由什么想问的？</font>

<font style="color:rgb(51, 51, 51);">			</font><font style="color:rgb(51, 51, 51);">老师，我没看过源码怎么办？</font>

<font style="color:rgb(51, 51, 51);">		具体的细节我记不太清了，但是spring中的bean都是通过反射的方式生成的，同时其中包含了很多的扩展点，比如最常用的对BeanFactory的扩展，对bean的扩展（对占位符的处理），我们在公司对这方面的使用是比较多的，除此之外，ioc中最核心的也就是填充具体bean的属性，和生命周期（背一下）。</font>



## 谈谈你对Spring底层实现原理的理解
<font style="color:rgb(51, 51, 51);">底层实现：工作原理，过程，数据结构，流程，设计模式，设计思想</font>

<font style="color:rgb(51, 51, 51);">你对他的理解和你了解过的实现过程</font>

<font style="color:rgb(51, 51, 51);">反射，工厂，设计模式（会的说，不会的不说），关键的几个方法</font>

<font style="color:rgb(51, 51, 51);">createBeanFactory，getBean,doGetBean,createBean,doCreateBean,createBeanInstance(getDeclaredConstructor,newinstance),populateBean,initializingBean</font>

<font style="color:rgb(51, 51, 51);">1、先通过createBeanFactory创建出一个Bean工厂（DefaultListableBeanFactory）</font>

<font style="color:rgb(51, 51, 51);">2、开始循环创建对象，因为容器中的bean默认都是单例的，所以优先通过getBean,doGetBean从容器中查找，找不到的话，</font>

<font style="color:rgb(51, 51, 51);">3、通过createBean,doCreateBean方法，以反射的方式创建对象，一般情况下使用的是无参的构造方法（getDeclaredConstructor，newInstance）</font>

<font style="color:rgb(51, 51, 51);">4、进行对象的属性填充populateBean</font>

<font style="color:rgb(51, 51, 51);">5、进行其他的初始化操作（initializingBean）</font>







##  谈谈你对Spring中Bean对象生命周期的理解
<font style="color:rgb(51, 51, 51);">背图：记住图中的流程</font>

<font style="color:rgb(51, 51, 51);">在表述的时候不要只说图中有的关键点，要学会扩展描述</font>

<font style="color:rgb(51, 51, 51);">1、实例化bean：反射的方式生成对象</font>

<font style="color:rgb(51, 51, 51);">2、填充bean的属性：populateBean(),循环依赖的问题（三级缓存）</font>

<font style="color:rgb(51, 51, 51);">3、调用aware接口相关的方法：invokeAwareMethod(完成BeanName,BeanFactory,BeanClassLoader对象的属性设置)</font>

<font style="color:rgb(51, 51, 51);">4、调用BeanPostProcessor中的前置处理方法：使用比较多的有（ApplicationContextPostProcessor,设置ApplicationContext,Environment,ResourceLoader,EmbeddValueResolver等对象）</font>

<font style="color:rgb(51, 51, 51);">5、调用initmethod方法：invokeInitmethod(),判断是否实现了initializingBean接口，如果有，调用afterPropertiesSet方法，没有就不调用</font>

<font style="color:rgb(51, 51, 51);">6、调用BeanPostProcessor的后置处理方法：spring的aop就是在此处实现的，AbstractAutoProxyCreator</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">注册Destuction相关的回调接口：钩子函数</font>

<font style="color:rgb(51, 51, 51);">7、获取到完整的对象，可以通过getBean的方式来进行对象的获取</font>

<font style="color:rgb(51, 51, 51);">8、销毁流程，1；判断是否实现了DispoableBean接口，2，调用destroyMethod方法</font>



## 谈谈你对Spring中解决循环依赖的理解
<font style="color:rgb(51, 51, 51);">三级缓存，提前暴露对象，aop</font>

<font style="color:rgb(51, 51, 51);">总：什么是循环依赖问题，A依赖B,B依赖A</font>

<font style="color:rgb(51, 51, 51);">分：先说明bean的创建过程：实例化，初始化（填充属性）</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">1、先创建A对象，实例化A对象，此时A对象中的b属性为空，填充属性b</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">2、从容器中查找B对象，如果找到了，直接赋值不存在循环依赖问题（不通），找不到直接创建B对象</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">3、实例化B对象，此时B对象中的a属性为空，填充属性a</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">4、从容器中查找A对象，找不到，直接创建</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">形成闭环的原因</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">此时，如果仔细琢磨的话，会发现A对象是存在的，只不过此时的A对象不是一个完整的状态，只完成了实例化但是未完成初始化，如果在程序调用过程中，拥有了某个对象的引用，能否在后期给他完成赋值操作，可以优先把非完整状态的对象优先赋值，等待后续操作来完成赋值，相当于提前暴露了某个不完整对象的引用，所以解决问题的核心在于实例化和初始化分开操作，这也是解决循环依赖问题的关键，</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">当所有的对象都完成实例化和初始化操作之后，还要把完整对象放到容器中，此时在容器中存在对象的几个状态，完成实例化=但未完成初始化，完整状态，因为都在容器中，所以要使用不同的map结构来进行存储，此时就有了一级缓存和二级缓存，如果一级缓存中有了，那么二级缓存中就不会存在同名的对象，因为他们的查找顺序是1，2，3这样的方式来查找的。一级缓存中放的是完整对象，二级缓存中放的是非完整对象</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">为什么需要三级缓存？三级缓存的value类型是ObjectFactory,是一个函数式接口，存在的意义是保证在整个容器的运行过程中同名的bean对象只能有一个。</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">如果一个对象需要被代理，或者说需要生成代理对象，那么要不要优先生成一个普通对象？要</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">普通对象和代理对象是不能同时出现在容器中的，因此当一个对象需要被代理的时候，就要使用代理对象覆盖掉之前的普通对象，在实际的调用过程中，是没有办法确定什么时候对象被使用，所以就要求当某个对象被调用的时候，优先判断此对象是否需要被代理，类似于一种回调机制的实现，因此传入lambda表达式的时候，可以通过lambda表达式来执行对象的覆盖过程，getEarlyBeanReference()</font>

<font style="color:rgb(51, 51, 51);">		因此，所有的bean对象在创建的时候都要优先放到三级缓存中，在后续的使用过程中，如果需要被代理则返回代理对象，如果不需要被代理，则直接返回普通对象</font>

## 谈谈你对Spring中三级缓存和二级缓存的理解
<font style="color:rgb(51, 51, 51);">三级缓存：createBeanInstance之后：addSingletonFactory</font>

<font style="color:rgb(51, 51, 51);">二级缓存：第一次从三级缓存确定对象是代理对象还是普通对象的时候，同时删除三级缓存 getSingleton</font>

<font style="color:rgb(51, 51, 51);">一级缓存：生成完整对象之后放到一级缓存，删除二三级缓存:addSingleton</font>

## 谈谈你对Bean Factory和FactoryBean的理解
<font style="color:rgb(51, 51, 51);">相同点：都是用来创建bean对象的</font>

<font style="color:rgb(51, 51, 51);">不同点：使用BeanFactory创建对象的时候，必须要遵循严格的生命周期流程，太复杂了，，如果想要简单的自定义某个对象的创建，同时创建完成的对象想交给spring来管理，那么就需要实现FactroyBean接口了</font>

<font style="color:rgb(51, 51, 51);">			</font><font style="color:rgb(51, 51, 51);">isSingleton:是否是单例对象</font>

<font style="color:rgb(51, 51, 51);">			</font><font style="color:rgb(51, 51, 51);">getObjectType:获取返回对象的类型</font>

<font style="color:rgb(51, 51, 51);">			getObject:自定义创建对象的过程(new，反射，动态代理)</font>

## Spring中用到了哪些设计模式?
<font style="color:rgb(51, 51, 51);">单例模式：bean默认都是单例的</font>

<font style="color:rgb(51, 51, 51);">原型模式：指定作用域为prototype</font>

<font style="color:rgb(51, 51, 51);">工厂模式：BeanFactory</font>

<font style="color:rgb(51, 51, 51);">模板方法：postProcessBeanFactory,onRefresh,initPropertyValue</font>

<font style="color:rgb(51, 51, 51);">策略模式：XmlBeanDefinitionReader,PropertiesBeanDefinitionReader</font>

<font style="color:rgb(51, 51, 51);">观察者模式：listener，event，multicast</font>

<font style="color:rgb(51, 51, 51);">适配器模式：Adapter</font>

<font style="color:rgb(51, 51, 51);">装饰者模式：BeanWrapper</font>

<font style="color:rgb(51, 51, 51);">责任链模式：使用aop的时候会先生成一个拦截器链</font>

<font style="color:rgb(51, 51, 51);">代理模式：动态代理</font>

<font style="color:rgb(51, 51, 51);">委托者模式：delegate</font>

<font style="color:rgb(51, 51, 51);">。。。。。。。。。</font>

## 谈谈你对Spring中AOP的理解
<font style="color:rgb(51, 51, 51);">动态代理</font>

<font style="color:rgb(51, 51, 51);">aop是ioc的一个扩展功能，先有的ioc，再有的aop，只是在ioc的整个流程中新增的一个扩展点而已：BeanPostProcessor</font>

<font style="color:rgb(51, 51, 51);">总：aop概念，应用场景，动态代理</font>

<font style="color:rgb(51, 51, 51);">分：</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">bean的创建过程中有一个步骤可以对bean进行扩展实现，aop本身就是一个扩展功能，所以在BeanPostProcessor的后置处理方法中来进行实现</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">1、代理对象的创建过程（advice，切面，切点）</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">2、通过jdk或者cglib的方式来生成代理对象</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">3、在执行方法调用的时候，会调用到生成的字节码文件中，直接回找到DynamicAdvisoredInterceptor类中的intercept方法，从此方法开始执行</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">4、根据之前定义好的通知来生成拦截器链</font>

<font style="color:rgb(51, 51, 51);">		5、从拦截器链中依次获取每一个通知开始进行执行，在执行过程中，为了方便找到下一个通知是哪个，会有一个CglibMethodInvocation的对象，找的时候是从-1的位置一次开始查找并且执行的。</font>

## 谈谈你对Spring中事务这块的理解
<font style="color:rgb(51, 51, 51);">spring的事务管理是如何实现的？</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">总：spring的事务是由aop来实现的，首先要生成具体的代理对象，然后按照aop的整套流程来执行具体的操作逻辑，正常情况下要通过通知来完成核心功能，但是事务不是通过通知来实现的，而是通过一个TransactionInterceptor来实现的，然后调用invoke来实现具体的逻辑</font>

<font style="color:rgb(51, 51, 51);">		</font><font style="color:rgb(51, 51, 51);">分：1、先做准备工作，解析各个方法上事务相关的属性，根据具体的属性来判断是否开始新事务</font>

<font style="color:rgb(51, 51, 51);">				</font><font style="color:rgb(51, 51, 51);">2、当需要开启的时候，获取数据库连接，关闭自动提交功能，开起事务</font>

<font style="color:rgb(51, 51, 51);">				</font><font style="color:rgb(51, 51, 51);">3、执行具体的sql逻辑操作</font>

<font style="color:rgb(51, 51, 51);">				</font><font style="color:rgb(51, 51, 51);">4、在操作过程中，如果执行失败了，那么会通过completeTransactionAfterThrowing看来完成事务的回滚操作，回滚的具体逻辑是通过doRollBack方法来实现的，实现的时候也是要先获取连接对象，通过连接对象来回滚</font>

<font style="color:rgb(51, 51, 51);">				</font><font style="color:rgb(51, 51, 51);">5、如果执行过程中，没有任何意外情况的发生，那么通过commitTransactionAfterReturning来完成事务的提交操作，提交的具体逻辑是通过doCommit方法来实现的，实现的时候也是要获取连接，通过连接对象来提交</font>

<font style="color:rgb(51, 51, 51);">				</font><font style="color:rgb(51, 51, 51);">6、当事务执行完毕之后需要清除相关的事务信息cleanupTransactionInfo</font>

<font style="color:rgb(51, 51, 51);">如果想要聊的更加细致的话，需要知道TransactionInfo,TransactionStatus,</font>



## 具体谈谈你对Spring中事务传播行为的理解
<font style="color:rgb(51, 51, 51);">传播特性有几种？7种</font>

<font style="color:rgb(51, 51, 51);">			</font><font style="color:rgb(51, 51, 51);">Required,Requires_new,nested,Support,Not_Support,Never,Mandatory</font>

<font style="color:rgb(51, 51, 51);">			</font><font style="color:rgb(51, 51, 51);">某一个事务嵌套另一个事务的时候怎么办？</font>

<font style="color:rgb(51, 51, 51);">			</font><font style="color:rgb(51, 51, 51);">A方法调用B方法，AB方法都有事务，并且传播特性不同，那么A如果有异常，B怎么办，B如果有异常，A怎么办？</font>

---

<font style="color:rgb(51, 51, 51);">			</font><font style="color:rgb(51, 51, 51);">总：事务的传播特性指的是不同方法的嵌套调用过程中，事务应该如何进行处理，是用同一个事务还是不同的事务，当出现异常的时候会回滚还是提交，两个方法之间的相关影响，在日常工作中，使用比较多的是required，Requires_new,nested</font>

<font style="color:rgb(51, 51, 51);">			</font><font style="color:rgb(51, 51, 51);">分：1、先说事务的不同分类，可以分为三类：支持当前事务，不支持当前事务，嵌套事务</font>

<font style="color:rgb(51, 51, 51);">				2、如果外层方法是required，内层方法是，required,requires_new,nested</font>

<font style="color:rgb(51, 51, 51);">				3、如果外层方法是requires_new，内层方法是，required,requires_new,nested</font>

<font style="color:rgb(51, 51, 51);">				4、如果外层方法是nested，内层方法是，required,requires_new,nested</font>





事务传播总结: 多个事务嵌套底层逻辑， a 方法 b方法， 嵌套调用 ，该如何影响。

核心逻辑就是说， 两个方法是公用一个connection 链接 还是两个connection 链接， 如果彼此影响

那就用一个connection 链接，如果单方面影响 或者 那就用连个链接。 通过 aop 生成的拦截器链 进行控制

事务挂起 事务回滚，事务提交















