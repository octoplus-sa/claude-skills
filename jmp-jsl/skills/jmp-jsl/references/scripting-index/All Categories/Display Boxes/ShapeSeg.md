# ShapeSeg

*Source: [https://jsl.jmp.com/All%20Categories/Display%20Boxes/ShapeSeg.html](https://jsl.jmp.com/All%20Categories/Display%20Boxes/ShapeSeg.html)*

---

# [ShapeSeg](#shapeseg)[](#shapeseg "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Shape Seg](#shape-seg)[](#shape-seg "Click to copy url")

**Syntax:** ss = Shape Seg( {Path(\<path\>), ...}, \< Row States( dt \| dt,\[rows\] \| dt,{{rows}, ...} \| {states} ) \> )

**Description:** Returns a display seg with a collection of shapes. Each shape draws a stroke along the given path if fill is 0, or paints the interior of the given path if fill is not 0. The path can be specified with an N x 3 matrix or with a text representation. A path matrix has three columns for x, y, and flags for each point in the path. The flag values are 0 for control, 1 for move, 2 for line segment, 3 for cubic Bézier segment, and are negative if the point also closes the path. Path text supports SVG syntax.

**Example 1**

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
```

**Example 2**

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )},
            Row States( {Selected State( 1 ), Color State( "red" )} )
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Child](#child)[](#child "Click to copy url")

**Syntax:** seg2 = obj \<\< Child

**Description:** Returns the first child of the display seg.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Child; // not many segs support children
```

### [Class Name](#class-name)[](#class-name "Click to copy url")

**Syntax:** classname = obj \<\< Class Name

**Description:** Returns the name of the display class for the display seg.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Class Name;
```

### [Clip Shape](#clip-shape)[](#clip-shape "Click to copy url")

**Syntax:** seg \<\< Clip Shape(Boundaries(Shape File, \[ID(string)\]) \| Path(\[string\] \| \[matrix\]) \| Empty())

**Description:** Clips the geometry by the given shape. The shape can be specified using a shape file or a path. An optional ID can be specified with a shape file to select a single shape from the file, otherwise the union of all shapes is used as the clipping region. A clipping path can be specified with an N x 3 matrix or with a text representation. A path matrix has three columns for x, y, and flags for each point in the path. The flag values are 0 for control, 1 for move, 2 for line segment, 3 for cubic Bézier segment, and are negative if the point also closes the path. Path text supports SVG syntax.

**JMP Version Added:** 14

``` jsl
Open( "$SAMPLE_DATA/Cities.jmp" );
gb = Graph Builder(
    Size( 653, 396 ),
    Show Control Panel( 0 ),
    Variables( X( :Longitude ), Y( :Latitude ) ),
    Elements( Contour( X, Y, Legend( 2 ) ) ),
    SendToReport(
        Dispatch( {}, "Graph Builder", FrameBox,
            {Background Map( Boundaries( "US States" ) ), Grid Line Order( 2 ),
            Reference Line Order( 3 )}
        )
    )
);
cs = (gb << Report)[FrameBox( 1 )] << Find Seg( Contour Seg( 1 ) );
Wait( 2 );
cs << Clip Shape( Boundaries( "US States" ) );
```

### [Color](#color)[](#color "Click to copy url")

**Syntax:** obj \<\< Color( color )

**Description:** Sets the color for all shapes.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Color( "Green" );
```

### [Color Theme](#color-theme)[](#color-theme "Click to copy url")

**Syntax:** obj \<\< Color Theme

### [Delete](#delete)[](#delete "Click to copy url")

**Syntax:** obj \<\< Delete

**Description:** Delete the display seg.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Delete;
```

### [Density Gradient](#density-gradient)[](#density-gradient "Click to copy url")

**Syntax:** obj \<\< Density Gradient( "Fade to White"\|"Fade To Gray"\|"Full Color"="Fade to White" )

**Description:** Sets the coloring behavior of density gradients. "Fade to White" by default.

**JMP Version Added:** 15

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Density Gradient( "Fade to Gray" );
```

### [Fill Color](#fill-color)[](#fill-color "Click to copy url")

**Syntax:** obj \<\< Fill Color( color )

**Description:** Sets the fill color for all shapes.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Fill Color( "Green" );
```

### [Frame](#frame)[](#frame "Click to copy url")

**Syntax:** FrameBox = obj \<\< Frame

**Description:** Returns the frame box that the display seg is in.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Frame;
```

### [Get Clip Shape](#get-clip-shape)[](#get-clip-shape "Click to copy url")

**Syntax:** obj \<\< Get Clip Shape

**Description:** Returns the current clipping shape

**JMP Version Added:** 14

``` jsl
Open( "$SAMPLE_DATA/Cities.jmp" );
gb = Graph Builder(
    Size( 653, 396 ),
    Show Control Panel( 0 ),
    Variables( X( :Longitude ), Y( :Latitude ) ),
    Elements( Contour( X, Y, Legend( 2 ) ) ),
    SendToReport(
        Dispatch( {}, "Graph Builder", FrameBox,
            {Background Map( Boundaries( "US States" ) ), Grid Line Order( 2 ),
            Reference Line Order( 3 )}
        )
    )
);
cs = (gb << Report)[FrameBox( 1 )] << Find Seg( Contour Seg( 1 ) );
cs << Clip Shape( Boundaries( "US States" ) );
Wait( 2 );
cs << Get Clip Shape();
```

### [Get Color](#get-color)[](#get-color "Click to copy url")

**Syntax:** color = obj \<\< Get Color

**Description:** Returns the shape color.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Color;
```

### [Get Density Gradient](#get-density-gradient)[](#get-density-gradient "Click to copy url")

**Syntax:** obj \<\< Get Density Gradient

**Description:** Gets the coloring behavior of density gradients.

**JMP Version Added:** 15

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Density Gradient;
```

### [Get Description](#get-description)[](#get-description "Click to copy url")

**Syntax:** description = obj \<\< Get Description

**Description:** Gets the description for the display seg.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << get description();
```

### [Get Fill Color](#get-fill-color)[](#get-fill-color "Click to copy url")

**Syntax:** obj \<\< Get Fill Color

**Description:** Returns the fill color of the shapes.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Fill Color;
```

### [Get Fill Pattern](#get-fill-pattern)[](#get-fill-pattern "Click to copy url")

**Syntax:** obj \<\< Get Fill Pattern

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Fill Pattern;
```

### [Get Gradient](#get-gradient)[](#get-gradient "Click to copy url")

**Syntax:** obj \<\< Get Gradient

**Description:** Gets the coloring gradient.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient;
```

### [Get Gradient Color Theme](#get-gradient-color-theme)[](#get-gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Get Gradient Color Theme

**Description:** Gets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Color Theme;
```

### [Get Gradient Discrete Colors](#get-gradient-discrete-colors)[](#get-gradient-discrete-colors "Click to copy url")

**Syntax:** obj \<\< Get Gradient Discrete Colors

**Description:** Gets if each level in a gradient should be a single color or if colors should transition smoothly.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Discrete Colors;
```

### [Get Gradient Fill](#get-gradient-fill)[](#get-gradient-fill "Click to copy url")

**Syntax:** obj \<\< Get Gradient Fill

**Description:** Gets the coloring behavior for values outside of the range of the gradient's scale.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Get Gradient Fill;
```

### [Get Gradient Label Count](#get-gradient-label-count)[](#get-gradient-label-count "Click to copy url")

**Syntax:** obj \<\< Get Gradient Label Count

**Description:** Gets the number of labels in a gradient's legend.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Label Count;
```

### [Get Gradient Label Levels](#get-gradient-label-levels)[](#get-gradient-label-levels "Click to copy url")

**Syntax:** \[value1,value1, ... value N\] = obj \<\< Get Gradient Label Levels

**Description:** Gets the set of values used for labels in the gradient's scale.

**JMP Version Added:** 18

**Example 1**

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Get Gradient Scale Values;
```

**Example 2**

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Scale Values( [-10.0, 0.0, 100] );
seg << Get Gradient Scale Values;
```

### [Get Gradient Legend Horizontal](#get-gradient-legend-horizontal)[](#get-gradient-legend-horizontal "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Horizontal

**Description:** Gets if the gradient's legend should be drawn horizontally.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Legend Horizontal;
```

### [Get Gradient Legend Label Format](#get-gradient-legend-label-format)[](#get-gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Label Format

**Description:** Gets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Legend Label Format;
```

### [Get Gradient Legend Label Width](#get-gradient-legend-label-width)[](#get-gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Label Width

**Description:** Gets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Legend Label Width;
```

### [Get Gradient Legend Show Labels](#get-gradient-legend-show-labels)[](#get-gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Show Labels

**Description:** Gets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Legend Show Labels;
```

### [Get Gradient Level Count](#get-gradient-level-count)[](#get-gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Get Gradient Level Count

**Description:** Gets the number of levels in a gradient.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Levels;
```

### [Get Gradient Lightness Range](#get-gradient-lightness-range)[](#get-gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Get Gradient Lightness Range

**Description:** Gets the minimum and maximum lightness for level colors in a gradient. Missing values indicate that the color theme's original value is used.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Lightness Range;
```

### [Get Gradient Range](#get-gradient-range)[](#get-gradient-range "Click to copy url")

**Syntax:** obj \<\< Get Gradient Range

**Description:** Gets the range over which non-custom gradient scales are generated.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Get Gradient Range;
```

### [Get Gradient Reverse Color Order](#get-gradient-reverse-color-order)[](#get-gradient-reverse-color-order "Click to copy url")

**Syntax:** obj \<\< Get Gradient Reverse Color Order

**Description:** Gets if the order of colors in a gradient is reversed.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Reverse Color Order;
```

### [Get Gradient Reverse Label Order](#get-gradient-reverse-label-order)[](#get-gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Get Gradient Reverse Label Order

**Description:** Gets if the order of labels in a gradient is reversed.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Reverse Label Order;
```

### [Get Gradient Scale](#get-gradient-scale)[](#get-gradient-scale "Click to copy url")

**Syntax:** obj \<\< Get Gradient Scale

**Description:** Gets the gradient scale type.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Get Gradient Scale;
```

### [Get Gradient Scale Values](#get-gradient-scale-values)[](#get-gradient-scale-values "Click to copy url")

**Syntax:** \[value1,value1, ... value N\] = obj \<\< Get Gradient Scale Values

**Description:** Gets the set of values used for labels in the gradient's scale.

**JMP Version Added:** 18

**Example 1**

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Get Gradient Scale Values;
```

**Example 2**

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Scale Values( [-10.0, 0.0, 100] );
seg << Get Gradient Scale Values;
```

### [Get Gradient Show Missing](#get-gradient-show-missing)[](#get-gradient-show-missing "Click to copy url")

**Syntax:** obj \<\< Get Gradient Show Missing

**Description:** Gets when to show the legend entry for missing values.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Show Missing;
```

### [Get Gradient Transparency](#get-gradient-transparency)[](#get-gradient-transparency "Click to copy url")

**Syntax:** obj \<\< Get Gradient Transparency

**Description:** Gets the transparency behavior of gradients.

**JMP Version Added:** 15

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Gradient Transparency;
```

### [Get Line Style](#get-line-style)[](#get-line-style "Click to copy url")

**Syntax:** pen style = obj \<\< Get Line Style

**Description:** Returns the style of the lines.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Line Style;
```

### [Get Line Width](#get-line-width)[](#get-line-width "Click to copy url")

**Syntax:** number = obj \<\< Get Line Width

**Description:** Returns the width of the lines.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Line Width;
```

### [Get Transparency](#get-transparency)[](#get-transparency "Click to copy url")

**Syntax:** obj \<\< Get Transparency

**Description:** Returns a numeric value representing transparency between 0 and 1.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Get Transparency;
```

### [Gradient](#gradient)[](#gradient "Click to copy url")

**Syntax:** obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<Contour Levels(num)\>, \<Reverse Gradient(0\|1)\>, \<Density Gradient("Fade To White"\|"Fade To Gray"\|"Full Color")\>, \<Gradient Transparency("None"\|"Linear")\> } obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<N Labels(num)\>, \<Show Missing Color("On"\|"Off"\|"Auto")\>, \<Scale Type("Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom")\>, \<Scale Values(\[v1, v2, …\])\>, \<Range Type("Default"\|"Exact Data Range"\|"Middle 90%")\>, \<Fill("Between"\|"Above"\|"Below"\|"Above Below")\>, \<Reverse Gradient(0\|1)\>, \<Reverse Labels(0\|1)\>, \<Discrete Color(0\|1)\> }, \<Label Format(labelFormat)\>, \<Width(num)\>, \<Horizontal(0\|1)\>, \<Show Labels(0\|1)\>

**Description:** Sets the coloring gradient.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient( {Color Theme( "Viridis" ), N Labels( 7 )} );
```

### [Gradient Color Theme](#gradient-color-theme)[](#gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Gradient Color Theme

**Description:** Sets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Color Theme( "Viridis" );
```

### [Gradient Discrete Colors](#gradient-discrete-colors)[](#gradient-discrete-colors "Click to copy url")

**Syntax:** obj \<\< Gradient Discrete Colors

**Description:** Sets if each level in a gradient should be a single color or if colors should transition smoothly.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Points( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Marker Seg( 1 ) );
seg << Set Gradient Discrete Colors( 1 );
```

### [Gradient Fill](#gradient-fill)[](#gradient-fill "Click to copy url")

**Syntax:** obj \<\< Gradient Fill( "Between"\|"Above"\|"Below"\|"Above Below"="Above Below" )

**Description:** Sets the coloring behavior for values outside of the range of the gradient's scale. "Above Below" by default.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Range( "Middle 90%" );
seg << Set Gradient Fill( "Between" );
```

### [Gradient Label Count](#gradient-label-count)[](#gradient-label-count "Click to copy url")

**Syntax:** obj \<\< Gradient Label Count

**Description:** Sets the number of labels in a gradient's legend. This is one more than the number of contour levels.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Label Count( 8 );
```

### [Gradient Label Levels](#gradient-label-levels)[](#gradient-label-levels "Click to copy url")

**Syntax:** obj \<\< Gradient Label Levels( \[value1,value1, ... value N\] )

**Description:** Sets a custom set of values for use in the gradient's scale.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Scale Values( [-10.0, 0.0, 10.0] );
```

### [Gradient Legend Horizontal](#gradient-legend-horizontal)[](#gradient-legend-horizontal "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Horizontal

**Description:** Sets if the gradient's legend should be drawn horizontally.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Legend Horizontal( 1 );
```

### [Gradient Legend Label Format](#gradient-legend-label-format)[](#gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Label Format

**Description:** Sets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Legend Label Format( "Fixed Dec", 6, 3 );
```

### [Gradient Legend Label Width](#gradient-legend-label-width)[](#gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Label Width

**Description:** Sets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Legend Label Width( 4 );
```

### [Gradient Legend Show Labels](#gradient-legend-show-labels)[](#gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Show Labels

**Description:** Sets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Legend Show Labels( 0 );
```

### [Gradient Level Count](#gradient-level-count)[](#gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Gradient Level Count

**Description:** Sets the number of levels in a gradient. This is one less than the number of labels.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Levels( 7 );
```

### [Gradient Lightness Range](#gradient-lightness-range)[](#gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Gradient Lightness Range

**Description:** Sets the minimum and maximum lightness for level colors in a gradient. The colors will be scaled to cover this range. A missing value is treated as no change.

**JMP Version Added:** 18

**Example 1**

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Lightness Range( Min( 0.25 ), Max( 0.75 ) );
```

**Example 2**

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Lightness Range( 0.25, 0.75 );
```

**Example 3**

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Lightness Range( ., 0.75 );
```

### [Gradient Range](#gradient-range)[](#gradient-range "Click to copy url")

**Syntax:** obj \<\< Gradient Range( "Default"\|"Exact Data Range"\|"Middle 90%"="Default" )

**Description:** Sets the range over which non-custom gradient scales are generated. "Default" by default.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Range( "Exact Data Range" );
```

### [Gradient Reverse Color Order](#gradient-reverse-color-order)[](#gradient-reverse-color-order "Click to copy url")

**Syntax:** obj \<\< Gradient Reverse Color Order

**Description:** Reverses the order of the colors in a gradient.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Reverse Color Order( 1 );
```

### [Gradient Reverse Label Order](#gradient-reverse-label-order)[](#gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Gradient Reverse Label Order

**Description:** Reverses the order of the labels in a gradient.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Reverse Label Order( 1 );
```

### [Gradient Scale](#gradient-scale)[](#gradient-scale "Click to copy url")

**Syntax:** obj \<\< Gradient Scale( "Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom"="Linear" )

**Description:** Sets the gradient scale type. "Linear" by default.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Scale( "Quantile" );
```

### [Gradient Scale Values](#gradient-scale-values)[](#gradient-scale-values "Click to copy url")

**Syntax:** obj \<\< Gradient Scale Values( \[value1,value1, ... value N\] )

**Description:** Sets a custom set of values for use in the gradient's scale.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Scale Values( [-10.0, 0.0, 10.0] );
```

### [Gradient Show Missing](#gradient-show-missing)[](#gradient-show-missing "Click to copy url")

**Syntax:** obj \<\< Gradient Show Missing( "Auto"\|"On"\|"Off"="Auto" )

**Description:** Sets when to show the legend entry for missing values. "Auto" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$Sample_Data/Cities.jmp" );
gb = Graph Builder(
    Variables( X( :city ), Y( :POP ), Color( :NO ) ),
    Elements( Bar( X, Y ) )
);
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Bar Seg( 1 ) );
seg << Set Gradient Show Missing( "Off" );
```

### [Gradient Transparency](#gradient-transparency)[](#gradient-transparency "Click to copy url")

**Syntax:** obj \<\< Gradient Transparency( "None"\|"Linear"="Linear" )

**Description:** Sets the transparency behavior of gradients. "Linear" by default.

**JMP Version Added:** 15

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Gradient Transparency( "None" );
```

