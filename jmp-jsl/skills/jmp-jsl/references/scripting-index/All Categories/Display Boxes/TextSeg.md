# TextSeg

*Source: [https://jsl.jmp.com/All%20Categories/Display%20Boxes/TextSeg.html](https://jsl.jmp.com/All%20Categories/Display%20Boxes/TextSeg.html)*

---

# [TextSeg](#textseg)[](#textseg "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Text Seg](#text-seg)[](#text-seg "Click to copy url")

**Syntax:** seg = Text Seg("text")

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Child](#child)[](#child "Click to copy url")

**Syntax:** seg2 = obj \<\< Child

**Description:** Returns the first child of the display seg.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Child; // not many segs support children
```

### [Class Name](#class-name)[](#class-name "Click to copy url")

**Syntax:** classname = obj \<\< Class Name

**Description:** Returns the name of the display class for the display seg.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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

### [Color Theme](#color-theme)[](#color-theme "Click to copy url")

**Syntax:** obj \<\< Color Theme

### [Delete](#delete)[](#delete "Click to copy url")

**Syntax:** obj \<\< Delete

**Description:** Delete the display seg.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Delete;
```

### [Density Gradient](#density-gradient)[](#density-gradient "Click to copy url")

**Syntax:** obj \<\< Density Gradient( "Fade to White"\|"Fade To Gray"\|"Full Color"="Fade to White" )

**Description:** Sets the coloring behavior of density gradients. "Fade to White" by default.

**JMP Version Added:** 15

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Density Gradient( "Fade to Gray" );
```

### [Error Bar Cap](#error-bar-cap)[](#error-bar-cap "Click to copy url")

**Syntax:** obj \<\< Error Bar Cap( "None"\|"Tiny"\|"Small"\|"Medium"\|"Large" )

**Description:** Specifies what type of end cap to put on error bars.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :Age ), Y( :Height ) ),
    Elements( Line( X, Y, Legend( 4 ), Error Bars( "Range" ) ) ), 

);
frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( "Bar Seg" ));
seg << Set Error Bar Cap( "Large" );
```

### [Error Bar Cap Shape](#error-bar-cap-shape)[](#error-bar-cap-shape "Click to copy url")

**Syntax:** obj \<\< Error Bar Cap Shape( begin, end )

**Description:** Specifies the shape of the end cap to display on error bars. A single argument sets the shape for both ends of the bar, or separate arguments can be provided for the start and end. The default shape is "Line". A shape of "Arrow" draws an outward pointing arrow, and "None" omits the cap.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :Age ), Y( :Height ) ),
    Elements( Line( X, Y, Legend( 4 ), Error Bars( "Range" ) ) ), 

);
frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( "Bar Seg" ));
seg << Set Error Bar Cap Shape( "Line", "Arrow" );
```

### [Fill Color](#fill-color)[](#fill-color "Click to copy url")

**Syntax:** obj \<\< Fill Color( color )

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Fill Color( "Green" );
```

### [First Value](#first-value)[](#first-value "Click to copy url")

**Syntax:** obj \<\< First Value( state=0\|1 )

**JMP Version Added:** 16

### [Frame](#frame)[](#frame "Click to copy url")

**Syntax:** FrameBox = obj \<\< Frame

**Description:** Returns the frame box that the display seg is in.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Frame;
```

### [Get Base Font](#get-base-font)[](#get-base-font "Click to copy url")

**Syntax:** font = obj \<\< Get Base Font

**Description:** Returns the base font used for text drawn by the box. Base fonts are predefined names such as Title, Text, Annotation, and others, which are specified in the Preferences for fonts.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Get Base Font;
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

### [Get Density Gradient](#get-density-gradient)[](#get-density-gradient "Click to copy url")

**Syntax:** obj \<\< Get Density Gradient

**Description:** Gets the coloring behavior of density gradients.

**JMP Version Added:** 15

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Density Gradient;
```

### [Get Description](#get-description)[](#get-description "Click to copy url")

**Syntax:** description = obj \<\< Get Description

