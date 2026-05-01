# Pareto Plot

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Pareto%20Plot.html](https://jsl.jmp.com/All%20Categories/Objects/Pareto%20Plot.html)*

---

# [Pareto Plot](#pareto-plot)[](#pareto-plot "Click to copy url")

## [Columns](#columns)[](#columns "Click to copy url")

### [By](#by)[](#by "Click to copy url")

**Syntax:** obj \<\< By( column(s) )

**Description:** Performs a separate analysis for each level of the specified column.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Show Pareto Bars( 0 );
```

### [Cause](#cause)[](#cause "Click to copy url")

**Syntax:** obj \<\< Cause( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
```

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    Freq( :_freqcol )
);
obj << Show Pareto Bars( 0 );
```

### [Grouping](#grouping)[](#grouping "Click to copy url")

**Syntax:** obj \<\< Grouping( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
```

### [Subcategory](#subcategory)[](#subcategory "Click to copy url")

**Syntax:** obj \<\< Subcategory( column )

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
```

### [Weight](#weight)[](#weight "Click to copy url")

**Syntax:** obj \<\< Weight( column )

**Description:** Specifies a column whose values assign a weight to each row for the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_weightcol", Numeric, Continuous, Set Each Value( Random Beta( 1, 1 ) ) );
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    Weight( :_weightcol )
);
obj << Show Pareto Bars( 0 );
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** obj \<\< X( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Alias](#alias)[](#alias "Click to copy url")

**Syntax:** obj \<\< Alias( cause, alias )

**Description:** Sets a different name for a cause.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ), Alias( "doping", "substitution" ) );
```

### [Bar Label Format](#bar-label-format)[](#bar-label-format "Click to copy url")

**Syntax:** obj \<\< Bar Label Format

**Description:** Sets the format for the Pareto bar labels.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Freq( :N ),
    Label( 1 ),
    Bar Label Format( "Currency", "USD", Use thousands separator( 0 ), 12, 0 )
);
```

### [Bar Style](#bar-style)[](#bar-style "Click to copy url")

**Syntax:** obj \<\< Bar Style( "Bar"\|"Float" )

**Description:** Controls the display of the Pareto bars.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Bar Style( Float );
```

### [Cause Colors](#cause-colors)[](#cause-colors "Click to copy url")

**Syntax:** obj \<\< Cause Colors( { { causeName, color }, ...} )

**Description:** Changes the color of the specified bars.

**JMP Version Added:** 17

#### [All Colors](#all-colors)[](#all-colors "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ), Show Cum Percent Points( 1 ) );
obj << Cause Colors( "Orange" );
```

#### [Multiple Color List](#multiple-color-list)[](#multiple-color-list "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ), Show Cum Percent Points( 1 ) );
obj << Cause Colors( {{"miscellaneous", "Purple"}, {"silicon defect", "Red"}} );
```

#### [Single Color List](#single-color-list)[](#single-color-list "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ), Show Cum Percent Points( 1 ) );
obj << Cause Colors( {"corrosion", "Light Gray"} );
```

#### [Single RGB Color](#single-rgb-color)[](#single-rgb-color "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ), Show Cum Percent Points( 1 ) );
obj << Cause Colors( {117, 150, 200} );
```

### [Cause Labels](#cause-labels)[](#cause-labels "Click to copy url")

**Syntax:** obj \<\< Cause Labels( { { causeName, 0\|1 }, ...} )

**Description:** Displays the count as a label for the specified bars.

**JMP Version Added:** 17

#### [All Causes](#all-causes)[](#all-causes "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ), Cause Labels( 1 ) );
```

#### [List of Causes](#list-of-causes)[](#list-of-causes "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Freq( :N ),
    Cause Labels( {{"contamination", 1}, {"oxide defect", 1}} )
);
```

#### [Single Cause](#single-cause)[](#single-cause "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Freq( :N ),
    Cause Labels( {"contamination", 1} )
);
```

### [Cause Markers](#cause-markers)[](#cause-markers "Click to copy url")

**Syntax:** obj \<\< Cause Markers( { { causeName, marker }, ...} )

**Description:** Changes the cumulative percent marker shown on the graph for the specified bars.

**JMP Version Added:** 17

#### [All Causes](#all-causes_1)[](#all-causes_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ), Show Cum Percent Points( 1 ) );
obj << Cause Markers( 1 );
```

