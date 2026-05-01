# XGBoost

*Source: [https://jsl.jmp.com/All%20Categories/Objects/XGBoost.html](https://jsl.jmp.com/All%20Categories/Objects/XGBoost.html)*

---

# [XGBoost](#xgboost)[](#xgboost "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [XGBoost](#xgboost_1)[](#xgboost_1 "Click to copy url")

**Syntax:** XGBoost(Y( columns ), X( columns ))

**Description:** Predictive modeling interface to eXtreme Gradient Boosted trees.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

## [Columns](#columns)[](#columns "Click to copy url")

### [Censor](#censor)[](#censor "Click to copy url")

**Syntax:** obj = XGBoost(...\<Censor( column )\>...)

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

### [Factor](#factor)[](#factor "Click to copy url")

**Syntax:** obj = XGBoost(...Factor( column(s) )...)

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj = XGBoost(...\<Freq( column )\>...)

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

### [Response](#response)[](#response "Click to copy url")

**Syntax:** obj = XGBoost(...Response( column(s) )...)

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

### [Validation](#validation)[](#validation "Click to copy url")

**Syntax:** obj = XGBoost(...\<Validation( column(s) )\>...)

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

### [Weight](#weight)[](#weight "Click to copy url")

**Syntax:** obj = XGBoost(...\<Weight( column )\>...)

**Description:** Specifies a column whose values assign a weight to each row for the analysis.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_weightcol", Numeric, Continuous, Set Each Value( Random Beta( 1, 1 ) ) );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** obj = XGBoost(...X( column(s) )...)

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj = XGBoost(...Y( column(s) )...)

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Change Variables](#change-variables)[](#change-variables "Click to copy url")

**Syntax:** obj \<\< Change Variables

**Description:** Changes X, Y, and other variables for subsequent models.

**JMP Version Added:** 16

### [Compare](#compare)[](#compare "Click to copy url")

**Syntax:** obj \<\< Compare

**Description:** Updates the XGBoost comparison metrics.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit( Objective( 0 ) ) );
obj << Compare( Correlation( 1 ) );
```

### [Fit](#fit)[](#fit "Click to copy url")

**Syntax:** obj \<\< Fit

**Description:** Fits an XGBoost model. You can specify XGBoost parameters and fitting specifications within this.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
```

### [Get Measures](#get-measures)[](#get-measures "Click to copy url")

**Syntax:** obj \<\< Get Measures

**JMP Version Added:** 16

### [Method](#method)[](#method "Click to copy url")

**Syntax:** obj \<\< Method( "xgboost"\|"lightgbm"="xgboost" )

**Description:** Select either XGBoost or LightGBM as a method for gradient boosting fitting. "xgboost" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost(
    Y( :Weight ),
    X( :Height ),
    Fit( Method( "lightgbm" ), objective( "regression" ) )
);
```

### [Redo Analysis](#redo-analysis)[](#redo-analysis "Click to copy url")

**Syntax:** obj \<\< Redo Analysis

**Description:** Rerun this same analysis in a new window. The analysis will be different if the data has changed.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj << Relaunch Analysis;
```

### [Show Details](#show-details)[](#show-details "Click to copy url")

**Syntax:** obj \<\< Show Details( state=0\|1 )

**Description:** Shows more details.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Show Details( 1 ) );
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

### [Copy ByGroup Script](#copy-bygroup-script)[](#copy-bygroup-script "Click to copy url")

**Syntax:** obj \<\< Copy ByGroup Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj << Copy Script;
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
t = obj[1] << Get ByGroup Script;
Show( t );
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
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

### [Report](#report)[](#report "Click to copy url")

**Syntax:** obj \<\< Report; Report( obj )

**Description:** Returns a reference to the report object.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
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

### [Title](#title)[](#title "Click to copy url")

**Syntax:** obj \<\< Title( "new title" )

**Description:** Sets the title of the platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << XGBoost( Y( :Weight ), X( :Height ), Fit );
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

## [XGBoost Compare](#xgboost-compare)[](#xgboost-compare "Click to copy url")

### [Associated Constructors](#associated-constructors_1)[](#associated-constructors_1 "Click to copy url")

#### [XGBoost Compare](#xgboost-compare_1)[](#xgboost-compare_1 "Click to copy url")

