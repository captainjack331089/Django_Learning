#### 爬虫

- 模拟人去请求数据
- 提取数据
- 存储数据



#### MIME

- 作用： 指定传输数据使用哪种形式打开
- 格式： 大类型/小类型
  - image/png
  - Image/jpg



#### Json

- JsonObject
  - { }
  - Key - value
- JsonArray
  - [ ]
  - 列表中可以是普通数据类型，也可以是JsonObject
- JsonObject和JsonArray可以嵌套
- 给移动端的Json
- 给Ajax
  - 前后端
  - DRF



#### HTTPResponse

- HttpResponseRedirect
  - 重定向
  - 302
  - 简写 redirect
- JsonResponse
  - 以json格式返回数据
  - 重写了____init____, 序列化json数据，指定content_type为application/json
- HttpResponseBadRequest
  - 400
- HttpResponseNotFound
  - 404
- HttpResponseForbidden
  - 403
- HttpReponseNotAllowed
  - 405
- HttpResponseServerError
  - 500
- Http404
  - Exception
  - raise 主动抛异常



#### 会话技术

- 出现场景
  - 服务器如何识别客户端
  - Http在web开发中基本都是短连接
- 请求生命周期
  - 从request开始
  - 到response结束
- 种类
  - cookie
    - 客户端会话技术
      - 数据存储在客户端
    - 键值对存储
    - 支持过期时间
    - 默认cookie会自动携带，本网站所有cookie
    - cookie跨域名，跨网站
    - 通过HttpResponse操作客户端浏览器
    - cookie默认不支持中文
    - 可以加盐
      - 加密
      - 解密
  - session
    - 服务端会话技术
    - 数据存储在服务器中
    - 默认session存储在内存中
    - Django中默认会把session持久化到数据库
    - Django中session的默认过期时间是14天
    - 主键是字符串
    - 数据是使用了数据安全（=结尾是使用了base64的编码）
      - 使用base64
      - 在头部添加了一 个混淆串
    - Session依赖于cookie
  - token
    - 服务端会话技术
    - 自定义的session
    - 如果web页面开发中，使用起来和session基本一致
    - 如果 使用在移动端或客户端开发中，通常以json形式传输，需要移动端自己存储token，需要获取token关联数据的时候 ，主动传递 token
  - cookie，session， token对比
    - cookie使用更简洁，服务器压力更小，数据不是很安全
    - session服务器要 维护session，相对安全
    - token拥有session的所有优点，自己维护略微麻烦，支持更多的终端



#### CSRF

- 防跨站攻击
- 防止恶意注册，确保客户端是我们自己的客户端
- 使用了cookie中csrftoken进行验证，传输
- 服务器发送给客户端，客户端将cookie获取过来，还要进行编码转换（数据安全）
- 如何实现csrf机制：
  - 在我们中存在 csrf标签的页面中，响应会自动设置一个cookie，叫csrftoken
  - 当我们提交的时候，会自动验证csrftoken
  - 验证通过，正常执行以后流程，如果不通过，直接403



#### 算法

- 编码解码
  - base64
  - urlencode
- 摘要算法，指纹算法，杂凑算法
  - MD5，SHA
    - MD5默认是128的二进制
    - 32位的十六进制
    - 32位的Unicode
  - 单向不可逆
  - 不管输入多长，输出都是固定长度
  - 只要输入有任意的变更，输出都会发生巨大的变化
- 加密
  - 对称加密
    - 一把钥匙
    - DES，AES
    - 加密解密效率高
    - 钥匙一旦 丢失，所有数据都没了
  - 非对称加密
    - 两把钥匙，成对的
    - 公钥和私钥（互相制约）
    - RSA，PGP
    - 安全性最高
    - 算法复杂，需要时间长
    - 支付宝，微信都是RSA



#### 编码

- ASCII
- Unicode



#### 优秀程序

- 松耦合
  - 解耦合
- 高内聚



#### 登陆

- 首先有一个页面
  - 页面中有输入框
  - 有登录按钮
- 点完登陆，默认进入个人中心
- 个人中心可以显示用户名





#### 核心内容

- 数据爬取
- 数据提取
- 数据存储
- 提升效率
  - 进程
  - 线程
  - 协程





### 总结

- MTV
  - template
  - views
  - model
    - model关系
    - model继承
- 高级
  - 第三方插件
  - 底层的部分原理
  - aop面向切面编程
    - 反扒 
    - 安全
  - 文件上传
  - 前后端分离
    - RESTful
  - 日志
  - 后台管理
  - 用户角色，用户权限 
  - 部署
  - 支付宝支付