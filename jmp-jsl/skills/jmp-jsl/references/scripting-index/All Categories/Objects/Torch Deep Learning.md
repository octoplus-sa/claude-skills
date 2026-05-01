# Torch Deep Learning

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Torch%20Deep%20Learning.html](https://jsl.jmp.com/All%20Categories/Objects/Torch%20Deep%20Learning.html)*

---

# [Torch Deep Learning](#torch-deep-learning)[](#torch-deep-learning "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Torch Deep Learning](#torch-deep-learning_1)[](#torch-deep-learning_1 "Click to copy url")

**Syntax:** Torch Deep Learning(Y( columns ), X( columns ))

**Description:** Interface to predictive modeling via the Torch Deep Learning add-in

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

## [Columns](#columns)[](#columns "Click to copy url")

### [Censor](#censor)[](#censor "Click to copy url")

**Syntax:** obj \<\< Censor( column )

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

### [Inputs](#inputs)[](#inputs "Click to copy url")

**Syntax:** obj \<\< Inputs( column(s) )

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

### [Responses](#responses)[](#responses "Click to copy url")

**Syntax:** obj \<\< Responses( column(s) )

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

### [Subject](#subject)[](#subject "Click to copy url")

**Syntax:** obj \<\< Subject( column )

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

### [Validation](#validation)[](#validation "Click to copy url")

**Syntax:** obj \<\< Validation( column(s) )

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

### [Weight](#weight)[](#weight "Click to copy url")

**Syntax:** obj \<\< Weight( column )

**Description:** Specifies a column whose values assign a weight to each row for the analysis.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
dt << New Column( "_weightcol", Numeric, Continuous, Set Each Value( Random Beta( 1, 1 ) ) );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** obj \<\< X( column(s) )

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Change Variables](#change-variables)[](#change-variables "Click to copy url")

**Syntax:** obj \<\< Change Variables

**Description:** Changes X, Y, and other variables for subsequent models.

**JMP Version Added:** 18

### [Compare](#compare)[](#compare "Click to copy url")

**Syntax:** obj \<\< Compare

**Description:** Updates the Torch Deep Learning comparison metrics.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj << Compare( AUC( 1 ) );
```

### [Fit](#fit)[](#fit "Click to copy url")

**Syntax:** obj \<\< Fit

**Description:** Fits a Torch Deep Learning model. You can specify parameters and fitting specifications within this command.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
```

### [Get Measures](#get-measures)[](#get-measures "Click to copy url")

**Syntax:** obj \<\< Get Measures

**JMP Version Added:** 18

### [Redo Analysis](#redo-analysis)[](#redo-analysis "Click to copy url")

**Syntax:** obj \<\< Redo Analysis

**Description:** Rerun this same analysis in a new window. The analysis will be different if the data has changed.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Return to the launcher for this analysis.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj << Relaunch Analysis;
```

### [Set](#set)[](#set "Click to copy url")

**Syntax:** obj \<\< Set

**Description:** Specifies parameters for a Torch Deep Learning model.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Set( Epochs( 5 ) ) );
```

### [Show Details](#show-details)[](#show-details "Click to copy url")

**Syntax:** obj \<\< Show Details( state=0\|1 )

**Description:** Shows more details.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Show Details( 1 ) );
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
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
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
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
t = obj[1] << Get ByGroup Script;
Show( t );
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
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
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
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
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
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
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = Torch Deep Learning( Y( :sex ), X( :picture ), Fit );
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

## [Torch Deep Learning Compare](#torch-deep-learning-compare)[](#torch-deep-learning-compare "Click to copy url")

### [Associated Constructors](#associated-constructors_1)[](#associated-constructors_1 "Click to copy url")

#### [Torch Deep Learning Compare](#torch-deep-learning-compare_1)[](#torch-deep-learning-compare_1 "Click to copy url")