**Syntax:** XGBoost Compare

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [AUC](#auc)[](#auc "Click to copy url")

**Syntax:** obj \<\< AUC( state=0\|1 )

**Description:** Shows or hides the AUROC, which is the area under the receiver operating characteristic curve. On by default.

**JMP Version Added:** 16

#### [AUPRC](#auprc)[](#auprc "Click to copy url")

**Syntax:** obj \<\< AUPRC( state=0\|1 )

**Description:** Area under the Precision Recall Curve On by default.

**JMP Version Added:** 17

#### [Accuracy](#accuracy)[](#accuracy "Click to copy url")

**Syntax:** obj \<\< Accuracy( state=0\|1 )

**Description:** Shows or hides the accuracy, which is the proportion of correct classifications. On by default.

**JMP Version Added:** 15

#### [Censor](#censor_1)[](#censor_1 "Click to copy url")

**Syntax:** obj \<\< Censor( state=0\|1 )

**Description:** Shows or hides the Censor command On by default.

**JMP Version Added:** 17

#### [Concordance](#concordance)[](#concordance "Click to copy url")

**Syntax:** obj \<\< Concordance( state=0\|1 )

**Description:** Shows or hides the concordance, which is the Harrell C-Index and measures strength of sorting efficiency On by default.

**JMP Version Added:** 17

#### [Correlation](#correlation)[](#correlation "Click to copy url")

**Syntax:** obj \<\< Correlation( state=0\|1 )

**Description:** Shows or hides the Pearson correlation, which is a measure of the strength of the linear relationship. On by default.

**JMP Version Added:** 15

#### [F1](#f1)[](#f1 "Click to copy url")

**Syntax:** obj \<\< F1( state=0\|1 )

**Description:** Shows or hides the F1 Score, which is the harmonic average of precision and recall. On by default.

**JMP Version Added:** 15

#### [Features](#features)[](#features "Click to copy url")

**Syntax:** obj \<\< Features( state=0\|1 )

**Description:** Shows or hides the Features column. On by default.

**JMP Version Added:** 16

#### [Freq](#freq_1)[](#freq_1 "Click to copy url")

**Syntax:** obj \<\< Freq( state=0\|1 )

**Description:** Shows or hides the Freq column. On by default.

**JMP Version Added:** 16

#### [H Measure](#h-measure)[](#h-measure "Click to copy url")

**Syntax:** obj \<\< H Measure( state=0\|1 )

**Description:** Shows or hides the H Measure, which measures proportion improvement over baseline. On by default.

**JMP Version Added:** 17

#### [Hide All Models](#hide-all-models)[](#hide-all-models "Click to copy url")

**Syntax:** obj \<\< Hide All Models

**Description:** Hides all models.

**JMP Version Added:** 16

#### [LogLoss](#logloss)[](#logloss "Click to copy url")

**Syntax:** obj \<\< LogLoss( state=0\|1 )

**Description:** Shows or hides the logarithm of the likelihood-based loss function. On by default.

**JMP Version Added:** 15

#### [MAE](#mae)[](#mae "Click to copy url")

**Syntax:** obj \<\< MAE( state=0\|1 )

**Description:** Shows or hides the MAE, which is the mean absolute error. On by default.

**JMP Version Added:** 15

#### [MCC](#mcc)[](#mcc "Click to copy url")

**Syntax:** obj \<\< MCC( state=0\|1 )

**Description:** Shows or hides the Matthews correlation coefficient, which is the Pearson correlation for binary variables. On by default.

**JMP Version Added:** 15

#### [Misclass](#misclass)[](#misclass "Click to copy url")

**Syntax:** obj \<\< Misclass( state=0\|1 )

**Description:** Shows or hides the misclassification rate, which is the proportion of incorrect classifications. On by default.

**JMP Version Added:** 15

#### [Predictors](#predictors)[](#predictors "Click to copy url")

**Syntax:** obj \<\< Predictors( state=0\|1 )

**Description:** Shows or hides the Predictors column. On by default.

**JMP Version Added:** 16

#### [Profit](#profit)[](#profit "Click to copy url")

**Syntax:** obj \<\< Profit( state=0\|1 )

**Description:** Shows or hides the expected profit. On by default.

**JMP Version Added:** 16

#### [RMSE](#rmse)[](#rmse "Click to copy url")

**Syntax:** obj \<\< RMSE( state=0\|1 )

**Description:** Shows or hides the RMSE, which is the root mean square error. On by default.

**JMP Version Added:** 15

#### [RSquare](#rsquare)[](#rsquare "Click to copy url")

**Syntax:** obj \<\< RSquare( state=0\|1 )

**Description:** Shows or hides RSquare value, which is the proportion of variability explained. On by default.

**JMP Version Added:** 15

#### [Remove Hidden Models](#remove-hidden-models)[](#remove-hidden-models "Click to copy url")

**Syntax:** obj \<\< Remove Hidden Models

**Description:** Removes all models for which the Show box is not checked.

**JMP Version Added:** 16

#### [Remove Shown Models](#remove-shown-models)[](#remove-shown-models "Click to copy url")

**Syntax:** obj \<\< Remove Shown Models

**Description:** Removes all models for which the Show check box is checked and shows the remaining models.

**JMP Version Added:** 15

#### [Response](#response_1)[](#response_1 "Click to copy url")

**Syntax:** obj \<\< Response( state=0\|1 )

**Description:** Shows or hides the Response column. On by default.

**JMP Version Added:** 16

#### [Show All Models](#show-all-models)[](#show-all-models "Click to copy url")

**Syntax:** obj \<\< Show All Models

**Description:** Shows all models.

**JMP Version Added:** 16

#### [Training Metrics](#training-metrics)[](#training-metrics "Click to copy url")

**Syntax:** obj \<\< Training Metrics( state=0\|1 )

**Description:** Shows or hides all training metrics. On by default.

**JMP Version Added:** 15

#### [Validation](#validation_1)[](#validation_1 "Click to copy url")

**Syntax:** obj \<\< Validation( state=0\|1 )

**Description:** Shows or hides the Validation column. On by default.

**JMP Version Added:** 16

#### [Validation Metrics](#validation-metrics)[](#validation-metrics "Click to copy url")

**Syntax:** obj \<\< Validation Metrics( state=0\|1 )

**Description:** Shows or hides all validation metrics. On by default.

**JMP Version Added:** 15

#### [Weight](#weight_1)[](#weight_1 "Click to copy url")

**Syntax:** obj \<\< Weight( state=0\|1 )

**Description:** Shows or hides the Weight column. On by default.

**JMP Version Added:** 16

## [XGBoost Fit](#xgboost-fit)[](#xgboost-fit "Click to copy url")

### [Associated Constructors](#associated-constructors_2)[](#associated-constructors_2 "Click to copy url")

#### [XGBoost Fit](#xgboost-fit_1)[](#xgboost-fit_1 "Click to copy url")

**Syntax:** XGBoost Fit

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Actual by Predicted Plots](#actual-by-predicted-plots)[](#actual-by-predicted-plots "Click to copy url")

**Syntax:** obj \<\< Actual by Predicted Plots( state=0\|1 )

**Description:** Shows or hides a plot using the training data with the predicted values on the X axis and actual values on the Y axis. On by default.

**JMP Version Added:** 15

#### [Autotune](#autotune)[](#autotune "Click to copy url")

**Syntax:** obj \<\< Autotune( state=0 )

**Description:** Creates a fast flexible filling design within min and max parameter settings to fit n models, where n is Number of Runs. "0" by default.

**JMP Version Added:** 17

#### [Confusion Matrices](#confusion-matrices)[](#confusion-matrices "Click to copy url")

**Syntax:** obj \<\< ( fit\[number\] \<\< Confusion Matrices( state=0\|1 ) )

**Description:** Shows or hides a crosstabulation matrix of actual and predicted levels. On by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << XGBoost(
    Y( :Species ),
    X( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    Fit
);
obj << (fit[1] << Confusion Matrices( 1 ));
```

#### [Contour Profiler](#contour-profiler)[](#contour-profiler "Click to copy url")

**Syntax:** obj \<\< Contour Profiler

**Description:** Shows or hides interactive graphs of cross-sections of the prediction function.

**JMP Version Added:** 15

#### [Copy Parameters to Launch](#copy-parameters-to-launch)[](#copy-parameters-to-launch "Click to copy url")

**Syntax:** obj \<\< Copy Parameters to Launch

**Description:** Copies the parameters from this model to the model launch section.

**JMP Version Added:** 16

#### [Decision Thresholds](#decision-thresholds)[](#decision-thresholds "Click to copy url")

**Syntax:** obj \<\< Decision Thresholds( state=0\|1 )

**Description:** Shows or hides decision threshold graphs and tables. On by default.

**JMP Version Added:** 16

#### [Fit Details](#fit-details)[](#fit-details "Click to copy url")

**Syntax:** obj \<\< Fit Details( state=0\|1 )

**Description:** Shows or hides the statistics for the fitted model. On by default.

**JMP Version Added:** 15

#### [Generate Python Code](#generate-python-code)[](#generate-python-code "Click to copy url")

**Syntax:** obj \<\< Generate Python Code

**Description:** Creates Python code for training and scoring.

**JMP Version Added:** 16

#### [Importances](#importances)[](#importances "Click to copy url")

**Syntax:** obj \<\< Importances( state=0\|1 )

**Description:** Shows or hides the importance statistics for each predictor. On by default.

**JMP Version Added:** 15

#### [Lift Curves](#lift-curves)[](#lift-curves "Click to copy url")

**Syntax:** obj \<\< Lift Curves( state=0\|1 )

**Description:** Shows or hides the Lift Curve plot. A lift curve plots the lift versus the portion of the observations and provides another view of the predictive ability of a model.

**JMP Version Added:** 15

#### [Number of Design Points](#number-of-design-points)[](#number-of-design-points "Click to copy url")

**Syntax:** obj \<\< Number of Design Points( number=10 )

**Description:** Specifies the number of tuning design runs to perform. If you have a large problem, keep this value relatively small. "10" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( Number of Design Points( 10 ) ) );
```

#### [Number of Inner Folds](#number-of-inner-folds)[](#number-of-inner-folds "Click to copy url")

**Syntax:** obj \<\< Number of Inner Folds( number=2 )

**Description:** Specifies the number of nested inner folds used during the autotune process. "2" by default.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( Number of Inner Folds( 2 ) ) );
```

#### [Precision Recall Curves](#precision-recall-curves)[](#precision-recall-curves "Click to copy url")

**Syntax:** obj \<\< Precision Recall Curves( state=0\|1 )

**Description:** Plots the trade-off between precision and recall for different classification thresholds. It is preferred in scenarios where class imbalances exist.

**JMP Version Added:** 15

#### [Profiler](#profiler)[](#profiler "Click to copy url")

**Syntax:** obj \<\< Profiler

**Description:** Shows or hides the prediction profiler, which is used to graphically explore the prediction equation by slicing it one factor at a time. The prediction profiler contains features for optimization.

**JMP Version Added:** 15

#### [Publish Prediction Formula](#publish-prediction-formula)[](#publish-prediction-formula "Click to copy url")

**Syntax:** obj \<\< Publish Prediction Formula

**Description:** Creates prediction formulas and saves them as formula column scripts in the Formula Depot platform.

**JMP Version Added:** 15

#### [ROC Curves](#roc-curves)[](#roc-curves "Click to copy url")

**Syntax:** obj \<\< ROC Curves( state=0\|1 )

**Description:** Shows or hides the Receiver Operating Characteristic (ROC) curve for each level of the response variable. The ROC curve is a plot of sensitivity versus (1 - specificity).

**JMP Version Added:** 15

#### [Remove All But This Fit](#remove-all-but-this-fit)[](#remove-all-but-this-fit "Click to copy url")

**Syntax:** obj \<\< ( fit\[number\] \<\< Remove All But This Fit )

**Description:** Removes the reports and plots for all models except this one.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << XGBoost(
    Y( :Species ),
    X( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    Fit
);
Wait( 2 );
obj << (Fit[1] << Remove All But This Fit);
```

#### [Remove Fit](#remove-fit)[](#remove-fit "Click to copy url")

**Syntax:** obj \<\< ( fit\[number\] \<\< Remove Fit )

**Description:** Removes the entire model report.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << XGBoost(
    Y( :Species ),
    X( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    Fit
);
Wait( 2 );
obj << (Fit[1] << Remove Fit);
```

#### [Save Predicteds](#save-predicteds)[](#save-predicteds "Click to copy url")

**Syntax:** obj \<\< Save Predicteds

**Description:** Saves the predicted values in a new column in the data table.

**JMP Version Added:** 15

#### [Save Prediction Formula](#save-prediction-formula)[](#save-prediction-formula "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the prediction formula in a new column in the data table. Calculations can be slow for large models.

**JMP Version Added:** 15

#### [Save SHAPs](#save-shaps)[](#save-shaps "Click to copy url")

**Syntax:** obj \<\< Save SHAPs

**Description:** Saves Shapley values to the data table. These values break down predictions into components for each predictor.

**JMP Version Added:** 17

#### [Set Random Seed](#set-random-seed)[](#set-random-seed "Click to copy url")

**Syntax:** obj \<\< Set Random Seed( number=0 )

**Description:** Sets the random seed to a specific value assuring that all subsequent runs using the same seed are reproducible. "0" by default.

**JMP Version Added:** 19

#### [Surface Profiler](#surface-profiler)[](#surface-profiler "Click to copy url")

**Syntax:** obj \<\< Surface Profiler

**Description:** Shows or hides interactive graphs of cross-sections of the prediction function.

**JMP Version Added:** 15

#### [Tree Details](#tree-details)[](#tree-details "Click to copy url")

**Syntax:** obj \<\< Tree Details( state=0\|1 )

**Description:** Shows or hides the breakdown of each tree split.

**JMP Version Added:** 15

#### [Tuning Design Table](#tuning-design-table)[](#tuning-design-table "Click to copy url")

**Syntax:** Tuning Design Table( "table name" )

**Description:** Specifies the name of an open JMP data table of parameter settings used to fit a series of models. The columns of this table must exactly match parameter names, and each row must contain values of these parameters to use for that model fit. Parameters that are not specified are set to their values from this dialog.

**JMP Version Added:** 15

#### [alpha](#alpha)[](#alpha "Click to copy url")

**Syntax:** obj \<\< alpha( number=0.0 )

**Description:** Specifies the L1 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "0.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( alpha( 0.0 ) ) );
```

#### [alpha_max](#alpha_max)[](#alpha_max "Click to copy url")

**Syntax:** obj \<\< alpha_max( number=0.5 )

**Description:** Specifies the maximum L1 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "0.5" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( alpha_max( 2.0 ) ) );
```

#### [alpha_min](#alpha_min)[](#alpha_min "Click to copy url")

**Syntax:** obj \<\< alpha_min( number=0.0 )

**Description:** Specifies the minimum L1 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "0.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( alpha_min( 0.0 ) ) );
```

#### [bagging_by_query](#bagging_by_query)[](#bagging_by_query "Click to copy url")

**Syntax:** obj \<\< bagging_by_query( state=0 )

**Description:** Specifies whether to force rowwise histogram building. Enabling this option reduces memory cost, especially for data that have many samples and are associated with small bagging fraction or GOSS sample strategy. This option cannot be used together with force columnwise. "0" by default.

**JMP Version Added:** 19

#### [bagging_fraction](#bagging_fraction)[](#bagging_fraction "Click to copy url")

**Syntax:** obj \<\< bagging_fraction( number=1 )

**Description:** Specifies the proportion of rows to sample during each iteration. This value must be between 0 and 1. This is a type of bagging. "1" by default.

**JMP Version Added:** 19

#### [bagging_fraction_max](#bagging_fraction_max)[](#bagging_fraction_max "Click to copy url")

**Syntax:** obj \<\< bagging_fraction_max( number=1.0 )

**Description:** Specifies the maximum proportion of rows to sample during each iteration. This value must be between 0 and 1. This is a type of bagging. "1.0" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( bagging_fraction_max( 1.0 ) ) );
```

#### [bagging_fraction_min](#bagging_fraction_min)[](#bagging_fraction_min "Click to copy url")

**Syntax:** obj \<\< bagging_fraction_min( number=0.3 )

**Description:** Specifies the minimum proportion of rows to sample during each iteration. This value must be between 0 and 1. This is a type of bagging. "0.3" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( bagging_fraction_min( 0.3 ) ) );
```

