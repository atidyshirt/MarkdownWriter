# MarkdownWriter

A little module to write markdown output from python code

**Example of use**

```python
  poly1 = create_polygon()
  poly2 = create_polygon()
  cont = poly1.checkContiguity(poly2)
  md = MarkdownWriter("./out.md")
  md.clear()
  md.header1("First triange")
  md.bold("Triange consists of the following lines:")
  md.math(f"{poly1.lines[0]}, {poly1.lines[1]}, {poly1.lines[2]}")
  md.header1("Second triange")
  md.bold("Triange consists of the following lines:")
  md.math(f"{poly2.lines[0]}, {poly2.lines[1]}, {poly2.lines[2]}")
  if cont:
      md.header2(f"Result: The two triangles are contigutious along the line {cont}")
  else:
      print(f"Result: The two triangles are not contigutious on any line")
```

> Generated output

```md
# First triange

**Triange consists of the following lines:**

$$ from point (1, 3) to point (3, 4), from point (3, 4) to point (4, 5), from point (4, 5) to point (1, 3) $$

# Second triange

**Triange consists of the following lines:**

$$ from point (1, 3) to point (3, 4), from point (3, 4) to point (5, 6), from point (5, 6) to point (1, 3) $$

## Result: The two triangles are contigutious along the line from point (1, 3) to point (3, 4)
```