#### [List of Causes](#list-of-causes_1)[](#list-of-causes_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ), Show Cum Percent Points( 1 ) );
obj << Cause Markers( {{"miscellaneous", "Square"}, {"silicon defect", "Diamond"}} );
```

#### [Single Cause](#single-cause_1)[](#single-cause_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ), Show Cum Percent Points( 1 ) );
obj << Cause Markers( {"silicon defect", "Diamond"} );
```

### [Combine Causes](#combine-causes)[](#combine-causes "Click to copy url")

**Syntax:** obj \<\< Combine Causes( {cause1, cause2, ... } \| \<\< First(N) \| \<\< Last(N), \<label\> )

**Description:** Combines the specified causes into a single cause. The causes can be specified as a list of cause names or sending the First or Last message with a number of causes to combine. Optionally, a label for the combined cause can be specified.

#### [Labeled](#labeled)[](#labeled "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Freq( :N ),
    Combine Causes( {"miscellaneous", "silicon defect", "doping"}, "Others" )
);
```

#### [No Label](#no-label)[](#no-label "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
Wait( 2 );
obj << Combine Causes( {"miscellaneous", "silicon defect", "doping"} );
```

#### [Send Last](#send-last)[](#send-last "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Freq( :N ),
    Combine Causes( <<Last( 2 ), "Last 2" )
);
```

### [Cum Line Connect Style](#cum-line-connect-style)[](#cum-line-connect-style "Click to copy url")

**Syntax:** obj \<\< Cum Line Connect Style( "Line"\|"Curve"\|"Step" )

**Description:** Controls the connection style of the cumulative percent line.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Cum Line Connect Style( "Step" );
```

### [Cum Percent Curve Color](#cum-percent-curve-color)[](#cum-percent-curve-color "Click to copy url")

**Syntax:** obj \<\< Cum Percent Curve Color( color )

**Description:** Changes the color of the cumulative percent curve on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Cum Percent Curve Color( "Red" );
```

### [Cum Percent Label Format](#cum-percent-label-format)[](#cum-percent-label-format "Click to copy url")

**Syntax:** obj \<\< Cum Percent Label Format

**Description:** Sets the format for the cumulative percent marker labels.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Freq( :N ),
    Label Cum Percent Points( 1 ),
    Cum Percent Label Format( "Percent", 12, 1 )
);
```

### [Get Causes](#get-causes)[](#get-causes "Click to copy url")

**Syntax:** obj \<\< Get Causes( \<"First" \| "Last" \| "First %" \| "Last %", number\> )

**Description:** Returns a list of cause names from the Pareto plot based on the current order of appearance. If no options are provided, then all causes are returned. Otherwise, it uses the keyword and the number to return either the first N, last N, first N percent, or last N percent.

**JMP Version Added:** 17

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot( Cause( :Causes ), Freq( :Count ) );
obj << Get Causes;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot( Cause( :Causes ), Freq( :Count ) );
obj << Get Causes( "First", 3 );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot( Cause( :Causes ), Freq( :Count ) );
obj << Get Causes( "Last %", 10 );
```

**Example 4**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot(
    Cause( :Causes ),
    Freq( :Count ),
    Combine Causes( {"Corrosion", "Metallization", "Doping"}, "3 Others" ),
    Move to Last( {"3 Others"} )
);
obj << Get Causes( "Last", 3 );
```

### [Group Settings](#group-settings)[](#group-settings "Click to copy url")

**Syntax:** obj \<\< Group Settings( Column, \<Levels In View( number )\>, \<Start Level( number ), \<Show Title (0\|1)\>, \<Title Color( color )\>, \<Levels Color( color )\> )

**Description:** Controls the appearance of the grouped Pareto

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Group Settings(
        :clean,
        Levels In View( 1 ),
        Start Level( 1 ),
        Title Color( "Blue" ),
        Levels Color( "Light Blue" )
    )
);
```

### [Label Cum Percent Points](#label-cum-percent-points)[](#label-cum-percent-points "Click to copy url")

**Syntax:** obj \<\< Label Cum Percent Points( state=0\|1 )

**Description:** Displays or hides the labels showing cumulative percentages for each bar on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Label Cum Percent Points( 1 );
```

### [Legend Position](#legend-position)[](#legend-position "Click to copy url")

