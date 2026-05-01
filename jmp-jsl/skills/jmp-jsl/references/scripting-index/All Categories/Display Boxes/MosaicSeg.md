# MosaicSeg

*Source: [https://jsl.jmp.com/All%20Categories/Display%20Boxes/MosaicSeg.html](https://jsl.jmp.com/All%20Categories/Display%20Boxes/MosaicSeg.html)*

---

# [MosaicSeg](#mosaicseg)[](#mosaicseg "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Add Graphics Script](#add-graphics-script)[](#add-graphics-script "Click to copy url")

**Syntax:** obj \<\< Add Graphics Script( \<"Back" \| "Front" \| position\>, \<Description("name")\>, \<"Selected Layer"\>, \<Scale IDs(XID, YID)\>, script )

**Description:** Enter a script that will draw inside this frame. Selected elements are always above unselected elements. If you specify a selected layer, this script is called during the second drawing pass, when selected elements are drawn.

**Example 1**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = Bivariate( Y( :weight ), X( :height ), FitLine );
rbiv = biv << report;
framebox = rbiv[frame box( 1 )];
framebox << Add Graphics Script(
    Transparency( 0.5 );
    Fill Color( {1.0, 0.5, 0.0} );
    Polygon( [60, 72, 57], [75, 120, 120] );
);
```

**Example 2**

``` jsl

gbox = Graph Box(
    Frame Size( 300, 300 ),
    X Axis( Scale ID( 1 ), Side( 1 ), Min( 1 ), Max( 100 ), Inc( 5 ) ),
    X Axis( Scale ID( 2 ), Side( 2 ), Min( 4 ), Max( 50 ), Inc( 3 ) ),
    Y Axis( Scale ID( 3 ), Min( -100 ), Max( 200 ) ),
    Y Axis( Scale ID( 4 ), Side( 2 ), Min( 1 ), Max( 10 ), Inc( 1 ) ), 

);

fbox = gbox[frame box( 1 )];

fbox << Add Graphics Script(
    Scale IDs( 1, 4 ), //use scale ID's 1 and 4 for this graphics script
    Pen Color( "Green" );
    Line( [20 50 80], [4 3 6] );
);
New Window( "Example", gbox );
```

**Example 3**

``` jsl
table = New Table( "test table",
    Add Rows( 150000 ),
    <<New Column( "X", "Numeric", <<Set Each Value( Random Normal() ) ),
    <<New Column( "Y", "Numeric", <<Set Each Value( Random Normal() ) )
);
b = Bivariate( X( :x ), Y( :y ) );
table << select rows( 1 :: 10000 );
Report( b )[Frame Box( 1 )] << Add Graphics Script(
    Description( "Red Line Above Selected" ),
    "selected layer",
    Pen Color( "Red" );
    Pen Size( 5 );
    Line( [-5, 5], [-5, 5] );
);
Report( b )[Frame Box( 1 )] << Add Graphics Script(
    Description( "Green Line Below Selected Above Unselected" ),
    Pen Color( "Green" );
    Pen Size( 3 );
    Line( [5, -5], [-5, 5] );
);
```

### [Add Image](#add-image)[](#add-image "Click to copy url")

**Syntax:** obj \<\< Add Image( image \| open("image filename"), \<bounds( left(value), top(value), bottom(value), right(value) ) \| move(centerX, centerY)\> )

**Description:**

Adds an image to the frame.

You can reference an existing image (already created via a new image() or open() command) or you can specify an image file directly with the open() parameter. The image can be positioned in the frame by the move() command, which specifies where to place the center of the image based on the axes units. Or the image can be sized and placed in the frame by specifying the bounds().

``` jsl
img = Open( "$SAMPLE_IMAGES/windmap.png", "png" );
w = New Window( "View Image",
    Graph Box(
        FrameSize( 500, 500 ),
        X Scale( 0, 100 ),
        Y Scale( 0, 100 ),
        <<Add Image(
            image( img ),
            bounds( top( 90 ), Left( 10 ), bottom( 10 ), Right( 90 ) )
        )
    )
);
```

### [Append Seg](#append-seg)[](#append-seg "Click to copy url")

**Syntax:** obj \<\< Append Seg( display seg )

**Description:** Adds a display seg to the FrameBox

``` jsl
x = [20, 40, 60, 80];
New Window( "Example",
    Graph Box( Frame Size( 300, 120 ), Append Seg( Marker Seg( x, x ), Line Seg( x, x ) ) ),
    Graph Box( Frame Size( 300, 120 ) )
);
gb2 = Current Report()[FrameBox( 2 )];
gb2 << append seg( Current Report()[FrameBox( 1 )] << find seg( Marker Seg( 1 ) ) );
```

### [Background Map](#background-map)[](#background-map "Click to copy url")

**Syntax:** obj \<\< Background Map( \<Images("None" \| "Simple Earth" \| "Detailed Earth" \| "Nasa Server" \| ("Web Map Service", url, layer) , \<Transparency(0-1)\> )\> \| \<Boundaries("None" \| Shape File)\> )

**Description:**

Adds a background map to the frame.

Images are rasterized maps and support transparency. Boundaries are vector maps, defined by a shape file, and can be created by a user. You can specify either an image or a boundary or both.

``` jsl
dt = Open( "$SAMPLE_DATA/Hurricanes.jmp" );
plot = Bubble Plot(
    X( :Longitude ),
    Y( :Latitude ),
    Sizes( :"Wind (Knots)"n ),
    Time( :Date ),
    Coloring( :Landfall in USA ),
    ID( :Name and ID ),
    Speed( 1 ),
    Time Index( 2117.70195 ),
    Trail Bubbles( 1 ),
    All Labels( 0 ),
    No Labels( 0 ),
    Title Position( -88.679, 59.73 )
);
rplot = plot << report;
framebox = rplot[Frame Box( 1 )];
framebox << Background Map(
    Images( "Simple Earth", Transparency( 0.7 ) ),
    Boundaries( "World" )
);
```

### [Bottom](#bottom)[](#bottom "Click to copy url")

**Syntax:** obj \<\< Bottom( state=0\|1 )

**Description:** Shows or hides a border on the bottom of the frame.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Bottom( 0 );
```

### [Cell Labeling](#cell-labeling)[](#cell-labeling "Click to copy url")

**Syntax:** obj \<\< Cell Labeling( "No Labels"\|"Label by Count"\|"Label by Percent"\|"Label by Value"\|"Label by Row" )

**JMP Version Added:** 15

### [Child Seg](#child-seg)[](#child-seg "Click to copy url")

**Syntax:** obj \<\< Child Seg

**Description:** Returns the display seg child of the Framebox

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = Bivariate( Y( :weight ), X( :height ), FitLine );
rbiv = biv << report;
rbiv[Frame Box( 1 )] << Child Seg();
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

### [Copy Customizations](#copy-customizations)[](#copy-customizations "Click to copy url")

**Syntax:** obj \<\< Copy Customizations

**Description:** Copy a script that contains graph customizations.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv1 = biv << report;
rbiv2 = rbiv1 << Clone Box;
rbiv1 << append( rbiv2 );
framebox1 = rbiv1[Frame Box( 1 )];
framebox2 = rbiv2[Frame Box( 1 )];
framebox1 << Marker Drawing Mode( outlined );
framebox1 << Copy Customizations;
framebox2 << Paste Customizations;
```

### [Copy Frame Contents](#copy-frame-contents)[](#copy-frame-contents "Click to copy url")

**Syntax:** obj \<\< Copy Frame Contents

**Description:** Create Journal text containing settings for this frame and copy it to the clipboard.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv1 = biv << report;
rbiv2 = rbiv1 << Clone Box;
rbiv1 << append( rbiv2 );
framebox1 = rbiv1[Frame Box( 1 )];
framebox2 = rbiv2[Frame Box( 1 )];
biv << Fit Line;
framebox1 << Copy Frame Contents;
framebox2 << Paste Frame Contents;
```

### [Copy Frame Settings](#copy-frame-settings)[](#copy-frame-settings "Click to copy url")

**Syntax:** obj \<\< Copy Frame Settings

**Description:** Create a script containing settings for this frame, and copy it to the clipboard.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv1 = biv << report;
rbiv2 = rbiv1 << Clone Box;
rbiv1 << append( rbiv2 );
framebox1 = rbiv1[Frame Box( 1 )];
framebox2 = rbiv2[Frame Box( 1 )];
framebox1 << Background Color( "Green" );
framebox1 << Copy Frame Settings;
framebox2 << Paste Frame Settings;
```

### [Copy Polygons](#copy-polygons)[](#copy-polygons "Click to copy url")

**Syntax:** obj \<\< Copy Polygons

**Description:** Saves a copy of the polygons located on the frame to the clipboard.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
pa = framebox << Add Polygon Annotation(
    Points( {144, 53}, {182, 30}, {213, 80}, {181, 95} )
);
pa << Closed( 1 );
framebox << Copy Polygons;
```

### [Customize](#customize)[](#customize "Click to copy url")

**Syntax:** obj \<\< Customize

**Description:** Change the properties of the graph contents.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Customize;
```

### [Density Gradient](#density-gradient)[](#density-gradient "Click to copy url")

**Syntax:** obj \<\< Density Gradient( "Fade to White"\|"Fade To Gray"\|"Full Color"="Fade to White" )

**Description:** Sets the coloring behavior of density gradients. "Fade to White" by default.

**JMP Version Added:** 15

``` jsl
seg << Density Gradient( "Fade to Gray" );
```

### [Dispatch Segs](#dispatch-segs)[](#dispatch-segs "Click to copy url")

**Syntax:** obj \<\< Dispatch Segs( command )

**Description:** Sends command to all visual elements ('segs') in the display box.

**JMP Version Added:** 15

### [DispatchSeg](#dispatchseg)[](#dispatchseg "Click to copy url")

**Syntax:** obj \<\< DispatchSeg( command )

**Description:** Sends command to the display box.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Distribution(
    Continuous Distribution( Column( :weight ), Fit Distribution( Normal ) ),
    Nominal Distribution( Column( :age ) ),
    SendToReport(
        Dispatch( {"weight"}, "Distrib Histogram", FrameBox,
            {DispatchSeg(
                Hist Seg( 1 ),
                {Line Style( "Dotted" ), Fill Color( {0, 128, 0} ), Histogram Color( -32768 )
                }
            ), DispatchSeg( Line Seg( 1 ), {Line Color( {0, 0, 255} ), Line Width( 5 )} )}
        )
    )
);
```

### [Edit Graphics Script](#edit-graphics-script)[](#edit-graphics-script "Click to copy url")

**Syntax:** obj \<\< Edit Graphics Script

**Description:** Edit scripts already installed in this frame.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = Bivariate( Y( :weight ), X( :height ), FitLine );
rbiv = biv << report;
framebox = rbiv[frame box( 1 )];
framebox << Add Graphics Script(
    Transparency( 0.5 );
    Fill Color( {1.0, 0.5, 0.0} );
    Polygon( [60, 72, 57], [75, 120, 120] );
);
framebox << Edit Graphics Script;
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

### [Fill Selection Mode](#fill-selection-mode)[](#fill-selection-mode "Click to copy url")

**Syntax:** obj \<\< Fill Selection Mode( "Preferred Mode"\|"Selected Patterned"\|"Selected Darker"\|"Selected Outlined"\|"Selected Same Color"\|"Unselected Faded" )

**Description:** Sets the selection style for fills.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dist = Distribution( Continuous Distribution( Column( :height ) ), Histograms Only );
rdist = dist << report;
dt << Select Where( dt:age == 12 );
framebox = rdist[Frame Box( 1 )];
framebox << Fill Selection Mode( "Selected Darker" );
```

### [Find Seg](#find-seg)[](#find-seg "Click to copy url")

**Syntax:** obj \<\< Find Seg( display seg )

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = Bivariate( Y( :weight ), X( :height ), FitLine );
rbiv = biv << report;
ms = rbiv[Frame Box( 1 )] << Find Seg( Marker Seg( 1 ) );
ms << delete;
```

### [Find Segs](#find-segs)[](#find-segs "Click to copy url")

**Syntax:** obj \<\< Find Segs

**JMP Version Added:** 15

### [First Value](#first-value)[](#first-value "Click to copy url")

**Syntax:** obj \<\< First Value( state=0\|1 )

**JMP Version Added:** 16

### [Frame Size](#frame-size)[](#frame-size "Click to copy url")

**Syntax:** obj \<\< Frame Size

**Description:** Change the frame size.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Frame Size( 300, 300 );
```

### [Get Background Fill](#get-background-fill)[](#get-background-fill "Click to copy url")

**Syntax:** obj \<\< Get Background Fill

**Description:** Returns the state (0\|1) of the background fill color of graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( weight ), x( height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
//Set background color
framebox << Background Color( "red" );
//Wait to see the color change
Wait( 1 );
//Turn off background fill color
framebox << Set Background Fill( 0 );
val1 = framebox << Get Background Fill;
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
seg << Get Density Gradient;
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

### [Get Fill Selection Mode](#get-fill-selection-mode)[](#get-fill-selection-mode "Click to copy url")

**Syntax:** obj \<\< Get Fill Selection Mode

**Description:** Returns the selection style for fills.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dist = Distribution( Continuous Distribution( Column( :height ) ), Histograms Only );
rdist = dist << report;
dt << Select Where( dt:age == 12 );
framebox = rdist[Frame Box( 1 )];
framebox << Fill Selection Mode( "Selected Darker" );
framebox << Get Fill Selection Mode;
```

### [Get Gradient](#get-gradient)[](#get-gradient "Click to copy url")

**Syntax:** obj \<\< Get Gradient

**Description:** Gets the coloring gradient.

``` jsl
seg << Get Gradient;
```

### [Get Gradient Color Theme](#get-gradient-color-theme)[](#get-gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Get Gradient Color Theme

**Description:** Gets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
seg << Get Gradient Color Theme;
```

### [Get Gradient Discrete Colors](#get-gradient-discrete-colors)[](#get-gradient-discrete-colors "Click to copy url")

**Syntax:** obj \<\< Get Gradient Discrete Colors

**Description:** Gets if each level in a gradient should be a single color or if colors should transition smoothly.

**JMP Version Added:** 18

``` jsl
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
seg << Get Gradient Legend Horizontal;
```

### [Get Gradient Legend Label Format](#get-gradient-legend-label-format)[](#get-gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Label Format

**Description:** Gets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
seg << Get Gradient Legend Label Format;
```

### [Get Gradient Legend Label Width](#get-gradient-legend-label-width)[](#get-gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Label Width

**Description:** Gets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
seg << Get Gradient Legend Label Width;
```

### [Get Gradient Legend Show Labels](#get-gradient-legend-show-labels)[](#get-gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Get Gradient Legend Show Labels

**Description:** Gets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
seg << Get Gradient Legend Show Labels;
```

### [Get Gradient Level Count](#get-gradient-level-count)[](#get-gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Get Gradient Level Count

**Description:** Gets the number of levels in a gradient.

**JMP Version Added:** 18

``` jsl
seg << Get Gradient Levels;
```

### [Get Gradient Lightness Range](#get-gradient-lightness-range)[](#get-gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Get Gradient Lightness Range

**Description:** Gets the minimum and maximum lightness for level colors in a gradient. Missing values indicate that the color theme's original value is used.

**JMP Version Added:** 18

``` jsl
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
seg << Get Gradient Reverse Color Order;
```

### [Get Gradient Reverse Label Order](#get-gradient-reverse-label-order)[](#get-gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Get Gradient Reverse Label Order

**Description:** Gets if the order of labels in a gradient is reversed.

**JMP Version Added:** 18

``` jsl
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
seg << Get Gradient Show Missing;
```

### [Get Gradient Transparency](#get-gradient-transparency)[](#get-gradient-transparency "Click to copy url")

**Syntax:** obj \<\< Get Gradient Transparency

**Description:** Gets the transparency behavior of gradients.

**JMP Version Added:** 15

``` jsl
seg << Get Gradient Transparency;
```

### [Get Image](#get-image)[](#get-image "Click to copy url")

**Syntax:** image = obj \<\< Get Image

**Description:** Returns a reference to the background image.

``` jsl
Open( "$SAMPLE_DATA/Animals.jmp" );
op = Overlay Plot( X( :subject ), Y( :miles ), Separate Axes( 1 ) );
opr = op << report;
fb = opr[Frame Box( 1 )];
fb << Add Image(
    Open( Convert File Path( "$SAMPLE_IMAGES/black rhino footprint.jpg" ) ),
    Transparency( 0.9 ),
    Rotate( 90 ),
    Bounds(
        Left( 0.135416666666667 ),
        Right( 3.26041666666667 ),
        Top( 11.8333333333333 ),
        Bottom( -1 )
    ),
    SetSize( {300, 210} )
);
fb << Marker Size( 8 );
Print( fb << Get Image );
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
seg << Get Line Color;
```

### [Get Line Style](#get-line-style)[](#get-line-style "Click to copy url")

**Syntax:** pen style = obj \<\< Get Line Style

**Description:** Returns the style of the lines.

**JMP Version Added:** 14

``` jsl
seg << Get Line Style;
```

### [Get Line Width](#get-line-width)[](#get-line-width "Click to copy url")

**Syntax:** number = obj \<\< Get Line Width

**Description:** Returns the width of the lines.

**JMP Version Added:** 14

``` jsl
seg << Get Line Width;
```

### [Get Marker](#get-marker)[](#get-marker "Click to copy url")

**Syntax:** marker = obj \<\< Get Marker

**Description:** Returns the marker style.

**JMP Version Added:** 14

``` jsl
seg << Get Marker;
```

### [Get Marker Selection Mode](#get-marker-selection-mode)[](#get-marker-selection-mode "Click to copy url")

**Syntax:** obj \<\< Get Marker Selection Mode

**Description:** Returns the marker selection style.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Where( dt:age == 12 );
framebox = rbiv[Frame Box( 1 )];
framebox << Marker Selection Mode( "Selected Haloed" );
framebox << Get Marker Selection Mode;
```

### [Get Marker Size](#get-marker-size)[](#get-marker-size "Click to copy url")

**Syntax:** size = obj \<\< Get Marker Size

**Description:** Returns the size of the markers.

**JMP Version Added:** 14

``` jsl
seg << Get Marker Size;
```

### [Get Polygons](#get-polygons)[](#get-polygons "Click to copy url")

**Syntax:** obj \<\< Get Polygons

**Description:** Returns a list of polygons located on the frame.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
pa = framebox << Add Polygon Annotation(
    Points( {144, 53}, {182, 30}, {213, 80}, {181, 95} )
);
pa << Closed( 1 );
Print( framebox << Get Polygons );
```

### [Gradient](#gradient)[](#gradient "Click to copy url")

**Syntax:** obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<Contour Levels(num)\>, \<Reverse Gradient(0\|1)\>, \<Density Gradient("Fade To White"\|"Fade To Gray"\|"Full Color")\>, \<Gradient Transparency("None"\|"Linear")\> } obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<N Labels(num)\>, \<Show Missing Color("On"\|"Off"\|"Auto")\>, \<Scale Type("Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom")\>, \<Scale Values(\[v1, v2, …\])\>, \<Range Type("Default"\|"Exact Data Range"\|"Middle 90%")\>, \<Fill("Between"\|"Above"\|"Below"\|"Above Below")\>, \<Reverse Gradient(0\|1)\>, \<Reverse Labels(0\|1)\>, \<Discrete Color(0\|1)\> }, \<Label Format(labelFormat)\>, \<Width(num)\>, \<Horizontal(0\|1)\>, \<Show Labels(0\|1)\>

