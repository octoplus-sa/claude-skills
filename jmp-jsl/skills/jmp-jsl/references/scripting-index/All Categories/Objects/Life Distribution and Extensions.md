# Life Distribution and Extensions

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Life%20Distribution%20and%20Extensions.html](https://jsl.jmp.com/All%20Categories/Objects/Life%20Distribution%20and%20Extensions.html)*

---

# [Life Distribution and Extensions](#life-distribution-and-extensions)[](#life-distribution-and-extensions "Click to copy url")

## [Compare Groups](#compare-groups)[](#compare-groups "Click to copy url")

### [Columns](#columns)[](#columns "Click to copy url")

#### [Censor](#censor)[](#censor "Click to copy url")

**Syntax:** obj \<\< Censor( column )

#### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

#### [Grouping](#grouping)[](#grouping "Click to copy url")

**Syntax:** obj \<\< Grouping( column(s) )

#### [Label](#label)[](#label "Click to copy url")

**Syntax:** obj \<\< Label( column )

#### [Time to Event](#time-to-event)[](#time-to-event "Click to copy url")

**Syntax:** obj \<\< Time to Event( column(s) )

#### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

### [Item Messages](#item-messages)[](#item-messages "Click to copy url")

#### [Change Confidence Level](#change-confidence-level)[](#change-confidence-level "Click to copy url")

**Syntax:** obj \<\< Change Confidence Level( fraction )

**Description:** Specifies the confidence level for the entire platform. All plots and reports update accordingly.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor ),
    Select Distribution( Distribution, Exponential )
);
obj << Change Confidence Level( 0.99 );
```

#### [Default Parametric Distribution](#default-parametric-distribution)[](#default-parametric-distribution "Click to copy url")

**Syntax:** obj \<\< Default Parametric Distribution( "Lognormal"\|"Weibull"\|"Loglogistic"\|"Frechet"\|"Normal"\|"SEV"\|"Logistic"\|"LEV"\|"Exponential"\|"LogGenGamma"\|"GenGamma"\|"TH Weibull"\|"TH Lognormal"\|"TH Frechet"\|"TH Loglogistic"\|"ZI Weibull"\|"ZI Lognormal"\|"ZI Frechet"\|"ZI Loglogistic"\|"DS Weibull"\|"DS Lognormal"\|"DS Frechet"\|"DS Loglogistic" )

#### [Estimate Probability](#estimate-probability)[](#estimate-probability "Click to copy url")

**Syntax:** obj \<\< Estimate Probability( state=\<0\|1\> \| \<Compute( array )\> )

**Description:** Shows or hides an Estimate Probability report that corresponds to the most recently selected distribution in the Compare Distribution report. Use the Compute argument to specify an array of time values for the probability estimation.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor ),
    Select Distribution( Distribution, Exponential )
);
obj << Estimate Probability( 1 );
obj << Estimate Probability( Compute( [1000] ) );
```

#### [Estimate Quantile](#estimate-quantile)[](#estimate-quantile "Click to copy url")

**Syntax:** obj \<\< Estimate Quantile( state=\<0\|1\> \| \<Compute( array )\> )

**Description:** Shows or hides an Estimate Quantile report that corresponds to the most recently selected distribution in the Compare Quantile report. Use the Compute argument to specify an array of probability values for the quantile estimation.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor ),
    Show Quantile Functions( 1 )
);
obj << Select Distribution( Quantile, Exponential );
obj << Estimate Quantile( 1 );
obj << Estimate Quantile( Compute( [.1] ) );
```

#### [Fit Distribution](#fit-distribution)[](#fit-distribution "Click to copy url")

**Syntax:** obj \<\< Fit Distribution( distribution )

**Description:** Fits the specified distribution.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor )
);
obj << Fit Distribution( "Loglogistic" );
```

#### [Interval Type](#interval-type)[](#interval-type "Click to copy url")

**Syntax:** obj \<\< Interval Type( "Simultaneous"\|"Pointwise" )

**Description:** Specifies the type of confidence interval shown for the Nonparametric fit in the Compare Distributions plot. The available options are pointwise or simultaneous confidence intervals.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor )
);
Wait( 1 );
obj << Interval Type( "Pointwise" );
```

#### [Select Distribution](#select-distribution)[](#select-distribution "Click to copy url")

**Syntax:** obj \<\< Select Distribution( Distribution\|Quantile\|Hazard\|Density, distribution )

**Description:** Specifies a distribution to show for each group on the specified graph. This is equivalent to selecting a distribution option in the Compare Distribution, Compare Quantile, Compare Hazard, or Compare Density reports.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor )
);
obj << Select Distribution( Distribution, Weibull );
```

#### [Select Scale](#select-scale)[](#select-scale "Click to copy url")

**Syntax:** obj \<\< Select Scale( distribution )

**Description:** Specifies a scale for the probability axis in the Compare Distribution plot. This is equivalent to selecting an option under Scale in the Compare Distribution report.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor )
);
obj << Select Scale( Normal );
```

#### [Show Confidence Area](#show-confidence-area)[](#show-confidence-area "Click to copy url")

**Syntax:** obj \<\< Show Confidence Area( state=0\|1 )

**Description:** Shows or hides the shaded confidence regions in the plots. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor ),
    Select Distribution( Distribution, Exponential )
);
Wait( 1 );
obj << Show Confidence Area( 0 );
```

#### [Show Density Functions](#show-density-functions)[](#show-density-functions "Click to copy url")

**Syntax:** obj \<\< Show Density Functions( state=0\|1 )

**Description:** Shows or hides the Compare Density report, which overlays plots of the density functions for each group for the selected distribution.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor ),
    Show Density Functions( 1 )
);
obj << Select Distribution( Density, Weibull );
```

#### [Show Hazard Functions](#show-hazard-functions)[](#show-hazard-functions "Click to copy url")

**Syntax:** obj \<\< Show Hazard Functions( state=0\|1 )

**Description:** Shows or hides the Compare Hazard report, which overlays plots of the hazard functions for each group for the selected distribution.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor ),
    Show Hazard Functions( 1 )
);
obj << Select Distribution( Hazard, Weibull );
```

#### [Show Points](#show-points)[](#show-points "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides data points in the probability plot. The Life Distribution platform uses the midpoint estimates of the step function to construct probability plots. When you deselect the Show Points option, the midpoint estimates are replaced by Kaplan-Meier estimates. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor )
);
Wait( 1 );
obj << Show Points( 0 );
```

#### [Show Quantile Functions](#show-quantile-functions)[](#show-quantile-functions "Click to copy url")

**Syntax:** obj \<\< Show Quantile Functions( state=0\|1 )

**Description:** Shows or hides the Compare Quantile report, which overlays plots of the quantile functions for each group for the selected distribution.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor ),
    Show Quantile Functions( 1 )
);
obj << Select Distribution( Quantile, Weibull );
```

#### [Show Survival Curve](#show-survival-curve)[](#show-survival-curve "Click to copy url")

**Syntax:** obj \<\< Show Survival Curve( state=0\|1 )

**Description:** Switches between the failure probability and the survival curve on the Compare Distribution probability plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor ),
    Show Survival Curve( 1 )
);
```

#### [Tabbed Report](#tabbed-report)[](#tabbed-report "Click to copy url")

**Syntax:** obj \<\< Tabbed Report( state=0\|1 )

**Description:** Shows graphs and data in individual tabs rather than in the default outline style.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Life Distribution(
    Perspective( Compare Groups ),
    Y( :days ),
    Grouping( :Group ),
    Censor( :Censor ),
    Tabbed Report( 1 )
);
```

### [Shared Item Messages](#shared-item-messages)[](#shared-item-messages "Click to copy url")

#### [Action](#action)[](#action "Click to copy url")

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

#### [Apply Preset](#apply-preset)[](#apply-preset "Click to copy url")

**Syntax:** Apply Preset( preset ); Apply Preset( source, label, \<Folder( folder {, folder2, ...} )\> )