#### [bagging_freq](#bagging_freq)[](#bagging_freq "Click to copy url")

**Syntax:** obj \<\< bagging_freq( number=0 )

**Description:** Specifies the frequency of bagging. This value determines the number of iterations at which a new random sample of training data is drawn to train the model. "0" by default.

**JMP Version Added:** 19

#### [bagging_seed](#bagging_seed)[](#bagging_seed "Click to copy url")

**Syntax:** obj \<\< bagging_seed( number=3 )

**Description:** Specifies the seed that is used for the bagging random number generator. "3" by default.

**JMP Version Added:** 19

#### [base_score](#base_score)[](#base_score "Click to copy url")

**Syntax:** obj \<\< base_score( number=0.5 )

**Description:** Specifies the initial prediction score of all instances, which is the global bias. The mean of y is typically a good choice. "0.5" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( base_score( 0.5 ) ) );
```

#### [bin_construct_sample_cnt](#bin_construct_sample_cnt)[](#bin_construct_sample_cnt "Click to copy url")

**Syntax:** obj \<\< bin_construct_sample_cnt( number=200000 )

**Description:** Specifies the number of observations that are sampled to construct feature discrete bins. If this option is set to small values, you might encounter unexpected errors and poor accuracy. "200000" by default.

**JMP Version Added:** 19

#### [boost_from_average](#boost_from_average)[](#boost_from_average "Click to copy url")

**Syntax:** obj \<\< boost_from_average( state=1 )

**Description:** Specifies whether the initial prediction is set to the average of the response variable or to a constant zero. This option is used only in regression, binary, multiclass, and cross-entropy objectives. On by default.

**JMP Version Added:** 19

#### [booster](#booster)[](#booster "Click to copy url")

**Syntax:** obj \<\< booster( "gbtree"\|"gblinear"\|"dart"="gbtree" )

**Description:** Specifies which booster to use. "gbtree" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( booster( "gbtree" ) ) );
```

#### [boosting](#boosting)[](#boosting "Click to copy url")

**Syntax:** obj \<\< boosting( "gbdt"\|"rf"\|"dart"="gbdt" )

**Description:** Specifies the boosting strategy that is used during model training. "gbdt" by default.

**JMP Version Added:** 19

#### [cat_l2](#cat_l2)[](#cat_l2 "Click to copy url")

**Syntax:** obj \<\< cat_l2( number=10 )

**Description:** Specifies the L2 regularization value for categorical features. "10" by default.

**JMP Version Added:** 19

#### [cat_l2_max](#cat_l2_max)[](#cat_l2_max "Click to copy url")

**Syntax:** obj \<\< cat_l2_max( number=15 )

**Description:** Specifies the maximum L2 regularization value for categorical features. "15" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( cat_l2_max( 2.0 ) ) );
```

#### [cat_l2_min](#cat_l2_min)[](#cat_l2_min "Click to copy url")

**Syntax:** obj \<\< cat_l2_min( number=5 )

**Description:** Specifies the minimum L2 regularization value for categorical features. "5" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( cat_l2_min( 0.0 ) ) );
```

#### [cat_smooth](#cat_smooth)[](#cat_smooth "Click to copy url")

**Syntax:** obj \<\< cat_smooth( number=10 )

**Description:** Specifies the regularization value that is used to reduce the impact of noise in categorical features, especially for those categories with few observations. "10" by default.

**JMP Version Added:** 19

#### [cegb_penalty_split](#cegb_penalty_split)[](#cegb_penalty_split "Click to copy url")

**Syntax:** obj \<\< cegb_penalty_split( number=0 )

**Description:** "0" by default.

**JMP Version Added:** 19

#### [cegb_tradeoff](#cegb_tradeoff)[](#cegb_tradeoff "Click to copy url")

**Syntax:** obj \<\< cegb_tradeoff( number=1 )

**Description:** "1" by default.

**JMP Version Added:** 19

#### [colsample_bylevel](#colsample_bylevel)[](#colsample_bylevel "Click to copy url")

**Syntax:** obj \<\< colsample_bylevel( number=1.0 )

**Description:** Specifies the proportion of columns to sample for each level. Sampling occurs once for every new depth level reached in a tree. "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( colsample_bylevel( 1.0 ) ) );
```

#### [colsample_bynode](#colsample_bynode)[](#colsample_bynode "Click to copy url")

**Syntax:** obj \<\< colsample_bynode( number=1.0 )

**Description:** Specifies the proportion of columns to sample for each node (split). Sampling occurs once every time a new split is evaluated. "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( colsample_bynode( 1.0 ) ) );
```

#### [colsample_bytree](#colsample_bytree)[](#colsample_bytree "Click to copy url")

**Syntax:** obj \<\< colsample_bytree( number=1.0 )

