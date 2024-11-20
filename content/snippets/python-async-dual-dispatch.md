Title: Adding a Sync Version to Async Functions
Date: 2024-11-19 21:39
Category: snippets
Tags: python, async, decorator, Guido

Sometimes you need to call an async function synchronously. This `add_sync_version` decorator makes it straightforward
by adding a `.sync` attribute to your async function. The `.sync` version
uses `asyncio.new_event_loop().run_until_complete` to run the async code in a blocking way. Just decorate your function
with `@add_sync_version`, and you can call `func.sync(*args, **kwargs)` when sync access is needed. Inspired by
Guido's [comment here](https://discuss.python.org/t/how-can-async-support-dispatch-between-sync-and-async-variants-of-the-same-code/15014/7)
, it’s a simple way to handle mixed async and sync requirements.

```python
import asyncio
import functools


def add_sync_version(func):
    """
    Decorator that adds a `.sync` attribute to an async function, allowing it 
    to be called synchronously. The synchronous version uses a new event loop 
    to run the async function.

    Example:
        @add_sync_version
        async def spam():
            return "Hello, async world!"

        # Async usage:
        result = await spam()

        # Synchronous usage:
        result = spam.sync()

    Args:
        func (coroutine): The async function to wrap.

    Returns:
        coroutine: The original async function with an added `.sync` attribute.
    """
    assert asyncio.iscoroutinefunction(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.new_event_loop().run_until_complete(func(*args, **kwargs))

    func.sync = wrapper
    return func

```