**Description:** Gets the description for the display seg.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << get description();
```

### [Get Error Bar Cap](#get-error-bar-cap)[](#get-error-bar-cap "Click to copy url")

**Syntax:** obj \<\< Get Error Bar Cap

**Description:** Returns the current kind of error bar end cap.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :Age ), Y( :Height ) ),
    Elements( Line( X, Y, Legend( 4 ), Error Bars( "Range" ) ) ), 

);
frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( "Bar Seg" ));
seg << Get Error Bar Cap();
```

### [Get Error Bar Cap Shape](#get-error-bar-cap-shape)[](#get-error-bar-cap-shape "Click to copy url")

**Syntax:** { begin, end } = obj \<\< Get Error Bar Cap Shape

**Description:** Returns the shape of the end cap on error bars.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :Age ), Y( :Height ) ),
    Elements( Line( X, Y, Legend( 4 ), Error Bars( "Range" ) ) ), 

);
frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( "Bar Seg" ));
seg << Get Error Bar Cap Shape();
```

### [Get Fill Color](#get-fill-color)[](#get-fill-color "Click to copy url")

**Syntax:** color = obj \<\< Get Fill Color

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Fill Color;
```

### [Get Fill Pattern](#get-fill-pattern)[](#get-fill-pattern "Click to copy url")

**Syntax:** obj \<\< Get Fill Pattern

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Fill Pattern;
```

### [Get Font](#get-font)[](#get-font "Click to copy url")

**Syntax:** obj \<\< Get Font

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Get Font;
```

### [Get Font Name](#get-font-name)[](#get-font-name "Click to copy url")

**Syntax:** obj \<\< Get Font Name

**Description:** Returns the name of the font.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Set Font Name( "Times New Roman" );
fontobj << Get Font Name;
```

### [Get Font Scale](#get-font-scale)[](#get-font-scale "Click to copy url")

**Syntax:** obj \<\< Get Font Scale

**Description:** Returns the current scale factor for font.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Get Font Scale;
```

### [Get Font Size](#get-font-size)[](#get-font-size "Click to copy url")

**Syntax:** obj \<\< Get Font Size

**Description:** Returns the size of the font.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Get Font Size;
```

### [Get Font Style](#get-font-style)[](#get-font-style "Click to copy url")

**Syntax:** obj \<\< Get Font Style

**Description:** Returns the font style name.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Set Font Name( "Arial" );
fontobj << Set Font Style( "Italic" );
fontobj << Get Font Style;
```

### [Get Gradient](#get-gradient)[](#get-gradient "Click to copy url")

**Syntax:** obj \<\< Get Gradient

**Description:** Gets the coloring gradient.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient;
```

### [Get Gradient Color Theme](#get-gradient-color-theme)[](#get-gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Get Gradient Color Theme

**Description:** Gets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient Color Theme;
```

### [Get Gradient Discrete Colors](#get-gradient-discrete-colors)[](#get-gradient-discrete-colors "Click to copy url")

**Syntax:** obj \<\< Get Gradient Discrete Colors

**Description:** Gets if each level in a gradient should be a single color or if colors should transition smoothly.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient Legend Horizontal;
```

### [Get Gradient Legend Label Format](#get-gradient-legend-label-format)[](#get-gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Label Format

**Description:** Gets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient Legend Label Format;
```

### [Get Gradient Legend Label Width](#get-gradient-legend-label-width)[](#get-gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Label Width

**Description:** Gets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient Legend Label Width;
```

### [Get Gradient Legend Show Labels](#get-gradient-legend-show-labels)[](#get-gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Show Labels

**Description:** Gets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient Legend Show Labels;
```

### [Get Gradient Level Count](#get-gradient-level-count)[](#get-gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Get Gradient Level Count

**Description:** Gets the number of levels in a gradient.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient Levels;
```

### [Get Gradient Lightness Range](#get-gradient-lightness-range)[](#get-gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Get Gradient Lightness Range

**Description:** Gets the minimum and maximum lightness for level colors in a gradient. Missing values indicate that the color theme's original value is used.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient Reverse Color Order;
```

