Title: Python Enum Reference
Date: 2025-06-05 11:36
Category: snippets
Tags: python, guides

I am always forgetting the particulars of this, so here is a quick reminder.

```python
from enum import Enum


class EnumTesting(str, Enum):
    a = "a"
    b = "b"


a = "a"
b = "bad"

print(EnumTesting(a))  # Enumtesting.a
try:
    print(EnumTesting(b))
    assert False
except ValueError:
    print("Got error")

print(EnumTesting[a])  # Enumtesting.a
try:
    print(EnumTesting[b])
    assert False
except KeyError:
    print("Got error")


print(EnumTesting(EnumTesting.a))  # Enumtesting.a
print(EnumTesting[EnumTesting.a])  # Enumtesting.a
```