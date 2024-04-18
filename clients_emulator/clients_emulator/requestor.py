import threading
import time
from typing import Callable

import requests


def fire_and_forget(function: Callable, *args, **kwargs):
    threading.Thread(target=function, args=tuple(args)).start()


def _get(url: str):
    return requests.get(url=url)


def main(url: str = "http://0.0.0.0:9000/"):
    for i in range(1000):
    #     fire_and_forget(requests.request, "GET", url)
        # print(response.content)
        _get(url=url)


if __name__ == "__main__":
    starting_time = time.time()
    main()
    ending_time = time.time()
    print(f"Execution time: {ending_time - starting_time}")
