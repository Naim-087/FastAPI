
import asyncio
import time


async def task_a():
    print("Task A started")
    await asyncio.sleep(2)
    print("Task A finished")


async def task_b():
    print("Task B started")
    await asyncio.sleep(1)
    print("Task B finished")


async def main():
    start = time.perf_counter()

    await task_a()
    await task_b()

    elapsed = time.perf_counter() - start
    print(f"Total time: {elapsed:.2f} seconds")


asyncio.run(main())
