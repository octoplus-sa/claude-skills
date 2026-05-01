# Explore Outliers

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Explore%20Outliers.html](https://jsl.jmp.com/All%20Categories/Objects/Explore%20Outliers.html)*

---

# [Explore Outliers](#explore-outliers)[](#explore-outliers "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Explore Outliers](#explore-outliers_1)[](#explore-outliers_1 "Click to copy url")

**Syntax:** Explore Outliers( Y( columns ) )

**Description:** Identifies, explores, and manages outliers in univariate or multivariate data.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
```

## [Columns](#columns)[](#columns "Click to copy url")

### [By](#by)[](#by "Click to copy url")

**Syntax:** obj \<\< By( column(s) )

**Description:** Performs a separate analysis for each level of the specified column.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
```

### [Label](#label)[](#label "Click to copy url")

**Syntax:** obj \<\< Label( column )

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
```

### [Validation](#validation)[](#validation "Click to copy url")

**Syntax:** obj \<\< Validation( column )

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [K Nearest Neighbor Outliers](#k-nearest-neighbor-outliers)[](#k-nearest-neighbor-outliers "Click to copy url")

**Syntax:** obj \<\< K Nearest Neighbor Outliers

**Description:** For each point, finds the distance to its kth nearest neighbor.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << k Nearest Neighbor Outliers( K( 5 ) );
```

### [Multivariate k Nearest Neighbor Outliers](#multivariate-k-nearest-neighbor-outliers)[](#multivariate-k-nearest-neighbor-outliers "Click to copy url")

**Syntax:** obj \<\< Multivariate k Nearest Neighbor Outliers

**JMP Version Added:** 14

### [Quantile Range Outliers](#quantile-range-outliers)[](#quantile-range-outliers "Click to copy url")

**Syntax:** obj \<\< Quantile Range Outliers

**Description:** Finds values more than a scale multiple of an interquantile range beyond the quantiles.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers;
```

### [Robust Fit Outliers](#robust-fit-outliers)[](#robust-fit-outliers "Click to copy url")

**Syntax:** obj \<\< Robust Fit Outliers

**Description:** Finds values more than a multiple of the scale away from the center using robust estimates of the center and scale.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers;
```

### [Robust PCA Outliers](#robust-pca-outliers)[](#robust-pca-outliers "Click to copy url")

**Syntax:** obj \<\< Robust PCA Outliers

**Description:** Robustly decomposes data into a low-rank matrix and a sparse matrix of residuals. Outliers are detected in the residuals. It can also impute missing values.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( 2 :: 10 ) );
obj << Robust PCA Outliers;
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
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
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
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
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
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
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
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
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
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
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
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
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
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
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
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
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
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
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

**Syntax:** obj = Explore Outliers(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

## [K Nearest Neighbor Outliers](#k-nearest-neighbor-outliers_1)[](#k-nearest-neighbor-outliers_1 "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Close](#close)[](#close "Click to copy url")

**Syntax:** obj \<\< Close

**JMP Version Added:** 16

#### [Exclude Selected Rows](#exclude-selected-rows)[](#exclude-selected-rows "Click to copy url")

**Syntax:** obj \<\< Exclude Selected Rows

**JMP Version Added:** 16

#### [Impute Missing](#impute-missing)[](#impute-missing "Click to copy url")

**Syntax:** obj \<\< Impute Missing( state=0 )

**Description:** If there are missing values, Robust PCA is used to impute them before analyzing with K Nearest Neighbors. On by default.

**JMP Version Added:** 16

#### [K](#k)[](#k "Click to copy url")

**Syntax:** obj \<\< K( number=8 )

**Description:** The number of near-neighbor rows to find for each row in the table. "8" by default.

**JMP Version Added:** 16

#### [Save NN Distances](#save-nn-distances)[](#save-nn-distances "Click to copy url")

**Syntax:** obj \<\< Save NN Distances

**Description:** Saves new columns to the data table containing distances to the kth nearest neighbor.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( 2 :: 10 ) );
obj << k Nearest Neighbor Outliers( K( 4 ) );
obj << Save NN Distances;
```

#### [Scatterplot Matrix](#scatterplot-matrix)[](#scatterplot-matrix "Click to copy url")

**Syntax:** obj \<\< Scatterplot Matrix

**Description:** Opens a window containing a scatterplot matrix for all columns.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( 2 :: 10 ) );
obj << k Nearest Neighbor Outliers( K( 4 ) );
obj << Scatterplot Matrix;
```