**Description:** Specifies the proportion of columns to sample when constructing each tree. Sampling occurs once for each tree. This value must be between 0 and 1. "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( colsample_bytree( 1.0 ) ) );
```

#### [colsample_bytree_max](#colsample_bytree_max)[](#colsample_bytree_max "Click to copy url")

**Syntax:** obj \<\< colsample_bytree_max( number=1.0 )

**Description:** Specifies the maximum proportion of columns to sample when constructing each tree. Sampling occurs once for each tree. This value must be between 0 and 1. "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( colsample_bytree_max( 1.0 ) ) );
```

#### [colsample_bytree_min](#colsample_bytree_min)[](#colsample_bytree_min "Click to copy url")

**Syntax:** obj \<\< colsample_bytree_min( number=0.5 )

**Description:** Specifies the minimum proportion of columns to sample when constructing each tree. Sampling occurs once for each tree. This value must be between 0 and 1. "0.5" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( colsample_bytree_min( 0.3 ) ) );
```

#### [data_random_seed](#data_random_seed)[](#data_random_seed "Click to copy url")

**Syntax:** obj \<\< data_random_seed( number=1 )

**Description:** Specifies the seed that is used for the random number generator when sampling data to construct histogram bins. "1" by default.

**JMP Version Added:** 19

#### [data_sample_strategy](#data_sample_strategy)[](#data_sample_strategy "Click to copy url")

**Syntax:** obj \<\< data_sample_strategy( "bagging"\|"goss"="bagging" )

**Description:** Specifies the strategy for drawing samples for usage on each boosting iteration. "bagging" by default.

**JMP Version Added:** 19

#### [deterministic](#deterministic)[](#deterministic "Click to copy url")

**Syntax:** obj \<\< deterministic( state=0 )

**Description:** Specifies that results can be reproduced. Setting this option to true ensures stable results when using different numbers of threads for the same data samples and parameters. This option is useful for reproducibility. "0" by default.

**JMP Version Added:** 19

#### [device_type](#device_type)[](#device_type "Click to copy url")

**Syntax:** obj \<\< device_type( "cpu"\|"gpu"="cpu" )

**Description:** Specifies whether to use the CPU or GPU device. "cpu" by default.

**JMP Version Added:** 19

#### [drop_rate](#drop_rate)[](#drop_rate "Click to copy url")

**Syntax:** obj \<\< drop_rate( number=0.1 )

**Description:** Specifies the fraction of previous trees to drop during the dropout for DART boosting. "0.1" by default.

**JMP Version Added:** 19

#### [drop_seed](#drop_seed)[](#drop_seed "Click to copy url")

**Syntax:** obj \<\< drop_seed( number=4 )

**Description:** Specifies the seed that is used for the dropout procedure in DART boosting. "4" by default.

**JMP Version Added:** 19

#### [early_stopping_min_delta](#early_stopping_min_delta)[](#early_stopping_min_delta "Click to copy url")

**Syntax:** obj \<\< early_stopping_min_delta( number=0 )

**Description:** Specifies the minimum value by which the training metric must improve on each iteration. Otherwise, the training process stops when using an early stopping round. "0" by default.

**JMP Version Added:** 19

#### [early_stopping_round](#early_stopping_round)[](#early_stopping_round "Click to copy url")

**Syntax:** obj \<\< early_stopping_round( number=0 )

**Description:** Specifies the maximum number of iterations for which to continue training while the training metric does not improve. A value of zero means no early stopping. "0" by default.

**JMP Version Added:** 19

#### [enable_bundle](#enable_bundle)[](#enable_bundle "Click to copy url")

**Syntax:** obj \<\< enable_bundle( state=1 )

**Description:** Specifies whether to use exclusive feature bundling. If this option is set to false, the training speed might be slow for sparse data sets. On by default.

**JMP Version Added:** 19

#### [eval_at](#eval_at)[](#eval_at "Click to copy url")

**Syntax:** obj \<\< eval_at( text=1,2,3,4,5 )

**Description:** Specifies the cutoff points when ranking models with either of the NDGG or MAP metrics. "1,2,3,4,5" by default.

**JMP Version Added:** 19

#### [eval_metric](#eval_metric)[](#eval_metric "Click to copy url")

**Syntax:** obj \<\< eval_metric( text )

**Description:** Specifies the metric shown in the iteration history plot but does not affect the actual model fit. Leave this value blank for the default metric corresponding to the objective function, or specify one of the following: rmse, rmsle, mae, logloss, error, error@t, merror, auc, aucpr, ndcg, map, ndcg@n, map@n, ndcg-, map-, ndcg@n-, map@n-, poisson-nloglik, gamma-nloglik, cox-nloglik, gamma-deviance, tweedie-nloglik.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( eval_metric( rmse ) ) );
```

#### [extra_seed](#extra_seed)[](#extra_seed "Click to copy url")

**Syntax:** obj \<\< extra_seed( number=6 )

**Description:** Specifies the seed that is used for selecting thresholds when the extra trees option is specified. "6" by default.

**JMP Version Added:** 19

#### [extra_trees](#extra_trees)[](#extra_trees "Click to copy url")

**Syntax:** obj \<\< extra_trees( state=0 )

**Description:** Specifies whether to use extremely randomized trees. Instead of evaluating all possible split points for each feature to find the optimal split, this option randomly selects a subset of features at each node. For each selected feature, this option randomly chooses one threshold to evaluate for the splitting node. "0" by default.

**JMP Version Added:** 19

#### [fair_c](#fair_c)[](#fair_c "Click to copy url")

**Syntax:** obj \<\< fair_c( number=1 )

**Description:** Specifies the parameter that controls the smoothness of the fair objective loss. "1" by default.

**JMP Version Added:** 19

#### [feature_fraction](#feature_fraction)[](#feature_fraction "Click to copy url")

**Syntax:** obj \<\< feature_fraction( number=1 )

**Description:** Specifies the proportion of columns to sample when constructing each tree. Sampling occurs once for each tree. This value must be between 0 and 1. "1" by default.

**JMP Version Added:** 19

#### [feature_fraction_bynode](#feature_fraction_bynode)[](#feature_fraction_bynode "Click to copy url")

**Syntax:** obj \<\< feature_fraction_bynode( number=1 )

**Description:** Specifies the fraction of features that are randomly selected during training. A value of 0.75 means 75% of features are randomly selected for training. "1" by default.

**JMP Version Added:** 19

#### [feature_fraction_max](#feature_fraction_max)[](#feature_fraction_max "Click to copy url")

**Syntax:** obj \<\< feature_fraction_max( number=1.0 )

**Description:** Specifies the maximum proportion of columns to sample when constructing each tree. Sampling occurs once for each tree. This value must be between 0 and 1. "1.0" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( feature_fraction_max( 1.0 ) ) );
```

#### [feature_fraction_min](#feature_fraction_min)[](#feature_fraction_min "Click to copy url")

**Syntax:** obj \<\< feature_fraction_min( number=0.2 )

**Description:** Specifies the minimum proportion of columns to sample when constructing each tree. Sampling occurs once for each tree. This value must be between 0 and 1. "0.2" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( feature_fraction_min( 0.2 ) ) );
```

#### [feature_fraction_seed](#feature_fraction_seed)[](#feature_fraction_seed "Click to copy url")

**Syntax:** obj \<\< feature_fraction_seed( number=2 )

**Description:** Specifies the seed that is used for the feature fraction random number generator. "2" by default.

**JMP Version Added:** 19

#### [feature_pre_filter](#feature_pre_filter)[](#feature_pre_filter "Click to copy url")

**Syntax:** obj \<\< feature_pre_filter( state=1 )

**Description:** Specifies whether to ignore features that are not splittable based on the specified value for minimum observations in each leaf. If this option is set to false, the training speed might be slow. On by default.

**JMP Version Added:** 19

#### [feature_selector](#feature_selector)[](#feature_selector "Click to copy url")

**Syntax:** obj \<\< feature_selector( "cyclic"\|"shuffle"\|"greedy"\|"thrifty"="cyclic" )

**Description:** Specifies the feature selection and ordering method for the linear booster. "cyclic" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost(
    Y( :Weight ),
    X( :Height ),
    Booster( "gblinear" ),
    Fit( feature_selector( "cyclic" ) )
);
```

#### [force_col_wise](#force_col_wise)[](#force_col_wise "Click to copy url")

**Syntax:** obj \<\< force_col_wise( state=0 )

**Description:** Specifies whether to force columnwise histogram building. Enabling this option reduces memory cost, especially for data that have many features. This option cannot be used together with force rowwise. "0" by default.

**JMP Version Added:** 19

#### [force_row_wise](#force_row_wise)[](#force_row_wise "Click to copy url")

**Syntax:** obj \<\< force_row_wise( state=0 )

**Description:** "0" by default.

**JMP Version Added:** 19

#### [gamma](#gamma)[](#gamma "Click to copy url")

**Syntax:** obj \<\< gamma( number=0.0 )

**Description:** Specifies the minimum loss reduction required to make a further partition on a leaf node of the tree. "0.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( Gamma( 0.0 ) ) );
```