**Description:** Sets the coloring gradient.

``` jsl
seg << Set Gradient( {Color Theme( "Viridis" ), N Labels( 7 )} );
```

### [Gradient Color Theme](#gradient-color-theme)[](#gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Gradient Color Theme

**Description:** Sets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
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
seg << Set Gradient Legend Horizontal( 1 );
```

### [Gradient Legend Label Format](#gradient-legend-label-format)[](#gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Label Format

**Description:** Sets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
seg << Set Gradient Legend Label Format( "Fixed Dec", 6, 3 );
```

### [Gradient Legend Label Width](#gradient-legend-label-width)[](#gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Label Width

**Description:** Sets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
seg << Set Gradient Legend Label Width( 4 );
```

### [Gradient Legend Show Labels](#gradient-legend-show-labels)[](#gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Gradient Legend Show Labels

**Description:** Sets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
seg << Set Gradient Legend Show Labels( 0 );
```

### [Gradient Level Count](#gradient-level-count)[](#gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Gradient Level Count

**Description:** Sets the number of levels in a gradient. This is one less than the number of labels.

**JMP Version Added:** 18

``` jsl
seg << Set Gradient Levels( 7 );
```

### [Gradient Lightness Range](#gradient-lightness-range)[](#gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Gradient Lightness Range

**Description:** Sets the minimum and maximum lightness for level colors in a gradient. The colors will be scaled to cover this range. A missing value is treated as no change.

**JMP Version Added:** 18

**Example 1**

``` jsl
seg << Set Gradient Lightness Range( Min( 0.25 ), Max( 0.75 ) );
```

**Example 2**

``` jsl
seg << Set Gradient Lightness Range( 0.25, 0.75 );
```

**Example 3**

``` jsl
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
seg << Set Gradient Reverse Color Order( 1 );
```

### [Gradient Reverse Label Order](#gradient-reverse-label-order)[](#gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Gradient Reverse Label Order

**Description:** Reverses the order of the labels in a gradient.

**JMP Version Added:** 18

``` jsl
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
seg << Gradient Transparency( "None" );
```

### [Grid Line Order](#grid-line-order)[](#grid-line-order "Click to copy url")

**Syntax:** obj \<\< Grid Line Order( position )

**Description:** Draw the grid lines in front of or behind other objects in the graph

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = Bivariate( Y( :weight ), X( :height ), FitLine );
rbiv = biv << report;
rbiv[axis box( 1 )] << Add Ref Line( 90, "Solid", blue );
rbiv[axis box( 2 )] << Show Major Grid( 1 );
framebox = rbiv[frame box( 1 )];
framebox << Grid Line Order( 1 );
```

### [Horizontal Gap](#horizontal-gap)[](#horizontal-gap "Click to copy url")

**Syntax:** obj \<\< Horizontal Gap( number )

**JMP Version Added:** 15

### [Hover Label Editor](#hover-label-editor)[](#hover-label-editor "Click to copy url")

**Syntax:** obj \<\< Hover Label Editor

**Description:** Displays the Hover Label Editor window.

**JMP Version Added:** 15

### [Last Value](#last-value)[](#last-value "Click to copy url")

**Syntax:** obj \<\< Last Value( state=0\|1 )

**JMP Version Added:** 16

### [Left](#left)[](#left "Click to copy url")

**Syntax:** obj \<\< Left( state=0\|1 )

**Description:** Shows or hides a border on the left of the frame.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Left( 0 );
```

### [Line Color](#line-color)[](#line-color "Click to copy url")

**Syntax:** obj \<\< Line Color( color )

**Description:** Set the color for all lines in the display seg.

``` jsl
seg << Set Line Color( "Green" );
```

### [Line Style](#line-style)[](#line-style "Click to copy url")

**Syntax:** obj \<\< Line Style( pen style )

**Description:** Sets the style of the lines. Options are Solid, Dotted, Dashed, DashDot, and DashDotDot.

**JMP Version Added:** 14

``` jsl
seg << Set Line Style( "Dotted" );
```

### [Line Width](#line-width)[](#line-width "Click to copy url")

**Syntax:** obj \<\< Line Width( "1"\|"2"\|"3"\|"4"\|"5"\|"6"\|"Other..." )

**Description:** Sets the width of the lines.

**JMP Version Added:** 14

``` jsl
seg << Set Line Width( 3 );
```

### [Line Width Scale](#line-width-scale)[](#line-width-scale "Click to copy url")

**Syntax:** obj \<\< Line Width Scale( 0\|scale )

**Description:** Sets the width of the line to the inputted value. A value of 0 means the line width scale is determined by the font size scale.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ), FitLine );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Line Width Scale( 2.0 );
```

### [Make table of graphs like this](#make-table-of-graphs-like-this)[](#make-table-of-graphs-like-this "Click to copy url")

**Syntax:** obj \<\< Make table of graphs like this

**Description:** create a data table of graphs

### [Marker](#marker)[](#marker "Click to copy url")

**Syntax:** obj \<\< Marker( marker )

**Description:** Sets the marker style for all markers.

**JMP Version Added:** 14

``` jsl
seg << Set Marker( "Square" );
```

### [Marker Drawing Mode](#marker-drawing-mode)[](#marker-drawing-mode "Click to copy url")

**Syntax:** obj \<\< Marker Drawing Mode( "Normal"\|"Fast"\|"Outlined" )

**Description:** Sets the style of the marker.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Marker Drawing Mode( "outlined" );
```

### [Marker Label Color Style](#marker-label-color-style)[](#marker-label-color-style "Click to copy url")

**Syntax:** obj \<\< Marker Label Color Style( "Preferred Mode"\|"Marker Color"\|"Marker Color Faded"\|"Fixed Color" )

**Description:** Changes the color of marker labels

### [Marker Selection Mode](#marker-selection-mode)[](#marker-selection-mode "Click to copy url")

**Syntax:** obj \<\< Marker Selection Mode( "Preferred Mode"\|"Unselected Faded"\|"Selected Larger"\|"Selected Haloed"\|"Selected Outlined"\|"Selected Same Color" )

**Description:** Sets the selection style of the marker.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Where( dt:age == 12 );
framebox = rbiv[Frame Box( 1 )];
framebox << Marker Selection Mode( "Selected Haloed" );
```

### [Marker Size](#marker-size)[](#marker-size "Click to copy url")

**Syntax:** obj \<\< Marker Size( size )

**Description:** Sets the size for the markers. Size options are Dot, Small, Medium, Large, XL, XXL, and XXXL.

**JMP Version Added:** 14

``` jsl
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

### [Name Selection in Column](#name-selection-in-column)[](#name-selection-in-column "Click to copy url")

**Syntax:** obj \<\< Name Selection in Column

**Description:** Label the currently selected rows and save the value(label) in a column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Rows( 1 );
dt:(Column( 2 )) << Set Selected( 1 );
framebox = rbiv[Frame Box( 1 )];
framebox << Select Matching Cells;
framebox << Name Selection in Column;
```

### [Paste Background Image](#paste-background-image)[](#paste-background-image "Click to copy url")

**Syntax:** obj \<\< Paste Background Image

**Description:** Paste the background image that is saved in memory on the clipboard.

``` jsl
Open( "$SAMPLE_DATA/Animals.jmp" );
op = Overlay Plot( X( :subject ), Y( :miles ), Separate Axes( 1 ) );
opr1 = op << report;
opr2 = opr1 << Clone Box;
opr1 << append( opr2 );
fb1 = opr1[Frame Box( 1 )];
fb1 << Add Image(
    Open( Convert File Path( "$SAMPLE_IMAGES/black rhino footprint.jpg" ) ),
    Transparency( 0.9 ),
    Rotate( 90 ),
    Bounds(
        Left( 0.135416666666667 ),
        Right( 3.26041666666667 ),
        Top( 11.8333333333333 ),
        Bottom( -1 )
    ),
    SetSize( {300, 210} )
);
fb1 << Copy Picture;
fb2 = opr2[Frame Box( 1 )];
fb2 << Paste Background Image;
```

### [Paste Customizations](#paste-customizations)[](#paste-customizations "Click to copy url")

**Syntax:** obj \<\< Paste Customizations

**Description:** Paste a script that contains graph customizations.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv1 = biv << report;
rbiv2 = rbiv1 << Clone Box;
rbiv1 << append( rbiv2 );
framebox1 = rbiv1[Frame Box( 1 )];
framebox2 = rbiv2[Frame Box( 1 )];
framebox1 << Marker Drawing Mode( outlined );
framebox1 << Copy Customizations;
framebox2 << Paste Customizations;
```

### [Paste Frame Contents](#paste-frame-contents)[](#paste-frame-contents "Click to copy url")

**Syntax:** obj \<\< Paste Frame Contents

**Description:** The clipboard contains journal text for Frame contents. Parse it and install it in this frame.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv1 = biv << report;
rbiv2 = rbiv1 << Clone Box;
rbiv1 << append( rbiv2 );
framebox1 = rbiv1[Frame Box( 1 )];
framebox2 = rbiv2[Frame Box( 1 )];
biv << Fit Line;
framebox1 << Copy Frame Contents;
framebox2 << Paste Frame Contents;
```

### [Paste Frame Settings](#paste-frame-settings)[](#paste-frame-settings "Click to copy url")

**Syntax:** obj \<\< Paste Frame Settings

**Description:** Paste the clipboard's contents into this frame.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv1 = biv << report;
rbiv2 = rbiv1 << Clone Box;
rbiv1 << append( rbiv2 );
framebox1 = rbiv1[Frame Box( 1 )];
framebox2 = rbiv2[Frame Box( 1 )];
framebox1 << Background Color( "Green" );
framebox1 << Copy Frame Settings;
framebox2 << Paste Frame Settings;
```

