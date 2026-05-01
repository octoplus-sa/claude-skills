# Fit Group

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Fit%20Group.html](https://jsl.jmp.com/All%20Categories/Objects/Fit%20Group.html)*

---

# [Fit Group](#fit-group)[](#fit-group "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Fit Group](#fit-group_1)[](#fit-group_1 "Click to copy url")

**Syntax:** Fit Group( model1, model2, ... ); Fit Group( model1; model2; ... )

**Description:** Groups separate least squares, nonlinear, neural, gaussian processing, and mixed model fits in the same output window with a shared profiler.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Arrange in Rows](#arrange-in-rows)[](#arrange-in-rows "Click to copy url")

**Syntax:** obj \<\< Arrange in Rows( number )

**Description:** Rearranges the reports for the platform analyses in a specified number of rows.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
Wait( 1 );
obj << Arrange in Rows( 2 );
```

### [Contour Profiler](#contour-profiler)[](#contour-profiler "Click to copy url")

**Syntax:** obj \<\< Contour Profiler( state=0\|1 )

**Description:** Shows or hides a contour profiler for all responses. You can explore the effects of model terms on all responses simultaneously.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Contour Profiler( 1 );
```

### [Order by Goodness of Fit](#order-by-goodness-of-fit)[](#order-by-goodness-of-fit "Click to copy url")

**Syntax:** obj \<\< Order by Goodness of Fit

**Description:** Sorts the reports by significance of fit, where significance is measured by the R-square statistic for each model. This option is applicable only for platforms that surface the R-square statistic to the platform level.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Bivariate( Y( :HARDNESS ), X( :SILICA, :SILANE, :SULFUR ), Fit Line( 1 ) ),
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    )
);
Wait( 1 );
obj << Order by Goodness of Fit;
```

### [Profiler](#profiler)[](#profiler "Click to copy url")

**Syntax:** obj \<\< Profiler( state=0\|1 )

**Description:** Shows or hides a prediction profiler for all responses. You can view the effects of model terms on all responses simultaneously. You can also perform multiple optimizations across the responses.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Profiler( 1 );
```

### [Surface Profiler](#surface-profiler)[](#surface-profiler "Click to copy url")

**Syntax:** obj \<\< Surface Profiler( state=0\|1 )

**Description:** Shows or hides separate surface profiler reports for each response.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Surface Profiler( 1 );
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
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Automatic Recalc( 1 );
dt << Select Rows( 5 ) << Exclude( 1 );
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

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
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

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
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
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
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
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
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
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Report View( "Summary" );
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
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
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Fit Group(
    Fit Model(
        Y( :ABRASION ),
        Effects(
            :SILICA & RS, :SILANE & RS, :SULFUR & RS, :SILICA * :SILICA, :SILICA * :SILANE,
            :SILANE * :SILANE, :SILICA * :SULFUR, :SILANE * :SULFUR, :SULFUR * :SULFUR
        ),
        Personality( "Standard Least Squares" ),
        Emphasis( "Minimal Report" ),
        Run
    ),
    Gaussian Process(
        Y( :HARDNESS ),
        X( :SILICA, :SILANE, :SULFUR ),
        Set Correlation Function( "Cubic" )
    )
);
r = obj << Top Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [View Web XML](#view-web-xml)[](#view-web-xml "Click to copy url")

**Syntax:** obj \<\< View Web XML

**Description:** Returns the XML code that is used to create the interactive HTML report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
xml = obj << View Web XML;
```

[ Previous](Fit%20Group%20Orthogonal%20Supersaturated.html "Fit Group Orthogonal Supersaturated") [Next ](Fit%20Life%20by%20X.html "Fit Life by X")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
