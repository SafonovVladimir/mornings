import asyncio

# A co-routine
async def add(x: int, y: int):
    return x + y

# An event loop
loop = asyncio.get_event_loop()

# Create a function to schedule co-routines on the event loop
# then print results and stop the loop
async def get_results():
    result1 = await add(3, 4)
    result2 = await add(5, 5)

    print(result1, result2) # Prints 7 10
    loop.stop()

loop.create_task(get_results())

# Blocking call interrupted by loop.stop()
try:
    loop.run_forever()
finally:
    loop.close()
