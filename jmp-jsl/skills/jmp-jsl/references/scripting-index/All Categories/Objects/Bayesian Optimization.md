# Bayesian Optimization

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Bayesian%20Optimization.html](https://jsl.jmp.com/All%20Categories/Objects/Bayesian%20Optimization.html)*

---

# [Bayesian Optimization](#bayesian-optimization)[](#bayesian-optimization "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Bayesian Optimization](#bayesian-optimization_1)[](#bayesian-optimization_1 "Click to copy url")

**Syntax:** Bayesian Optimization( Y( columns ), X( columns ) )

**Description:** Recommends factor settings to optimize responses by augmenting the data table.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
```

## [Columns](#columns)[](#columns "Click to copy url")

### [Iteration](#iteration)[](#iteration "Click to copy url")

**Syntax:** obj \<\< Iteration( column )

**Description:** Specifies a batch label column. Batches are expected to be labeled 0, 1, 2, ..., where batch 0 indicates the original training data.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
dt << New Column( "_itercol",
    Numeric,
    Ordinal,
    set values( V Concat( (Repeat( 0, N Rows( dt ) - 10 )), Repeat( 1, 10 ) ) )
);
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Iteration( _itercol )
);
```

### [Run Order](#run-order)[](#run-order "Click to copy url")

**Syntax:** obj \<\< Run Order( column )

**Description:** Specifies a permutation column of row numbers that indicate the order of observations.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
dt << New Column( "_runorder", Numeric, Ordinal, set values( 1 :: (N Rows( dt )) ) );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Run Order( _runorder )
);
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** obj \<\< X( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Automatically Generate a Batch](#automatically-generate-a-batch)[](#automatically-generate-a-batch "Click to copy url")

**Syntax:** obj \<\< Automatically Generate a Batch( state=0\|1 )

**Description:** Indicates whether to run automatic candidate set generation and batch selection. Optionally, you can specify which method to use to select batches. This option is equivalent to specifying both the Generate Candidate Set option and Autoselect Batch option at the same time.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Automatically Generate a Batch( 1 )
);
```

### [Autoselect Batch](#autoselect-batch)[](#autoselect-batch "Click to copy url")

**Syntax:** obj \<\< Autoselect Batch( state=0\|1 )

**Description:** Selects a batch from the currently loaded candidate set. If no candidate set is loaded, a space-filling set of size 1000 times the number of input variables is generated. This option can also be used to turn off auto batch selection on launch.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Generate Candidate Set(
        Candidate Set Size( 10 ),
        Include Runs that Do Not Conform to Constraints( 0 )
    ),
    Autoselect Batch( Batch Size( 1 ), Minimum RSquare( 0.5 ) )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Generate Candidate Set(
        Candidate Set Size( 10 ),
        Include Runs that Do Not Conform to Constraints( 0 )
    ),
    Autoselect Batch( 0 )
);
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Automatically Generate a Batch( 0 )
);
obj << Autoselect Batch( Batch Size( 5 ), Augmentation Method( Space Filling Exploration ) );
```

### [Batch Size](#batch-size)[](#batch-size "Click to copy url")

**Syntax:** obj \<\< Batch Size( number )

**Description:** Specifies the batch size to autoselect on launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Batch Size( 5 )
);
```

### [Candidate Set Size](#candidate-set-size)[](#candidate-set-size "Click to copy url")

**Syntax:** obj \<\< Candidate Set Size( number )

**Description:** Specifies the desired candidate set size to generate.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Candidate Set Size( 10 )
);
```

### [Continuous Correlation Type](#continuous-correlation-type)[](#continuous-correlation-type "Click to copy url")

**Syntax:** obj \<\< Continuous Correlation Type( "Gaussian"\|"Matern 3/2"\|"Matern 5/2"\|"Exponential" )

