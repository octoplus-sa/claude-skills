# Partial Least Squares

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Partial%20Least%20Squares.html](https://jsl.jmp.com/All%20Categories/Objects/Partial%20Least%20Squares.html)*

---

# [Partial Least Squares](#partial-least-squares)[](#partial-least-squares "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Partial Least Squares](#partial-least-squares_1)[](#partial-least-squares_1 "Click to copy url")

**Syntax:** Partial Least Squares( Y( columns ), X( columns ) )

**Description:** Fits a model to one or more response variables using latent factors. This permits models to be fit when explanatory variables are highly correlated, or when there are more explanatory variables than there are observations.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Go
);
```

## [Columns](#columns)[](#columns "Click to copy url")

### [By](#by)[](#by "Click to copy url")

**Syntax:** obj \<\< By( column(s) )

**Description:** Performs a separate analysis for each level of the specified column.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) ),
    Go
);
```

### [Factor](#factor)[](#factor "Click to copy url")

**Syntax:** obj \<\< Factor( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
```

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Freq( :_freqcol ),
    Go
);
```

### [Response](#response)[](#response "Click to copy url")

**Syntax:** obj \<\< Response( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
```

### [Validation](#validation)[](#validation "Click to copy url")

**Syntax:** obj \<\< Validation( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** obj \<\< X( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Centering](#centering)[](#centering "Click to copy url")

**Syntax:** obj = Partial Least Squares(...Centering( state=0\|1)...)

**Description:** Centers all Y variables and model effects by subtracting the mean from each column. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Centering( 0 ),
    Validation Method( KFold( 7 ) ),
    Go
);
```

### [Fit](#fit)[](#fit "Click to copy url")

**Syntax:** obj \<\< Fit( SVD( Fast\|Classical ), Method( NIPALS\|SIMPLS ), Number of Factors( number ) )

**Description:** Fits a partial least squares model with a specified method and number of factors.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Method( NIPALS ), Number of Factors( 7 ) ),
    Go
);
```

### [Go](#go)[](#go "Click to copy url")

**Syntax:** obj \<\< Go

**Description:** Launches the partial least squares model fit.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    )
);
obj << Go;
```

### [Imputation Method](#imputation-method)[](#imputation-method "Click to copy url")

**Syntax:** obj = Partial Least Squares(...Imputation Method( "Mean"\|"EM" )...)

**Description:** Specifies the imputation method. The Mean method replaces missing values with the mean of the nonmissing values in the same column. The EM method uses an iterative Expectation-Maximization (EM) approach to impute missing values.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Partial Least Squares(
    Y( :Y ),
    X( :OZONE, :CO, :SO2, :NO, :PM10, :Lead ),
    Impute Missing Data( 1 ),
    Imputation Method( "EM" ),
    Max Iterations( 2 ),
    Validation Method( None, Initial Number of Factors( 6 ) ),
    Fit( Method( NIPALS ), Number of Factors( 6 ) )
);
```

### [Impute Missing Data](#impute-missing-data)[](#impute-missing-data "Click to copy url")

**Syntax:** obj = Partial Least Squares(...Impute Missing Data( state=0\|1 )...)

**Description:** Replaces missing data values in the responses and regressors with nonmissing values. Otherwise, rows with missing values are excluded from the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = Partial Least Squares(
    Y( :Y ),
    X( :OZONE, :CO, :SO2, :NO, :PM10, :Lead ),
    Impute Missing Data( 1 ),
    Validation Method( None, Initial Number of Factors( 6 ) ),
    Go
);
```

### [Initial Number of Factors](#initial-number-of-factors)[](#initial-number-of-factors "Click to copy url")

**Syntax:** obj \<\< Partial Least Squares( Validation Method(...Initial Number of Factors( number )...) )

**Description:** Specifies the initial number of factors for cross validation.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Validation Method( KFold( 7 ), Initial Number of Factors( 10 ) ), 

);
obj << Go;
```

### [Max Iterations](#max-iterations)[](#max-iterations "Click to copy url")

**Syntax:** obj = Partial Least Squares(...Max Iterations( number=1 )...)

**Description:** Specifies the maximum number of iterations to perform in the EM imputation loop. "1" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Partial Least Squares(
    Y( :Y ),
    X( :OZONE, :CO, :SO2, :NO, :PM10, :Lead ),
    Impute Missing Data( 1 ),
    Imputation Method( "EM" ),
    Max Iterations( 2 ),
    Validation Method( None, Initial Number of Factors( 6 ) ),
    Fit( Method( NIPALS ), Number of Factors( 6 ) )
);
```

