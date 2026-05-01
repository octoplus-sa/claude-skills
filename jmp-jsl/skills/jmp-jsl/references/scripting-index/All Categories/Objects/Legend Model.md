# Legend Model

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Legend%20Model.html](https://jsl.jmp.com/All%20Categories/Objects/Legend%20Model.html)*

---

# [Legend Model](#legend-model)[](#legend-model "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Get Fill Color](#get-fill-color)[](#get-fill-color "Click to copy url")

**Syntax:** obj \<\< Get Fill Color

**Description:** Returns the fill color of the Legend Model Item which is linked to a Display Seg in the graph.

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Overlay( :sex ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Ellipse( X, Y, Legend( 3 ) ) )
);
server = gb << Get Legend Server;
item = server << Get Legend Item( 3, 1 );
Show( item << Get Fill Color );
```

### [Get Gradient Settings](#get-gradient-settings)[](#get-gradient-settings "Click to copy url")

**Syntax:** obj \<\< Get Gradient Settings

**Description:** Returns a list of Gradient Settings for the Legend Model Item which is linked to a Display Seg in the graph.

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Color( :weight ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) )
);
server = gb << Get Legend Server;
item = server << Get Legend Item( 1, 1 );
Print( item << Get Gradient Settings );
```

### [Get Label](#get-label)[](#get-label "Click to copy url")

**Syntax:** obj \<\< Get Label

**Description:** Returns the label of the Legend Model Item.

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Overlay( :sex ), Color( :age ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) )
);
server = gb << Get Legend Server;
item = server << Get Legend Item( 2, 1 );
Print( item << Get Label );
```

### [Get Marker Size Settings](#get-marker-size-settings)[](#get-marker-size-settings "Click to copy url")

**Syntax:** obj \<\< Get Marker Size Settings

**Description:** Returns a list of Marker Size Settings for the Legend Model Item which is linked to a Display Seg in the graph.

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Size( :height ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) )
);
server = gb << Get Legend Server;
item = server << Get Legend Item( 1, 1 );
Print( item << Get Marker Size Settings );
```

### [Get Pen Settings](#get-pen-settings)[](#get-pen-settings "Click to copy url")

**Syntax:** obj \<\< Get Pen Settings

**Description:** Returns a list of Pen Settings for the Legend Model Item which is linked to a Display Seg in the graph.

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Overlay( :sex ), Color( :age ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) )
);
server = gb << Get Legend Server;
item = server << Get Legend Item( 1, 7 );
Print( item << Get Pen Settings );
```

### [Get Type](#get-type)[](#get-type "Click to copy url")

**Syntax:** obj \<\< Get Type

**Description:** Returns the type of the Legend Model Item. Types are: "None", "Marker", "H Line", "V Line", "Step", "Bar", "V Box Plot", "H Interval", "V Interval", "H Bar Box Plot", "V Bar Box Plot", "OHLC Plot", "H Box Plot",Gradient", "Density Gradient", "Fill and Line", "Marker Size", "Line Size", Gradient Line", "Gradient Contour", "Mark Color", "Marker Size Categorical", "Cell Size".

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Overlay( :sex ), Color( :age ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) )
);
server = gb << Get Legend Server;
item = server << Get Legend Item( 2, 1 );
Print( item << Get Type );
```

### [Set Label](#set-label)[](#set-label "Click to copy url")

**Syntax:** obj \<\< Set Label( text )

**Description:** Sets the label for the Legend Model Item which is linked to a Display Seg in the graph.

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Overlay( :sex ), Color( :age ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) )
);
server = gb << Get Legend Server;
items = server << Get Legend Items;
For Each( {item, index}, items[1], item << Set Label( "Item " || Char( index ) ) );
```

### [Set Properties](#set-properties)[](#set-properties "Click to copy url")

**Syntax:** obj \<\< Set Properties

**Description:** Set arbitrary display properties for the Legend Model Item which is linked to a Display Seg in the graph.

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Size( :height ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) )
);
server = gb << Get Legend Server;
item = server << Get Legend Item( 1, 1 );
item << Set Properties(
    {Marker Size( 5 ), Marker Scale( {Marker Size Minimum( "Dot" ), Style( "Nested Full" )} )
    }
);
```

[ Previous](Legend%20Item.html "Legend Item") [Next ](Life%20Distribution%20and%20Extensions.html "Life Distribution and Extensions")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