**Description:** Specifies the desired kernel for continuous input variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Continuous Correlation Type( "Matern 5/2" )
);
```

### [Generate Candidate Set](#generate-candidate-set)[](#generate-candidate-set "Click to copy url")

**Syntax:** obj \<\< Generate Candidate Set( Candidate Set Size( number ), \<Include Runs that Do Not Conform to Constraints( state = 0\|1 )\> )

**Description:** Generates a candidate set. You can provide candidate set size and specify whether to allow points that violate the linear constraints in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Generate Candidate Set(
        Candidate Set Size( 10 ),
        Include Runs that Do Not Conform to Constraints( 0 )
    )
);
```

### [Include Runs that Do Not Conform to Constraints](#include-runs-that-do-not-conform-to-constraints)[](#include-runs-that-do-not-conform-to-constraints "Click to copy url")

**Syntax:** obj \<\< Include Runs that Do Not Conform to Constraints( state=0\|1 )

**Description:** Specifies whether to include points that violate the linear constraints in the data table when generating or loading a candidate set.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Include Runs that Do Not Conform to Constraints( 0 )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
dtCand = New Table( "Tiretread Candidate Set",
    Add Rows( 15 ),
    New Column( "SILICA",
        Continuous,
        Set Values(
            [1.2, 1.60825, 0.79175, 0.995875, 1.812375, 1.404125, 0.587625, 0.6896875,
            1.5061875, 1.9144375, 1.0979375, 0.8938125, 1.7103125, 1.3020625, 0.4855625]
        )
    ),
    New Column( "SILANE",
        Continuous,
        Set Values(
            [50, 41.835, 58.165, 45.9175, 62.2475, 37.7525, 54.0825, 43.87625, 60.20625,
            35.71125, 52.04125, 39.79375, 56.12375, 47.95875, 64.28875]
        )
    ),
    New Column( "SULFUR",
        Continuous,
        Set Values(
            [2.3, 1.89175, 2.70825, 2.504125, 1.687625, 2.912375, 2.095875, 3.0144375,
            2.1979375, 2.6061875, 1.7896875, 1.9938125, 2.8103125, 1.5855625, 2.4020625]
        )
    )
);
dt << New Script( "Constraint", {:SILICA + :SULFUR <= 3} );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Include Runs that Do Not Conform to Constraints( 0 ),
    Load Candidate Set from Data Table( dtCand )
);
```

### [Minimum RSquare](#minimum-rsquare)[](#minimum-rsquare "Click to copy url")

**Syntax:** obj \<\< Minimum RSquare( number )

**Description:** Specifies the minimum required R-square metric for the batch autoselection algorithm. In the Bayesian Optimization platform launch window, this option is referred to as Model Based Augmentation RSquare Threshold.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Minimum RSquare( 0.25 )
);
```

### [Nominal Correlation Type](#nominal-correlation-type)[](#nominal-correlation-type "Click to copy url")

**Syntax:** obj \<\< Nominal Correlation Type( "Equal Correlations"\|"Unequal Correlations" )

**Description:** Specifies the desired kernel for nominal input variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Nominal Correlation Type( "Equal Correlations" )
);
```

### [Ordinal Correlation Type](#ordinal-correlation-type)[](#ordinal-correlation-type "Click to copy url")

**Syntax:** obj \<\< Ordinal Correlation Type( "Equal Correlations"\|"Unequal Correlations"\|"Latent Variable" )

**Description:** Specifies the desired kernel for ordinal input variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Ordinal Correlation Type( "Equal Correlations" )
);
```

