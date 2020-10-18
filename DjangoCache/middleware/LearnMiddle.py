import random
import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):

    def process_request(self,request):
        print(request.META.get("REMOTE_ADDR"))

        ip = request.META.get("REMOTE_ADDR")

        #getphone页面
        # if request.path == '/app/getphone/':
        #     if ip == '127.0.0.1':
        #         if random.randrange(100) > 20:
        #             return HttpResponse('恭喜你抢到supreme!')
        #
        # #限制10。1。1。2的ip用户买到supreme
        # if request.path == '/app/getticket/':
        #     if ip.startswith('10.1.1.2'):
        #         return HttpResponse('已售完')
        #
        # if request.path == '/app/search/':
        #     result = cache.get(ip)
        #     if result:
        #         return HttpResponse('您的访问过于频繁，请10秒后再次搜索')
        #     cache.set(ip, ip, timeout=10)

        #反爬虫 1分钟最多访问10次

        blacklist = cache.get('black', [])
        if ip in blacklist:
            return HttpResponse('黑名单用户')
        requests =  cache.get(ip, [])
        while requests and time.time() - requests[-1] > 60:
            requests.pop()

        requests.insert(0, time.time())
        cache.set(ip, requests, timeout=60)

        if len(requests) > 300:
            blacklist.append(ip)
            cache.set('black', blacklist, timeout=20)
            return HttpResponse('你被ban了')

        if len(requests) > 100:
            return HttpResponse('请求次数过于频繁')


    def process_exception(self, request, exception):
        print(request, exception)
        return redirect(reverse('App:home'))


class TwoMiddle(MiddlewareMixin):
    def process_request(self,request):
        print('Two Middleware')