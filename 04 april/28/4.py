import asyncio
import time


async def func1(x):
    print(x ** 2)
    await asyncio.sleep(2)
    print("func1 finished")


async def func2(x):
    print(x ** 2)
    await asyncio.sleep(2)
    print("func2 finished")


async def func3(x):
    print(x ** 2)
    await asyncio.sleep(2)
    print("func3 finished")

async def main():
    task3 = asyncio.create_task(func3(4))
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(4))
    # task3 = asyncio.create_task(func3(4))

    # await task3
    # await asyncio.gather(task1, task2)
    await task2
    await task1
    await task3

if __name__ == "__main__":
    print(time.strftime("%X"))
    asyncio.run(main())
    print(time.strftime("%X"))
