### MVC(Model, View, Controller)



- Model：用于封装与应用程序的业务逻辑相关的数据以及对数据的处理方法，是web应用程序中用于处理应用程序的数据逻辑部分，Model通常只提供功能性的借口，通过这些借口 可以获取Model的所有功能。
- View： 负责数据的显示和呈现，View是对用户的直接输出
- Controller： 负责从用户端收集用户的输入，可以看成提供view的反响功能。



### MVT/MTV (Model,View,Template)

- Model: 负责业务对象与数据库的对象
- View： 负责业务逻辑，并在适当的时候调用Model和Template
- Template：负责把页面展示给用户



在Django中 还有一个url分发器（路由）， 主要用来讲一个个url页面的请求分发给不同的view进行处理 ，view再调用相应的Model和template。



#### 实现一个请求

- 注册一个路由
  - urls中实现
    - url
      - 参数1: 匹配规则
      - 参数2: 视图函数
- 去views中实现对应的函数
  - 第一个参数数request
  - 返回response



#### 模版配置

- 在app中进行模版配置：
  - 只需在app的根目录创建templates文件夹
  - 如果想让代码自动提示，我们应该标记文件夹为模版文件夹
- 在项目目录中进行模版配置
  - 需要在项目目录中 创建templates文件夹标记
  - 需要在settings中进行注册
- 在开发中使用第二种
  - 模版可以继承，复用



#### 路由优化配置

- 项目如果逻辑过于复杂，可以进行拆分
- 拆分为多个app
- 继续拆分路由器 urls
  - 在app中创建自己的urls
    - 在urlpatterns路有规则列表
    - 在根urls中进行子路有的包含
  - 子路由使用
    - 跟路由规则 + 子路由的规则



#### models 使用了ORM技术

- Object Relational Mapping 对象关系映射
- 将业务逻辑和sql进行了一个解耦合
  - object.save()
  - object.delete()
- 关系型数据库
  - DDL
  - 通过models定义实现数据库表的定义
- 数据操作
  - 增删改查
  - 存储
    - save（）
  - 查询
    - 查所有 objects.all()
    - 查单个 objects.get(pk=i)
  - 更新
    - 基于查询的
    - 查好的对象，修改属性，然后save（）
  - 删除
    - 基于查询
    - 调用delete（）

#### 连接mysql驱动

- mysqlclient
  - Python2，3都能直接使用
  - 致命缺点：
    - 对mysql安装有要求，必须指定位置存在配置文件
- python-mysql
  - Python2支持很好
  - python3不支持
- pymysql
  - python3，python3都支持
  - 它还可以伪装成前面的库



#### django shell

- 集成了python环境的shell终端
- 通常在终端做一些调试工作



#### 如何看bug

- 看日志
  - 先看第一条
  - 再看最后一条
- 梳理思路
  - 程序在哪一个位置和预期出现偏差



#### 表关系

- 1:1
- 1:M
- M:N