### [Get Gradient Reverse Label Order](#get-gradient-reverse-label-order)[](#get-gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Get Gradient Reverse Label Order

**Description:** Gets if the order of labels in a gradient is reversed.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient Show Missing;
```

### [Get Gradient Transparency](#get-gradient-transparency)[](#get-gradient-transparency "Click to copy url")

**Syntax:** obj \<\< Get Gradient Transparency

**Description:** Gets the transparency behavior of gradients.

**JMP Version Added:** 15

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Gradient Transparency;
```

### [Get Interval Draw Directions](#get-interval-draw-directions)[](#get-interval-draw-directions "Click to copy url")

**Syntax:** obj \<\< Get Interval Draw Directions

**Description:** Gets the directions in which intervals should be drawn.

**JMP Version Added:** 17

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :age ), Y( :weight ) ),
    Elements(
        Points(
            X,
            Y,
            Legend( 3 ),
            Summary Statistic( "Mean" ),
            Error Interval( "Standard Deviation" )
        )
    ),
    SendToReport(
        Dispatch( {}, "Graph Builder", FrameBox,
            {Reference Line Order( 3 ), DispatchSeg(
                BarSeg( 1 ),
                {Set Interval Draw Directions( "Upper" )}
            )}
        )
    )
);

frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( "Bar Seg" ));
seg << Get Interval Draw Directions;
```

### [Get Line Color](#get-line-color)[](#get-line-color "Click to copy url")

**Syntax:** color = obj \<\< Get Line Color

**Description:** Returns the color of the lines.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Line Color;
```

### [Get Line Style](#get-line-style)[](#get-line-style "Click to copy url")

**Syntax:** pen style = obj \<\< Get Line Style

**Description:** Returns the style of the lines.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Line Style;
```

### [Get Line Width](#get-line-width)[](#get-line-width "Click to copy url")

**Syntax:** number = obj \<\< Get Line Width

**Description:** Returns the width of the lines.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Line Width;
```

### [Get Location](#get-location)[](#get-location "Click to copy url")

**Syntax:** obj \<\< Get Location

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( ts = Text Seg( "moves with axes" ) );
ts << set location( 60, 60 );
ts << get location();
```

### [Get Marker](#get-marker)[](#get-marker "Click to copy url")

**Syntax:** marker = obj \<\< Get Marker

**Description:** Returns the marker style.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Marker;
```

### [Get Marker Size](#get-marker-size)[](#get-marker-size "Click to copy url")

**Syntax:** size = obj \<\< Get Marker Size

**Description:** Returns the size of the markers.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Marker Size;
```

### [Get Relative](#get-relative)[](#get-relative "Click to copy url")

**Syntax:** obj \<\< Get Relative

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "fixed bottom left" ) );
seg << set location( 0, 1 );
seg << set relative( 1, 1 );
seg << get relative();
```

### [Get Text](#get-text)[](#get-text "Click to copy url")

**Syntax:** obj \<\< Get Text

**Description:** Returns the string used by the text seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements(
        Points( X, Y, Legend( 1 ), Jitter( 1 ) ),
        Line Of Fit(
            X,
            Y,
            Legend( 4 ),
            Confidence of Fit( 1 ),
            Confidence of Prediction( 1 ),
            Degree( "Cubic" ),
            Equation( 1 ),
            Root Mean Square Error( 1 ),
            R²( 0 )
        )
    )
);
fontobj = seg = Report( gb )[Framebox( 1 )] << Find Seg( "TextSeg" );
seg << Get Text;
```

### [Get Text Color](#get-text-color)[](#get-text-color "Click to copy url")

**Syntax:** obj \<\< Get Text Color

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Text Color;
```

### [Get Text Style](#get-text-style)[](#get-text-style "Click to copy url")

**Syntax:** obj \<\< Get Text Style

**Description:** Gets how the text is drawn with respect to the cursor pen.

