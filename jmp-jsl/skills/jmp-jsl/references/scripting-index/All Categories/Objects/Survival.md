# Survival

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Survival.html](https://jsl.jmp.com/All%20Categories/Objects/Survival.html)*

---

# [Survival](#survival)[](#survival "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Survival](#survival_1)[](#survival_1 "Click to copy url")

**Syntax:** Survival( Y( columns ), Censor( column ), \<Grouping( column )\> )

**Description:** Calculates estimates of survival functions using the product-limit (Kaplan-Meier) method for one or more groups.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
```

## [Columns](#columns)[](#columns "Click to copy url")

### [By](#by)[](#by "Click to copy url")

**Syntax:** obj \<\< By( column(s) )

**Description:** Performs a separate analysis for each level of the specified column.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
```

### [Censor](#censor)[](#censor "Click to copy url")

**Syntax:** obj \<\< Censor( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
```

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ), Freq( :_freqcol ) );
```

### [Grouping](#grouping)[](#grouping "Click to copy url")

**Syntax:** obj \<\< Grouping( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
```

### [Time to Event](#time-to-event)[](#time-to-event "Click to copy url")

**Syntax:** obj \<\< Time to Event( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Censor Code](#censor-code)[](#censor-code "Click to copy url")

**Syntax:** obj = Survival(...Censor Code( value=1 )...)

**Description:** Identifies the value in the Censor column that designates right-censored observations. "1" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Survival( Y( :Time ), Censor( :Censor ), Censor Code( 0 ) );
```

### [Competing Causes](#competing-causes)[](#competing-causes "Click to copy url")

**Syntax:** obj \<\< Competing Causes( column )

**Description:** Performs an estimation of the Weibull model using the specified causes to indicate a failure event and other causes to indicate censored observations. The fitted distribution appears as a dashed line in the Survival Plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Competing Causes( :Failure Cause );
```

### [Connect Quantile Points](#connect-quantile-points)[](#connect-quantile-points "Click to copy url")

**Syntax:** obj \<\< Connect Quantile Points( state=0\|1 )

**Description:** Shows or hides the lines in the Exponential Plot, the Weibull Plot, and the LogNormal Plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Weibull Plot( 1 );
Wait( 1 );
obj << Connect Quantile Points( 0 );
```

### [Estimate Survival Probability](#estimate-survival-probability)[](#estimate-survival-probability "Click to copy url")

**Syntax:** obj \<\< Estimate Survival Probability( \[time1, time2, ...\], Alpha( level ) )

**Description:** Estimates survival probabilities and confidence intervals for the specified time values using the fitted distributions.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Weibull Fit( 1 );
obj << Estimate Survival Probability( [100, 200, 300], Alpha( 0.001 ) );
```

### [Estimate Time Quantile](#estimate-time-quantile)[](#estimate-time-quantile "Click to copy url")

**Syntax:** obj \<\< Estimate Time Quantile( \[p1, p2, ...\], Alpha( level ) )

**Description:** Estimates a time quantile and confidence intervals for each specified survival probability using the fitted distributions.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Weibull Fit( 1 );
obj << Estimate Time Quantile( [0.5, 0.9, 0.95], Alpha( 0.01 ) );
```

### [Exponential Fit](#exponential-fit)[](#exponential-fit "Click to copy url")

**Syntax:** obj \<\< Exponential Fit( state=0\|1 )

**Description:** Shows or hides the Exponential Parameter Estimates table. This option also adds a linear fit to the exponential cumulative distribution function in the Exponential Plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Exponential Plot( 1 );
Wait( 1 );
obj << Exponential Fit( 1 );
```

### [Exponential Plot](#exponential-plot)[](#exponential-plot "Click to copy url")

**Syntax:** obj \<\< Exponential Plot( state=0\|1 )

**Description:** Shows or hides the Exponential Plot, which shows the cumulative exponential failure probability by time for each group. Lines that are approximately linear empirically indicate the appropriateness of using an exponential model for further analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Exponential Plot( 1 );
```

### [Failure Plot](#failure-plot)[](#failure-plot "Click to copy url")

**Syntax:** obj \<\< Failure Plot( state=0\|1 )

**Description:** Shows or hides the failure plot, which contains overlaid failure curves (proportion failing over time) for each group. A failure plot reverses the vertical axis to show the number of failures rather than the number of survivors. This is useful in reliability analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Failure Plot( 1 );
```

### [Fitted Distribution Plots](#fitted-distribution-plots)[](#fitted-distribution-plots "Click to copy url")

**Syntax:** obj \<\< Fitted Distribution Plots( state=0\|1 )

**Description:** Shows or hides a set of plots for each fitted distribution. The set of plots includes the fitted survival function, the fitted density function, and the fitted hazard function. If you have not performed a fit, no plot appears.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Weibull Fit( 1 );
obj << Fitted Distribution Plots( 1 );
```

### [Fitted Failure CI](#fitted-failure-ci)[](#fitted-failure-ci "Click to copy url")

**Syntax:** obj \<\< Fitted Failure CI( state=0\|1 )

**Description:** Shows or hides confidence intervals for each group in the Failure Plot. A set of intervals is plotted for each of the fitted distributions.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ), Failure Plot( 1 ) );
obj << Weibull Fit( 1 );
obj << Fitted Failure CI( 1 );
```

### [Fitted Quantile](#fitted-quantile)[](#fitted-quantile "Click to copy url")

**Syntax:** obj \<\< Fitted Quantile( state=0\|1 )

**Description:** Shows or hides straight-line fits for each group in the Exponential Plot, the Weibull Plot, and the LogNormal Plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Exponential Plot( 1 );
obj << Exponential Fit( 1 );
Wait( 1 );
obj << Fitted Quantile( 0 );
```

### [Fitted Quantile CI Lines](#fitted-quantile-ci-lines)[](#fitted-quantile-ci-lines "Click to copy url")

**Syntax:** obj \<\< Fitted Quantile CI Lines( state=0\|1 )

**Description:** Shows or hides the 95% confidence bands for each group in the Exponential Plot, the Weibull Plot, and the LogNormal Plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Lognormal Plot( 1 );
obj << Lognormal Fit( 1 );
obj << Fitted Quantile CI Lines( 1 );
```

### [Fitted Quantile CI Shaded](#fitted-quantile-ci-shaded)[](#fitted-quantile-ci-shaded "Click to copy url")

**Syntax:** obj \<\< Fitted Quantile CI Shaded( state=0\|1 )

**Description:** Shows or hides shaded regions for the 95% confidence bands for each group in the Exponential Plot, the Weibull Plot, and the LogNormal Plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Weibull Plot( 1 );
obj << Weibull Fit( 1 );
obj << Fitted Quantile CI Shaded( 1 );
```

### [Fitted Survival CI](#fitted-survival-ci)[](#fitted-survival-ci "Click to copy url")

**Syntax:** obj \<\< Fitted Survival CI( state=0\|1 )

**Description:** Shows or hides confidence intervals for each group in the Survival Plot. A set of intervals is plotted for each of the fitted distributions.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Exponential Fit( 1 );
obj << Fitted Survival CI( 1 );
```

### [LogNormal Fit](#lognormal-fit)[](#lognormal-fit "Click to copy url")

**Syntax:** obj \<\< LogNormal Fit( state=0\|1 )

**Description:** Shows or hides the LogNormal Parameter Estimates table. This option also adds a linear fit to the lognormal cumulative distribution function in the LogNormal Plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << LogNormal Plot( 1 );
Wait( 1 );
obj << LogNormal Fit( 1 );
```

### [LogNormal Plot](#lognormal-plot)[](#lognormal-plot "Click to copy url")

**Syntax:** obj \<\< LogNormal Plot( state=0\|1 )

**Description:** Shows or hides the LogNormal Plot, which shows the cumulative lognormal failure probability by log(time) for each group. Lines that are approximately linear empirically indicate the appropriateness of using a lognormal model for further analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << LogNormal Plot( 1 );
```

### [Midstep Quantile Points](#midstep-quantile-points)[](#midstep-quantile-points "Click to copy url")

**Syntax:** obj \<\< Midstep Quantile Points( state=0\|1 )

**Description:** Specifies that the modified Kaplan-Meier plotting positions are used in the Exponential Plot, the Weibull Plot, and the LogNormal Plot. These plotting positions are equivalent to taking mid-step positions of the Kaplan-Meier curve, rather than the bottom-of-step positions. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Weibull Plot( 1 );
Wait( 1 );
obj << Midstep Quantile Points( 0 );
```

### [Plot Failure Instead of Survival](#plot-failure-instead-of-survival)[](#plot-failure-instead-of-survival "Click to copy url")

**Syntax:** obj = Survival(...Plot Failure instead of Surivival( state=0\|1 )...)

**Description:** Shows a failure probability plot instead of its reverse (a survival probability plot).

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
    Plot Failure instead of Survival( 1 )
);
```

### [Save Estimates](#save-estimates)[](#save-estimates "Click to copy url")

**Syntax:** obj \<\< Save Estimates

**Description:** Creates a new data table that contains survival and failure estimates, confidence intervals, and other distribution statistics for each group.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Save Estimates;
```