### [Paste Graphlet](#paste-graphlet)[](#paste-graphlet "Click to copy url")

**Syntax:** obj \<\< Paste Graphlet

**Description:** Adds a Graphlet customization based on the clipboard contents.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
gb = dt << Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ), Y( :weight ) ),
    Elements( Bar( X, Y, Legend( 7 ) ) )
);
Set Clipboard(JSLQuote(Bivariate(
                             Y( :height ),
                             X( :weight ),
                             Histogram Borders( 1 ),
                             Fit Robust( {Line Color( {212, 73, 88} )} ),
                             Fit Cauchy( {Line Color( {61, 174, 70} )} ),
                             SendToReport(
                                 Dispatch(
                                     {},
                                     "Bivar Plot",
                                     FrameBox,
                                     {Grid Line Order( 1 ), Reference Line Order( 2 )}
                                 )
                             )
                         )));
frame = (gb << report)[FrameBox( 1 )];
frame << Paste Graphlet();
gpin = frame << Add Pin Annotation(
    Seg( BarSeg( 1 ) ),
    Index( {0, 0} ),
    Index Row( {0, 0} ),
    UniqueID( 1513503376 ),
    FoundPt( {107, 211} ),
    Origin( {0.00867052023121384, 96.6870397553517} ),
    Tag Line( 1 )
);
gpin << Launch Graphlet;
```

### [Reference Line Order](#reference-line-order)[](#reference-line-order "Click to copy url")

**Syntax:** obj \<\< Reference Line Order( position )

**Description:** Draw the reference lines in front of or behind other objects in the graph

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = Bivariate( Y( :weight ), X( :height ), FitLine );
rbiv = biv << report;
rbiv[axis box( 1 )] << Add Ref Line( 90, "Solid", blue );
rbiv[axis box( 2 )] << Show Major Grid( 1 );
framebox = rbiv[frame box( 1 )];
framebox << Reference Line Order( 1 );
```

### [Remove Graphics Script](#remove-graphics-script)[](#remove-graphics-script "Click to copy url")

**Syntax:** obj \<\< Remove Graphics Script( position )

**Description:** Removes the graphics script attached to the frame at the given position.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = Bivariate( Y( :weight ), X( :height ), FitLine );
rbiv = biv << report;
framebox = rbiv[frame box( 1 )];
framebox << Add Graphics Script(
    Transparency( 0.5 );
    Fill Color( {1.0, 0.5, 0.0} );
    Polygon( [60, 72, 57], [75, 120, 120] );
);
framebox << Add Graphics Script(
    Transparency( 0.5 );
    Fill Color( {0.0, 0.5, 1.0} );
    Polygon( [60, 72, 57], [150, 120, 120] );
);
Wait( 2 );
framebox << Remove Graphics Script( 2 );
```

### [Reorder Segs](#reorder-segs)[](#reorder-segs "Click to copy url")

**Syntax:** obj \<\< Reorder Segs( List of integers representing the current segs in the new order. )

**Description:** Reorders segs that are in a graph.

**JMP Version Added:** 16

``` jsl
Open( "$sample_data\big class.jmp" );
gb = Graph Builder(
    Size( 534, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y, Legend( 6 ) ), Bar( X, Y, Legend( 7 ) ) ),
    SendToReport(
        Dispatch( {}, "weight", ScaleBox,
            {Label Row( {Show Major Grid( 1 ), Show Minor Grid( 1 )} )}
        )
    )
);
For( blink = 1, blink < 4, blink++,
    Wait( .5 );
    (gb << report)[FrameBox( 1 )] << reorder segs( {4, 3, 2, 1} );
);
```

### [Right](#right)[](#right "Click to copy url")

**Syntax:** obj \<\< Right( state=0\|1 )

**Description:** Shows or hides a border on the right of the frame.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Right( 0 );
```

### [Right Y Axis](#right-y-axis)[](#right-y-axis "Click to copy url")

**Syntax:** obj \<\< Right Y Axis( \< Min( min ) \>, \< Max( max ) \>, \< Inc( n ) \>, ... )

**Description:** Applies one or more right Y axis changes in a single message. Opens the right Y Axis Settings window if no arguments are given.

**Example 1**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ), Y( :height ), Y( :weight, Position( 1 ), Side( "Right" ) ) ),
    Elements(
        Points( X, Y( 1 ), Legend( 1 ), Jitter( 1 ) ),
        Points( X, Y( 2 ), Legend( 3 ), Jitter( 1 ) )
    )
);
gbr = gb << report;
fb = gbr[Frame Box( 1 )];
fb << Right Y Axis;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :age, Size( 23 ) ),
        Y( :height, Size( 37 ) ),
        Y( :weight, Position( 1 ), Size( 37 ), Side( "Right" ) )
    ),
    Elements(
        Points( X, Y( 1 ), Legend( 1 ), Jitter( 1 ) ),
        Points( X, Y( 2 ), Legend( 3 ), Jitter( 1 ) )
    )
);
framebox = Report( gb )[framebox( 1 )];
framebox << Right Y Axis(
    Rotated Labels( "Angled" ),
    Scale( "Log" ),
    Add Ref Line( 125, dashed, "red" )
);
```

### [Row Colors](#row-colors)[](#row-colors "Click to copy url")

**Syntax:** obj \<\< Row Colors( color )

**Description:** Sets the color of the selected rows.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Where( dt:age == 12 );
framebox = rbiv[Frame Box( 1 )];
framebox << Row Colors( "Red" );
```

### [Row Editor](#row-editor)[](#row-editor "Click to copy url")

**Syntax:** obj \<\< Row Editor

**Description:** Bring up the Row Editor window, starting on the first selected point.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Row Editor;
```

### [Row Exclude](#row-exclude)[](#row-exclude "Click to copy url")

**Syntax:** obj \<\< Row Exclude

**Description:** Excludes (or unexcludes) the corresponding rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Where( dt:age == 12 );
framebox = rbiv[Frame Box( 1 )];
framebox << Row Exclude( 1 );
```

### [Row Hide](#row-hide)[](#row-hide "Click to copy url")

**Syntax:** obj \<\< Row Hide

**Description:** Hides (or unhides) the corresponding rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Where( dt:age == 12 );
framebox = rbiv[Frame Box( 1 )];
framebox << Row Hide( 1 );
```

### [Row Hide and Exclude](#row-hide-and-exclude)[](#row-hide-and-exclude "Click to copy url")

**Syntax:** obj \<\< Row Hide and Exclude

**Description:** Hides and excludes (or unhide or unexcludes) the corresponding rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Where( dt:age == 12 );
framebox = rbiv[Frame Box( 1 )];
framebox << Row Hide and Exclude( 1 );
```

### [Row Label](#row-label)[](#row-label "Click to copy url")

**Syntax:** obj \<\< Row Label

**Description:** Labels (or unlabels) the corresponding rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Where( dt:age == 12 );
framebox = rbiv[Frame Box( 1 )];
framebox << Row Label( 1 );
```

### [Row Legend](#row-legend)[](#row-legend "Click to copy url")

**Syntax:** obj \<\< Row Legend( Color( 0\|1), Marker( 0\|1 ), \<Color theme( string )\>, \<Marker theme( string )\>, \< Continuous scale(0\|1)\>, \<Reverse scale(0\|1)\>, \<Excluded Row( 0\|1 ), \<Make window with legend\> )

**Description:** Color the rows according to a data column, and insert a legend to the right of this frame.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Row Legend( "age", color( 1 ), Marker( 1 ) );
```

### [Row Markers](#row-markers)[](#row-markers "Click to copy url")

**Syntax:** obj \<\< Row Markers( marker )

**Description:** Sets the marker of the selected rows.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Where( dt:age == 12 );
framebox = rbiv[Frame Box( 1 )];
framebox << Row Markers( 3 );
```

### [Scale with Font](#scale-with-font)[](#scale-with-font "Click to copy url")

**Syntax:** obj \<\< Scale with Font

**Description:** Sets the line width to scale with the font size scale. Equivalent to \<\<Line Width Scale(0).

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( weight ), x( height ), FitLine );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Scale with Font;
```

### [Seg Count](#seg-count)[](#seg-count "Click to copy url")

**Syntax:** obj \<\< Seg Count( \<seg type\> )

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = Bivariate( Y( :weight ), X( :height ), FitLine );
rbiv = biv << report;
rbiv[Frame Box( 1 )] << Seg Count( MarkerSeg );
```

### [Select Matching Cells](#select-matching-cells)[](#select-matching-cells "Click to copy url")

**Syntax:** obj \<\< Select Matching Cells

**Description:** Select points that have similar labels to the selected rows

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Rows( 1 );
dt:(Column( 2 )) << Set Selected( 1 );
framebox = rbiv[Frame Box( 1 )];
framebox << Select Matching Cells;
```

### [Select Similar](#select-similar)[](#select-similar "Click to copy url")

**Syntax:** obj \<\< Select Similar

**Description:** Selects the rows that have similar data values as the selected column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
dt << Select Rows( 1 );
dt:(Column( 3 )) << Set Selected( 1 );
framebox = rbiv[Frame Box( 1 )];
framebox << Select Similar;
```

### [Set Background Fill](#set-background-fill)[](#set-background-fill "Click to copy url")

**Syntax:** obj \<\< Set Background Fill( state=0\|1 )

**Description:** Enables or disables filling the graph background with the background color.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( weight ), x( height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
//Set background color
framebox << Background Color( "red" );
//Wait to see the color change
Wait( 1 );
//Turn off background fill color
framebox << Set Background Fill( 0 );
```

### [Set Colors](#set-colors)[](#set-colors "Click to copy url")

**Syntax:** obj \<\< Set Colors

**JMP Version Added:** 15

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

### [Set Gradient](#set-gradient)[](#set-gradient "Click to copy url")

**Syntax:** obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<Contour Levels(num)\>, \<Reverse Gradient(0\|1)\>, \<Density Gradient("Fade To White"\|"Fade To Gray"\|"Full Color")\>, \<Gradient Transparency("None"\|"Linear")\> } obj \<\< { \<Color Theme(theme)\>, \<Min Lightness(0-1)\>, \<Max Lightness(0-1)\>, \<N Labels(num)\>, \<Show Missing Color("On"\|"Off"\|"Auto")\>, \<Scale Type("Linear"\|"Quantile"\|"Standard Deviation"\|"Log"\|"Log Offset"\|"Custom")\>, \<Scale Values(\[v1, v2, …\])\>, \<Range Type("Default"\|"Exact Data Range"\|"Middle 90%")\>, \<Fill("Between"\|"Above"\|"Below"\|"Above Below")\>, \<Reverse Gradient(0\|1)\>, \<Reverse Labels(0\|1)\>, \<Discrete Color(0\|1)\> }, \<Label Format(labelFormat)\>, \<Width(num)\>, \<Horizontal(0\|1)\>, \<Show Labels(0\|1)\>

**Description:** Sets the coloring gradient.

``` jsl
seg << Set Gradient( {Color Theme( "Viridis" ), N Labels( 7 )} );
```

### [Set Gradient Color Theme](#set-gradient-color-theme)[](#set-gradient-color-theme "Click to copy url")

**Syntax:** obj \<\< Set Gradient Color Theme

**Description:** Sets the gradient's color theme.

**JMP Version Added:** 18

``` jsl
seg << Set Gradient Color Theme( "Viridis" );
```

### [Set Gradient Custom Scale](#set-gradient-custom-scale)[](#set-gradient-custom-scale "Click to copy url")

**Syntax:** obj \<\< Set Gradient Custom Scale

**Description:** Sets the gradient to use a list of values for a custom scale.

**JMP Version Added:** 18

``` jsl
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
seg << Set Gradient Legend Horizontal( 1 );
```

### [Set Gradient Legend Label Format](#set-gradient-legend-label-format)[](#set-gradient-legend-label-format "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Label Format

**Description:** Sets the format for gradient legend labels

**JMP Version Added:** 18

``` jsl
seg << Set Gradient Legend Label Format( "Fixed Dec", 6, 3 );
```

### [Set Gradient Legend Label Width](#set-gradient-legend-label-width)[](#set-gradient-legend-label-width "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Label Width

**Description:** Sets the maximum character length of gradient legend labels.

**JMP Version Added:** 18

``` jsl
seg << Set Gradient Legend Label Width( 4 );
```

### [Set Gradient Legend Show Labels](#set-gradient-legend-show-labels)[](#set-gradient-legend-show-labels "Click to copy url")

**Syntax:** obj \<\< Set Gradient Legend Show Labels

**Description:** Sets if the level labels should be shown in the gradient's legend.

**JMP Version Added:** 18

``` jsl
seg << Set Gradient Legend Show Labels( 0 );
```

### [Set Gradient Level Count](#set-gradient-level-count)[](#set-gradient-level-count "Click to copy url")

**Syntax:** obj \<\< Set Gradient Level Count

**Description:** Sets the number of levels in a gradient. This is one less than the number of labels.

**JMP Version Added:** 18

``` jsl
seg << Set Gradient Levels( 7 );
```

### [Set Gradient Lightness Range](#set-gradient-lightness-range)[](#set-gradient-lightness-range "Click to copy url")

**Syntax:** obj \<\< Set Gradient Lightness Range

**Description:** Sets the minimum and maximum lightness for level colors in a gradient. The colors will be scaled to cover this range. A missing value is treated as no change.

**JMP Version Added:** 18

**Example 1**

``` jsl
seg << Set Gradient Lightness Range( Min( 0.25 ), Max( 0.75 ) );
```

**Example 2**

``` jsl
seg << Set Gradient Lightness Range( 0.25, 0.75 );
```

**Example 3**

``` jsl
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
seg << Set Gradient Reverse Color Order( 1 );
```

### [Set Gradient Reverse Label Order](#set-gradient-reverse-label-order)[](#set-gradient-reverse-label-order "Click to copy url")

**Syntax:** obj \<\< Set Gradient Reverse Label Order

**Description:** Reverses the order of the labels in a gradient.

**JMP Version Added:** 18