**Syntax:** Torch Deep Learning Compare

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [AUC](#auc)[](#auc "Click to copy url")

**Syntax:** obj \<\< AUC( state=0\|1 )

**Description:** Shows or hides the AUROC, which is the area under the receiver operating characteristic curve. On by default.

**JMP Version Added:** 18

#### [Accuracy](#accuracy)[](#accuracy "Click to copy url")

**Syntax:** obj \<\< Accuracy( state=0\|1 )

**Description:** Shows or hides the accuracy, which is the proportion of correct classifications. On by default.

**JMP Version Added:** 18

#### [Censor](#censor_1)[](#censor_1 "Click to copy url")

**Syntax:** obj \<\< Censor( state=0\|1 )

**Description:** Shows or hides the Censor command On by default.

**JMP Version Added:** 18

#### [Concordance](#concordance)[](#concordance "Click to copy url")

**Syntax:** obj \<\< Concordance( state=0\|1 )

**Description:** Shows or hides the concordance, which is the Harrell C-Index and measures strength of sorting efficiency On by default.

**JMP Version Added:** 18

#### [Correlation](#correlation)[](#correlation "Click to copy url")

**Syntax:** obj \<\< Correlation( state=0\|1 )

**Description:** Shows or hides the Pearson correlation, which is a measure of the strength of the linear relationship. On by default.

**JMP Version Added:** 18

#### [F1](#f1)[](#f1 "Click to copy url")

**Syntax:** obj \<\< F1( state=0\|1 )

**Description:** Shows or hides the F1 Score, which is the harmonic average of precision and recall. On by default.

**JMP Version Added:** 18

#### [Freq](#freq_1)[](#freq_1 "Click to copy url")

**Syntax:** obj \<\< Freq( state=0\|1 )

**Description:** Shows or hides the Freq column. On by default.

**JMP Version Added:** 18

#### [H Measure](#h-measure)[](#h-measure "Click to copy url")

**Syntax:** obj \<\< H Measure( state=0\|1 )

**Description:** Shows or hides the H Measure, which measures proportion improvement over baseline. On by default.

**JMP Version Added:** 18

#### [Hide All Models](#hide-all-models)[](#hide-all-models "Click to copy url")

**Syntax:** obj \<\< Hide All Models

**Description:** Hides all models.

**JMP Version Added:** 18

#### [LogLoss](#logloss)[](#logloss "Click to copy url")

**Syntax:** obj \<\< LogLoss( state=0\|1 )

**Description:** Shows or hides the logarithm of the likelihood-based loss function. On by default.

**JMP Version Added:** 18

#### [MAE](#mae)[](#mae "Click to copy url")

**Syntax:** obj \<\< MAE( state=0\|1 )

**Description:** Shows or hides the MAE, which is the mean absolute error. On by default.

**JMP Version Added:** 18

#### [MCC](#mcc)[](#mcc "Click to copy url")

**Syntax:** obj \<\< MCC( state=0\|1 )

**Description:** Shows or hides the Matthews correlation coefficient, which is the Pearson correlation for binary variables. On by default.

**JMP Version Added:** 18

#### [Misclass](#misclass)[](#misclass "Click to copy url")

**Syntax:** obj \<\< Misclass( state=0\|1 )

**Description:** Shows or hides the misclassification rate, which is the proportion of incorrect classifications. On by default.

**JMP Version Added:** 18

#### [Precision Recall AUC](#precision-recall-auc)[](#precision-recall-auc "Click to copy url")

**Syntax:** obj \<\< Precision Recall AUC( state=0\|1 )

**Description:** Shows or hides the Precision Recall AUC, which is the area under the precision-recall curve. On by default.

**JMP Version Added:** 18

#### [Predictors](#predictors)[](#predictors "Click to copy url")

**Syntax:** obj \<\< Predictors( state=0\|1 )

**Description:** Shows or hides the Predictors column. On by default.

**JMP Version Added:** 18

#### [Profit](#profit)[](#profit "Click to copy url")

**Syntax:** obj \<\< Profit( state=0\|1 )

**Description:** Shows or hides the expected profit. On by default.

**JMP Version Added:** 18

#### [RMSE](#rmse)[](#rmse "Click to copy url")

**Syntax:** obj \<\< RMSE( state=0\|1 )

**Description:** Shows or hides the RMSE, which is the root mean square error. On by default.

**JMP Version Added:** 18

#### [RSquare](#rsquare)[](#rsquare "Click to copy url")

**Syntax:** obj \<\< RSquare( state=0\|1 )

**Description:** Shows or hides RSquare value, which is the proportion of variability explained. On by default.

**JMP Version Added:** 18

#### [Remove Hidden Models](#remove-hidden-models)[](#remove-hidden-models "Click to copy url")

**Syntax:** obj \<\< Remove Hidden Models

**Description:** Removes all models for which the Show box is not checked.

**JMP Version Added:** 18

#### [Remove Shown Models](#remove-shown-models)[](#remove-shown-models "Click to copy url")

**Syntax:** obj \<\< Remove Shown Models

**Description:** Removes all models for which the Show check box is checked and shows the remaining models.

**JMP Version Added:** 18

#### [Response](#response)[](#response "Click to copy url")

**Syntax:** obj \<\< Response( state=0\|1 )

**Description:** Shows or hides the Response column. On by default.

**JMP Version Added:** 18

#### [Show All Models](#show-all-models)[](#show-all-models "Click to copy url")

**Syntax:** obj \<\< Show All Models

**Description:** Shows all models.

**JMP Version Added:** 18

#### [Subject](#subject_1)[](#subject_1 "Click to copy url")

**Syntax:** obj \<\< Subject( state=0\|1 )

**Description:** Shows or hides the Subject column On by default.

**JMP Version Added:** 18

#### [Training Metrics](#training-metrics)[](#training-metrics "Click to copy url")

**Syntax:** obj \<\< Training Metrics( state=0\|1 )

**Description:** Shows or hides all training metrics. On by default.

**JMP Version Added:** 18

#### [Validation](#validation_1)[](#validation_1 "Click to copy url")

**Syntax:** obj \<\< Validation( state=0\|1 )

**Description:** Shows or hides the Validation column. On by default.

**JMP Version Added:** 18

#### [Validation Metrics](#validation-metrics)[](#validation-metrics "Click to copy url")

**Syntax:** obj \<\< Validation Metrics( state=0\|1 )

**Description:** Shows or hides all validation metrics. On by default.

**JMP Version Added:** 18

#### [Weight](#weight_1)[](#weight_1 "Click to copy url")

**Syntax:** obj \<\< Weight( state=0\|1 )

**Description:** Shows or hides the Weight column. On by default.

**JMP Version Added:** 18

## [Torch Deep Learning Fit \> Post](#torch-deep-learning-fit-post)[](#torch-deep-learning-fit-post "Click to copy url")

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Actual by Predicted Plots](#actual-by-predicted-plots)[](#actual-by-predicted-plots "Click to copy url")

**Syntax:** obj \<\< Actual by Predicted Plots( state=0\|1 )

**Description:** Shows or hides a plot using the training data with the predicted values on the X axis and actual values on the Y axis. On by default.

**JMP Version Added:** 18

#### [Confusion Matrices](#confusion-matrices)[](#confusion-matrices "Click to copy url")

**Syntax:** obj \<\< ( fit\[number\] \<\< Confusion Matrices( state=0\|1 ) )

**Description:** Shows or hides a crosstabulation matrix of actual and predicted levels. On by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Torch Deep Learning(
    Y( :Species ),
    X( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    Fit
);
obj << (fit[1] << Confusion Matrices( 1 ));
```

#### [Contour Profiler.](#contour-profiler)[](#contour-profiler "Click to copy url")

**Syntax:** obj \<\< Contour Profiler.

**Description:** Shows or hides interactive graphs of cross-sections of the prediction function.

**JMP Version Added:** 18

#### [Decision Thresholds](#decision-thresholds)[](#decision-thresholds "Click to copy url")

**Syntax:** obj \<\< Decision Thresholds( state=0\|1 )

**Description:** Shows or hides decision threshold graphs and tables. On by default.

**JMP Version Added:** 18

#### [Fit Details](#fit-details)[](#fit-details "Click to copy url")

**Syntax:** obj \<\< Fit Details( state=0\|1 )

**Description:** Shows or hides the statistics for the fitted model. On by default.

**JMP Version Added:** 18

#### [Lift Curves](#lift-curves)[](#lift-curves "Click to copy url")

**Syntax:** obj \<\< Lift Curves( state=0\|1 )

**Description:** Plots how much more saturated the top x-percent of predicted values are compared to the whole population.

**JMP Version Added:** 18

#### [Model Details](#model-details)[](#model-details "Click to copy url")

**Syntax:** obj \<\< Model Details( state=0\|1 )

**Description:** Shows or hides model details On by default.

**JMP Version Added:** 18

#### [Precision Recall Curves](#precision-recall-curves)[](#precision-recall-curves "Click to copy url")

**Syntax:** obj \<\< Precision Recall Curves( state=0\|1 )

**Description:** Plots the trade-off between precision and recall for different classification thresholds. It is preferred in scenarios where class imbalances exist.

**JMP Version Added:** 18

#### [Profiler](#profiler)[](#profiler "Click to copy url")

**Syntax:** obj \<\< Profiler

**Description:** Shows or hides the Prediction Profiler.

**JMP Version Added:** 18

#### [ROC Curves](#roc-curves)[](#roc-curves "Click to copy url")

**Syntax:** obj \<\< ROC Curves( state=0\|1 )

**Description:** Plots the response-category sorting efficiency of the model predictions.

**JMP Version Added:** 18

#### [Surface Profiler](#surface-profiler)[](#surface-profiler "Click to copy url")

**Syntax:** obj \<\< Surface Profiler

**Description:** Shows or hides interactive graphs of cross-sections of the prediction function.

**JMP Version Added:** 18

## [Torch Deep Learning Fit](#torch-deep-learning-fit)[](#torch-deep-learning-fit "Click to copy url")

### [Associated Constructors](#associated-constructors_2)[](#associated-constructors_2 "Click to copy url")

#### [Post](#post)[](#post "Click to copy url")

**Syntax:** Post

#### [Torch Deep Learning Fit](#torch-deep-learning-fit_1)[](#torch-deep-learning-fit_1 "Click to copy url")

**Syntax:** Torch Deep Learning Fit

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [Activation](#activation)[](#activation "Click to copy url")

**Syntax:** obj \<\< Activation( "CELU"\|"ELU"\|"GELU"\|"Hardshrink"\|"Hardtanh"\|"LeakyReLU"\|"LogSigmoid"\|"Mish"\|"PReLU"\|"ReLU"\|"ReLU6"\|"RReLU"\|"SELU"\|"Sigmoid"\|"SiLU"\|"Softplus"\|"Softshrink"\|"Softsign"\|"Tanh"\|"Tanhshrink"\|"None"="ReLU" )

**Description:** Specifies the activation function to use after each layer. "ReLU" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Activation( "ReLU" ) ) );
```

#### [Activations](#activations)[](#activations "Click to copy url")

**Syntax:** obj \<\< Activations( text )

**Description:** Specifies a space-delimited list of activation functions to use in sequential layers. This parameter overrides Activation when it is specified, and the last value carries forward.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Activations( "ReLU" ) ) );
```

#### [Anchor Scale](#anchor-scale)[](#anchor-scale "Click to copy url")

**Syntax:** obj \<\< Anchor Scale( number=16 )

**Description:** Specifies a multiplier applied to an internal range of anchor sizes. Larger values tend to work better for larger boxes. "16" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Anchor Scale( "16" ) ) );
```

