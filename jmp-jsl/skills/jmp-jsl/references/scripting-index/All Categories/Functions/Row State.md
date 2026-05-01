# Row State

*Source: [https://jsl.jmp.com/All%20Categories/Functions/Row%20State.html](https://jsl.jmp.com/All%20Categories/Functions/Row%20State.html)*

---

# [Row State](#row-state)[](#row-state "Click to copy url")

### [As Row State](#as-row-state)[](#as-row-state "Click to copy url")

**Syntax:** rs = As Row State( x )

**Description:** Converts a number into a row state value.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
For Each Row(
    Row State() = As Row State(
        (:sex == "F") * 2 + (:sex == "M") * 4 + ((:sex == "F") * 2 + (:sex == "M") * 6) * 16
         + (:age - 11) * 256
    )
);
```

### [Color Of](#color-of)[](#color-of "Click to copy url")

**Syntax:** y = Color Of( \<rs\> ); Color Of( \<Row State( \<r\> )\> ) = y

**Description:** Returns the color component of the specified row state value, either a positive JMP color palette index or a negative RGB-encoded value. If Color Of is used as an L-value, it changes the color of the current (or rth) row in the current data table.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" ) << Color By Column( :height );
Color To RGB( Color Of( Row State( 3 ) ) );
Row() = 3;
Color To RGB( Color Of() );
```

### [Color State](#color-state)[](#color-state "Click to copy url")

**Syntax:** rs = Color State( color )

**Description:** Returns a row state value with the color component set to the specified value. The color argument can be any valid JSL color.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Color State( {1, 0.5, 1} );
Color To RGB( Color Of( Row State( 3 ) ) );
```

### [Combine States](#combine-states)[](#combine-states "Click to copy url")

**Syntax:** rs = Combine States( rs1, ... )

**Description:** Combines several row state values into one.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Combine States( Hue State( 5 ), Shade State( 1 ) );
```

### [Excluded](#excluded)[](#excluded "Click to copy url")

**Syntax:** y = Excluded( \<rs\> ); Excluded( \<Row State( \<r\> )\> ) = y

**Description:** Returns the excluded component of the specified row state value, 0 or 1. If the Excluded() function is used as an L-value, it changes the excluded state of the current (or rth) row in the current data table.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Excluded State( 1 );
Excluded( Row State( 3 ) );
Row() = 3;
Excluded();
```

### [Excluded State](#excluded-state)[](#excluded-state "Click to copy url")

**Syntax:** rs = Excluded State( x )

**Description:** Returns a row state value with the excluded component set to the specified value.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Excluded State( 1 );
Excluded( Row State( 3 ) );
```

### [Hidden](#hidden)[](#hidden "Click to copy url")

**Syntax:** y = Hidden( \<rs\> ); Hidden( \<Row State( \<r\> )\> ) = y

**Description:** Returns the hidden component of the specified row state value, 0 or 1. If Hidden is used as an L-value, it changes the hidden state of the current (or rth) row in the current data table.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Hidden State( 1 );
Hidden( Row State( 3 ) );
Row() = 3;
Hidden();
```

### [Hidden State](#hidden-state)[](#hidden-state "Click to copy url")

**Syntax:** rs = Hidden State( x )

**Description:** Returns a row state value with the hidden component set to the specified value.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Hidden State( 1 );
Hidden( Row State( 3 ) );
```

### [Hue State](#hue-state)[](#hue-state "Click to copy url")

**Syntax:** rs = Hue State( x )

**Description:** Returns a row state value with the color hue component set to the specified value. Needs to be combined with a Shade State() value to produce a valid color.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Combine States( Hue State( 5 ), Shade State( 1 ) );
```

### [Labeled](#labeled)[](#labeled "Click to copy url")

**Syntax:** y = Labeled( \<rs\> ); Labeled( \<Row State( \<r\> )\> ) = y

**Description:** Returns the labeled component of the specified row state value, 0 or 1. If Labeled is used as an L-value, it changes the labeled state of the current (or rth) row in the current data table.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Labeled State( 1 );
Labeled( Row State( 3 ) );
Row() = 3;
Labeled();
```

### [Labeled State](#labeled-state)[](#labeled-state "Click to copy url")

**Syntax:** rs = Labeled State( x )

**Description:** Returns a row state value with the labeled component set to the specified value.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Labeled State( 1 );
Labeled( Row State( 3 ) );
```

### [Marker Of](#marker-of)[](#marker-of "Click to copy url")

**Syntax:** y = Marker Of( \<rs\> ); Marker Of( \<Row State( \<r\> )\> ) = y

**Description:** Returns the marker component of the specified row state value. If Marker Of is used as an L-value, it changes the marker of the current (or rth) row in the current data table.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Marker State( 5 );
Marker Of( Row State( 3 ) );
Row() = 3;
Marker Of();
```

### [Marker State](#marker-state)[](#marker-state "Click to copy url")

**Syntax:** rs = Marker State( marker )

**Description:** Returns a row state value with the marker component set to the specified value. The marker argument specifies a marker and can be a positive integer, a character, a positive integer for Unicode character, or a hex character for Unicode character.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Marker State( 5 );
Marker Of( Row State( 3 ) );
```

### [Row State](#row-state_1)[](#row-state_1 "Click to copy url")

**Syntax:** y = Row State( \<dt\>, \<r\> ); Row State( \<dt\>, \<r\> ) = y

**Description:** Returns the row state of the current (or rth) row in the current data table. If the Row State() function is used as an L-value, it changes the row state of the current (or rth) row in the current data table.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Color State( {1, .5, 1} );
Color To RGB( Color Of( Row State( 3 ) ) );
```

### [Selected](#selected)[](#selected "Click to copy url")

**Syntax:** y = Selected( \<rs\> );Selected( \<Row State( \<r\> )\> ) = y

**Description:** Returns the selected component of the specified row state value, 0 or 1. If Selected is used as an L-value, it changes the selected state of the current (or rth) row in the current data table.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Selected State( 1 );
Selected( Row State( 3 ) );
Row() = 3;
Selected();
```

### [Selected State](#selected-state)[](#selected-state "Click to copy url")

**Syntax:** rs = Selected State( x )

**Description:** Returns a row state value with the selected component set to the specified value.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Selected State( 1 );
Selected( Row State( 3 ) );
```

### [Shade State](#shade-state)[](#shade-state "Click to copy url")

**Syntax:** rs = Shade State( x )

**Description:** Returns a row state value with the color shade component set to the specified value. Needs to be combined with a Hue State() value to produce a valid color.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( 3 ) = Combine States( Hue State( 5 ), Shade State( 1 ) );
```

[ Previous](Random.html "Random") [Next ](Row.html "Row")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