### [Save Prediction Formula](#save-prediction-formula)[](#save-prediction-formula "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the prediction formula to a new column in the data table.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Save Prediction Formula;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Save Prediction Formula( Elong );
```

### [Set Tab](#set-tab)[](#set-tab "Click to copy url")

**Syntax:** obj \<\< Set Tab( number )

**Description:** Specifies the current tab. The argument interprets 0 as the Model Summary tab, 1 as Batch Selection, and so on, in the order in which the tabs appear in the report window.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << set tab( 1 );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << set tab( "ABRASION" );
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Report View( "Summary" );
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
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
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
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

## [Bayesian Optimization Batch Customizer \> Candidate Set View](#bayesian-optimization-batch-customizer-candidate-set-view)[](#bayesian-optimization-batch-customizer-candidate-set-view "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Export Candidate Set to Data Table](#export-candidate-set-to-data-table)[](#export-candidate-set-to-data-table "Click to copy url")

**Syntax:** obj \<\< Export Candidate Set to Data Table

**Description:** Exports the currently loaded candidate set to a new data table. You can specify desired column groups as arguments. This option exports factor settings by default if no column groups provided. If no arguments are specified, a window appears where you can specify options.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Export Candidate Set to Data Table( Go );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Export Candidate Set to Data Table();
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Export Candidate Set to Data Table(
    Order Added, Factor Settings, Bayesian Desirability, Bayesian Desirability Std Dev,
    Multimodel Prediction Std Dev, MaxPro Space Filling Criterion,
    Bayesian Desirability Expected Improvement, Bayesian Desirability Upper Confidence Bound,
    Training Response Predictions, Augmented Response Prediction Std Dev,
    Augmented Response Prediction Confidence Intervals
);
```

#### [Select Runs](#select-runs)[](#select-runs "Click to copy url")

**Syntax:** obj \<\< Select Runs( Row Index( \[ numbers \] ), \<Order Added( \[ numbers \]\>, \<Reason Added( { text } )\>, \<Replace( 0\|1 )\> )

**Description:** Selects rows from the candidate set table to add to the current batch.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Select Runs(
        Row Index( [3 5] ),
        Order Added( [1 2] ),
        Reason Added( {"Custom Reason", "Custom Reason"} ),
        Replace( 1 )
    )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    autoselect batch( 0 )
);
obj << Select Runs(
    Row Index( [3 5] ),
    Order Added( [1 2] ),
    Reason Added( {"Custom Reason", "Custom Reason"} ),
    Replace( 0 )
);
```

#### [Show Table Columns](#show-table-columns)[](#show-table-columns "Click to copy url")

**Syntax:** obj \<\< Show Table Columns( \<"Column Group Name"\>,... )

**Description:** Specifies which groups of columns are visible in the candidate set table.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Show Table Columns( Order Added, Factor Settings, Bayesian Desirability )
);
```

## [Bayesian Optimization Batch Customizer](#bayesian-optimization-batch-customizer)[](#bayesian-optimization-batch-customizer "Click to copy url")

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Add Current Profiler Settings to Batch](#add-current-profiler-settings-to-batch)[](#add-current-profiler-settings-to-batch "Click to copy url")

**Syntax:** obj \<\< Add Current Profiler Settings to Batch

**Description:** Adds the current profiler settings to the candidate set and selects it for inclusion as a run in the next augmentation batch.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Add Current Profiler Settings to Batch;
```

#### [Augmented Acquisition Functions Profiler](#augmented-acquisition-functions-profiler)[](#augmented-acquisition-functions-profiler "Click to copy url")

**Syntax:** obj \<\< Augmented Acquisition Functions Profiler( state=0\|1 )

**Description:** Shows or hides a profiler that enables you to explore how each acquisition function changes with respect to changes in each factor value. Functions are conditional on the assumption that the points in the current batch will be sampled. This profiler reflects changes to factor levels and desirability functions made in the Augmented Prediction Profiler.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Augmented Acquisition Functions Profiler( 0 );
```

#### [Augmented Prediction Profiler](#augmented-prediction-profiler)[](#augmented-prediction-profiler "Click to copy url")

**Syntax:** obj \<\< Augmented Prediction Profiler( state=0\|1 )

**Description:** Shows or hides a profiler that enables you to explore how each column changes with respect to changes in each factor value across models. Predictions are conditional on the assumption that the points in the current batch will be sampled.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Augmented Prediction Profiler( 0 );
```

#### [Deselect All](#deselect-all)[](#deselect-all "Click to copy url")

**Syntax:** obj \<\< Deselect All

**Description:** Deselect all points in current batch.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Deselect All;
```

#### [Load Candidate Set from Data Table](#load-candidate-set-from-data-table)[](#load-candidate-set-from-data-table "Click to copy url")

**Syntax:** obj \<\< Load Candidate Set from Data Table

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Load Candidate Set from Data Table()
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Borehole Latin Hypercube.jmp" );
:log y << Set Property( "Response Limits", {Goal( maximize ), Importance( 1 )} );
obj = dt << Bayesian Optimization(
    Y( :log y ),
    X( :log10 Rw, :log10 R, :Tu, :Tl, :Hu, :Hl, :L, :Kw )
);
dt_candidate = Open( "$SAMPLE_DATA/Design Experiment/Borehole Uniform.jmp" );
obj << Load Candidate Set from Data Table( dt_candidate );
```

#### [Make Table](#make-table)[](#make-table "Click to copy url")

**Syntax:** obj \<\< Make Table

**Description:** Export currently selected batch points to data table based on current settings.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Make Table;
```

#### [Make Table Options](#make-table-options)[](#make-table-options "Click to copy url")

**Syntax:** obj \<\< Make Table Options( \<Location( state = 0\|1 )\>, \<Randomize Runs( state = 0\|1 )\>, \< "Include Option Name"( state = 0\|1 ) \> , ... )

**Description:** Enables you to select option settings that are used when exporting the selected batch to a data table. Note the "Include Option Name" syntax input refers to any of the options under the Include Options menu.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Make Table Options(
        Location( 1 ),
        Randomize Runs( 0 ),
        Save desirability function values to columns( 1 ),
        Save startup script for next batch selection to data table( 1 ),
        Include observed desirabilities( 1 ),
        Include original candidate set row indices( 1 ),
        Include reason added column( 1 ),
        Include predicted response values( 1 ),
        Include prediction standard deviations( 1 ),
        Include Bayesian desirability expected improvement column( 1 )
    )
);
```

#### [Maximize Bayesian Desirability](#maximize-bayesian-desirability)[](#maximize-bayesian-desirability "Click to copy url")

**Syntax:** obj \<\< Maximize Bayesian Desirability

**Description:** Finds the factor settings that maximize the posterior mean of the desirability distribution.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Maximize Bayesian Desirability;
```