#### [gpu_device_id](#gpu_device_id)[](#gpu_device_id "Click to copy url")

**Syntax:** obj \<\< gpu_device_id( number=-1 )

**Description:** Specifies the device number when using the GPU. "-1" by default.

**JMP Version Added:** 19

#### [gpu_platform_id](#gpu_platform_id)[](#gpu_platform_id "Click to copy url")

**Syntax:** obj \<\< gpu_platform_id( number=-1 )

**Description:** Specifies the platform number when using the GPU. "-1" by default.

**JMP Version Added:** 19

#### [gpu_use_dp](#gpu_use_dp)[](#gpu_use_dp "Click to copy url")

**Syntax:** obj \<\< gpu_use_dp( state=0 )

**Description:** Specifies whether to use double precision math on the GPU. "0" by default.

**JMP Version Added:** 19

#### [grow_policy](#grow_policy)[](#grow_policy "Click to copy url")

**Syntax:** obj \<\< grow_policy( "depthwise"\|"lossguide"="depthwise" )

**Description:** Specifies the method used to add new nodes to trees. Currently, this option applies only when tree_method=hist. "depthwise" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( grow_policy( "depthwise" ) ) );
```

#### [histogram_pool_size](#histogram_pool_size)[](#histogram_pool_size "Click to copy url")

**Syntax:** obj \<\< histogram_pool_size( number=-1 )

**Description:** Specifies the maximum memory size in megabytes for the historical histogram. "-1" by default.

**JMP Version Added:** 19

#### [interaction_constraints](#interaction_constraints)[](#interaction_constraints "Click to copy url")

**Syntax:** obj \<\< interaction_constraints( text )

**Description:** Specifies feature interaction constraints as a nested list of feature indices using brackets. Features grouped together can interact only with each other.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Age << Set Modeling Type( "Continuous" );
dt << XGBoost(
    Y( :Weight ),
    X( :Age, :Height ),
    Fit( interaction_constraints( "[[0,1]]" ) )
);
```

#### [is_enable_sparse](#is_enable_sparse)[](#is_enable_sparse "Click to copy url")

**Syntax:** obj \<\< is_enable_sparse( state=1 )

**Description:** Specifies whether to enable sparse optimization. On by default.

**JMP Version Added:** 19

#### [is_unbalance](#is_unbalance)[](#is_unbalance "Click to copy url")

**Syntax:** obj \<\< is_unbalance( state=0 )

**Description:** Specifies whether the training data set is unbalanced in binary and multiclass regression. "0" by default.

**JMP Version Added:** 19

#### [iterations](#iterations)[](#iterations "Click to copy url")

**Syntax:** obj \<\< iterations( number=30 )

**Description:** Specifies the number of boosting iterations. "30" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( iterations( 100 ) ) );
```

#### [iterations_max](#iterations_max)[](#iterations_max "Click to copy url")

**Syntax:** obj \<\< iterations_max( number=100 )

**Description:** Specifies the maximum number of boosting iterations. "100" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( iterations_max( 300 ) ) );
```

#### [iterations_min](#iterations_min)[](#iterations_min "Click to copy url")

**Syntax:** obj \<\< iterations_min( number=20 )

**Description:** Specifies the minimum number of boosting iterations. "20" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( iterations_min( 20 ) ) );
```

#### [lambda](#lambda)[](#lambda "Click to copy url")

**Syntax:** obj \<\< lambda( number=1.0 )

**Description:** Specifies the L2 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( lambda( 1.0 ) ) );
```

#### [lambda_l1](#lambda_l1)[](#lambda_l1 "Click to copy url")

**Syntax:** obj \<\< lambda_l1( number=0 )

**Description:** Specifies the L1 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "0" by default.

**JMP Version Added:** 19

#### [lambda_l1_max](#lambda_l1_max)[](#lambda_l1_max "Click to copy url")

**Syntax:** obj \<\< lambda_l1_max( number=2.0 )

**Description:** Specifies the maximum L1 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "2.0" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( lambda_l1_max( 2.0 ) ) );
```

#### [lambda_l1_min](#lambda_l1_min)[](#lambda_l1_min "Click to copy url")

**Syntax:** obj \<\< lambda_l1_min( number=0.0 )

**Description:** Specifies the minimum L1 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "0.0" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( lambda_l1_min( 0.0 ) ) );
```

#### [lambda_l2](#lambda_l2)[](#lambda_l2 "Click to copy url")

**Syntax:** obj \<\< lambda_l2( number=0 )

**Description:** Specifies the L2 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "0" by default.

**JMP Version Added:** 19

#### [lambda_l2_max](#lambda_l2_max)[](#lambda_l2_max "Click to copy url")

**Syntax:** obj \<\< lambda_l2_max( number=2.0 )

**Description:** Specifies the maximum L2 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "2.0" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( lambda_l2_max( 2.0 ) ) );
```

#### [lambda_l2_min](#lambda_l2_min)[](#lambda_l2_min "Click to copy url")

**Syntax:** obj \<\< lambda_l2_min( number=0.0 )

**Description:** Specifies the minimum L2 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "0.0" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( lambda_l2_min( 0.0 ) ) );
```

#### [lambda_max](#lambda_max)[](#lambda_max "Click to copy url")

**Syntax:** obj \<\< lambda_max( number=2.0 )

**Description:** Specifies the maximum L2 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "2.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( lambda_max( 2.0 ) ) );
```

#### [lambda_min](#lambda_min)[](#lambda_min "Click to copy url")

**Syntax:** obj \<\< lambda_min( number=0.0 )

**Description:** Specifies the minimum L2 regularization term on weights. Increasing this value makes the model more conservative. This value must be nonnegative. "0.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( lambda_min( 0.0 ) ) );
```

#### [lambdarank_norm](#lambdarank_norm)[](#lambdarank_norm "Click to copy url")

**Syntax:** obj \<\< lambdarank_norm( state=1 )

**Description:** Specifies whether to normalize the lambdas for different queries and improve performance in unbalanced data. On by default.

**JMP Version Added:** 19

#### [lambdarank_position_bias_regularization](#lambdarank_position_bias_regularization)[](#lambdarank_position_bias_regularization "Click to copy url")

**Syntax:** obj \<\< lambdarank_position_bias_regularization( number=0 )

**Description:** Specifies the value that controls position information bias for the LambdaRank objective. Larger values reduce inferred position biased factors. "0" by default.

**JMP Version Added:** 19

#### [lambdarank_truncation_level](#lambdarank_truncation_level)[](#lambdarank_truncation_level "Click to copy url")

**Syntax:** obj \<\< lambdarank_truncation_level( number=30 )

**Description:** Specifies the parameter that controls the number of top results on which the model should focus during training for the LambdaRank objective. "30" by default.

**JMP Version Added:** 19

#### [learning_rate](#learning_rate)[](#learning_rate "Click to copy url")

**Syntax:** obj \<\< learning_rate( number=0.3 )

**Description:** Specifies the learning rate. Smaller learning rates tend to fit better but require more iterations to converge, whereas larger learning rates fit faster. "0.3" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( learning_rate( 0.3 ) ) );
```

#### [learning_rate_max](#learning_rate_max)[](#learning_rate_max "Click to copy url")

**Syntax:** obj \<\< learning_rate_max( number=0.4 )

**Description:** Specifies the maximum learning rate. Smaller learning rates tend to fit better but require more iterations to converge, whereas larger learning rates fit faster. "0.4" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( learning_rate_max( 0.4 ) ) );
```

#### [learning_rate_min](#learning_rate_min)[](#learning_rate_min "Click to copy url")

**Syntax:** obj \<\< learning_rate_min( number=0.05 )

