import requests


class CustomSession(requests.Session):
    def __init__(self):
        super().__init__()
        self.headers.update({'User-agent': 'CustomSession', 'Accept': 'application/json'})

    def get(self, url, **kwargs):
        print('Performing GET on {}'.format(url))
        resp = super().get(url=url, **kwargs)
        resp.raise_for_status()
        print('{} returned status: {}'.format(url, resp.status_code))
        return resp.json()



class MyAppClient(CustomSession):
    URL = 'https://myapp.corpdomain/'

    def get_stuff(self):
        resp = super().get(url='{}stuff'.format(self.URL))
        return resp


class TestSession(CustomSession):
    def get(self, url, **kwargs):
        print('TEST: app tried to GET {}'.format(url))
        return {}


class TestMyAppClient(MyAppClient, TestSession):
    pass
