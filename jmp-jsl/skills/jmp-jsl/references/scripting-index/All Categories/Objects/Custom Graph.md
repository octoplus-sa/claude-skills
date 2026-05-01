# Custom Graph

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Custom%20Graph.html](https://jsl.jmp.com/All%20Categories/Objects/Custom%20Graph.html)*

---

# [Custom Graph](#custom-graph)[](#custom-graph "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Custom Graph](#custom-graph_1)[](#custom-graph_1 "Click to copy url")

**Syntax:** New Window(Window title, \<Editable\|Dialog\>, Graph Box( named arguments, ..., script segment

**Description:** Creates a graph using a custom script.

``` jsl
obj = New Window( "Example",
    Graph Box(
        Y Scale( -10, 90 ),
        X Scale( -10, 90 ),
        Oval(
            X Origin() + 10,
            (Y Origin() + Y Range()) - 10,
            (X Origin() + X Range()) - 10,
            Y Origin() + 10,
            1
        ),
        Title( "Oval" )
    )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Append Seg](#append-seg)[](#append-seg "Click to copy url")

**Syntax:** obj \<\< Append Seg( display seg )

**Description:** Adds a display seg to the FrameBox

``` jsl
x = [20, 40, 60, 80];
New Window( "Example",
    Graph Box( Frame Size( 300, 120 ), Append Seg( Marker Seg( x, x ), Line Seg( x, x ) ) )
);
```

### [Background Map](#background-map)[](#background-map "Click to copy url")

**Syntax:** obj \<\< Background Map

### [Bottom](#bottom)[](#bottom "Click to copy url")

**Syntax:** obj \<\< Bottom( number )

### [FrameSize](#framesize)[](#framesize "Click to copy url")

**Syntax:** Frame Size( width, height )

**Description:** Sets the size of the graph.

**Example 1**

``` jsl
obj = New Window( "Example",
    Graph Box(
        Framesize( 400, 400 ),
        <<backgroundcolor( "cyan" ),
        XAxis( Show Major Grid ),
        Title( "Sine curve" ),
        Y Function( 10 + 50 * Sin( a / 30 ), a )
    )
);
```

**Example 2**

``` jsl
xmin = -2;
xmax = 1;
ymin = -1.5;
ymax = 1.5;
contourMatrix = J( 30, 20, 0 );
depth = 100;
/* build a demonstration matrix -- a really low resolution Mandelbrot */
Parallel Assign(
    {r = N Row( contourMatrix ) - 1, c = N Col( contourMatrix ) - 1, xmin = xmin, xmax = xmax,
    ymin = ymin, ymax = ymax, depth = depth},
    contourMatrix[irow, icol] = Mandelbrot(
        depth,
        2,
        (xmax - xmin) * (irow - 1) / (r) + xmin,
        (ymax - ymin) * (icol - 1) / (c) + ymin
    )
);
colors = J( depth + 1, 1, 0 ); // color choices for contours
For( i = 1, i <= depth + 1, i++,
    colors[i] = RGB Color(
        0,
        (Sqrt( Sqrt( (i - 1) / depth ) )),
        1 - (Sqrt( Sqrt( (i - 1) / depth ) ))
    )
);
/* see the Mandelbrot Function for a better way to do this */
New Window( "Example",
    Graph Box(
        X Scale( xmin, xmax ),
        Y Scale( ymin, ymax ),
        framesize( 500, 500 ),
        Contour( /* map the matrix rows onto the axes */
            (0 :: N Row( contourMatrix ) - 1) * (xmax - xmin) / (N Row( contourMatrix ) - 1)
             + xmin,
            (0 :: N Col( contourMatrix ) - 1) * (ymax - ymin) / (N Col( contourMatrix ) - 1)
             + ymin, 
            // the low res Mandelbrot data
            contourMatrix, 
            // the Mandelbrot function returns integers from 1 to depth, map them to colors
            0 :: depth,
            colors,
            fill
        )
    )
);
```

### [Get Background Color](#get-background-color)[](#get-background-color "Click to copy url")

**Syntax:** obj \<\< Get Background Color( color )

### [Get Background Fill](#get-background-fill)[](#get-background-fill "Click to copy url")

**Syntax:** obj \<\< Get Background Fill( state=0\|1 )

### [Get Bottom](#get-bottom)[](#get-bottom "Click to copy url")

**Syntax:** obj \<\< Get Bottom

### [Get Graphics Script](#get-graphics-script)[](#get-graphics-script "Click to copy url")

**Syntax:** obj \<\< Get Graphics Script

### [Get Height](#get-height)[](#get-height "Click to copy url")

**Syntax:** obj \<\< Get Height

### [Get Left](#get-left)[](#get-left "Click to copy url")

**Syntax:** obj \<\< Get Left

### [Get Right](#get-right)[](#get-right "Click to copy url")

**Syntax:** obj \<\< Get Right

### [Get Sides](#get-sides)[](#get-sides "Click to copy url")

**Syntax:** obj \<\< Get Sides

### [Get Top](#get-top)[](#get-top "Click to copy url")

**Syntax:** obj \<\< Get Top

### [Get Width](#get-width)[](#get-width "Click to copy url")

**Syntax:** obj \<\< Get Width

### [Get X Axis](#get-x-axis)[](#get-x-axis "Click to copy url")

**Syntax:** obj \<\< Get X Axis

### [Get X Name](#get-x-name)[](#get-x-name "Click to copy url")

**Syntax:** obj \<\< Get X Name

### [Get Y Axis](#get-y-axis)[](#get-y-axis "Click to copy url")

**Syntax:** obj \<\< Get Y Axis

### [Get Y Name](#get-y-name)[](#get-y-name "Click to copy url")

**Syntax:** obj \<\< Get Y Name

### [Left](#left)[](#left "Click to copy url")

**Syntax:** obj \<\< Left( number )

### [Right](#right)[](#right "Click to copy url")

**Syntax:** obj \<\< Right( number )

### [Set Background Color](#set-background-color)[](#set-background-color "Click to copy url")

**Syntax:** obj \<\< Set Background Color( color )

### [Set Background Fill](#set-background-fill)[](#set-background-fill "Click to copy url")

**Syntax:** obj \<\< Set Background Fill( state=0\|1 )

### [Set Graphics Script](#set-graphics-script)[](#set-graphics-script "Click to copy url")

**Syntax:** obj \<\< Set Graphics Script

### [Set Height](#set-height)[](#set-height "Click to copy url")

**Syntax:** obj \<\< Set Height

### [Set Width](#set-width)[](#set-width "Click to copy url")

**Syntax:** obj \<\< Set Width

### [Set X Axis](#set-x-axis)[](#set-x-axis "Click to copy url")

**Syntax:** obj \<\< Set X Axis

### [Set X Name](#set-x-name)[](#set-x-name "Click to copy url")

**Syntax:** obj \<\< Set X Name

### [Set Y Axis](#set-y-axis)[](#set-y-axis "Click to copy url")

**Syntax:** obj \<\< Set Y Axis

### [Set Y Name](#set-y-name)[](#set-y-name "Click to copy url")

**Syntax:** obj \<\< Set Y Name

### [Sides](#sides)[](#sides "Click to copy url")

**Syntax:** obj \<\< Sides( number )

### [Suppress Axes](#suppress-axes)[](#suppress-axes "Click to copy url")

**Syntax:** obj \<\< Suppress Axes

**Description:** Hides the axes of the graph box.

``` jsl
obj = New Window( "Example",
    Graph Box(
        Framesize( 400, 400 ),
        Suppress Axes,
        <<backgroundcolor( "cyan" ),
        XAxis( Show Major Grid ),
        Title( "Sine curve" ),
        Y Function( 10 + 50 * Sin( a / 30 ), a )
    )
);
```

### [Title](#title)[](#title "Click to copy url")

**Syntax:** Title( string )

**Description:** Sets the title for the graph.

``` jsl
obj = New Window( "Example",
    Graph Box(
        <<backgroundcolor( "cyan" ),
        XAxis( Show Major Grid ),
        Title( "Sine curve" ),
        Y Function( 10 + 50 * Sin( a / 30 ), a )
    )
);
```

### [Top](#top)[](#top "Click to copy url")

**Syntax:** obj \<\< Top( number )

### [X Scale](#x-scale)[](#x-scale "Click to copy url")

**Syntax:** X Scale( xMin, xMax )

**Description:** Sets the scale for the X axis on the graph.

``` jsl
obj = New Window( "Example",
    Graph Box(
        Y Scale( -10, 90 ),
        X Scale( -10, 90 ),
        Oval(
            X Origin() + 10,
            (Y Origin() + Y Range()) - 10,
            (X Origin() + X Range()) - 10,
            Y Origin() + 10,
            1
        ),
        Title( "Oval" )
    )
);
```

### [XAxis](#xaxis)[](#xaxis "Click to copy url")

**Syntax:** X Axis(Scale, Min, Max, Inc, Tick Font, Show Major Ticks, Show Minor Ticks, Show Major Grid, Show Minor Grid, Format, Decimal, Show Labels, Rotated Labels, Rotated Labels Alt, Minor Ticks, Add Ref Line )

**Description:** Sets X Axis features on the graph.

``` jsl
obj = New Window( "Example",
    Graph Box(
        Framesize( 400, 400 ),
        <<backgroundcolor( "cyan" ),
        XName( "Time" ),
        YName( "Result" ),
        XAxis( Show Major Grid, Inc( 5 ) ),
        Title( "Cosine curve" ),
        Y Function( 50 + 10 * Cos( a / 10 ), a )
    )
);
```

### [XName](#xname)[](#xname "Click to copy url")

**Syntax:** X Name( string )

**Description:** Sets the name for the X Axis on the graph.

``` jsl
obj = New Window( "Example",
    Graph Box(
        Framesize( 400, 400 ),
        <<backgroundcolor( "blue" ),
        XName( "Time" ),
        YName( "Result" ),
        XAxis( Show Major Grid ),
        Title( "Sine curve" ),
        Y Function( 10 + 50 * Sin( a / 30 ), a )
    )
);
```

### [Y Scale](#y-scale)[](#y-scale "Click to copy url")

**Syntax:** Y Scale( yMin, yMax )

**Description:** Sets the scale for the Y axis on the graph.

``` jsl
obj = New Window( "Example",
    Graph Box(
        Y Scale( -10, 90 ),
        X Scale( -10, 90 ),
        Oval(
            X Origin() + 10,
            (Y Origin() + Y Range()) - 10,
            (X Origin() + X Range()) - 10,
            Y Origin() + 10,
            1
        ),
        Title( "Oval" )
    )
);
```

### [YAxis](#yaxis)[](#yaxis "Click to copy url")

**Syntax:** Y Axis(Scale, Min, Max, Inc, Tick Font, Show Major Ticks, Show Minor Ticks, Show Major Grid, Show Minor Grid, Format, Decimal, Show Labels, Rotated Labels, Rotated Labels Alt, Minor Ticks, Add Ref Line )

**Description:** Sets Y Axis features on the graph.

``` jsl
obj = New Window( "Example",
    Graph Box(
        Framesize( 400, 400 ),
        <<backgroundcolor( "cyan" ),
        XName( "Time" ),
        YName( "Result" ),
        YAxis( Show Major Grid ),
        Title( "Cosine curve" ),
        Y Function( 50 + 10 * Cos( a / 10 ), a )
    )
);
```

### [YName](#yname)[](#yname "Click to copy url")

**Syntax:** Y Name( string )

**Description:** Sets the name for the Y Axis on the graph.

``` jsl
obj = New Window( "Example",
    Graph Box(
        Framesize( 400, 400 ),
        <<backgroundcolor( "cyan" ),
        XName( "Time" ),
        YName( "Result" ),
        XAxis( Show Major Grid ),
        Title( "Cosine curve" ),
        Y Function( 50 + 10 * Cos( a / 10 ), a )
    )
);
```

[ Previous](Custom%20Function.html "Custom Function") [Next ](Custom%20Profiler.html "Custom Profiler")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