### [Method](#method)[](#method "Click to copy url")

**Syntax:** obj = Partial Least Squares(...Fit( Method( NIPALS\|SIMPLS)... )

**Description:** Specifies the method used to fit the partial least squares model.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Method( NIPALS ), Number of Factors( 11 ) ),
    Go
);
```

### [Model Dialog](#model-dialog)[](#model-dialog "Click to copy url")

**Syntax:** obj \<\< Model Dialog

**Description:** Opens the Fit Model launch window. You can fit a Partial Least Squares model from this launch window by selecting the Partial Least Squares personality.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
obj << Model Dialog;
```

### [SVD](#svd)[](#svd "Click to copy url")

**Syntax:** obj \<\< SVD( Fast\|Classical )

**Description:** Sets the implementation of the SVD algorithm for computing the partial least squares model to Fast or Classical. The Fast option implements the Lanczos SVD routine and the Classical option implements the Golub-Kahan routine.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Validation Method( KFold( 7 ) ),
    Go
);
obj << Fit( SVD( Classical ), Method( SIMPLS ) );
```

### [Scaling](#scaling)[](#scaling "Click to copy url")

**Syntax:** obj = Partial Least Squares(...Scaling( state=0\|1)...)

**Description:** Scales all Y variables and model effects by dividing each column by its standard deviation. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Scaling( 0 ),
    Validation Method( KFold( 7 ) ),
    Go
);
```

### [Set Random Seed](#set-random-seed)[](#set-random-seed "Click to copy url")

**Syntax:** obj \<\< Set Random Seed( number )

**Description:** Specifies the random seed for running a partial least squares model with cross validation.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Set Random Seed( 12345 ),
    Validation Method( KFold( 7 ) ),
    Go
);
```

### [Validation Method](#validation-method)[](#validation-method "Click to copy url")

**Syntax:** obj \<\< Validation Method( KFold( number )\|Holdback( fraction )\|"Leave-One-Out"\|None, Initial Number of Factors( number ) )

**Description:** Sets the method used for model validation.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Validation Method( KFold( 7 ), Initial Number of Factors( 15 ) ),
    Go
);
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
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) ),
    Go
);
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
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
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) ),
    Go
);
t = obj[1] << Get ByGroup Script;
Show( t );
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
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
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
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
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
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
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
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
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) ),
    Go
);
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) ),
    Go
);
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) ),
    Go
);
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) ),
    Go
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) ),
    Go
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
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
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Tasting.jmp" );
obj = dt << Partial Least Squares(
    Y( :Hedonic, :Goes with meat, :Goes with dessert ),
    X( :Price, :Sugar, :Alcohol, :Acidity ),
    Go
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

**Syntax:** obj = Partial Least Squares(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

## [Partial Least Squares Fit](#partial-least-squares-fit)[](#partial-least-squares-fit "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Coefficient Plots](#coefficient-plots)[](#coefficient-plots "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Coefficient Plots( state=0\|1 ))

**Description:** Shows or hides plots of the model coefficients for each response across the X variables. There is a plot for the centered and scaled data and a plot for the original data.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Coefficient Plots( 1 ));
```

#### [Correlation Loading Plot](#correlation-loading-plot)[](#correlation-loading-plot "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Correlation Loading Plot( state=0\|1 ))

**Description:** Shows or hides either a single scatterplot or a scatterplot matrix of the X and Y loadings overlaid on the same plot. The scatterplot matrix is shown if the specified number of factors is greater than 2.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Correlation Loading Plot( 2 ));
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Correlation Loading Plot( 4 ));
```

#### [Diagnostics Plots](#diagnostics-plots)[](#diagnostics-plots "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Diagnostics Plots( state=0\|1 ))

**Description:** Shows or hides diagnostic plots.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Diagnostics Plots( 1 ));
```

#### [Distance Plots](#distance-plots)[](#distance-plots "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Distance Plots( state=0\|1 ))

**Description:** Shows or hides the distance plots. There is a plot of the distance from each observation to the X model, a plot of the distance from each observation to the Y model, and a scatterplot of distances to both the X and Y models.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Distance Plots( 1 ));
```

#### [Fit Line](#fit-line)[](#fit-line "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Fit Line( state=0\|1 ))

**Description:** Shows or hides a fitted line through the points on the X-Y Scores Plots. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
Wait( 2 );
obj << (Fit[1] << Fit Line( 0 ));
```

