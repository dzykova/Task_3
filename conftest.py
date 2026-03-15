import pytest
import requests
import random
import string
import uuid
from selenium import webdriver
from urls import BASE_URL

@pytest.fixture(params=["firefox", "chrome"])
def driver(request):

    if request.param == "firefox":
        driver = webdriver.Firefox()

    elif request.param == "chrome":
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user():
    
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_email():
        return f"test_{uuid.uuid4().hex}@gmail.com"

    email = generate_email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(f"{BASE_URL}/api/auth/register", data=payload)
    accessToken = response.json()["accessToken"]

    yield {
        "email": email,
        "password": password
    }

    # teardown
    requests.delete(f"{BASE_URL}/api/auth/user", headers={'Authorization': accessToken})