### [Show Combined](#show-combined)[](#show-combined "Click to copy url")

**Syntax:** obj \<\< Show Combined( state=0\|1 )

**Description:** Shows or hides the combined Kaplan-Meier survival functions on both the survival and failure plots.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Failure Plot( 1 );
Wait( 1 );
obj << Show Combined( 1 );
```

### [Show Confid Interval](#show-confid-interval)[](#show-confid-interval "Click to copy url")

**Syntax:** obj \<\< Show Confid Interval( state=0\|1 )

**Description:** Shows or hides the 95% pointwise confidence bands for the Kaplan-Meier survival functions in the Survival Plot and the Failure Plot. This option also shows confidence bands for the combined survival functions when the Show Combined option is selected.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Failure Plot( 1 );
Wait( 1 );
obj << Show Confid Interval( 1 );
Wait( 1 );
obj << Show Combined( 1 );
```

### [Show Kaplan Meier](#show-kaplan-meier)[](#show-kaplan-meier "Click to copy url")

**Syntax:** obj \<\< Show Kaplan Meier( state=0\|1 )

**Description:** Shows or hides the Kaplan-Meier survival functions for each group on both the survival and failure plots. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
    Show Kaplan Meier( 0 )
);
Wait( 1 );
obj << Show Kaplan Meier( 1 );
```

### [Show Points](#show-points)[](#show-points "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides the points in the Survival Plot and the Failure Plot. Failures appear at the bottom of the steps, and censored observations are indicated by points above the steps.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Failure Plot( 1 );
Wait( 1 );
obj << Show Points( 1 );
```