### [Line Style](#line-style)[](#line-style "Click to copy url")

**Syntax:** obj \<\< Line Style( pen style )

**Description:** Sets the style of the lines. Options are Solid, Dotted, Dashed, DashDot, and DashDotDot.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Line Style( "Dotted" );
```

### [Line Width](#line-width)[](#line-width "Click to copy url")

**Syntax:** obj \<\< Line Width( "1"\|"2"\|"3"\|"4"\|"5"\|"6"\|"Other..." )

**Description:** Sets the width of the lines.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Line Width( 3 );
```

### [Parent](#parent)[](#parent "Click to copy url")

**Syntax:** seg2 = obj \<\< Parent

**Description:** Returns the parent of the display seg.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Parent;
```

### [Revert](#revert)[](#revert "Click to copy url")

**Syntax:** obj \<\< Revert

**Description:** Changes the seg back to its original state.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
Wait( 1 );
seg << Set Color( "Red" );
Wait( 1 );
seg << Revert;
```

### [Set Color](#set-color)[](#set-color "Click to copy url")

**Syntax:** obj \<\< Set Color( color )

**Description:** Sets the color for all shapes.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Color( "Green" );
```

### [Set Description](#set-description)[](#set-description "Click to copy url")

**Syntax:** obj \<\< Set Description( description )

**Description:** Sets the description for the display seg.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << set description( "my seg" );
```