**Description:** Specifies the minimum learning rate. Smaller learning rates tend to fit better but require more iterations to converge, whereas larger learning rates fit faster. "0.05" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( learning_rate_min( 0.05 ) ) );
```

#### [linear_lambda](#linear_lambda)[](#linear_lambda "Click to copy url")

**Syntax:** obj \<\< linear_lambda( number=0.0 )

**Description:** Specifies the regularization parameter for linear trees. "0.0" by default.

**JMP Version Added:** 19

#### [linear_tree](#linear_tree)[](#linear_tree "Click to copy url")

**Syntax:** obj \<\< linear_tree( state=0 )

**Description:** Specifies whether to fit piecewise linear gradient boosting tree. The splits are chosen in the usual manner, but the model is linear at each leaf instead of constant. "0" by default.

**JMP Version Added:** 19

#### [max_bin](#max_bin)[](#max_bin "Click to copy url")

**Syntax:** obj \<\< max_bin( number=256 )

**Description:** Specifies the maximum number of discrete bins into which to bucket continuous features. This option applies only for tree_method=hist. "256" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( max_bin( 256 ) ) );
```

#### [max_bin_by_feature](#max_bin_by_feature)[](#max_bin_by_feature "Click to copy url")

**Syntax:** obj \<\< max_bin_by_feature( text )

**Description:** Specifies the maximum number of bins for each feature.

**JMP Version Added:** 19

#### [max_cat_threshold](#max_cat_threshold)[](#max_cat_threshold "Click to copy url")

**Syntax:** obj \<\< max_cat_threshold( number=32 )

**Description:** Specifies the threshold for maximum number of unique categories to consider when splitting categorical features. Larger values result in a more exhaustive search for optimal categorical splits at the expense of longer training time. "32" by default.

**JMP Version Added:** 19

#### [max_cat_to_onehot](#max_cat_to_onehot)[](#max_cat_to_onehot "Click to copy url")

**Syntax:** obj \<\< max_cat_to_onehot( number=4 )

**Description:** Specifies the maximum number of categories that a categorical feature can have to use the one-vs-other split algorithm. Categorical features with more than the maximum number of categories are handled by a different algorithm. "4" by default.

**JMP Version Added:** 19

#### [max_delta_step](#max_delta_step)[](#max_delta_step "Click to copy url")

**Syntax:** obj \<\< max_delta_step( number=0.0 )

**Description:** Specifies the maximum delta step that each leaf output can take. "0.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( max_delta_step( 0.0 ) ) );
```

#### [max_depth](#max_depth)[](#max_depth "Click to copy url")

**Syntax:** obj \<\< max_depth( number=6 )

**Description:** Specifies the maximum depth of the tree. This value must be an integer. Complexity increases as depth increases. Models with larger max_depth have a higher risk of overfitting. "6" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( max_depth( 6 ) ) );
```

#### [max_depth_max](#max_depth_max)[](#max_depth_max "Click to copy url")

**Syntax:** obj \<\< max_depth_max( number=8 )

**Description:** Specifies the maximum depth of tree maximum. This value must be an integer. Complexity increases as depth increases. Models with depths of 2^depth and larger have higher risk of overfitting. "8" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( max_depth_max( 9 ) ) );
```

#### [max_depth_min](#max_depth_min)[](#max_depth_min "Click to copy url")

**Syntax:** obj \<\< max_depth_min( number=1 )

**Description:** Specifies the maximum depth of tree minimum. This value must be an integer. Complexity increases as depth increases. Models with depths of 2^depth and larger have higher risk of overfitting. "1" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( max_depth_min( 3 ) ) );
```

#### [max_drop](#max_drop)[](#max_drop "Click to copy url")

**Syntax:** obj \<\< max_drop( number=50 )

**Description:** Specifies the maximum number of dropped trees on each DART boosting iteration. "50" by default.

**JMP Version Added:** 19

#### [max_leaves](#max_leaves)[](#max_leaves "Click to copy url")

**Syntax:** obj \<\< max_leaves( number=0 )

**Description:** Specifies the maximum number of nodes to be added. This option applies only for grow_policy=lossguide. "0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( max_leaves( 0 ) ) );
```

#### [metric](#metric)[](#metric "Click to copy url")

**Syntax:** obj \<\< metric( "default"\|"l1"\|"l2"\|"rmse"\|"quantile"\|"mape"\|"huber"\|"fair"\|"poisson"\|"gamma"\|"gamma_deviance"\|"tweedie"\|"ndcg"\|"map"\|"auc"\|"average_precision"\|"binary_logloss"\|"binary_error"\|"auc_mu"\|"multi_logloss"\|"multi_error"\|"cross_entropy"\|"cross_entropy_lambda"\|"kulback_leibler"="default" )

**Description:** Specifies the metric that is evaluated in both training and validation sets. "default" by default.

**JMP Version Added:** 19

#### [min_child_weight](#min_child_weight)[](#min_child_weight "Click to copy url")

**Syntax:** obj \<\< min_child_weight( number=1.0 )

**Description:** Specifies the minimum sum of instance weight (Hessian) needed in a child. This value is the minimum size of each leaf. "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( min_child_weight( 1.0 ) ) );
```

#### [min_child_weight_max](#min_child_weight_max)[](#min_child_weight_max "Click to copy url")

**Syntax:** obj \<\< min_child_weight_max( number=3.0 )

**Description:** Specifies the maximum sum of instance weight (Hessian) needed in a child. This value is the maximum size of each leaf. "3.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( min_child_weight_max( 10.0 ) ) );
```

#### [min_child_weight_min](#min_child_weight_min)[](#min_child_weight_min "Click to copy url")

**Syntax:** obj \<\< min_child_weight_min( number=1.0 )

**Description:** Specifies the minimum sum of instance weight (Hessian) needed in a child. This value is the minimum size of each leaf. "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( min_child_weight_min( 1.0 ) ) );
```

#### [min_data_in_bin](#min_data_in_bin)[](#min_data_in_bin "Click to copy url")

**Syntax:** obj \<\< min_data_in_bin( number=3 )

**Description:** Specifies the minimum number of observations that are included in each bin. "3" by default.

**JMP Version Added:** 19

#### [min_data_in_leaf](#min_data_in_leaf)[](#min_data_in_leaf "Click to copy url")

**Syntax:** obj \<\< min_data_in_leaf( number=20 )

**Description:** Specifies the minimum number of observations in each leaf. "20" by default.

**JMP Version Added:** 19

#### [min_data_per_group](#min_data_per_group)[](#min_data_per_group "Click to copy url")

**Syntax:** obj \<\< min_data_per_group( number=100 )

**Description:** Specifies the minimum number of observations per categorical group on categorical features. "100" by default.

**JMP Version Added:** 19

#### [min_gain_to_split](#min_gain_to_split)[](#min_gain_to_split "Click to copy url")

**Syntax:** obj \<\< min_gain_to_split( number=0 )

**Description:** Specifies the maximum depth of the tree. This value must be an integer. Complexity increases as depth increases. Models with larger max_depth have a higher risk of overfitting. "0" by default.

**JMP Version Added:** 19

#### [min_sum_hessian_in_leaf](#min_sum_hessian_in_leaf)[](#min_sum_hessian_in_leaf "Click to copy url")

**Syntax:** obj \<\< min_sum_hessian_in_leaf( number=0.001 )

**Description:** Specifies the minimum sum of instance weight (Hessian) needed in a child. This value is the minimum size of each leaf. "0.001" by default.

**JMP Version Added:** 19

#### [min_sum_hessian_in_leaf_max](#min_sum_hessian_in_leaf_max)[](#min_sum_hessian_in_leaf_max "Click to copy url")

**Syntax:** obj \<\< min_sum_hessian_in_leaf_max( number=10.0 )

**Description:** Specifies the maximum sum of instance weight (Hessian) needed in a child. This value is the maximum size of each leaf. "10.0" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( min_sum_hessian_in_leaf_max( 10.0 ) ) );
```

#### [min_sum_hessian_in_leaf_min](#min_sum_hessian_in_leaf_min)[](#min_sum_hessian_in_leaf_min "Click to copy url")

**Syntax:** obj \<\< min_sum_hessian_in_leaf_min( number=0.5 )

**Description:** Specifies the minimum sum of instance weight (Hessian) needed in a child. This value is the minimum size of each leaf. "0.5" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( min_sum_hessian_in_leaf_min( 0.5 ) ) );
```

#### [monotone_constraints](#monotone_constraints)[](#monotone_constraints "Click to copy url")

**Syntax:** obj \<\< monotone_constraints( text=None )

