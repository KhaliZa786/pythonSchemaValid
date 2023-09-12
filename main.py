import pytest
import requests
from pytest_check import check
import schema
from jsonschema import validate

def test_ListUsers():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    message = response.text
    validate(message,schema.schemaListUsers())

def test_SingleUser():
    url = 'https://reqres.in/api/users/2'
    response = requests.get(url)
    message = response.text
    validate(message, schema.schemaSingleUser())

def test_SingleUserNotFound():
    url = 'https://reqres.in/api/users/23'
    response = requests.get(url)
    message = response.text
    if response.status_code = 200:
        validate(message, schema.schemaSingleUserNotFound())
    elif response.status_code = 400:
        assert True

def test_ListResource():
    url = 'https://reqres.in/api/unknown'
    response = requests.get(url)
    message = response.text
    validate(message, schema.schemaListResource())

def test_SingleResource():
    url = 'https://reqres.in/api/unknown/2'
    response = requests.get(url)
    message = response.text
    validate(message, schema.schemaSingleResource())

def test_SingleResourceNotFound():
    url = 'https://reqres.in/api/unknown/23'
    response = requests.get(url)
    message = response.text
    if response.status_code = 200:
        validate(message, schema.schemaSingleUserNotFound())
    elif response.status_code = 400:
        assert True

def test_Create():
    url = 'https://reqres.in/api/users'
    response = requests.post(url)
    message = response.text
    validate(message, schema.schemaCreate())

def test_Update():
    url = '/api/users/2'
    response = requests.put(url)
    message = response.text
    validate(message, schema.schemaUpdate())

def test_Update():
    url = '/api/users/2'
    response = requests.patch(url)
    message = response.text
    validate(message, schema.schemaUpdate())

def test_Delete():
    url = '/api/users/2'
    response = requests.delete(url)
    message = response.text
    if response.status_code = 200:
        validate(message, schema.schemaSingleUserNotFound())
    elif response.status_code = 400:
        assert True

def test_RegisterSuccessful():
    url = '/api/register'
    response = requests.post(url)
    message = response.text
    if response.status_code = 200:
        validate(message, schema.schemaRegisterSuccessful())
    elif response.status_code = 400:
        assert True


def test_LoginSuccessful():
    url = '/api/login'
    response = requests.post(url)
    message = response.text
    if response.status_code = 200:
        validate(message, schema.schemaLoginSuccessful())
    elif response.status_code = 400:
        assert True

def test_DelayedResponse():
    url = '/api/users?delay=3'
    response = requests.get(url)
    message = response.text
    validate(message, schema.schemaDelayedResponse())