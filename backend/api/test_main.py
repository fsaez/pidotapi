from fastapi.testclient import TestClient
import pytest
import random

from main import app
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hola Mundo"}

def test_result_is_float():
    random_limit=random.uniform(1,100)
    dec = round(random.uniform(random_limit/2,random_limit))
    response = client.get("/pi/?random_limit={}".format(dec))
    assert response.status_code == 200
    assert float(response.json()["PiCalc"])