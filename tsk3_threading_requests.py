import json
import threading

import requests


def get_url(_url, json_result):
    result = requests.get(_url)
    json_result.append((_url, result.json()))


if __name__ == "__main__":
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5",
    ]

    data = []
    threads = []
    for url in urls:
        thread = threading.Thread(target=get_url, args=(url, data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
