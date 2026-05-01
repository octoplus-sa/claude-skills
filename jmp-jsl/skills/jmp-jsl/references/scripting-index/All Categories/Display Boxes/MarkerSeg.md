# MarkerSeg

*Source: [https://jsl.jmp.com/All%20Categories/Display%20Boxes/MarkerSeg.html](https://jsl.jmp.com/All%20Categories/Display%20Boxes/MarkerSeg.html)*

---

# [MarkerSeg](#markerseg)[](#markerseg "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Marker Seg](#marker-seg)[](#marker-seg "Click to copy url")

**Syntax:** me = Marker Seg( x, y, \< Row States( dt \| dt,\[rows\] \| dt,{{rows}, ...} \| {states} ) \>, \< Sizes( s ) \> )

**Description:** Returns a display seg with markers for all of the X and Y values.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Always Show Label](#always-show-label)[](#always-show-label "Click to copy url")

**Syntax:** obj \<\< Always Show Label( {pt, state=0\|1}, ... )

**Description:** Always show the marker label even if it being hidden by an overlapping label

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
For( i = 1, i <= 40, i++,
    Labeled( Row State( i ) ) = 1
);
r = Bivariate( Y( :weight ), X( :height ) ) << Report();
frame = r[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << always show label( {0, 1}, {1, 1}, {2, 1}, {3, 1}, {4, 1}, {5, 1} );
```

### [Child](#child)[](#child "Click to copy url")

**Syntax:** seg2 = obj \<\< Child

**Description:** Returns the first child of the display seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Child; // not many segs support children
```

### [Class Name](#class-name)[](#class-name "Click to copy url")

**Syntax:** classname = obj \<\< Class Name

**Description:** Returns the name of the display class for the display seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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

**Description:** Sets the color for all markers.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Color( "Green" );
```

### [Color Theme](#color-theme)[](#color-theme "Click to copy url")

**Syntax:** obj \<\< Color Theme

### [Delete](#delete)[](#delete "Click to copy url")

**Syntax:** obj \<\< Delete

**Description:** Delete the display seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Delete;
```

### [Density Gradient](#density-gradient)[](#density-gradient "Click to copy url")

**Syntax:** obj \<\< Density Gradient( "Fade to White"\|"Fade To Gray"\|"Full Color"="Fade to White" )

**Description:** Sets the coloring behavior of density gradients. "Fade to White" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Density Gradient( "Fade to Gray" );
```

### [Frame](#frame)[](#frame "Click to copy url")

**Syntax:** FrameBox = obj \<\< Frame

**Description:** Returns the frame box that the display seg is in.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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

**Description:** Returns the marker color.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Color;
```

### [Get Colors](#get-colors)[](#get-colors "Click to copy url")

**Syntax:** list = obj \<\< Get Colors

**Description:** Returns a list of marker colors based on the row states for the markers.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Colors;
```

### [Get Density Gradient](#get-density-gradient)[](#get-density-gradient "Click to copy url")

**Syntax:** obj \<\< Get Density Gradient

**Description:** Gets the coloring behavior of density gradients.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Density Gradient;
```

### [Get Description](#get-description)[](#get-description "Click to copy url")

**Syntax:** description = obj \<\< Get Description

**Description:** Gets the description for the display seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << get description();
```

### [Get Force Labels](#get-force-labels)[](#get-force-labels "Click to copy url")

**Syntax:** obj \<\< Get Force Labels( "No Labels"\|"Label by Value"\|"Label by Row"\|"Label by Row and Value" )

**Description:** Label every marker regardless of the data table row state flags.

**JMP Version Added:** 18

### [Get Gradient](#get-gradient)[](#get-gradient "Click to copy url")

**Syntax:** obj \<\< Get Gradient

**Description:** Gets the coloring gradient.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient;
```

### [Get Gradient Color Theme](#get-gradient-color-theme)[](#get-gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Get Gradient Color Theme

**Description:** Gets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient Color Theme;
```

### [Get Gradient Discrete Colors](#get-gradient-discrete-colors)[](#get-gradient-discrete-colors "Click to copy url")

**Syntax:** obj \<\< Get Gradient Discrete Colors

**Description:** Gets if each level in a gradient should be a single color or if colors should transition smoothly.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient Legend Horizontal;
```

### [Get Gradient Legend Label Format](#get-gradient-legend-label-format)[](#get-gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Label Format

**Description:** Gets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient Legend Label Format;
```

### [Get Gradient Legend Label Width](#get-gradient-legend-label-width)[](#get-gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Label Width

**Description:** Gets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient Legend Label Width;
```

### [Get Gradient Legend Show Labels](#get-gradient-legend-show-labels)[](#get-gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Show Labels

**Description:** Gets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient Legend Show Labels;
```

### [Get Gradient Level Count](#get-gradient-level-count)[](#get-gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Get Gradient Level Count

**Description:** Gets the number of levels in a gradient.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient Levels;
```

### [Get Gradient Lightness Range](#get-gradient-lightness-range)[](#get-gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Get Gradient Lightness Range

**Description:** Gets the minimum and maximum lightness for level colors in a gradient. Missing values indicate that the color theme's original value is used.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient Reverse Color Order;
```

### [Get Gradient Reverse Label Order](#get-gradient-reverse-label-order)[](#get-gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Get Gradient Reverse Label Order

**Description:** Gets if the order of labels in a gradient is reversed.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient Show Missing;
```

### [Get Gradient Transparency](#get-gradient-transparency)[](#get-gradient-transparency "Click to copy url")

**Syntax:** obj \<\< Get Gradient Transparency

**Description:** Gets the transparency behavior of gradients.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Gradient Transparency;
```

### [Get Hide Missing Color](#get-hide-missing-color)[](#get-hide-missing-color "Click to copy url")

**Syntax:** true/false = obj \<\< Get Hide Missing Color

``` jsl
Random Reset( 1111111 );
n = 1000;
T1 = J( n, 1, Random Normal() );
T1[Loc( J( n, 1, Random Integer( 0, 1 ) ) )] = .;
dt = New Table( "Test",
    New Column( "X", Values( J( n, 1, Random Uniform() ) ) ),
    New Column( "Y", Values( J( n, 1, Random Uniform() ) ) ),
    New Column( "T1", Values( T1 ) ),

);
obj = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :X ), Y( :Y ), Color( :T1 ) ),
    Elements( Points( X, Y, Legend( 16 ) ) )
);

frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Hide Missing Color;
```

### [Get Hide Missing Size](#get-hide-missing-size)[](#get-hide-missing-size "Click to copy url")

**Syntax:** true/false = obj \<\< Get Hide Missing Size

``` jsl
Random Reset( 1111111 );
n = 1000;
T1 = J( n, 1, Random Normal() );
T1[Loc( J( n, 1, Random Integer( 0, 1 ) ) )] = .;
dt = New Table( "Test",
    New Column( "X", Values( J( n, 1, Random Uniform() ) ) ),
    New Column( "Y", Values( J( n, 1, Random Uniform() ) ) ),
    New Column( "T1", Values( T1 ) ),

);
obj = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :X ), Y( :Y ), Size( :T1 ) ),
    Elements( Points( X, Y, Legend( 16 ) ) )
);

frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Hide Missing Size;
```

### [Get Jitter](#get-jitter)[](#get-jitter "Click to copy url")

**Syntax:** {method, axis, limit, spacing, seed, side, overlap, grid offset, smoothing, max error, bandwidth} = obj \<\< Get Jitter

**Description:** Returns settings used to offset marker positions for collision reduction. method is none\|random uniform\|random normal\|centered\|centered grid\|positive grid. axis is X\|Y\|XY. limit is the width of the jitter, adjusted for the method. spacing is the percentage of the marker size using for jittering or 0 for auto-adjustment.

**JMP Version Added:** 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
r = Oneway( Y( :height ), X( :sex ), Means( 1 ), MeanDiamonds( 1 ), XAxisProportional( 0 ) );
frame = (r << report)[FrameBox( 1 )];
seg = (frame << FindSeg( Marker Seg( 1 ) ));
{method, axis, limit, spacing, seed, side, overlap, grid offset, smoothing, max error,
bandwidth} = seg << Get Jitter();
```