**JMP Version Added:** 17

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y, Legend( 3 ) ), Line Of Fit( X, Y, Legend( 5 ), Equation( 1 ) ) )
);

frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( “Text Seg” ));
seg << Get Text Style;
```

### [Get Transparency](#get-transparency)[](#get-transparency "Click to copy url")

**Syntax:** obj \<\< Get Transparency

**Description:** Returns a numeric value representing transparency between 0 (clear) and 1 (opaque).

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Get Transparency;
```

### [Gradient](#gradient)[](#gradient "Click to copy url")

**Syntax:** obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<Contour Levels(num)\>, \<Reverse Gradient(0\|1)\>, \<Density Gradient("Fade To White"\|"Fade To Gray"\|"Full Color")\>, \<Gradient Transparency("None"\|"Linear")\> } obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<N Labels(num)\>, \<Show Missing Color("On"\|"Off"\|"Auto")\>, \<Scale Type("Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom")\>, \<Scale Values(\[v1, v2, …\])\>, \<Range Type("Default"\|"Exact Data Range"\|"Middle 90%")\>, \<Fill("Between"\|"Above"\|"Below"\|"Above Below")\>, \<Reverse Gradient(0\|1)\>, \<Reverse Labels(0\|1)\>, \<Discrete Color(0\|1)\> }, \<Label Format(labelFormat)\>, \<Width(num)\>, \<Horizontal(0\|1)\>, \<Show Labels(0\|1)\>

**Description:** Sets the coloring gradient.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient( {Color Theme( "Viridis" ), N Labels( 7 )} );
```

### [Gradient Color Theme](#gradient-color-theme)[](#gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Gradient Color Theme

**Description:** Sets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Legend Horizontal( 1 );
```

### [Gradient Legend Label Format](#gradient-legend-label-format)[](#gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Label Format

**Description:** Sets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Legend Label Format( "Fixed Dec", 6, 3 );
```

### [Gradient Legend Label Width](#gradient-legend-label-width)[](#gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Label Width

**Description:** Sets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Legend Label Width( 4 );
```

### [Gradient Legend Show Labels](#gradient-legend-show-labels)[](#gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Show Labels

**Description:** Sets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Legend Show Labels( 0 );
```

### [Gradient Level Count](#gradient-level-count)[](#gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Gradient Level Count

**Description:** Sets the number of levels in a gradient. This is one less than the number of labels.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Levels( 7 );
```

### [Gradient Lightness Range](#gradient-lightness-range)[](#gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Gradient Lightness Range

**Description:** Sets the minimum and maximum lightness for level colors in a gradient. The colors will be scaled to cover this range. A missing value is treated as no change.

**JMP Version Added:** 18

**Example 1**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Lightness Range( Min( 0.25 ), Max( 0.75 ) );
```

**Example 2**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Lightness Range( 0.25, 0.75 );
```

**Example 3**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Reverse Color Order( 1 );
```

### [Gradient Reverse Label Order](#gradient-reverse-label-order)[](#gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Gradient Reverse Label Order

**Description:** Reverses the order of the labels in a gradient.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Gradient Transparency( "None" );
```

### [Last Value](#last-value)[](#last-value "Click to copy url")

**Syntax:** obj \<\< Last Value( state=0\|1 )

**JMP Version Added:** 16

### [Line Color](#line-color)[](#line-color "Click to copy url")

**Syntax:** obj \<\< Line Color( color )

**Description:** Set the color for all lines in the display seg.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Line Color( "Green" );
```

### [Line Style](#line-style)[](#line-style "Click to copy url")

**Syntax:** obj \<\< Line Style( pen style )

**Description:** Sets the style of the lines. Options are Solid, Dotted, Dashed, DashDot, and DashDotDot.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Line Style( "Dotted" );
```

### [Line Width](#line-width)[](#line-width "Click to copy url")

**Syntax:** obj \<\< Line Width( "1"\|"2"\|"3"\|"4"\|"5"\|"6"\|"Other..." )

