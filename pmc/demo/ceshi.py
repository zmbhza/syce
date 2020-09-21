from locust import HttpUser, TaskSet, task
from demo import params as p
from demo import index as i


class WebsiteTasks(TaskSet):
    def locust_setup(self):
        pass
    @task(1)
    def job(self):
        p.ase_post(self,'登录')
    @task(0)
    def s(self):
        print('saaa')
class WebsiteUser(HttpUser):
    host = "http://47.99.56.148/"
    tasks = [WebsiteTasks]
    min_wait = 1000
    max_wait = 5000
if __name__ == '__main__':
    import os
    os.system("locust -f  C:/Users/zhao/PycharmProjects/pmc/demo/ceshi.py --web-host=127.0.0.1")