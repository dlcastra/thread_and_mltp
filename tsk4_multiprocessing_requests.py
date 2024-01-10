import multiprocessing

import requests


def make_request(_url):
    response = requests.get(_url)
    return f"URL: {_url}, Status Code: {response.status_code}"


if __name__ == "__main__":
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5",
    ]

    with multiprocessing.Pool(5) as pool:
        results = pool.map(make_request, urls)

    for result in results:
        print(result)