**Description:** Sets the width of the lines.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Line Width( 3 );
```

### [Marker](#marker)[](#marker "Click to copy url")

**Syntax:** obj \<\< Marker( marker )

**Description:** Sets the marker style for all markers.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Marker( "Square" );
```

### [Marker Size](#marker-size)[](#marker-size "Click to copy url")

**Syntax:** obj \<\< Marker Size( size )

**Description:** Sets the size for the markers. Size options are Dot, Small, Medium, Large, XL, XXL, and XXXL.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Marker( "Square" );
seg << Set Marker Size( "XL" );
```

### [Max Value](#max-value)[](#max-value "Click to copy url")

**Syntax:** obj \<\< Max Value( state=0\|1 )

**JMP Version Added:** 16

### [Min Value](#min-value)[](#min-value "Click to copy url")

**Syntax:** obj \<\< Min Value( state=0\|1 )

**JMP Version Added:** 16

### [Name](#name)[](#name "Click to copy url")

**Syntax:** obj \<\< Name( state=0\|1 )

**JMP Version Added:** 16

### [Parent](#parent)[](#parent "Click to copy url")

**Syntax:** seg2 = obj \<\< Parent

**Description:** Returns the parent of the display seg.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Parent;
```

### [Revert](#revert)[](#revert "Click to copy url")

**Syntax:** obj \<\< Revert

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Revert;
```

### [Set Base Font](#set-base-font)[](#set-base-font "Click to copy url")

**Syntax:** obj \<\< Set Base Font( "Text"\|"Heading"\|"Title"\|"Small"\|"Mono"\|"Formula Editor"\|"Annotation"\|"Axis"\|"Marker"\|"Axis Title"\|"Graph Label"\|"Legend"\|"Graph Title"\|"Caption"\|"Data Table"\|"Hover Label" )

**Description:** Sets the base font for text drawn by the box.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
Wait( 2 );
fontobj << Set Base Font( "Title" );
```

### [Set Description](#set-description)[](#set-description "Click to copy url")

**Syntax:** obj \<\< Set Description( description )

**Description:** Sets the description for the display seg.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << set description( "my seg" );
```

### [Set Error Bar Cap](#set-error-bar-cap)[](#set-error-bar-cap "Click to copy url")

**Syntax:** obj \<\< Set Error Bar Cap( "None"\|"Tiny"\|"Small"\|"Medium"\|"Large" )

**Description:** Specifies what type of end cap to put on error bars.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :Age ), Y( :Height ) ),
    Elements( Line( X, Y, Legend( 4 ), Error Bars( "Range" ) ) ), 

);
frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( "Bar Seg" ));
seg << Set Error Bar Cap( "Large" );
```

### [Set Error Bar Cap Shape](#set-error-bar-cap-shape)[](#set-error-bar-cap-shape "Click to copy url")

**Syntax:** obj \<\< Set Error Bar Cap Shape( begin, end )

**Description:** Specifies the shape of the end cap to display on error bars. A single argument sets the shape for both ends of the bar, or separate arguments can be provided for the start and end. The default shape is "Line". A shape of "Arrow" draws an outward pointing arrow, and "None" omits the cap.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :Age ), Y( :Height ) ),
    Elements( Line( X, Y, Legend( 4 ), Error Bars( "Range" ) ) ), 

);
frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( "Bar Seg" ));
seg << Set Error Bar Cap Shape( "Line", "Arrow" );
```

### [Set Fill Color](#set-fill-color)[](#set-fill-color "Click to copy url")

**Syntax:** obj \<\< Set Fill Color( color )

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Fill Color( "Green" );
```

### [Set Fill Pattern](#set-fill-pattern)[](#set-fill-pattern "Click to copy url")

**Syntax:** obj \<\< Set Fill Pattern

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Fill Pattern( "h wave medium" );
```

### [Set Font](#set-font)[](#set-font "Click to copy url")

**Syntax:** obj \<\< Set Font( fontName, \<size\>, \<"bold italic underline strikeout"\>, \<angle\> )

**Example 1**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Set Font( "Arial Black" );
```

