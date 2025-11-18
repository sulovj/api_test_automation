from src.api_client import APIClient
import time
import json
from jsonschema.exceptions import ValidationError
from jsonschema import validate
from src.config import API_KEY, WRONG_API_KEY, endpoints, expectedResponseTime

client = APIClient()


def testGetListUsers():
    # ----------------------------------------------------------------------------------------------
    
    # Penetration testing - Negative testing
    # invalid authorization - api_key is wrong
    # response = client.request_get(endpoint=endpoints.get("getListUsers"), api_key=WRONG_API_KEY)

    # assert response.status_code == 403  # Forbidden


    # ----------------------------------------------------------------------------------------------
    # Penetration testing - Positive testing
    # valid authorization - api_key is correct
    response = client.request_get(endpoint=endpoints.get("getListUsers"), api_key=API_KEY)

    assert response.status_code == 200 # OK

    received_data = response.json()

    # Assertion of received data in Response

    assert received_data.get("total")


    assert received_data["data"][0].get("last_name")
    assert received_data["data"][0].get("last_name") == "Lawson"
    assert received_data["data"][1].get("last_name")
    assert received_data["data"][1].get("last_name") == "Ferguson"

    assert received_data.get("total") == len(response.json().get("data"))
    # assert (received_data.get("total")/received_data.get("total_pages")) == len(received_data.get("data"))

    # Assertions of possible data types
    assert isinstance(received_data.get("page"), int), "The instance is not type int"
    assert isinstance(received_data.get("per_page"), int), "The instance is not type int"
    assert isinstance(received_data.get("total"), int), "The instance is not type int"
    assert isinstance(received_data.get("total_pages"), int), "The instance is not type int"
    assert isinstance(received_data.get("data"), list), "The instance is not type list"

    for user in received_data.get("data"):     
        assert isinstance(user.get("id"), int), "The instance is not type int"
        assert isinstance(user.get("email"), str), "The instance is not type str"
        assert isinstance(user.get("first_name"), str), "The instance is not type str"
        assert isinstance(user.get("last_name"), str), "The instance is not type str"
        assert isinstance(user.get("avatar"), str), "The instance is not type str"



def testPostCreateUser():
    with open("src/schemas/newUser.json") as f:
        payload = json.load(f)
    
    # ----------------------------------------------------------------------------------------------
    
    # Penetration testing - Negative testing
    # invalid authorization - api_key is wrong
    response = client.request_post(endpoint=endpoints.get("postCreate"), api_key=WRONG_API_KEY)

    assert response.status_code == 403  # Forbidden


    # ----------------------------------------------------------------------------------------------
    # Penetration testing - Positive testing
    # valid authorization - api_key is correct
    # response = client.request_post(endpoint=endpoints.get("postCreate"), api_key=API_KEY, data=payload)

    start_time = time.time()
    response = client.request_post(endpoint="/api/users", api_key=API_KEY, data=payload)
    end_time = time.time()

    elapsed_response_time = (int)((end_time - start_time) * 1000)

    assert response.status_code == 201 # OK

    assert elapsed_response_time < expectedResponseTime, f"ERROR: The response time is {elapsed_response_time} ms that exceeded the limit 100ms"

    transmitted_data = response.json()


    assert transmitted_data.get("id")
    assert transmitted_data.get("createdAt")

    with open("src/schemas/createUser.json") as f:
        schema_createUser = json.load(f)
    
    # Verifying the response schema
    try:
        validate(instance=transmitted_data, schema=schema_createUser)
        assert True
    except ValidationError as ex:
        print(ex)
        assert False
    
    