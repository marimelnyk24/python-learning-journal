# Enum

Status: 🟡 Learning

## What is it?

`Enum` is a class used to define a set of named constant values.

Instead of using raw strings or numbers, you define a controlled set of values.

This helps avoid typos and makes code more readable and safe.

---

## Why it is useful

Without Enum:

```python
status = "success"
```

Problems:
- easy to make typos ("succes")
- no validation
- unclear meaning

---

With Enum:

```python
from enum import Enum

class Status(Enum):
    SUCCESS = "success"
    ERROR = "error"
```

---

## When to use

- API statuses (success, error, pending)
- HTTP codes or labels
- Test categories (smoke, regression, integration)
- Environments (dev, stage, prod)
- Fixed sets of options in automation frameworks

---

## Example

```python
from enum import Enum

class Status(Enum):
    SUCCESS = "success"
    ERROR = "error"
    PENDING = "pending"


def handle_status(status: Status):
    if status == Status.SUCCESS:
        print("OK")
```

---

## Advanced usage

### auto()

When values do not matter:

```python
from enum import Enum, auto

class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
```

---

## Where did I use it?


---

## Benefits

- Prevents typos
- Makes code self-documenting
- Easier refactoring
- Centralized control of allowed values
- Better readability in tests and framework

---

## Things I can forget

### Enum comparison

Always compare with Enum members:

```python
status == Status.SUCCESS  # correct
status == "success"       # bad practice
```

---

### Accessing values

```python
Status.SUCCESS.value  # "success"
```

---

### Iterating over Enum

```python
for status in Status:
    print(status)
```

---

## Rules of Thumb

Use Enum when:
- values are fixed and limited
- you want to avoid magic strings
- you want safer comparisons in tests/framework

Do NOT use Enum when:
- values are dynamic
- data comes from unknown external sources and changes often

---

## Question for Future Me

When should I use:
- Enum
- constants module
- simple strings

and what is the tradeoff between flexibility and safety?