**Example 2**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Set Font( "Arial Black", 12, "Italic Underline" );
```

### [Set Font Name](#set-font-name)[](#set-font-name "Click to copy url")

**Syntax:** obj \<\< Set Font Name( fontname )

**Description:** Sets the font for text strings.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Set Font Name( "Arial Black" );
```

### [Set Font Scale](#set-font-scale)[](#set-font-scale "Click to copy url")

**Syntax:** obj \<\< Set Font Scale( f )

**Description:** Sets a scale factor for the current font. The scale factor will be applied to the size that is determined from the base font and point size.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
Wait( 2 );
fontobj << Set Font Scale( 2.0 );
```

### [Set Font Size](#set-font-size)[](#set-font-size "Click to copy url")

**Syntax:** obj \<\< Set Font Size( n )

**Description:** Sets the font size in points for text strings.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Set Font Size( 14 );
```

### [Set Font Style](#set-font-style)[](#set-font-style "Click to copy url")

**Syntax:** obj \<\< Set Font Style( style )

**Description:** Sets the font style for text strings. To set more than one style at once, place them in the same string, separated by spaces (see Example 2 below).

**Example 1**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Set Font Style( "Italic" );
```

**Example 2**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
fontobj << Set Font Style( "Italic Bold Underline" );
```

### [Set Gradient](#set-gradient)[](#set-gradient "Click to copy url")

**Syntax:** obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<Contour Levels(num)\>, \<Reverse Gradient(0\|1)\>, \<Density Gradient("Fade To White"\|"Fade To Gray"\|"Full Color")\>, \<Gradient Transparency("None"\|"Linear")\> } obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<N Labels(num)\>, \<Show Missing Color("On"\|"Off"\|"Auto")\>, \<Scale Type("Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom")\>, \<Scale Values(\[v1, v2, …\])\>, \<Range Type("Default"\|"Exact Data Range"\|"Middle 90%")\>, \<Fill("Between"\|"Above"\|"Below"\|"Above Below")\>, \<Reverse Gradient(0\|1)\>, \<Reverse Labels(0\|1)\>, \<Discrete Color(0\|1)\> }, \<Label Format(labelFormat)\>, \<Width(num)\>, \<Horizontal(0\|1)\>, \<Show Labels(0\|1)\>

**Description:** Sets the coloring gradient.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient( {Color Theme( "Viridis" ), N Labels( 7 )} );
```

### [Set Gradient Color Theme](#set-gradient-color-theme)[](#set-gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Set Gradient Color Theme

**Description:** Sets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Color Theme( "Viridis" );
```

### [Set Gradient Custom Scale](#set-gradient-custom-scale)[](#set-gradient-custom-scale "Click to copy url")

**Syntax:** obj \<\< Set Gradient Custom Scale

**Description:** Sets the gradient to use a list of values for a custom scale.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Legend Horizontal( 1 );
```

### [Set Gradient Legend Label Format](#set-gradient-legend-label-format)[](#set-gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Label Format

**Description:** Sets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Legend Label Format( "Fixed Dec", 6, 3 );
```

### [Set Gradient Legend Label Width](#set-gradient-legend-label-width)[](#set-gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Label Width

**Description:** Sets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Legend Label Width( 4 );
```

### [Set Gradient Legend Show Labels](#set-gradient-legend-show-labels)[](#set-gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Show Labels

**Description:** Sets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Legend Show Labels( 0 );
```

### [Set Gradient Level Count](#set-gradient-level-count)[](#set-gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Set Gradient Level Count

**Description:** Sets the number of levels in a gradient. This is one less than the number of labels.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Levels( 7 );
```

### [Set Gradient Lightness Range](#set-gradient-lightness-range)[](#set-gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Set Gradient Lightness Range

**Description:** Sets the minimum and maximum lightness for level colors in a gradient. The colors will be scaled to cover this range. A missing value is treated as no change.

**JMP Version Added:** 18

**Example 1**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Lightness Range( Min( 0.25 ), Max( 0.75 ) );
```

