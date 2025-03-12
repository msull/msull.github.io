Title: Python Format String Specifiers - A Quick Reference Guide
Date: 2025-01-16 12:00
Category: snippets
Tags: python, guides

# Python Format String Specifiers: A Quick Reference Guide

Python provides multiple ways to format strings, with the most common methods being **f-strings** (`f""`) and
the `.format()` method.

## 1. Floating-Point Numbers

### Limit to 2 decimal places

```python
num = 12.34567
print(f"{num:.2f}")  # 12.35
print("{:.2f}".format(num))  # 12.35
```

### Fixed width with padding (10 chars, right-aligned)

```python
print(f"{num:10.2f}")  # '     12.35'
```

### Scientific notation

```python
print(f"{num:.2e}")  # 1.23e+01
```

## 2. Integers

### Basic integer formatting

```python
num = 42
print(f"{num:d}")  # 42
```

### Padding with spaces (width 5, right-aligned)

```python
print(f"{num:5d}")  # '   42'
```

### Padding with zeros (width 5, left-padded with zeros)

```python
print(f"{num:05d}")  # '00042'
```

### Binary, Octal, Hex representations

```python
print(f"{num:b}")  # Binary: 101010
print(f"{num:o}")  # Octal: 52
print(f"{num:x}")  # Hex lowercase: 2a
print(f"{num:X}")  # Hex uppercase: 2A
```

## 3. Strings

### Fixed width with alignment

```python
text = "Hi"
print(f"{text:10}")  # 'Hi        ' (right-aligned)
print(f"{text:<10}")  # 'Hi        ' (left-aligned)
print(f"{text:^10}")  # '    Hi    ' (center-aligned)
```

## 4. Percentages

### Convert to percentage (multiplies by 100 and adds % sign)

```python
fraction = 0.1234
print(f"{fraction:.2%}")  # 12.34%
```

## 5. Thousand Separator

### Use commas to format large numbers

```python
big_num = 1234567890
print(f"{big_num:,}")  # 1,234,567,890
```

### For European-style separators (dot instead of comma)

```python
print(f"{big_num:_}")  # 1_234_567_890
```

## Format Specifiers Cheat Sheet

| Specifier | Example | Description |
|-----------|---------|-------------|
| `:.2f` | `3.1415 → 3.14` | 2 decimal places |
| `:5d` | `42 → '   42'` | Right-align integer in 5 spaces |
| `:05d` | `42 → '00042'` | Zero-padding for width 5 |
| `:.2e` | `12345 → 1.23e+04` | Scientific notation |
| `:b` | `42 → '101010'` | Binary representation |
| `:o` | `42 → '52'` | Octal representation |
| `:x` | `42 → '2a'` | Hex lowercase |
| `:X` | `42 → '2A'` | Hex uppercase |
| `:^10` | `"Hi" → '    Hi    '` | Center align |
| `:<10` | `"Hi" → 'Hi        '` | Left align |
| `:>10` | `"Hi" → '        Hi'` | Right align |
| `:,` | `1234567 → '1,234,567'` | Thousands separator |
| `:.2%` | `0.1234 → '12.34%'` | Convert to percentage |
