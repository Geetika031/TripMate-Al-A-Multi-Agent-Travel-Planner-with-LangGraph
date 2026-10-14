import asyncio
async def test():
    asyncio.sleep(2)
    return "hi"

async def test2():
    x = await test()
    y = await test()
    print(x)
    print(y)

asyncio.run(test2())