#### [Aspect Sigma](#aspect-sigma)[](#aspect-sigma "Click to copy url")

**Syntax:** obj \<\< Aspect Sigma( number=0 )

**Description:** Standard deviation of Gaussian aspect ratio deformation "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Aspect Sigma( 0.0 ) ) );
```

#### [Attention Heads](#attention-heads)[](#attention-heads "Click to copy url")

**Syntax:** obj \<\< Attention Heads( text=4 )

**Description:** For transformer models, specifies the number of attention heads as a space delimited list of positive integers, each of which must evenly divide its corresponding layer size. Last value carries forward if necessary. "4" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Attention Heads( 1 ) ) );
```

#### [Base Activation](#base-activation)[](#base-activation "Click to copy url")

**Syntax:** obj \<\< Base Activation( "CELU"\|"ELU"\|"GELU"\|"Hardshrink"\|"Hardtanh"\|"LeakyReLU"\|"LogSigmoid"\|"Mish"\|"PReLU"\|"ReLU"\|"ReLU6"\|"RReLU"\|"SELU"\|"Sigmoid"\|"SiLU"\|"Softplus"\|"Softshrink"\|"Softsign"\|"Tanh"\|"Tanhshrink"\|"None"="GELU" )

**Description:** Specifies the base activation function for Kolmogorov Arnold B Splines. "GELU" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Base Activation( "GELU" ) ) );
```

#### [Basis Function](#basis-function)[](#basis-function "Click to copy url")

**Syntax:** obj \<\< Basis Function( "Gaussian"\|"Linear"\|"Quadradic"\|"InverseQuadradic"\|"MultiQuadric"\|"InverseMultiQuadric"\|"Spline"\|"Poisson1"\|"Poisson2"\|"Matern32"\|"Matern52"="Gaussian" )

**Description:** For Radial Basis Machine models, specify the basis function. "Gaussian" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning(
    Y( :sex ),
    X( :height, :weight ),
    Fit( Tabular Model( "RadialBasisMachine" ), Basis Function( "Gaussian" ) )
);
```