``` jsl
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

### [Set Graphlet](#set-graphlet)[](#set-graphlet "Click to copy url")

**Syntax:** obj \<\< Set Graphlet

**Description:** Defines the hover label embedded visualization (graphlet) for this graph.

**JMP Version Added:** 15

#### [External image](#external-image)[](#external-image "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
gb = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :Petal length ), Y( :Sepal length ), Color( :Species ) ),
    Elements( Points( X, Y, Legend( 2 ) ) )
);
frame = (gb << report)[FrameBox( 1 )];
frame << Set Graphlet(
    Picture(
        local:img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/" ||
        Match( local:_Species,
            "versicolor", "2/27/Blue_Flag%2C_Ottawa.jpg/240px-Blue_Flag%2C_Ottawa.jpg",
            "virginica", "f/f8/Iris_virginica_2.jpg/240px-Iris_virginica_2.jpg",
            "setosa",
                "5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/180px-Kosaciec_szczecinkowaty_Iris_setosa.jpg"
        );
        Open( local:img_url );
    ),
    Click( Web( "https://en.wikipedia.org/wiki/Iris_" || local:_Species ) ),
    Title( "External Image" ),
    Reapply( 1 )
);
gpin = frame << Add Pin Annotation(
    Seg( Marker Seg( 1 ) ),
    Index( 18 ),
    Index Row( 18 ),
    UniqueID( 1441114818 ),
    FoundPt( {123, 293} ),
    Origin( {1.70752129817444, 5.66359183673469} ),
    Tag Line( 1 )
);
gpin << Launch Graphlet;
```

#### [Preset](#preset)[](#preset "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
gb = dt << Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ), Y( :weight ) ),
    Elements( Bar( X, Y, Legend( 7 ) ) )
);
frame = (gb << report)[FrameBox( 1 )];
frame << Set Graphlet(
    Picture(
        loader = Include( "$BUILTIN_SCRIPTS/hllib.jsl" );
        hlp = loader:lazyLoad( "hllPresets" );
        hlp:launchPie();
    ),
    Title( "Pie Preset" ),
    Reapply( 1 )
);
gpin = frame << Add Pin Annotation(
    Seg( BarSeg( 1 ) ),
    Index( {0, 0} ),
    Index Row( {0, 0} ),
    UniqueID( 1513503376 ),
    FoundPt( {107, 211} ),
    Origin( {0.00867052023121384, 96.6870397553517} ),
    Tag Line( 1 )
);
gpin << Launch Graphlet;
```

### [Set Gridlet](#set-gridlet)[](#set-gridlet "Click to copy url")

**Syntax:** obj \<\< Set Gridlet

**Description:** Defines the hover label content grid (gridlet) for this graph.

**JMP Version Added:** 15

#### [Append](#append)[](#append "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
gb = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :Petal length ), Y( :Sepal length ), Color( :Species ) ),
    Elements( Points( X, Y, Legend( 2 ) ) )
);
frame = (gb << report)[FrameBox( 1 )];
frame << Set Gridlet(
    Expunge( {{Matcher( "Species" )}} ),
    Annex(
        {{Matcher( "Species@Wikipedia" ), value( local:_Species ),
        click( Web( "https://wikipedia.com/wiki/Iris_" || local:_Species ) )}}
    )
);
frame << Add Pin Annotation(
    Seg( Marker Seg( 1 ) ),
    Index( 133 ),
    Index Row( 133 ),
    UniqueID( 1441114933 ),
    FoundPt( {384, 228} ),
    Origin( {5.08093306288033, 6.30828571428571} ),
    Tag Line( 1 )
);
```

#### [Delete](#delete)[](#delete "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
gb = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :Petal length ), Y( :Sepal length ), Color( :Species ) ),
    Elements( Points( X, Y, Legend( 2 ) ) )
);
frame = (gb << report)[FrameBox( 1 )];
frame << Set Gridlet( Expunge( {{Matcher( "Row" )}} ) );
frame << Add Pin Annotation(
    Seg( Marker Seg( 1 ) ),
    Index( 133 ),
    Index Row( 133 ),
    UniqueID( 1441114933 ),
    FoundPt( {384, 228} ),
    Origin( {5.08093306288033, 6.30828571428571} ),
    Tag Line( 1 )
);
```

#### [Reformat](#reformat)[](#reformat "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
gb = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :Petal length ), Y( :Sepal length ), Color( :Species ) ),
    Elements( Points( X, Y, Legend( 2 ) ) )
);
frame = (gb << report)[FrameBox( 1 )];
frame << Set Gridlet(
    Reformat(
        {{Matcher( "Petal length" ), Format( "Scientific", 80 ), 80},
        {Matcher( "Sepal length" ), Format( "Scientific", 80 ), 80}}
    )
);
frame << Add Pin Annotation(
    Seg( Marker Seg( 1 ) ),
    Index( 133 ),
    Index Row( 133 ),
    UniqueID( 1441114933 ),
    FoundPt( {384, 228} ),
    Origin( {5.08093306288033, 6.30828571428571} ),
    Tag Line( 1 )
);
```

#### [Rename](#rename)[](#rename "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
gb = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :Petal length ), Y( :Sepal length ), Color( :Species ) ),
    Elements( Points( X, Y, Legend( 2 ) ) )
);
frame = (gb << report)[FrameBox( 1 )];
frame << Set Gridlet( Rename( {{Matcher( "Row" ), value( "Observation" )}} ) );
frame << Add Pin Annotation(
    Seg( Marker Seg( 1 ) ),
    Index( 133 ),
    Index Row( 133 ),
    UniqueID( 1441114933 ),
    FoundPt( {384, 228} ),
    Origin( {5.08093306288033, 6.30828571428571} ),
    Tag Line( 1 )
);
```

#### [Style](#style)[](#style "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
gb = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :Petal length ), Y( :Sepal length ), Color( :Species ) ),
    Elements( Points( X, Y, Legend( 2 ) ) )
);
frame = (gb << report)[FrameBox( 1 )];
frame << Set Gridlet(
    Style(
        {{Matcher( "Species" ), Text Color( "Red" ), Background Color( "Light Yellow" ),
        Justification( "Center" ), "Font"("Times New Roman", 14, "Italic")}}
    )
);
frame << Add Pin Annotation(
    Seg( Marker Seg( 1 ) ),
    Index( 133 ),
    Index Row( 133 ),
    UniqueID( 1441114933 ),
    FoundPt( {384, 228} ),
    Origin( {5.08093306288033, 6.30828571428571} ),
    Tag Line( 1 )
);
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
seg << Set Line Color( "Green" );
```

### [Set Line Style](#set-line-style)[](#set-line-style "Click to copy url")

**Syntax:** obj \<\< Set Line Style( pen style )

**Description:** Sets the style of the lines. Options are Solid, Dotted, Dashed, DashDot, and DashDotDot.

**JMP Version Added:** 14

``` jsl
seg << Set Line Style( "Dotted" );
```

### [Set Line Width](#set-line-width)[](#set-line-width "Click to copy url")

**Syntax:** obj \<\< Set Line Width( "1"\|"2"\|"3"\|"4"\|"5"\|"6"\|"Other..." )

**Description:** Sets the width of the lines.

**JMP Version Added:** 14

``` jsl
seg << Set Line Width( 3 );
```

### [Set Marker](#set-marker)[](#set-marker "Click to copy url")

**Syntax:** obj \<\< Set Marker( marker )

**Description:** Sets the marker style for all markers.

**JMP Version Added:** 14

``` jsl
seg << Set Marker( "Square" );
```

### [Set Marker Size](#set-marker-size)[](#set-marker-size "Click to copy url")

**Syntax:** obj \<\< Set Marker Size( size )

**Description:** Sets the size for the markers. Size options are Dot, Small, Medium, Large, XL, XXL, and XXXL.

**JMP Version Added:** 14

``` jsl
seg << Set Marker( "Square" );
seg << Set Marker Size( "XL" );
```

### [Set Textlet](#set-textlet)[](#set-textlet "Click to copy url")

**Syntax:** obj \<\< Set Textlet

**Description:** Defines the hover label rich text content (textlet) for this graph.

**JMP Version Added:** 15

``` jsl
//This example uses hardcoded content from Wikipedia
// For a complete example that uses dynamic, data-driven content, please see
// https://community.jmp.com/t5/JMP-Scripts/WikiReader-Augmenting-Hover-Labels-with-web-data-and-images/ta-p/237488
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
gb = dt << Graph Builder(
    Size( 531, 456 ),
    Show Control Panel( 0 ),
    Variables( X( :Petal length ), Y( :Sepal length ), Color( :Species ) ),
    Elements( Points( X, Y, Legend( 2 ) ) )
);
frame = (gb << report)[FrameBox( 1 )];
frame << Set Textlet(
    Setup(
        local:description =
        "Iris virginica, with the common name Virginia iris, is a perennial species of flowering plant, native to eastern North America.";
        local:text = Substr( local:description, 1, 140 ) || "...";
    ),
    Markup(
        "<background color='white'><i><font family='Arial' size='12'>{local:text}</font></i></background>"
    ),
    Width( 320 )
);
gpin = frame << Add Pin Annotation(
    Seg( Marker Seg( 1 ) ),
    Index( 133 ),
    Index Row( 133 ),
    UniqueID( 1441114933 ),
    FoundPt( {384, 228} ),
    Origin( {5.08093306288033, 6.30828571428571} ),
    Tag Line( 1 )
);
```

### [Set Transparency](#set-transparency)[](#set-transparency "Click to copy url")

**Syntax:** obj \<\< Set Transparency( number )

**Description:** Sets the shape transparency. The argument should be a numeric value between 0 and 1.

**JMP Version Added:** 16

``` jsl
seg << Set Transparency( .3 );
```

### [Size to Isometric](#size-to-isometric)[](#size-to-isometric "Click to copy url")

**Syntax:** obj \<\< Size to Isometric

**Description:** Resize the frame so that the number of real units per pixel is the same in X and Y directions.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Size To Isometric;
```

### [Ternary X Title](#ternary-x-title)[](#ternary-x-title "Click to copy url")

**Syntax:** obj \<\< Ternary X Title( text )

**Description:** Sets the X-axis title for a ternary frame.

**JMP Version Added:** 15

### [Ternary Y Title](#ternary-y-title)[](#ternary-y-title "Click to copy url")

**Syntax:** obj \<\< Ternary Y Title( text )

**Description:** Sets the Y-axis title for a ternary frame.

**JMP Version Added:** 15

### [Ternary Y1 Title](#ternary-y1-title)[](#ternary-y1-title "Click to copy url")

**Syntax:** obj \<\< Ternary Y1 Title( text )

**Description:** Sets the Y1-axis title for a ternary frame.

**JMP Version Added:** 15

### [Top](#top)[](#top "Click to copy url")

**Syntax:** obj \<\< Top( state=0\|1 )

**Description:** Shows or hides a border on the top of the frame.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
framebox = rbiv[Frame Box( 1 )];
framebox << Top( 0 );
```

### [Transparency](#transparency)[](#transparency "Click to copy url")

**Syntax:** obj \<\< Transparency( number )

**Description:** Sets the shape transparency. The argument should be a numeric value between 0 and 1.

**JMP Version Added:** 16

``` jsl
seg << Set Transparency( .3 );
```

### [Vertical Gap](#vertical-gap)[](#vertical-gap "Click to copy url")

**Syntax:** obj \<\< Vertical Gap( number )

**JMP Version Added:** 15

### [X Axis](#x-axis)[](#x-axis "Click to copy url")

**Syntax:** obj \<\< X Axis( \< Min( min ) \>, \< Max( max ) \>, \< Inc( n ) \>, ... )

**Description:** Applies one or more X axis changes in a single message. Opens the X Axis Settings window if no arguments are given.

**Example 1**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ), Y( :height ), Y( :weight, Position( 1 ), Side( "Right" ) ) ),
    Elements(
        Points( X, Y( 1 ), Legend( 1 ), Jitter( 1 ) ),
        Points( X, Y( 2 ), Legend( 3 ), Jitter( 1 ) )
    )
);
gbr = gb << report;
fb = gbr[Frame Box( 1 )];
fb << X Axis;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :age, Size( 23 ) ),
        Y( :height, Size( 37 ) ),
        Y( :weight, Position( 1 ), Size( 37 ), Side( "Right" ) )
    ),
    Elements(
        Points( X, Y( 1 ), Legend( 1 ), Jitter( 1 ) ),
        Points( X, Y( 2 ), Legend( 3 ), Jitter( 1 ) )
    )
);
framebox = Report( gb )[framebox( 1 )];
framebox << X Axis(
    Min( -2 ),
    Max( 7 ),
    Inc( 1 ),
    Add Ref Line( 5, "Solid", "Blue" ),
    Rotated Labels( "Vertical" )
);
```

### [Y Axis](#y-axis)[](#y-axis "Click to copy url")

**Syntax:** obj \<\< Y Axis( \< Min( min ) \>, \< Max( max ) \>, \< Inc( n ) \>, ... )

**Description:** Applies one or more Y axis changes in a single message. Opens the Y Axis Settings window if no arguments are given.

**Example 1**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ), Y( :height ), Y( :weight, Position( 1 ), Side( "Right" ) ) ),
    Elements(
        Points( X, Y( 1 ), Legend( 1 ), Jitter( 1 ) ),
        Points( X, Y( 2 ), Legend( 3 ), Jitter( 1 ) )
    )
);
gbr = gb << report;
fb = gbr[Frame Box( 1 )];
fb << Y Axis;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :age, Size( 23 ) ),
        Y( :height, Size( 37 ) ),
        Y( :weight, Position( 1 ), Size( 37 ), Side( "Right" ) )
    ),
    Elements(
        Points( X, Y( 1 ), Legend( 1 ), Jitter( 1 ) ),
        Points( X, Y( 2 ), Legend( 3 ), Jitter( 1 ) )
    )
);
framebox = Report( gb )[framebox( 1 )];
framebox << Y Axis(
    Add Ref Line( 61.25, "Solid", "Medium Dark Green" ),
    Show Major Grid( 1 ),
    Show Minor Grid( 1 ),
    Format( "Fixed Dec", 5, 2 ),
    Rotated Labels( "Perpendicular" )
);
```

## [Shared Item Messages](#shared-item-messages)[](#shared-item-messages "Click to copy url")

### [Add Line Annotation](#add-line-annotation)[](#add-line-annotation "Click to copy url")

**Syntax:** obj \<\< Add Line Annotation

**Description:** Adds a line on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Line Annotation( Line( 160, 235, 240, 235 ) );
```

### [Add Pin Annotation](#add-pin-annotation)[](#add-pin-annotation "Click to copy url")

**Syntax:** obj \<\< Add Pin Annotation

**Description:** Adds a pinned annotation on top of a display box. Most attributes (such as Index Row, UniqueID and FoundPt) are designed for internal use only.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Bivariate(
    Y( :weight ),
    X( :height ),
    SendToReport(
        Dispatch( {}, "Bivar Plot", FrameBox,
            Add Pin Annotation(
                Seg( Marker Seg( 1 ) ),
                Index( 17 ),
                Index Row( 17 ),
                UniqueID( -960001792 ),
                FoundPt( {238, 219} ),
                Origin( {64.9765625, 142} ),
                Offset( {-174, -40} ),
                Tag Line( 1 ),
                Font( "Helvetica", 11, "Plain" )
            )
        )
    )
);
```

