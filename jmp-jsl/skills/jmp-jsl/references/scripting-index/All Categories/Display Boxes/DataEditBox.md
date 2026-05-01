# DataEditBox

*Source: [https://jsl.jmp.com/All%20Categories/Display%20Boxes/DataEditBox.html](https://jsl.jmp.com/All%20Categories/Display%20Boxes/DataEditBox.html)*

---

# [DataEditBox](#dataeditbox)[](#dataeditbox "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Blink](#blink)[](#blink "Click to copy url")

**Syntax:** obj \<\< Blink

**Description:** Blinks the row displayed in the Data Edit Box.

``` jsl
Open( "$SAMPLE_DATA/SAT.jmp" );
New Window( "Example",
    cp = Cell Plot(
        Scale Uniformly( 0 ),
        Center at zero( 0 ),
        Y( :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n )
    )
);
cpr = cp << report;
cpb = cpr[Cell Plot Box( 1 )];
cpb << Row Editor;
win = Window( "Row Editor for SAT" );
dataedit = win[Data Edit Box( 1 )];
dataedit << Blink;
```

### [Find](#find)[](#find "Click to copy url")

**Syntax:** obj \<\< Find( search term )

**Description:** Shows the row found by the inputted search term.

``` jsl
Open( "$SAMPLE_DATA/SAT.jmp" );
New Window( "Example",
    cp = Cell Plot(
        Scale Uniformly( 0 ),
        Center at zero( 0 ),
        Y( :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n )
    )
);
cpr = cp << report;
cpb = cpr[Cell Plot Box( 1 )];
cpb << Row Editor;
win = Window( "Row Editor for SAT" );
dataedit = win[Data Edit Box( 1 )];
dataedit << Find( Contains( :State, "North Carolina" ) );
```

### [Go to row](#go-to-row)[](#go-to-row "Click to copy url")

**Syntax:** obj \<\< Go to row( row )

**Description:** Shows the inputted row in the Data Edit Box.

``` jsl
Open( "$SAMPLE_DATA/SAT.jmp" );
New Window( "Example",
    cp = Cell Plot(
        Scale Uniformly( 0 ),
        Center at zero( 0 ),
        Y( :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n )
    )
);
cpr = cp << report;
cpb = cpr[Cell Plot Box( 1 )];
cpb << Row Editor;
win = Window( "Row Editor for SAT" );
dataedit = win[Data Edit Box( 1 )];
dataedit << Go To Row( 23 );
```

### [New Row](#new-row)[](#new-row "Click to copy url")

**Syntax:** obj \<\< New Row

**Description:** Creates a new row in the data table and shows that row in the Data Edit Box.

``` jsl
Open( "$SAMPLE_DATA/SAT.jmp" );
New Window( "Example",
    cp = Cell Plot(
        Scale Uniformly( 0 ),
        Center at zero( 0 ),
        Y( :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n )
    )
);
cpr = cp << report;
cpb = cpr[Cell Plot Box( 1 )];
cpb << Row Editor;
win = Window( "Row Editor for SAT" );
dataedit = win[Data Edit Box( 1 )];
dataedit << New Row;
```

### [Next](#next)[](#next "Click to copy url")

**Syntax:** obj \<\< Next

**Description:** Show the next selected row in the Data Edit Box.

``` jsl
Open( "$SAMPLE_DATA/SAT.jmp" );
New Window( "Example",
    cp = Cell Plot(
        Scale Uniformly( 0 ),
        Center at zero( 0 ),
        Y( :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n )
    )
);
cpr = cp << report;
cpb = cpr[Cell Plot Box( 1 )];
cpb << Row Editor;
win = Window( "Row Editor for SAT" );
dataedit = win[Data Edit Box( 1 )];
dataedit << Next;
```

### [Next Selected](#next-selected)[](#next-selected "Click to copy url")

**Syntax:** obj \<\< Next Selected

**Description:** From the rows selected, show the next selected row in the Data Edit Box.

``` jsl
dt = Open( "$SAMPLE_DATA/SAT.jmp" );
New Window( "Example",
    cp = Cell Plot(
        Scale Uniformly( 0 ),
        Center at zero( 0 ),
        Y( :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n )
    )
);
cpr = cp << report;
cpb = cpr[Cell Plot Box( 1 )];
cpb << Row Editor;
win = Window( "Row Editor for SAT" );
dt << Select Where( dt:population > 10000000 );
dataedit = win[Data Edit Box( 1 )];
dataedit << Next Selected;
```

### [Prev](#prev)[](#prev "Click to copy url")

**Syntax:** obj \<\< Prev

**Description:** Show the previous selected row in the Data Edit Box.

``` jsl
Open( "$SAMPLE_DATA/SAT.jmp" );
New Window( "Example",
    cp = Cell Plot(
        Scale Uniformly( 0 ),
        Center at zero( 0 ),
        Y( :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n )
    )
);
cpr = cp << report;
cpb = cpr[Cell Plot Box( 1 )];
cpb << Row Editor;
win = Window( "Row Editor for SAT" );
dataedit = win[Data Edit Box( 1 )];
dataedit << Go To Row( 23 );
dataedit << Prev;
```

### [Prev Selected](#prev-selected)[](#prev-selected "Click to copy url")

**Syntax:** obj \<\< Prev Selected

**Description:** From the rows selected, show the previous selected row in the Data Edit Box.

``` jsl
dt = Open( "$SAMPLE_DATA/SAT.jmp" );
New Window( "Example",
    cp = Cell Plot(
        Scale Uniformly( 0 ),
        Center at zero( 0 ),
        Y( :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n )
    )
);
cpr = cp << report;
cpb = cpr[Cell Plot Box( 1 )];
cpb << Row Editor;
win = Window( "Row Editor for SAT" );
dt << Select Where( dt:population > 10000000 );
dataedit = win[Data Edit Box( 1 )];
dataedit << Prev Selected;
```

### [Save](#save)[](#save "Click to copy url")

**Syntax:** obj \<\< Save

**Description:** Saves the row values in the Data Edit Box to the data table.

``` jsl

dt = Open( "$SAMPLE_DATA/SAT.jmp" );
dt << Save( "$TEMP/SAT.jmp" );
New Window( "Example",
    cp = dt << Cell Plot(
        Scale Uniformly( 0 ),
        Center at zero( 0 ),
        Y( :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n )
    )
);
cpr = cp << report;
cpb = cpr[Cell Plot Box( 1 )];
cpb << Row Editor;
win = Window( "Row Editor for SAT" );
dataedit = win[Data Edit Box( 1 )];
dataedit << New Row;
dataedit << Save;
```

[ Previous](DataColumnNameBox.html "DataColumnNameBox") [Next ](DataFilterContextBox.html "DataFilterContextBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
