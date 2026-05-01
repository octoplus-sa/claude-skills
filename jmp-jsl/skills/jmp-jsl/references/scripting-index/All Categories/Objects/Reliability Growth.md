# Reliability Growth

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Reliability%20Growth.html](https://jsl.jmp.com/All%20Categories/Objects/Reliability%20Growth.html)*

---

# [Reliability Growth](#reliability-growth)[](#reliability-growth "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Reliability Growth](#reliability-growth_1)[](#reliability-growth_1 "Click to copy url")

**Syntax:** obj = Reliability Growth( Input Format( Time to Event ), Time to Event( column, \<column\> ), \<Event Count( column )\>, \<Phase( column )\> ); obj = Reliability Growth( Input Format( Dates ), Timestamp( column, \<column\> ), \<Event Count( column )\>, \<Phase( column )\> ); obj = Reliability Growth( Input Format( Concurrent Systems ), Time to Event( column, column, ... ), System ID( column ), \<Phase( column )\> ) obj = Reliability Growth( Input Format( Parallel Systems ), Time to Event( column, column, ... ), \<Event Count( column )\>, System ID( column ), \<Phase( column )\> )

**Description:** Models the change in reliability of a single repairable system over time as improvements are incorporated into its design. The platform accepts several input formats. See each format for specification details.

#### [Concurrent Systems](#concurrent-systems)[](#concurrent-systems "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Concurrent Systems.jmp" );
obj = dt << Reliability Growth(
    Input Format( Concurrent Systems ),
    Time to Event( :Prototype 1, :Prototype 2 ),
    System ID( :Failed System ),

);
obj << Crow AMSAA;
```

#### [Dates](#dates)[](#dates "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/BrakeReliability.jmp" );
obj = dt << Reliability Growth(
    Input Format( Dates ),
    Timestamp( :Date ),
    Event Count( :Fixes )
);
```

#### [Parallel Systems](#parallel-systems)[](#parallel-systems "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Parallel Systems Multiple Phases.jmp" );
obj = dt << Reliability Growth(
    Input Format( Parallel Systems ),
    Time to Event( :Hours ),
    Event Count( :Fixes ),
    System ID( :System ID ),
    Phase( :Phase )
);
obj << Piecewise Weibull NHPP with Different Intercepts;
```

#### [Time to Event](#time-to-event)[](#time-to-event "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Crow AMSAA](#crow-amsaa)[](#crow-amsaa "Click to copy url")

**Syntax:** obj \<\< Crow AMSAA

**Description:** Fits a Crow-AMSAA model. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
```

### [Crow AMSAA with Modified MLE](#crow-amsaa-with-modified-mle)[](#crow-amsaa-with-modified-mle "Click to copy url")

**Syntax:** obj \<\< Crow AMSAA with Modified MLE

**Description:** Fits a Crow-AMSAA model with bias correction for beta. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA with Modified MLE;
```

### [Distinct Phase Weibull NHPP](#distinct-phase-weibull-nhpp)[](#distinct-phase-weibull-nhpp "Click to copy url")

**Syntax:** obj \<\< Distinct Phase Weibull NHPP

**Description:** Fits a Distinct Phase Weibull NHPP model, where each system in a multi-phase study follows the same Crow-AMSAA model in each phase. This model contains one beta parameter and one lambda parameter for each phase. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Parallel Systems Different Intercepts.jmp" );
obj = dt << Reliability Growth(
    Input Format( Parallel Systems ),
    Time to Event( :Hours ),
    Event Count( :Fixes ),
    System ID( :System ID ),
    Phase( :Phase )
);
obj << Distinct Phase Weibull NHPP;
```

### [Distinct System Weibull NHPP](#distinct-system-weibull-nhpp)[](#distinct-system-weibull-nhpp "Click to copy url")

**Syntax:** obj \<\< Distinct System Weibull NHPP

**Description:** Fits a Distinct System Weibull NHPP model, where each system in the study follows a separate Crow-AMSAA model with different parameters. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Parallel Systems One Phase.jmp" );
obj = dt << Reliability Growth(
    Input Format( Parallel Systems ),
    Time to Event( :Hours ),
    Event Count( :Repairs ),
    System ID( :System ID )
);
obj << Distinct System Weibull NHPP;
```

### [Distinct Weibull NHPP](#distinct-weibull-nhpp)[](#distinct-weibull-nhpp "Click to copy url")

**Syntax:** obj \<\< Distinct Weibull NHPP

**Description:** Fits a Distinct Weibull NHPP model, where each system in a multi-phase study follows a separate Crow-AMSAA model in each phase. This model contains one beta parameter and one lambda parameter for each combination of system and phase in the study. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Parallel Systems Different Intercepts.jmp" );
obj = dt << Reliability Growth(
    Input Format( Parallel Systems ),
    Time to Event( :Hours ),
    Event Count( :Fixes ),
    System ID( :System ID ),
    Phase( :Phase )
);
obj << Distinct Weibull NHPP;
```

### [Fixed Parameter Crow AMSAA](#fixed-parameter-crow-amsaa)[](#fixed-parameter-crow-amsaa "Click to copy url")

**Syntax:** obj \<\< Fixed Parameter Crow AMSAA( \<lambda ( number )\>, \<beta ( number )\> )

**Description:** Fits a Fixed Parameter Crow-AMSAA model. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Fixed Parameter Crow AMSAA( lambda( .02 ) );
```

### [Get Results](#get-results)[](#get-results "Click to copy url")

**Syntax:** obj \<\< Get Results

**Description:** Returns a named list that contains the model estimation results.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
Show( obj << Get Results );
```

### [Identical System Weibull NHPP](#identical-system-weibull-nhpp)[](#identical-system-weibull-nhpp "Click to copy url")

**Syntax:** obj \<\< Identical System Weibull NHPP

**Description:** Fits an Identical System Weibull NHPP model, where each system in the study follows a single Crow-AMSAA model. The differences among the systems are assumed to be due to the randomness of individual realizations of the same model. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Parallel Systems One Phase.jmp" );
obj = dt << Reliability Growth(
    Input Format( Parallel Systems ),
    Time to Event( :Hours ),
    Event Count( :Repairs ),
    System ID( :System ID )
);
obj << Identical System Weibull NHPP;
```

### [Piecewise Weibull NHPP](#piecewise-weibull-nhpp)[](#piecewise-weibull-nhpp "Click to copy url")

**Syntax:** obj \<\< Piecewise Weibull NHPP

**Description:** Fits a Piecewise Weibull NHPP model. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/TurbineEngineDesign1.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Day ),
    Event Count( :Fixes ),
    Phase( :Design Phase )
);
obj << Piecewise Weibull NHPP;
```

### [Piecewise Weibull NHPP Change Point Detection](#piecewise-weibull-nhpp-change-point-detection)[](#piecewise-weibull-nhpp-change-point-detection "Click to copy url")

**Syntax:** obj \<\< Piecewise Weibull NHPP Change Point Detection

**Description:** Estimates a change point in the data and fits a Piecewise Weibull NHPP model. This option is not available when a Phase variable is specified. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/BrakeReliability.jmp" );
obj = dt << Reliability Growth(
    Input Format( Dates ),
    Timestamp( :Date ),
    Event Count( :Fixes )
);
obj << Piecewise Weibull NHPP Change Point Detection;
```

### [Piecewise Weibull NHPP with Different Intercepts](#piecewise-weibull-nhpp-with-different-intercepts)[](#piecewise-weibull-nhpp-with-different-intercepts "Click to copy url")

**Syntax:** obj \<\< Piecewise Weibull NHPP with Different Intercepts

**Description:** Fits a Piecewise Weibull NHPP with Different Intercepts model, where each system in a multi-phase study follows a separate piecewise Weibull NHPP model. This model contains one beta parameter for each phase and one lambda parameter for each system. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Parallel Systems Multiple Phases.jmp" );
obj = dt << Reliability Growth(
    Input Format( Parallel Systems ),
    Time to Event( :Hours ),
    Event Count( :Fixes ),
    System ID( :System ID ),
    Phase( :Phase )
);
obj << Piecewise Weibull NHPP with Different Intercepts;
```

### [Reinitialized Weibull NHPP](#reinitialized-weibull-nhpp)[](#reinitialized-weibull-nhpp "Click to copy url")

**Syntax:** obj \<\< Reinitialized Weibull NHPP

**Description:** Fits a Reinitialized Weibull NHPP model. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/ProductionEquipment.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Hours of Operation ),
    Event Count( :Fixes ),
    Phase( :Design Stage )
);
obj << Reinitialized Weibull NHPP;
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
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
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
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
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
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
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
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
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
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
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
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
obj << Report View( "Summary" );
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Hours ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Crow AMSAA;
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Hours ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj << Crow AMSAA;
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
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
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
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

