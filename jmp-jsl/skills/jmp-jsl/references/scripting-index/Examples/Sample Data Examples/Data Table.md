# Data Table

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Data%20Table.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Data%20Table.html)*

---

# [Data Table](#data-table)[](#data-table "Click to copy url")

More examples for this topic using the sample data files provided with JMP

## [Concatenate](#concatenate)[](#concatenate "Click to copy url")

### [Concatenate 2 tables](#concatenate-2-tables)[](#concatenate-2-tables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cancer2.jmp");
// Concatenate
Open( "$SAMPLE_DATA/Cancer1.jmp" ) <<
Concatenate( Data Table( "Cancer2" ) );
```

``` jsl
// Open data table
dt = Open("$Sample_Data/Cancer1.jmp");
// Concatenate
Data Table( "Cancer1" ) <<
Concatenate(
    Open( "$SAMPLE_DATA/Cancer2.jmp" )
);
```

## [Value Labels](#value-labels)[](#value-labels "Click to copy url")

### [Set value labels column property](#set-value-labels-column-property)[](#set-value-labels-column-property "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Big Class.jmp");
// Set Age Value Labels
Column( "age" ) <<
ValueLabels(
    {12, 13, 14, 15, 16, 17},
    {"Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen"}
);
Column( "age" ) << UseValueLabels;
```

[ Previous](DOE.html "DOE") [Next ](Data%20Tables.html "Data Tables")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
