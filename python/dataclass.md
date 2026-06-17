# dataclass

Status: 🟡 Learning

## What is it
A decorator that automatically generates common methods such as:
- __init__
- __repr__
- __eq__

for classes that primarily store data.

## When to use
- API response models
- Test data objects
- Configuration objects

## Example

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str

## Where did I use it?

- Created response models and converted API responses into those models.
- Used models in Factory classes for generating test data.

## Benefits

- Less boilerplate code
- Better readability
- IDE autocompletion
- Easier object comparison in tests

## Things I can forget

- frozen=True
- field(default_factory=...)
- Difference between dataclass and regular class
- Difference between dataclass and Pydantic

## Question for future me

When should I use a dataclass and when is a simple dictionary enough?