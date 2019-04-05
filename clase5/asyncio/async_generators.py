import asyncio


def z(x):
    pass


def gen(x):
    pass


def stuff(x):
    pass


async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y


async def g(x):
    yield x  # OK - this is an async generator


# async def m(x):
#     yield from gen(x)  # No - SyntaxError


def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y


@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine, older syntax"""
    yield from stuff(1)


async def py35_coro():
    """Native coroutine, modern syntax"""
    await stuff(1)
