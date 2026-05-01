# Model Comparison

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Model%20Comparison.html](https://jsl.jmp.com/All%20Categories/Objects/Model%20Comparison.html)*

---

# [Model Comparison](#model-comparison)[](#model-comparison "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Model Comparison](#model-comparison_1)[](#model-comparison_1 "Click to copy url")

**Syntax:** Model Comparison( Predictors( columns ), Group( column ) )

**Description:** Compares performance across models using prediction formula columns.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
```

## [Columns](#columns)[](#columns "Click to copy url")

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window ),
    Freq( :_freqcol )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window ),
    Freq( :_freqcol )
);
obj = Model Comparison();
```

### [Group](#group)[](#group "Click to copy url")

**Syntax:** obj \<\< Group( column(s) )

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
```

### [Predictors](#predictors)[](#predictors "Click to copy url")

**Syntax:** obj \<\< Predictors( column(s) )

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
```

### [Weight](#weight)[](#weight "Click to copy url")

**Syntax:** obj \<\< Weight( column )

**Description:** Specifies a column whose values assign a weight to each row for the analysis.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << New Column( "_weightcol", Numeric, Continuous, Set Each Value( Random Beta( 1, 1 ) ) );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window ),
    Weight( :_weightcol )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window ),
    Weight( :_weightcol )
);
obj = Model Comparison();
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [AUC Comparison](#auc-comparison)[](#auc-comparison "Click to copy url")

**Syntax:** obj \<\< AUC Comparison( state=0\|1 )

**Description:** Shows or hides a comparison of the area under the ROC curve (AUC) from each model.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :sex ),
    Effects( :height ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
dt << Fit Model(
    Y( :sex ),
    Effects( :age ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
Model Comparison( AUC Comparison( 1 ) );
```

### [Confusion Matrix](#confusion-matrix)[](#confusion-matrix "Click to copy url")

**Syntax:** obj \<\< Confusion Matrix( state=0\|1 )

**Description:** Shows or hides a crosstabulation matrix of actual and predicted responses.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :sex ),
    Effects( :height ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
dt << Fit Model(
    Y( :sex ),
    Effects( :age ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
Model Comparison( Confusion Matrix( 1 ) );
```

### [Cum Gains Curve](#cum-gains-curve)[](#cum-gains-curve "Click to copy url")

**Syntax:** obj \<\< Cum Gains Curve( state=0\|1 )

**Description:** Shows or hides a plot of cumulative gains curves for each level of the response variable. A cumulative gains curve plots the proportion of a response level that is identified by the model against the proportion of all responses.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :sex ),
    Effects( :height ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
dt << Fit Model(
    Y( :sex ),
    Effects( :age ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
Model Comparison( Cum Gains Curve( 1 ) );
```

### [Decision Threshold](#decision-threshold)[](#decision-threshold "Click to copy url")

**Syntax:** obj \<\< Decision Threshold( state = 0\|1, Set Probability Threshold( number ) )

**Description:** Shows or hides the distribution of fitted probabilities and actual versus predicted tables for each model. You can change the probability threshold to explore how different thresholds affect the classification results.

**JMP Version Added:** 16

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :sex ),
    Effects( :height ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
dt << Fit Model(
    Y( :sex ),
    Effects( :age ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
Model Comparison( Decision Threshold( 1 ) );
```

### [Lift Curve](#lift-curve)[](#lift-curve "Click to copy url")

**Syntax:** obj \<\< Lift Curve( state=0\|1 )

**Description:** Shows or hides lift curves for each level of the response variable. The curves for the different models are overlaid in the plots.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :sex ),
    Effects( :height ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
dt << Fit Model(
    Y( :sex ),
    Effects( :age ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
Model Comparison( Lift Curve( 1 ) );
```

### [Model Averaging](#model-averaging)[](#model-averaging "Click to copy url")

**Syntax:** obj \<\< Model Averaging

**Description:** Saves a new prediction column of the average of the predicted probabilities across models. This prediction column often results in a model with better prediction capability than the individual models.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
Model Comparison( Model Averaging );
```

### [Plot Actual by Predicted](#plot-actual-by-predicted)[](#plot-actual-by-predicted "Click to copy url")

**Syntax:** obj \<\< Plot Actual by Predicted( state=0\|1 )

**Description:** Shows or hides a plot with the actual response values on the vertical axis and the predicted values on the horizontal axis. In good fits, points are near the diagonal. You can see which points are far from the diagonal, look for patterns, and visualize the test.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
Model Comparison( Plot Actual by Predicted( 1 ) );
```

### [Plot Residual by Row](#plot-residual-by-row)[](#plot-residual-by-row "Click to copy url")

**Syntax:** obj \<\< Plot Residual by Row( state=0\|1 )

**Description:** Shows or hides a plot with the residuals on the vertical axis and the row number on the horizontal axis.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
Model Comparison( Plot Residual by Row( 1 ) );
```

### [Precision Recall Curve](#precision-recall-curve)[](#precision-recall-curve "Click to copy url")

**Syntax:** obj \<\< Precision Recall Curve( state=0\|1 )

**Description:** Shows or hides Precision-Recall Curve plots for each level of the response variable. The curves for the different models are overlaid in the plots.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :sex ),
    Effects( :height ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
dt << Fit Model(
    Y( :sex ),
    Effects( :age ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
Model Comparison( Precision Recall Curve( 1 ) );
```

### [Profiler](#profiler)[](#profiler "Click to copy url")

**Syntax:** obj \<\< Profiler( state=0\|1 )

**Description:** Shows or hides the prediction profiler, which is used to graphically explore the prediction equation by slicing it one factor at a time. The prediction profiler contains features for optimization.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
Model Comparison( Profiler( 1 ) );
```

### [ROC Curve](#roc-curve)[](#roc-curve "Click to copy url")

**Syntax:** obj \<\< ROC Curve( state=0\|1 )

**Description:** Shows or hides Receiver Operating Characteristic (ROC) curves for each level of the response variable. The curves for the different models are overlaid in the plots.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :sex ),
    Effects( :height ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
dt << Fit Model(
    Y( :sex ),
    Effects( :age ),
    Target Level( "M" ),
    Personality( "Nominal Logistic" ),
    Run( Save Probability Formula, Close Window )
);
Model Comparison( ROC Curve( 1 ) );
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
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
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
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
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
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
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
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
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
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
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
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
obj << Report View( "Summary" );
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj = Model Comparison();
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj = Model Comparison();
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
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
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
dt << Fit Model(
    Y( :weight ),
    Effects( :height ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
dt << Fit Model(
    Y( :weight ),
    Effects( :age ),
    Personality( "Standard Least Squares" ),
    Run( Prediction Formula, Close Window )
);
obj = Model Comparison();
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

[ Previous](Mixture%20Profiler.html "Mixture Profiler") [Next ](Model%20Driven%20Multivariate%20Control%20Chart.html "Model Driven Multivariate Control Chart")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
