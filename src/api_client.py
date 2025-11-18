import requests as r

from src.config import BASE_URL, API_KEY, WRONG_API_KEY


class APIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    # def request_valid_auth(self, methon="get", endpoint=""):
    #     return reqs.get(methon)(
    #         url=f"{self.base_url}{endpoint}",
    #         headers={"x-api-key": API_KEY},
    #     )

    # def request_invalid_auth(self, methon="get", endpoint=""):
    #     return reqs.get(methon)(
    #         url=f"{self.base_url}{endpoint}", 
    #         headers={"x-api-key": "abcd_abcd_1"},
    #     )

    # def request_no_auth(self, methon="get", endpoint=""):
    #     return reqs.get(methon)(
    #         url=f"{self.base_url}{endpoint}", 
    #         headers={},
    #     )

    # def request(self, methon="get" or "post", endpoint="", api_key=""):
    
    #     return reqs.get(methon)(
    #         url=f"{self.base_url}{endpoint}",
    #         headers={"x-api-key": api_key,},
            
    #     )

    def request_get(self, endpoint="", api_key=""):
        return r.get(
            url=f"{self.base_url}{endpoint}",
            headers={"x-api-key": api_key},
        )
    
    # def request_get_with_no_apiKey(self, endpoint=""):
    #     return r.get(
    #         url=f"{self.base_url}{endpoint}",
    #         headers={},
    #     )
    
    def request_post(self, endpoint="", api_key="", data={}):
        return r.post(
            url=f"{self.base_url}{endpoint}",
            headers={"x-api-key": api_key, "Content-Type": "application/json"},
            json=data,
        )