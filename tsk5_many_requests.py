import concurrent.futures
import time

import requests


def make_request(_url):
    requests.get(_url)


def make_liner_request(urls):
    start = time.time()

    for url in urls:
        make_request(url)

    stop = time.time()
    print(f"Витрачений час на послідовні запити: {stop - start}")


def make_concurrent_requests(urls):
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(2) as executor:
        executor.map(make_request, urls)

    stop = time.time()
    print(f"Витрачений час на thread запити: {stop - start}")


if __name__ == "__main__":
    urls_to_request = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5",
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5",
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5",
    ]

    make_liner_request(urls_to_request)
    make_concurrent_requests(urls_to_request)
