# CUSUM Control Chart

*Source: [https://jsl.jmp.com/All%20Categories/Objects/CUSUM%20Control%20Chart.html](https://jsl.jmp.com/All%20Categories/Objects/CUSUM%20Control%20Chart.html)*

---

# [CUSUM Control Chart](#cusum-control-chart)[](#cusum-control-chart "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [CUSUM Control Chart](#cusum-control-chart_1)[](#cusum-control-chart_1 "Click to copy url")

**Syntax:** CUSUM Control Chart( Y( column ), \<X( column )\>, \<By( column )\>, \<Data Units( 0\|1 )\>, \<Show Excluded Region( 0\|1 )\> )

**Description:** Creates a chart that plots the cumulative sums of deviations of subgroup means from a target. This chart is also called a tabular CUSUM chart.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
```

## [Columns](#columns)[](#columns "Click to copy url")

### [By](#by)[](#by "Click to copy url")

**Syntax:** By( column )

**Description:** Specifies the By column during launch.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Diameter.jmp" );
obj = dt << CUSUM Control Chart( Y( :DIAMETER ), X( :DAY ), By( :Phase ) );
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** X( column )

**Description:** Specifies the X column during launch.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    X( :hour ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** Y( column )

**Description:** Specifies the Y column during launch.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [ARL Profiler](#arl-profiler)[](#arl-profiler "Click to copy url")

**Syntax:** obj \<\< ARL Profiler( state=0\|1 )

**Description:** Shows or hides an interactive profiler for the Average Run Length as parameters change.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << ARL Profiler( 1 );
```

### [Alarm Script](#alarm-script)[](#alarm-script "Click to copy url")

**Syntax:** Alarm Script(Write("...")\|Speak("...")\|Mail(address, subject,"...") )

**Description:** Sends a message whenever a point on a control chart fails a given test. The message can be sent to the log, can be spoken, or can be emailed.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Alarm Script(
        Write(
            "Out of Control for test ",
            qc_test,
            " in column ",
            qc_col,
            " in sample ",
            qc_sample,
            ". \!N"
        )
    ),
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Test Beyond Limits( 1 );
```

### [Control Panel](#control-panel)[](#control-panel "Click to copy url")

**Syntax:** obj \<\< Control Panel( state=0\|1 )

**Description:** Shows or hides a report that contains the current values of the parameters and enables you to change them. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
Wait( 1 );
obj << Control Panel( 0 );
```

### [Data Units](#data-units)[](#data-units "Click to copy url")

**Syntax:** obj = CUSUM Control Chart(...Data Units( state=0\|1 )...)

**Description:** Specifies that data units are used in the report rather than standard deviation units.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 0.1 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 ),
    Data Units( 1 )
);
```

### [Get Limits](#get-limits)[](#get-limits "Click to copy url")

**Syntax:** obj \<\< Get Limits

**Description:** Imports control limits from a selected data table and replaces calculated limits on the chart.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
limitsTable = New Table( "Cusum Limits",
    Add Rows( 4 ),
    New Column( "_LimitsKey", Character, Set Values( {"_H", "_K", "_Std Dev", "_Mean"} ) ),
    New Column( "weight", Set Values( [4, 0.5, 0.01, 8.1] ) )
);
Wait();
obj << Get Limits( limitsTable );
```

### [H](#h)[](#h "Click to copy url")

**Syntax:** obj \<\< H( number=5 )

**Description:** Specifies the value of the parameter that defines the limits. If the Data Units option was not specified, this is the h parameter. If the Data Units option was specified, this is the H parameter. Note that H is equal to h times Sigma. "5" by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << H( 4.5 );
```

### [Head Start](#head-start)[](#head-start "Click to copy url")

**Syntax:** obj \<\< Head Start( number )

**Description:** Specifies the value of the cumulative sums before the first sample. Starting the cumulative sums at a nonzero value increases the sensitivity of the CUSUM chart near the beginning of the samples. This parameter is also known as the fast initial response (FIR) value. By default, this parameter is set to 0.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Head start( 1.0 );
```

### [K](#k)[](#k "Click to copy url")

**Syntax:** obj \<\< K( number=0.5 )

**Description:** Specifies the value of the parameter that defines the smallest change in the mean that is valuable to detect. If the Data Units option was not specified, this is the k parameter. If the Data Units option was specified, this is the K parameter. Note that K is equal to k times Sigma. "0.5" by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << K( 0.1 );
```

### [Lower Side](#lower-side)[](#lower-side "Click to copy url")

**Syntax:** obj \<\< Lower Side( state=0\|1 )

**Description:** Shows or hides the negative values for the cumulative sum on the chart. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Lower Side( 0 );
```

### [Parameters Report](#parameters-report)[](#parameters-report "Click to copy url")

**Syntax:** obj \<\< Parameters Report( state=0\|1 )

**Description:** Shows or hides the parameters report.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Parameters Report( 1 );
```

### [Reset to Defaults](#reset-to-defaults)[](#reset-to-defaults "Click to copy url")

**Syntax:** obj \<\< Reset to Defaults

**Description:** Resets all parameters back to the default values.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << H( 3 );
Wait( 1 );
obj << Reset to Defaults();
```

### [Save Limits](#save-limits)[](#save-limits "Click to copy url")

**Syntax:** obj \<\< Save Limits( "in Column"\|"in New Table" )

**Description:** Saves chart parameters to either a column property or a new data table.