### [Get Jitter Offsets](#get-jitter-offsets)[](#get-jitter-offsets "Click to copy url")

**Syntax:** matrix = obj \<\< Get Jitter Offsets

**Description:** Returns an N by 2 matrix of X and Y jitter offsets.

``` jsl
x = J( 1, 100, Random Normal() );
y = J( 1, 100, 0 );
New Window( "Marker Seg Example",
    g = Graph Box(
        X Scale( -4, 4 ),
        Y Scale( -0.5, 0.5 ),
        Frame Size( 300, 200 ),
        Marker Seg( x, y, <<Set Marker Size( 5 ), <<Set Jitter( {"Grid", "Y"} ) )
    )
);
seg = (g[FrameBox( 1 )] << Find Seg( Marker Seg( 1 ) ));
jitter = seg << Get Jitter Offsets;
avg = Mean( jitter[0, 1] );
```

### [Get Label Value Axis](#get-label-value-axis)[](#get-label-value-axis "Click to copy url")

**Syntax:** obj \<\< Get Label Value Axis( "X"\|"Y" )

**Description:** Whether forced labels show the X or Y value.

**JMP Version Added:** 18

### [Get Label Value Format](#get-label-value-format)[](#get-label-value-format "Click to copy url")

**Syntax:** obj \<\< Get Label Value Format

**Description:** How to format the X or Y value; Auto means use axis format.

**JMP Version Added:** 18

### [Get Marker](#get-marker)[](#get-marker "Click to copy url")

**Syntax:** marker = obj \<\< Get Marker

**Description:** Returns the marker style.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Marker;
```

### [Get Marker Draw Column](#get-marker-draw-column)[](#get-marker-draw-column "Click to copy url")

**Syntax:** column = obj \<\< Get Marker Draw Column

**Description:** Returns any custom marker drawing data table column.

**JMP Version Added:** 16

``` jsl
Open( "$SAMPLE_DATA/Big Class Families.jmp" );
r = Bivariate( Y( :height ), X( :weight ) );
frame = (r << report)[FrameBox( 1 )];
seg = (frame << FindSeg( Marker Seg( 1 ) ));
seg << Set Marker Draw Column( :picture );
ex = seg << Get Marker Draw Column();
```

### [Get Marker Draw Expr](#get-marker-draw-expr)[](#get-marker-draw-expr "Click to copy url")

**Syntax:** expr = obj \<\< Get Marker Draw Expr

**Description:** Returns the custom marker drawing expression.

**JMP Version Added:** 16

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
r = Bivariate( Y( :height ), X( :weight ) );
frame = (r << report)[FrameBox( 1 )];
seg = (frame << FindSeg( Marker Seg( 1 ) ));
seg << Set Marker Draw Expr( [-1 0, 0 2, 1 0, 0 1, -1 0] );
ex = seg << Get Marker Draw Expr();
```

### [Get Marker Size](#get-marker-size)[](#get-marker-size "Click to copy url")

**Syntax:** size = obj \<\< Get Marker Size

**Description:** Returns the marker size.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Marker Size;
```

### [Get Markers](#get-markers)[](#get-markers "Click to copy url")

**Syntax:** list = obj \<\< Get Markers

**Description:** Returns a list of markers based on the row states.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Markers;
```

### [Get Overlay Color](#get-overlay-color)[](#get-overlay-color "Click to copy url")

