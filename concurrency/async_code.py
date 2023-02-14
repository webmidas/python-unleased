import asyncio


async def async_sleep():
    print('before sleep')
    await asyncio.sleep(10)
    print('After sleep')


def print_something():
    print('hello')

async def main():
    await async_sleep()
    print_something()



if __name__ == "__main__":
    asyncio.run(main())