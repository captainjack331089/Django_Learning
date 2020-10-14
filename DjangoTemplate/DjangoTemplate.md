#### 标签

- {% %}标识符
- 标签分为单标签和成对标签
- 成对的标签不能省略，开始标签和结束标签



#### 结构标签

- block
  - 块
  - 用来规划我们的布局（挖坑）
  - 首次出现，代表规划
  - 第二次出现，代表填充以前的规划
  - 第三次出现，代表填充以前的规划，默认动作是覆盖
    - 如果不想覆盖，可以添加block.super
    - 这样就实现了增量式操作
- extends
  - 继承
  - 可以获取父模版中的所有结构
- block + extends
  - 化整为零
- include
  - 包含
  - 可以将页面作为一部分，嵌入到其他页面中
- include + block
  - 由零聚一
- 三个标签也可以混合使用
- 能用block + extends搞定的，就尽量不要使用include
- 如果继承自一个父模版，子模版自己直接重写的页面结构是不生效的，只能在既有的坑中进行填充



#### 静态资源

- 动静分离
- 创建静态文件夹
- 在settings中注册STATICFILES_DIRS=[]
- 在模版中使用
  - 先加载静态资源{% load static %}
  - 使用{% static 'xxxx' %} xxx相对路径
- 坑点
  - 仅在debug模式中使用
  - 以后需要自己单独处理

#### urls

- 路由器
  - 按照列表的书写顺序进行匹配的
  - 从上到下匹配，没有最优匹配的概念
- 路由匹配规则
  - 我们通常直接指定以^开头
  - 在结尾处直接添加反斜线
- 路由器/url组成
  - 协议
    - schema
    - http
    - https
    - ftp
    - rtmp
  - 域名
    - ip：port
    - 域名
  - 路径/path（相对于主机的路径）
  - GET请求参数，QueryString, 查询参数
  - 锚点
- 路由路径中的参数使用()进行获取
  - 一个圆括号对应视图函数中的一个参数
  - 参数
    - 路径参数
      - 位置参数
        - 按照书写顺序进行匹配
      - 关键字参数
        - 按照参数名称匹配，和顺序就无关了
    - 参数个数必须和视图函数中参数个数一致（除默认的request以外）
- 反向解析
  - 根据跟路由中注册的namespace和在子路由中注册name，这两个参数来动态获取我们的路径
  - 在模版中使用{% url 'namespace:name' %}
  - 如果带有位置参数 {% url 'namespace:name' value1 value2 [value...] %}
  - 如果带有关键字参数{% url 'namespace:name' key1=value1 key2=value2 [keyn=valuen...] %}



#### 错误页面定制

- 在模版中重写对应错误状态吗页面
- 关闭debug
- 实现原则
  - 就近原则



#### 双R

- Request
  - 内置属性
    - method
    - path
    - GET
      - 类字典结构
      - 一个key允许对应多个值
      - get
      - getlist
    - POST
    - META
      - 各种客户端源信息
      - REMOTE_ADDR远端反问ip
- Response





#### 知识点

- locals
  - 内置函数
  - 将局部变量使用字典的方式打包
  - key是变量名，value是变量中存储的数据