### [Add Polygon Annotation](#add-polygon-annotation)[](#add-polygon-annotation "Click to copy url")

**Syntax:** obj \<\< Add Polygon Annotation

**Description:** Adds a polygon on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Polygon Annotation(
    Points( {210, 80}, {230, 70}, {280, 115}, {240, 120} ),
    Color( "Red" ),
    Closed( 1 )
);
```

### [Add Simple Shape Annotation](#add-simple-shape-annotation)[](#add-simple-shape-annotation "Click to copy url")

**Syntax:** obj \<\< Add Simple Shape Annotation

**Description:** Adds a simple shape on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Simple Shape Annotation( Oval( 210, 100, 250, 75 ) );
rbiv << Add Simple Shape Annotation( Rectangle( 70, 180, 95, 215 ) );
```

### [Add Text Annotation](#add-text-annotation)[](#add-text-annotation "Click to copy url")

**Syntax:** obj \<\< Add Text Annotation

**Description:** Adds text on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Text Annotation(
    Text( "We need to discuss this at the next meeting." ),
    Text Box( {65, 35, 200, 77} )
);
```

### [Append](#append_1)[](#append_1 "Click to copy url")

**Syntax:** obj \<\< Append( db2 )

**Description:** Add db2 to the display tree after db.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << append( Text Box( "=== below ===" ) );
```

### [Background Color](#background-color)[](#background-color "Click to copy url")

**Syntax:** obj \<\< Background Color( color ); color = obj \<\< Get Background Color

**Description:** If the background color is set, the box is filled with the background color prior to drawing its content. If the background color is not set, the background and content of the containing boxes show through.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Background Color );
Wait( 2 );
tb << Background Color( "Yellow" );
```

### [Border](#border)[](#border "Click to copy url")

**Syntax:** obj \<\< Border( sides ); sides = obj \<\< Get Border

**Description:** Borders are solid lines drawn around the outside of a display box. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical borders.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Border );
Wait( 1 );
tb << Border( 1 );
```

### [Border Color](#border-color)[](#border-color "Click to copy url")

**Syntax:** obj \<\< Border Color( color ); color = obj \<\< Get Border Color

**Description:** Optional color to override the default color for box borders.

**JMP Version Added:** 19

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Wait( 2 );
tb << Border( 1 );
tb << Border Color( "Light Red" );
```

### [Bring Window To Front](#bring-window-to-front)[](#bring-window-to-front "Click to copy url")

**Syntax:** obj \<\< Bring Window To Front

**Description:** Brings the window to the front.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Run Script( "Bivariate" );
w << Bring Window To Front;
```

### [Child](#child)[](#child "Click to copy url")

**Syntax:** obj \<\< Child

**Description:** Returns the child of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisParent = axisbox << parent();
axisChild = axisParent << child();
Print( axisChild << Class Name() );
```

### [Class Name](#class-name)[](#class-name "Click to copy url")

**Syntax:** obj \<\< Class Name

**Description:** Returns the name of the display class for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisbox << Class Name();
```

### [Clone Box](#clone-box)[](#clone-box "Click to copy url")

**Syntax:** obj \<\< Clone Box

**Description:** Makes a new copy of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << append( Text Box( "=== below ===" ) );
clonedBox = rbiv << Clone Box();
rbiv << append( clonedBox );
```

### [Close Window](#close-window)[](#close-window "Click to copy url")

**Syntax:** obj \<\< Close Window( \<"NoSave"\> )

**Description:** Closes the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
w << Close Window;
```

### [Copy Data](#copy-data)[](#copy-data "Click to copy url")

**Syntax:** obj \<\< Copy Data

**Description:** copies the tab-delimited data from a matrix or table to the clip board.

``` jsl
New Window( "x", mat = Matrix Box( [1 2 3, 4 5 6, 7 8 9] ) );
mat << CopyData;
```

### [Copy Graph](#copy-graph)[](#copy-graph "Click to copy url")

**Syntax:** obj \<\< Copy Graph

**Description:** Puts a picture of the graph and axes on the clipboard.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
(rbiv[FrameBox( 1 )]) << Copy Graph();
"paste into a paint program";
```

### [Copy Picture](#copy-picture)[](#copy-picture "Click to copy url")

**Syntax:** obj \<\< Copy Picture

**Description:** Puts a picture of the display box on the clipboard.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Copy Picture();
```

### [Delete Box](#delete-box)[](#delete-box "Click to copy url")

**Syntax:** obj \<\< Delete Box

**Description:** Delete the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisbox << Delete Box();
```

### [Deselect](#deselect)[](#deselect "Click to copy url")

**Syntax:** obj \<\< Deselect

**Description:** Deselects this object for use by Edit menu commands.

``` jsl
//This message applies to all display box objects
selected = 0;
New Window( "Example",
    ex = Button Box( "Press Me",
        selected = !selected;
        refresh;
    )
);
refresh = Function( {},
    If( selected,
        ex << Select,
        ex << Deselect
    )
);
```

### [Dispatch](#dispatch)[](#dispatch "Click to copy url")

**Syntax:** obj \<\< Dispatch( {outline node, ...}, display element, display element type, command )

**Description:** Send command to a specific part of a display tree.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Dispatch( {}, "Bivar Plot", FrameBox, {Marker Size( 3 )} );
```

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

### [Find](#find)[](#find "Click to copy url")

**Syntax:** obj \<\< Find

**Description:** Returns a display box with the given argument.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv << Find( axis box( 1 ) );
axisbox << Delete();
```

### [Get Annotation](#get-annotation)[](#get-annotation "Click to copy url")

**Syntax:** obj \<\< Get Annotation

**Description:** Returns the first annotation that is anchored to this display box. Other annotations can be accessed by using Sib() on the result.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Text Annotation(
    Text( "We need to discuss this at the next meeting." ),
    Text Box( {65, 35, 200, 77} )
);
annotation = rbiv << Get Annotation;
annotation << delete;
```

### [Get Background Color](#get-background-color)[](#get-background-color "Click to copy url")

**Syntax:** obj \<\< Background Color( color ); color = obj \<\< Get Background Color

**Description:** If the background color is set, the box is filled with the background color prior to drawing its content. If the background color is not set, the background and content of the containing boxes show through.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Background Color );
Wait( 2 );
tb << Background Color( "Yellow" );
```

### [Get Border](#get-border)[](#get-border "Click to copy url")

**Syntax:** obj \<\< Border( sides ); sides = obj \<\< Get Border

**Description:** Borders are solid lines drawn around the outside of a display box. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical borders.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Border );
Wait( 1 );
tb << Border( 1 );
```

### [Get Border Color](#get-border-color)[](#get-border-color "Click to copy url")

**Syntax:** obj \<\< Border Color( color ); color = obj \<\< Get Border Color

**Description:** Optional color to override the default color for box borders.

**JMP Version Added:** 19

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Wait( 2 );
tb << Border( 1 );
tb << Border Color( "Light Red" );
```

### [Get Content Size](#get-content-size)[](#get-content-size "Click to copy url")

**Syntax:** obj \<\< Get Content Size

**Description:** Returns the content size within the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
c = w << Get Content Size();
Show( c );
```

### [Get Display Path](#get-display-path)[](#get-display-path "Click to copy url")

**Syntax:** obj \<\< Get Display Path( parent box, \<receiver expr\>, \<Mode("XPath"\|"Subscript")\> )

**Description:** Gets a relatively robust expression to navigate between parent box and obj. This path is not guaranteed to be stable across JMP releases. The receiver expr is incorporated into the output expression if provided. If not, the expression provided for parent box is used instead. As shown in the example, this message is mainly useful for increasing the robustness of a path you already have available. The XPath mode is default.

#### [Basic](#basic)[](#basic "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
rpt = Report( biv );
xpath expr = rpt[Number Col Box( 9 )] << Get Display Path( rpt, Expr( Report( biv ) ) ); // Make Number Col Box(9) more robust
Show( xpath expr );
xpath expr << Select;
```

#### [Subscript Mode](#subscript-mode)[](#subscript-mode "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
rpt = Report( biv );
subscript expr = rpt[Number Col Box( 9 )] << Get Display Path( rpt, Mode( "Subscript" ) ); // Make Number Col Box(9) more robust
Show( subscript expr );
subscript expr << Select;
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

### [Get HTML](#get-html)[](#get-html "Click to copy url")

**Syntax:** obj \<\< Get HTML( \<format\> )

**Description:** Returns a string containing HTML source for the display box.

**Example 1**

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << Set Text( win << Get HTML );
```

**Example 2**

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), Means( 1 ), Mean Diamonds( 1 ) );
Save Text File( "$TEMP/Oneway.html", obj << Get HTML( "svg" ) ); // Prefer <<Save HTML
Web( "$TEMP/Oneway.html", JMPWindow );
```

### [Get Height](#get-height)[](#get-height "Click to copy url")

**Syntax:** width = obj \<\< Get Height

**Description:** Returns the height of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Height;
```

### [Get Horizontal Alignment](#get-horizontal-alignment)[](#get-horizontal-alignment "Click to copy url")

**Syntax:** obj \<\< Horizontal Alignment( "Default"\|"Left"\|"Center"\|"Right" ); "Default"\|"Left"\|"Center"\|"Right" = obj \<\< Get Horizontal Alignment

**Description:** Horizontal alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Border( 1 );
Wait( 2 );
lb << Horizontal Alignment( "Right" );
```

### [Get Journal](#get-journal)[](#get-journal "Click to copy url")

**Syntax:** obj \<\< Get Journal

**Description:** Returns a string containing journal source for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
Print( rbiv << Get Journal );
```

### [Get Margin](#get-margin)[](#get-margin "Click to copy url")

**Syntax:** obj \<\< Margin( sides ); sides = obj \<\< Get Margin