## [Crow AMSAA](#crow-amsaa_1)[](#crow-amsaa_1 "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Achieved MTBF](#achieved-mtbf)[](#achieved-mtbf "Click to copy url")

**Syntax:** scrobj \<\< Achieved MTBF( state=0\|1 )

**Description:** Shows or hides the Achieved MTBF report. Use the optional alpha argument to specify alpha.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Achieved MTBF( .01 );
```

#### [Goodness of Fit](#goodness-of-fit)[](#goodness-of-fit "Click to copy url")

**Syntax:** scrobj \<\< Goodness of Fit( state=0\|1 )

**Description:** Shows or hides the Goodness of Fit report that contains a test of the null hypothesis that the data follow a Crow-AMSAA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Goodness of Fit( 1 );
```

#### [Show Cumulative Events Plot](#show-cumulative-events-plot)[](#show-cumulative-events-plot "Click to copy url")

**Syntax:** scrobj \<\< Show Cumulative Events Plot( state=0\|1 )

**Description:** Shows or hides the Cumulative Events plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show Cumulative Events Plot( 1 );
```

#### [Show Intensity Plot](#show-intensity-plot)[](#show-intensity-plot "Click to copy url")

**Syntax:** scrobj \<\< Show Intensity Plot( state=0\|1 )

**Description:** Shows or hides the Intensity plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show Intensity Plot( 1 );
```

