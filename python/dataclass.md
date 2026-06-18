# dataclass

Status: 🟡 Learning

## What is it?

A decorator that automatically generates common methods for data-centric classes:

- `__init__`
- `__repr__`
- `__eq__`

It helps reduce boilerplate code and makes classes easier to read and maintain.

## When to use

- API response models
- Test data objects
- Configuration objects
- DTOs (Data Transfer Objects)

## Example

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
```

## Where did I use it?

### API response models

Convert API responses into typed Python objects instead of working with dictionaries.

### Test data

Use dataclass models together with Factory classes to generate test data.

## Benefits

- Less boilerplate code
- Better readability
- IDE autocompletion
- Easier object comparison in tests
- Clear data structure

## Things I can forget

### `frozen=True`

Makes instances immutable.

```python
@dataclass(frozen=True)
class User:
    id: int
    name: str
```

### `field(default_factory=...)`

Avoid mutable default values.

❌ Bad:

```python
@dataclass
class User:
    tags: list = []
```

All instances will share the same list.

✅ Good:

```python
from dataclasses import dataclass, field

@dataclass
class User:
    tags: list = field(default_factory=list)
```

### Dataclass vs Regular Class

**Dataclass**
- Primarily stores data
- Less boilerplate
- Auto-generated methods

**Regular Class**
- Contains business logic and behavior
- More control over implementation

### Dataclass vs Pydantic

**Dataclass**
- Stores data
- No runtime validation

**Pydantic**
- Validates and parses data
- Useful for API requests/responses and configuration

## Rules of Thumb

Use a dataclass when:
- The structure is known in advance
- The object mainly stores data

Use a dictionary when:
- The structure is dynamic
- Data is temporary and used only once

## Question for Future Me

When should I choose:
- a dictionary?
- a dataclass?
- a Pydantic model?