**Syntax:** obj \<\< Legend Position( ("Right" \| "Bottom" \| "Left" \| "Top") )

**Description:** Sets the position of the legend.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Legend Position( "Bottom" );
```

### [Legend Settings](#legend-settings)[](#legend-settings "Click to copy url")

**Syntax:** obj \<\< Legend Settings

**Description:** Opens a dialog to modify the properties of the legend.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
Wait( 1 );
obj << Legend Settings();
```

### [Move to First](#move-to-first)[](#move-to-first "Click to copy url")

**Syntax:** obj \<\< Move to First( {level1, level2, ...} \| \<\< First(N) \| \<\< Last(N) )

**Description:** Moves the bar(s) for the specified level(s) to appear first. The levels can be specified as a list of cause names or by sending the First or Last message with a number of causes to combine.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure Raw Data.jmp" );
obj = dt << Pareto Plot( Cause( :failure ) );
obj << Move to First( {"corrosion", "doping"} );
```

### [Move to Last](#move-to-last)[](#move-to-last "Click to copy url")

**Syntax:** obj \<\< Move to Last( {level1, level2, ...} \| \<\< First(N) \| \<\< Last(N) )

**Description:** Moves the bar(s) for the specified level(s) to appear last. The levels can be specified as a list of cause names or by sending the First or Last message with a number of causes to combine.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure Raw Data.jmp" );
obj = dt << Pareto Plot( Cause( :failure ) );
obj << Move to Last( {"miscellaneous"} );
```

### [N Legend](#n-legend)[](#n-legend "Click to copy url")

**Syntax:** obj \<\< N Legend( state=0\|1 )

**Description:** Displays the total sample size in the plot area.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure Raw Data.jmp" );
obj = dt << Pareto Plot( Cause( :failure ) );
obj << N Legend( 1 );
```

### [No Plot](#no-plot)[](#no-plot "Click to copy url")

**Syntax:** obj \<\< No Plot( state=0\|1 )

**Description:** Closes the outline node for the Pareto plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot( Cause( :Causes ), Freq( :Count ), Per Unit Rates( 1 ) );
obj << No Plot( 1 );
```

### [Orientation](#orientation)[](#orientation "Click to copy url")

**Syntax:** obj \<\< Orientation( "Vertical"\|"Horizontal" )

**Description:** Controls the orientation of the Pareto plot.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Orientation( "Horizontal" );
```

### [Pareto Line Connect Style](#pareto-line-connect-style)[](#pareto-line-connect-style "Click to copy url")

**Syntax:** obj \<\< Pareto Line Connect Style( "Line"\|"Curve"\|"Step" )

**Description:** Controls the connection style of the Pareto line.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    Show Pareto Bars( 0 )
);
obj << Pareto Line Connect Style( "Step" );
```

### [Per Unit Rates](#per-unit-rates)[](#per-unit-rates "Click to copy url")

**Syntax:** obj \<\< Per Unit Rates( state=0\|1 )

**Description:** Compares defect rates across groups. If a sample size is specified, defects per unit (DPU) and parts per million (PPM) columns are added to the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot(
    Cause( :Causes ),
    Per Unit Analysis( Constant( Sample Size( 1000 ) ) ),
    Freq( :Count )
);
obj << Per Unit Rates( 1 );
```

### [Percent Scale](#percent-scale)[](#percent-scale "Click to copy url")

**Syntax:** obj \<\< Percent Scale( state=0\|1 )

**Description:** Displays the left vertical axis as a percent scale.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure Raw Data.jmp" );
obj = dt << Pareto Plot( Cause( :failure ) );
obj << Percent Scale( 1 );
```

### [Pie Chart](#pie-chart)[](#pie-chart "Click to copy url")

**Syntax:** obj \<\< Pie Chart( state=0\|1 )

**Description:** Displays the bars as a pie chart.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ) );
obj << Pie Chart( 1 );
```

### [Reorder Horizontal](#reorder-horizontal)[](#reorder-horizontal "Click to copy url")

**Syntax:** obj \<\< Reorder Horizontal( level1, level2, ... )

**Description:** Reorders horizontally grouped Pareto plots when there are two or more groups.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ) );
Wait( 2 );
obj << Reorder Horizontal( "before", "after" );
```