**Syntax:** color = obj \<\< Get Overlay Color( marker index )

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
op = dt << Overlay Plot( X( :age ), Y( :height, :weight ) );
rep = op << report;
frame = rep[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Overlay Color( 1 );
```

### [Get Overlay Count](#get-overlay-count)[](#get-overlay-count "Click to copy url")

**Syntax:** number = obj \<\< Get Overlay Count

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
op = dt << Overlay Plot( X( :age ), Y( :height, :weight ) );
rep = op << report;
frame = rep[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Overlay Count;
```

### [Get Overlay Marker](#get-overlay-marker)[](#get-overlay-marker "Click to copy url")

**Syntax:** marker = obj \<\< Get Overlay Marker( marker index )

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
op = dt << Overlay Plot( X( :age ), Y( :height, :weight ) );
rep = op << report;
frame = rep[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Overlay Marker( 1 );
```

### [Get Point](#get-point)[](#get-point "Click to copy url")

**Syntax:** point = obj \<\< Get Point( index )

**Description:** Returns the X and Y coordinates of the specified point.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Point( 2 );
```

### [Get Point Count](#get-point-count)[](#get-point-count "Click to copy url")

**Syntax:** Number = obj \<\< Get Point Count

**Description:** Returns the number of points in the display seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Point Count;
```

### [Get Row Numbers](#get-row-numbers)[](#get-row-numbers "Click to copy url")

**Syntax:** matrix = obj \<\< Get Row Numbers

**Description:** Returns a vector of marker row numbers.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
x = [10 50 70];
y = [60 50 10];
New Window( "Marker Seg Example",
    g = Graph Box( Marker Seg( x, y, Row States( dt, [5 7 9] ) ) )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Row Numbers;
```

### [Get Sizes](#get-sizes)[](#get-sizes "Click to copy url")

**Syntax:** matrix = obj \<\< Get Sizes

**Description:** Returns a vector of marker sizes.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Sizes;
```

### [Get Transparency](#get-transparency)[](#get-transparency "Click to copy url")

**Syntax:** obj \<\< Get Transparency

**Description:** Returns a numeric value representing transparency between 0 and 1.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Transparency;
```

### [Get Value Label Width](#get-value-label-width)[](#get-value-label-width "Click to copy url")

**Syntax:** obj \<\< Get Value Label Width( number )

**Description:** Maximum width for a formatted label value.

**JMP Version Added:** 18

### [Get X Values](#get-x-values)[](#get-x-values "Click to copy url")

**Syntax:** matrix = obj \<\< Get X Values

**Description:** Returns a list of X values.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get X Values;
```

### [Get Y Values](#get-y-values)[](#get-y-values "Click to copy url")

**Syntax:** matrix = obj \<\< Get Y Values

**Description:** Returns a list of Y values.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Get Y Values;
```

### [Gradient](#gradient)[](#gradient "Click to copy url")

**Syntax:** obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<Contour Levels(num)\>, \<Reverse Gradient(0\|1)\>, \<Density Gradient("Fade To White"\|"Fade To Gray"\|"Full Color")\>, \<Gradient Transparency("None"\|"Linear")\> } obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<N Labels(num)\>, \<Show Missing Color("On"\|"Off"\|"Auto")\>, \<Scale Type("Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom")\>, \<Scale Values(\[v1, v2, …\])\>, \<Range Type("Default"\|"Exact Data Range"\|"Middle 90%")\>, \<Fill("Between"\|"Above"\|"Below"\|"Above Below")\>, \<Reverse Gradient(0\|1)\>, \<Reverse Labels(0\|1)\>, \<Discrete Color(0\|1)\> }, \<Label Format(labelFormat)\>, \<Width(num)\>, \<Horizontal(0\|1)\>, \<Show Labels(0\|1)\>

**Description:** Sets the coloring gradient.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient( {Color Theme( "Viridis" ), N Labels( 7 )} );
```

### [Gradient Color Theme](#gradient-color-theme)[](#gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Gradient Color Theme

**Description:** Sets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Legend Horizontal( 1 );
```

### [Gradient Legend Label Format](#gradient-legend-label-format)[](#gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Label Format

**Description:** Sets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Legend Label Format( "Fixed Dec", 6, 3 );
```

### [Gradient Legend Label Width](#gradient-legend-label-width)[](#gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Label Width

**Description:** Sets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Legend Label Width( 4 );
```