#### [Get Measures](#get-measures)[](#get-measures "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Get Measures)

**Description:** Returns summary measures of fit from the model.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Get Measures);
```

#### [Loading Plots](#loading-plots)[](#loading-plots "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Loading Plots( state=0\|1 ))

**Description:** Shows or hides plots of the X and Y loadings for each extracted factor. There are separate plots for the X and Y variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Loading Plots( 1 ));
```

#### [Loading Scatterplot Matrices](#loading-scatterplot-matrices)[](#loading-scatterplot-matrices "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Loading Scatterplot Matrices( state=0\|1 ))

**Description:** Shows or hides scatterplot matrices of the X and Y loadings. There are separate scatterplot matrices for the X and Y variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Loading Scatterplot Matrices( 1 ));
```

#### [Make Model Using VIP](#make-model-using-vip)[](#make-model-using-vip "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Make Model Using VIP)

**Description:** Opens and populates a launch window with the appropriate responses entered as Ys and the variables whose VIPs exceed the specified threshold entered as Xs.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Make Model Using VIP);
```

#### [Model Driven Multivariate Control Chart for Saved X Scores](#model-driven-multivariate-control-chart-for-saved-x-scores)[](#model-driven-multivariate-control-chart-for-saved-x-scores "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Model Driven Multivariate Control Chart for Saved X Scores)

**Description:** Saves the formulas for each X Score and launches the Model Driven Multivariate Control Chart (MDMCC) launch window.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Model Driven Multivariate Control Chart for Saved X Scores);
```

#### [Percent Variation Plots](#percent-variation-plots)[](#percent-variation-plots "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Percent Variation Plots( state=0\|1 ))

**Description:** Shows or hides plots of the percent of variation explained for X Effects and for Y Responses.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Percent variation plots( 1 ));
```

#### [Profiler](#profiler)[](#profiler "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Profiler( state=0\|1 ))

**Description:** Shows or hides a profiler for each response.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Profiler( 1 ));
```

#### [Profiler for Predicteds](#profiler-for-predicteds)[](#profiler-for-predicteds "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Model Driven Multivariate Control Chart for Saved X Scores)

**Description:** Saves the formulas for each Y as a function of the X Score and launches the Profiler launch window.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Profiler for Predicteds);
```

#### [Publish Prediction Formula](#publish-prediction-formula)[](#publish-prediction-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Publish Prediction Formula)

**Description:** Creates a prediction formula and publishes it as a formula column script in the Formula Depot platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Publish Prediction Formula);
```

#### [Publish Score Formula](#publish-score-formula)[](#publish-score-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Publish Score Formula)

**Description:** Creates X and Y score formulas and saves them as formula column scripts in the Formula Depot platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Publish Score Formula);
```

#### [Remove Fit](#remove-fit)[](#remove-fit "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Remove Fit)

**Description:** Removes the model report from the main platform report.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
Wait( 3 );
obj << (Fit[1] << Remove Fit);
```

#### [Save Distance](#save-distance)[](#save-distance "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Distance)

**Description:** Saves new columns to the original data table. The new columns contain the Distance to X Model (DModX) and Distance to Y Model (DModY) values.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Distance);
```

#### [Save Distance as X Score Formula](#save-distance-as-x-score-formula)[](#save-distance-as-x-score-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Distance as X Score Formula)

**Description:** Saves new formula columns to the original data table. The new columns contain the Distance to X Model (DModX) and Distance to Y Model (DModY) formulas that are functions of the X Score formulas.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Distance as X Score Formula);
```

#### [Save Imputation](#save-imputation)[](#save-imputation "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Imputation)

**Description:** Saves columns to a new data table. For each X and Y variable, there is a column that contains the original data column with missing values replaced by their imputed values.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Partial Least Squares(
    Y( :Y ),
    X( :OZONE, :CO, :SO2, :NO, :PM10, :Lead ),
    Impute Missing Data( 1 ),
    Imputation Method( "EM" ),
    Max Iterations( 2 ),
    Validation Method( None, Initial Number of Factors( 6 ) ),
    Fit( Method( NIPALS ), Number of Factors( 6 ) )
);
obj << (Fit[1] << Save Imputation);
```