**Example 2**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Lightness Range( 0.25, 0.75 );
```

**Example 3**

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Gradient Reverse Color Order( 1 );
```

### [Set Gradient Reverse Label Order](#set-gradient-reverse-label-order)[](#set-gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Set Gradient Reverse Label Order

**Description:** Reverses the order of the labels in a gradient.

**JMP Version Added:** 18

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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

### [Set Interval Draw Directions](#set-interval-draw-directions)[](#set-interval-draw-directions "Click to copy url")

**Syntax:** obj \<\< Set Interval Draw Directions( Both\|Upper\|Lower\|None )

**Description:** Sets the directions in which intervals should be drawn.

**JMP Version Added:** 17

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :age ), Y( :weight ) ),
    Elements(
        Points(
            X,
            Y,
            Legend( 3 ),
            Summary Statistic( "Mean" ),
            Error Interval( "Standard Deviation" )
        )
    ),
    SendToReport(
        Dispatch( {}, "Graph Builder", FrameBox,
            {Reference Line Order( 3 ), DispatchSeg(
                BarSeg( 1 ),
                {Set Interval Draw Directions( "Upper" )}
            )}
        )
    )
);

frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( "Bar Seg" ));
seg << Set Interval Draw Directions( "Lower" );
```

### [Set Line Color](#set-line-color)[](#set-line-color "Click to copy url")

**Syntax:** obj \<\< Set Line Color( color )

**Description:** Set the color for all lines in the display seg.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Line Color( "Green" );
```

### [Set Line Style](#set-line-style)[](#set-line-style "Click to copy url")

**Syntax:** obj \<\< Set Line Style( pen style )

**Description:** Sets the style of the lines. Options are Solid, Dotted, Dashed, DashDot, and DashDotDot.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Line Style( "Dotted" );
```

### [Set Line Width](#set-line-width)[](#set-line-width "Click to copy url")

**Syntax:** obj \<\< Set Line Width( "1"\|"2"\|"3"\|"4"\|"5"\|"6"\|"Other..." )

**Description:** Sets the width of the lines.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Line Width( 3 );
```

### [Set Location](#set-location)[](#set-location "Click to copy url")

**Syntax:** obj \<\< Set Location

**Description:** Sets the location of the text. If Relative is set, the 0,0 will be the top left and 1,1 will be the bottom right. If Relative is not set, then the coordinates will be relative to the axes.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "fixed bottom left" ) );
seg << set location( 0, 1 );
seg << set relative( 1, 1 );
w[FrameBox( 1 )] << append seg( ts2 = Text Seg( "moves with axes" ) );
ts2 << set location( 60, 60 );
ts2 << get location();
```

### [Set Marker](#set-marker)[](#set-marker "Click to copy url")

**Syntax:** obj \<\< Set Marker( marker )

**Description:** Sets the marker style for all markers.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Marker( "Square" );
```

### [Set Marker Size](#set-marker-size)[](#set-marker-size "Click to copy url")

**Syntax:** obj \<\< Set Marker Size( size )

**Description:** Sets the size for the markers. Size options are Dot, Small, Medium, Large, XL, XXL, and XXXL.

**JMP Version Added:** 14

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Marker( "Square" );
seg << Set Marker Size( "XL" );
```

### [Set Relative](#set-relative)[](#set-relative "Click to copy url")

**Syntax:** obj \<\< Set Relative( 0\|1,0\|1 )

**Description:** A value of 0 means the x or y coordinate will be relative to the frame box and a value of 1 means the x or y value will be relative to the axes. When relative is set to 0, the x and y coordinates will map from 0,0 to 1,1 for the top left to bottom right of the graph box.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "fixed bottom left" ) );
seg << set location( 0, 1 );
seg << set relative( 1, 1 );
w[FrameBox( 1 )] << append seg( ts2 = Text Seg( "moves with axes" ) );
ts2 << set location( 60, 60 );
```

### [Set Text](#set-text)[](#set-text "Click to copy url")