### [Set Fill Color](#set-fill-color)[](#set-fill-color "Click to copy url")

**Syntax:** obj \<\< Set Fill Color( color )

**Description:** Sets the fill color for all shapes.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Fill Color( "Green" );
```

### [Set Fill Pattern](#set-fill-pattern)[](#set-fill-pattern "Click to copy url")

**Syntax:** obj \<\< Set Fill Pattern

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Fill Color( "Blue" );
seg << Set Fill Pattern( "h wave medium" );
```

### [Set Gradient](#set-gradient)[](#set-gradient "Click to copy url")

**Syntax:** obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<Contour Levels(num)\>, \<Reverse Gradient(0\|1)\>, \<Density Gradient("Fade To White"\|"Fade To Gray"\|"Full Color")\>, \<Gradient Transparency("None"\|"Linear")\> } obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<N Labels(num)\>, \<Show Missing Color("On"\|"Off"\|"Auto")\>, \<Scale Type("Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom")\>, \<Scale Values(\[v1, v2, …\])\>, \<Range Type("Default"\|"Exact Data Range"\|"Middle 90%")\>, \<Fill("Between"\|"Above"\|"Below"\|"Above Below")\>, \<Reverse Gradient(0\|1)\>, \<Reverse Labels(0\|1)\>, \<Discrete Color(0\|1)\> }, \<Label Format(labelFormat)\>, \<Width(num)\>, \<Horizontal(0\|1)\>, \<Show Labels(0\|1)\>