**Description:** Specifies monotonicity constraints for each feature. The constraints must be specified using a comma-separated list of values within parentheses, where -1 indicates negative, 1 indicates positive, and 0 indicates no constraint. "None" by default.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Age << Set Modeling Type( "Continuous" );
dt << XGBoost( Y( :Weight ), X( :Age, :Height ), Fit( monotone_constraints( "(1,1)" ) ) );
```

#### [monotone_constraints_method](#monotone_constraints_method)[](#monotone_constraints_method "Click to copy url")

**Syntax:** obj \<\< monotone_constraints_method( "basic"\|"intermediate"\|"advanced"="basic" )

**Description:** Specifies the method for the monotone constraint when a constraint is set to be enforced. "basic" by default.

**JMP Version Added:** 19

#### [monotone_penalty](#monotone_penalty)[](#monotone_penalty "Click to copy url")

**Syntax:** obj \<\< monotone_penalty( number=0 )

**Description:** Specifies the strictness of the monotone constraint when a constraint is set to be enforced. A specified value of K forbids any monotone splits on the first K levels of the tree. Larger values result in more penalization in the early tree building process. "0" by default.

**JMP Version Added:** 19

#### [multi_error_top_k](#multi_error_top_k)[](#multi_error_top_k "Click to copy url")

**Syntax:** obj \<\< multi_error_top_k( number=1 )

**Description:** Specifies the threshold for the top-k multierror metric in multiclass classification. "1" by default.

**JMP Version Added:** 19

#### [neg_bagging_fraction](#neg_bagging_fraction)[](#neg_bagging_fraction "Click to copy url")

**Syntax:** obj \<\< neg_bagging_fraction( number=1 )

**Description:** Specifies the value by which to adjust the process of drawing negative samples in unbalanced binary regression. "1" by default.

**JMP Version Added:** 19

#### [normalize_type](#normalize_type)[](#normalize_type "Click to copy url")

**Syntax:** obj \<\< normalize_type( "tree"\|"forest"="tree" )

**Description:** Specifies the type of normalization algorithm for the DART booster. "tree" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost(
    Y( :Weight ),
    X( :Height ),
    Booster( "dart" ),
    Fit( normalize_type( "tree" ) )
);
```

#### [nthread](#nthread)[](#nthread "Click to copy url")

**Syntax:** obj \<\< nthread( number=0 )

**Description:** Specifies the number of parallel threads used to run XGBoost. By default, all available threads are used. "0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( nthread( 8 ) ) );
```

#### [num_grad_quant_bins](#num_grad_quant_bins)[](#num_grad_quant_bins "Click to copy url")

**Syntax:** obj \<\< num_grad_quant_bins( number=4 )

**Description:** Specifies the number of bins for the quantization gradients and Hessian matrices when using the quantized gradient. Larger values produce quantized training that is closer to full precision training. "4" by default.

**JMP Version Added:** 19

#### [num_iteration_predict](#num_iteration_predict)[](#num_iteration_predict "Click to copy url")

**Syntax:** obj \<\< num_iteration_predict( number=-1 )

**Description:** Specifies the number of iterations for which to make predictions. "-1" by default.

**JMP Version Added:** 19

#### [num_iterations](#num_iterations)[](#num_iterations "Click to copy url")

**Syntax:** obj \<\< num_iterations( number=100 )

**Description:** Specifies the number of boosting iterations. "100" by default.

**JMP Version Added:** 19

#### [num_iterations_max](#num_iterations_max)[](#num_iterations_max "Click to copy url")

**Syntax:** obj \<\< num_iterations_max( number=100 )

**Description:** Specifies the maximum number of boosting iterations. "100" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( num_iterations_max( 100 ) ) );
```

#### [num_iterations_min](#num_iterations_min)[](#num_iterations_min "Click to copy url")

**Syntax:** obj \<\< num_iterations_min( number=20 )

**Description:** Specifies the minimum number of boosting iterations. "20" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( num_iterations_min( 20 ) ) );
```

#### [num_leaves](#num_leaves)[](#num_leaves "Click to copy url")

**Syntax:** obj \<\< num_leaves( number=31 )

**Description:** Specifies the maximum number of leaves on each tree. "31" by default.

**JMP Version Added:** 19

#### [num_parallel_tree](#num_parallel_tree)[](#num_parallel_tree "Click to copy url")

**Syntax:** obj \<\< num_parallel_tree( number=1 )

**Description:** Specifies the number of boosted trees to grow in parallel. Then the results are averaged. "1" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( num_parallel_tree( 1 ) ) );
```

#### [num_threads](#num_threads)[](#num_threads "Click to copy url")

**Syntax:** obj \<\< num_threads( number=0 )

**Description:** Specifies the number of threads. For the best speed, set this to the number of core CPUs. "0" by default.

**JMP Version Added:** 19

#### [objective](#objective)[](#objective "Click to copy url")

**Syntax:** obj \<\< objective( "reg:squarederror"\|"binary:logistic"\|"binary:hinge"\|"count:poisson"\|"multi:softprob"\|"rank:pairwise"\|"rank:ndcg"\|"rank:map"\|"reg:gamma"\|"reg:logistic"\|"reg:pseudohubererror"\|"reg:squaredlogerror"\|"reg:tweedie"\|"survival:cox"="reg:squarederror" )

**Description:** Specifies the function to be optimized for model fitting. The function must be consistent with the modeling type of the response. "reg:squarederror" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), objective( "reg:squarederror" ) );
```

#### [objective_seed](#objective_seed)[](#objective_seed "Click to copy url")

**Syntax:** obj \<\< objective_seed( number=5 )

**Description:** Specifies the seed that is used in the random number generator for the objective parameter. "5" by default.

**JMP Version Added:** 19

#### [one_drop](#one_drop)[](#one_drop "Click to copy url")

**Syntax:** obj \<\< one_drop( number=0 )

**Description:** When this flag is enabled in the DART booster, at least one tree is always dropped during the dropout. "0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( booster( "dart" ), one_drop( 0 ) ) );
```

#### [other_rate](#other_rate)[](#other_rate "Click to copy url")

**Syntax:** obj \<\< other_rate( number=0.1 )

**Description:** Specifies the retain ratio of small gradient data for the GOSS data sampling strategy. "0.1" by default.

**JMP Version Added:** 19

#### [path_smooth](#path_smooth)[](#path_smooth "Click to copy url")

**Syntax:** obj \<\< path_smooth( number=0 )

**Description:** "0" by default.

**JMP Version Added:** 19

#### [poisson_max_delta_step](#poisson_max_delta_step)[](#poisson_max_delta_step "Click to copy url")

**Syntax:** obj \<\< poisson_max_delta_step( number=0.7 )

**Description:** Specifies a value that serves to limit the maximum prediction contribution of leaves for the Poisson model. "0.7" by default.

**JMP Version Added:** 19

#### [pos_bagging_fraction](#pos_bagging_fraction)[](#pos_bagging_fraction "Click to copy url")

**Syntax:** obj \<\< pos_bagging_fraction( number=1 )

**Description:** Specifies the value by which to adjust the process of drawing positive samples in unbalanced binary regression. "1" by default.

**JMP Version Added:** 19

#### [pred_early_stop](#pred_early_stop)[](#pred_early_stop "Click to copy url")

**Syntax:** obj \<\< pred_early_stop( state=0 )

**Description:** Specifies whether to enforce prediction early stopping in classification and ranking applications. If this option is set to true, prediction can be faster, but accuracy might be affected. "0" by default.

**JMP Version Added:** 19

#### [pred_early_stop_freq](#pred_early_stop_freq)[](#pred_early_stop_freq "Click to copy url")

**Syntax:** obj \<\< pred_early_stop_freq( number=10 )

**Description:** Specifies the frequency of checking prediction early stopping when prediction early stopping is specified. "10" by default.

**JMP Version Added:** 19

#### [pred_early_stop_margin](#pred_early_stop_margin)[](#pred_early_stop_margin "Click to copy url")

**Syntax:** obj \<\< pred_early_stop_margin( number=10 )

**Description:** Specifies the threshold margin in prediction early stopping when prediction early stopping is specified. This parameter enables the prediction process to stop early if the margin is far enough from the threshold. "10" by default.

**JMP Version Added:** 19

#### [predict_disable_shape_check](#predict_disable_shape_check)[](#predict_disable_shape_check "Click to copy url")

**Syntax:** obj \<\< predict_disable_shape_check( state=0 )

**Description:** Specifies whether to raise the error when predicting on data that have different numbers of features than the training data. "0" by default.

**JMP Version Added:** 19

#### [predictor](#predictor)[](#predictor "Click to copy url")

**Syntax:** obj \<\< predictor( "auto"\|"cpu_predictor"\|"gpu_predictor"="auto" )