#### [Batch Size](#batch-size)[](#batch-size "Click to copy url")

**Syntax:** obj \<\< Batch Size( number=128 )

**Description:** Specifies the number of rows to randomly sample for each training batch and optimization update. Decrease it to save memory and update gradients more frequently; increase it to pass through the data faster and regularize the model more. "128" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Batch Size( 128 ) ) );
```

#### [Binary Loss](#binary-loss)[](#binary-loss "Click to copy url")

**Syntax:** obj \<\< Binary Loss( "BCE"\|"SM"="BCE" )

**Description:** Specifies the loss function for binary responses. Choose from Binary Cross Entropy (BCE) or Soft Margin (SM). "BCE" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Binary Loss( "BCE" ) ) );
```

#### [Blur Max Sigma](#blur-max-sigma)[](#blur-max-sigma "Click to copy url")

**Syntax:** obj \<\< Blur Max Sigma( number=0 )

**Description:** Maximum standard deviation of Gaussian blur "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Blur Max Sigma( 1 ) ) );
```

#### [Class Loss Weight](#class-loss-weight)[](#class-loss-weight "Click to copy url")

**Syntax:** obj \<\< Class Loss Weight( number=4.0 )

**Description:** Specifies the multiplier for class loss. "4.0" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Class Loss Weight( 4.0 ) ) );
```

#### [Confidence Threshold](#confidence-threshold)[](#confidence-threshold "Click to copy url")

**Syntax:** obj \<\< Confidence Threshold( number=0.05 )

**Description:** Specifies the confidence score threshold for predicted boxes. Boxes with probability score less than this threshold are dropped. "0.05" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Confidence Threshold( 0.05 ) ) );
```

#### [Continuous Loss](#continuous-loss)[](#continuous-loss "Click to copy url")

**Syntax:** obj \<\< Continuous Loss( "MSE"\|"L1"\|"SmoothL1"\|"Huber"\|"Poisson"\|"Quantile"\|"CoxPH"="MSE" )

**Description:** Specifies the loss function for continuous responses. Choose from Mean Squared Error (MSE), Mean Absolute Error (L1), Smoothed L1 (with margin), Huber (with margin), or Poisson (for count responses). "MSE" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :weight ), X( :picture ), Fit( Continuous Loss( "MSE" ) ) );
```

#### [Copy Parameters to Launch](#copy-parameters-to-launch)[](#copy-parameters-to-launch "Click to copy url")

**Syntax:** obj \<\< Copy Parameters to Launch

**Description:** Copies the parameter values from this model to the model launch section.

**JMP Version Added:** 18

#### [Covariance Structure](#covariance-structure)[](#covariance-structure "Click to copy url")

**Syntax:** obj \<\< Covariance Structure( "DotProduct"\|"Gaussian"="DotProduct" )

**Description:** For mixed models, specify the covariance structure. "DotProduct" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning(
    Y( :sex ),
    X( :height, :weight ),
    Fit( Tabular Model( "MixedModel" ), Covariance Structure( "DotProduct" ) )
);
```

#### [Data Threads](#data-threads)[](#data-threads "Click to copy url")

**Syntax:** obj \<\< Data Threads( number=4 )

**Description:** Specifies the number of threads to use to load data into memory. A number near half the number of actual cores is usually near optimal. "4" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Data Threads( 0 ) ) );
```