**Description:** Sets the coloring gradient.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient( {Color Theme( "Viridis" ), N Labels( 7 )} );
```

### [Set Gradient Color Theme](#set-gradient-color-theme)[](#set-gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Set Gradient Color Theme

**Description:** Sets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Color Theme( "Viridis" );
```

### [Set Gradient Custom Scale](#set-gradient-custom-scale)[](#set-gradient-custom-scale "Click to copy url")

**Syntax:** obj \<\< Set Gradient Custom Scale

**Description:** Sets the gradient to use a list of values for a custom scale.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Custom Scale( {0.0, 5.0, 10.0, 20.0} );
```

### [Set Gradient Discrete Colors](#set-gradient-discrete-colors)[](#set-gradient-discrete-colors "Click to copy url")

**Syntax:** obj \<\< Set Gradient Discrete Colors

**Description:** Sets if each level in a gradient should be a single color or if colors should transition smoothly.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Points( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Marker Seg( 1 ) );
seg << Set Gradient Discrete Colors( 1 );
```

### [Set Gradient Fill](#set-gradient-fill)[](#set-gradient-fill "Click to copy url")

**Syntax:** obj \<\< Set Gradient Fill( "Between"\|"Above"\|"Below"\|"Above Below"="Above Below" )

**Description:** Sets the coloring behavior for values outside of the range of the gradient's scale. "Above Below" by default.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Range( "Middle 90%" );
seg << Set Gradient Fill( "Between" );
```

### [Set Gradient Label Count](#set-gradient-label-count)[](#set-gradient-label-count "Click to copy url")

**Syntax:** obj \<\< Set Gradient Label Count

**Description:** Sets the number of labels in a gradient's legend. This is one more than the number of contour levels.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Label Count( 8 );
```

