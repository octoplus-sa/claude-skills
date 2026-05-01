# LinesSeg

*Source: [https://jsl.jmp.com/All%20Categories/Display%20Boxes/LinesSeg.html](https://jsl.jmp.com/All%20Categories/Display%20Boxes/LinesSeg.html)*

---

# [LinesSeg](#linesseg)[](#linesseg "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Lines Seg](#lines-seg)[](#lines-seg "Click to copy url")

**Syntax:** ls = Lines Seg(\[x1 y1 x2 y2,...\])

**Description:** Creates a display seg with a sequence of line segments for the given x and y values. The optional second argument enables row state assignments, from either a data table (dt) or independently.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Child](#child)[](#child "Click to copy url")

**Syntax:** seg2 = obj \<\< Child

**Description:** Returns the first child of the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Child; // not many segs support children
```

### [Class Name](#class-name)[](#class-name "Click to copy url")

**Syntax:** classname = obj \<\< Class Name

**Description:** Returns the name of the display class for the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
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

### [Delete](#delete)[](#delete "Click to copy url")

**Syntax:** obj \<\< Delete

**Description:** Delete the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Delete;
```

### [First Value](#first-value)[](#first-value "Click to copy url")

**Syntax:** obj \<\< First Value( state=0\|1 )

**JMP Version Added:** 16

### [Frame](#frame)[](#frame "Click to copy url")

**Syntax:** FrameBox = obj \<\< Frame

**Description:** Returns the frame box that the display seg is in.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
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

### [Get Connected](#get-connected)[](#get-connected "Click to copy url")

**Syntax:** 0\|1 = obj \<\< Get Connected

**Description:** Returns the connection state of all line segments in the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Get Connected;
```

### [Get Description](#get-description)[](#get-description "Click to copy url")

**Syntax:** description = obj \<\< Get Description

**Description:** Gets the description for the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << get description();
```

### [Get Line](#get-line)[](#get-line "Click to copy url")

**Syntax:** \[x1 y1 x2 y2\] = obj \<\< Get Line( index )

**Description:** Returns the X and Y coordinates of the specified line.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Get Line( 2 );
```

### [Get Line Color](#get-line-color)[](#get-line-color "Click to copy url")

**Syntax:** color = obj \<\< Get Line Color

**Description:** Returns the color of the lines.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Get Line Color;
```

### [Get Line Count](#get-line-count)[](#get-line-count "Click to copy url")

**Syntax:** Number = obj \<\< Get Line Count

**Description:** Returns the number of lines in the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Get Line Count;
```

### [Get Line Style](#get-line-style)[](#get-line-style "Click to copy url")

**Syntax:** pen style = obj \<\< Get Line Style

**Description:** Returns the style of the lines.

**JMP Version Added:** 14

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Get Line Style;
```

### [Get Line Width](#get-line-width)[](#get-line-width "Click to copy url")

**Syntax:** number = obj \<\< Get Line Width

**Description:** Returns the width of the lines.

**JMP Version Added:** 14

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Get Line Width;
```

### [Get Lines](#get-lines)[](#get-lines "Click to copy url")

**Syntax:** \[x1 y1 x2 y2, ...\] = obj \<\< Get Lines

**Description:** Returns the X and Y coordinate values for all lines.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Get Lines;
```

### [Last Value](#last-value)[](#last-value "Click to copy url")

**Syntax:** obj \<\< Last Value( state=0\|1 )

**JMP Version Added:** 16

### [Line Color](#line-color)[](#line-color "Click to copy url")

**Syntax:** obj \<\< Line Color( color )

**Description:** Set the color for all lines in the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Set Line Color( "Green" );
```

### [Line Style](#line-style)[](#line-style "Click to copy url")

**Syntax:** obj \<\< Line Style( pen style )

**Description:** Sets the style of the lines. Options are Solid, Dotted, Dashed, DashDot, and DashDotDot.

**JMP Version Added:** 14

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Set Line Style( "Dotted" );
```

### [Line Width](#line-width)[](#line-width "Click to copy url")

**Syntax:** obj \<\< Line Width( "1"\|"2"\|"3"\|"4"\|"5"\|"6"\|"Other..." )

**Description:** Sets the width of the lines.

**JMP Version Added:** 14

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Set Line Width( 3 );
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
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Parent;
```

### [Set Connected](#set-connected)[](#set-connected "Click to copy url")

**Syntax:** obj \<\< Set Connected( state=0\|1 )

**Description:** Sets the connection state for all line segments in the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Set Connected( 1 );
```

### [Set Description](#set-description)[](#set-description "Click to copy url")

**Syntax:** obj \<\< Set Description( description )

**Description:** Sets the description for the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << set description( "my seg" );
```

### [Set Line Color](#set-line-color)[](#set-line-color "Click to copy url")

**Syntax:** obj \<\< Set Line Color( color )

**Description:** Set the color for all lines in the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Set Line Color( "Green" );
```

### [Set Line Style](#set-line-style)[](#set-line-style "Click to copy url")

**Syntax:** obj \<\< Set Line Style( pen style )

**Description:** Sets the style of the lines. Options are Solid, Dotted, Dashed, DashDot, and DashDotDot.

**JMP Version Added:** 14

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Set Line Style( "Dotted" );
```

### [Set Line Width](#set-line-width)[](#set-line-width "Click to copy url")

**Syntax:** obj \<\< Set Line Width( "1"\|"2"\|"3"\|"4"\|"5"\|"6"\|"Other..." )

**Description:** Sets the width of the lines.

**JMP Version Added:** 14

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
seg << Set Line Width( 3 );
```

### [Sib](#sib)[](#sib "Click to copy url")

**Syntax:** seg2 = obj \<\< Sib

**Description:** Returns the sibling of the display seg.

``` jsl
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
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
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
New Window( "Lines Seg Example", g = Graph Box( Lines Seg( lines ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( Lines Seg( 1 ) ));
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

[ Previous](LineUpRulerBox.html "LineUpRulerBox") [Next ](ListBox.html "ListBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
