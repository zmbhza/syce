from locust import HttpUser, TaskSet, task
from locust.contrib.fasthttp import FastHttpUser
import time
class WebsiteTasks(TaskSet):

    @task(1)
    def job_1(self):
        # 模拟商品列表接口

        url = "http://pressure.baishapu.com/dev-api/product/test/feign-productList"

        payload = "{\"brandIds\":null,\"classifyIds\":null,\"maxPrice\":null,\"minPrice\":null,\"modelIds\":null,\"name\":null,\"newProduct\":null,\"page\":1,\"pageSize\":10,\"priceSort\":null,\"quotedPriceId\":null,\"marketingId\":null,\"saleSort\":null,\"type\":null}"
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }
        with self.client.post(url, data=payload,headers=headers,catch_response=True) as res:
            s = res.json()
            #print (s['code'],time.strftime("%Y-%m-%d %H:%M:%S"))

        try :
            if s['code'] == 200:
                res.success()
        except:
                res.failure('返回错误')
    @task(0)
    def job_02(self):
        #全组建调用
        url = "http://pressure.baishapu.com/dev-api/product/test/feign/feign-post"

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }
        with self.client.post(url, data=payload,headers=headers,catch_response=True) as res:
            s = res.json()
            #print(s['code'])
        try :
            if s['code'] == 200:
                res.success()
        except:
                res.failure('返回错误')

    @task(0)
    def job_03(self):
        url = "http://pressure.baishapu.com/dev-api/uc/test/this/this-post"

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }
        with self.client.post(url, data=payload,headers=headers,catch_response=True) as res:
            s = res.json()
            #print(s['code'])
        try :
            if s['code'] == 200:
                res.success()
        except:
                res.failure('返回错误')


class WebsiteUser(FastHttpUser):
    host = "http://pressure.baishapu.com"
    tasks = [WebsiteTasks]
    min_wait = 1000
    max_wait = 3000

