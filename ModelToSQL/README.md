- DB --> Model
  - Python. manage.py inspectdb
  - 可以直接生成Model
  - python manage.py inspectie > models.py
  - 生成的Model拥有元信息 manage=False



- 静态资源
  - 使用的时候注意配置资源信息
  - STATICFILE_DIRS
  - 使用{% load static %}
  - {% static '相对路径' %}



- 文件上传
  - 客户端
    - 必须使用POST
    - 指定enctype='multiplepart/form-data'
  - 原生
    - 文件复制
    - 从request.FILES中获取上传上来的文件
    - 从上传上来的文件进行读取，向打开的文件中进行写入
    - 每次写入记得flush
  - Django内置
    - ImageField
      - 依赖pillow
      - 配置使用
        - settings中指定MEDIA_ROOT
        - 指定字段的upload_to
          - 相对于MEDIA_ROOT的路径
          - 支持时间格式化
            - %Y
            - %M
            - %D
            - %h
            - ...







### PROJECT

-  创建拥有图片的主页
- 上传头像，照片