**Description:** Apply a previously created preset to the object, updating the options and customizations to match the saved settings.

**JMP Version Added:** 18

**Anonymous preset**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
dt2 = Open( "$SAMPLE_DATA/Dogs.jmp" );
obj2 = dt2 << Oneway( Y( :LogHist0 ), X( :drug ) );
Wait( 1 );
obj2 << Apply Preset( preset );
```

**Search by name**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "Compare Distributions" );
```

**Search within folder(s)**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "t-Tests", Folder( "Compare Means" ) );
```

#### [Automatic Recalc](#automatic-recalc)[](#automatic-recalc "Click to copy url")

**Syntax:** obj \<\< Automatic Recalc( state=0\|1 )

**Description:** Redoes the analysis automatically for exclude and data changes. If the Automatic Recalc option is turned on, you should consider using Wait(0) commands to ensure that the exclude and data changes take effect before the recalculation.

``` jsl
obj << Automatic Recalc( 1 );
dt << Select Rows( 5 ) << Exclude( 1 );
```

#### [Broadcast](#broadcast)[](#broadcast "Click to copy url")

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

#### [Column Switcher](#column-switcher)[](#column-switcher "Click to copy url")

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

#### [Copy ByGroup Script](#copy-bygroup-script)[](#copy-bygroup-script "Click to copy url")

**Syntax:** obj \<\< Copy ByGroup Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
obj[1] << Copy ByGroup Script;
```

#### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
obj << Copy Script;
```

#### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
obj << Data Table Window;
```

#### [Get By Levels](#get-by-levels)[](#get-by-levels "Click to copy url")

**Syntax:** obj \<\< Get By Levels

**Description:** Returns an associative array mapping the by group columns to their values.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv << Get By Levels;
```

#### [Get ByGroup Script](#get-bygroup-script)[](#get-bygroup-script "Click to copy url")

**Syntax:** obj \<\< Get ByGroup Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
t = obj[1] << Get ByGroup Script;
Show( t );
```

#### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

**General**

``` jsl
t = obj << Get Container;
Show( (t << XPath( "//OutlineBox" )) << Get Title );
```

**Platform with Filter**

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

#### [Get Data Table](#get-data-table)[](#get-data-table "Click to copy url")

**Syntax:** obj \<\< Get Data Table

**Description:** Returns a reference to the data table.

``` jsl
t = obj << Get Datatable;
Show( N Rows( t ) );
```

#### [Get Group Platform](#get-group-platform)[](#get-group-platform "Click to copy url")

**Syntax:** obj \<\< Get Group Platform

**Description:** Return the Group Platform object if this platform is part of a Group. Otherwise, returns Empty().

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( Y( :weight ), X( :height ), By( :sex ) );
group = biv[1] << Get Group Platform;
Wait( 1 );
group << Layout( "Arrange in Tabs" );
```

#### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
t = obj << Get Script;
Show( t );
```

#### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
t = obj << Get Script With Data Table;
Show( t );
```

#### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
t = obj << Get Timing;
Show( t );
```

#### [Get Web Support](#get-web-support)[](#get-web-support "Click to copy url")

**Syntax:** obj \<\< Get Web Support

**Description:** Return a number indicating the level of Interactive HTML support for the display object. 1 means some or all elements are supported. 0 means no support.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
s = obj << Get Web Support();
Show( s );
```

#### [Get Where Expr](#get-where-expr)[](#get-where-expr "Click to copy url")

**Syntax:** obj \<\< Get Where Expr

**Description:** Returns the Where expression for the data subset, if the platform was launched with By() or Where(). Otherwise, returns Empty()

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv2 = dt << Bivariate( X( :height ), Y( :weight ), Where( :age < 14 & :height > 60 ) );
Show( biv[1] << Get Where Expr, biv2 << Get Where Expr );
```

#### [Ignore Platform Preferences](#ignore-platform-preferences)[](#ignore-platform-preferences "Click to copy url")

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

#### [Local Data Filter](#local-data-filter)[](#local-data-filter "Click to copy url")

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

#### [New Preset](#new-preset)[](#new-preset "Click to copy url")

**Syntax:** obj = New Preset()

**Description:** Create an anonymous preset representing the options and customizations applied to the object. This object can be passed to Apply Preset to copy the settings to another object of the same type.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
```

#### [Paste Local Data Filter](#paste-local-data-filter)[](#paste-local-data-filter "Click to copy url")

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

#### [Redo Analysis](#redo-analysis)[](#redo-analysis "Click to copy url")

**Syntax:** obj \<\< Redo Analysis

**Description:** Rerun this same analysis in a new window. The analysis will be different if the data has changed.

``` jsl
obj << Redo Analysis;
```

#### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
obj << Relaunch Analysis;
```

#### [Remove Column Switcher](#remove-column-switcher)[](#remove-column-switcher "Click to copy url")

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

#### [Remove Local Data Filter](#remove-local-data-filter)[](#remove-local-data-filter "Click to copy url")

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

#### [Report](#report)[](#report "Click to copy url")

**Syntax:** obj \<\< Report; Report( obj )

**Description:** Returns a reference to the report object.

``` jsl
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

#### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
obj << Report View( "Summary" );
```

#### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
obj[1] << Save ByGroup Script to Data Table;
```

#### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
obj[1] << Save ByGroup Script to Journal;
```

#### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
obj[1] << Save ByGroup Script to Script Window;
```

#### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
obj << Save Script for All Objects;
```

#### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

#### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

#### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
obj << Save Script to Journal;
```

#### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
obj << Save Script to Report;
```

#### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
obj << Save Script to Script Window;
```

#### [SendToByGroup](#sendtobygroup)[](#sendtobygroup "Click to copy url")

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

#### [SendToEmbeddedScriptable](#sendtoembeddedscriptable)[](#sendtoembeddedscriptable "Click to copy url")

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

#### [SendToReport](#sendtoreport)[](#sendtoreport "Click to copy url")

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

#### [Sync to Data Table Changes](#sync-to-data-table-changes)[](#sync-to-data-table-changes "Click to copy url")

**Syntax:** obj \<\< Sync to Data Table Changes

**Description:** Sync with the exclude and data changes that have been made.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dist = Distribution( Continuous Distribution( Column( :POP ) ) );
Wait( 1 );
dt << Delete Rows( dt << Get Rows Where( :Region == "W" ) );
dist << Sync To Data Table Changes;
```

#### [Title](#title)[](#title "Click to copy url")

**Syntax:** obj \<\< Title( "new title" )

**Description:** Sets the title of the platform.

``` jsl
obj << Title( "My Platform" );
```

#### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
r = obj << Top Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

#### [Transform Column](#transform-column)[](#transform-column "Click to copy url")

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

#### [View Web XML](#view-web-xml)[](#view-web-xml "Click to copy url")

**Syntax:** obj \<\< View Web XML

**Description:** Returns the XML code that is used to create the interactive HTML report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
xml = obj << View Web XML;
```

#### [Window View](#window-view)[](#window-view "Click to copy url")

**Syntax:** obj = Y(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

## [Competing Cause \> Mean Remaining Life](#competing-cause-mean-remaining-life)[](#competing-cause-mean-remaining-life "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Compute](#compute)[](#compute "Click to copy url")

**Syntax:** obj \<\< Mean Remaining Life( Compute( array ) )

**Description:** Specifies an array of time values to be added to the Mean Remaining Life Calculator.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Mean Remaining Life( Configuration( 1, 100, 1000, 333 ), Compute( [1000 2000] ) );
```

#### [Configuration](#configuration)[](#configuration "Click to copy url")

**Syntax:** obj \<\< Mean Remaining Life( Configuration( useBootstrap, BootstrapSize, SampleSize, RandomSeed ) )

