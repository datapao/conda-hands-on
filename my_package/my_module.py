import requests

HELLO_URL = "https://datapao-public.s3.amazonaws.com/hello-from-datapao.json"


def hello():
    print(requests.get(HELLO_URL).json())


def main_function():
    hello()


if __name__ == "__main__":
    main_function()