### [Set Gradient Label Levels](#set-gradient-label-levels)[](#set-gradient-label-levels "Click to copy url")

**Syntax:** obj \<\< Set Gradient Label Levels( \[value1,value1, ... value N\] )

**Description:** Sets a custom set of values for use in the gradient's scale.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Scale Values( [-10.0, 0.0, 10.0] );
```

### [Set Gradient Legend Horizontal](#set-gradient-legend-horizontal)[](#set-gradient-legend-horizontal "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Horizontal

**Description:** Sets if the gradient's legend should be drawn horizontally.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Legend Horizontal( 1 );
```

### [Set Gradient Legend Label Format](#set-gradient-legend-label-format)[](#set-gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Label Format

**Description:** Sets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Legend Label Format( "Fixed Dec", 6, 3 );
```

### [Set Gradient Legend Label Width](#set-gradient-legend-label-width)[](#set-gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Label Width

**Description:** Sets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Legend Label Width( 4 );
```

### [Set Gradient Legend Show Labels](#set-gradient-legend-show-labels)[](#set-gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Show Labels

**Description:** Sets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Legend Show Labels( 0 );
```

### [Set Gradient Level Count](#set-gradient-level-count)[](#set-gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Set Gradient Level Count

**Description:** Sets the number of levels in a gradient. This is one less than the number of labels.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Levels( 7 );
```