**Description:** Specifies the settings for the Mean Remaining Life Calculator, which estimates the mean remaining life of a unit at a set of given survival times. The arguments specify if a bootstrap should be used, the number of bootstrap aggregated distributions, the number of simulated failure times, and a random seed. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Mean Remaining Life( Configuration( 1, 100, 1000, 333 ), Compute( [1000 2000] ) );
```

#### [Get Results](#get-results)[](#get-results "Click to copy url")

**Syntax:** obj \<\< Mean Remaining Life( Get Results )

**Description:** Returns a matrix of the table in the Mean Remaining Life Calculator.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Mean Remaining Life( Configuration( 1, 100, 1000, 333 ), Compute( [1000 2000] ) );
obj << Mean Remaining Life( Get Results );
```

## [Competing Cause](#competing-cause)[](#competing-cause "Click to copy url")

### [Columns](#columns_1)[](#columns_1 "Click to copy url")

#### [By](#by)[](#by "Click to copy url")

**Syntax:** obj \<\< By( column(s) )

**Description:** Performs a separate analysis for each level of the specified column.

#### [Censor](#censor_1)[](#censor_1 "Click to copy url")

**Syntax:** obj \<\< Censor( column )

#### [Failure Cause](#failure-cause)[](#failure-cause "Click to copy url")

**Syntax:** obj \<\< Failure Cause( column )

#### [Freq](#freq_1)[](#freq_1 "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

#### [Label](#label_1)[](#label_1 "Click to copy url")

**Syntax:** obj \<\< Label( column )

#### [Time to Event](#time-to-event_1)[](#time-to-event_1 "Click to copy url")

**Syntax:** obj \<\< Time to Event( column(s) )

#### [Y](#y_1)[](#y_1 "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Bootstrap Sample Size](#bootstrap-sample-size)[](#bootstrap-sample-size "Click to copy url")

**Syntax:** obj \<\< Bootstrap Sample Size( n )

**Description:** Specifies the number of samples to be used in the bootstrap method that is used to obtain Bayesian estimates or Weibayes results. For Bayesian and Weibayes methods, the confidence limits for the aggregated functions that appear in the Distribution Profiler must be simulated using a parametric bootstrap.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull ),
    Allow failure mode to use Bayesian models( 1 ),
    Fit Model(
        {{"0", Bayesian Lognormal, 0}, {"1", Weibull, 1}, {"10", Weibull, 0}, {"15", Weibull,
        0}, {"2", Weibull, 0}, {"5", Weibull, 0}, {"6", Weibull, 0}, {"9", Weibull, 0}}
    )
);
obj << Bootstrap Sample Size( 1000 );
```

#### [Compute Remaining Life Distribution](#compute-remaining-life-distribution)[](#compute-remaining-life-distribution "Click to copy url")

**Syntax:** obj \<\< Compute Remaining Life Distribution( time0, time1 )

**Description:** Returns a list that contains the remaining life distribution value at time1, given that the unit survived through time0. The list also contains lower and upper limits for the remaining life estimate.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Show Remaining Life Distribution( 1 );
p = obj << Compute Remaining Life Distribution( 2000, 4000 );
```

#### [Density](#density)[](#density "Click to copy url")

**Syntax:** obj \<\< Density( t )

**Description:** Returns the density value at the specified time.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
d = obj << Density( .5 );
```

#### [Export Bootstrap Results](#export-bootstrap-results)[](#export-bootstrap-results "Click to copy url")

**Syntax:** obj \<\< Export Bootstrap Results( time )

**Description:** Saves the bootstrap results to a new data table. A bootstrap method is used to obtain Bayesian estimates or Weibayes results. For Bayesian and Weibayes methods, the confidence limits for the aggregated functions that appear in the Distribution Profiler must be simulated using a parametric bootstrap.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull ),
    Allow failure mode to use Bayesian models( 1 ),
    Fit Model(
        {{"0", Bayesian Lognormal, 0}, {"1", Weibull, 1}, {"10", Weibull, 0}, {"15", Weibull,
        0}, {"2", Weibull, 0}, {"5", Weibull, 0}, {"6", Weibull, 0}, {"9", Weibull, 0}}
    )
);
obj << Export Bootstrap Results( 15000 );
```

#### [Export Lifetime Data for Individual Causes](#export-lifetime-data-for-individual-causes)[](#export-lifetime-data-for-individual-causes "Click to copy url")

**Syntax:** obj \<\< Export Lifetime Data for Individual Causes

**Description:** Export a stacked data set that consists of lifetime data for individual causes. A lifetime data for a cause is a copy of the original data while right censoring all observations other than the cause.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull ),
    Allow failure mode to use Bayesian models( 1 )
);
dt = obj << Export Lifetime Data for Individual Causes();
```

#### [Fit Model](#fit-model)[](#fit-model "Click to copy url")

**Syntax:** obj \<\< Fit Model( specification )

**Description:** Fits a competing cause model using the given specification. The model is specified by a list of 3-item lists for each cause. Each sublist consists of a cause code, a distribution, and an indicator to omit the cause or not.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Fit Model(
    {{"0", Weibull, 1}, {"10", Weibull, 0}, {"15", Weibull, 0}, {"2", Weibull, 0}, {"5",
    Weibull, 0}, {"6", Weibull, 0}, {"9", Weibull, 0}}
);
```

#### [Get Causes](#get-causes)[](#get-causes "Click to copy url")

**Syntax:** obj \<\< Get Causes

**Description:** Returns a list of the cause codes.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
lst = obj << Get Causes;
```

#### [Get Estimates](#get-estimates)[](#get-estimates "Click to copy url")

**Syntax:** obj \<\< Get Estimates

**Description:** Returns a list that contains the causes, counts, distributions, and parameter estimates for the competing cause model.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
res = obj << Get Estimates;
```

#### [Get Life Distribution](#get-life-distribution)[](#get-life-distribution "Click to copy url")

**Syntax:** obj \<\< Get Life Distribution( i )

**Description:** Returns a reference to the specified Life Distribution report object in the Individual Causes section of the Competing Cause report. For the argument to this option, the Life Distribution reports are indexed from 0 to n-1, where n is the number of causes.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
ld = (obj << Get Life Distribution( 1 ));
```

#### [Get Model Specification](#get-model-specification)[](#get-model-specification "Click to copy url")

**Syntax:** obj \<\< Get Model Specification

**Description:** Returns a list that contains the specifications for the competing cause model. This list can be used as the argument for the Fit Model message for the Competing Cause platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
spec = obj << Get Model Specification;
```

#### [Hazard](#hazard)[](#hazard "Click to copy url")

**Syntax:** obj \<\< Hazard( t )

**Description:** Returns the value of the hazard function at the specified time.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
h = obj << Hazard( 2500 );
```

#### [Mean Remaining Life](#mean-remaining-life)[](#mean-remaining-life "Click to copy url")

**Syntax:** obj \<\< Mean Remaining Life( state=0\|1 ) obj \<\< Mean Remaining Life( Configuration(), Compute(), Get Results )

**Description:** Shows or hides the Mean Remaining Life Calculator, which enables you to estimate the mean remaining life of a unit at a given survival time. You can also use this option to send messages to the Mean Remaining Life calculator object.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Mean Remaining Life( 1 );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Mean Remaining Life( Configuration( 1, 100, 1000, 333 ), Compute( [1000 2000] ) );
```

#### [Omit](#omit)[](#omit "Click to copy url")

**Syntax:** obj \<\< Omit( k, 0\|1 )

**Description:** Shows or hides the specified cause from the Cause Combination plot. The first argument specifies the number of the cause. If the second argument is 1, the specified cause is removed; if the second argument is 0, the specified cause is included.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
Wait( 1 );
obj << Omit( 1, 1 );
```

#### [Probability](#probability)[](#probability "Click to copy url")

**Syntax:** obj \<\< Probability( t )

**Description:** Returns the failure probability at the specified time.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
p = obj << Probability( 2500 );
```

#### [Quantile](#quantile)[](#quantile "Click to copy url")

**Syntax:** obj \<\< Quantile( p )

