import argparse
import asyncio, logging
import time
import aiohttp

logger = logging.getLogger(__name__)


def profiled_aiohttp_reqs(aiohttp_session, url: str,):
    starting_time = time.time()
    ending_time = time.time()
    working_time = ending_time-starting_time
    

def get_tasks(aiohttp_session, url: str, number_request: int):
    tasks = [aiohttp_session.get(url) for i in range(number_request)]
    # Alternatively, this is throwing those tasks straight into the event loop. Gather will wait for them instead
    # of throwing them in the event loop.
    # tasks = [asyncio.create_task(aiohttp_session.get(url) for i in range(1000))]
    return tasks


async def main(url: str = "http://0.0.0.0:9000/", number_requests: int = 1000):
    # dummy_url = "http://localhost:9000/"
    # dummy_url = "http://0.0.0.0:9000/"

    # aiohttp --------------------
    aiohttp_client = aiohttp.ClientSession()
    async with aiohttp_client as session:
        tasks = get_tasks(aiohttp_session=session, url=url, number_request=number_requests)
        responses = await asyncio.gather(*tasks)

    # for response in responses:
    #     print(f"{await response.text()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', type=str, required=True)
    parser.add_argument('-nr', '--number_requests', type=int)
    args = parser.parse_args()

    starting_time = time.time()
    print(f"Starting...:")
    number_requests = 1000 or args.number_requests
    asyncio.run(main(url=args.__dict__.get("server"), number_requests=number_requests))

    ending_time = time.time()
    print(f"🤖 {number_requests} requests executed!")
    print(f"Execution time: {ending_time - starting_time}")
