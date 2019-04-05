"""
Python3.5+ asyncio example
"""

import asyncio


async def slow_operation(future):
    await asyncio.sleep(2)
    future.set_result('Future is done!')


def got_result(future):
    print(future.result())
    loop.stop()


loop = asyncio.get_event_loop()  # Event loop used to run
future = asyncio.Future()  # Promise of a result
asyncio.ensure_future(slow_operation(future))  # Get coroutine into the event loop
future.add_done_callback(got_result)  # Completed call back

try:
    loop.run_forever()
finally:
    loop.close()