#### [Show MTBF Plot](#show-mtbf-plot)[](#show-mtbf-plot "Click to copy url")

**Syntax:** scrobj \<\< Show MTBF Plot( state=0\|1 )

**Description:** Shows or hides the mean time between failures (MTBF) plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show MTBF Plot( 0 );
```

#### [Show Profilers](#show-profilers)[](#show-profilers "Click to copy url")

**Syntax:** scrobj \<\< Show Profilers( state=0\|1 )

**Description:** Shows or hides the profilers for mean time between failures (MTBF), failure intensity, and cumulative events.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show Profilers( 1 );
```

## [Cumulative Events Plot](#cumulative-events-plot)[](#cumulative-events-plot "Click to copy url")

### [Associated Constructors](#associated-constructors_1)[](#associated-constructors_1 "Click to copy url")

#### [Cumulative Events Plot](#cumulative-events-plot_1)[](#cumulative-events-plot_1 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( ... ); scrobj = obj \<\< Cumulative Events Plot

**Description:** Enables you to show or hide models in the Cumulative Events plot. If specified without an argument, this option returns a scriptable reference to the plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
plot = obj << Cumulative Events Plot;
plot << Crow AMSAA( 0 );
```

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Crow AMSAA](#crow-amsaa_2)[](#crow-amsaa_2 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Crow AMSAA( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Crow AMSAA( state=0\|1 ) ); scrobj \<\< Crow AMSAA( state=0\|1 ) )

**Description:** Shows or hides the Crow-AMSAA model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Crow AMSAA;
Wait( 1 );
obj << Cumulative Events Plot( Crow AMSAA( 0 ) );
obj << Mean Time Between Failures Plot( Crow AMSAA( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Crow AMSAA;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Crow AMSAA( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Crow AMSAA( 0 );
```