**Syntax:** obj \<\< Set Text( text )

**Description:** Sets the string used by the text seg.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements(
        Points( X, Y, Legend( 1 ), Jitter( 1 ) ),
        Line Of Fit(
            X,
            Y,
            Legend( 4 ),
            Confidence of Fit( 1 ),
            Confidence of Prediction( 1 ),
            Degree( "Cubic" ),
            Equation( 1 ),
            Root Mean Square Error( 1 ),
            R²( 0 )
        )
    )
);
g = Report( gb );
fontobj = seg = g[Framebox( 1 )] << Find Seg( "TextSeg" );
seg << Get Text;
seg << Set Text( seg << Get Text || "  Tallest: Lawrence" );
```

### [Set Text Alignment](#set-text-alignment)[](#set-text-alignment "Click to copy url")

**Syntax:** obj \<\< Set Text Alignment( left\|center\|right,\<top\|center\|bottom\> )

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "center" ) );
seg << set relative( 1, 1 );
seg << set location( .5, .5 );
seg << set text alignment( center, center );
```

### [Set Text Color](#set-text-color)[](#set-text-color "Click to copy url")

**Syntax:** obj \<\< Set Text Color( color )

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Text Color( "Green" );
```

### [Set Text Style](#set-text-style)[](#set-text-style "Click to copy url")

**Syntax:** obj \<\< Set Text Style( \[Left\|Center\|Right\], \[Top\|VCenter\|Baseline\|Bottom\], \[Erased\], \[Boxed\] )

**Description:** Sets how the text is drawn with respect to the cursor pen. When supported, "Erased" fills the bounding box of the text and "Erased" outlines it. If not specified, the default horizontal alignment is "Left" and vertical is "Baseline".

**JMP Version Added:** 17

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y, Legend( 3 ) ), Line Of Fit( X, Y, Legend( 5 ), Equation( 1 ) ) )
);

frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( “Text Seg” ));
seg << Set Text Style( {Center, VCenter} );
```

### [Set Transparency](#set-transparency)[](#set-transparency "Click to copy url")

**Syntax:** obj \<\< Set Transparency( number )

**Description:** Sets the shape transparency. The argument should be a numeric value between 0 and 1.

**JMP Version Added:** 16

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Transparency( .3 );
```

### [Sib](#sib)[](#sib "Click to copy url")

**Syntax:** seg2 = obj \<\< Sib

**Description:** Returns the sibling of the display seg.

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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

### [Text Color](#text-color)[](#text-color "Click to copy url")

**Syntax:** obj \<\< Text Color( color )

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
seg << Set Text Color( "Green" );
```

### [Text Style](#text-style)[](#text-style "Click to copy url")

**Syntax:** obj \<\< Text Style( \[Left\|Center\|Right\], \[Top\|VCenter\|Baseline\|Bottom\], \[Erased\], \[Boxed\] )

**Description:** Sets how the text is drawn with respect to the cursor pen. When supported, "Erased" fills the bounding box of the text and "Erased" outlines it. If not specified, the default horizontal alignment is "Left" and vertical is "Baseline".

**JMP Version Added:** 17

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Graph Builder(
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y, Legend( 3 ) ), Line Of Fit( X, Y, Legend( 5 ), Equation( 1 ) ) )
);

frame = Report( obj )[FrameBox( 1 )];
seg = (frame << Find Seg( “Text Seg” ));
seg << Set Text Style( {Center, VCenter} );
```

### [Transparency](#transparency)[](#transparency "Click to copy url")

**Syntax:** obj \<\< Transparency( number )

**Description:** Sets the shape transparency. The argument should be a numeric value between 0 and 1.

**JMP Version Added:** 16

``` jsl
w = New Window( "test", Graph Box( FrameSize( 400, 400 ), ) );
w[FrameBox( 1 )] << append seg( seg = Text Seg( "default location fixed bottom left" ) );
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

[ Previous](TextEditBox.html "TextEditBox") [Next ](TextTruncatorBox.html "TextTruncatorBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
