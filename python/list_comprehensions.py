posts = [
    {"id": 1, "title": "Post 1"},
    {"id": 2, "title": "Post 2"},
    {"id": 3, "title": "Post 3"},
]


post_ids = [post["id"] for post in posts]
print (post_ids)

# Filtering
numbers = [1, 2, 3, 4, 5]

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Nested comprehensions
result = [(i, j)
          for i in range(3)
          for j in range(2)]

print(result)

responses = [
    [
        {"id": 1},
        {"id": 2}
    ],
    [
        {"id": 3},
        {"id": 4}
    ]
]

ids = [post["id"] for response in responses for post in response]
print(ids)