#### [Device](#device)[](#device "Click to copy url")

**Syntax:** obj \<\< Device( "auto"\|"cpu"\|"cuda:0"\|"cuda:1"\|"cuda:2"\|"cuda:3"="auto" )

**Description:** Specifies the computational device that Torch uses. "auto" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Device( "cpu" ) ) );
```

#### [Dilations](#dilations)[](#dilations "Click to copy url")

**Syntax:** obj \<\< Dilations( text=1 )

**Description:** For custom convolutional models, specifies the dilations as a space-delimited list of positive integers. Last value carries forward if necessary. "1" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Dilations( "1" ) ) );
```

#### [Dropout Probs](#dropout-probs)[](#dropout-probs "Click to copy url")

**Syntax:** obj \<\< Dropout Probs( text=0.0 )

**Description:** Specifies the probabilities of dropout to use after each layer as a space-delimited list of decimals between 0 and 1. Last value carries forward if necessary. "0.0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Dropout Probs( "0.1" ) ) );
```

#### [Epochs](#epochs)[](#epochs "Click to copy url")

**Syntax:** obj \<\< Epochs( number=20 )

**Description:** Specifies the number of iterations through the training data to optimize the loss function for each batch and train the model. "20" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Epochs( 100 ) ) );
```

#### [Factorization Machine Layers](#factorization-machine-layers)[](#factorization-machine-layers "Click to copy url")

**Syntax:** obj \<\< Factorization Machine Layers( text=0 )

**Description:** Specify a space-separated list of 0s and 1s indicating if factorization machine interactions should be added to each linear layer. Last value carries forward. "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning(
    Y( :sex ),
    X( :height, :weight ),
    Fit( Factorization Machine Layers( "1" ) )
);
```

#### [Fit Ys Separately](#fit-ys-separately)[](#fit-ys-separately "Click to copy url")

**Syntax:** obj \<\< Fit Ys Separately( state=0 )

**Description:** Check to fit a distinct model for each Y variable, and uncheck to model them jointly. "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex, :height ), X( :picture ), Fit( Model Ys Separately( 1 ) ) );
```

#### [Fixed Effects](#fixed-effects)[](#fixed-effects "Click to copy url")

**Syntax:** obj \<\< Fixed Effects( number=0 )

**Description:** Specify the number of fixed effects, all of which must be at the beginning of the X variable list "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Fixed Effects( 0 ) ) );
```

#### [Folder](#folder)[](#folder "Click to copy url")

**Syntax:** obj \<\< Folder( text )

**Description:** Select a folder in which to save modeling results. A subfolder for each model is created in this folder.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Folder( "" ) ) );
```

#### [Frozen Epochs](#frozen-epochs)[](#frozen-epochs "Click to copy url")

**Syntax:** obj \<\< Frozen Epochs( number=0 )

**Description:** Specifies the number of epochs for which pretrained model bodies remain frozen. After this number there is full training gradients for all parameters. "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Frozen Epochs( 3 ) ) );
```

#### [Generate Python Code](#generate-python-code)[](#generate-python-code "Click to copy url")

**Syntax:** obj \<\< Generate Python Code

**Description:** Creates Python code for model deployment.

**JMP Version Added:** 18

#### [Grid Size](#grid-size)[](#grid-size "Click to copy url")

**Syntax:** obj \<\< Grid Size( number=5 )

**Description:** For Kolmogorov Arnold B Spline networks, specifies the number of points in the grid for the spline interpolation. "5" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Grid Size( 5 ) ) );
```

#### [HFlip Prob](#hflip-prob)[](#hflip-prob "Click to copy url")

**Syntax:** obj \<\< HFlip Prob( number=0 )

**Description:** Probability of horizontal flip "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( HFlip Prob( 0.3 ) ) );
```

#### [Highway Layers](#highway-layers)[](#highway-layers "Click to copy url")

**Syntax:** obj \<\< Highway Layers( text=0 )

**Description:** Specify a space-separated list of nonnegative integers specifying the number of highway layers to insert in the network. Last value carries forward. "0" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Highway Layers( "1" ) ) );
```

#### [Image Model](#image-model)[](#image-model "Click to copy url")

**Syntax:** obj \<\< Image Model( ="LeNet5" )

**Description:** Specifies the image network architecture to use. Models are ordered by size. Smaller models train faster but may not perform as well as larger models. "LeNet5" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Image Model( "LeNet5" ) ) );
```

#### [Image Size](#image-size)[](#image-size "Click to copy url")

**Syntax:** obj \<\< Image Size( number=28 )

**Description:** Specifies the size of image to use while training. Input images are transformed to this size square; larger images have higher resolution but slower training times. "28" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Image Size( 28 ) ) );
```

#### [Kernel Sizes](#kernel-sizes)[](#kernel-sizes "Click to copy url")

**Syntax:** obj \<\< Kernel Sizes( text=3 )

