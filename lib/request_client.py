import requests as rq
import os

class RequestClient:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def login(func):
        api_url = os.getenv("api_url")
        username = os.getenv("fb_username")
        password = os.getenv("fb_password")
        headers = {}

        def with_token(self, *args, **kwargs):
            res = rq.post(
                url=f"{api_url}/login",
                headers={
                    "Content-Type": "application/json"
                },
                json={
                    "username": username,
                    "password": password
                }
            )
            if res.ok:
                token = res.text
                headers["X-Auth"] = token
                self.headers = headers
                self.token = token
                return func(self, *args, **kwargs)
            else:
                print(res.text)
                raise Exception("Cannot login")
        
        return with_token