**Description:** Margin adds space between the border of the box and adjacent boxes. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical margins.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Margin );
tb << Border( 1 );
Wait( 2 );
tb << Margin( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Get Max Size](#get-max-size)[](#get-max-size "Click to copy url")

**Syntax:** width,height = obj \<\< Get Max Size

**Description:** Returns the maximum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Max Size;
```

### [Get Min Size](#get-min-size)[](#get-min-size "Click to copy url")

**Syntax:** width,height = obj \<\< Get Min Size

**Description:** Returns the minimum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Min Size;
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

### [Get On Close](#get-on-close)[](#get-on-close "Click to copy url")

**Syntax:** obj \<\< Get On Close

**Description:** Returns the script or function that will run when the window closes.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << On Close(
    // Modal dialogs return Button(1) if OK is pressed, Button(-1) if canceled
    New Window( "Are you sure?",
        <<modal,
        V List Box(
            Text Box( "Press OK to allow the window to close" ),
            H List Box( Button Box( "OK" ), Button Box( "Cancel" ) )
        )
    )["button"] == 1
);
Show( w << Get On Close );
```

### [Get Padding](#get-padding)[](#get-padding "Click to copy url")

**Syntax:** obj \<\< Padding( sides ); sides = obj \<\< Get Padding

**Description:** Padding adds space between the content and the border of the box. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical padding.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Padding );
tb << Border( 1 );
Wait( 1 );
tb << Padding( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Get Page Setup](#get-page-setup)[](#get-page-setup "Click to copy url")

**Syntax:** obj \<\< Get Page Setup

**Description:** Get page setup information for PDF

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Page Setup Test" ) );
w << get page setup();
```

### [Get Picture](#get-picture)[](#get-picture "Click to copy url")

**Syntax:** obj \<\< Get Picture( \<Scale(factor)\>, \<Type("Bitmap" \| "Scalable")\>, \<View("Picture" \| "Screen" \| "Print"), \<Appearance("Default" \| "Current")\>, \<SubRect(Left(number), Top(number), Right(number), Bottom(number))\> )

**Description:** Captures db as an Image Object. The optional Scale argument will render the image at a scaled resolution. Scaling requires that the display box be stretchable. The Type argument determines whether the result will be a scalable vector image or a bitmap. By default a scalable image is returned, which is suitable for saving to vector formats like PDF. The View option changes the behavior of some boxes. The default option of "Picture" draws the report as it would when exporting to an image format, with scrolled areas fully shown. View mode of "Screen" draws the report as seen on-screen, and "Print" draws the report as it does when printing, without any of the page setup features. The SubRect option will capture a portion of the resulting image rather than a full image. The Appearance option can change from the "Default" output colors to the "Current" colors as seen on-screen. The View, SubRect, and Appearance options are only supported for Type "Bitmap".

#### [Default](#default)[](#default "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
New Window( "Example", rbiv << Get Picture );
```

#### [Scale](#scale)[](#scale "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv[FrameBox( 1 )] << Set Stretch( "Window", "Window" );
New Window( "Example", rbiv << Get Picture( Scale( 1.5 ) ) );
```

#### [View and Appearance](#view-and-appearance)[](#view-and-appearance "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate(
    Y( :weight ),
    X( :height ),
    Fit Line( {Line Color( {212, 73, 88} )} ),
    Fit Polynomial( 3, {Line Color( {61, 174, 70} )} ),
    Kernel Smoother( 1, 1, 0.5, 0 )
);
rbiv = biv << report;
rbiv[FrameBox( 1 )] << Set Stretch( "Window", "Window" );
New Window( "Example",
    H List Box(
        rbiv << Get Picture( View( "Screen" ), Appearance( "Current" ) ),
        rbiv << Get Picture( View( "Print" ), Appearance( "Default" ) )
    )
);
```

### [Get Project](#get-project)[](#get-project "Click to copy url")

**Syntax:** project = obj \<\< Get Project()

**Description:** Returns the parent project of the window, or Empty() if it is not in a project.

**JMP Version Added:** 14

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
c = w << Get Project();
Show( c );
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

### [Get RTF](#get-rtf)[](#get-rtf "Click to copy url")

**Syntax:** obj \<\< Get RTF( \<format\> )

**Description:** Returns a string containing RTF source for the display box.

**Example 1**

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << Set Text( win << Get RTF );
```

**Example 2**

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), Means( 1 ), Mean Diamonds( 1 ) );
Save Text File( "$TEMP/Oneway.rtf", obj << Get RTF( "png" ) ); // Prefer <<Save RTF
Open( "$TEMP/Oneway.rtf" );
```

### [Get Row States](#get-row-states)[](#get-row-states "Click to copy url")

**Syntax:** rs = obj \<\< Get Row States( \<dt\> )

**Description:** Returns a vector containing the row state for every row in the given data table or the current data table. The row states can come from the table, or from the filter context of the box.

#### [Single table](#single-table)[](#single-table "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    Data Filter Context Box(
        H List Box(
            dt << Data Filter(
                Local,
                Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
                Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
            ),
            V List Box(
                t = Text Box( "0 Rows Excluded" ),
                Distribution(
                    Continuous Distribution( Column( :weight ) ),
                    Nominal Distribution( Column( :age ) )
                )
            )
        )
    )
);
updatetext = Function( {},
    rs = t << Get Row States( dt );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = t << Make Row State Handler( dt, rsupdate );
updatetext();
```

#### [Where subset](#where-subset)[](#where-subset "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    t = Text Box( "0 Rows Excluded" ),
    dist = Distribution(
        Continuous Distribution( Column( :weight ) ),
        Nominal Distribution( Column( :age ) ),
        Local Data Filter(
            Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
            Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
        ),
        Where( :sex == "F" )
    )
);
subset = dist << Get Data Table();
updatetext = Function( {},
    rs = Report( dist ) << Get Row States( subset );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = Report( dist ) << Make Row State Handler( subset, rsupdate );
updatetext();
```

### [Get Show Window](#get-show-window)[](#get-show-window "Click to copy url")

**Syntax:** obj \<\< Get Show Window

**Description:** Returns the visibility of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Show Window( 0 );
Wait( 2 );
Print( w << Get Show Window() );
```

### [Get Size](#get-size)[](#get-size "Click to copy url")

**Syntax:** width,height = obj \<\< Get Size

**Description:** Returns the size of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
Print( fb << Get Size );
```

### [Get Stretch](#get-stretch)[](#get-stretch "Click to copy url")

**Syntax:** x,y = obj \<\< Get Stretch

**Description:** Returns the stretching flags for this display box in the horizontal and vertical directions.

**JMP Version Added:** 16

``` jsl
//This message applies to all display box objects
New Window( "Stretch",
    V List Box(
        H List Box( Text Edit Box( "String1" ), Text Edit Box( "String2" ) ),
        spacer = Spacer Box(
            Size( 20, 20 ),
            Color( "Light Red" ),
            <<Set Stretch( "Fill", "Off" )
        )
    )
);
spacer << Get Stretch();
```

### [Get Text](#get-text)[](#get-text "Click to copy url")

**Syntax:** obj \<\< Get Text

**Description:** Returns a string containing the text of the display box.

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << Set Text( win << Get Text );
```

### [Get Text Color](#get-text-color)[](#get-text-color "Click to copy url")

**Syntax:** obj \<\< Text Color( color ); color = obj \<\< Get Text Color

**Description:** Text will be drawn using the text color if it has been set. If the property has not been set, the box will inherit the text color of the containing box.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Text Color );
Wait( 2 );
tb << Text Color( "Red" );
```

### [Get UI Only](#get-ui-only)[](#get-ui-only "Click to copy url")

**Syntax:** obj \<\< UI Only( state=0\|1 ); state = obj \<\< Get UI Only

### [Get User Resizable](#get-user-resizable)[](#get-user-resizable "Click to copy url")

**Syntax:** obj \<\< User Resizable; obj \<\< Get User Resizable

**Description:** If the box is user resizable, the cursor will change near the bottom and right edges to allow drag-and-drop resizing.

``` jsl
root1 = Tree Node( "Parent 1" );
root2 = Tree Node( "Parent 2" );
c1 = Tree Node( "Child 1" );
c2 = Tree Node( "Child 2" );
c3 = Tree Node( "Child 3" );
c4 = Tree Node( "Child 4" );
root1 << Append( c1 );
root1 << Append( c2 );
root2 << Append( c3 );
root2 << Append( c4 );
New Window( "resize",
    H Splitter Box(
        Size( 600, 200 ),
        tree = Tree Box( {root1, root2} ),
        scroll = Scroll Box(
            Size( 300, 200 ),
            Picture Box( Open( "$SAMPLE_IMAGES/tile.jpg", jpg ) )
        )
    )
);
tree << Set Stretch( "Window", "Window" ) << Set Max Size( 10000, 10000 );
scroll << Set Stretch( "Window", "Window" ) << Set Max Size( 10000, 10000 );
Wait( 2 );
tree << User Resizable( {0, 0} );
scroll << User Resizable( {0, 0} );
```

### [Get Vertical Alignment](#get-vertical-alignment)[](#get-vertical-alignment "Click to copy url")

**Syntax:** obj \<\< Vertical Alignment( "Default"\|"Top"\|"Center"\|"Bottom" ); "Default"\|"Top"\|"Center"\|"Bottom" = obj \<\< Get Vertical Alignment

**Description:** Vertical alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Set Horizontal( 1 );
lb = r[List Box( 7 )];
lb << Border( 1 );
Wait( 2 );
lb << Vertical Alignment( "Bottom" );
```

### [Get Visibility](#get-visibility)[](#get-visibility "Click to copy url")

**Syntax:** obj \<\< Visibility( "Visible"\|"Hidden"\|"Collapse" ); "Visible"\|"Hidden"\|"Collapse" = obj \<\< Get Visibility

**Description:** Visibility determines whether a box is shown and whether it takes up space. The default value of "Visible" means that the object will be shown. A "Hidden" box is not shown but still takes up space, while a "Collapsed" box takes up no space in the layout.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Visibility );
Wait( 1 );
tb << Visibility( "Collapse" );
Show( tb << Get Visibility );
```

### [Get Web Support](#get-web-support)[](#get-web-support "Click to copy url")

**Syntax:** obj \<\< Get Web Support

**Description:** Return a number indicating the level of Interactive HTML support for the display object. 1 means some or all elements are supported. 0 means no support.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Bivariate( Y( :Weight ), X( :Height ) );
s = obj << Get Web Support();
Show( s );
```

### [Get Width](#get-width)[](#get-width "Click to copy url")

**Syntax:** width = obj \<\< Get Width

**Description:** Returns the width of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Width;
```

### [Get Window Icon](#get-window-icon)[](#get-window-icon "Click to copy url")

**Syntax:** obj \<\< Get Window Icon

**Description:** Returns the window icon.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
t = w << Get Window Icon;
Show( t );
```

### [Get Window Position](#get-window-position)[](#get-window-position "Click to copy url")

**Syntax:** obj \<\< Get Window Position

**Description:** Returns the position of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
p = w << Get Window Position();
Show( p );
```

### [Get Window Size](#get-window-size)[](#get-window-size "Click to copy url")

**Syntax:** obj \<\< Get Window Size

**Description:** Returns the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = w << Get Window Size();
Show( s );
```

### [Get Window Title](#get-window-title)[](#get-window-title "Click to copy url")

**Syntax:** obj \<\< Get Window Title

**Description:** Returns the window title.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
t = w << Get Window Title;
Show( t );
```

### [Get Window View](#get-window-view)[](#get-window-view "Click to copy url")

**Syntax:** obj \<\< Get Window View

**Description:** Returns the current window view. Windows can be "Visible", "Invisible", or "Private".

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Print( w << Get Window View() );
```

### [Get XML](#get-xml)[](#get-xml "Click to copy url")

**Syntax:** obj \<\< Get XML( \<English(0\|1)\>, \<NoData(0\|1)\> )

**Description:** Retrieves the display tree formatted as XML. By default, strings are returned in the local language, and the XML includes data values within some boxes. Use the English option to return English strings where available. Use the NoData option to omit the data values within boxes, which can be very large for some display trees.

``` jsl
//This message applies to all display box objects
win = New Window( "test", a = Text Box( "my test" ) );
a << set text( win << get xml );
```

### [GetOffset](#getoffset)[](#getoffset "Click to copy url")

**Syntax:** x,y = obj \<\< GetOffset

**Description:** Returns the offset of this display box relative to the parent box. You might need to use the \<\<parent message in a loop to accumulate several offsets.

``` jsl
New Window( "example",
    MouseBox(
        Graph Box(
            title( "title" ),
            Pen Size( 3 );
            Y Function( -3 + 100 / 2 * (1 + Sin( (2 * Pi() * (x + .3)) / 100 )), x );
        ),
        <<settrackenable( 1 ) // put the mouse box to work, watching "tracking"
    ,
        <<settrack( // events from the mouse (movement, with button up or down)
            Function( {this, pt}, // parameters: this is the mousebox, pt is mouse x,y
                {fb, offset, t, off, size}, // local variables
                // recalulate offset and size each time, the values can change
                fb = this[framebox( 1 )]; // the framebox in the graph 
                offset = [0, 0]; // accumulator to sum up the offset between framebox and mousebox
                t = fb; // a temporary box that starts at the frame 
                While( t != this, // and walks up to the mousebox
                    off = t << getOffset; // ask each box for its offset to the immediate parent
                    offset += Matrix( off ); // convert list answer to matrix so + will work
                    t = t << parent; // crawl up to the mousebox, one box at a time
                );
                size = Matrix( fb << getSize ); // the frame knows its size
                If( // over the frame box
                    offset[1] < pt[1] < offset[1] + size[1] & offset[2] < pt[2] < offset[2]
                     + size[2]
                ,
                    fb << setbackgroundcolor( "red" ),
                    fb << setbackgroundcolor( "blue" )
                );
            )
        )
    )
);
```

### [Horizontal Alignment](#horizontal-alignment)[](#horizontal-alignment "Click to copy url")

**Syntax:** obj \<\< Horizontal Alignment( "Default"\|"Left"\|"Center"\|"Right" ); "Default"\|"Left"\|"Center"\|"Right" = obj \<\< Get Horizontal Alignment

**Description:** Horizontal alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Border( 1 );
Wait( 2 );
lb << Horizontal Alignment( "Right" );
```

### [Inval](#inval)[](#inval "Click to copy url")

**Syntax:** obj \<\< Inval

**Description:** Invalidate the displaybox. The window will update when either the \<\<UpdateWindow message is sent or the operating system has time for the update.

``` jsl
//This message applies to all display box objects
color = "green"; /* initial color in a variable */
New Window( "Inval example",
    Button Box( "red",
        color = "red";
        g1 << inval; /* tell the oval to redraw */
        g2 << inval; /* tell the rectangle to redraw */
        g1 << updateWindow; /* tell the window to update immediately */
        // this is a busy-wait to help demonstrate the various behaviors...
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 /* delay without wait(.5) */ );
    ),
    Button Box( "blue",
        color = "blue";
        g1 << inval; /* same comments */
        g2 << inval;
        g1 << updateWindow;
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 );
    ),
    g1 = Graph Box(/* the graph does NOT watch for the color variable to change 
                      but will use the current value of color when it reshows */
        Fill Color( color );
        Oval( 10, 80, 70, 50, 1 );
    ),
    g2 = Graph Box(
        Fill Color( color );
        Rect( 10, 80, 70, 50, 1 );
    )
);
```

### [Is Dirty](#is-dirty)[](#is-dirty "Click to copy url")

**Syntax:** obj \<\< Is Dirty

**Description:** Gets the document's modified status. 1 means the document has been modified and will prompt for saving; 0 means the document is not modified.

**JMP Version Added:** 14

``` jsl

ww = New Window( "Test", <<Script, "Open(\!"$SAMPLE_DATA\Big Class.jmp\!");" );
Show( ww << Is Dirty );
ww << Set Dirty( 0 );
Show( ww << Is Dirty );
```

### [Is Modal Dialog](#is-modal-dialog)[](#is-modal-dialog "Click to copy url")

**Syntax:** obj \<\< Is Modal Dialog

**Description:** Returns true if the window is a modal dialog. Only useful when called from a window handler callback.

``` jsl
With Window Handler(
    New Window( "Modal Window", <<Modal ),
    Function( {win},
        Print( win << Is Modal Dialog() );
        win << close window();
    )
);
```

### [Journal](#journal)[](#journal "Click to copy url")

**Syntax:** obj \<\< Journal

**Description:** Makes a journal from the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << journal;
```

### [Journal Window](#journal-window)[](#journal-window "Click to copy url")

**Syntax:** obj \<\< Journal Window

**Description:** Opens a journal window of the window.

``` jsl
//This message applies to all display box objects
w = New Window( "Main Window", Text Box( "Main JMP Window" ) );
w << Journal Window;
```

### [Launch](#launch)[](#launch "Click to copy url")

**Syntax:** obj \<\< Launch

**Description:** Evaluates the given argument in the context of the display box.

``` jsl
//This message applies to all display box objects
Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "example",
    ob1 = Outline Box( "treemap launcher" ),
    ob2 = Outline Box( "bivariate partial" ),
    ob3 = Outline Box( "bivariate launched" )
);
ob1 << launch( Treemap() );
ob2 << launch( Bivariate( Y( :height ) ) );
ob3 << launch( Bivariate( Y( :height ), X( :weight ) ) );
```

### [Make RowState Handler](#make-rowstate-handler)[](#make-rowstate-handler "Click to copy url")

**Syntax:** rs = obj \<\< Make RowState Handler( \<dt\>, function(a) )

**Description:** Creates a row state handler for the given data table or the current data table. The function is called when the row states change in the filter context of the box. The argument of the function holds the rows numbers that have changed, or -1 if the row state filter has changed.

#### [Single table](#single-table_1)[](#single-table_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    Data Filter Context Box(
        H List Box(
            dt << Data Filter(
                Local,
                Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
                Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
            ),
            V List Box(
                t = Text Box( "0 Rows Excluded" ),
                Distribution(
                    Continuous Distribution( Column( :weight ) ),
                    Nominal Distribution( Column( :age ) )
                )
            )
        )
    )
);
updatetext = Function( {},
    rs = t << Get Row States( dt );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = t << Make Row State Handler( dt, rsupdate );
updatetext();
```