**Description:** Returns the quantile value at the specified probability.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
q = obj << Quantile( .5 );
```

#### [Set Scale](#set-scale)[](#set-scale "Click to copy url")

**Syntax:** obj \<\< Set Scale( name )

**Description:** Specifies the probability scale for the vertical axis of the Cause Combination plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
Wait( 1 );
obj << Set Scale( Weibull );
```

#### [Show Points](#show-points_1)[](#show-points_1 "Click to copy url")

**Syntax:** obj \<\< Show Points( \<0\|1\> )

**Description:** Shows or hides data points in the Cause Combination plot. The Life Distribution platform uses the midpoint estimates of the step function to construct probability plots. When you deselect the Show Points option, the midpoint estimates are replaced by Kaplan-Meier estimates. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
Wait( 1 );
obj << Show Points( 0 );
```

#### [Show Remaining Life Distribution](#show-remaining-life-distribution)[](#show-remaining-life-distribution "Click to copy url")

**Syntax:** obj \<\< Show Remaining Life Distribution( state=0\|1 )

**Description:** Shows or hides the profiler of the remaining life distribution, which is conditional upon the unit surviving through a given time.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Show Remaining Life Distribution( 1 );
```

#### [Show Subdistributions](#show-subdistributions)[](#show-subdistributions "Click to copy url")

**Syntax:** obj \<\< Show Subdistributions( state=0\|1 )

**Description:** Shows or hides the profiler for each individual cause subdistribution. When you select the Show Subdistributions option, the Cause Combination plot updates to show the subdistribution functions for all causes.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Show Subdistributions( 1 );
```

#### [Subdistribution](#subdistribution)[](#subdistribution "Click to copy url")

**Syntax:** obj \<\< Subdistribution( Cause(i), Compute(m) )

**Description:** Specifies the cause and time values for the subdistribution calculations. The Cause argument specifies the number of the cause. The Compute argument is a column vector of time values. The Show Subdistributions option must be selected before using this message.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull )
);
obj << Show Subdistributions( 1 );
obj << Subdistribution( Cause( 2 ), Compute( [5000, 10000] ) );
```

#### [Tabbed Report](#tabbed-report_1)[](#tabbed-report_1 "Click to copy url")

**Syntax:** obj \<\< Tabbed Report( state=0\|1 )

**Description:** Organizes the sections of the Competing Cause report into tabs.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull ),
    Tabbed Report( 1 )
);
```

#### [Tabbed Report for Individual Causes](#tabbed-report-for-individual-causes)[](#tabbed-report-for-individual-causes "Click to copy url")

**Syntax:** obj \<\< Tabbed Report for Individual Causes( state=0\|1 )

**Description:** Organizes the Life Distribution reports in the Individual Causes section of the Competing Cause report into tabs.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Appliance.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause( Weibull ),
    Tabbed Report for Individual Causes( 1 )
);
```

### [Shared Item Messages](#shared-item-messages_1)[](#shared-item-messages_1 "Click to copy url")

#### [Action](#action_1)[](#action_1 "Click to copy url")

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

#### [Apply Preset](#apply-preset_1)[](#apply-preset_1 "Click to copy url")

**Syntax:** Apply Preset( preset ); Apply Preset( source, label, \<Folder( folder {, folder2, ...} )\> )

**Description:** Apply a previously created preset to the object, updating the options and customizations to match the saved settings.

**JMP Version Added:** 18

**Anonymous preset**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
dt2 = Open( "$SAMPLE_DATA/Dogs.jmp" );
obj2 = dt2 << Oneway( Y( :LogHist0 ), X( :drug ) );
Wait( 1 );
obj2 << Apply Preset( preset );
```

**Search by name**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "Compare Distributions" );
```

**Search within folder(s)**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "t-Tests", Folder( "Compare Means" ) );
```

#### [Automatic Recalc](#automatic-recalc_1)[](#automatic-recalc_1 "Click to copy url")

**Syntax:** obj \<\< Automatic Recalc( state=0\|1 )

**Description:** Redoes the analysis automatically for exclude and data changes. If the Automatic Recalc option is turned on, you should consider using Wait(0) commands to ensure that the exclude and data changes take effect before the recalculation.

``` jsl
obj << Automatic Recalc( 1 );
dt << Select Rows( 5 ) << Exclude( 1 );
```

#### [Broadcast](#broadcast_1)[](#broadcast_1 "Click to copy url")

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

#### [Column Switcher](#column-switcher_1)[](#column-switcher_1 "Click to copy url")

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

#### [Copy ByGroup Script](#copy-bygroup-script_1)[](#copy-bygroup-script_1 "Click to copy url")

**Syntax:** obj \<\< Copy ByGroup Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
obj[1] << Copy ByGroup Script;
```

#### [Copy Script](#copy-script_1)[](#copy-script_1 "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
obj << Copy Script;
```

#### [Data Table Window](#data-table-window_1)[](#data-table-window_1 "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
obj << Data Table Window;
```

#### [Get By Levels](#get-by-levels_1)[](#get-by-levels_1 "Click to copy url")

**Syntax:** obj \<\< Get By Levels

**Description:** Returns an associative array mapping the by group columns to their values.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv << Get By Levels;
```

#### [Get ByGroup Script](#get-bygroup-script_1)[](#get-bygroup-script_1 "Click to copy url")

**Syntax:** obj \<\< Get ByGroup Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
t = obj[1] << Get ByGroup Script;
Show( t );
```

#### [Get Container](#get-container_1)[](#get-container_1 "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

**General**

``` jsl
t = obj << Get Container;
Show( (t << XPath( "//OutlineBox" )) << Get Title );
```

**Platform with Filter**

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

#### [Get Data Table](#get-data-table_1)[](#get-data-table_1 "Click to copy url")

**Syntax:** obj \<\< Get Data Table

**Description:** Returns a reference to the data table.

``` jsl
t = obj << Get Datatable;
Show( N Rows( t ) );
```

#### [Get Group Platform](#get-group-platform_1)[](#get-group-platform_1 "Click to copy url")

**Syntax:** obj \<\< Get Group Platform

**Description:** Return the Group Platform object if this platform is part of a Group. Otherwise, returns Empty().

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( Y( :weight ), X( :height ), By( :sex ) );
group = biv[1] << Get Group Platform;
Wait( 1 );
group << Layout( "Arrange in Tabs" );
```

#### [Get Script](#get-script_1)[](#get-script_1 "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
t = obj << Get Script;
Show( t );
```

#### [Get Script With Data Table](#get-script-with-data-table_1)[](#get-script-with-data-table_1 "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
t = obj << Get Script With Data Table;
Show( t );
```

#### [Get Timing](#get-timing_1)[](#get-timing_1 "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
t = obj << Get Timing;
Show( t );
```

#### [Get Web Support](#get-web-support_1)[](#get-web-support_1 "Click to copy url")

**Syntax:** obj \<\< Get Web Support

**Description:** Return a number indicating the level of Interactive HTML support for the display object. 1 means some or all elements are supported. 0 means no support.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
s = obj << Get Web Support();
Show( s );
```

#### [Get Where Expr](#get-where-expr_1)[](#get-where-expr_1 "Click to copy url")

**Syntax:** obj \<\< Get Where Expr

**Description:** Returns the Where expression for the data subset, if the platform was launched with By() or Where(). Otherwise, returns Empty()

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv2 = dt << Bivariate( X( :height ), Y( :weight ), Where( :age < 14 & :height > 60 ) );
Show( biv[1] << Get Where Expr, biv2 << Get Where Expr );
```

#### [Ignore Platform Preferences](#ignore-platform-preferences_1)[](#ignore-platform-preferences_1 "Click to copy url")

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

#### [Local Data Filter](#local-data-filter_1)[](#local-data-filter_1 "Click to copy url")

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

#### [New Preset](#new-preset_1)[](#new-preset_1 "Click to copy url")

**Syntax:** obj = New Preset()

