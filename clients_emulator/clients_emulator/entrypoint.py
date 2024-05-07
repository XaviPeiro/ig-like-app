import argparse
import asyncio
from datetime import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--server', type=str, required=True)
    parser.add_argument('-t', '--type', type=str, required=True)
    args = parser.parse_args()


    starting_time = time.time()
    print(f"Starting...:")

    # if args.type == ""
    number_requests = 1000
    # asyncio.run(main(url=args.__dict__.get("server"), number_requests=number_requests))

    ending_time = time.time()
    print(f"🤖 {number_requests} requests executed!")
    print(f"Execution time: {ending_time - starting_time}")