**Description:** For custom convolutional models, specifies the kernel sizes as a space-delimited list of positive integers. Last value carries forward if necessary. "3" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Kernel Sizes( "3" ) ) );
```

#### [L1 Penalty](#l1-penalty)[](#l1-penalty "Click to copy url")

**Syntax:** obj \<\< L1 Penalty( number=0.0 )

**Description:** Specifies a multiplier for the sum of absolute values of weight parameters to be added to the loss and induce sparsity. "0.0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( L1 Penalty( 0.0001 ) ) );
```

#### [Layer Sizes](#layer-sizes)[](#layer-sizes "Click to copy url")

**Syntax:** obj \<\< Layer Sizes( text=16 )

**Description:** Specifies output sizes of hidden layers as a space-delimited list of integers (actual sizes) or decimals (multipliers of the previous layer size). The final value is the embedding size. "16" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Layer Sizes( "16" ) ) );
```

#### [Learning Rate](#learning-rate)[](#learning-rate "Click to copy url")

**Syntax:** obj \<\< Learning Rate( number=0.001 )

**Description:** Specifies the learning rate. Smaller learning rates tend to fit better but require more iterations to converge, whereas larger learning rates fit faster. "0.001" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Learning Rate( 0.001 ) ) );
```

#### [Margin](#margin)[](#margin "Click to copy url")

**Syntax:** obj \<\< Margin( number=1.0 )

**Description:** Specifies the margin used in margin-based loss functions. Larger values should produce larger embedding distances between nominal responses with different levels, but may adversely affect training. "1.0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Margin( 1.0 ) ) );
```

#### [Max Boxes](#max-boxes)[](#max-boxes "Click to copy url")

**Syntax:** obj \<\< Max Boxes( number=5 )

**Description:** Specifies the maximum number of predicted boxes per image. "5" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Max Boxes( 5 ) ) );
```

#### [Max Seq Length](#max-seq-length)[](#max-seq-length "Click to copy url")

**Syntax:** obj \<\< Max Seq Length( number=512 )

**Description:** For text models, specifies the maximum number of tokens to create for each text item. "512" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Chips.jmp" );
Torch Deep Learning(
    Y( :Buy again? ),
    X( :Potato Chip Product Review ),
    Fit( Max Seq Length( 512 ) )
);
```

#### [Mixup Portion](#mixup-portion)[](#mixup-portion "Click to copy url")

**Syntax:** obj \<\< Mixup Portion( number=0.0 )

**Description:** Specifies portion of mixup samples to add to each training batch. For example, if Batch Size is 128 and Mixup Portion is 0.5, then 64 mixup samples are added. "0.0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Mixup Portion( 0.5 ) ) );
```

#### [NMS Threshold](#nms-threshold)[](#nms-threshold "Click to copy url")

**Syntax:** obj \<\< NMS Threshold( number=0.5 )

**Description:** Specifies the non-maximum suppression threshold for predicted boxes. Overlapping boxes with IOU values above this threshold are dropped. "0.5" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( NMS Threshold( 0.5 ) ) );
```

#### [Noise Max Sigma](#noise-max-sigma)[](#noise-max-sigma "Click to copy url")

**Syntax:** obj \<\< Noise Max Sigma( number=0 )

**Description:** Maximum standard deviation of additive Gaussian noise "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Noise Max Sigma( 1 ) ) );
```

#### [Nominal Image Threshold](#nominal-image-threshold)[](#nominal-image-threshold "Click to copy url")

**Syntax:** obj \<\< Nominal Image Threshold( number=10 )

**Description:** Specifies the cutoff for determining if images in a column are nominal or continuous. If the number of unique pixel levels is \<= this number, then the images are considered to be nominal. "10" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Nominal Image Threshold( 10 ) ) );
```

#### [Nominal Loss](#nominal-loss)[](#nominal-loss "Click to copy url")

**Syntax:** obj \<\< Nominal Loss( "NLL"="NLL" )

**Description:** Specifies the loss function for nominal responses. Choose from Negative Loglikelihood (NLL). "NLL" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Nominal Loss( "NLL" ) ) );
```

#### [Norm](#norm)[](#norm "Click to copy url")

**Syntax:** obj \<\< Norm( "None"\|"Batch"\|"Group"\|"Instance"="Batch" )

**Description:** Specifies the type of normalization to apply to each MLP layer. "Batch" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Norm( "Batch" ) ) );
```

#### [Norm First](#norm-first)[](#norm-first "Click to copy url")

**Syntax:** obj \<\< Norm First( "None"\|"Batch"="Batch" )

**Description:** Specifies the type of normalization to apply to the input data to the tabular model. Batch norm effectively centers and scales each input. "Batch" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Norm First( "Batch" ) ) );
```

#### [Num Linear](#num-linear)[](#num-linear "Click to copy url")

**Syntax:** obj \<\< Num Linear( number=1 )

**Description:** For custom convolutional and message passing models, specifies the number of linear layers at the end of Layer Sizes. "1" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Num Linear( 1 ) ) );
```

#### [Optimizer](#optimizer)[](#optimizer "Click to copy url")

**Syntax:** obj \<\< Optimizer( "Adam"\|"AdamW"\|"SGD"\|"SGDAGC"="AdamW" )

**Description:** Specifies the optimization method. Choose between Adaptive moment estimation (Adam), Adam weight decay (AdamW), Stochastic Gradient Descent (SGD), or SGD with Adaptive Gradient Clipping (SGDAGC). "AdamW" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Optimizer( "AdamW" ) ) );
```