**Description:** Create an anonymous preset representing the options and customizations applied to the object. This object can be passed to Apply Preset to copy the settings to another object of the same type.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
```

#### [Paste Local Data Filter](#paste-local-data-filter_1)[](#paste-local-data-filter_1 "Click to copy url")

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

#### [Redo Analysis](#redo-analysis_1)[](#redo-analysis_1 "Click to copy url")

**Syntax:** obj \<\< Redo Analysis

**Description:** Rerun this same analysis in a new window. The analysis will be different if the data has changed.

``` jsl
obj << Redo Analysis;
```

#### [Relaunch Analysis](#relaunch-analysis_1)[](#relaunch-analysis_1 "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
obj << Relaunch Analysis;
```

#### [Remove Column Switcher](#remove-column-switcher_1)[](#remove-column-switcher_1 "Click to copy url")

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

#### [Remove Local Data Filter](#remove-local-data-filter_1)[](#remove-local-data-filter_1 "Click to copy url")

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

#### [Report](#report_1)[](#report_1 "Click to copy url")

**Syntax:** obj \<\< Report; Report( obj )

**Description:** Returns a reference to the report object.

``` jsl
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

#### [Report View](#report-view_1)[](#report-view_1 "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
obj << Report View( "Summary" );
```

#### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table_1)[](#save-bygroup-script-to-data-table_1 "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
obj[1] << Save ByGroup Script to Data Table;
```

#### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal_1)[](#save-bygroup-script-to-journal_1 "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
obj[1] << Save ByGroup Script to Journal;
```

#### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window_1)[](#save-bygroup-script-to-script-window_1 "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
obj[1] << Save ByGroup Script to Script Window;
```

#### [Save Script for All Objects](#save-script-for-all-objects_1)[](#save-script-for-all-objects_1 "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
obj << Save Script for All Objects;
```

#### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table_1)[](#save-script-for-all-objects-to-data-table_1 "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

#### [Save Script to Data Table](#save-script-to-data-table_1)[](#save-script-to-data-table_1 "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

#### [Save Script to Journal](#save-script-to-journal_1)[](#save-script-to-journal_1 "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
obj << Save Script to Journal;
```

#### [Save Script to Report](#save-script-to-report_1)[](#save-script-to-report_1 "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
obj << Save Script to Report;
```

#### [Save Script to Script Window](#save-script-to-script-window_1)[](#save-script-to-script-window_1 "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
obj << Save Script to Script Window;
```

#### [SendToByGroup](#sendtobygroup_1)[](#sendtobygroup_1 "Click to copy url")

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

#### [SendToEmbeddedScriptable](#sendtoembeddedscriptable_1)[](#sendtoembeddedscriptable_1 "Click to copy url")

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

#### [SendToReport](#sendtoreport_1)[](#sendtoreport_1 "Click to copy url")

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

#### [Sync to Data Table Changes](#sync-to-data-table-changes_1)[](#sync-to-data-table-changes_1 "Click to copy url")

**Syntax:** obj \<\< Sync to Data Table Changes

**Description:** Sync with the exclude and data changes that have been made.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dist = Distribution( Continuous Distribution( Column( :POP ) ) );
Wait( 1 );
dt << Delete Rows( dt << Get Rows Where( :Region == "W" ) );
dist << Sync To Data Table Changes;
```

#### [Title](#title_1)[](#title_1 "Click to copy url")

**Syntax:** obj \<\< Title( "new title" )

**Description:** Sets the title of the platform.

``` jsl
obj << Title( "My Platform" );
```

#### [Top Report](#top-report_1)[](#top-report_1 "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
r = obj << Top Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

#### [Transform Column](#transform-column_1)[](#transform-column_1 "Click to copy url")

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

#### [View Web XML](#view-web-xml_1)[](#view-web-xml_1 "Click to copy url")

**Syntax:** obj \<\< View Web XML

**Description:** Returns the XML code that is used to create the interactive HTML report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
xml = obj << View Web XML;
```

#### [Window View](#window-view_1)[](#window-view_1 "Click to copy url")

**Syntax:** obj = Y(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

## [Life Distribution](#life-distribution)[](#life-distribution "Click to copy url")

### [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

#### [Life Distribution](#life-distribution_1)[](#life-distribution_1 "Click to copy url")

**Syntax:** Life Distribution( Y( column(s) ) )

**Description:** Analyzes the distribution of time-to-event data. Can be used for modeling censored data, product lifetime, reliability, and competing causes.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
```

### [Columns](#columns_2)[](#columns_2 "Click to copy url")

#### [By](#by_1)[](#by_1 "Click to copy url")

**Syntax:** obj \<\< By( column(s) )

**Description:** Performs a separate analysis for each level of the specified column.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
```

#### [Censor](#censor_2)[](#censor_2 "Click to copy url")

**Syntax:** obj \<\< Censor( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
```

#### [Failure Cause](#failure-cause_1)[](#failure-cause_1 "Click to copy url")

**Syntax:** obj \<\< Failure Cause( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
```

#### [Freq](#freq_2)[](#freq_2 "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ), Freq( :_freqcol ) );
```

#### [Label](#label_2)[](#label_2 "Click to copy url")

**Syntax:** obj \<\< Label( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
```

#### [Time to Event](#time-to-event_2)[](#time-to-event_2 "Click to copy url")

**Syntax:** obj \<\< Time to Event( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
```

#### [Y](#y_2)[](#y_2 "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
```

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [Censor Code](#censor-code)[](#censor-code "Click to copy url")

**Syntax:** obj = Life Distribution(... Censor Code( value ) )

**Description:** Identifies the value in the Censor column that designates right-censored observations. "1" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Devalt.jmp" );
obj = dt << Life Distribution(
    Y( :Hours ),
    Censor( :Status ),
    Freq( :Weight ),
    Censor Code( "Censored" )
);
obj << Fit Lognormal;
```

#### [Change Confidence Level](#change-confidence-level_1)[](#change-confidence-level_1 "Click to copy url")

**Syntax:** obj \<\< Change Confidence Level( fraction )

**Description:** Specifies the confidence level for the entire platform. All plots and reports update accordingly.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ), Fit Exponential );
obj << Change Confidence Level( 0.99 );
```

#### [Comparison Criterion](#comparison-criterion)[](#comparison-criterion "Click to copy url")

**Syntax:** obj \<\< Comparison Criterion( \<Negative Loglikelihood\|AICc\|BIC\> )

**Description:** Specifies the criterion used to rank models in the Model Comparison report. For all three criteria, smaller values indicate better fit.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit All Distributions;
obj << Comparison Criterion( BIC );
```

#### [Confidence Interval Method](#confidence-interval-method)[](#confidence-interval-method "Click to copy url")

**Syntax:** obj = Life Distribution(... Confidence Interval Method( "Wald"\|"Likelihood" ) )

**Description:** Specifies the method used for computing confidence intervals for the parameters. The default is Wald, but you can select Likelihood instead. However, all confidence intervals provided in the profilers are based on the Wald method. "Wald" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Devalt.jmp" );
obj = dt << Life Distribution(
    Y( :Hours ),
    Censor( :Status ),
    Freq( :Weight ),
    Censor Code( "Censored" ),
    Confidence Interval Method( "Likelihood" )
);
obj << Fit Lognormal;
```

#### [Do Same Analyses For All Groups](#do-same-analyses-for-all-groups)[](#do-same-analyses-for-all-groups "Click to copy url")

**Syntax:** obj \<\< Do Same Analyses For All Groups

**Description:** Applies all selected options from the current group to all by-group sections of the output.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Blenders.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    By( :Group ),
    Censor( :Censor ),
    Fit Exponential
);
obj[2] << Fit Weibull;
Wait( 1 );
obj[2] << Do Same Analyses For All Groups;
```

#### [Fit All DS Distributions](#fit-all-ds-distributions)[](#fit-all-ds-distributions "Click to copy url")

**Syntax:** obj \<\< Fit All DS Distributions