### [Set Gradient Lightness Range](#set-gradient-lightness-range)[](#set-gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Set Gradient Lightness Range

**Description:** Sets the minimum and maximum lightness for level colors in a gradient. The colors will be scaled to cover this range. A missing value is treated as no change.

**JMP Version Added:** 18

**Example 1**

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Lightness Range( Min( 0.25 ), Max( 0.75 ) );
```

**Example 2**

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Lightness Range( 0.25, 0.75 );
```

**Example 3**

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Lightness Range( ., 0.75 );
```

### [Set Gradient Range](#set-gradient-range)[](#set-gradient-range "Click to copy url")

**Syntax:** obj \<\< Set Gradient Range( "Default"\|"Exact Data Range"\|"Middle 90%"="Default" )

**Description:** Sets the range over which non-custom gradient scales are generated. "Default" by default.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Range( "Exact Data Range" );
```

### [Set Gradient Reverse Color Order](#set-gradient-reverse-color-order)[](#set-gradient-reverse-color-order "Click to copy url")

**Syntax:** obj \<\< Set Gradient Reverse Color Order

**Description:** Reverses the order of the colors in a gradient.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Reverse Color Order( 1 );
```

### [Set Gradient Reverse Label Order](#set-gradient-reverse-label-order)[](#set-gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Set Gradient Reverse Label Order

**Description:** Reverses the order of the labels in a gradient.

**JMP Version Added:** 18

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Gradient Reverse Label Order( 1 );
```

### [Set Gradient Scale](#set-gradient-scale)[](#set-gradient-scale "Click to copy url")

