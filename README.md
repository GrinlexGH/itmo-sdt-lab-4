# Geometry

A small Python module for calculating the area and perimeter of basic geometric shapes: **Circle**, **Rectangle**, **Square**, and **Triangle**.

## Features

- [x] **Circle:** `Circle.area(r)`, `Circle.perimeter(r)`
- [x] **Rectangle:** `Rectangle.area(a, b)`, `Rectangle.perimeter(a, b)`
- [x] **Square:** `Square.area(a)`, `Square.perimeter(a)`
- [x] **Triangle:** `Triangle.area(a, h)`, `Triangle.perimeter(a, b, c)`

## Quick start

```bash
git clone <repository-url>
cd project
python -c "from geometry import Circle, Rectangle; print(Rectangle.area(3, 4)); print(Circle.area(5))"

# Run tests
python -m unittest -v test_geometry.py
```

### Example usage

```python
from geometry import Circle, Rectangle, Square, Triangle

print("Circle area:", Circle.area(5))
print("Rectangle perimeter:", Rectangle.perimeter(3, 4))
print("Square area:", Square.area(4))
print("Triangle perimeter:", Triangle.perimeter(3, 4, 5))
```

## Documentation

Full class and method reference: [docs/index.md](docs/index.md).

## Change history

- `5e4c80b` Update README.md for tests
- `4e10f5b` Add unit tests
- `98e0f15` Update README.md
- `0be8a5e` Update documentation
- `f22fc2a` Replace rectangle with geometry lib
- `28fe430` Add README.md
- `938fc52` Add documentation
- `dac84b9` Change documentation to doxygen style
- `410988b` Document rectangle API
- `748050e` Add rectangle API

## Author

Temirbekov Maxim Kuanyshbekovich, group M3109