### [Reorder Vertical](#reorder-vertical)[](#reorder-vertical "Click to copy url")

**Syntax:** obj \<\< Reorder Vertical( level1, level2, ... )

**Description:** Reorders vertically grouped Pareto plots when there are two or more variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot( Cause( :Causes ), X( :Process, :Day ), Freq( :Count ) );
Wait( 2 );
obj << Reorder Vertical( "Process B", "Process A" );
```

### [Separate Causes](#separate-causes)[](#separate-causes "Click to copy url")

**Syntax:** obj \<\< Separate Causes

**Description:** Separates combined causes into separate bars.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Combine Causes( {"miscellaneous", "silicon defect", "doping"} );
Wait( 2 );
obj << Separate Causes;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Combine Causes( {"miscellaneous", "silicon defect", "doping"}, "Other Causes" );
Wait( 2 );
obj << Separate Causes( "Other Causes" );
```

### [Show Cum Percent Axis](#show-cum-percent-axis)[](#show-cum-percent-axis "Click to copy url")

**Syntax:** obj \<\< Show Cum Percent Axis( state=0\|1 )

**Description:** Displays or hides the cumulative percent axis on the right side of the plot. Note: Only available on the right most plot when an X or Grouping variable is present. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ) );
obj << Show Cum Percent Axis( 1 );
```

### [Show Cum Percent Curve](#show-cum-percent-curve)[](#show-cum-percent-curve "Click to copy url")

**Syntax:** obj \<\< Show Cum Percent Curve( state=0\|1 )

**Description:** Displays or hides the cumulative percent curve. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ) );
obj << Show Cum Percent Curve( 1 );
```

### [Show Cum Percent Points](#show-cum-percent-points)[](#show-cum-percent-points "Click to copy url")

**Syntax:** obj \<\< Show Cum Percent Points( state=0\|1 )

**Description:** Displays or hides the cumulative percent points on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Show Cum Percent Points( 1 );
```

### [Show Error Bars](#show-error-bars)[](#show-error-bars "Click to copy url")

**Syntax:** obj \<\< Show Error Bars( state=0\|1 )

**Description:** Shows or hides error bars on the Pareto bars for confidence range.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ) );
obj << Show Error Bars( 1 );
```

### [Show Pareto Bars](#show-pareto-bars)[](#show-pareto-bars "Click to copy url")

**Syntax:** obj \<\< Show Pareto Bars( state=0\|1 )

**Description:** Shows or hides the bars displaying the value for each cause. On by default.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
```

### [Show Pareto Line](#show-pareto-line)[](#show-pareto-line "Click to copy url")

**Syntax:** obj \<\< Show Pareto Line( state=0\|1 )

**Description:** Shows or hides a line that connects the values for each cause.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ) );
obj << Show Pareto Line( 1 );
```

### [Show Pareto Markers](#show-pareto-markers)[](#show-pareto-markers "Click to copy url")

**Syntax:** obj \<\< Show Pareto Markers( state=0\|1 )

**Description:** Shows or hides markers at the value for each cause.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ) );
obj << Show Pareto Markers( 1 );
```

### [Subcategory Bar Style](#subcategory-bar-style)[](#subcategory-bar-style "Click to copy url")

**Syntax:** obj \<\< Subcategory Bar Style( "Side by side"\|"Stacked"\|"Bullet"\|"Nested"\|"Single"\|"Needle"\|"Float" )

**Description:** Controls the display of the bars when a subcategory is present.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Subcategory( :clean ),
    Freq( :N ),
    Subcategory Bar Style( Stacked )
);
```

### [Subset](#subset)[](#subset "Click to copy url")

**Syntax:** obj \<\< Subset

**Description:** Creates a subset data table from the selections in the Pareto plot

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
dt << Select Where( :Causes == "Corrosion" );
obj = dt << Pareto Plot( Cause( :Causes ), Freq( :Count ) );
obj << Subset;
```

### [Swap Group Orientation](#swap-group-orientation)[](#swap-group-orientation "Click to copy url")

**Syntax:** obj \<\< Swap Group Orientation( state=0\|1 )

**Description:** Swaps the horizontal and vertical groups. If there is only one group, changes the display orientation.

**JMP Version Added:** 17

#### [One Group](#one-group)[](#one-group "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot( Cause( :Causes ), X( :Process ), Freq( :Count ) );
Wait( 2 );
obj << Swap Group Orientation( true );
```