**Syntax:** obj \<\< Set Gradient Scale( "Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom"="Linear" )

**Description:** Sets the gradient scale type. "Linear" by default.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Scale( "Quantile" );
```

### [Set Gradient Scale Values](#set-gradient-scale-values)[](#set-gradient-scale-values "Click to copy url")

**Syntax:** obj \<\< Set Gradient Scale Values( \[value1,value1, ... value N\] )

**Description:** Sets a custom set of values for use in the gradient's scale.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Little Pond.jmp" );
gb = Graph Builder( Variables( X( :X ), Y( :Y ), Color( :Z ) ), Elements( Contour( X, Y ) ) );
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Contour Seg( 1 ) );
seg << Set Gradient Scale Values( [-10.0, 0.0, 10.0] );
```

### [Set Gradient Show Missing](#set-gradient-show-missing)[](#set-gradient-show-missing "Click to copy url")

**Syntax:** obj \<\< Set Gradient Show Missing( "Auto"\|"On"\|"Off"="Auto" )

**Description:** Sets when to show the legend entry for missing values. "Auto" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$Sample_Data/Cities.jmp" );
gb = Graph Builder(
    Variables( X( :city ), Y( :POP ), Color( :NO ) ),
    Elements( Bar( X, Y ) )
);
frame = (gb << Report)[FrameBox( 1 )];
seg = frame << Find Seg( Bar Seg( 1 ) );
seg << Set Gradient Show Missing( "Off" );
```

### [Set Label Offset](#set-label-offset)[](#set-label-offset "Click to copy url")

**Syntax:** obj \<\< Set Label Offset {Index, Longitude, Latitude}, ...

**Description:** Positions row labels according to the given coordinates.

**JMP Version Added:** 16

### [Set Line Style](#set-line-style)[](#set-line-style "Click to copy url")

**Syntax:** obj \<\< Set Line Style( pen style )

**Description:** Sets the style of the lines. Options are Solid, Dotted, Dashed, DashDot, and DashDotDot.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Line Style( "Dotted" );
```

### [Set Line Width](#set-line-width)[](#set-line-width "Click to copy url")

**Syntax:** obj \<\< Set Line Width( "1"\|"2"\|"3"\|"4"\|"5"\|"6"\|"Other..." )

**Description:** Sets the width of the lines.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Line Width( 3 );
```

### [Set Transparency](#set-transparency)[](#set-transparency "Click to copy url")

**Syntax:** obj \<\< Set Transparency( number )

**Description:** Sets the shape transparency. The argument should be a numeric value between 0 and 1.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Transparency( .3 );
```

### [Sib](#sib)[](#sib "Click to copy url")

**Syntax:** seg2 = obj \<\< Sib

**Description:** Returns the sibling of the display seg.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Sib;
```

### [Sib Append](#sib-append)[](#sib-append "Click to copy url")

**Syntax:** obj \<\< Sib Append( seg2 )

**Description:** Adds a display seg immediately after the display seg.

``` jsl
win = New Window( "World",
    gb = Graph(
        FrameSize( 800, 400 ),
        X Scale( -180, 180 ),
        Y Scale( -90, 90 ),
        <<Background Map( Images( "Simple Earth" ) )
    )
);
imgBox = win[framebox( 1 )];
mapSeg = imgBox << FindSeg( MapSeg( 1 ) );
mapSeg << Transparency( 0.5 );
Try(
    xAxis = gb[AxisBox( 2 )];
    xMin = (xAxis << get min);
    xMax = (xAxis << get max);
,
    xMin = 0;
    xMax = 100;
);
yAxis = gb[AxisBox( 1 )];
yMin = (yAxis << get min);
yMax = (yAxis << get max);
xval = Matrix( {xmin, xmax} );
yval = Matrix( {ymin, ymax} );
mapSeg << Sib Append( Line Seg( xval, yval, <<line color( "Green" ), <<line width( 3 ) ) );
```

### [Sib Prepend](#sib-prepend)[](#sib-prepend "Click to copy url")

**Syntax:** obj \<\< Sib Prepend( seg2 )

**Description:** Adds a display seg immediately before the display seg.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
Try(
    xAxis = g[AxisBox( 2 )];
    xMin = (xAxis << get min);
    xMax = (xAxis << get max);
,
    xMin = 0;
    xMax = 100;
);
yAxis = g[AxisBox( 1 )];
yMin = (yAxis << get min);
yMax = (yAxis << get max);
xval = Matrix( {xmin, xmax} );
yval = Matrix( {ymin, ymax} );
seg << Sib Prepend( Line Seg( xval, yval, <<line color( "Green" ), <<line width( 3 ) ) );
```