#### [Crow AMSAA with Modified MLE](#crow-amsaa-with-modified-mle_1)[](#crow-amsaa-with-modified-mle_1 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Crow AMSAA with Modified MLE( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Crow AMSAA with Modified MLE( state=0\|1 ) ); scrobj \<\< Crow AMSAA with Modified MLE( state=0\|1 ) )

**Description:** Shows or hides the Crow-AMSAA model with bias correction for beta in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Crow AMSAA with Modified MLE;
Wait( 1 );
obj << Cumulative Events Plot( Crow AMSAA with Modified MLE( 0 ) );
obj << Mean Time Between Failures Plot( Crow AMSAA with Modified MLE( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Crow AMSAA with Modified MLE;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Crow AMSAA with Modified MLE( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Crow AMSAA with Modified MLE( 0 );
```

#### [Fixed Parameter Crow AMSAA](#fixed-parameter-crow-amsaa_1)[](#fixed-parameter-crow-amsaa_1 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Fixed Parameter Crow AMSAA( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Fixed Parameter Crow AMSAA( state=0\|1 ) ); scrobj \<\< Fixed Parameter Crow AMSAA( state=0\|1 ) )

**Description:** Shows or hides the Fixed Parameter Crow-AMSAA model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Fixed Parameter Crow AMSAA;
Wait( 1 );
obj << Cumulative Events Plot( Fixed Parameter Crow AMSAA( 0 ) );
obj << Mean Time Between Failures Plot( Fixed Parameter Crow AMSAA( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Fixed Parameter Crow AMSAA;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Fixed Parameter Crow AMSAA( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Fixed Parameter Crow AMSAA( 0 );
```

#### [Piecewise Weibull NHPP](#piecewise-weibull-nhpp_1)[](#piecewise-weibull-nhpp_1 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Piecewise Weibull NHPP( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Piecewise Weibull NHPP( state=0\|1 ) ); scrobj \<\< Piecewise Weibull NHPP( state=0\|1 ) )

**Description:** Shows or hides the Piecewise Weibull NHPP model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/TurbineEngineDesign1.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Day ),
    Event Count( :Fixes ),
    Phase( :Design Phase )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Piecewise Weibull NHPP;
Wait( 1 );
obj << Cumulative Events Plot( Piecewise Weibull NHPP( 0 ) );
obj << Mean Time Between Failures Plot( Piecewise Weibull NHPP( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/TurbineEngineDesign1.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Day ),
    Event Count( :Fixes ),
    Phase( :Design Phase )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Piecewise Weibull NHPP;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Piecewise Weibull NHPP( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Piecewise Weibull NHPP( 0 );
```

#### [Piecewise Weibull NHPP Change Point Detection](#piecewise-weibull-nhpp-change-point-detection_1)[](#piecewise-weibull-nhpp-change-point-detection_1 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Piecewise Weibull NHPP Change Point Detection( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Piecewise Weibull NHPP Change Point Detection( state=0\|1 ) ); scrobj \<\< Piecewise Weibull NHPP Change Point Detection( state=0\|1 ) )

**Description:** Shows or hides the Reinitialized Weibull NHPP model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/BrakeReliability.jmp" );
obj = dt << Reliability Growth(
    Input Format( Dates ),
    Timestamp( :Date ),
    Event Count( :Fixes )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Piecewise Weibull NHPP Change Point Detection;
Wait( 1 );
obj << Cumulative Events Plot( Piecewise Weibull NHPP Change Point Detection( 0 ) );
obj << Mean Time Between Failures Plot( Piecewise Weibull NHPP Change Point Detection( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/BrakeReliability.jmp" );
obj = dt << Reliability Growth(
    Input Format( Dates ),
    Timestamp( :Date ),
    Event Count( :Fixes )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Piecewise Weibull NHPP Change Point Detection;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Piecewise Weibull NHPP Change Point Detection( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Piecewise Weibull NHPP Change Point Detection( 0 );
```

#### [Reinitialized Weibull NHPP](#reinitialized-weibull-nhpp_1)[](#reinitialized-weibull-nhpp_1 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Reinitialized Weibull NHPP( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Reinitialized Weibull NHPP( state=0\|1 ) ); scrobj \<\< Reinitialized Weibull NHPP( state=0\|1 ) )

**Description:** Shows or hides the Reinitialized Weibull NHPP model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/ProductionEquipment.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Hours of Operation ),
    Event Count( :Fixes ),
    Phase( :Design Stage )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Reinitialized Weibull NHPP;
Wait( 1 );
obj << Cumulative Events Plot( Reinitialized Weibull NHPP( 0 ) );
obj << Mean Time Between Failures Plot( Reinitialized Weibull NHPP( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/ProductionEquipment.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Hours of Operation ),
    Event Count( :Fixes ),
    Phase( :Design Stage )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Reinitialized Weibull NHPP;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Reinitialized Weibull NHPP( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Reinitialized Weibull NHPP( 0 );
```

## [Fixed Parameter Crow AMSAA](#fixed-parameter-crow-amsaa_2)[](#fixed-parameter-crow-amsaa_2 "Click to copy url")

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [Show Cumulative Events Plot](#show-cumulative-events-plot_1)[](#show-cumulative-events-plot_1 "Click to copy url")

**Syntax:** scrobj \<\< Show Cumulative Events Plot( state=0\|1 )

**Description:** Shows or hides the Cumulative Events plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show Cumulative Events Plot( 1 );
```

#### [Show Intensity Plot](#show-intensity-plot_1)[](#show-intensity-plot_1 "Click to copy url")

**Syntax:** scrobj \<\< Show Intensity Plot( state=0\|1 )

**Description:** Shows or hides the Intensity plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show Intensity Plot( 1 );
```

#### [Show MTBF Plot](#show-mtbf-plot_1)[](#show-mtbf-plot_1 "Click to copy url")

**Syntax:** scrobj \<\< Show MTBF Plot( state=0\|1 )

**Description:** Shows or hides the mean time between failures (MTBF) plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show MTBF Plot( 0 );
```

#### [Show Profilers](#show-profilers_1)[](#show-profilers_1 "Click to copy url")

**Syntax:** scrobj \<\< Show Profilers( state=0\|1 )

**Description:** Shows or hides the profilers for mean time between failures (MTBF), failure intensity, and cumulative events.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show Profilers( 1 );
```

#### [beta](#beta)[](#beta "Click to copy url")

**Syntax:** obj \<\< Fixed Parameter Crow AMSAA( beta( number ) )

**Description:** Specifies the value of the fixed beta parameter. If the argument is a missing value, then the parameter is not fixed.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
obj << Fixed Parameter Crow AMSAA( Beta( 0.8 ) );
Report( obj )["Crow-AMSAA"] << Close( 1 );
```

#### [lambda](#lambda)[](#lambda "Click to copy url")

**Syntax:** obj \<\< Fixed Parameter Crow AMSAA( lambda( number ) )

**Description:** Specifies the value of the fixed lambda parameter. If the argument is a missing value, then the parameter is not fixed.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
obj << Fixed Parameter Crow AMSAA( lambda( 0.02 ) );
Report( obj )["Crow-AMSAA"] << Close( 1 );
```

## [Mean Time Between Failures Plot](#mean-time-between-failures-plot)[](#mean-time-between-failures-plot "Click to copy url")

### [Associated Constructors](#associated-constructors_2)[](#associated-constructors_2 "Click to copy url")

#### [Mean Time Between Failures Plot](#mean-time-between-failures-plot_1)[](#mean-time-between-failures-plot_1 "Click to copy url")

**Syntax:** obj \<\< Mean Time Between Failures Plot( ... ); scrobj = obj \<\< Mean Time Between Failures Plot

**Description:** Enables you to show or hide models in the Mean Time Between Failures plot. If specified without an argument, this option returns a scriptable reference to the plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Crow AMSAA;
Report( obj )["Mean Time Between Failures"] << Close( 0 );
plot = obj << Mean Time Between Failures Plot;
plot << Crow AMSAA( 0 );
```

### [Item Messages](#item-messages_4)[](#item-messages_4 "Click to copy url")

#### [Crow AMSAA](#crow-amsaa_3)[](#crow-amsaa_3 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Crow AMSAA( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Crow AMSAA( state=0\|1 ) ); scrobj \<\< Crow AMSAA( state=0\|1 ) )

**Description:** Shows or hides the Crow-AMSAA model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Crow AMSAA;
Wait( 1 );
obj << Cumulative Events Plot( Crow AMSAA( 0 ) );
obj << Mean Time Between Failures Plot( Crow AMSAA( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Crow AMSAA;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Crow AMSAA( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Crow AMSAA( 0 );
```

#### [Crow AMSAA with Modified MLE](#crow-amsaa-with-modified-mle_2)[](#crow-amsaa-with-modified-mle_2 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Crow AMSAA with Modified MLE( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Crow AMSAA with Modified MLE( state=0\|1 ) ); scrobj \<\< Crow AMSAA with Modified MLE( state=0\|1 ) )

**Description:** Shows or hides the Crow-AMSAA model with bias correction for beta in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Crow AMSAA with Modified MLE;
Wait( 1 );
obj << Cumulative Events Plot( Crow AMSAA with Modified MLE( 0 ) );
obj << Mean Time Between Failures Plot( Crow AMSAA with Modified MLE( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Crow AMSAA with Modified MLE;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Crow AMSAA with Modified MLE( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Crow AMSAA with Modified MLE( 0 );
```

#### [Customize Average MTBF](#customize-average-mtbf)[](#customize-average-mtbf "Click to copy url")

**Syntax:** obj \<\< Mean Time Between Failures( Options( Sample MTBF Type( "Customized Average MTBF" ), Customize Average MTBF( vector ) ) ); scrobj \<\< Options( Sample MTBF Type( "Customized Average MTBF" ), Customize Average MTBF( vector ) )

**Description:** Specifies a set of disjoint intervals that are used to calculate mean time between failures (MTBF).

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
obj << Mean Time Between Failures Plot(
    Options(
        Sample MTBF Type( "Customized Average MTBF" ),
        Customize Average MTBF( [2500, 5000, 7500, 11000] )
    )
);
(obj << report)["Mean Time Between Failures"] << Close( 0 );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
plot = obj << Mean Time Between Failures Plot;
plot << Options(
    Sample MTBF Type( "Customized Average MTBF" ),
    Customize Average MTBF( [2500, 5000, 7500, 11000] )
);
(obj << report)["Mean Time Between Failures"] << Close( 0 );
```

#### [Fixed Parameter Crow AMSAA](#fixed-parameter-crow-amsaa_3)[](#fixed-parameter-crow-amsaa_3 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Fixed Parameter Crow AMSAA( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Fixed Parameter Crow AMSAA( state=0\|1 ) ); scrobj \<\< Fixed Parameter Crow AMSAA( state=0\|1 ) )

**Description:** Shows or hides the Fixed Parameter Crow-AMSAA model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Fixed Parameter Crow AMSAA;
Wait( 1 );
obj << Cumulative Events Plot( Fixed Parameter Crow AMSAA( 0 ) );
obj << Mean Time Between Failures Plot( Fixed Parameter Crow AMSAA( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Fixed Parameter Crow AMSAA;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Fixed Parameter Crow AMSAA( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Fixed Parameter Crow AMSAA( 0 );
```

#### [Interval Size](#interval-size)[](#interval-size "Click to copy url")

**Syntax:** obj \<\< Mean Time Between Failures( Options( Sample MTBF Type( "Equal Interval Average MTBF" ), Interval Size( number ) ) ); scrobj \<\< Options( Sample MTBF Type( "Equal Interval Average MTBF" ), Interval Size( number ) )

**Description:** Specifies the size of the interval that is used to calculate mean time between failures (MTBF).

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Mean Time Between Failures Plot(
    Options( Sample MTBF Type( "Equal Interval Average MTBF" ), Interval Size( 2500 ) )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Mean Time Between Failures"] << Close( 0 );
plot = obj << Mean Time Between Failures Plot;
plot << Options( Sample MTBF Type( "Equal Interval Average MTBF" ), Interval Size( 2500 ) );
```

#### [Options](#options)[](#options "Click to copy url")

**Syntax:** obj \<\< Mean Time Between Failures( Options( ... ) ); scrobj \<\< Options( ... )

**Description:** Enables you to configure the Mean Time Between Failures plot.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/TurbineEngineDesign1.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Day ),
    Event Count( :Fixes ),
    Phase( :Design Phase )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Mean Time Between Failures Plot(
    Options( Sample MTBF Type( "Equal Interval Average MTBF" ) )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/TurbineEngineDesign1.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Day ),
    Event Count( :Fixes ),
    Phase( :Design Phase )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Options( Sample MTBF Type( "Equal Interval Average MTBF" ) );
```

#### [Piecewise Weibull NHPP](#piecewise-weibull-nhpp_2)[](#piecewise-weibull-nhpp_2 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Piecewise Weibull NHPP( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Piecewise Weibull NHPP( state=0\|1 ) ); scrobj \<\< Piecewise Weibull NHPP( state=0\|1 ) )

**Description:** Shows or hides the Piecewise Weibull NHPP model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/TurbineEngineDesign1.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Day ),
    Event Count( :Fixes ),
    Phase( :Design Phase )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Piecewise Weibull NHPP;
Wait( 1 );
obj << Cumulative Events Plot( Piecewise Weibull NHPP( 0 ) );
obj << Mean Time Between Failures Plot( Piecewise Weibull NHPP( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/TurbineEngineDesign1.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Day ),
    Event Count( :Fixes ),
    Phase( :Design Phase )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Piecewise Weibull NHPP;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Piecewise Weibull NHPP( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Piecewise Weibull NHPP( 0 );
```

#### [Piecewise Weibull NHPP Change Point Detection](#piecewise-weibull-nhpp-change-point-detection_2)[](#piecewise-weibull-nhpp-change-point-detection_2 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Piecewise Weibull NHPP Change Point Detection( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Piecewise Weibull NHPP Change Point Detection( state=0\|1 ) ); scrobj \<\< Piecewise Weibull NHPP Change Point Detection( state=0\|1 ) )

**Description:** Shows or hides the Reinitialized Weibull NHPP model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/BrakeReliability.jmp" );
obj = dt << Reliability Growth(
    Input Format( Dates ),
    Timestamp( :Date ),
    Event Count( :Fixes )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Piecewise Weibull NHPP Change Point Detection;
Wait( 1 );
obj << Cumulative Events Plot( Piecewise Weibull NHPP Change Point Detection( 0 ) );
obj << Mean Time Between Failures Plot( Piecewise Weibull NHPP Change Point Detection( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/BrakeReliability.jmp" );
obj = dt << Reliability Growth(
    Input Format( Dates ),
    Timestamp( :Date ),
    Event Count( :Fixes )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Piecewise Weibull NHPP Change Point Detection;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Piecewise Weibull NHPP Change Point Detection( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Piecewise Weibull NHPP Change Point Detection( 0 );
```

#### [Reinitialized Weibull NHPP](#reinitialized-weibull-nhpp_2)[](#reinitialized-weibull-nhpp_2 "Click to copy url")

**Syntax:** obj \<\< Cumulative Events Plot( Reinitialized Weibull NHPP( state=0\|1 ) ); obj \<\< Mean Time Between Failures Plot( Reinitialized Weibull NHPP( state=0\|1 ) ); scrobj \<\< Reinitialized Weibull NHPP( state=0\|1 ) )

**Description:** Shows or hides the Reinitialized Weibull NHPP model in the Cumulative Events or Mean Time Between Failures plot. On by default.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/ProductionEquipment.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Hours of Operation ),
    Event Count( :Fixes ),
    Phase( :Design Stage )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Reinitialized Weibull NHPP;
Wait( 1 );
obj << Cumulative Events Plot( Reinitialized Weibull NHPP( 0 ) );
obj << Mean Time Between Failures Plot( Reinitialized Weibull NHPP( 0 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/ProductionEquipment.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Hours of Operation ),
    Event Count( :Fixes ),
    Phase( :Design Stage )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Reinitialized Weibull NHPP;
Wait( 1 );
cep = obj << Cumulative Events Plot;
cep << Reinitialized Weibull NHPP( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Reinitialized Weibull NHPP( 0 );
```

#### [Sample MTBF Type](#sample-mtbf-type)[](#sample-mtbf-type "Click to copy url")

**Syntax:** obj \<\< Mean Time Between Failures( Options( Sample MTBF Type( "Equal Interval Average MTBF"\|"Customized Average MTBF" ) ) ); scrobj \<\< Options( Sample MTBF Type( "Equal Interval Average MTBF"\|"Customized Average MTBF" ) )

**Description:** Specifies the calculation method for the Mean Time Between Failures plot.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/TurbineEngineDesign1.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Day ),
    Event Count( :Fixes ),
    Phase( :Design Phase )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
obj << Mean Time Between Failures Plot(
    Options( Sample MTBF Type( "Equal Interval Average MTBF" ) )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/TurbineEngineDesign1.jmp" );
obj = dt << Reliability Growth(
    Input Format( Time to Event ),
    Time to Event( :Day ),
    Event Count( :Fixes ),
    Phase( :Design Phase )
);
Report( obj )["Mean Time Between Failures"] << Close( 0 );
mtbf = obj << Mean Time Between Failures Plot;
mtbf << Options( Sample MTBF Type( "Equal Interval Average MTBF" ) );
```

## [Reliability Growth Report](#reliability-growth-report)[](#reliability-growth-report "Click to copy url")

### [Item Messages](#item-messages_5)[](#item-messages_5 "Click to copy url")

#### [Show Cumulative Events Plot](#show-cumulative-events-plot_2)[](#show-cumulative-events-plot_2 "Click to copy url")

**Syntax:** scrobj \<\< Show Cumulative Events Plot( state=0\|1 )

**Description:** Shows or hides the Cumulative Events plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show Cumulative Events Plot( 1 );
```

#### [Show Intensity Plot](#show-intensity-plot_2)[](#show-intensity-plot_2 "Click to copy url")

**Syntax:** scrobj \<\< Show Intensity Plot( state=0\|1 )

**Description:** Shows or hides the Intensity plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show Intensity Plot( 1 );
```

#### [Show MTBF Plot](#show-mtbf-plot_2)[](#show-mtbf-plot_2 "Click to copy url")

**Syntax:** scrobj \<\< Show MTBF Plot( state=0\|1 )

**Description:** Shows or hides the mean time between failures (MTBF) plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show MTBF Plot( 0 );
```

#### [Show Profilers](#show-profilers_2)[](#show-profilers_2 "Click to copy url")

**Syntax:** scrobj \<\< Show Profilers( state=0\|1 )

**Description:** Shows or hides the profilers for mean time between failures (MTBF), failure intensity, and cumulative events.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/NewEngineOperation.jmp" );
obj = dt << Reliability Growth( Input Format( Time to Event ), Time to Event( :Hours ) );
Report( obj )["Observed Data"] << Close( 1 );
report = obj << Crow AMSAA;
report << Show Profilers( 1 );
```

[ Previous](Reliability%20Forecast.html "Reliability Forecast") [Next ](Repeated%20Measures%20Degradation.html "Repeated Measures Degradation")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