**Description:** Fits all defective subpopulation (DS) distributions.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit All DS Distributions;
```

#### [Fit All Distributions](#fit-all-distributions)[](#fit-all-distributions "Click to copy url")

**Syntax:** obj \<\< Fit All Distributions

**Description:** Fits all distributions except the threshold (TH) distributions.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit All Distributions;
```

#### [Fit All Nonnegative](#fit-all-nonnegative)[](#fit-all-nonnegative "Click to copy url")

**Syntax:** obj \<\< Fit All Nonnegative

**Description:** Fits all distributions that support nonnegative observations.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit All Nonnegative;
```

#### [Fit Competing Risk Mixture](#fit-competing-risk-mixture)[](#fit-competing-risk-mixture "Click to copy url")

**Syntax:** obj \<\< Fit Competing Risk Mixture( Mix( distribution( n ), \<distribution( n ), ...\>, method, \<Show Profilers( 0\|1 )\>

**Description:** Specifies the distributions and options for a competing risk mixture model. The method argument is required and must be one of the following starting value methods: Single Cluster, Separable Clusters, or Overlapping Clusters.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Devalt.jmp" );
obj = dt << Life Distribution(
    Y( :Hours ),
    Censor( :Status ),
    Censor Code( "Censored" ),
    Freq( :Weight ),
    <<Fit Lognormal
);
obj << Fit Competing Risk Mixture(
    Mix( Lognormal( 2 ), Single Cluster, Show Profilers( 0 ) )
);
```

#### [Fit DS Frechet](#fit-ds-frechet)[](#fit-ds-frechet "Click to copy url")

**Syntax:** obj \<\< Fit DS Frechet

**Description:** Fits a defective subpopulation Fréchet distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit DS Frechet;
```

#### [Fit DS Loglogistic](#fit-ds-loglogistic)[](#fit-ds-loglogistic "Click to copy url")

**Syntax:** obj \<\< Fit DS Loglogistic

**Description:** Fits a defective subpopulation loglogistic distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit DS Loglogistic;
```

#### [Fit DS Lognormal](#fit-ds-lognormal)[](#fit-ds-lognormal "Click to copy url")

**Syntax:** obj \<\< Fit DS Lognormal

**Description:** Fits a defective subpopulation lognormal distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit DS Lognormal;
```

#### [Fit DS Weibull](#fit-ds-weibull)[](#fit-ds-weibull "Click to copy url")

**Syntax:** obj \<\< Fit DS Weibull

**Description:** Fits a defective subpopulation Weibull distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit DS Weibull;
```

#### [Fit Exponential](#fit-exponential)[](#fit-exponential "Click to copy url")

**Syntax:** obj \<\< Fit Exponential

**Description:** Fits an exponential distribution to the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit Exponential;
```

#### [Fit Frechet](#fit-frechet)[](#fit-frechet "Click to copy url")

**Syntax:** obj \<\< Fit Frechet

**Description:** Fits a Fréchet distribution to the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit Frechet;
```

#### [Fit GenGamma](#fit-gengamma)[](#fit-gengamma "Click to copy url")

**Syntax:** obj \<\< Fit GenGamma

**Description:** Fits a generalized gamma distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit GenGamma;
```

#### [Fit LEV](#fit-lev)[](#fit-lev "Click to copy url")

**Syntax:** obj \<\< Fit LEV

**Description:** Fits a largest extreme value (LEV) distribution to the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit LEV;
```

#### [Fit LogGenGamma](#fit-loggengamma)[](#fit-loggengamma "Click to copy url")

**Syntax:** obj \<\< Fit LogGenGamma

**Description:** Fits a log generalized gamma distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit LogGenGamma;
```

#### [Fit Logistic](#fit-logistic)[](#fit-logistic "Click to copy url")

**Syntax:** obj \<\< Fit Logistic

**Description:** Fits a logistic distribution to the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit Logistic;
```

#### [Fit Loglogistic](#fit-loglogistic)[](#fit-loglogistic "Click to copy url")

**Syntax:** obj \<\< Fit Loglogistic

**Description:** Fits a loglogistic distribution to the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit Loglogistic;
```

#### [Fit Lognormal](#fit-lognormal)[](#fit-lognormal "Click to copy url")

**Syntax:** obj \<\< Fit Lognormal

**Description:** Fits a lognormal distribution to the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit Lognormal;
```

#### [Fit Mixture](#fit-mixture)[](#fit-mixture "Click to copy url")

**Syntax:** obj \<\< Fit Mixture( Mix( distribution( n ), \<distribution( n ), ...\>, method, \<Show Profilers( 0\|1 )\>

**Description:** Specifies the distributions and options for a mixture model. The method argument is required and must be one of the following starting value methods: Single Cluster, Separable Clusters, or Overlapping Clusters.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Devalt.jmp" );
obj = dt << Life Distribution(
    Y( :Hours ),
    Censor( :Status ),
    Censor Code( "Censored" ),
    Freq( :Weight ),
    <<Fit Lognormal
);
obj << Fit Mixture( Mix( Lognormal( 2 ), Single Cluster, Show Profilers( 0 ) ) );
```

#### [Fit Normal](#fit-normal)[](#fit-normal "Click to copy url")

**Syntax:** obj \<\< Fit Normal

**Description:** Fits a normal distribution to the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit Normal;
```

#### [Fit SEV](#fit-sev)[](#fit-sev "Click to copy url")

**Syntax:** obj \<\< Fit SEV

**Description:** Fits a smallest extreme value (SEV) distribution to the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit SEV;
```

#### [Fit TH Frechet](#fit-th-frechet)[](#fit-th-frechet "Click to copy url")

**Syntax:** obj \<\< Fit TH Frechet

**Description:** Fits a Fréchet with threshold distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit TH Frechet;
```

#### [Fit TH Loglogistic](#fit-th-loglogistic)[](#fit-th-loglogistic "Click to copy url")

**Syntax:** obj \<\< Fit TH Loglogistic

**Description:** Fits a loglogistic with threshold distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit TH Loglogistic;
```

#### [Fit TH Lognormal](#fit-th-lognormal)[](#fit-th-lognormal "Click to copy url")

**Syntax:** obj \<\< Fit TH Lognormal

**Description:** Fits a lognormal with threshold distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit TH Lognormal;
```

#### [Fit TH Weibull](#fit-th-weibull)[](#fit-th-weibull "Click to copy url")

**Syntax:** obj \<\< Fit TH Weibull

**Description:** Fits a Weibull with threshold distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit TH Weibull;
```

#### [Fit Weibull](#fit-weibull)[](#fit-weibull "Click to copy url")

**Syntax:** obj \<\< Fit Weibull

**Description:** Fits a Weibull distribution to the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Fit Weibull;
```

#### [Fit ZI Frechet](#fit-zi-frechet)[](#fit-zi-frechet "Click to copy url")

**Syntax:** obj \<\< Fit ZI Frechet

**Description:** Fits a zero-inflated Fréchet distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Spring.jmp" );
obj = dt << Life Distribution( Y( :Precip ) );
obj << Fit ZI Frechet;
```

#### [Fit ZI Loglogistic](#fit-zi-loglogistic)[](#fit-zi-loglogistic "Click to copy url")

**Syntax:** obj \<\< Fit ZI Loglogistic

**Description:** Fits a zero-inflated loglogistic distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Spring.jmp" );
obj = dt << Life Distribution( Y( :Precip ) );
obj << Fit ZI Loglogistic;
```

#### [Fit ZI Lognormal](#fit-zi-lognormal)[](#fit-zi-lognormal "Click to copy url")

**Syntax:** obj \<\< Fit ZI Lognormal

**Description:** Fits a zero-inflated lognormal distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Spring.jmp" );
obj = dt << Life Distribution( Y( :Precip ) );
obj << Fit ZI Lognormal;
```

#### [Fit ZI Weibull](#fit-zi-weibull)[](#fit-zi-weibull "Click to copy url")

**Syntax:** obj \<\< Fit ZI Weibull

**Description:** Fits a zero-inflated Weibull distribution to the data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Spring.jmp" );
obj = dt << Life Distribution( Y( :Precip ) );
obj << Fit ZI Weibull;
```

#### [Get Estimates](#get-estimates_1)[](#get-estimates_1 "Click to copy url")

**Syntax:** obj \<\< Get Estimates

**Description:** Returns a list that contains the estimates for all fitted distributions. The list also contains the original data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    Fit Exponential,
    Set Scale( Exponential )
);
estimate = obj << Get Estimates;
Show( estimate );
```

#### [Get Formula](#get-formula)[](#get-formula "Click to copy url")

**Syntax:** obj \<\< Get Formula

**Description:** Returns a list that contains the formulas for all fitted distributions. The list also contains the original data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    Fit Exponential,
    Set Scale( Exponential )
);
formula = obj << Get Formula;
Show( formula );
```

#### [Get Results](#get-results_1)[](#get-results_1 "Click to copy url")

**Syntax:** obj \<\< Get Results

**Description:** Returns a list that contains the results for all fitted distributions. The list also contains the original data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    Fit Exponential,
    Set Scale( Exponential )
);
r = obj << Get Results;
Show( r );
```

#### [Interval Type](#interval-type_1)[](#interval-type_1 "Click to copy url")

**Syntax:** obj \<\< Interval Type( "Simultaneous"\|"Pointwise" )

**Description:** Specifies the type of confidence interval shown for the Nonparametric fit in the Compare Distributions plot. The available options are pointwise or simultaneous confidence intervals.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ), Fit Exponential );
obj << Interval Type( "Pointwise" );
```