### [Show Shaded Pointwise CI](#show-shaded-pointwise-ci)[](#show-shaded-pointwise-ci "Click to copy url")

**Syntax:** obj \<\< Show Shaded Pointwise CI( state=0\|1 )

**Description:** Shows or hides shaded regions for the 95% pointwise confidence bands for the Kaplan-Meier survival functions in the Survival Plot and the Failure Plot. This option also shows shaded confidence regions for the combined survival functions when the Show Combined option is selected.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Show Shaded Pointwise CI( 1 );
```

### [Show Shaded Simultaneous CI](#show-shaded-simultaneous-ci)[](#show-shaded-simultaneous-ci "Click to copy url")

**Syntax:** obj \<\< Show Shaded Simultaneous CI( state=0\|1 )

**Description:** Shows or hides shaded regions for the 95% simultaneous confidence bands for the Kaplan-Meier survival functions in the Survival Plot and the Failure Plot. This option also shows confidence bands for the combined survival functions when the Show Combined option is selected.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Show Shaded Simultaneous CI( 1 );
```

### [Show Simultaneous CI](#show-simultaneous-ci)[](#show-simultaneous-ci "Click to copy url")

**Syntax:** obj \<\< Show Simultaneous CI( state=0\|1 )

**Description:** Shows or hides the 95% simultaneous confidence bands for the Kaplan-Meier survival functions in the Survival Plot and the Failure Plot. This option also shows confidence bands for the combined survival functions when the Show Combined option is selected.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Show Simultaneous CI( 1 );
```

### [Survival Plot](#survival-plot)[](#survival-plot "Click to copy url")

**Syntax:** obj \<\< Survival Plot( state=0\|1 )

**Description:** Shows or hides the survival plot, which contains overlaid survival curves for each group. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Survival Plot( 0 );
Wait( 1 );
obj << Survival Plot( 1 );
```