#### [Save Indiv Confidence Limit Formula](#save-indiv-confidence-limit-formula)[](#save-indiv-confidence-limit-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Indiv Confidence Limit Formula)

**Description:** Saves new formula columns to the original data table. For each Y variable, there are columns for the lower and upper confidence limits for an individual prediction that are functions of the X Score formulas. The default level for alpha is 0.05, which creates 95% confidence limits.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Indiv Confidence Limit Formula);
```

#### [Save Loadings](#save-loadings)[](#save-loadings "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Loadings)

**Description:** Saves columns to two new data tables. There is a data table that contains the loadings for the X variables and a data table that contains the loadings for the Y variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Loadings);
```

#### [Save Mean Confidence Limit Formula](#save-mean-confidence-limit-formula)[](#save-mean-confidence-limit-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Mean Confidence Limit Formula( \<alpha=0.05\> ))

**Description:** Saves new formula columns to the original data table. For each Y variable, there are columns for the lower and upper confidence limits for the mean response that are functions of the X Score formulas. The default level for alpha is 0.05, which creates 95% confidence limits.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Mean Confidence Limit Formula);
```

#### [Save Percent Variation Explained For X Effects](#save-percent-variation-explained-for-x-effects)[](#save-percent-variation-explained-for-x-effects "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Percent Variation Explained For X Effects)

**Description:** Saves columns to a new data table. For each X variable, there is a column that contains the percent of variation explained across all extracted factors.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Percent Variation Explained For X Effects);
```

#### [Save Percent Variation Explained For Y Responses](#save-percent-variation-explained-for-y-responses)[](#save-percent-variation-explained-for-y-responses "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Percent Variation Explained For Y Responses)

**Description:** Saves columns to a new data table. For each Y variable, there is a column that contains the percent of variation explained across all extracted factors.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Percent Variation Explained For Y Responses);
```

#### [Save Prediction As X Score Formula](#save-prediction-as-x-score-formula)[](#save-prediction-as-x-score-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Prediction as X Score Formula)

**Description:** Saves new formula columns to the original data table. For each Y variable, there is a column that contains a prediction formula that is a function of the X Score formulas.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Prediction as X Score Formula);
```

#### [Save Prediction Formula](#save-prediction-formula)[](#save-prediction-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Prediction Formula)

**Description:** Saves new formula columns to the original data table. For each Y variable, there is a column that contains a prediction formula that is a function of the X variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Prediction Formula);
```

#### [Save Score Formula](#save-score-formula)[](#save-score-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Score Formula)

**Description:** Saves new formula columns to the original data table. For each extracted factor, there is a column that contains an X Score formula and a column that contains a Y Score formula. The X Score formulas are functions of the X variables and the Y Score formulas are functions of the X Score formulas.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Score Formula);
```

#### [Save Scores](#save-scores)[](#save-scores "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Scores)

**Description:** Saves new columns to the original data table. For each extracted factor, there is a column that contains the X scores and a column that contains the Y scores.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Scores);
```

#### [Save Standard Errors of Prediction Formula](#save-standard-errors-of-prediction-formula)[](#save-standard-errors-of-prediction-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Standard Errors of Prediction Formula)

**Description:** Saves new formula columns to the original data table. For each Y variable, there is a column that contains the formula for the standard error of the predicted mean that is a function of the X variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Standard Errors of Prediction Formula);
```

#### [Save Standardized Loadings](#save-standardized-loadings)[](#save-standardized-loadings "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Standardized Loadings)

**Description:** Saves columns to two new data tables. There is a data table that contains the standardized loadings for the X variables and a data table that contains the standardized loadings for the Y variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Standardized Loadings);
```

#### [Save Standardized Scores](#save-standardized-scores)[](#save-standardized-scores "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Standardized Scores)

**Description:** Saves new columns to the original data table. The new columns contain the X and Y standardized scores for each extracted factor.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Standardized Scores);
```

#### [Save T Square](#save-t-square)[](#save-t-square "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save T Square)

**Description:** Saves a new formula column to the original data table. The new column contains the T squared formula as a function of the X variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save T Square);
```

#### [Save T Square as X Score Formula](#save-t-square-as-x-score-formula)[](#save-t-square-as-x-score-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save T Square as X Score Formula)

**Description:** Saves a new formula column to the original data table. The new column contains the T squared formula as a function of the X Score formulas.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save T Square as X Score Formula);
```