### [Transparency](#transparency)[](#transparency "Click to copy url")

**Syntax:** obj \<\< Transparency( number )

**Description:** Sets the shape transparency. The argument should be a numeric value between 0 and 1.

``` jsl
New Window( "Shape Seg Example",
    g = Graph Box(
        Shape Seg(
            {Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
            Path( "M20,20 C20,60 60,60 60,20 Z" )}
        )
    )
);
frame = g[Frame Box( 1 )];
seg = (frame << Find Seg( Shape Seg( 1 ) ));
seg << Set Transparency( .3 );
```

## [Shared Item Messages](#shared-item-messages)[](#shared-item-messages "Click to copy url")

### [Enabled](#enabled)[](#enabled "Click to copy url")

**Syntax:** obj \<\< Enabled( state=0\|1 ); state = obj \<\< Get Enabled

**Description:** An object that is not enabled will not respond to keyboard or mouse input. This property is inherited by child objects, so a container object that is disabled will cause all descendent objects to be disabled.

``` jsl
//This message applies to all display objects
New Window( "enabled",
    V List Box(
        check = Check Box(
            {"Use Password"},
            ptext << Enabled( check << Get( 1 ) );
            pvalue << Enabled( check << Get( 1 ) );
        ),
        Lineup Box( N Col( 2 ),
            Text Box( "Username:" ),
            Text Edit Box( "", <<Set Width( 100 ) ),
            ptext = Text Box( "Password:", <<Enabled( 0 ) ),
            pvalue = Text Edit Box( "",
                <<Password Style( 1 ),
                <<Set Width( 20 ),
                <<Enabled( 0 )
            )
        )
    )
);
```

### [Get Enabled](#get-enabled)[](#get-enabled "Click to copy url")

**Syntax:** obj \<\< Enabled( state=0\|1 ); state = obj \<\< Get Enabled

**Description:** An object that is not enabled will not respond to keyboard or mouse input. This property is inherited by child objects, so a container object that is disabled will cause all descendent objects to be disabled.

``` jsl
//This message applies to all display objects
New Window( "enabled",
    V List Box(
        check = Check Box(
            {"Use Password"},
            ptext << Enabled( check << Get( 1 ) );
            pvalue << Enabled( check << Get( 1 ) );
        ),
        Lineup Box( N Col( 2 ),
            Text Box( "Username:" ),
            Text Edit Box( "", <<Set Width( 100 ) ),
            ptext = Text Box( "Password:", <<Enabled( 0 ) ),
            pvalue = Text Edit Box( "",
                <<Password Style( 1 ),
                <<Set Width( 20 ),
                <<Enabled( 0 )
            )
        )
    )
);
```

### [Get Namespace](#get-namespace)[](#get-namespace "Click to copy url")

**Syntax:** obj \<\< Get Namespace

**Description:** Returns the namespace associated with this display object.

``` jsl
//This message applies to all display objects
x = 1;
w = New Window( "Test", b = Button Box( "Press me" ) );
b:x = 2;
ns = b << GetNamespace();
Show( ns:x, x );
```

### [Get Properties](#get-properties)[](#get-properties "Click to copy url")

**Syntax:** obj \<\< Get Properties

**Description:** Returns an associative array that contains the display box's properties and their values.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Get Properties;
```

### [Get Property](#get-property)[](#get-property "Click to copy url")

**Syntax:** obj \<\< Get Property( "property" )

**Description:** Returns the current setting for the named property.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Get Property( "Enabled" );
```

### [Get Property List](#get-property-list)[](#get-property-list "Click to copy url")

**Syntax:** obj \<\< Get Property List

**Description:** Returns a list of properties the display box has.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Get Property List;
```

### [Set Property](#set-property)[](#set-property "Click to copy url")

**Syntax:** obj \<\< Set Property( "property", value )

**Description:** Sets the value for the named property for the display box.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Set Property( "Enabled", 0 );
```

[ Previous](ShapeBorderBox.html "ShapeBorderBox") [Next ](SheetBox.html "SheetBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
