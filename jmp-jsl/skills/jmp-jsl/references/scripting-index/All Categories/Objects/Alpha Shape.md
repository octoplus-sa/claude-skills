# Alpha Shape

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Alpha%20Shape.html](https://jsl.jmp.com/All%20Categories/Objects/Alpha%20Shape.html)*

---

# [Alpha Shape](#alpha-shape)[](#alpha-shape "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Alpha Shape](#alpha-shape_1)[](#alpha-shape_1 "Click to copy url")

**Syntax:** ashape = Alpha Shape(Triangulation)

**Description:** Returns the alpha shape for the given triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Get Alpha](#get-alpha)[](#get-alpha "Click to copy url")

**Syntax:** alpha = obj \<\< Get Alpha

**Description:** Returns the current alpha value.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
ashape << Get Alpha();
```

### [Get Edges](#get-edges)[](#get-edges "Click to copy url")

**Syntax:** edges = obj \<\< Get Edges

**Description:** Returns the indices of the edges in the form an Nx2 matrix.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get Edges;
```

### [Get Hull Edges](#get-hull-edges)[](#get-hull-edges "Click to copy url")

**Syntax:** ind = obj \<\< Get Hull Edges

**Description:** Returns the indices of the edges on the boundary of the triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get Hull Edges;
```

### [Get Hull Path](#get-hull-path)[](#get-hull-path "Click to copy url")

**Syntax:** ind = obj \<\< Get Hull Path

**Description:** Returns the boundary of the triangulation as a path.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get Hull Path;
```

### [Get Hull Points](#get-hull-points)[](#get-hull-points "Click to copy url")

**Syntax:** ind = obj \<\< Get Hull Points

**Description:** Returns the indices of the points on the boundary of the triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get Hull Points;
```

### [Get N Edges](#get-n-edges)[](#get-n-edges "Click to copy url")

**Syntax:** nedge = obj \<\< Get N Edges

**Description:** Returns the number of edges in the triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get NEdges;
```

### [Get N Hull Edges](#get-n-hull-edges)[](#get-n-hull-edges "Click to copy url")

**Syntax:** nhull = obj \<\< Get N Hull Edges

**Description:** Returns the number of edges on the boundary of the triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get N Hull Edges;
```

### [Get N Hull Points](#get-n-hull-points)[](#get-n-hull-points "Click to copy url")

**Syntax:** nhull = obj \<\< Get N Hull Points

**Description:** Returns the number of points on the boundary of the triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get N Hull Points;
```

### [Get N Points](#get-n-points)[](#get-n-points "Click to copy url")

**Syntax:** npt = obj \<\< Get N Points

**Description:** Returns the number of unique points in the triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get N Points;
```

### [Get N Triangles](#get-n-triangles)[](#get-n-triangles "Click to copy url")

**Syntax:** ntri = obj \<\< Get N Triangles

**Description:** Returns the number of triangles.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get N Triangles;
```

### [Get Points](#get-points)[](#get-points "Click to copy url")

**Syntax:** {x1,x2} = obj \<\< Get Points

**Description:** Returns the coordinates of the unique points in the triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get Points;
```

### [Get Tri Alpha](#get-tri-alpha)[](#get-tri-alpha "Click to copy url")

**Syntax:** \[alpha1, ...\] = obj \<\< Get Tri Alpha

**Description:** Returns the alpha values for each triangle.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
ashape << Get Tri Alpha();
```

### [Get Triangles](#get-triangles)[](#get-triangles "Click to copy url")

**Syntax:** m = obj \<\< Get Triangles

**Description:** Returns the indices of the triangles in the form of an Nx3 matrix.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get Triangles;
```

### [Get Y](#get-y)[](#get-y "Click to copy url")

**Syntax:** y = obj \<\< Get Y

**Description:** Returns the Y values of the unique points in the triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
tri << Get Y;
```

### [Peel](#peel)[](#peel "Click to copy url")

**Syntax:** tri = obj \<\< Peel

**Description:** Peel the boundary layer of a triangulation, returning a new triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
Show( tri << Get N Triangles );
tri2 = tri << Peel;
Show( tri2 << Get N Triangles );
```

### [Set Alpha](#set-alpha)[](#set-alpha "Click to copy url")

**Syntax:** obj \<\< Set Alpha( alpha )

**Description:** Sets the current alpha value and recomputes the triangulation.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
ashape << Set Alpha( 0.5 );
```

### [Subset](#subset)[](#subset "Click to copy url")

**Syntax:** tri = obj \<\< Subset( {indices} )

**Description:** Returns a triangulation resulting from the given subset of points.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
triang = Triangulation( X( :X, :Y ), Y( :POP ) );
ashape = tri = Alpha Shape( triang );
Show( tri << Get N Triangles );
tri2 = tri << Subset( tri << Get Hull Points );
Show( tri2 << Get N Triangles );
```

[ Previous](Add-In.html "Add-In") [Next ](Association%20Analysis.html "Association Analysis")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
