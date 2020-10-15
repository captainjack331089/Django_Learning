- Template

  - MTV中的Template

  - 充当数据展示的角色

  - 在Django中使用的就是Django模版

  - 模版组成

    - 静态HTML
    - 模版语法 
      - 变量
        - {{ var }}
        - 变量名遵循命名规范
        - 来源
          - 视图中传递过来的
          - 在标签，逻辑中创建出来的
      - 标签
        - {% exp %}
        - 标签分为单标签和双标签
        - 双标签必须闭合
        - 结构标签
          - block
            - 块
            - 用来规划填充页面
              - 首次出现：规划
              - 第二次出现：填坑
              - 第三次出现：也代表填坑，默认会覆盖
              - 第N次..
              - 如果不想被覆盖 block.super
          - extend
            - 继承
            - 面向对象的体现
            - 提高模版的复用率
          - include
            - 包含
            - 将其他模版作为一部分，包裹到页面中
          - block+extends
            - 化整为零
          - include+xxx
            - 由零聚一
        - 功能标签
          - if
            - 分支
            - 判断
            - if-else
            - if-else-else
          - for
            - for i in xxx
            - empty
            - forloop
          - ifequal
          - ifnotequal
          - withratio
        - 过滤器
          - 将前面的输入作为后面的输出
          - upper
          - lower
          - safe
            - 确认安全
            - 进行渲染
          - add
        - 注释
          - 单行(#  #)
          - 多行(% comment T%)

  - 模版加载

    - 加载模版
    - 渲染模版

  - 请求状态码

    - 2xx: 成功

    - 3xx: 重定向

    - 4xx: 客户端错误

    - 5xx: 服务端错误

      

- Views - 视图函数 - MTV中的V
  - 视图函数
    - 相当于controller的作用
    - 控制器，接受用户输入
    - 协调模版模型，对数据进行处理
  - 路由器
    - urls
      - urlpatterns
      - 跟路由中，我们会使用include形式将整个子路由添加进来
      - 第一个参数，正则匹配的路径
      - 第二个参数，包含那个路由
      - 第三个参数，namespace，命名空间用来以后反向解析
      - 在子路由中
        - 前两个参数一致
        - 第三个参数name
        - 以后会根据namespace：name动态获取我们的路由
    - 接受参数
      - 路径参数
        - 位置参数
          - 使用圆括号包含规则
          - 一个圆括号代表一个参数
          - 代表视图函数上的一个参数
          - 参数个数和视图函数上的参数一一对应（除默认request）
        - 关键字参数
          - 可以在圆括号中指定参数名字(?P<name>reg)
          - 视图函数中存在和圆括号中name对应的参数
          - 参数不区分顺序
          - 个数也需要保持一致，一一对应
      - 请求参数
    - 反向解析
      - 在模版中使用
      - {% url %} 
        - {% url 'namespace:name'%}
        - 如果存在位置参数
          - {% url 'namespace:name' value1 value2... %}
        - 如果存在关键字参数
          - { % url 'namespace:name' key1=value1 key2=value2... %}
    - 路由规则
      - 按照书写顺序，从上到下匹配
      - 没有最优匹配的概念，匹配到就停止了
  - 双R
    - Request
      - Django框架根据Htttp请求报文自动生成的一个对象
      - 包含了请求各种信息
      - path
      - method
        - GET
        - POST
      - encoding
      - GET
        - QueryDict
        - 类字典结构
          - Key-value
          - 一个key可以对应多个值
          - get
          - getlist
      - POST
      - FILES
      - COOKIES
      - session
      - is_ajax()
      - META
        - 元信息
        - 客户端的所有信息
          - ip
          - 环境所有信息变量
          - ...
    - Response
      - 服务器针对客户端的请求作出的响应
      - 开发者自己创建的
      - 响应分类
        - HTML响应
          - 基类HttpResponse
          - HttpResponseRedirect
            - 响应重定向
            - 302: 资源临时性发生转移
            - 301:永久性转移
            - 路由地址
            - reverse：python代码中的反向解析
              - reverse('namespace:name')
              - 位置参数：reverse('namespace:name', args=(value1,value2...))
              - 关键字参数： reverse('namespace:name', kwargs={key1:value1, key2:value2...})
          - 状态码
            - 301：永久性转移
            - 400：不好的错误请求
            - 403：被禁止
            - 404:   买找到
            - 405：请求方法 不支持
            - 500:   服务器错误
        - json
          - JsonResponse
          - 只是在init的时候，将数据序列化为json
      - 属性和方法
        - content
        - encoding
        - status_code
        - content_type
          - MINE: 互联网邮件传输扩展类型
            - 标识浏览器以什么形式打开我们的内容
            - 大类型/小类型
        - write
        - flush
  - 错误页面自定义
    - 创建错误码对应的模版
    - 就近原则查找
    - 关闭DEBUG
  - 会话技术
    - 为什么会有会话技术
      - 服务器为了识别客户端
      - web开发中绝大多数都是短连接
      - 请求生命周期从request开始，到response就结束了
      - 让客户端记住自己是谁
    - 会话技术的实现
      - cookie
        - 客户端会话技术
        - 数据都存储在客户端
        - 以key-value形式进行存储
        - 支持过期时间
        - 默认请求携带本网站的左右cookie
        - cookie不能跨域名，不能跨浏览器
        - cookie默认不支持中文 
      - session
        - 服务端会话技术
        - 数据都存储在服务端
        - 支持过期
        - 在django中被持久化到数据库中
        - 默认做了数据安全，使用了BASE64
        - 依赖于cookies
      - token
        - 会话技术
        - 自定义的session
        - 数据存储在服务器中
        - 如果用在web网站开发中效果等同于session
        - 主要应用场景是在移动端和专用客户端开发中，不支持cookie的设备中、
  - 常见的算法
    - 编码
    - 摘要
    - 指纹
    - 杂凑
      - 单向不可逆
      - 输出长度固定
      - 输入变更一点点，输出发生很大的变更
      - MD5,SHA
      - hashlib
    - 加密
      - 对称加密
        - 一把钥匙
      - 非对称加密
        - 一对钥匙
        - 公钥
        - 私钥
        - RSA，PGP
  - CSRF
    - 防跨站攻击
    - Django中内置csrf插件
    - 实现机制
      - 页面中存在{% csrf %}时，在渲染的时候，会向Response中添加 csrftoken的cookie
      - 在提交的时候，会被添加到请求体中，被验证有效性





### PROJECT



利用request和response

- 创建登录页面
- 创建登录成功页面
- 创建注销页面
- 创建注册页面

