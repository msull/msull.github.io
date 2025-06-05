Title: Python List Comprehensions Reference
Date: 2025-01-16 12:00
Category: snippets
Tags: python, guides

## Python List Comprehensions Reference

List comprehensions provide a concise way to create lists in Python. Here are some practical examples:

### 1. Basic List Comprehension
```python
# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Convert temperatures (Celsius to Fahrenheit)
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

### 2. Filtering with Comprehensions
```python
# Get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]
```

### 3. Nested List Comprehension
```python
# Create a matrix
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

### 4. String Manipulation
```python
# Convert words to uppercase
words = ['hello', 'world', 'python']
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # ['HELLO', 'WORLD', 'PYTHON']
```

### Key Takeaways
- List comprehensions offer a compact syntax for list creation
- They can include filtering conditions
- They can transform elements during creation
- They can be nested for more complex operations