#### [Where subset](#where-subset_1)[](#where-subset_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    t = Text Box( "0 Rows Excluded" ),
    dist = Distribution(
        Continuous Distribution( Column( :weight ) ),
        Nominal Distribution( Column( :age ) ),
        Local Data Filter(
            Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
            Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
        ),
        Where( :sex == "F" )
    )
);
subset = dist << Get Data Table();
updatetext = Function( {},
    rs = Report( dist ) << Get Row States( subset );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = Report( dist ) << Make Row State Handler( subset, rsupdate );
updatetext();
```

### [Margin](#margin)[](#margin "Click to copy url")

**Syntax:** obj \<\< Margin( sides ); sides = obj \<\< Get Margin

**Description:** Margin adds space between the border of the box and adjacent boxes. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical margins.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Margin );
tb << Border( 1 );
Wait( 2 );
tb << Margin( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Maximize Window](#maximize-window)[](#maximize-window "Click to copy url")

**Syntax:** obj \<\< Maximize Window( \<state=0\|1\> )

**Description:** Maximizes the window. Default argument is 1.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Maximize Window( 1 );
Wait( 1 );
w << Maximize Window( 0 );
```

### [Minimize Window](#minimize-window)[](#minimize-window "Click to copy url")

**Syntax:** obj \<\< Minimize Window( \<state=0\|1\> )

**Description:** Minimizes the window. Default argument is 1.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Minimize Window( 1 );
Wait( 1 );
w << Minimize Window( 0 );
```

### [Move Window](#move-window)[](#move-window "Click to copy url")

**Syntax:** obj \<\< Move Window( x,y )

**Description:** Moves the window to the specified position.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
w << Move Window( 500, 500 );
```

### [Next](#next)[](#next "Click to copy url")

**Syntax:** obj \<\< Next

**Description:** Returns the display box after this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
next = rbiv << Next();
Print( next << Class Name() );
```

### [On Close](#on-close)[](#on-close "Click to copy url")

**Syntax:** obj \<\< On Close( script )

**Description:** Sets a script or function to run upon closing the window. This script should return 1 to allow the close, or 0 to prevent the window from closing.

#### [Close Function](#close-function)[](#close-function "Click to copy url")

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << On Close(
    Function( {this}, 
        // Modal dialogs return Button(1) if OK is pressed, Button(-1) if cancelled
        New Window( "Are you sure?",
            <<modal,
            V List Box(
                Text Box( "Press OK to allow " || (this << Get Window Title) || " to close" ),
                H List Box( Button Box( "OK" ), Button Box( "Cancel" ) )
            )
        )["button"] == 1
    )
);
```

#### [Close Script](#close-script)[](#close-script "Click to copy url")

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << On Close(
    // Modal dialogs return Button(1) if OK is pressed, Button(-1) if canceled
    New Window( "Are you sure?",
        <<modal,
        V List Box(
            Text Box( "Press OK to allow the window to close" ),
            H List Box( Button Box( "OK" ), Button Box( "Cancel" ) )
        )
    )["button"] == 1
);
```

### [Optimize Display](#optimize-display)[](#optimize-display "Click to copy url")

**Syntax:** obj \<\< Optimize Display

**Description:** Sets a data table's column widths and window to an optimum size.

**JMP Version Added:** 14

``` jsl
//This message applies to Data Table objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Optimize Display;
```

### [Pad Window](#pad-window)[](#pad-window "Click to copy url")

**Syntax:** obj \<\< Pad Window( bool )

**Description:** Turns window padding on or off.

``` jsl
//This message applies to all display box objects
Open( "$SAMPLE_DATA/Big Class.jmp" );
d = distribution( Column( :height ) );
r = d << report;
r << Pad Window( 0 );
```

### [Padding](#padding)[](#padding "Click to copy url")

**Syntax:** obj \<\< Padding( sides ); sides = obj \<\< Get Padding

**Description:** Padding adds space between the content and the border of the box. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical padding.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Padding );
tb << Border( 1 );
Wait( 1 );
tb << Padding( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Page Break](#page-break)[](#page-break "Click to copy url")

**Syntax:** obj \<\< Page Break

**Description:** Inserts a page break before the display box.

``` jsl
//This message applies to all display box objects
New Window( "Example",
    ob = Outline Box( "Outline Box",
        V List Box(
            ob2 = Outline Box( "Outline Box 2",
                H List Box( Text Edit Box( "Top Left" ), Text Edit Box( "Top Right" ) )
            ),
            ob3 = Outline Box( "Outline Box",
                H List Box( Text Edit Box( "Bottom Left" ), Text Edit Box( "Bottom Right" ) )
            )
        )
    )
);
ob3 << Page Break;
```

### [Parent](#parent)[](#parent "Click to copy url")

**Syntax:** obj \<\< Parent

**Description:** Returns the parent of this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisParent = axisbox << parent();
Print( axisParent << Class Name() );
```

### [Prepend](#prepend)[](#prepend "Click to copy url")

**Syntax:** obj \<\< Prepend( db2 )

**Description:** Add db2 to the display tree before db.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << prepend( Text Box( "=== above ===" ) );
```

### [Prev Sib](#prev-sib)[](#prev-sib "Click to copy url")

**Syntax:** obj \<\< Prev Sib

**Description:** Returns the previous sibling of the display box.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 2 )];
axisSibling = axisbox << Prev Sib();
Print( axisSibling << Class Name() );
```

### [Print Window](#print-window)[](#print-window "Click to copy url")

**Syntax:** obj \<\< Print Window

**Description:** Prints the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Print Window;
```

### [Reshow](#reshow)[](#reshow "Click to copy url")

**Syntax:** obj \<\< Reshow

**Description:** Invalidate the displaybox and update the window with the new content. See \<\<Inval and \<\<UpdateWindow messages if more control over timing of the update is required.

``` jsl
//This message applies to all display box objects
color = "green"; /* initial color in a variable */
New Window( "Reshow example",
    Button Box( "red",
        color = "red";
        g << reshow/* tell the graph that something changed */;
    ),
    Button Box( "blue",
        color = "blue";
        g << reshow/* tell the graph that something changed */;
    ),
    g = Graph Box(/* the graph does NOT watch for the color variable to change
                     but will use the current value of color when it reshows */
        Fill Color( color );
        Oval( 10, 80, 70, 50, 1 );
    )
);
```

### [Save Capture](#save-capture)[](#save-capture "Click to copy url")

**Syntax:** obj \<\< Save Capture( \<"path"\>, \<format\>, \<Add Sibling(n)\> )

**Description:** Saves a screen capture of the display box at the specified path. If a path is not given, the Save As window appears.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Capture( "$TEMP/jmp_example.png", "png" );
```

### [Save HTML](#save-html)[](#save-html "Click to copy url")

**Syntax:** obj \<\< Save HTML( \<pathname\>, \<format\> )

**Description:** Saves HTML source and folder of graphics in format specified.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save HTML( "$TEMP/jmp_example.html" );
```

### [Save Interactive HTML](#save-interactive-html)[](#save-interactive-html "Click to copy url")

**Syntax:** obj \<\< Save Interactive HTML( \<pathname\>, \<Boolean\> )

**Description:** Saves Interactive HTML with Data to a file. The Boolean argument represents the report being static.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Interactive HTML( "$TEMP/jmp_example.html" );
```

### [Save Journal](#save-journal)[](#save-journal "Click to copy url")

**Syntax:** obj \<\< Save Journal( \<pathname\> )

**Description:** Saves journal source for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Journal( "$TEMP/jmp_example.jrn" );
```

### [Save MSWord](#save-msword)[](#save-msword "Click to copy url")

**Syntax:** obj \<\< Save MSWord( \<pathname\>, \<format\> )

**Description:** Saves the display box as a Microsoft Word document. (Windows Only)

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save MSWord( "$TEMP/jmp_example.doc" );
```

### [Save PDF](#save-pdf)[](#save-pdf "Click to copy url")

**Syntax:** obj \<\< Save PDF( \<pathname\>, \<Show Page Setup(0\|1)\>, \<Portrait(0\|1)\> )

**Description:** Saves a PDF of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save PDF( "$TEMP/jmp_example.pdf" );
```

### [Save Picture](#save-picture)[](#save-picture "Click to copy url")

**Syntax:** obj \<\< Save Picture( \<pathname\>, \<format\>, \<Scale(factor)\>, \<Type("Bitmap" \| "Scalable")\>, \<View("Picture" \| "Screen" \| "Print"), \<Appearance("Default" \| "Current")\>, \<SubRect(Left(number), Top(number), Right(number), Bottom(number))\> )

**Description:** Saves a picture of the display box. Supported formats are EMF(Windows), PICT(Macintosh), JPEG or JPG, GIF, or PNG. The optional Scale argument will render the image at a scaled resolution. Scaling requires that the display box be stretchable. The Type argument determines whether the result will be a scalable vector image or a bitmap. By default a scalable image is returned, which is suitable for saving to vector formats like PDF. The View option changes the behavior of some boxes. The default option of "Picture" draws the report as it would when exporting to an image format, with scrolled areas fully shown. View mode of "Screen" draws the report as seen on-screen, and "Print" draws the report as it does when printing, without any of the page setup features. The SubRect option will capture a portion of the resulting image rather than a full image. The Appearance option can change from the "Default" output colors to the "Current" colors as seen on-screen. The View, SubRect, and Appearance options are only supported for Type "Bitmap".

#### [Default](#default_1)[](#default_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Picture( "$TEMP/jmp_example.png", "png" );
```

#### [Scale](#scale_1)[](#scale_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv[FrameBox( 1 )] << Set Stretch( "Window", "Window" );
rbiv << Save Picture( "$TEMP/jmp_example_scale.png", "png", Scale( 1.5 ) );
New Window( "scaled image", New Image( "$TEMP/jmp_example_scale.png" ) );
```

#### [View and Appearance](#view-and-appearance_1)[](#view-and-appearance_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate(
    Y( :weight ),
    X( :height ),
    Fit Line( {Line Color( {212, 73, 88} )} ),
    Fit Polynomial( 3, {Line Color( {61, 174, 70} )} ),
    Kernel Smoother( 1, 1, 0.5, 0 )
);
rbiv = biv << report;
rbiv << Save Picture(
    "$TEMP/jmp_example_screen.png",
    "png",
    View( "Screen" ),
    Appearance( "Current" )
);
rbiv << Save Picture(
    "$TEMP/jmp_example_print.png",
    "png",
    View( "Print" ),
    Appearance( "Default" )
);
New Window( "Example",
    H List Box(
        New Image( "$TEMP/jmp_example_screen.png" ),
        New Image( "$TEMP/jmp_example_print.png" )
    )
);
```

### [Save Presentation](#save-presentation)[](#save-presentation "Click to copy url")

**Syntax:** obj \<\< Save Presentation( "filename.pptx", \<Template("path\to\my_template.pptx")\>, \<Insert(Begin\|End\|#) \| Replace(Begin\|End\|#) \| Append\>, \<Outline Titles(None\|Hide\|TopLeft\|TopRight\|BottomLeft\|BottomRight)\>, \<"EMF"\|"PNG"\|"JPG"\|"Native"\> )

**Description:** Saves the display box tables and graphs slides in a presentation. The presentation can be opened with Microsoft PowerPoint or other presentation software.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Presentation( "$TEMP/jmp_example.pptx" );
Open( "$TEMP/jmp_example.pptx" );
```

### [Save RTF](#save-rtf)[](#save-rtf "Click to copy url")

**Syntax:** obj \<\< Save RTF( \<pathname\>, \<format\> )

**Description:** Saves RTF source with graphics in format specified.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save RTF( "$TEMP/jmp_example.rtf", "png" );
```

### [Save Text](#save-text)[](#save-text "Click to copy url")

**Syntax:** obj \<\< Save Text( \<pathname\>, \<format\> )

**Description:** Saves a file containing the text of the display box.

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << save text( "$TEMP/jmp_example.txt" );
```

### [Save Window Report](#save-window-report)[](#save-window-report "Click to copy url")

**Syntax:** obj \<\< Save Window Report( pathname, \<embed data(0\|1)\> )

**Description:** Saves the current report window to a JMP report file (.jrp).

**JMP Version Added:** 16

``` jsl
//This message can be sent to any display box object but will be applied to the report window
Open( "$SAMPLE_DATA/Big Class.jmp" );
d = distribution( Column( :height ) );
d << Save Window Report( "$DOCUMENTS/test.jrp", embed data( 1 ) );
```

### [Scroll Window](#scroll-window)[](#scroll-window "Click to copy url")

**Syntax:** obj \<\< Scroll Window( DisplayBox \| \<Relative(\<v\> \| \<h\>,\<v\>)\> \| \<Absolute(\<v\> \| \<h\>,\<v\>) )

**Description:** Adjust the window scrollbar to bring the given DisplayBox into view, or scroll a relative number of pixels, or scroll to an absolute pixel location. In place of a number of pixels the keywords "Start" or "End" can be used.

#### [Absolute](#absolute)[](#absolute "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
fm = Fit Model(
    Y( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    Effects( :Subject, :Dose ),
    Personality( "Manova" ),
    Run
);
fm << setwindowsize( 600, 600 ); // shrink the window
fm << scroll window( Absolute( "End", "End" ) );
Wait( 1 );
fm << scroll window( Absolute( 0, 300 ) );
Wait( 1 );
```

#### [Box](#box)[](#box "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
fm = Fit Model(
    Y( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    Effects( :Subject, :Dose ),
    Personality( "Manova" ),
    Run
);
fm << setwindowsize( 600, 600 ); // shrink the window
For( i = 1, i <= 5, i++, // repeatedly, bring each frame box into view for 1/2 second
    fm << scroll window( Report( fm )[framebox( 2 )] );
    Wait( .5 );
    fm << scroll window( Report( fm )[framebox( 3 )] );
    Wait( .5 );
    fm << scroll window( Report( fm )[framebox( 1 )] );
    Wait( .5 );
);
```

#### [Relative](#relative)[](#relative "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
fm = Fit Model(
    Y( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    Effects( :Subject, :Dose ),
    Personality( "Manova" ),
    Run
);
fm << setwindowsize( 600, 600 ); // shrink the window
fm << scroll window( Relative( 300 ) );
Wait( 1 );
fm << scroll window( Relative( -50 ) );
Wait( 1 );
fm << scroll window( Relative( "Start" ) );
Wait( 1 );
```

### [Select](#select)[](#select "Click to copy url")

**Syntax:** obj \<\< Select

**Description:** Selects this object for use by Edit menu commands.

``` jsl
//This message applies to all display box objects
New Window( "Example", ex = Button Box( "Press Me" ) );
ex << Select;
```

### [Set Content Size](#set-content-size)[](#set-content-size "Click to copy url")

**Syntax:** obj \<\< Set Content Size( x,y )

**Description:** Sets the content size within the window.

``` jsl
//This message applies to all display box objects
w = New Window( "Test",
    lb = List Box( {"a", "b", "c", "d"} ),
    Button Box( "Enable 2nd item",
        lb << enable item( 2, 1 );
        Show( lb << item enabled( 2 ) );
    ),
    Button Box( "Disable 2nd item",
        lb << enable item( 2, 0 );
        Show( lb << item enabled( 2 ) );
    )
);
Wait( 2 );
w << Set Content Size( 400, 300 );
```

### [Set Dirty](#set-dirty)[](#set-dirty "Click to copy url")

**Syntax:** obj \<\< Set Dirty

**Description:** Sets the document's modified status. 0 will not prompt for saving; 1 will prompt.

**JMP Version Added:** 14

``` jsl

ww = New Window( "Test", <<Script, "Open(\!"$SAMPLE_DATA\Big Class.jmp\!");" );
Show( ww << Is Dirty );
ww << Set Dirty( 0 );
Show( ww << Is Dirty );
```

### [Set Height](#set-height)[](#set-height "Click to copy url")

**Syntax:** obj \<\< Set Height( width )

**Description:** Sets the height of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Height( 150 );
```

### [Set Main Window](#set-main-window)[](#set-main-window "Click to copy url")

**Syntax:** obj \<\< Set Main Window

**Description:** Set the window to be the main window in JMP and sets the prior main window to be a normal window

``` jsl
//This message applies to all display box objects
w = New Window( "Main Window", Text Box( "Main JMP Window" ) );
w << Set Main Window;
```

### [Set Max Size](#set-max-size)[](#set-max-size "Click to copy url")

**Syntax:** obj \<\< Set Max Size( width,height )

**Description:** Sets the maximum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Max Size( 500, 500 );
fb << Get Max Size;
```

### [Set Min Size](#set-min-size)[](#set-min-size "Click to copy url")

**Syntax:** obj \<\< Set Min Size( width,height )

**Description:** Sets the minimum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Min Size( 30, 30 );
fb << Get Min Size;
```

### [Set Page Setup](#set-page-setup)[](#set-page-setup "Click to copy url")

**Syntax:** obj \<\< Set Page Setup( \<margins(left, top, right, bottom)\>, \<scale(s)\>, \<portrait(0\|1)\>, \<paper size(p)\>, \<Table of Contents(always, never, default)\> )

**Description:** Sets the page setup information that is used during printing or saving as pdf. A Table of Contents can optionally be generated from Outline Boxes.

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Outline Box( "TOC", Text Box( "Page Setup Test" ) ) );
w << Set page setup(
    margins( 1, 1, 1, 1 ),
    scale( 1 ),
    portrait( 1 ),
    paper size( "Letter" ),
    Table of Contents( "always" )
);
w << Save pdf( "$DOCUMENTS\test.pdf" );
```

### [Set Print Footers](#set-print-footers)[](#set-print-footers "Click to copy url")

**Syntax:** obj \<\< Set Print Footers( left footer, center footer, right header )

**Description:** Sets the left, center, and right footers for printed output

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Footer Test" ) );
w << Set Print Footers(
    "Today is: &d;"/*left*/, "&wt;"/*center*/,
    "Page &pn; of &pc;"/*right*/
);
w << Print Window;
```

### [Set Print Headers](#set-print-headers)[](#set-print-headers "Click to copy url")

**Syntax:** obj \<\< Set Print Headers( left header, center header, right header )

**Description:** Sets the left, center, and right headers for printed output

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Header Test" ) );
w << Set Print Headers(
    "Today is: &d;"/*left*/, "&wt;"/*center*/,
    "Page &pn; of &pc;"/*right*/
);
w << Print Window;
```

### [Set Property](#set-property)[](#set-property "Click to copy url")

**Syntax:** obj \<\< Set Property( "property", value )

**Description:** Sets the value for the named property for the display box.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Set Property( "Enabled", 0 );
```

### [Set Report Title](#set-report-title)[](#set-report-title "Click to copy url")

**Syntax:** obj \<\< Set Report Title( "string" )

**Description:** Changes the report title.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Set Report Title( "New Title" );
```

### [Set Stretch](#set-stretch)[](#set-stretch "Click to copy url")

**Syntax:** obj \<\< Set Stretch( x,y )

**Description:** Sets the horizontal and vertical stretching behavior of the box. Boxes that stretch with Window will resize as the window or splitter size changes. Boxes that stretch to Fill will stretch to fill available space in their container. Boxes with stretching turned Off generally will not stretch. Most boxes default to Neutral, which means that they will determine their behavior based on their child boxes.

**JMP Version Added:** 16

#### [Stretch to Fill](#stretch-to-fill)[](#stretch-to-fill "Click to copy url")

``` jsl
//This message applies to all display box objects
New Window( "Stretch",
    V List Box(
        H List Box( Text Edit Box( "String1" ), Text Edit Box( "String2" ) ),
        Spacer Box( Size( 20, 20 ), Color( "Light Red" ), <<Set Stretch( "Fill", "Off" ) )
    )
);
```

#### [Stretch with Window](#stretch-with-window)[](#stretch-with-window "Click to copy url")

``` jsl
//This message applies to all display box objects
New Window( "Example",
    H List Box(
        tv = Text Box( "V+V", <<rotate text( left ) ),
        V List Box(
            Text Box( "resize the containing window" ),
            th = Text Box( "H+H" ),
            ts = Spacer Box( <<Size( 10, 30 ), <<Color( "blue" ) )
        )
    )
);
tv << Vertical Alignment( "Center" );
th << Horizontal Alignment( "Center" );
th << Set Stretch( "Window", "Off" );
ts << Set Min Size( 5, 20 );
ts << Set Max Size( 100000, 100 );
ts << Set Stretch( "Window", "Window" );
```

### [Set Summary Behavior](#set-summary-behavior)[](#set-summary-behavior "Click to copy url")

**Syntax:** obj \<\< Set Summary Behavior( "Default"\|"Visible"\|"Collapse" )

**Description:** Sets the behavior of the box when a report is viewed in Summary mode.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
d << Report View( "Summary" );
r = d << Report;
tb = r[Table Box( 1 )];
tb << Set Summary Behavior( "Visible" );
```

### [Set Width](#set-width)[](#set-width "Click to copy url")

**Syntax:** obj \<\< Set Width( width )

**Description:** Sets the width of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Width( 400 );
```

### [Set Window Icon](#set-window-icon)[](#set-window-icon "Click to copy url")

**Syntax:** obj \<\< Set Window Icon( icon name )

**Description:** Sets the window icon.

``` jsl
//This message applies to all display box objects
w = New Window( "Example", ex = Button Box( "New Analysis" ) );
w << Set Window Icon( "Scatter3D" );
```

### [Set Window Size](#set-window-size)[](#set-window-size "Click to copy url")

**Syntax:** obj \<\< Set Window Size( x,y )

**Description:** Sets the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Set Window Size( 800, 1200 );
```

### [Set Window Title](#set-window-title)[](#set-window-title "Click to copy url")

**Syntax:** obj \<\< Set Window Title( "string" )

**Description:** Changes the window title.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Set Window Title( "New Title" );
```

### [Show Properties](#show-properties)[](#show-properties "Click to copy url")

**Syntax:** obj \<\< Show Properties

**Description:** Displays a property editor for display boxes

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Show Properties();
```

### [Show Tree Structure](#show-tree-structure)[](#show-tree-structure "Click to copy url")

**Syntax:** obj \<\< Show Tree Structure

**Description:** Displays a hierarchical tree structure of the display box and its related nodes.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Show Tree Structure();
```

### [Show Window](#show-window)[](#show-window "Click to copy url")

**Syntax:** obj \<\< Show Window( state=0\|1 )

**Description:** Shows or hides the window. This is useful for hiding windows temporarily. On by default.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Show Window( 0 );
Wait( 2 );
w << Show Window( 1 );
```

### [Sib](#sib)[](#sib "Click to copy url")

**Syntax:** obj \<\< Sib

**Description:** Returns the sibling of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisSibling = axisbox << sib();
Print( axisSibling << Class Name() );
```

### [Sib Append](#sib-append)[](#sib-append "Click to copy url")

**Syntax:** obj \<\< Sib Append( Display box, Horizontal\|Vertical )

**Description:** Adds a display box immediately after this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r()[framebox( 1 )];
fb << sib append(
    Text Box( "============ after ==============", Rotate Text( "Right" ) ),
    "Horizontal"
);
fb << sib append( Text Box( "=== below ===" ), "Vertical" );
```

### [Sib Prepend](#sib-prepend)[](#sib-prepend "Click to copy url")

**Syntax:** obj \<\< Sib Prepend( Display box, Horizontal\|Vertical )

**Description:** Adds a display box immediately before this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << sib prepend(
    Text Box( "    ============ before ==============", Rotate Text( "Right" ) ),
    "Horizontal"
);
fb << sib prepend( Text Box( "=== above ===" ), "Vertical" );
```

### [Size Window](#size-window)[](#size-window "Click to copy url")

**Syntax:** obj \<\< Size Window( x,y )

**Description:** Sets the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Size Window( 500, 500 );
```

### [Text Color](#text-color)[](#text-color "Click to copy url")

**Syntax:** obj \<\< Text Color( color ); color = obj \<\< Get Text Color

**Description:** Text will be drawn using the text color if it has been set. If the property has not been set, the box will inherit the text color of the containing box.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Text Color );
Wait( 2 );
tb << Text Color( "Red" );
```

### [Top Parent](#top-parent)[](#top-parent "Click to copy url")

**Syntax:** obj \<\< Top Parent

**Description:** Returns the root parent of this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rootParent = rbiv << Top Parent();
Print( rootParent << Class Name() );
```

### [UI Only](#ui-only)[](#ui-only "Click to copy url")

**Syntax:** obj \<\< UI Only( state=0\|1 ); state = obj \<\< Get UI Only

### [Update Window](#update-window)[](#update-window "Click to copy url")

**Syntax:** obj \<\< Update Window

**Description:** Update the window holding the displaybox if there are invalidated regions. The \<\<Inval message creates invalidated regions.

``` jsl
//This message applies to all display box objects
color = "green"; /* initial color in a variable */
New Window( "UpdateWindow example",
    Button Box( "red",
        color = "red";
        // try commenting out each of the 4 lines that follow, run the script,
        // click the buttons, and resize the windows (for example) to force a
        // redraw.  All 4 lines are important, though the last two may be
        // slightly different on Windows and Mac OSs.
        g1 << inval; /* tell the oval to redraw */
        g2 << inval; /* tell the rectangle to redraw */
        g1 << updateWindow; /* tell the oval window to update immediately */
        g2 << updateWindow; /* tell the rect window to update immediately */
        // this is a busy-wait to help demonstrate the various behaviors...
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 /* delay without wait(.5) */ );
    ),
    Button Box( "blue",
        color = "blue";
        g1 << inval; /* same comments */
        g2 << inval;
        g1 << updateWindow;
        g2 << updateWindow;
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 );
    )
);
New Window( "oval",
    g1 = Graph Box(/* the graph does NOT watch for the color variable to change
                      but will use the current value of color when it reshows */
        Fill Color( color );
        Oval( 10, 80, 70, 50, 1 );
    )
);
New Window( "rect",
    g2 = Graph Box(
        Fill Color( color );
        Rect( 10, 80, 70, 50, 1 );
    )
);
```

### [User Resizable](#user-resizable)[](#user-resizable "Click to copy url")

**Syntax:** obj \<\< User Resizable; obj \<\< Get User Resizable

**Description:** If the box is user resizable, the cursor will change near the bottom and right edges to allow drag-and-drop resizing.

``` jsl
root1 = Tree Node( "Parent 1" );
root2 = Tree Node( "Parent 2" );
c1 = Tree Node( "Child 1" );
c2 = Tree Node( "Child 2" );
c3 = Tree Node( "Child 3" );
c4 = Tree Node( "Child 4" );
root1 << Append( c1 );
root1 << Append( c2 );
root2 << Append( c3 );
root2 << Append( c4 );
New Window( "resize",
    H Splitter Box(
        Size( 600, 200 ),
        tree = Tree Box( {root1, root2} ),
        scroll = Scroll Box(
            Size( 300, 200 ),
            Picture Box( Open( "$SAMPLE_IMAGES/tile.jpg", jpg ) )
        )
    )
);
tree << Set Stretch( "Window", "Window" ) << Set Max Size( 10000, 10000 );
scroll << Set Stretch( "Window", "Window" ) << Set Max Size( 10000, 10000 );
Wait( 2 );
tree << User Resizable( {0, 0} );
scroll << User Resizable( {0, 0} );
```

### [Vertical Alignment](#vertical-alignment)[](#vertical-alignment "Click to copy url")

**Syntax:** obj \<\< Vertical Alignment( "Default"\|"Top"\|"Center"\|"Bottom" ); "Default"\|"Top"\|"Center"\|"Bottom" = obj \<\< Get Vertical Alignment

**Description:** Vertical alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Set Horizontal( 1 );
lb = r[List Box( 7 )];
lb << Border( 1 );
Wait( 2 );
lb << Vertical Alignment( "Bottom" );
```

### [Visibility](#visibility)[](#visibility "Click to copy url")

**Syntax:** obj \<\< Visibility( "Visible"\|"Hidden"\|"Collapse" ); "Visible"\|"Hidden"\|"Collapse" = obj \<\< Get Visibility

**Description:** Visibility determines whether a box is shown and whether it takes up space. The default value of "Visible" means that the object will be shown. A "Hidden" box is not shown but still takes up space, while a "Collapsed" box takes up no space in the layout.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Visibility );
Wait( 1 );
tb << Visibility( "Collapse" );
Show( tb << Get Visibility );
```

### [Window Class Name](#window-class-name)[](#window-class-name "Click to copy url")

**Syntax:** obj \<\< Window Class Name

**Description:** Returns the name of the window class for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
Show( biv << Window Class Name() );
Show( rbiv << Window Class Name() );
```

### [XPath](#xpath)[](#xpath "Click to copy url")

**Syntax:** obj \<\< XPath( XPath expression, \<English(0\|1)\>, \<NoData(0\|1)\> )

**Description:** Applies an XPath expression to the XML representation of the display tree and returns the results. By default, strings are returned in the local language, and the XML includes data values within some boxes. Use the English option to return English strings where available. Use the NoData option to omit the data values within boxes, which is useful for performance when your query is based only on box attributes.

#### [Attributes](#attributes)[](#attributes "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//OutlineBox[@isOpen='false']" )) << Close( 0 );
```

#### [Box type](#box-type)[](#box-type "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//TextEditBox" )) << Text Color( "Green" );
```

#### [Child box](#child-box)[](#child-box "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//OutlineBox[text()='Summary of Fit']/TableBox" )) <<
Make Into Data Table;
```

#### [Data](#data)[](#data "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//NumberColBoxItem[text()='40']/parent::*" )) <<
Text Color( "Green" );
```

#### [Display Seg](#display-seg)[](#display-seg "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//MarkerSeg" )) << Set Marker( "Square" );
```

#### [Text](#text)[](#text "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//OutlineBox[text()='Parameter Estimates']" )) << Close;
```

### [Zoom Window](#zoom-window)[](#zoom-window "Click to copy url")

**Syntax:** obj \<\< Zoom Window

**Description:** Resizes the window to be large enough to show all of its contents.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Set Window Size( 80, 120 );
Wait( 2 );
w << Zoom Window;
```

[ Previous](MatrixBox.html "MatrixBox") [Next ](MouseBox.html "MouseBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