#### [Pitch Sigma](#pitch-sigma)[](#pitch-sigma "Click to copy url")

**Syntax:** obj \<\< Pitch Sigma( number=0 )

**Description:** Standard deviation of Gaussian pitch "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Pitch Sigma( 5 ) ) );
```

#### [Pooling Layers](#pooling-layers)[](#pooling-layers "Click to copy url")

**Syntax:** obj \<\< Pooling Layers( text=Max )

**Description:** Specifies pooling layers as a space-delimited list of one of four keywords: Max, Avg, Cat, or None. Last value carries forward if necessary. "Max" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Pooling Layers( "Max" ) ) );
```

#### [Pretrained Tabular](#pretrained-tabular)[](#pretrained-tabular "Click to copy url")

**Syntax:** obj \<\< Pretrained Tabular( ="None" )

**Description:** Specify a pretrained tabular model that is prepended to the Tabular Model. "None" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Pretrained Tabular( "None" ) ) );
```

#### [Quantiles](#quantiles)[](#quantiles "Click to copy url")

**Syntax:** obj \<\< Quantiles( text=0.9 )

**Description:** Specify a space-delimited list of quantiles to use for Quantile loss. "0.9" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Quantiles( "0.9" ) ) );
```

#### [RPN NMS Threshold](#rpn-nms-threshold)[](#rpn-nms-threshold "Click to copy url")

**Syntax:** obj \<\< RPN NMS Threshold( number=0.7 )

**Description:** Specifies the non-maximum suppression threshold for region proposals. Overlapping boxes with IOU values above this threshold are dropped. "0.7" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( RPN NMS Threshold( 0.7 ) ) );
```

#### [Remove All But This Fit](#remove-all-but-this-fit)[](#remove-all-but-this-fit "Click to copy url")

**Syntax:** obj \<\< ( fit\[number\] \<\< Remove All But This Fit )

**Description:** Removes the reports and plots for all models except this one.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Torch Deep Learning(
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

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Torch Deep Learning(
    Y( :Species ),
    X( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    Fit
);
Wait( 2 );
obj << (Fit[1] << Remove Fit);
```

#### [Restore From](#restore-from)[](#restore-from "Click to copy url")

**Syntax:** obj \<\< Restore From( " "=" " )

**Description:** Select a subfolder containing saved files from a previously fit model. Training for a new model will begin where this model finished. Model architectures and validation variables should match. Leave this field blank to train from scratch. " " by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Restore From( "" ) ) );
```

#### [Roll Sigma](#roll-sigma)[](#roll-sigma "Click to copy url")

**Syntax:** obj \<\< Roll Sigma( number=0 )

**Description:** Standard deviation of Gaussian roll "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Roll Sigma( 5 ) ) );
```

#### [Save CAMs](#save-cams)[](#save-cams "Click to copy url")

**Syntax:** obj \<\< Save CAMs

**Description:** Save gradient-based class activation maps (CAMs) as a new column.

**JMP Version Added:** 18

#### [Save Embeddings](#save-embeddings)[](#save-embeddings "Click to copy url")

**Syntax:** obj \<\< Save Embeddings

**Description:** Saves model embeddings (from final hidden layer) as new columns in the data table

**JMP Version Added:** 18

#### [Save Model](#save-model)[](#save-model "Click to copy url")

**Syntax:** obj \<\< Save Model

**Description:** Saves serialized modeling components to disk in a folder that you name. You can then specify this folder in Restore From to begin training with this model.

**JMP Version Added:** 18

#### [Save Predicteds](#save-predicteds)[](#save-predicteds "Click to copy url")

**Syntax:** obj \<\< Save Predicteds

**Description:** Saves the predicted values in a new column in the data table.

**JMP Version Added:** 18

#### [Screening Method](#screening-method)[](#screening-method "Click to copy url")

**Syntax:** obj \<\< Screening Method( "ResponseScreening"\|"BootstrapForest"="ResponseScreening" )

**Description:** Choose a method by which to screen Tabular Model predictors prior to fitting the model within each fold. ResponseScreening is fast and BootstrapForest is more thorough. "ResponseScreening" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning(
    Y( :sex ),
    X( :picture ),
    Fit( Screening Method( "ResponseScreening" ) )
);
```

#### [Screening Threshold](#screening-threshold)[](#screening-threshold "Click to copy url")

**Syntax:** obj \<\< Screening Threshold( number=0 )

**Description:** If \>= 1, the number of Tabular Model predictors to select by screening. If \< 1, the predictors with cumulative portion less than the threshold. "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Screening Threshold( 1 ) ) );
```

#### [Seed](#seed)[](#seed "Click to copy url")

**Syntax:** obj \<\< Seed( number=0 )