#### [Maximize Bayesian Desirability Std Dev](#maximize-bayesian-desirability-std-dev)[](#maximize-bayesian-desirability-std-dev "Click to copy url")

**Syntax:** obj \<\< Maximize Bayesian Desirability Std Dev

**Description:** Finds the factor settings that maximize the posterior deviation of the desirability distribution.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Maximize Bayesian Desirability Std Dev;
```

#### [Maximize Expected Improvement](#maximize-expected-improvement)[](#maximize-expected-improvement "Click to copy url")

**Syntax:** obj \<\< Maximize Expected Improvement

**Description:** Finds the factor settings with the largest expected improvement as measured by Bayesian desirability.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Maximize Expected Improvement;
```

#### [Maximize MaxPro Criterion](#maximize-maxpro-criterion)[](#maximize-maxpro-criterion "Click to copy url")

**Syntax:** obj \<\< Maximize MaxPro Criterion

**Description:** Finds the most space filling factor settings using the MaxPro criterion.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Maximize MaxPro Criterion;
```

#### [Maximize Multimodel Std Dev](#maximize-multimodel-std-dev)[](#maximize-multimodel-std-dev "Click to copy url")

**Syntax:** obj \<\< Maximize Multimodel Std Dev

**Description:** Finds the factor settings that maximize the multiple response prediction standard deviation.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Maximize Multimodel Std Dev;
```

#### [Maximize Upper Confidence Bound](#maximize-upper-confidence-bound)[](#maximize-upper-confidence-bound "Click to copy url")

**Syntax:** obj \<\< Maximize Upper Confidence Bound

**Description:** Finds the factor settings for the Bayesian desirability prediction with the highest upper confidence bound. This is often called the UCB criterion.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Maximize Upper Confidence Bound;
```

#### [Restore Best Training Point](#restore-best-training-point)[](#restore-best-training-point "Click to copy url")

**Syntax:** obj \<\< Restore Best Training Point

**Description:** Returns factor settings to those of the training row with the highest observed desirability.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR )
);
obj << Maximize Bayesian Desirability;
obj << Add Current Profiler Settings to Batch;
obj << Restore Best Training Point;
```

