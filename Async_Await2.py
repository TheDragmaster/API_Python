import asyncio
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)   #Can basically do both at the same time change the sleep amount 
    print('done fetching')
    return{'data' : 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)  #Prints 4 numbers every second 


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2

asyncio.run(main())