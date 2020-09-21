from demo import index as i
def ase_post(a,b):
    url = i.name(b)
    payload = i.payload(b)
    headers = i.headers(b)
    with a.client.post(url, data=payload, headers=headers, catch_response=True) as res:
        s = res.json()
        try :
            if s['code'] == 200:
                res.success()
                print(s['code'])
        except:
            res.failure('返回错误')
def ase_get(a,b):
    url = i.name(b)
    payload = i.payload(b)
    headers = i.headers(b)
    with a.client.get(url, data=payload, headers=headers, catch_response=True) as res:
        s = res.json()
        try :
            if s['code'] == 200:
                res.success()
                print(s['code'])
        except:
            res.failure('返回错误')