#### [Nonparametric Estimate Plot Options](#nonparametric-estimate-plot-options)[](#nonparametric-estimate-plot-options "Click to copy url")

**Syntax:** obj \<\< Nonparametric Estimate Plot Options( "Points"\|"Step Function"\|"Both"\|"None" )

**Description:** Specifies how the data points in the probability plot are represented. You can choose between points, step functions, both points and step functions, or neither.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
Wait( 1 );
obj << Nonparametric Estimate Plot Options( "Step Function" );
```

#### [Rejection Sampler Maximum Trials](#rejection-sampler-maximum-trials)[](#rejection-sampler-maximum-trials "Click to copy url")

**Syntax:** obj \<\< Rejection Sampler Maximum Trials( number=10000 )

**Description:** "10000" by default.

**JMP Version Added:** 14

#### [Save By Group Results](#save-by-group-results)[](#save-by-group-results "Click to copy url")

**Syntax:** obj \<\< Save By Group Results

**Description:** Saves the resulting estimates for all by groups as a separate row in a new table.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Blenders.jmp" );
obj = dt << Life Distribution(
    Y( :Time Cycles ),
    By( :Group ),
    Censor( :Censor ),
    Fit Exponential
);
obj[1] << Save By Group Results;
```

#### [Set Scale](#set-scale_1)[](#set-scale_1 "Click to copy url")

**Syntax:** obj \<\< Set Scale( Linear\|Lognormal\|Weibull\|Loglogistic\|Frechet\|Normal\|SEV\|Logistic\|LEV\|Exponential )

**Description:** Specifies a scale for the probability axis in the Compare Distributions plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ), Fit Exponential );
obj << Set Scale( Exponential );
```

#### [Show Confidence Area](#show-confidence-area_1)[](#show-confidence-area_1 "Click to copy url")

**Syntax:** obj \<\< Show Confidence Area( state=0\|1 )

**Description:** Shows or hides the shaded confidence regions in the plots. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ), Fit Exponential );
Wait( 1 );
obj << Show Confidence Area( 0 );
```

#### [Show Event Plot Frequency Label](#show-event-plot-frequency-label)[](#show-event-plot-frequency-label "Click to copy url")

**Syntax:** obj \<\< Show Event Plot Frequency Label( state=0\|1 )

**Description:** Shows or hides the frequency labels in the Event Plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Microprocessor Data.jmp" );
obj = dt << Life Distribution( Y( :start time, end time ), Freq( :count ) );
Report( obj )["Event Plot"] << Close( 0 );
Wait( 1 );
obj << Show Event Plot Frequency Label( 0 );
```

#### [Show Hazard Functions](#show-hazard-functions_1)[](#show-hazard-functions_1 "Click to copy url")

**Syntax:** obj \<\< Show Hazard Functions( state=0\|1 )

**Description:** Shows or hides the Hazard Profiler report, which overlays the plots of hazard functions for the selected distributions.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ), Fit Exponential );
obj << Show Hazard Functions( 1 );
```

#### [Show Points](#show-points_2)[](#show-points_2 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides data points in the probability plot. The Life Distribution platform uses the midpoint estimates of the step function to construct probability plots. When you deselect the Show Points option, the midpoint estimates are replaced by Kaplan-Meier estimates. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
Wait( 1 );
obj << Show Points( 0 );
```

#### [Show Quantile Functions](#show-quantile-functions_1)[](#show-quantile-functions_1 "Click to copy url")

**Syntax:** obj \<\< Show Quantile Functions( state=0\|1 )

**Description:** Shows or hides the Quantile Profiler report, which overlays the plots of quantile functions for the selected distributions.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ), Fit Exponential );
obj << Show Quantile Functions( 1 );
```

#### [Show Statistics](#show-statistics)[](#show-statistics "Click to copy url")

**Syntax:** obj \<\< Show Statistics( state=0\|1 )

**Description:** Shows or hides the Statistics report, which contains model comparisons, a data summary, and nonparametric and parametric estimates. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ), Fit Exponential );
Wait( 1 );
obj << Show Statistics( 0 );
```

#### [Show Survival Curve](#show-survival-curve_1)[](#show-survival-curve_1 "Click to copy url")

**Syntax:** obj \<\< Show Survival Curve( state=0\|1 )

**Description:** Switches between the failure probability and the survival curve on the Compare Distributions probability plot and the Distribution Profiler plots.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    Show Survival Curve( 1 ),
    Fit Exponential
);
```

#### [Suppress Plot](#suppress-plot)[](#suppress-plot "Click to copy url")

**Syntax:** obj \<\< Suppress Plot( distribution name )

**Description:** Removes the specified distribution from the plots in the report. This option is equivalent to unchecking the corresponding box under Distribution in the Compare Distributions, Hazard Profiler, or Quantile Profiler reports.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Fit Weibull, Fit Lognormal, Set Scale( Weibull ) );
Wait( 2 );
obj << Suppress Plot( Lognormal );
```

#### [Tabbed Report](#tabbed-report_2)[](#tabbed-report_2 "Click to copy url")

**Syntax:** obj \<\< Tabbed Report( state=0\|1 )

**Description:** Shows graphs and data in individual tabs rather than in the default outline style.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ), Fit Exponential );
obj << Tabbed Report( 1 );
```

### [Shared Item Messages](#shared-item-messages_2)[](#shared-item-messages_2 "Click to copy url")

#### [Action](#action_2)[](#action_2 "Click to copy url")

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

#### [Apply Preset](#apply-preset_2)[](#apply-preset_2 "Click to copy url")

**Syntax:** Apply Preset( preset ); Apply Preset( source, label, \<Folder( folder {, folder2, ...} )\> )

**Description:** Apply a previously created preset to the object, updating the options and customizations to match the saved settings.

**JMP Version Added:** 18

**Anonymous preset**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
dt2 = Open( "$SAMPLE_DATA/Dogs.jmp" );
obj2 = dt2 << Oneway( Y( :LogHist0 ), X( :drug ) );
Wait( 1 );
obj2 << Apply Preset( preset );
```

**Search by name**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "Compare Distributions" );
```

