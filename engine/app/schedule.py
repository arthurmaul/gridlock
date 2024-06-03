import asyncio
from uuid import uuid4

groups = dict()

def create(name=None):
    key = name if name else str(uuid4())
    groups[key] = list()
    return groups[key]

def register(group, function, *args, **kwargs):
    group.append((function, args, kwargs))
    return register

async def pipeline(group):
    for coroutine, args, kwargs in group:
        await coroutine(*args, **kwargs)

async def phase(group):
    coroutines = (coroutine(*args, **kwargs)
        for coroutine, args, kwargs in group)
    await asyncio.gather(*coroutines)

def run(program):
    asyncio.run(program)