#### [Two Groups](#two-groups)[](#two-groups "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot( Cause( :Causes ), X( :Process, :Day ), Freq( :Count ) );
Wait( 2 );
obj << Swap Group Orientation( true );
```

### [Synchronize Y Axes](#synchronize-y-axes)[](#synchronize-y-axes "Click to copy url")

**Syntax:** obj \<\< Synchronize Y Axes( state=0\|1 )

**Description:** Locks the right y-axis so that zooming and panning is synchronized with the left y-axis On by default.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), Freq( :N ) );
obj << Synchronize Y Axes( 0 );
```

### [Tables Match Plot](#tables-match-plot)[](#tables-match-plot "Click to copy url")

**Syntax:** obj \<\< Tables Match Plot( {\<Per Unit Rates( 0\|1 )\>, \<Test Rate Within Groups( 0\|1 )\>, \<Test Rates Across Groups( 0\|1 )\>} )

**Description:** Controls whether the count analysis tables display the combined cause values that match the Pareto plot or the uncombined original causes. A value of 1 will show the combined cause values. A value of 0 will show the uncombined values. Not all tables must be specified in the command.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Per Unit Rates( 1 ),
    Test Rate Within Groups( 1 ),
    Test Rates Across Groups( 1 ),
    Combine Causes( {"silicon defect", "oxide defect", "doping"}, "3 Others" ),
    Move to Last( {"corrosion", "miscellaneous", "3 Others"} )
);
obj << Tables Match Plot(
    {Per Unit Rates( 1 ), Test Rate Within Groups( 1 ), Test Rates Across Groups( 1 )}
);
```

### [Test Rate Within Groups](#test-rate-within-groups)[](#test-rate-within-groups "Click to copy url")

**Syntax:** obj \<\< Test Rate Within Groups( state=0\|1 )

**Description:** Performs a likelihood ratio test within groups, testing whether the causes have equal ratios within the groups.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot( Cause( :Causes ), X( :Process ), Freq( :Count ) );
obj << Test Rate Within Groups( 1 );
```

### [Test Rates Across Groups](#test-rates-across-groups)[](#test-rates-across-groups "Click to copy url")

**Syntax:** obj \<\< Test Rates Across Groups( state=0\|1 )

**Description:** Performs a likelihood ratio test across groups, testing whether the causes have equal ratios across the groups.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Pareto Plot( Cause( :Causes ), X( :Process, :Day ), Freq( :Count ) );
obj << Test Rates Across Groups( 1 );
```

### [Threshold of Combined Causes](#threshold-of-combined-causes)[](#threshold-of-combined-causes "Click to copy url")

**Syntax:** obj \<\< Threshold of Combined Causes

**Description:** Combines causes which fall below the threshold. This happens on initial platform launch.

#### [Count](#count)[](#count "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Freq( :N ),
    Threshold of Combined Causes( Count( 5 ) )
);
```

#### [Tail %](#tail)[](#tail "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Freq( :N ),
    Threshold of Combined Causes( Tail %( 25 ) )
);
```

### [Ungroup Plots](#ungroup-plots)[](#ungroup-plots "Click to copy url")

**Syntax:** obj \<\< Ungroup Plots( state=0\|1 )

**Description:** Separates grouped Pareto plots when there are two or more groups.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ) );
Wait( 2 );
obj << Ungroup Plots( 1 );
```

## [Shared Item Messages](#shared-item-messages)[](#shared-item-messages "Click to copy url")

### [Action](#action)[](#action "Click to copy url")

**Syntax:** obj \<\< Action

**Description:** All-purpose trapdoor within a platform to insert expressions to evaluate. Temporarily sets the DisplayBox and DataTable contexts to the Platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Bivariate(
    Y( :height ),
    X( :weight ),
    Action( Distribution( Y( :height, :weight ), Histograms Only ) )
);
```

### [Apply Preset](#apply-preset)[](#apply-preset "Click to copy url")

**Syntax:** Apply Preset( preset ); Apply Preset( source, label, \<Folder( folder {, folder2, ...} )\> )

**Description:** Apply a previously created preset to the object, updating the options and customizations to match the saved settings.

**JMP Version Added:** 18

#### [Anonymous preset](#anonymous-preset)[](#anonymous-preset "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
dt2 = Open( "$SAMPLE_DATA/Dogs.jmp" );
obj2 = dt2 << Oneway( Y( :LogHist0 ), X( :drug ) );
Wait( 1 );
obj2 << Apply Preset( preset );
```

