# Geometry: Documentation

> A small library for calculating the area and perimeter of basic geometric shapes.

## Table of contents

1. [Overview](#overview)
2. [Class reference](#class-reference)
   - [Circle](#circle)
   - [Rectangle](#rectangle)
   - [Square](#square)
   - [Triangle](#triangle)

## Overview

The `geometry.py` module provides four classes (`Circle`, `Rectangle`, `Square`, and `Triangle`) with static methods for calculating their **area** and **perimeter**.

| Class       | Method               | Returns   | Formula       |
|-------------|----------------------|-----------|---------------|
| `Circle`    | `area(r)`            | area      | `π * r²`      |
| `Circle`    | `perimeter(r)`       | perimeter | `2 * π * r`   |
| `Rectangle` | `area(a, b)`         | area      | `a * b`       |
| `Rectangle` | `perimeter(a, b)`    | perimeter | `2 * (a + b)` |
| `Square`    | `area(a)`            | area      | `a²`          |
| `Square`    | `perimeter(a)`       | perimeter | `4 * a`       |
| `Triangle`  | `area(a, h)`         | area      | `a * h / 2`   |
| `Triangle`  | `perimeter(a, b, c)` | perimeter | `a + b + c`   |

## Class reference

### `Circle`

Provides geometric calculations for a circle.

#### `Circle.area(r)`

Calculates the area of a circle.

**Parameters**

- `r`: radius of the circle

**Returns:** `math.pi * r * r`

**Example**

```python
from geometry import Circle

print(Circle.area(5))  # 78.53981633974483
```

#### `Circle.perimeter(r)`

Calculates the perimeter (circumference) of a circle.

**Parameters**

- `r`: radius of the circle

**Returns:** `2 * math.pi * r`

**Example**

```python
from geometry import Circle

print(Circle.perimeter(5))  # 31.41592653589793
```

---

### `Rectangle`

Provides geometric calculations for a rectangle.

#### `Rectangle.area(a, b)`

Calculates the area of a rectangle.

**Parameters**

- `a`: length of one side
- `b`: length of the adjacent side

**Returns:** `a * b`

**Example**

```python
from geometry import Rectangle

print(Rectangle.area(3, 4))  # 12
```

#### `Rectangle.perimeter(a, b)`

Calculates the perimeter of a rectangle.

**Parameters**

- `a`: length of one side
- `b`: length of the adjacent side

**Returns:** `2 * (a + b)`

**Example**

```python
from geometry import Rectangle

print(Rectangle.perimeter(3, 4))  # 14
```

---

### `Square`

Provides geometric calculations for a square.

#### `Square.area(a)`

Calculates the area of a square.

**Parameters**

- `a`: side length of the square

**Returns:** `a * a`

**Example**

```python
from geometry import Square

print(Square.area(4))  # 16
```

#### `Square.perimeter(a)`

Calculates the perimeter of a square.

**Parameters**

- `a`: side length of the square

**Returns:** `4 * a`

**Example**

```python
from geometry import Square

print(Square.perimeter(4))  # 16
```

---

### `Triangle`

Provides geometric calculations for a triangle.

#### `Triangle.area(a, h)`

Calculates the area of a triangle.

**Parameters**

- `a`: base length of the triangle
- `h`: height of the triangle

**Returns:** `a * h / 2`

**Example**

```python
from geometry import Triangle

print(Triangle.area(6, 4))  # 12.0
```

#### `Triangle.perimeter(a, b, c)`

Calculates the perimeter of a triangle.

**Parameters**

- `a`: length of the first side
- `b`: length of the second side
- `c`: length of the third side

**Returns:** `a + b + c`

**Example**

```python
from geometry import Triangle

print(Triangle.perimeter(3, 4, 5))  # 12
```