#### [Save Validation](#save-validation)[](#save-validation "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Validation)

**Description:** Saves a new column to the original data table. The new column contains numbers that indicate how each observation was used in validation.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Validation);
```

#### [Save X Predicted Values](#save-x-predicted-values)[](#save-x-predicted-values "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save X Predicted Values)

**Description:** Saves new columns to the original data table. For each X variable, there is a column that contains the predicted X values.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save X Predicted Values);
```

#### [Save X Prediction as X Score Formula](#save-x-prediction-as-x-score-formula)[](#save-x-prediction-as-x-score-formula "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save X Prediction as X Score Formula)

**Description:** Saves new formula columns to the original data table. For each X variable, there is a column that contains a prediction formula that is a function of the X Score formulas.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save X Prediction as X Score Formula);
```

#### [Save X Residuals](#save-x-residuals)[](#save-x-residuals "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save X Residuals)

**Description:** Saves new columns to the original data table. For each X variable, there is a column that contains the X residual values.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save X Residuals);
```

#### [Save X Score Formula](#save-x-score-formula)[](#save-x-score-formula "Click to copy url")

**Syntax:** obj \<\< Save X Score Formula

#### [Save X Weights](#save-x-weights)[](#save-x-weights "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save X Weights)

**Description:** Saves columns to a new data table. For each extracted factor, there is a column that contains the weights for the X variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save X Weights);
```

#### [Save Y Predicted Values](#save-y-predicted-values)[](#save-y-predicted-values "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Y Predicted Values)

**Description:** Saves new columns to the original data table. For each Y variable, there is a column that contains the predicted Y values.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Y Predicted Values);
```

#### [Save Y Residuals](#save-y-residuals)[](#save-y-residuals "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Save Y Residuals)

**Description:** Saves new columns to the original data table. For each Y variable, there is a column that contains the Y residual values.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Save Y Residuals);
```

#### [Score Scatterplot Matrices](#score-scatterplot-matrices)[](#score-scatterplot-matrices "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Score Scatterplot Matrices( state=0\|1 ))

**Description:** Shows or hides a scatterplot matrix of the X scores and a scatterplot matrix of the Y scores.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Score Scatterplot Matrices( 1 ));
```

#### [Set VIP Threshold](#set-vip-threshold)[](#set-vip-threshold "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Set VIP Threshold( number=0.8 ))

**Description:** Sets the threshold level for the Variable Importance Plot, Variance Importance Table, and the VIP vs Coefficients Plots. "0.8" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Variable Importance Plot( 1 ));
Wait( 3 );
obj << (Fit[1] << Set VIP Threshold( 0.5 ));
```

#### [Show Confidence Band](#show-confidence-band)[](#show-confidence-band "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Show Confidence Band( state=0\|1 ))

**Description:** Shows or hides 95% confidence bands for the fitted lines on the X-Y Scores Plots.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Show Confidence Band( 1 ));
```

#### [Spectral Profiler](#spectral-profiler)[](#spectral-profiler "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Spectral Profiler( state=0\|1 ))

**Description:** Shows or hides a single profiler where all of the response variables appear in the first cell of the plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Spectral Profiler( 1 ));
```

#### [T Square Plot](#t-square-plot)[](#t-square-plot "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< T Square Plot( state=0\|1 ))

**Description:** Shows or hides a plot of T square statistics for each observation, along with a control limit.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << T Square Plot( 1 ));
```

#### [VIP vs Coefficients Plots](#vip-vs-coefficients-plots)[](#vip-vs-coefficients-plots "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< VIP vs Coefficients Plots( state=0\|1 ))

**Description:** Shows or hides a plot of the VIP statistics against the model coefficients.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << VIP vs Coefficients Plots( 1 ));
```

#### [Variable Importance Plot](#variable-importance-plot)[](#variable-importance-plot "Click to copy url")

**Syntax:** obj \<\< (Fit\[number\] \<\< Variable Importance Plot( state=0\|1 ))

**Description:** Shows or hides a plot that summarizes the contribution each variable makes to the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16,
        :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27
    ),
    Fit( Number of Factors( 5 ) )
);
obj << (Fit[1] << Variable Importance Plot( 1 ));
```

[ Previous](Pareto%20Plot.html "Pareto Plot") [Next ](Partition%20Platform.html "Partition Platform")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