#### [Search by name](#search-by-name)[](#search-by-name "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "Compare Distributions" );
```

#### [Search within folder(s)](#search-within-folders)[](#search-within-folders "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "t-Tests", Folder( "Compare Means" ) );
```

### [Automatic Recalc](#automatic-recalc)[](#automatic-recalc "Click to copy url")

**Syntax:** obj \<\< Automatic Recalc( state=0\|1 )

**Description:** Redoes the analysis automatically for exclude and data changes. If the Automatic Recalc option is turned on, you should consider using Wait(0) commands to ensure that the exclude and data changes take effect before the recalculation.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Automatic Recalc( 1 );
dt << Select Rows( 5 ) << Exclude( 1 );
```

### [Broadcast](#broadcast)[](#broadcast "Click to copy url")

**Syntax:** obj \<\< Broadcast(message)

**Description:** Broadcasts a message to a platform. If return results from individual objects are tables, they are concatenated if possible, and the final format is identical to either the result from the Save Combined Table option in a Table Box or the result from the Concatenate option using a Source column. Other than those, results are stored in a list and returned.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Diameter.jmp" );
objs = Control Chart Builder(
    Variables( Subgroup( :DAY ), Y( :DIAMETER ) ),
    By( :OPERATOR )
);
objs[1] << Broadcast( Save Summaries );
```

### [Column Switcher](#column-switcher)[](#column-switcher "Click to copy url")

**Syntax:** obj \<\< Column Switcher(column reference, {column reference, ...}, \< Title(title) \>, \< Close Outline(0\|1) \>, \< Retain Axis Settings(0\|1) \>, \< Layout(0\|1) \>)

**Description:** Adds a control panel for changing the platform's variables

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Contingency( Y( :size ), X( :marital status ) );
ColumnSwitcherObject = obj << Column Switcher(
    :marital status,
    {:sex, :country, :marital status}
);
```

### [Copy ByGroup Script](#copy-bygroup-script)[](#copy-bygroup-script "Click to copy url")

**Syntax:** obj \<\< Copy ByGroup Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Show Pareto Bars( 0 );
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Data Table Window;
```

### [Get By Levels](#get-by-levels)[](#get-by-levels "Click to copy url")

**Syntax:** obj \<\< Get By Levels

**Description:** Returns an associative array mapping the by group columns to their values.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv << Get By Levels;
```

### [Get ByGroup Script](#get-bygroup-script)[](#get-bygroup-script "Click to copy url")

**Syntax:** obj \<\< Get ByGroup Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Show Pareto Bars( 0 );
t = obj[1] << Get ByGroup Script;
Show( t );
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
t = obj << Get Container;
Show( (t << XPath( "//OutlineBox" )) << Get Title );
```

#### [Platform with Filter](#platform-with-filter)[](#platform-with-filter "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) ),
    Local Data Filter(
        Add Filter(
            columns( :age, :sex, :height ),
            Where( :age == {12, 13, 14} ),
            Where( :sex == "F" ),
            Where( :height >= 55 ),
            Display( :age, N Items( 6 ) )
        )
    )
);
New Window( "platform boxes",
    H List Box(
        Outline Box( "Report(platform)", Report( gb ) << Get Picture ),
        Outline Box( "platform << Get Container", (gb << Get Container) << Get Picture )
    )
);
```

### [Get Data Table](#get-data-table)[](#get-data-table "Click to copy url")

**Syntax:** obj \<\< Get Data Table

**Description:** Returns a reference to the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Group Platform](#get-group-platform)[](#get-group-platform "Click to copy url")

**Syntax:** obj \<\< Get Group Platform

**Description:** Return the Group Platform object if this platform is part of a Group. Otherwise, returns Empty().

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( Y( :weight ), X( :height ), By( :sex ) );
group = biv[1] << Get Group Platform;
Wait( 1 );
group << Layout( "Arrange in Tabs" );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
t = obj << Get Timing;
Show( t );
```

### [Get Web Support](#get-web-support)[](#get-web-support "Click to copy url")

**Syntax:** obj \<\< Get Web Support

