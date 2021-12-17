from locust import HttpUser, task, tag
from faker import Faker
from requests.auth import HTTPBasicAuth

from common.constants import OFD_BASIC_AUTH_USERNAME, OFD_BASIC_AUTH_PASSWORD


class TestSignupApiV100(HttpUser):
    host = 'http://34.121.223.187'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = Faker()
        self.params = None
        self.url = '/ofd_apis/v100/signup'
        self.authentication = HTTPBasicAuth(OFD_BASIC_AUTH_USERNAME, OFD_BASIC_AUTH_PASSWORD)

    @tag('signup_api')
    @task
    def test_api(self):
        self.client.post(url=self.url, data=self.params, auth=self.authentication)

    def on_start(self):
        self.params = {
            'username': self.faker.user_name(),
            'first_name': self.faker.first_name(),
            'last_name': self.faker.last_name(),
            'user_type': 1,
            'email': self.faker.email(),
            'password': self.faker.password()
        }