**Description:** Specifies the seed for the random number generator. Note results may not be fully reproducible with the same seed due to the stochastic nature of certain Torch calculations. "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Seed( 0 ) ) );
```

#### [Segmentation Model](#segmentation-model)[](#segmentation-model "Click to copy url")

**Syntax:** obj \<\< Segmentation Model( "UNet"\|"FPN"\|"LinkNet"\|"DeepLabV3"\|"DeepLabV3Plus"\|"PAN"\|"PSPNet"="UNet" )

**Description:** Specifies the image segmentation model. "UNet" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/segmentation.jmp" );
Torch Deep Learning( Y( :Mask ), X( :Picture ), Sett( Segmentation Model( "VGG11_BN" ) ) );
```

#### [Spline Order](#spline-order)[](#spline-order "Click to copy url")

**Syntax:** obj \<\< Spline Order( number=3 )

**Description:** For Kolmogorov Arnold B Spline networks, specifies the order of the spline used for interpolation. "3" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Spline Order( 3 ) ) );
```

#### [Strides](#strides)[](#strides "Click to copy url")

**Syntax:** obj \<\< Strides( text=1 )

**Description:** For custom convolutional models, specifies the strides as a space-delimited list of positive integers. Last value carries forward if necessary. "1" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :height, :weight ), Fit( Strides( "1" ) ) );
```

#### [Tabular Model](#tabular-model)[](#tabular-model "Click to copy url")

**Syntax:** obj \<\< Tabular Model( "MultiLayerPerceptron"\|"FTTransformer"\|"KolmogorovArnoldBSpline"\|"CustomConv1d"\|"LSTM"\|"RadialBasisMachine"\|"MixedModel"="MultiLayerPerceptron" )

**Description:** Specifies the tabular network architecture to use. Choose from Multilayer Perceptron (MLP), Feature Tokenized Transformer (FTTransformer), Kolmogorov Arnold Network (KolmogorovArnoldBSpline), or other options "MultiLayerPerceptron" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning(
    Y( :sex ),
    X( :picture ),
    Fit( Tabular Model( "MultiLayerPerceptron" ) )
);
```

#### [Text Model](#text-model)[](#text-model "Click to copy url")

**Syntax:** obj \<\< Text Model( ="BertTiny" )

**Description:** Specifies the text network architecture to use. Models are ordered by size. Smaller models train faster but may not perform as well as larger models. "BertTiny" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Chips.jmp" );
Torch Deep Learning(
    Y( :Buy again? ),
    X( :Potato Chip Product Review ),
    Fit( Text Model( "BERT" ) )
);
```

#### [Triplet Loss Weight](#triplet-loss-weight)[](#triplet-loss-weight "Click to copy url")

**Syntax:** obj \<\< Triplet Loss Weight( number=0.0 )

**Description:** Specifies the multiplier alpha to use in the following compound loss function: alpha \* triplet_loss + (1 - alpha) \* loss_function. Must be between 0 and 1. "0.0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Triplet Loss Weight( 0.5 ) ) );
```

#### [Use Data As Knots](#use-data-as-knots)[](#use-data-as-knots "Click to copy url")

**Syntax:** obj \<\< Use Data As Knots( state=0 )

**Description:** For Radial Basis Machine models, check to use the training data as knots to form an interpolation-style model. "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning(
    Y( :sex, :height ),
    X( :picture ),
    Fit( Tabular Model( "Radial Basis Machine" ), Use Data As Knots( 1 ) )
);
```

#### [VFlip Prob](#vflip-prob)[](#vflip-prob "Click to copy url")

**Syntax:** obj \<\< VFlip Prob( number=0 )

**Description:** Probability of vertical flip "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( VFlip Prob( 0.2 ) ) );
```

#### [Weight Decay](#weight-decay)[](#weight-decay "Click to copy url")

**Syntax:** obj \<\< Weight Decay( number=0.0 )

**Description:** Specifies a penalty term multiplier of the L2 norm of the trainable parameters, which regularizes them in a way similar to ridge regression. "0.0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Weight Decay( 0.0001 ) ) );
```

#### [Worker Count](#worker-count)[](#worker-count "Click to copy url")

**Syntax:** obj \<\< Worker Count( number=4 )

**Description:** Specifies the number of workers to use to load batches of data during training. A number near half the number of actual cores is usually near optimal. "4" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Worker Count( 0 ) ) );
```

#### [X Slide Sigma](#x-slide-sigma)[](#x-slide-sigma "Click to copy url")

**Syntax:** obj \<\< X Slide Sigma( number=0 )

**Description:** Standard deviation of Gaussian random shift along the X axis "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( X Slide Sigma( 5 ) ) );
```

#### [Y Slide Sigma](#y-slide-sigma)[](#y-slide-sigma "Click to copy url")

**Syntax:** obj \<\< Y Slide Sigma( number=0 )

**Description:** Standard deviation of Gaussian random shift along the Y axis "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Y Slide Sigma( 5 ) ) );
```

#### [Yaw Sigma](#yaw-sigma)[](#yaw-sigma "Click to copy url")

**Syntax:** obj \<\< Yaw Sigma( number=0 )

**Description:** Standard deviation of Gaussian yaw "0" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
Torch Deep Learning( Y( :sex ), X( :picture ), Fit( Yaw Sigma( 5 ) ) );
```

[ Previous](Titled%20List%20Box.html "Titled List Box") [Next ](Tree%20Node.html "Tree Node")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