### [Weibull Fit](#weibull-fit)[](#weibull-fit "Click to copy url")

**Syntax:** obj \<\< Weibull Fit( state=0\|1 )

**Description:** Shows or hides the Extreme-Value Parameter Estimates and Weibull Parameter Estimates tables. This option also adds a linear fit to the Weibull cumulative distribution function in the Weibull Plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Weibull Plot( 1 );
Wait( 1 );
obj << Weibull Fit( 1 );
```

### [Weibull Plot](#weibull-plot)[](#weibull-plot "Click to copy url")

**Syntax:** obj \<\< Weibull Plot( state=0\|1 )

**Description:** Shows or hides the Weibull Plot, which shows the cumulative Weibull failure probability by log(time) for each group. Lines that are approximately linear empirically indicate the appropriateness of using a Weibull model for further analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Weibull Plot( 1 );
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
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
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
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
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
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
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
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
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
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
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
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
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
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
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
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Survival(
    Y( :days ),
    Censor( :Censor ),
    Grouping( :Group ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
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
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
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

**Syntax:** obj = Survival(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

## [Competing Causes](#competing-causes_1)[](#competing-causes_1 "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Hazard Plot](#hazard-plot)[](#hazard-plot "Click to copy url")

**Syntax:** obj \<\< Hazard Plot( state=0\|1 )

**Description:** Shows or hides a plot of the hazard functions for the data based on the competing causes analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Competing Causes( :Failure Cause );
obj << Hazard Plot( 1 );
```

#### [Omit Causes](#omit-causes)[](#omit-causes "Click to copy url")

**Syntax:** obj \<\< Omit Causes( cause1, \<cause2\>, ... )

**Description:** Enables you to remove specific cause values from the analysis. The survival estimates are automatically recalculated. This option can be used to illustrate the alternative where specific causes are no longer hazardous.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Competing Causes( :Failure Cause );
obj << Omit Causes( "accident" );
```

#### [Save Cause Coordinates](#save-cause-coordinates)[](#save-cause-coordinates "Click to copy url")

**Syntax:** obj \<\< Save Cause Coordinates

**Description:** Saves a new column to the original data table. The new column is calculated as log(-log(Surv)). This value is often plotted against the time variable for the different values of a grouping variable, such as the code for type of failure.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Competing Causes( :Failure Cause );
obj << Save Cause Coordinates;
```

#### [Simulate](#simulate)[](#simulate "Click to copy url")

**Syntax:** obj \<\< Simulate( number )

**Description:** Creates a new data table that contains simulated time and cause information. The fitted Weibull distribution is used to simulate the new data.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Competing Causes( :Failure Cause );
obj << Simulate( 1000 );
```

#### [Weibull Lines](#weibull-lines)[](#weibull-lines "Click to copy url")

**Syntax:** obj \<\< Weibull Lines( state=0\|1 )

**Description:** Shows or hides Weibull lines in the survival plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
obj << Competing Causes( :Failure Cause );
obj << Weibull Lines( 1 );
```

[ Previous](Surface%20Plot.html "Surface Plot") [Next ](Tabulate.html "Tabulate")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