## [Multivariate Robust Outliers](#multivariate-robust-outliers)[](#multivariate-robust-outliers "Click to copy url")

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Close](#close_1)[](#close_1 "Click to copy url")

**Syntax:** obj \<\< Close

**JMP Version Added:** 16

#### [Exclude Selected Rows](#exclude-selected-rows_1)[](#exclude-selected-rows_1 "Click to copy url")

**Syntax:** obj \<\< Exclude Selected Rows

**JMP Version Added:** 16

## [Quantile Range Outliers](#quantile-range-outliers_1)[](#quantile-range-outliers_1 "Click to copy url")

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [Add Highest Nines to Missing Value Codes](#add-highest-nines-to-missing-value-codes)[](#add-highest-nines-to-missing-value-codes "Click to copy url")

**Syntax:** obj \<\< Add Highest Nines to Missing Value Codes( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments and finds the highest nines in each column. Creates a Missing Value Codes property for these values in each selected column.

``` jsl
dt = Open( "$SAMPLE_DATA/Probe.jmp" );
obj = dt << Explore Outliers(
    Y( Column Group( "Responses" ) ),
    Quantile Range Outliers( Show only columns with outliers( 1 ) )
);
obj << Add Highest Nines to Missing Value Codes( :PS_RPNBR );
dt:PS_RPNBR << Get Column Properties;
//See Log for Missing Value Codes column property
```

#### [Add to Missing Value Codes](#add-to-missing-value-codes)[](#add-to-missing-value-codes "Click to copy url")

**Syntax:** obj \<\< Add to Missing Value Codes( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments and adds a Missing Value Code property in those columns for outliers.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers;
obj << Add to Missing Value Codes( :"Q-E"n, :"ZN-E"n );
```

#### [Change Highest Nines to Missing](#change-highest-nines-to-missing)[](#change-highest-nines-to-missing "Click to copy url")

**Syntax:** obj \<\< Change Highest Nines to Missing( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments and finds the highest nines in these columns. Changes the highest nines to missing. Note that this changes the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Probe.jmp" );
obj = dt << Explore Outliers(
    Y( Column Group( "Responses" ) ),
    Quantile Range Outliers( Show only columns with outliers( 1 ) )
);
obj << Change Highest Nines to Missing( :PS_RPNBR );
```

#### [Change to Missing](#change-to-missing)[](#change-to-missing "Click to copy url")

**Syntax:** obj \<\< Change to Missing( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments. In selected columns, changes the values identified as outliers to missing values.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers( Tail Quantile( 0.3 ) );
Wait( 2 );
obj << Change to Missing( :"Q-E"n, :"ZN-E"n );
```

#### [Close](#close_2)[](#close_2 "Click to copy url")

**Syntax:** obj \<\< Close

**Description:** Removes a section of the analysis and reopens the command outline.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers;
obj << Robust Fit Outliers;
Wait( 2 );
obj << Close;
```

#### [Color Cells](#color-cells)[](#color-cells "Click to copy url")

**Syntax:** obj \<\< Color Cells( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments. In selected columns, colors the cells that correspond to outliers.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers( Tail Quantile( 0.3 ) );
obj << Color Cells( :"Q-E"n, :"ZN-E"n );
```

#### [Color Rows](#color-rows)[](#color-rows "Click to copy url")

**Syntax:** obj \<\< Color Rows( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments. In selected columns, assigns the Color row state to the rows that correspond to outliers.

**JMP Version Added:** 16

#### [Exclude Rows](#exclude-rows)[](#exclude-rows "Click to copy url")

**Syntax:** obj \<\< Exclude Rows( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments. In selected columns, excludes the rows containing values identified as outliers.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers( Tail Quantile( 0.3 ) );
obj << Exclude Rows( :"Q-E"n, :"ZN-E"n );
```

#### [Formula Columns](#formula-columns)[](#formula-columns "Click to copy url")

**Syntax:** obj \<\< Formula Columns( ALL or column1, column2, ... )

**Description:** Creates new formula columns from the selected columns by changing the outliers to missing.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers( Tail Quantile( 0.3 ) );
Wait( 2 );
obj << Formula Columns( Suffix( "Culled" ) );
```

#### [Formula Script](#formula-script)[](#formula-script "Click to copy url")

**Syntax:** obj \<\< Formula Script( ALL or column1, column2, ... )

**Description:** Creates a script to make new formula columns from the selected columns by changing the outliers to missing.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers( Tail Quantile( 0.3 ) );
Wait( 2 );
obj << Formula Script( Suffix( "Culled" ) );
```

#### [Get Quantile Outliers](#get-quantile-outliers)[](#get-quantile-outliers "Click to copy url")

**Syntax:** obj \<\< Get Quantile Outliers

**Description:** Returns a list containing a list of the columns that contain outliers and a list of vectors that contain outlier values in those columns.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers;
obj << Get Quantile Outliers;
```

#### [Q](#q)[](#q "Click to copy url")

**Syntax:** obj \<\< Q( number=3 )

**Description:** Sets the scale multiple, Q, for the interquantile distance. Values that fall more than Q times the interquantile distance beyond the tail quantiles are considered outliers. Use Rescan to apply the setting. "3" by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers( Q( 4 ) );
```

#### [Rescan](#rescan)[](#rescan "Click to copy url")

**Syntax:** obj \<\< Rescan

**Description:** Use after changing settings to recompute the criteria and rescan the data to obtain outliers.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers;
obj << Tail Quantile( 0.2 );
obj << Rescan;
```

#### [Restrict search to integers](#restrict-search-to-integers)[](#restrict-search-to-integers "Click to copy url")

**Syntax:** obj \<\< Restrict search to integers( state=0\|1 )

**Description:** Restricts outlier values to only integer values. This setting limits the search for outliers in order to find industry-specific missing value codes and error codes. Available for the Quantile Range Outliers and Robust Fit Outliers methods. Off by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    Quantile Range Outliers( Restrict search to integers( 1 ) )
);
```

#### [Save Quantile Outlier Limits](#save-quantile-outlier-limits)[](#save-quantile-outlier-limits "Click to copy url")

**Syntax:** obj \<\< Save Quantile Outlier Limits

**Description:** Opens a new data table containing the Quantile Range Outliers report information and a column of outlier values.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers;
obj << Save Quantile Outlier Limits;
```

#### [Select Rows](#select-rows)[](#select-rows "Click to copy url")

**Syntax:** obj \<\< Select Rows( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments and selects the rows that have outlying values in any of those columns.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers( Tail Quantile( 0.3 ) );
obj << Select Rows( :"Q-E"n, :"ZN-E"n );
```

#### [Show only columns with outliers](#show-only-columns-with-outliers)[](#show-only-columns-with-outliers "Click to copy url")

**Syntax:** obj \<\< Show only columns with outliers( state=0\|1 )

**Description:** Limits the list of columns in the report to those that contain outliers. Available for the Quantile Range Outliers and Robust Fit Outliers methods. Off by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    Quantile Range Outliers( Show only columns with outliers( 1 ) )
);
```

#### [Tail Quantile](#tail-quantile)[](#tail-quantile "Click to copy url")

**Syntax:** obj \<\< Tail Quantile( number=.10 )

**Description:** Sets the quantile value for each tail. The quantiles are used in computing the interquantile distance. Use Rescan to apply the setting. ".10" by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Quantile Range Outliers( Tail Quantile( 0.2 ) );
```

## [Robust Fit Outliers](#robust-fit-outliers_1)[](#robust-fit-outliers_1 "Click to copy url")

### [Item Messages](#item-messages_4)[](#item-messages_4 "Click to copy url")

#### [Add to Missing Value Codes](#add-to-missing-value-codes_1)[](#add-to-missing-value-codes_1 "Click to copy url")

**Syntax:** obj \<\< Add to Missing Value Codes( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments and adds a Missing Value Code property in those columns for outliers.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers( K Sigma( 2 ) );
obj << Add to Missing Value Codes( :"Q-E"n, :"ZN-E"n );
```

#### [Cauchy](#cauchy)[](#cauchy "Click to copy url")

**Syntax:** obj \<\< Cauchy( state=0\|1 )

**Description:** Uses a Cauchy distribution to estimate the robust center and scale of the values. The robust center and scale are used to determine outliers.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers;
obj << Cauchy( 1 );
obj << Rescan;
```

#### [Change to Missing](#change-to-missing_1)[](#change-to-missing_1 "Click to copy url")

**Syntax:** obj \<\< Change to Missing( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments. In selected columns, changes the values identified as outliers to missing values.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers( K Sigma( 2 ) );
Wait( 2 );
obj << Change to Missing( :"Q-E"n, :"ZN-E"n );
```

#### [Close](#close_3)[](#close_3 "Click to copy url")

**Syntax:** obj \<\< Close

**Description:** Removes a section of the analysis and reopens the command outline.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers;
Wait( 2 );
obj << Close;
```

#### [Color Cells](#color-cells_1)[](#color-cells_1 "Click to copy url")

**Syntax:** obj \<\< Color Cells( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments. In selected columns, colors the cells that correspond to outliers.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers( K Sigma( 2 ) );
obj << Color Cells( :"Q-E"n, :"ZN-E"n );
```

#### [Color Rows](#color-rows_1)[](#color-rows_1 "Click to copy url")

**Syntax:** obj \<\< Color Rows( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments. In selected columns, assigns the Color row state to the rows that correspond to outliers.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
dt << Clear Row States;
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers( K Sigma( 2 ) );
obj << Color Rows( :"Q-E"n, :"ZN-E"n );
```

#### [Exclude Rows](#exclude-rows_1)[](#exclude-rows_1 "Click to copy url")

**Syntax:** obj \<\< Exclude Rows( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments. In selected columns, excludes the rows containing values identified as outliers.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers( K Sigma( 2 ) );
obj << Exclude Rows( :"Q-E"n, :"ZN-E"n );
```

#### [Formula Columns](#formula-columns_1)[](#formula-columns_1 "Click to copy url")

**Syntax:** obj \<\< Formula Columns( ALL or column1, column2, ... )

**Description:** Creates new formula columns from the selected columns by changing the outliers to missing.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers( K Sigma( 2 ) );
Wait( 2 );
obj << Formula Columns( Suffix( "Culled" ) );
```

#### [Formula Script](#formula-script_1)[](#formula-script_1 "Click to copy url")

**Syntax:** obj \<\< Formula Script( ALL or column1, column2, ... )

**Description:** Creates a script to make new formula columns from the selected columns by changing the outliers to missing.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers( K Sigma( 2 ) );
Wait( 2 );
obj << Formula Script( Suffix( "Culled" ) );
```

#### [Huber](#huber)[](#huber "Click to copy url")

**Syntax:** obj \<\< Huber( state=0\|1 )

**Description:** Uses Huber estimation to estimate the robust center and scale of the values. The robust center and scale are used to determine outliers.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers;
obj << Huber( 1 );
obj << Rescan;
```

#### [K Sigma](#k-sigma)[](#k-sigma "Click to copy url")

**Syntax:** obj \<\< K Sigma( number=4 )

**Description:** Sets the K Sigma value where outliers are defined to be K times the robust scale values away from the robust center. "4" by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers;
obj << K Sigma( 3 );
obj << Rescan;
```

#### [Quartile](#quartile)[](#quartile "Click to copy url")

**Syntax:** obj \<\< Quartile( state=0\|1 )

**Description:** Uses the median to estimate the robust center and the interquartile range divided by 1.349 to estimate the robust scale. The robust center and scale are used to determine outliers.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers;
obj << Quartile( 1 );
obj << Rescan;
```

#### [Rescan](#rescan_1)[](#rescan_1 "Click to copy url")

**Syntax:** obj \<\< Rescan

**Description:** Use after changing settings to recompute the criteria and rescan the data to obtain outliers.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers;
obj << K Sigma( 2.5 );
obj << Rescan;
```

#### [Save Robust Outlier Limits](#save-robust-outlier-limits)[](#save-robust-outlier-limits "Click to copy url")

**Syntax:** obj \<\< Save Robust Outlier Limits

**Description:** Opens a new data table that contains information from the Robust Estimates and Outliers report.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers;
obj << Save Robust Outlier Limits;
```

#### [Select Rows](#select-rows_1)[](#select-rows_1 "Click to copy url")

**Syntax:** obj \<\< Select Rows( ALL or column1, column2, ... )

**Description:** Selects the columns listed as arguments and selects the rows that have outlying values in any of those columns.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
obj << Robust Fit Outliers( K Sigma( 2 ) );
obj << Select Rows( :"Q-E"n, :"ZN-E"n );
```

## [Robust PCA Outliers](#robust-pca-outliers_1)[](#robust-pca-outliers_1 "Click to copy url")

### [Item Messages](#item-messages_5)[](#item-messages_5 "Click to copy url")

#### [Center](#center)[](#center "Click to copy url")

**Syntax:** obj \<\< Center( state=1 )

**Description:** Specifies whether to center the data by the median before the analysis. On by default.

**JMP Version Added:** 16

#### [Close](#close_4)[](#close_4 "Click to copy url")

**Syntax:** obj \<\< Close

**Description:** Removes the RPCA analysis from the platform report.

**JMP Version Added:** 16

#### [Lambda](#lambda)[](#lambda "Click to copy url")

**Syntax:** obj \<\< Lambda( number )

**Description:** Robust PCA tuning with lower values making it more sensitive to declaring outliers. Default Lambda=2/sqrt(max(nRow,nCol))

**JMP Version Added:** 16

#### [MaxIt](#maxit)[](#maxit "Click to copy url")

**Syntax:** obj \<\< MaxIt( number )

**Description:** The maximum number of SVD iterations allowed before failing to converge.

**JMP Version Added:** 16

#### [Outlier Threshold](#outlier-threshold)[](#outlier-threshold "Click to copy url")

**Syntax:** obj \<\< Outlier Threshold( number=2 )

**Description:** Specifies that any scaled residual larger in absolute value than this threshold is shown as it is shown in the outlier report. "2" by default.

**JMP Version Added:** 16

#### [Randomized SVD Dim](#randomized-svd-dim)[](#randomized-svd-dim "Click to copy url")

**Syntax:** obj \<\< Randomized SVD Dim( state=0\|1 )

**Description:** Specifies the number of dimensions in the randomized SVD to which to reduce the wide problem.

**JMP Version Added:** 17

#### [Save Cleaned](#save-cleaned)[](#save-cleaned "Click to copy url")

**Syntax:** obj \<\< Save Cleaned( Trim(\<threshold\>),Impute(\<threshold\>),Make Missing(\<threshold\>),Color Impute(0\|1)--if none specified it will prompt with dialog )

**Description:** Creates a new set of columns that contain missing values imputed and outliers modified. Trim(arg) finds scaled residuals greater than arg and changes the scaled residuals in the corresponding cells to the signed arg. Impute(arg) finds scaled residuals greater than arg and changes the scaled residuals in the corresponding cells to the low-rank approximation. Make Missing(value) finds any scaled residual greater than arg and changes scaled residuals in the corresponding cells to missing.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    Robust PCA Outliers
);
obj << Save Cleaned( Trim( 25 ), Impute( 50 ), Make Missing( 100 ) );
```

#### [Save Large Outliers](#save-large-outliers)[](#save-large-outliers "Click to copy url")

**Syntax:** obj \<\< Save Large Outliers

**Description:** Creates a new data table that contains the outliers in the report.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    Robust PCA Outliers
);
obj << Save Large Outliers;
```

#### [Save Low Rank Approx](#save-low-rank-approx)[](#save-low-rank-approx "Click to copy url")

**Syntax:** obj \<\< Save Low Rank Approx

**Description:** Creates a new set of columns that contain the low-rank approximation, which is obtained from the singular value decomposition.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    Robust PCA Outliers
);
obj << Save Low Rank Approx;
```

#### [Save Residuals](#save-residuals)[](#save-residuals "Click to copy url")

**Syntax:** obj \<\< Save Residuals

**Description:** Creates a new set of columns that contain the residuals, which are the observations minus the low-rank approximation.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    Robust PCA Outliers
);
obj << Save Residuals;
```

#### [Save Scaled Residuals](#save-scaled-residuals)[](#save-scaled-residuals "Click to copy url")

**Syntax:** obj \<\< Save Scaled Residuals

**Description:** Creates a new set of columns that contain the scaled residuals, which are the scaled observations minus the low-rank approximation.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers(
    Y( Column Group( "Sensor Measurements" ) ),
    Robust PCA Outliers
);
obj << Save Scaled Residuals;
```

#### [Scale](#scale)[](#scale "Click to copy url")

**Syntax:** obj \<\< Scale( state=1 )

**Description:** Specifies whether to scale the data by an interquantile range analog to the standard deviation before the analysis. On by default.

**JMP Version Added:** 16

#### [Tolerance](#tolerance)[](#tolerance "Click to copy url")

**Syntax:** obj \<\< Tolerance( number )

**Description:** Specifies the convergence criterion, which determines when to stop the algorithm. The default convergence criterion values are set based on the number of columns specified in the launch.

**JMP Version Added:** 16

#### [Use Randomized SVD](#use-randomized-svd)[](#use-randomized-svd "Click to copy url")

**Syntax:** obj \<\< Use Randomized SVD( state=0\|1 )

**Description:** Reduces the dimensionality using the randomized SVD. This approach can speed up computations for very wide problems.

**JMP Version Added:** 17

[ Previous](Explore%20Missing%20Values.html "Explore Missing Values") [Next ](Explore%20Patterns.html "Explore Patterns")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
