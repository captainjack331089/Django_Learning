

### 缓存

- 提升服务器响应速度
- 将执行过的操作数据存储下来，在一定时间内，再次获取数据的时候，直接从缓存中获取
- 比较理想的方案，缓存使用内存级缓存
- Django内置缓存框架
  - 基于Memchached缓存
  - 使用数据库进行缓存
  - 使用文件系统进行缓存
  - 使用本地内存进行缓存
  - 提供缓存扩展接口



#### 缓存配置

1: 创建缓存表

​	python manage.py cretecachetable [table_name]

2: 缓存配置

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
        'TIMEOUT': 60 * 5,
      	'OPTIONS': {
          'MAX_ENTRIES': '300',
        }
      	'KEY_PREFIX': 'root',
      	'VERSION': '2',
    }
}
```



#### 缓存使用

- 在视图中使用（使用最多的场景）
- @cache_page()
  - time秒60*5 缓存5分钟
  - cashe缓存配置，默认default，
  - key_prefix前置字符串



#### 缓存底层

- 获取cashe

  - from django.core.cache import caches

    cache = caches['cache_name']

- 缓存操作

  - cache.set
    - key
    - value
    - timeout
  - get
  - add
  - get_or_set
  - get_many
  - set_many
  - delete
  - delete_many
  - clear
  - incr
    - incr(key,value) key对应的值上添加value
  - decr减少
    - decr(key,value) key对应的值上减少cache



#### 使用Redis做缓存

[Redis Download and Install Link](https://redis.io/download)

- 常见的有两个实现

  - django-redis
  - django-redis-cache

- 配置和内置的缓存配置基本一致

  ```python
  CACHES = {
      'default': {
          # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
          # 'LOCATION': 'my_cache_table',
          # 'TIMEOUT': 60 * 5,
          'BACKEND': 'django_redis.cache.RedisCache',
          'LOCATION': 'redis://127.0.0.1:6379',
          "OPTIONS": {
              "CLIENT_CLASS": "django_redis.client.DefaultClient",
          }
      }
  }
  ```

  

- 用法和内置缓存使用也一样

- 使用src/redis-cli，src/redis-server,启动redis，并查看缓存work不work



### AOP中间件

- 实现统计功能
  - 统计IP
  - 统计 浏览器
- 实现权重控制
  - 黑名单
  - 白名单
- 实现反爬
  - 反爬虫
    - eg：十秒之内搜索一次
  - 实现频率控制
- 界面友好化
- 应用交互友好化
- 调用顺序
  - 中间件注册的时候是一个列表
  - 如果我们没有在切点出直接进行返回 ，中间件会一次执行
  - 如果我们直接进行了返回，后续中间件就不再执行
- 切点
  - process_request
  - process_view
  - Process_template_response
  - Process_response
  - Process_exeption
- 切面