## [Bayesian Optimization Model Summary](#bayesian-optimization-model-summary)[](#bayesian-optimization-model-summary "Click to copy url")

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [All Responses Profiler](#all-responses-profiler)[](#all-responses-profiler "Click to copy url")

**Syntax:** obj \<\< All Responses Profiler( state=0\|1 )

**Description:** Explores how each column changes with respect to changes in each factor value across models.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    All Responses Profiler( 1 )
);
```

## [Gaussian Process Model](#gaussian-process-model)[](#gaussian-process-model "Click to copy url")

### [Item Messages](#item-messages_4)[](#item-messages_4 "Click to copy url")

#### [Intercept](#intercept)[](#intercept "Click to copy url")

**Syntax:** obj \<\< Intercept( number )

**Description:** Specifies the value to use as an intercept parameter for fitting a Gaussian Process model. If all theta, nugget, residual, and intercept values are provided, the values are treated as fixed. If a partial set of values is provided, the given values are treated as starting values.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Response Model Tab(
        Y( :ABRASION ),
        Theta Values( {0.5, 0.5, 0.5} ),
        Nugget( 0.05 ),
        Residual( 500 ),
        Intercept( 100 )
    )
);
```

#### [Nugget](#nugget)[](#nugget "Click to copy url")

**Syntax:** obj \<\< Nugget( number )

**Description:** Specifies the value to use as a nugget for fitting a Gaussian Process model. If all theta, nugget, residual, and intercept values are provided, the values are treated as fixed. If a partial set of values is provided, the given values are treated as starting values.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Response Model Tab(
        Y( :ABRASION ),
        Theta Values( {0.5, 0.5, 0.5} ),
        Nugget( 0.05 ),
        Residual( 500 ),
        Intercept( 100 )
    )
);
```

#### [Profiler](#profiler)[](#profiler "Click to copy url")

**Syntax:** obj \<\< Profiler( state=0\|1 )

**Description:** Explores how each column changes with respect to changes in each factor value across models.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Response Model Tab( Y( :MODULUS ), Profiler( 0 ) )
);
```

#### [Residual](#residual)[](#residual "Click to copy url")

**Syntax:** obj \<\< Residual( number )

**Description:** Specifies the value to use as a residual parameter for fitting a Gaussian Process model. If all theta, nugget, residual, and intercept values are provided, the values are treated as fixed. If a partial set of values is provided, the given values are treated as starting values.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Response Model Tab(
        Y( :ABRASION ),
        Theta Values( {0.5, 0.5, 0.5} ),
        Nugget( 0.05 ),
        Residual( 500 ),
        Intercept( 100 )
    )
);
```

#### [Starting Values](#starting-values)[](#starting-values "Click to copy url")

**Syntax:** obj \<\< Starting Values( number )

**Description:** Specifies the starting values to use for fitting a Gaussian Process model.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Response Model Tab(
        Y( :ABRASION ),
        Starting Values(
            Theta Values( {0.5, 0.5, 0.5} ),
            Nugget( 0.05 ),
            Residual( 500 ),
            Intercept( 100 )
        )
    )
);
```

#### [Theta Values](#theta-values)[](#theta-values "Click to copy url")

**Syntax:** obj \<\< Theta Values( number )

**Description:** Specifies the values to use as theta parameters for fitting a Gaussian Process model. If all theta, nugget, residual, and intercept values are provided, the values are treated as fixed. If a partial set of values is provided, the given values are treated as starting values.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
Bayesian Optimization(
    Y( :ABRASION, :MODULUS, :ELONG, :HARDNESS ),
    X( :SILICA, :SILANE, :SULFUR ),
    Response Model Tab(
        Y( :ABRASION ),
        Theta Values( {0.5, 0.5, 0.5} ),
        Nugget( 0.05 ),
        Residual( 500 ),
        Intercept( 100 )
    )
);
```

[ Previous](Attribute%20Chart.html "Attribute Chart") [Next ](Boosted%20Tree.html "Boosted Tree")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
