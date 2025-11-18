
BASE_URL = "https://reqres.in"

page = 2
endpoints = {
    "getListUsers": f"/api/users?page={page}",
    "postCreate": "/api/users"
}

API_KEY = "reqres-free-v1"
WRONG_API_KEY = "abcd_abcd_12"

expectedResponseTime = 100