**Search within folder(s)**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "t-Tests", Folder( "Compare Means" ) );
```

#### [Automatic Recalc](#automatic-recalc_2)[](#automatic-recalc_2 "Click to copy url")

**Syntax:** obj \<\< Automatic Recalc( state=0\|1 )

**Description:** Redoes the analysis automatically for exclude and data changes. If the Automatic Recalc option is turned on, you should consider using Wait(0) commands to ensure that the exclude and data changes take effect before the recalculation.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Automatic Recalc( 1 );
dt << Select Rows( 5 ) << Exclude( 1 );
```

#### [Broadcast](#broadcast_2)[](#broadcast_2 "Click to copy url")

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

#### [Column Switcher](#column-switcher_2)[](#column-switcher_2 "Click to copy url")

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

#### [Copy ByGroup Script](#copy-bygroup-script_2)[](#copy-bygroup-script_2 "Click to copy url")

**Syntax:** obj \<\< Copy ByGroup Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Copy ByGroup Script;
```

#### [Copy Script](#copy-script_2)[](#copy-script_2 "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Copy Script;
```

#### [Data Table Window](#data-table-window_2)[](#data-table-window_2 "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Data Table Window;
```

#### [Get By Levels](#get-by-levels_2)[](#get-by-levels_2 "Click to copy url")

**Syntax:** obj \<\< Get By Levels

**Description:** Returns an associative array mapping the by group columns to their values.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv << Get By Levels;
```

#### [Get ByGroup Script](#get-bygroup-script_2)[](#get-bygroup-script_2 "Click to copy url")

**Syntax:** obj \<\< Get ByGroup Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
t = obj[1] << Get ByGroup Script;
Show( t );
```

#### [Get Container](#get-container_2)[](#get-container_2 "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

**General**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
t = obj << Get Container;
Show( (t << XPath( "//OutlineBox" )) << Get Title );
```

**Platform with Filter**

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

#### [Get Data Table](#get-data-table_2)[](#get-data-table_2 "Click to copy url")

**Syntax:** obj \<\< Get Data Table

**Description:** Returns a reference to the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
t = obj << Get Datatable;
Show( N Rows( t ) );
```

#### [Get Group Platform](#get-group-platform_2)[](#get-group-platform_2 "Click to copy url")

**Syntax:** obj \<\< Get Group Platform

**Description:** Return the Group Platform object if this platform is part of a Group. Otherwise, returns Empty().

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( Y( :weight ), X( :height ), By( :sex ) );
group = biv[1] << Get Group Platform;
Wait( 1 );
group << Layout( "Arrange in Tabs" );
```

#### [Get Script](#get-script_2)[](#get-script_2 "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
t = obj << Get Script;
Show( t );
```

#### [Get Script With Data Table](#get-script-with-data-table_2)[](#get-script-with-data-table_2 "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
t = obj << Get Script With Data Table;
Show( t );
```

#### [Get Timing](#get-timing_2)[](#get-timing_2 "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
t = obj << Get Timing;
Show( t );
```

#### [Get Web Support](#get-web-support_2)[](#get-web-support_2 "Click to copy url")

**Syntax:** obj \<\< Get Web Support

**Description:** Return a number indicating the level of Interactive HTML support for the display object. 1 means some or all elements are supported. 0 means no support.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
s = obj << Get Web Support();
Show( s );
```

#### [Get Where Expr](#get-where-expr_2)[](#get-where-expr_2 "Click to copy url")

**Syntax:** obj \<\< Get Where Expr

**Description:** Returns the Where expression for the data subset, if the platform was launched with By() or Where(). Otherwise, returns Empty()

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv2 = dt << Bivariate( X( :height ), Y( :weight ), Where( :age < 14 & :height > 60 ) );
Show( biv[1] << Get Where Expr, biv2 << Get Where Expr );
```

#### [Ignore Platform Preferences](#ignore-platform-preferences_2)[](#ignore-platform-preferences_2 "Click to copy url")

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

#### [Local Data Filter](#local-data-filter_2)[](#local-data-filter_2 "Click to copy url")

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

#### [New Preset](#new-preset_2)[](#new-preset_2 "Click to copy url")

**Syntax:** obj = New Preset()

**Description:** Create an anonymous preset representing the options and customizations applied to the object. This object can be passed to Apply Preset to copy the settings to another object of the same type.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
```

#### [Paste Local Data Filter](#paste-local-data-filter_2)[](#paste-local-data-filter_2 "Click to copy url")

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

#### [Redo Analysis](#redo-analysis_2)[](#redo-analysis_2 "Click to copy url")

**Syntax:** obj \<\< Redo Analysis

**Description:** Rerun this same analysis in a new window. The analysis will be different if the data has changed.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Redo Analysis;
```

#### [Relaunch Analysis](#relaunch-analysis_2)[](#relaunch-analysis_2 "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Relaunch Analysis;
```

#### [Remove Column Switcher](#remove-column-switcher_2)[](#remove-column-switcher_2 "Click to copy url")

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

#### [Remove Local Data Filter](#remove-local-data-filter_2)[](#remove-local-data-filter_2 "Click to copy url")

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

#### [Report](#report_2)[](#report_2 "Click to copy url")

**Syntax:** obj \<\< Report; Report( obj )

**Description:** Returns a reference to the report object.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

#### [Report View](#report-view_2)[](#report-view_2 "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Report View( "Summary" );
```

#### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table_2)[](#save-bygroup-script-to-data-table_2 "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Data Table;
```

#### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal_2)[](#save-bygroup-script-to-journal_2 "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Journal;
```

#### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window_2)[](#save-bygroup-script-to-script-window_2 "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Script Window;
```

#### [Save Script for All Objects](#save-script-for-all-objects_2)[](#save-script-for-all-objects_2 "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Save Script for All Objects;
```

#### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table_2)[](#save-script-for-all-objects-to-data-table_2 "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

#### [Save Script to Data Table](#save-script-to-data-table_2)[](#save-script-to-data-table_2 "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

#### [Save Script to Journal](#save-script-to-journal_2)[](#save-script-to-journal_2 "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Save Script to Journal;
```

#### [Save Script to Report](#save-script-to-report_2)[](#save-script-to-report_2 "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Save Script to Report;
```

#### [Save Script to Script Window](#save-script-to-script-window_2)[](#save-script-to-script-window_2 "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Save Script to Script Window;
```

#### [SendToByGroup](#sendtobygroup_2)[](#sendtobygroup_2 "Click to copy url")

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

#### [SendToEmbeddedScriptable](#sendtoembeddedscriptable_2)[](#sendtoembeddedscriptable_2 "Click to copy url")

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

#### [SendToReport](#sendtoreport_2)[](#sendtoreport_2 "Click to copy url")

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

#### [Sync to Data Table Changes](#sync-to-data-table-changes_2)[](#sync-to-data-table-changes_2 "Click to copy url")

**Syntax:** obj \<\< Sync to Data Table Changes

**Description:** Sync with the exclude and data changes that have been made.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dist = Distribution( Continuous Distribution( Column( :POP ) ) );
Wait( 1 );
dt << Delete Rows( dt << Get Rows Where( :Region == "W" ) );
dist << Sync To Data Table Changes;
```

#### [Title](#title_2)[](#title_2 "Click to copy url")

**Syntax:** obj \<\< Title( "new title" )

**Description:** Sets the title of the platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
obj << Title( "My Platform" );
```

#### [Top Report](#top-report_2)[](#top-report_2 "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
r = obj << Top Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

#### [Transform Column](#transform-column_2)[](#transform-column_2 "Click to copy url")

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

#### [View Web XML](#view-web-xml_2)[](#view-web-xml_2 "Click to copy url")

**Syntax:** obj \<\< View Web XML

**Description:** Returns the XML code that is used to create the interactive HTML report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
xml = obj << View Web XML;
```

#### [Window View](#window-view_2)[](#window-view_2 "Click to copy url")

**Syntax:** obj = Life Distribution(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

[ Previous](Legend%20Model.html "Legend Model") [Next ](Loading%20Bar%20Plot.html "Loading Bar Plot")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