**Description:** Return a number indicating the level of Interactive HTML support for the display object. 1 means some or all elements are supported. 0 means no support.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
s = obj << Get Web Support();
Show( s );
```

### [Get Where Expr](#get-where-expr)[](#get-where-expr "Click to copy url")

**Syntax:** obj \<\< Get Where Expr

**Description:** Returns the Where expression for the data subset, if the platform was launched with By() or Where(). Otherwise, returns Empty()

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv2 = dt << Bivariate( X( :height ), Y( :weight ), Where( :age < 14 & :height > 60 ) );
Show( biv[1] << Get Where Expr, biv2 << Get Where Expr );
```

### [Ignore Platform Preferences](#ignore-platform-preferences)[](#ignore-platform-preferences "Click to copy url")

**Syntax:** Ignore Platform Preferences( state=0\|1 )

**Description:** Ignores the current settings of the platform's preferences. The message is ignored when sent to the platform after creation.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Bivariate(
    Ignore Platform Preferences( 1 ),
    Y( :height ),
    X( :weight ),
    Action( Distribution( Y( :height, :weight ), Histograms Only ) )
);
```

### [Local Data Filter](#local-data-filter)[](#local-data-filter "Click to copy url")

**Syntax:** obj \<\< Local Data Filter

**Description:** To filter data to specific groups or ranges, but local to this platform

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dt << Distribution(
    Nominal Distribution( Column( :country ) ),
    Local Data Filter(
        Add Filter( columns( :sex ), Where( :sex == "Female" ) ),
        Mode( Show( 1 ), Include( 1 ) )
    )
);
```

### [New Preset](#new-preset)[](#new-preset "Click to copy url")

**Syntax:** obj = New Preset()

**Description:** Create an anonymous preset representing the options and customizations applied to the object. This object can be passed to Apply Preset to copy the settings to another object of the same type.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
```

### [Paste Local Data Filter](#paste-local-data-filter)[](#paste-local-data-filter "Click to copy url")

**Syntax:** obj \<\< Paste Local Data Filter

**Description:** Apply the local data filter from the clipboard to the current report.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dist = Distribution( Continuous Distribution( Column( :POP ) ) );
filter = dist << Local Data Filter(
    Add Filter( columns( :Region ), Where( :Region == "MW" ) )
);
filter << Copy Local Data Filter;
dist2 = Distribution( Continuous Distribution( Column( :Lead ) ) );
Wait( 1 );
dist2 << Paste Local Data Filter;
```

### [Redo Analysis](#redo-analysis)[](#redo-analysis "Click to copy url")

**Syntax:** obj \<\< Redo Analysis

**Description:** Rerun this same analysis in a new window. The analysis will be different if the data has changed.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Relaunch Analysis;
```

### [Remove Column Switcher](#remove-column-switcher)[](#remove-column-switcher "Click to copy url")

**Syntax:** obj \<\< Remove Column Switcher

**Description:** Removes the most recent Column Switcher that has been added to the platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Contingency( Y( :size ), X( :marital status ) );
ColumnSwitcherObject = obj << Column Switcher(
    :marital status,
    {:sex, :country, :marital status}
);
Wait( 2 );
obj << Remove Column Switcher;
```

### [Remove Local Data Filter](#remove-local-data-filter)[](#remove-local-data-filter "Click to copy url")

**Syntax:** obj \<\< Remove Local Data Filter

**Description:** If a local data filter has been created, this removes it and restores the platform to use all the data in the data table directly

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dist = dt << Distribution(
    Nominal Distribution( Column( :country ) ),
    Local Data Filter(
        Add Filter( columns( :sex ), Where( :sex == "Female" ) ),
        Mode( Show( 1 ), Include( 1 ) )
    )
);
Wait( 2 );
dist << remove local data filter;
```

### [Report](#report)[](#report "Click to copy url")

**Syntax:** obj \<\< Report; Report( obj )

**Description:** Returns a reference to the report object.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Show Pareto Bars( 0 );
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Show Pareto Bars( 0 );
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Show Pareto Bars( 0 );
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Show Pareto Bars( 0 );
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Pareto Plot(
    Cause( :failure ),
    X( :clean ),
    Freq( :N ),
    Show Pareto Line( 1 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Show Pareto Bars( 0 );
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Save Script to Script Window;
```