If in Column is specified, the Avg is saved in a Control Limits column property.

If in New Table is specified, parameters h, k, the standard deviation, mean, and head start are saved to a new data table.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
Wait();
obj << Save Limits( "in Column" );
Wait();
obj << Save Limits( "in New Table" );
```

### [Save Sigma](#save-sigma)[](#save-sigma "Click to copy url")

**Syntax:** obj \<\< Save Sigma

**Description:** Saves the sigma used in the control chart as a column property in the data table.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Save Sigma;
```

### [Save Summaries](#save-summaries)[](#save-summaries "Click to copy url")

**Syntax:** obj \<\< Save Summaries

**Description:** Creates a new data table that contains statistics for each subgroup in the CUSUM chart.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Save Summaries;
```

### [Show ARL](#show-arl)[](#show-arl "Click to copy url")

**Syntax:** obj \<\< Show ARL( state=0\|1 )

**Description:** Shows or hides a report with the Average Run Length computed from the associated CUSUM chart.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Show ARL( 1 );
```

### [Show Center Line](#show-center-line)[](#show-center-line "Click to copy url")

**Syntax:** obj \<\< Show Center Line( state=0\|1 )

**Description:** Shows or hides the center line on the graph. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Show Center Line( 0 );
```

### [Show Excluded Region](#show-excluded-region)[](#show-excluded-region "Click to copy url")

**Syntax:** obj = CUSUM Control Chart(...Show Excluded Region( state=0\|1 )...)

**Description:** Specifies whether subgroups that are entirely excluded are shown on the horizontal axis in the CUSUM control chart. Applicable only when an X variable is specified.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Clips1.jmp" );
dt << Select Rows( {31, 32, 33, 34, 35, 36, 37, 38, 39, 40} ) << exclude << hide;
obj = dt << CUSUM Control Chart( Y( :Gap ), Subgroup( :Sample ), Show Excluded Region( 0 ) );
```

### [Show Limits](#show-limits)[](#show-limits "Click to copy url")

**Syntax:** obj \<\< Show Limits( state=0\|1 )

**Description:** Shows or hides the limits. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Show Limits( 0 );
```

### [Show Shift Lines](#show-shift-lines)[](#show-shift-lines "Click to copy url")

**Syntax:** obj \<\< Show Shift Lines( state=0\|1 )

**Description:** Shows or hides vertical lines that designate shifts in the chart. Shift lines are drawn at the start of a shift. Available only when there is a shift detected in the data. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
Wait( 1 );
obj << Show Shift Lines( 0 );
```

### [Sigma](#sigma)[](#sigma "Click to copy url")

**Syntax:** obj \<\< Sigma( number )

**Description:** Specifies the known value of the standard deviation. By default, this parameter is set to the average moving range of the Y column. If there is an X variable, the Sigma parameter is set to the average moving range of the summary data.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Sigma( 2 );
```

### [Target](#target)[](#target "Click to copy url")

**Syntax:** obj \<\< Target( number )

**Description:** Specifies the known value of the mean. This is the value of the center line in the chart. By default, this parameter is set to the Target value in the Spec Limits column property for the Y column. If the Y column does not have a Target value in the Spec Limits column property, this parameter is set to the overall average of the Y column.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Target( 9.5 );
```

### [Test Beyond Limits](#test-beyond-limits)[](#test-beyond-limits "Click to copy url")

**Syntax:** obj \<\< Test Beyond Limits( state=0\|1 )

**Description:** Shows or hides a red circle around any point that is above the upper limit or below the lower limit in the CUSUM chart.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Test Beyond Limits( 1 );
```

### [Tune Chart](#tune-chart)[](#tune-chart "Click to copy url")

**Syntax:** obj \<\< Tune Chart( \<0\|1\> \| Min( value, Max( value ) ) )

**Description:** Shows or hides a control that enables you to set the value of the k parameter by specifying an acceptable range for the Y variable. In a script, you can also specify the acceptable range directly.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Tune Chart( Min( 8.08, Max( 8.12 ) ) );
```

### [Upper Side](#upper-side)[](#upper-side "Click to copy url")

**Syntax:** obj \<\< Upper Side( state=0\|1 )

**Description:** Shows or hides the positive values for the cumulative sum on the chart. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Upper Side( 0 );
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
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
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

### [Copy ByGroup Script](#copy-bygroup-script)[](#copy-bygroup-script "Click to copy url")

**Syntax:** obj \<\< Copy ByGroup Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
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
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
t = obj[1] << Get ByGroup Script;
Show( t );
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
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
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
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
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
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

### [New Preset](#new-preset)[](#new-preset "Click to copy url")

**Syntax:** obj = New Preset()

**Description:** Create an anonymous preset representing the options and customizations applied to the object. This object can be passed to Apply Preset to copy the settings to another object of the same type.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
```

### [Redo Analysis](#redo-analysis)[](#redo-analysis "Click to copy url")

**Syntax:** obj \<\< Redo Analysis

**Description:** Rerun this same analysis in a new window. The analysis will be different if the data has changed.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Relaunch Analysis;
```

### [Report](#report)[](#report "Click to copy url")

**Syntax:** obj \<\< Report; Report( obj )

**Description:** Returns a reference to the report object.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
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
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
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

**Syntax:** obj = CUSUM Control Chart(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

[ Previous](Bubble%20Plot.html "Bubble Plot") [Next ](Categorical.html "Categorical")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