### [Gradient Legend Show Labels](#gradient-legend-show-labels)[](#gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Show Labels

**Description:** Sets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Legend Show Labels( 0 );
```

### [Gradient Level Count](#gradient-level-count)[](#gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Gradient Level Count

**Description:** Sets the number of levels in a gradient. This is one less than the number of labels.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Levels( 7 );
```

### [Gradient Lightness Range](#gradient-lightness-range)[](#gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Gradient Lightness Range

**Description:** Sets the minimum and maximum lightness for level colors in a gradient. The colors will be scaled to cover this range. A missing value is treated as no change.

**JMP Version Added:** 18

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Lightness Range( Min( 0.25 ), Max( 0.75 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Lightness Range( 0.25, 0.75 );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Reverse Color Order( 1 );
```

### [Gradient Reverse Label Order](#gradient-reverse-label-order)[](#gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Gradient Reverse Label Order

**Description:** Reverses the order of the labels in a gradient.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Gradient Transparency( "None" );
```

### [Label Offset](#label-offset)[](#label-offset "Click to copy url")

**Syntax:** obj \<\< Label Offset( {pt, x offset, y offset}, ... )

**Description:** Positions row labels according to the given coordinates.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Labeled( Row State( 5 ) ) = 1;
Labeled( Row State( 8 ) ) = 1;
dist = Distribution( Continuous Distribution( Column( :height ) ) );
frame = (dist << report)[FrameBox( 2 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << label offset( {0, -20, -10}, {1, -20, -30} );
```

### [Marker](#marker)[](#marker "Click to copy url")

**Syntax:** obj \<\< Marker( marker )

**Description:** Sets the marker style for all markers.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Marker( "Square" );
```

### [Marker Size](#marker-size)[](#marker-size "Click to copy url")

**Syntax:** obj \<\< Marker Size

**Description:** Sets the size for the markers. Size options are Dot, Small, Medium, Large, XL, XXL, and XXXL.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Marker Size( "XL" );
Wait( 1 );
seg << Set Marker Size( "dot" );
```

### [Parent](#parent)[](#parent "Click to copy url")

**Syntax:** seg2 = obj \<\< Parent

**Description:** Returns the parent of the display seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Parent;
```

### [Revert](#revert)[](#revert "Click to copy url")

**Syntax:** obj \<\< Revert

**Description:** Changes the seg back to its original state.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
Wait( 1 );
seg << Set Color( "Red" );
Wait( 1 );
seg << Revert;
```

### [Set Color](#set-color)[](#set-color "Click to copy url")

**Syntax:** obj \<\< Set Color( color )

**Description:** Sets the color for all markers.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Color( "Green" );
```

### [Set Description](#set-description)[](#set-description "Click to copy url")

**Syntax:** obj \<\< Set Description( description )

**Description:** Sets the description for the display seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << set description( "my seg" );
```

### [Set Force Labels](#set-force-labels)[](#set-force-labels "Click to copy url")

**Syntax:** obj \<\< Set Force Labels( "No Labels"\|"Label by Value"\|"Label by Row"\|"Label by Row and Value" )

**Description:** Label every marker regardless of the data table row state flags.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Bivariate(
    Y( :weight ),
    X( :height ),
    SendToReport(
        Dispatch( {}, "Bivar Plot", FrameBox,
            {DispatchSeg(
                Marker Seg( 1 ),
                Set Force Labels( "Label by Value" ),
                Set Label Value Axis( "X" ),
                Set Label Value Format( "Fixed", 1 )
            )}
        )
    )
);
```

### [Set Gradient](#set-gradient)[](#set-gradient "Click to copy url")

**Syntax:** obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<Contour Levels(num)\>, \<Reverse Gradient(0\|1)\>, \<Density Gradient("Fade To White"\|"Fade To Gray"\|"Full Color")\>, \<Gradient Transparency("None"\|"Linear")\> } obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<N Labels(num)\>, \<Show Missing Color("On"\|"Off"\|"Auto")\>, \<Scale Type("Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom")\>, \<Scale Values(\[v1, v2, …\])\>, \<Range Type("Default"\|"Exact Data Range"\|"Middle 90%")\>, \<Fill("Between"\|"Above"\|"Below"\|"Above Below")\>, \<Reverse Gradient(0\|1)\>, \<Reverse Labels(0\|1)\>, \<Discrete Color(0\|1)\> }, \<Label Format(labelFormat)\>, \<Width(num)\>, \<Horizontal(0\|1)\>, \<Show Labels(0\|1)\>

**Description:** Sets the coloring gradient.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient( {Color Theme( "Viridis" ), N Labels( 7 )} );
```

### [Set Gradient Color Theme](#set-gradient-color-theme)[](#set-gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Set Gradient Color Theme

**Description:** Sets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Color Theme( "Viridis" );
```

### [Set Gradient Custom Scale](#set-gradient-custom-scale)[](#set-gradient-custom-scale "Click to copy url")

**Syntax:** obj \<\< Set Gradient Custom Scale

**Description:** Sets the gradient to use a list of values for a custom scale.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Legend Horizontal( 1 );
```

### [Set Gradient Legend Label Format](#set-gradient-legend-label-format)[](#set-gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Label Format

**Description:** Sets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Legend Label Format( "Fixed Dec", 6, 3 );
```

### [Set Gradient Legend Label Width](#set-gradient-legend-label-width)[](#set-gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Label Width

**Description:** Sets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Legend Label Width( 4 );
```

### [Set Gradient Legend Show Labels](#set-gradient-legend-show-labels)[](#set-gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Show Labels

**Description:** Sets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Legend Show Labels( 0 );
```

### [Set Gradient Level Count](#set-gradient-level-count)[](#set-gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Set Gradient Level Count

**Description:** Sets the number of levels in a gradient. This is one less than the number of labels.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Levels( 7 );
```

### [Set Gradient Lightness Range](#set-gradient-lightness-range)[](#set-gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Set Gradient Lightness Range

**Description:** Sets the minimum and maximum lightness for level colors in a gradient. The colors will be scaled to cover this range. A missing value is treated as no change.

**JMP Version Added:** 18

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Lightness Range( Min( 0.25 ), Max( 0.75 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Lightness Range( 0.25, 0.75 );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Gradient Reverse Color Order( 1 );
```

### [Set Gradient Reverse Label Order](#set-gradient-reverse-label-order)[](#set-gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Set Gradient Reverse Label Order

**Description:** Reverses the order of the labels in a gradient.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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

### [Set Hide Missing Color](#set-hide-missing-color)[](#set-hide-missing-color "Click to copy url")

**Syntax:** obj \<\< Set Hide Missing Color( true/false )

``` jsl
Random Reset( 1111111 );
n = 1000;
T1 = J( n, 1, Random Normal() );
T1[Loc( J( n, 1, Random Integer( 0, 1 ) ) )] = .;
dt = New Table( "Test",
    New Column( "X", Values( J( n, 1, Random Uniform() ) ) ),
    New Column( "Y", Values( J( n, 1, Random Uniform() ) ) ),
    New Column( "T1", Values( T1 ) ),

);
obj = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :X ), Y( :Y ), Color( :T1 ) ),
    Elements( Points( X, Y, Legend( 16 ) ) )
);

frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Hide Missing Color( true );
```

### [Set Hide Missing Size](#set-hide-missing-size)[](#set-hide-missing-size "Click to copy url")

**Syntax:** obj \<\< Set Hide Missing Size( true/false )

``` jsl
Random Reset( 1111111 );
n = 1000;
T1 = J( n, 1, Random Normal() );
T1[Loc( J( n, 1, Random Integer( 0, 1 ) ) )] = .;
dt = New Table( "Test",
    New Column( "X", Values( J( n, 1, Random Uniform() ) ) ),
    New Column( "Y", Values( J( n, 1, Random Uniform() ) ) ),
    New Column( "T1", Values( T1 ) ),

);
obj = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :X ), Y( :Y ), Size( :T1 ) ),
    Elements( Points( X, Y, Legend( 16 ) ) )
);

frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Hide Missing Size( true );
```

### [Set Jitter](#set-jitter)[](#set-jitter "Click to copy url")

**Syntax:** obj \<\< Set Jitter( {method, axis, limit, spacing, seed, side, overlap, grid offset, smooth, max error, bandwidth} )

**Description:** Applies an offset to marker positions for collision reduction. method is none\|random uniform\|random normal\|centered\|centered grid\|positive grid. axis is X\|Y\|XY. limit is the width of the jitter, adjusted for the method. spacing is the percentage of the marker size using for jittering or 0 for auto-adjustment.

**JMP Version Added:** 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
r = Oneway( Y( :height ), X( :sex ), Means( 1 ), MeanDiamonds( 1 ), XAxisProportional( 0 ) );
frame = (r << report)[FrameBox( 1 )];
seg = (frame << FindSeg( Marker Seg( 1 ) ));
seg << Set Jitter( {"Grid", "X", 1, 0, 0, "Centered"} );
```

### [Set Label Value Axis](#set-label-value-axis)[](#set-label-value-axis "Click to copy url")

**Syntax:** obj \<\< Set Label Value Axis( "X"\|"Y" )

**Description:** Whether forced labels show the X or Y value.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Bivariate(
    Y( :weight ),
    X( :height ),
    SendToReport(
        Dispatch( {}, "Bivar Plot", FrameBox,
            {DispatchSeg(
                Marker Seg( 1 ),
                Set Force Labels( "Label by Value" ),
                Set Label Value Axis( "X" ),
                Set Label Value Format( "Fixed", 1 )
            )}
        )
    )
);
```

### [Set Label Value Format](#set-label-value-format)[](#set-label-value-format "Click to copy url")

**Syntax:** obj \<\< Set Label Value Format

**Description:** How to format the X or Y value; Auto means use axis format.

**JMP Version Added:** 18

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Bivariate(
    Y( :weight ),
    X( :height ),
    SendToReport(
        Dispatch( {}, "Bivar Plot", FrameBox,
            {DispatchSeg(
                Marker Seg( 1 ),
                Set Force Labels( "Label by Value" ),
                Set Label Value Axis( "X" ),
                Set Label Value Format( "Fixed", 1 )
            )}
        )
    )
);
```

### [Set Label Value Width](#set-label-value-width)[](#set-label-value-width "Click to copy url")

**Syntax:** obj \<\< Set Label Value Width( number )

**Description:** Maximum width for a formatted label value.

**JMP Version Added:** 18

### [Set Marker](#set-marker)[](#set-marker "Click to copy url")

**Syntax:** obj \<\< Set Marker( marker )

**Description:** Sets the marker style for all markers.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Marker( "Square" );
```

### [Set Marker Draw Column](#set-marker-draw-column)[](#set-marker-draw-column "Click to copy url")

**Syntax:** obj \<\< Set Marker Draw Column( column )

**Description:** Sets a custom marker drawing data table column, which could be a picture, matrix of points, text, drawing code or a function.

**JMP Version Added:** 16

``` jsl
Open( "$SAMPLE_DATA/Big Class Families.jmp" );
r = Bivariate( Y( :height ), X( :weight ) );
frame = (r << report)[FrameBox( 1 )];
seg = (frame << FindSeg( Marker Seg( 1 ) ));
Wait( 2 );
seg << Set Marker Draw Column( :sex );
Wait( 2 );
seg << Set Marker Draw Column( :picture );
```

### [Set Marker Draw Expr](#set-marker-draw-expr)[](#set-marker-draw-expr "Click to copy url")

**Syntax:** obj \<\< Set Marker Draw Expr( expr )

**Description:** Sets a custom marker drawing expression, which could be a matrix of points, text, drawing code or a function.

**JMP Version Added:** 16

#### [Drawing function](#drawing-function)[](#drawing-function "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
r = Bivariate( Y( :height ), X( :weight ) );
frame = (r << report)[FrameBox( 1 )];
seg = (frame << FindSeg( Marker Seg( 1 ) ));
seg << Set Marker Draw Expr(
    Function( {this seg, this row, x, y, size, row state},
        If( Mod( this row, 2 ) == 1,
            Line(
                Eval List( {x, y} ),
                Eval List( {:weight[this row + 1], :height[this row + 1]} )
            );
            "A";
        ,
            "B"
        )
    )
);
```

#### [Drawing script](#drawing-script)[](#drawing-script "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
r = Bivariate( Y( :height ), X( :weight ) );
frame = (r << report)[FrameBox( 1 )];
seg = (frame << FindSeg( Marker Seg( 1 ) ));
seg << Set Marker Draw Expr( Expr( Arc( -2, -:age / 3, 2, :age / 3, -90, 90 ) ) );
```

#### [Matrix polyline](#matrix-polyline)[](#matrix-polyline "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
r = Bivariate( Y( :height ), X( :weight ) );
frame = (r << report)[FrameBox( 1 )];
seg = (frame << FindSeg( Marker Seg( 1 ) ));
seg << Set Marker Draw Expr( [-1 0, 0 2, 1 0, 0 1, -1 0] );
```

#### [Text](#text)[](#text "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
r = Bivariate( Y( :height ), X( :weight ) );
frame = (r << report)[FrameBox( 1 )];
seg = (frame << FindSeg( Marker Seg( 1 ) ));
seg << Set Marker Draw Expr( Expr( :sex || Char( :age ) ) );
```

### [Set Marker Size](#set-marker-size)[](#set-marker-size "Click to copy url")

**Syntax:** obj \<\< Set Marker Size

**Description:** Sets the size for the markers. Size options are Dot, Small, Medium, Large, XL, XXL, and XXXL.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Marker Size( "XL" );
Wait( 1 );
seg << Set Marker Size( "dot" );
```

### [Set Overlay Color](#set-overlay-color)[](#set-overlay-color "Click to copy url")

**Syntax:** obj \<\< Set Overlay Color( marker index, color )

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
op = dt << Overlay Plot( X( :age ), Y( :height, :weight ) );
rep = op << report;
frame = rep[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Overlay Color( 1, "Green" );
```

### [Set Overlay Marker](#set-overlay-marker)[](#set-overlay-marker "Click to copy url")

**Syntax:** obj \<\< Set Overlay Marker( marker index, marker )

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
op = dt << Overlay Plot( X( :age ), Y( :height, :weight ) );
rep = op << report;
frame = rep[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Overlay Marker( 1, "Star" );
```

### [Set Transparency](#set-transparency)[](#set-transparency "Click to copy url")

**Syntax:** obj \<\< Set Transparency( number )

**Description:** Sets the marker transparency. The argument should be a numeric value between 0 and 1.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
seg << Set Transparency( .3 );
```

### [Sib](#sib)[](#sib "Click to copy url")

**Syntax:** seg2 = obj \<\< Sib

**Description:** Returns the sibling of the display seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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

**Description:** Sets the marker transparency. The argument should be a numeric value between 0 and 1.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
xx = Column( "height" ) << Get Values;
aa = [=> 0];
sz = Column( "age" ) << get values;
yy = J( N Rows( xx ), 1, 0 );
For( ii = 1, ii <= N Rows( xx ), ii++,
    aa[xx[ii]]++;
    yy[ii] = aa[xx[ii]];
);
New Window( "Marker Seg Example",
    g = Graph Box(
        Frame Size( 300, 120 ),
        X Scale( Min( xx ) - 5, Max( xx ) + 5 ),
        Y Scale( 0, 10 ),
        Marker Seg( xx, yy, Row States( dt ) )
    )
);
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Marker Seg( 1 ) ));
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

[ Previous](MapSeg.html "MapSeg") [Next ](MatrixBox.html "MatrixBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
