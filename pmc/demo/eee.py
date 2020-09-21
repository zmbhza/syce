from locust import HttpUser, TaskSet, task
import random,json
from locust.contrib.fasthttp import FastHttpUser
def name():
    first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常",'左']
    second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文","明浩", "光", "超", "军", "达"]
    name = random.choice(first_name) + random.choice(second_name)+random.choice(first_name)+random.choice(second_name)+random.choice(first_name) + random.choice(second_name)+random.choice(first_name) + random.choice(second_name)
    return name
class WebsiteTasks(TaskSet):
    """query  查询,get"""
    @task
    def job_1(self):
            url = "http://47.99.56.148:9006/test/this/mysql/user/query"

            payload = ""
            headers = {
                'cache-control': "no-cache",
                'Postman-Token': "e037a007-9167-4da3-a3d1-a53a5d4d669b"
            }

            with self.client.get(url, data=payload,headers=headers,catch_response=True) as res:
                s = res.json()
            try :
                if s['code'] == 200:
                    res.success()
            except:
                    res.failure('返回错误')


    @task(0)
    #"""add  添加,post"""
    def job_2(self):

            url = "http://47.99.56.148:9006/test/this/mysql/user/add"

            payload = {
                "address":name(),
                "age":18,
                "name":name(),
                "sex":0
}
            headers = {
                'Content-Type': "application/json;charset=utf-8",
                'cache-control': "no-cache",
                'Postman-Token': "fcb60c53-1ada-44fc-969e-32a962526d8b"
            }

            with self.client.post(url, data=json.dumps(payload),headers=headers,catch_response=True) as res:
                s = res.json()
            try :
                if s['code'] == 200:
                    res.success()
            except:
                    res.failure('返回错误')

class WebsiteUser(FastHttpUser):
    host = "http://47.99.56.148/"
    tasks = [WebsiteTasks]
    min_wait = 1000
    max_wait = 3000