**Description:** Specifies the type of predictor algorithm. "auto" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( predictor( "cpu_predictor" ) ) );
```

#### [process_type](#process_type)[](#process_type "Click to copy url")

**Syntax:** obj \<\< process_type( "default"\|"update"="default" )

**Description:** Specifies the type of boosting process to run. "default" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( process_type( "default" ) ) );
```

#### [quant_train_renew_leaf](#quant_train_renew_leaf)[](#quant_train_renew_leaf "Click to copy url")

**Syntax:** obj \<\< quant_train_renew_leaf( state=0 )

**Description:** Specifies whether to renew the leaf values with original gradients when quantized training is in effect. This option can improve the accuracy of the ranking objectives in quantized training. "0" by default.

**JMP Version Added:** 19

#### [rate_drop](#rate_drop)[](#rate_drop "Click to copy url")

**Syntax:** obj \<\< rate_drop( number=0.0 )

**Description:** Specifies the dropout rate for the DART booster. "0.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( booster( "dart" ), rate_drop( 0.0 ) ) );
```

#### [refresh_leaf](#refresh_leaf)[](#refresh_leaf "Click to copy url")

**Syntax:** obj \<\< refresh_leaf( number=1 )

**Description:** Specifies the parameter of the refresh updater. If set to 1, leaves and nodes updated. If set to 0, only nodes are updated. "1" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( refresh_leaf( 1 ) ) );
```

#### [reg_sqrt](#reg_sqrt)[](#reg_sqrt "Click to copy url")

**Syntax:** obj \<\< reg_sqrt( state=0 )

**Description:** Specifies whether to fit the square root of the response variable rather than the original values for regression models. "0" by default.

**JMP Version Added:** 19

#### [sample_type](#sample_type)[](#sample_type "Click to copy url")

**Syntax:** obj \<\< sample_type( "uniform"\|"weighted"="uniform" )

**Description:** Specifies the type of sampling algorithm for the DART booster. "uniform" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost(
    Y( :Weight ),
    X( :Height ),
    Booster( "dart" ),
    Fit( sample_type( "uniform" ) )
);
```

#### [scale_pos_weight](#scale_pos_weight)[](#scale_pos_weight "Click to copy url")

**Syntax:** obj \<\< scale_pos_weight( number=1.0 )

**Description:** Specifies the balance of positive and negative weights, which are useful for unbalanced classes. A typical value to consider is sum(negative instances) / sum(positive instances). "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( scale_posweight( 1.0 ) ) );
```

#### [seed](#seed)[](#seed "Click to copy url")

**Syntax:** obj \<\< seed( number=0 )

**Description:** Specifies the seed for the random number generator. Set this value for reproducibility of the results. "0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( seed( 0 ) ) );
```

#### [sigmoid](#sigmoid)[](#sigmoid "Click to copy url")

**Syntax:** obj \<\< sigmoid( number=1 )

**Description:** Specifies the parameter for the sigmoid function in binary and multiclass models. "1" by default.

**JMP Version Added:** 19

#### [sketch_eps](#sketch_eps)[](#sketch_eps "Click to copy url")

**Syntax:** obj \<\< sketch_eps( number=0.03 )

**Description:** Used only for tree_method=approx, this value approximately translates into (1 / sketch_eps) = number of bins. "0.03" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( sketch_eps( 0.03 ) ) );
```

#### [skip_drop](#skip_drop)[](#skip_drop "Click to copy url")

**Syntax:** obj \<\< skip_drop( number=0.0 )

**Description:** Specifies the probability of skipping the dropout procedure during a DART boosting iteration. "0.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( booster( "dart" ), skip_drop( 0.0 ) ) );
```

#### [start_iteration_predict](#start_iteration_predict)[](#start_iteration_predict "Click to copy url")

**Syntax:** obj \<\< start_iteration_predict( number=0 )

**Description:** Specifies the starting iteration for which to make predictions. "0" by default.

**JMP Version Added:** 19

#### [stochastic_rounding](#stochastic_rounding)[](#stochastic_rounding "Click to copy url")

**Syntax:** obj \<\< stochastic_rounding( state=1 )

**Description:** Specifies whether to use stochastic rounding in gradient quantization. On by default.

**JMP Version Added:** 19

#### [subsample](#subsample)[](#subsample "Click to copy url")

**Syntax:** obj \<\< subsample( number=1.0 )

**Description:** Specifies the proportion of rows to sample during each iteration. This value must be between 0 and 1. This is a type of bagging. "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( subsample( 1.0 ) ) );
```

#### [subsample_max](#subsample_max)[](#subsample_max "Click to copy url")

**Syntax:** obj \<\< subsample_max( number=1.0 )

**Description:** Specifies the maximum proportion of rows to sample during each iteration. This value must be between 0 and 1. This is a type of bagging. "1.0" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( subsample_max( 1.0 ) ) );
```

#### [subsample_min](#subsample_min)[](#subsample_min "Click to copy url")

**Syntax:** obj \<\< subsample_min( number=0.5 )

**Description:** Specifies the minimum proportion of rows to sample during each iteration. This value must be between 0 and 1. This is a type of bagging. "0.5" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( subsample_min( 0.3 ) ) );
```

#### [top_k](#top_k)[](#top_k "Click to copy url")

**Syntax:** obj \<\< top_k( number=256 )

**Description:** Specifies the number of top features to select in greedy and thrifty feature selector. This option applies only for the gblinear booster. "256" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( booster( "gblinear" ), top_k( 0 ) ) );
```

#### [top_rate](#top_rate)[](#top_rate "Click to copy url")

**Syntax:** obj \<\< top_rate( number=0.2 )

**Description:** Specifies the retain ratio of large gradient data for the GOSS data sampling strategy. "0.2" by default.

**JMP Version Added:** 19

#### [tree_method](#tree_method)[](#tree_method "Click to copy url")

**Syntax:** obj \<\< tree_method( "auto"\|"exact"\|"approx"\|"hist"\|"gpu_exact"\|"gpu_hist"="auto" )

**Description:** Specifies the tree construction algorithm used in XGBoost. "auto" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( tree_method( "auto" ) ) );
```

#### [tweedie_variance_power](#tweedie_variance_power)[](#tweedie_variance_power "Click to copy url")

**Syntax:** obj \<\< tweedie_variance_power( number=1.5 )

**Description:** Specifies the power of the Tweedie distribution. This value must be between 1 and 2. This option applies only for objective=reg:tweedie. "1.5" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost(
    Y( :Weight ),
    X( :Height ),
    Fit( objective( "reg:tweedie" ), tweedie_variance_power( 1.5 ) )
);
```

#### [uniform_drop](#uniform_drop)[](#uniform_drop "Click to copy url")

**Syntax:** obj \<\< uniform_drop( state=0 )

**Description:** Specifies whether to select trees for dropping in DART boosting using uniform probability. "0" by default.

**JMP Version Added:** 19

#### [updater](#updater)[](#updater "Click to copy url")

**Syntax:** obj \<\< updater( text )

**Description:** Specifies the tree updater to run for the gbtree booster. Specify one of the following: grow_colmaker, distcol, grow_histmaker, grow_local_histmaker, grow_skmaker, sync, refresh, prune. For the gblinear booster, specify either shotgun or coord_descent.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << XGBoost( Y( :Weight ), X( :Height ), Fit( updater( "grow_colmaker" ) ) );
```

#### [use_missing](#use_missing)[](#use_missing "Click to copy url")

**Syntax:** obj \<\< use_missing( state=1 )

**Description:** Specifies whether to enforce special handling of missing values. On by default.

**JMP Version Added:** 19

#### [use_quantized_grad](#use_quantized_grad)[](#use_quantized_grad "Click to copy url")

**Syntax:** obj \<\< use_quantized_grad( state=0 )

**Description:** Specifies whether to use gradient quantization when training. Enabling this option discretizes the gradients and Hessian matrices into bins, which can accelerate training with little loss in accuracy in most cases. "0" by default.

**JMP Version Added:** 19

#### [xgboost_dart_mode](#xgboost_dart_mode)[](#xgboost_dart_mode "Click to copy url")

**Syntax:** obj \<\< xgboost_dart_mode( state=0 )

**Description:** Specifies whether to use XGBoost DART mode. "0" by default.

**JMP Version Added:** 19

#### [zero_as_missing](#zero_as_missing)[](#zero_as_missing "Click to copy url")

**Syntax:** obj \<\< zero_as_missing( state=0 )

**Description:** Specifies whether to treat all zero values as missing values. "0" by default.

**JMP Version Added:** 19

[ Previous](Workflow.html "Workflow") [Next ](ZipArchive.html "ZipArchive")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