### [SendToByGroup](#sendtobygroup)[](#sendtobygroup "Click to copy url")

**Syntax:** SendToByGroup( {":Column == level"}, command );

**Description:** Sends platform commands or display customization commands to each level of a by-group.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Distribution(
    By( :Sex ),
    SendToByGroup(
        {:sex == "F"},
        Continuous Distribution( Column( :weight ), Normal Quantile Plot( 1 ) )
    ),
    SendToByGroup( {:sex == "M"}, Continuous Distribution( Column( :weight ) ) )
);
```

### [SendToEmbeddedScriptable](#sendtoembeddedscriptable)[](#sendtoembeddedscriptable "Click to copy url")

**Syntax:** SendToEmbeddedScriptable( Dispatch( "Outline name", "Element name", command );

**Description:** SendToEmbeddedScriptable restores settings of embedded scriptable objects.

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    Censor Code( 1 ),
    <<Fit Weibull,
    SendToEmbeddedScriptable(
        Dispatch(
            {"Statistics", "Parametric Estimate - Weibull", "Profilers", "Density Profiler"},
            {1, Confidence Intervals( 0 ), Term Value( Time( 6000, Lock( 0 ), Show( 1 ) ) )}
        )
    )
);
```

### [SendToReport](#sendtoreport)[](#sendtoreport "Click to copy url")

**Syntax:** SendToReport( Dispatch( "Outline name", "Element name", Element type, command );

**Description:** Send To Report is used in tandem with the Dispatch command to customize the appearance of a report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Distribution(
    Nominal Distribution( Column( :age ) ),
    Continuous Distribution( Column( :weight ) ),
    SendToReport( Dispatch( "age", "Distrib Nom Hist", FrameBox, {Frame Size( 178, 318 )} ) )
);
```

### [Sync to Data Table Changes](#sync-to-data-table-changes)[](#sync-to-data-table-changes "Click to copy url")

**Syntax:** obj \<\< Sync to Data Table Changes

**Description:** Sync with the exclude and data changes that have been made.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dist = Distribution( Continuous Distribution( Column( :POP ) ) );
Wait( 1 );
dt << Delete Rows( dt << Get Rows Where( :Region == "W" ) );
dist << Sync To Data Table Changes;
```

### [Title](#title)[](#title "Click to copy url")

**Syntax:** obj \<\< Title( "new title" )

**Description:** Sets the title of the platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ), Show Pareto Line( 1 ) );
obj << Show Pareto Bars( 0 );
r = obj << Top Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Transform Column](#transform-column)[](#transform-column "Click to copy url")

**Syntax:** obj = \<Platform\>(... Transform Column(\<name\>, Formula(\<expression\>), \[Random Seed(\<n\>)\], \[Numeric\|Character\|Expression\], \[Continuous\|Nominal\|Ordinal\|Unstructured Text\], \[column properties\]) ...)

**Description:** Create a transform column in the local context of an object, usually a platform. The transform column is active only for the lifetime of the platform.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Distribution(
    Transform Column( "age^2", Format( "Fixed Dec", 5, 0 ), Formula( :age * :age ) ),
    Continuous Distribution( Column( :"age^2"n ) )
);
```

### [View Web XML](#view-web-xml)[](#view-web-xml "Click to copy url")

**Syntax:** obj \<\< View Web XML

**Description:** Returns the XML code that is used to create the interactive HTML report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
xml = obj << View Web XML;
```

### [Window View](#window-view)[](#window-view "Click to copy url")

**Syntax:** obj = Show Pareto Bars(...Window View( "Visible"\|"Invisible"\|"Private" )...)

**Description:** Set the type of the window to be created for the report. By default a Visible report window will be created. An Invisible window will not appear on screen, but is discoverable by functions such as Window(). A Private window responds to most window messages but is not discoverable and must be addressed through the report object

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( Window View( "Private" ), Y( :weight ), X( :height ), Fit Line );
eqn = Report( biv )["Linear Fit", Text Edit Box( 1 )] << Get Text;
biv << Close Window;
New Window( "Bivariate Equation",
    Outline Box( "Big Class Linear Fit", Text Box( eqn, <<Set Base Font( "Title" ) ) )
);
```

[ Previous](Parallel%20Plot.html "Parallel Plot") [Next ](Partial%20Least%20Squares.html "Partial Least Squares")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
