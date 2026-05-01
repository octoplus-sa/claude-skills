# Data Table

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Data%20Table.html](https://jsl.jmp.com/All%20Categories/Objects/Data%20Table.html)*

---

# [Data Table](#data-table)[](#data-table "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Association Analysis](#association-analysis)[](#association-analysis "Click to copy url")

**Syntax:** Association Analysis( Item( columns ), ID( columns ) )

**Description:** Identifies connections among groups of items in an independent event or transaction. Association analysis is frequently used to analyze transactional data (also called market baskets) to identify items that often appear together in transactions.

``` jsl
dt = Open( "$SAMPLE_DATA/Grocery Purchases.jmp" );
obj = dt << Association Analysis( Item( :Product ), ID( :Customer ID ) );
```

### [Attribute Chart](#attribute-chart)[](#attribute-chart "Click to copy url")

**Syntax:** Attribute Chart( Y( columns ), X( columns ) )

**Description:** Analyzes categorical measurements to show you measures of agreement across responses, such as raters.

``` jsl
dt = Open( "$SAMPLE_DATA/Attribute Gauge.jmp" );
obj = dt << Attribute Chart( Y( :A, :B, :C ), X( :Part ), Standard( :Standard ) );
```

### [Bayesian Optimization](#bayesian-optimization)[](#bayesian-optimization "Click to copy url")

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

### [Bivariate](#bivariate)[](#bivariate "Click to copy url")

**Syntax:** Bivariate( Y( columns ), X( columns ) )

**Description:** Models a continuous response with respect to another continuous variable. Analysis methods include fitting lines, polynomials, splines, and bivariate densities.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
```

### [Boosted Tree](#boosted-tree)[](#boosted-tree "Click to copy url")

**Syntax:** Boosted Tree (Y( column ), X( columns ))

**Description:** Constructs a predictive model by building a large, additive decision tree that is a sequence of smaller decision trees. Each of the trees is fit on the residuals of the previous tree.

``` jsl
dt = Open( "$SAMPLE_DATA/Diabetes.jmp" );
obj = dt << Boosted Tree(
    Y( :Y ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Validation( :Validation ),
    Go
);
```

### [Bootstrap Forest](#bootstrap-forest)[](#bootstrap-forest "Click to copy url")

**Syntax:** Bootstrap Forest (Y( column ), X( columns ))

**Description:** Constructs a predictive model by averaging predicted values from many decision trees. Each decision tree is fit to a random bootstrap sample of the training data.

``` jsl
dt = Open( "$SAMPLE_DATA/Diabetes.jmp" );
obj = dt << Bootstrap Forest(
    Y( :Y ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Validation( :Validation ),
    Minimum Splits Per Tree( 5 ),
    Portion Bootstrap( 1 ),
    Number Terms( 3 ),
    Number Trees( 25 ),
    Go
);
```

### [Bubble Plot](#bubble-plot)[](#bubble-plot "Click to copy url")

**Syntax:** Bubble Plot( X( column ), Y( column ), \<Sizes( column )\>, \<Time( column )\>, \<ID( column )\>, \<Coloring( column ) )

**Description:** Produces a two-dimensional scatterplot of bubbles that can be animated over a time variable. Additional variables can be used to size and color the bubbles.

``` jsl
dt = Open( "$SAMPLE_DATA/PopAgeGroup.jmp" );
obj = dt << Bubble Plot(
    X( :"Portion 0-19"n ),
    Y( :"Portion60+"n ),
    Sizes( :Pop ),
    ID( :Country )
);
```

### [CUSUM Control Chart](#cusum-control-chart)[](#cusum-control-chart "Click to copy url")

**Syntax:** CUSUM Control Chart( Y( column ), \<X( column )\>, \<By( column )\>, \<Data Units( 0\|1 )\>, \<Show Excluded Region( 0\|1 )\> )

**Description:** Creates a chart that plots the cumulative sums of deviations of subgroup means from a target. This chart is also called a tabular CUSUM chart.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Oil1 Cusum.jmp" );
obj = dt << CUSUM Control Chart(
    Y( :weight ),
    H( 2 ),
    Lower Side( 1 ),
    Target( 8.1 ),
    K( 0.025 ),
    Sigma( 0.05 ),
    Head Start( 0.05 )
);
```

### [Categorical](#categorical)[](#categorical "Click to copy url")

**Syntax:** Categorical( Responses \| Aligned Responses \| Repeated Measures \| Rater Agreement \| Multiple Response \| Multiple Response by ID \| Multiple Delimited \| Indicator Group \| Response Frequencies( column ), X( column(s) ) )

**Description:** Summarizes and analyzes categorical response data. Data can be simple responses, multiple responses, repeated measures, rater agreement, aligned responses, or free text. Includes the ability to generate custom cross tabulations of responses.

#### [Aligned Responses](#aligned-responses)[](#aligned-responses "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
Categorical(
    Structured(
        Empty(),
        Empty(),
        Aligned Responses(
            :I am working on my career, :I want to see the world,
            :My home needs some major improvements, :I have vast interests outside of work,
            :I want to get my debt under control, :I come from a large family
        )
    )
);
```

#### [Multiple Response (Structured)](#multiple-response-structured)[](#multiple-response-structured "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
Categorical( Structured( :Gender, :Brush Delimited + :Floss Delimited ) );
```

#### [Multiple Response with Nested Groups](#multiple-response-with-nested-groups)[](#multiple-response-with-nested-groups "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Quality Control/Failure3MultipleField.jmp" );
Categorical( X( :clean, :date ), Multiple Response( :Failure1, :Failure2, :Failure3 ) );
```

#### [Nested within Individual Factors](#nested-within-individual-factors)[](#nested-within-individual-factors "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
Categorical(
    Structured(
        :Single Status * :Gender + :School Age Children * :Gender,
        :I am working on my career + :I want to see the world
    )
);
```

#### [One Response by Two Nested Factors](#one-response-by-two-nested-factors)[](#one-response-by-two-nested-factors "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Categorical( X( :sex, :marital status ), Responses( :country ) );
```

#### [Rater Agreement](#rater-agreement)[](#rater-agreement "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Attribute Gauge.jmp" );
Categorical( Rater Agreement( :A, :B, :C ) );
```

#### [Repeated Measures](#repeated-measures)[](#repeated-measures "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Presidential Elections.jmp" );
Categorical(
    Repeated Measures(
        :"1980 Winner"n, :"1984 Winner"n, :"1988 Winner"n, :"1992 Winner"n, :"1996 Winner"n,
        :"2000 Winner"n, :"2004 Winner"n, :"2008 Winner"n, :"2012 Winner"n
    )
);
```

#### [Three Responses by Two Individual Factors (Structured)](#three-responses-by-two-individual-factors-structured)[](#three-responses-by-two-individual-factors-structured "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
Categorical(
    Structured(
        :I am working on my career + :I want to see the world,
        :Gender + :Single Status + :Age Group
    )
);
```

### [Cell Plot](#cell-plot)[](#cell-plot "Click to copy url")

**Syntax:** Cell Plot( Y( column(s) ), \<X( column )\> )

**Description:** Produces a rectangular grid of cells drawn with one-to-one correspondence to data table values. The cells in the grid are colored by the values in the cells.

``` jsl
dt = Open( "$SAMPLE_DATA/SAT.jmp" );
obj = dt << Cell Plot(
    Y(
        :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n, :"2002 Verbal"n,
        :"2002 Math"n, :"2001 Verbal"n, :"2001 Math"n, :"1999 Verbal"n, :"1999 Math"n,
        :"1994 Verbal"n, :"1994 Math"n, :"1997 Verbal"n, :"1997 Math"n, :"1992 Verbal"n,
        :"1992 Math"n
    )
);
```

### [Choice](#choice)[](#choice "Click to copy url")

**Syntax:** Choice( Profile DataTable( data table ), Profile ID( column ), Profile Effects( column(s) ), \<Response Data Table( data table )\>, \<Subject Data Table( data table )\>, \<Response Profile ID Chosen( column )\>, \<Response Subject ID( column)\>, \<Response Grouping( column(s) )\>, \<Response Profile ID Choices( column(s) )\>, \<Profile Grouping( column(s) )\>, \<Subject Subject ID( column )\>, \<Subject Effects( column(s) )\> )

**Description:** Models data from a choice experiment that studies customer preferences. Estimates the probability that a specific configuration is preferred using a form of conditional logistic regression.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Pizza Profiles.jmp" );
dt2 = Open( "$SAMPLE_DATA/Pizza Responses.jmp" );
obj = dt << Choice(
    Response Data Table( Data Table( "Pizza Responses" ) ),
    Profile DataTable( Data Table( "Pizza Profiles" ) ),
    Response Profile ID Chosen( :Choice ),
    Response Subject ID( :Subject ),
    Response Profile ID Choices( :Choice1, :Choice2 ),
    Profile ID( :ID ),
    Profile Effects( :Crust, :Cheese, :Topping )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Pizza Combined.jmp" );
obj = Choice(
    One Table( 1 ),
    Profile DataTable( dt ),
    Profile ID( :Indicator ),
    Profile Effects( :Crust, :Cheese, :Topping ),
    Profile Grouping( :Subject, :Trial )
);
```

### [Close](#close)[](#close "Click to copy url")

**Syntax:** Close( \<dataTableRef\|name\>, \<NoSave\|Save( "path" )\> )

**Description:** Closes the data table referenced by the first argument, which defaults to the current data table. The second argument is used to save the data table. Use an appropriate file extension in the path to save the data table as a non-JMP format. Specifying NoSave bypasses the prompt to save or disregard changes.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
Close( dt );
```

### [Cluster Variables](#cluster-variables)[](#cluster-variables "Click to copy url")

**Syntax:** Cluster Variables( Y( columns ) )

**Description:** Clusters variables (columns) into groups that can be represented by a single component or variable. Cluster variables can be used as a dimension reduction technique.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Cluster Variables( Y( :OZONE, :CO, :SO2, :NO, :PM10 ) );
```

### [Contingency](#contingency)[](#contingency "Click to copy url")

**Syntax:** Contingency( Y( columns ), X( columns ) )

**Description:** Models a categorical response across a set of categorical groups. Analysis methods include chi-square tests and mosaic plots.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Contingency( Y( :Age ), X( :sex ) );
```

### [Contour Plot](#contour-plot)[](#contour-plot "Click to copy url")

**Syntax:** Contour Plot( X( column, column ), Y( column ) )

**Description:** Produces a graph of three variables in a two-dimensional view, where the third variable is represented by contour curves of equal value.

``` jsl
dt = Open( "$SAMPLE_DATA/Little Pond.jmp" );
obj = dt << Contour Plot( X( :X, :Y ), Y( :Z ) );
```

### [Contour Profiler](#contour-profiler)[](#contour-profiler "Click to copy url")

**Syntax:** Contour Profiler( Y( column1, column2, ... ) )

**Description:** Produces an interactive contour plot that enables you to explore how one or more predicted responses change across pairs of factors. The values of factors not used in the plot can be varied to further explore the impact of the factor settings on the predicted responses.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Contour Profiler(
    Y(
        :Pred Formula ABRASION, :Pred Formula MODULUS, :Pred Formula ELONG,
        :Pred Formula HARDNESS
    )
);
```

### [Control Chart Builder](#control-chart-builder)[](#control-chart-builder "Click to copy url")

**Syntax:** Control Chart Builder( Class( "Shewhart Variables"\|"Shewhart Attribute"\|"Short Run"\|"Rare Event" ), Variables( variables ), \<Chart( Position( number ), Points( Statistic( "statistic" ), \<points options\> ), Limits( Sigma( "sigma" ), \<limits options\> )\> ) ) )

**Description:** Enables you to interactively create control charts, which are used to determine whether a process is stable and predictable. The Control Chart Builder platform can be used to create the following types of control charts: IMR, XBar, Short Run, Run, P, NP, C, U, Laney P', Laney U', Levey-Jennings, IMR on Means, Three Way, and Rare Event charts.

#### [C Chart](#c-chart)[](#c-chart "Click to copy url")

``` jsl
// Create a C chart by adding a Y variable, changing the Class to Shewhart Attribute, changing the Statistic to Count, and changing the Sigma to Poisson.
dt = Open( "$SAMPLE_DATA/Quality Control/Orange Juice.jmp" );
obj = dt << Control Chart Builder(
    Class( "Shewhart Attribute" ),
    Variables( Subgroup( :Sample ), Y( :Status ), Phase( :Phase ) ),
    Chart( Points( Statistic( "Count" ) ), Limits( Sigma( "Poisson" ) ) ),
    Show Control Panel( 0 )
);
```

#### [IMR Chart](#imr-chart)[](#imr-chart "Click to copy url")

``` jsl
// Create an IMR chart by adding a continuous Y variable.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder( Variables( Y( :Weight ) ), Show Control Panel( 0 ) );
```

#### [IMR on Group Standard Deviation Chart (Set Subgroup Size)](#imr-on-group-standard-deviation-chart-set-subgroup-size)[](#imr-on-group-standard-deviation-chart-set-subgroup-size "Click to copy url")

``` jsl
// Create an IMR on Group Standard Deviation chart by adding a Y variable and defining a subgroup size, and changing the Statistic on the location chart to Standard Deviation, on the dispersion chart to Moving Range on Std Dev and the Sigma on both charts to Moving Range.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Y( :Weight ) ),
    Set Subgroup Size( 4 ),
    Chart(
        Position( 1 ),
        Points( Statistic( "Standard Deviation" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Std Dev" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [IMR on Group Standard Deviation Chart (Subgroup Variable)](#imr-on-group-standard-deviation-chart-subgroup-variable)[](#imr-on-group-standard-deviation-chart-subgroup-variable "Click to copy url")

``` jsl
// Create an IMR on Group Standard Deviation chart by adding a Y variable and a subgroup variable, and changing the Statistic on the location chart to Standard Deviation, on the dispersion chart to Moving Range on Std Dev and the Sigma on both charts to Moving Range.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Subgroup( :Sample ), Y( :Weight ) ),
    Chart(
        Position( 1 ),
        Points( Statistic( "Standard Deviation" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Std Dev" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [IMR on Means Chart (Set Subgroup Size)](#imr-on-means-chart-set-subgroup-size)[](#imr-on-means-chart-set-subgroup-size "Click to copy url")

``` jsl
// Create an IMR on Means chart by adding a Y variable and defining a subgroup size, and changing the Statistic on the dispersion chart to Moving Range on Means and the Sigma on both charts to Moving Range.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Y( :Weight ) ),
    Set Subgroup Size( 4 ),
    Chart( Position( 1 ), Limits( Sigma( "Moving Range" ) ) ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Means" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [IMR on Means Chart (Subgroup Variable)](#imr-on-means-chart-subgroup-variable)[](#imr-on-means-chart-subgroup-variable "Click to copy url")

``` jsl
// Create an IMR on Means chart by adding a Y variable and a subgroup variable, and changing the Statistic on the dispersion chart to Moving Range on Means and the Sigma on both charts to Moving Range.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Subgroup( :Sample ), Y( :Weight ) ),
    Chart( Position( 1 ), Limits( Sigma( "Moving Range" ) ) ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Means" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [Levey-Jennings Chart](#levey-jennings-chart)[](#levey-jennings-chart "Click to copy url")

``` jsl
// Create a Levey-Jennings chart by adding a Y variable, removing the dispersion chart, and changing the Sigma to Levey Jennings. Make sure that the Statistic is set to Individual.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Show Two Shewhart Charts( 0 ),
    Variables( Y( :Weight ) ),
    Chart( Points( Statistic( "Individual" ) ), Limits( Sigma( "Levey Jennings" ) ) ),
    Show Control Panel( 0 )
);
```

#### [Median Moving Range Chart](#median-moving-range-chart)[](#median-moving-range-chart "Click to copy url")

``` jsl
// Create a Median Moving Range chart by adding a Y variable and changing the Sigma to Median Moving Range on both the location and dispersion charts.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Y( :Weight ) ),
    Chart( Position( 1 ), Limits( Sigma( "Median Moving Range" ) ) ),
    Chart( Position( 2 ), Limits( Sigma( "Median Moving Range" ) ) ),
    Show Control Panel( 0 )
);
```

#### [Median Moving Range on Group Means Chart (Set Subgroup Size)](#median-moving-range-on-group-means-chart-set-subgroup-size)[](#median-moving-range-on-group-means-chart-set-subgroup-size "Click to copy url")

``` jsl
// Create a Median Moving Range on Group Means chart by adding a Y variable and defining a subgroup size, changing the Statistic on the dispersion chart to Moving Range on Means, and changing the Sigma to Median Moving Range on both the location and dispersion charts.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Y( :Weight ) ),
    Set Subgroup Size( 4 ),
    Chart( Position( 1 ), Limits( Sigma( "Median Moving Range" ) ) ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Means" ) ),
        Limits( Sigma( "Median Moving Range" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [Median Moving Range on Group Means Chart (Subgroup Variable)](#median-moving-range-on-group-means-chart-subgroup-variable)[](#median-moving-range-on-group-means-chart-subgroup-variable "Click to copy url")

``` jsl
// Create a Median Moving Range on Group Means chart by adding a Y variable and a subgroup variable, changing the Statistic on the dispersion chart to Moving Range on Means, and changing the Sigma to Median Moving Range on both the location and dispersion charts.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Subgroup( :Sample ), Y( :Weight ) ),
    Chart( Position( 1 ), Limits( Sigma( "Median Moving Range" ) ) ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Means" ) ),
        Limits( Sigma( "Median Moving Range" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [Median Moving Range on Group Standard Deviations Chart (Set Subgroup Size)](#median-moving-range-on-group-standard-deviations-chart-set-subgroup-size)[](#median-moving-range-on-group-standard-deviations-chart-set-subgroup-size "Click to copy url")

``` jsl
// Create a Median Moving Range on Group Standard Deviations chart by adding a Y variable and defining a subgroup size, changing the Statistic on the location chart to Standard deviation, on the dispersion chart to Moving Range on Std Dev, and changing the Sigma to Median Moving Range on both the location and dispersion charts.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Y( :Weight ) ),
    Set Subgroup Size( 4 ),
    Chart(
        Position( 1 ),
        Points( Statistic( "Standard Deviation" ) ),
        Limits( Sigma( "Median Moving Range" ) )
    ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Std Dev" ) ),
        Limits( Sigma( "Median Moving Range" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [Median Moving Range on Group Standard Deviations Chart (Subgroup Variable)](#median-moving-range-on-group-standard-deviations-chart-subgroup-variable)[](#median-moving-range-on-group-standard-deviations-chart-subgroup-variable "Click to copy url")

``` jsl
// Create a Median Moving Range on Group Standard Deviations chart by adding a Y variable and a subgroup variable, changing the Statistic on the location chart to Standard deviation, on the dispersion chart to Moving Range on Std Dev, and changing the Sigma to Median Moving Range on both the location and dispersion charts.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Subgroup( :Sample ), Y( :Weight ) ),
    Chart(
        Position( 1 ),
        Points( Statistic( "Standard Deviation" ) ),
        Limits( Sigma( "Median Moving Range" ) )
    ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Std Dev" ) ),
        Limits( Sigma( "Median Moving Range" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [NP Chart](#np-chart)[](#np-chart "Click to copy url")

``` jsl
// Create an NP chart by adding a Y variable, changing the Class to Shewhart Attribute, changing the Statistic to Count, and changing the Sigma to Binomial (P, NP).
dt = Open( "$SAMPLE_DATA/Quality Control/Orange Juice.jmp" );
obj = dt << Control Chart Builder(
    Class( "Shewhart Attribute" ),
    Variables( Subgroup( :Sample ), Y( :Status ), Phase( :Phase ) ),
    Chart( Points( Statistic( "Count" ) ), Limits( Sigma( "Binomial" ) ) ),
    Show Control Panel( 0 )
);
```

#### [P Chart](#p-chart)[](#p-chart "Click to copy url")

``` jsl
// Create a P chart by adding a Y variable, changing the Class to Shewhart Attribute, changing the Statistic to Proportion, and changing the Sigma to Binomial (P, NP).
dt = Open( "$SAMPLE_DATA/Quality Control/Orange Juice.jmp" );
obj = dt << Control Chart Builder(
    Class( "Shewhart Attribute" ),
    Variables( Subgroup( :Sample ), Y( :Status ), Phase( :Phase ) ),
    Chart( Points( Statistic( "Proportion" ) ), Limits( Sigma( "Binomial" ) ) ),
    Show Control Panel( 0 )
);
```

#### [P' Chart](#p-chart_1)[](#p-chart_1 "Click to copy url")

``` jsl
// Create a P' chart by adding a Y variable, changing the Class to Shewhart Attribute, changing the Statistic to Proportion, and changing the Sigma to Laney P'.
dt = Open( "$SAMPLE_DATA/Quality Control/Washers.jmp" );
obj = dt << Control Chart Builder(
    Class( "Shewhart Attribute" ),
    Variables( Subgroup( :Lot ), Y( :"# defective"n ), n Trials( :Lot Size ) ),
    Chart( Points( Statistic( "Proportion" ) ), Limits( Sigma( "Laney P Prime" ) ) ),
    Show Control Panel( 0 )
);
```

#### [Rare Event G Chart](#rare-event-g-chart)[](#rare-event-g-chart "Click to copy url")

``` jsl
// Create a G chart by changing the class to Rare Event and adding a nonnegative discrete Y variable. Make sure that the Sigma is set to Negative Binomial.
dt = Open( "$SAMPLE_DATA/Quality Control/Fan Burnout.jmp" );
obj = dt << Control Chart Builder(
    Class( "Rare Event" ),
    Variables( Subgroup( :Burnout ), Y( :Hours between Burnouts ) ),
    Chart( Points( Statistic( "Count" ) ), Limits( Sigma( "Negative Binomial" ) ) ),
    Show Control Panel( 0 )
);
```

#### [Rare Event T Chart](#rare-event-t-chart)[](#rare-event-t-chart "Click to copy url")

``` jsl
// Create a T chart by changing the class to Rare Event, changing the Sigma to Weibull, and adding a nonnegative discrete Y variable.
dt = Open( "$SAMPLE_DATA/Quality Control/Fan Burnout.jmp" );
obj = dt << Control Chart Builder(
    Class( "Rare Event" ),
    Variables( Subgroup( :Burnout ), Y( :Hours between Burnouts ) ),
    Chart( Points( Statistic( "Count" ) ), Limits( Sigma( "Weibull" ) ) ),
    Show Control Panel( 0 )
);
```

#### [Run Chart](#run-chart)[](#run-chart "Click to copy url")

``` jsl
// Create a Run chart by adding a Y variable, turning off the limits, and removing the dispersion chart.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Show Two Shewhart Charts( 0 ),
    Show Limit Summaries( 0 ),
    Variables( Y( :Weight ) ),
    Chart( Limits( Show Lower Limit( 0 ), Show Upper Limit( 0 ) ) ),
    Show Control Panel( 0 )
);
```

#### [Short Run Difference Chart](#short-run-difference-chart)[](#short-run-difference-chart "Click to copy url")

``` jsl
// Create a Short Run Difference chart by changing the class to Short Run and adding a Product or Part variable. Make sure that the Statistic values for the location chart and dispersion chart are set to Centered and Moving Range Centered, respectively. Centered Short Run control charts are sometimes referred to as Deviation from Nominal (DNOM) charts.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Class( "Short Run" ),
    Variables( Y( :Weight ), Part( :Product ) ),
    Show Control Panel( 0 )
);
```

#### [Short Run Difference Chart for XBar](#short-run-difference-chart-for-xbar)[](#short-run-difference-chart-for-xbar "Click to copy url")

``` jsl
// Create a Short Run Difference chart for summarized data by changing the class to Short Run and adding a Product or Part variable,  Short Run Standardized charts are sometimes referred to as Z-MR charts. Centered Short Run control charts are sometimes referred to as Deviation from Nominal (DNOM) charts.
dt = Open( "$SAMPLE_DATA/Quality Control/Fancy Chocolate Factory.jmp" );
obj = dt << Control Chart Builder(
    Show Product Separators( 0 ),
    Class( "Short Run" ),
    Variables( Subgroup( :Box ), Y( :"%Cocoa"n ), Part( :Product ) ),
    Show Control Panel( 0 )
);
```

#### [Short Run Standardized Chart](#short-run-standardized-chart)[](#short-run-standardized-chart "Click to copy url")

``` jsl
// Create a Short Run Standardized chart by changing the class to Short Run and adding a Subgroup and a Product or Part variable, changing the Statistic for the location chart type to Standardized, and changing the Statistic for the dispersion chart to Moving Range Standardized. Short Run Standardized charts are sometimes referred to as Z-MR charts.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Class( "Short Run" ),
    Variables( Y( :Weight ), Part( :Product ) ),
    Chart( Position( 1 ), Points( Statistic( "Standardized" ) ) ),
    Chart( Position( 2 ), Points( Statistic( "Moving Range Standardized" ) ) ),
    Show Control Panel( 0 )
);
```

#### [Short Run Standardized Chart for XBar](#short-run-standardized-chart-for-xbar)[](#short-run-standardized-chart-for-xbar "Click to copy url")

``` jsl
// Create a Short Run Standardized chart for summarized data by changing the class to Short Run and adding a Subgroup and a Product or Part variable,  Short Run Standardized charts are sometimes referred to as Z-MR charts. Centered Short Run control charts are sometimes referred to as Deviation from Nominal (DNOM) charts.
dt = Open( "$SAMPLE_DATA/Quality Control/Fancy Chocolate Factory.jmp" );
obj = dt << Control Chart Builder(
    Show Product Separators( 0 ),
    Class( "Short Run" ),
    Variables( Subgroup( :Box ), Y( :"%Cocoa"n ), Part( :Product ) ),
    Chart( Position( 1 ), Points( Statistic( "Standardized" ) ) ),
    Chart( Position( 2 ), Points( Statistic( "Range Standardized" ) ) ),
    Show Control Panel( 0 )
);
```

#### [Three Way Chart (Set Subgroup Size)](#three-way-chart-set-subgroup-size)[](#three-way-chart-set-subgroup-size "Click to copy url")

``` jsl
// Create a Three Way chart by adding a dispersion chart after adding a Y variable and setting a subgroup size.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Y( :Weight ) ),
    Set Subgroup Size( 4 ),
    Chart(
        Position( 1 ),
        Points( Statistic( "Average" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Means" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Chart(
        Position( 3 ),
        Points( Statistic( "Standard Deviation" ) ),
        Limits( Sigma( "Standard Deviation" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [Three Way Chart (Subgroup Variable)](#three-way-chart-subgroup-variable)[](#three-way-chart-subgroup-variable "Click to copy url")

``` jsl
// Create a Three Way chart by adding a dispersion chart after adding a Y variable and adding a subgroup variable.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Subgroup( :Sample ), Y( :Weight ) ),
    Chart(
        Position( 1 ),
        Points( Statistic( "Average" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Moving Range on Means" ) ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Chart( Position( 3 ), Points( Statistic( "Range" ) ), Limits( Sigma( "Range" ) ) ),
    Show Control Panel( 0 )
);
```

#### [U Chart](#u-chart)[](#u-chart "Click to copy url")

``` jsl
// Create a U chart by adding a Y variable, changing the Class to Shewhart Attribute, changing the Statistic to Proportion, and changing the Sigma to Poisson.
dt = Open( "$SAMPLE_DATA/Quality Control/Orange Juice.jmp" );
obj = dt << Control Chart Builder(
    Class( "Shewhart Attribute" ),
    Variables( Subgroup( :Sample ), Y( :Status ), Phase( :Phase ) ),
    Chart( Points( Statistic( "Proportion" ) ), Limits( Sigma( "Poisson" ) ) ),
    Show Control Panel( 0 )
);
```

#### [U' Chart](#u-chart_1)[](#u-chart_1 "Click to copy url")

``` jsl
// Create a U' chart by adding a Y variable, changing the Class to Shewhart Attribute, changing the Statistic to Proportion, and changing the Sigma to Laney U'.
dt = Open( "$SAMPLE_DATA/Quality Control/Washers.jmp" );
obj = dt << Control Chart Builder(
    Class( "Shewhart Attribute" ),
    Variables( Subgroup( :Lot ), Y( :"# defective"n ), n Trials( :Lot Size ) ),
    Chart( Points( Statistic( "Proportion" ) ), Limits( Sigma( "Laney U Prime" ) ) ),
    Show Control Panel( 0 )
);
```

#### [XBar/R Chart](#xbarr-chart)[](#xbarr-chart "Click to copy url")

``` jsl
// Create an XBar/R chart by adding a subgroup or setting a subgroup size after adding a Y variable.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Y( :Weight ) ),
    Set Subgroup Size( 4 ),
    Show Control Panel( 0 )
);
```

#### [XBar/S Chart (Set Subgroup Size)](#xbars-chart-set-subgroup-size)[](#xbars-chart-set-subgroup-size "Click to copy url")

``` jsl
// Create an XBar/S chart by adding a Y variable and defining a subgroup size, changing the Statistic for the dispersion chart to Standard Deviation, and changing the Sigma for the location chart to Standard Deviation.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Y( :Weight ) ),
    Set Subgroup Size( 4 ),
    Chart( Position( 1 ), Limits( Sigma( "Standard Deviation" ) ) ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Standard Deviation" ) ),
        Limits( Sigma( "Standard Deviation" ) )
    ),
    Show Control Panel( 0 )
);
```

#### [XBar/S Chart (Subgroup Variable)](#xbars-chart-subgroup-variable)[](#xbars-chart-subgroup-variable "Click to copy url")

``` jsl
// Create an XBar/S chart by adding a Y variable and a subgroup variable, changing the Statistic for the dispersion chart to Standard Deviation, and changing the Sigma for the location chart to Standard Deviation.
dt = Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
obj = dt << Control Chart Builder(
    Variables( Subgroup( :Sample ), Y( :Weight ) ),
    Chart( Position( 1 ), Limits( Sigma( "Standard Deviation" ) ) ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Standard Deviation" ) ),
        Limits( Sigma( "Standard Deviation" ) )
    ),
    Show Control Panel( 0 )
);
```

### [Cumulative Damage](#cumulative-damage)[](#cumulative-damage "Click to copy url")

**Syntax:** Cumulative Damage

**Description:** Analyzes varying-stress and step-stress models.

``` jsl
Open( "$SAMPLE_DATA/Reliability/CD Step Stress.jmp" );
Open( "$SAMPLE_DATA/Reliability/CD Step Stress Pattern.jmp" );
obj = Cumulative Damage(
    Model Type( "Step Stress" ),
    Time to Event Data Table(
        Data Table( "CD Step Stress" ),
        Time to Event( :Time ),
        Censor( :Censor ),
        Pattern ID( :Pattern ID ),
        Censor Code( 1 )
    ),
    Step Stress Pattern Data Table(
        Data Table( "CD Step Stress Pattern" ),
        Stress Duration( :Duration ),
        Stress( :Stress ),
        Pattern ID( :Pattern ID )
    ),
    Relationship( "Inverse Power" ),
    Distribution( "Lognormal" ),
    Pattern Continuation( "Terminate" )
);
```

### [Custom Profiler](#custom-profiler)[](#custom-profiler "Click to copy url")

**Syntax:** Custom Profiler( Y( column1, column2, ... ) )

**Description:** Provides an interface that enables you to optimize responses without a graphical output. This profiler is useful for larger problems.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Custom Profiler(
    Y(
        :Pred Formula ABRASION, :Pred Formula MODULUS, :Pred Formula ELONG,
        :Pred Formula HARDNESS
    )
);
```

### [Degradation](#degradation)[](#degradation "Click to copy url")

**Syntax:** Degradation( Y( column ), Time( column ), Application( "Repeated Measures Degradation"\|"Destructive Degradation"\|"Stability Test" ), \<X( column )\>, \<Label( column )\>, \<Freq( column )\>, \<Censor( column )\>, \<Censor Code( value )\>, \<Upper Spec Limit( value )\>, \<Lower Spec Limit( value )\>, \<Censoring Time( value )\> )

**Description:** Models degradation over time using linear and nonlinear curves. Analysis options include stability analysis and generation of pseudo-failure data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/GaAs Laser.jmp" );
obj = dt << Degradation(
    Y( :Current ),
    Time( :Hours ),
    Label( :Unit ),
    Application( "Repeated Measures Degradation" ),
    Upper Spec Limit( 10 ),
    Model Report(
        Simple Linear Path(
            X Scale( Linear ),
            Y Scale( Linear ),
            Intercept( Common ),
            Slope( Different )
        )
    )
);
```

### [Destructive Degradation](#destructive-degradation)[](#destructive-degradation "Click to copy url")

**Syntax:** Destructive Degradation( Y( column ), Time( column ), \<X( column )\>, \<Freq( column )\>, \<Censor( column ), Censor Code( value )\> )

**Description:** Models destructive degradation data over time.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Adhesive Bond.jmp" );
obj = dt << Destructive Degradation(
    Y( :Strength ),
    Time( :Weeks ),
    X( :Degrees ),
    Censor( :Censor ),
    Censor Code( "Right" ),
    Model( "Log10", "Sqrt", "Normal", "Individual Path with Intercept" ),
    Control( "Log10", "Sqrt", "Normal", "Individual Path with Intercept" )
);
```

### [Diagram](#diagram)[](#diagram "Click to copy url")

**Syntax:** Diagram( Y( column ), X( column ) )

**Description:** Creates a cause and effect diagram. Also called Ishikawa or fishbone diagrams. These are hierarchical diagrams that enable you to explore root causes.

``` jsl
dt = Open( "$SAMPLE_DATA/Ishikawa.jmp" );
obj = dt << Diagram( Y( :Child ), X( :Parent ) );
```

### [Discriminant](#discriminant)[](#discriminant "Click to copy url")

**Syntax:** Discriminant( Y( columns ), X( columns ) )

**Description:** Estimates the distance from each observation to each group's multivariate mean (centroid) using Mahalanobis distance. The observations are then classified into the group that they are closest to.

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Discriminant(
    X( :Species ),
    Y( :Sepal length, :Sepal width, :Petal length, :Petal width )
);
```

### [Distance Matrix](#distance-matrix)[](#distance-matrix "Click to copy url")

**Syntax:** Distance Matrix( Y( columns ) )

**Description:** Computes distances between rows using a variety of methods.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Distance Matrix( Y( :Sepal length, :Sepal width, :Petal length, :Petal width ) );
```

### [Distribution](#distribution)[](#distribution "Click to copy url")

**Syntax:** Distribution( Column() )

**Description:** Shows the distribution and univariate summary statistics for each variable. Results and options depend on the modeling type of each variable. Some options include histograms, box plots, quantile plots, fitting distributions, and capability analysis.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Distribution( Column( :Age, :Weight ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
colref = Column( "age" );
// Correct way to use the colref
Distribution( Column( colref ) );
// This will not work
Distribution( colref );
```

### [EMP Measurement Systems Analysis](#emp-measurement-systems-analysis)[](#emp-measurement-systems-analysis "Click to copy url")

**Syntax:** EMP Measurement Systems Analysis( Y( column ), X( columns ), Part(column), Model(Main\|Crossed\|Crossed with Two Factor Interactions\|Nested\|Crossed then Nested\|Nested then Crossed), Dispersion Chart Type(Range\|Standard Deviation) )

**Description:** Launches the EMP (Evaluating the Measurement Process) method for Measurement Systems Analysis. The average and dispersion (range or standard deviation) charts are displayed by default.

#### [Crossed Effects Model, Range Chart](#crossed-effects-model-range-chart)[](#crossed-effects-model-range-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/Gasket.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator ),
    Part( :Part ),
    Model( "Crossed" ),
    Dispersion Chart Type( "Range" ),
    Variance Components( 1 )
);
```

#### [Crossed Effects Model, Std Dev Chart](#crossed-effects-model-std-dev-chart)[](#crossed-effects-model-std-dev-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/Gasket.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator ),
    Part( :Part ),
    Model( "Crossed" ),
    Dispersion Chart Type( "Standard Deviation" ),
    Variance Components( 1 )
);
```

#### [Crossed then Nested Effects Model, Range Chart](#crossed-then-nested-effects-model-range-chart)[](#crossed-then-nested-effects-model-range-chart "Click to copy url")

``` jsl
dt = New Table( "3 Factors Crossed then Nested",
    Add Rows( 81 ),
    New Column( "Operator",
        Character( 7 ),
        "Nominal",
        Set Values(
            {"Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara",
            "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara",
            "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Jane", "Jane",
            "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane",
            "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane",
            "Jane", "Jane", "Jane", "Jane", "Jane"}
        ),
        Set Display Width( 0 )
    ),
    New Column( "Instrument",
        Character( 1 ),
        "Nominal",
        Set Values(
            {"A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B",
            "B", "B", "C", "C", "C", "C", "C", "C", "C", "C", "C", "A", "A", "A", "A", "A",
            "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B", "B", "B", "C", "C", "C",
            "C", "C", "C", "C", "C", "C", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B",
            "B", "B", "B", "B", "B", "B", "B", "B", "C", "C", "C", "C", "C", "C", "C", "C",
            "C"}
        ),
        Set Display Width( 0 )
    ),
    New Column( "Part",
        Numeric,
        "Nominal",
        Format( "Best", 8 ),
        Set Values(
            [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9,
            10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16,
            16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23,
            23, 23, 24, 24, 24, 25, 25, 25, 26, 26, 26, 27, 27, 27]
        ),
        Set Display Width( 0 )
    ),
    New Column( "Y",
        Numeric,
        "Continuous",
        Format( "Best", 8 ),
        Set Values(
            [0.5, 0.6, 0.2, 0.8, 0.6, 0.6, 1.6, 1.1, 1, 0.4, 0.2, 0.1, 0.1, 0.5, 0, 0.3, 0.6,
            0.8, 0.1, 0.1, 0.2, 0.4, 0.9, 1.8, 0.1, 0.3, 0.4, 0.1, 0.3, 0.1, 0.9, 0.4, 0, 0.6,
            0.7, 0.7, 0.3, 0.1, 0.2, 0.3, 0.6, 0.2, 0.2, 0.4, 0.4, 0.8, 0.3, 0.3, 2.6, 0.4,
            1.6, 0.5, 0.3, 2.9, 0, 0, 0.5, 0.1, 0, 0.3, 0.5, 0, 0, 0.4, 0, 0.4, 0.3, 0.2, 0,
            0, 0.5, 0.1, 0.1, 0.2, 0.3, 1.1, 0.2, 0.1, 0.6, 0.3, 0.6]
        ),
        Set Display Width( 68 )
    )
);
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator, :Instrument ),
    Part( :Part ),
    Model( "Crossed then Nested (3 Factors Only)"n ),
    Dispersion Chart Type( Range ),
    Variance Components( 1 )
);
```

#### [Crossed then Nested Effects Model, Std Dev Chart](#crossed-then-nested-effects-model-std-dev-chart)[](#crossed-then-nested-effects-model-std-dev-chart "Click to copy url")

``` jsl
dt = New Table( "3 Factors Crossed then Nested",
    Add Rows( 81 ),
    New Column( "Operator",
        Character( 7 ),
        "Nominal",
        Set Values(
            {"Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara",
            "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara",
            "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Jane", "Jane",
            "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane",
            "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane",
            "Jane", "Jane", "Jane", "Jane", "Jane"}
        ),
        Set Display Width( 0 )
    ),
    New Column( "Instrument",
        Character( 1 ),
        "Nominal",
        Set Values(
            {"A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B",
            "B", "B", "C", "C", "C", "C", "C", "C", "C", "C", "C", "A", "A", "A", "A", "A",
            "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B", "B", "B", "C", "C", "C",
            "C", "C", "C", "C", "C", "C", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B",
            "B", "B", "B", "B", "B", "B", "B", "B", "C", "C", "C", "C", "C", "C", "C", "C",
            "C"}
        ),
        Set Display Width( 0 )
    ),
    New Column( "Part",
        Numeric,
        "Nominal",
        Format( "Best", 8 ),
        Set Values(
            [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9,
            10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16,
            16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23,
            23, 23, 24, 24, 24, 25, 25, 25, 26, 26, 26, 27, 27, 27]
        ),
        Set Display Width( 0 )
    ),
    New Column( "Y",
        Numeric,
        "Continuous",
        Format( "Best", 8 ),
        Set Values(
            [0.5, 0.6, 0.2, 0.8, 0.6, 0.6, 1.6, 1.1, 1, 0.4, 0.2, 0.1, 0.1, 0.5, 0, 0.3, 0.6,
            0.8, 0.1, 0.1, 0.2, 0.4, 0.9, 1.8, 0.1, 0.3, 0.4, 0.1, 0.3, 0.1, 0.9, 0.4, 0, 0.6,
            0.7, 0.7, 0.3, 0.1, 0.2, 0.3, 0.6, 0.2, 0.2, 0.4, 0.4, 0.8, 0.3, 0.3, 2.6, 0.4,
            1.6, 0.5, 0.3, 2.9, 0, 0, 0.5, 0.1, 0, 0.3, 0.5, 0, 0, 0.4, 0, 0.4, 0.3, 0.2, 0,
            0, 0.5, 0.1, 0.1, 0.2, 0.3, 1.1, 0.2, 0.1, 0.6, 0.3, 0.6]
        ),
        Set Display Width( 68 )
    )
);
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator, :Instrument ),
    Part( :Part ),
    Model( "Crossed then Nested (3 Factors Only)"n ),
    Dispersion Chart Type( "Standard Deviation" ),
    Variance Components( 1 )
);
```

#### [Crossed with Two Factor Interaction Effects Model, Range Chart](#crossed-with-two-factor-interaction-effects-model-range-chart)[](#crossed-with-two-factor-interaction-effects-model-range-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/3 Factors Crossed.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :new Y ),
    X( :Operator, :Instrument ),
    Part( :Part ),
    Model( "Crossed with Two Factor Interactions" ),
    Dispersion Chart Type( "Range" ),
    Variance Components( 1 )
);
```

#### [Crossed with Two Factor Interaction Effects Model, Std Dev Chart](#crossed-with-two-factor-interaction-effects-model-std-dev-chart)[](#crossed-with-two-factor-interaction-effects-model-std-dev-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/3 Factors Crossed.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :new Y ),
    X( :Operator, :Instrument ),
    Part( :Part ),
    Model( "Crossed with Two Factor Interactions" ),
    Dispersion Chart Type( "Standard Deviation" ),
    Variance Components( 1 )
);
```

#### [Main Effects Model, Range Chart](#main-effects-model-range-chart)[](#main-effects-model-range-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/Gasket.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator ),
    Part( :Part ),
    Model( "Main" ),
    Dispersion Chart Type( "Range" ),
    Variance Components( 1 )
);
```

#### [Main Effects Model, Std Dev Chart](#main-effects-model-std-dev-chart)[](#main-effects-model-std-dev-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/Gasket.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator ),
    Part( :Part ),
    Model( "Main" ),
    Dispersion Chart Type( "Standard Deviation" ),
    Variance Components( 1 )
);
```

#### [Nested Effects Model, Range Chart](#nested-effects-model-range-chart)[](#nested-effects-model-range-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/2 Factors Nested.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator ),
    Part( :Part ),
    Model( "Nested" ),
    Dispersion Chart Type( "Range" ),
    Variance Components( 1 )
);
```

#### [Nested Effects Model, Std Dev Chart](#nested-effects-model-std-dev-chart)[](#nested-effects-model-std-dev-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/2 Factors Nested.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator ),
    Part( :Part ),
    Model( "Nested" ),
    Dispersion Chart Type( "Standard Deviation" ),
    Variance Components( 1 )
);
```

#### [Nested then Crossed Effects Model, Range Chart](#nested-then-crossed-effects-model-range-chart)[](#nested-then-crossed-effects-model-range-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/3 Factors Nested & Crossed.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator, :Instrument ),
    Part( :Part ),
    Model( "Nested then Crossed (3 Factors Only)"n ),
    Dispersion Chart Type( "Range" ),
    Variance Components( 1 )
);
```

#### [Nested then Crossed Effects Model, Std Dev Chart](#nested-then-crossed-effects-model-std-dev-chart)[](#nested-then-crossed-effects-model-std-dev-chart "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/3 Factors Nested & Crossed.jmp" );
obj = dt << EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator, :Instrument ),
    Part( :Part ),
    Model( "Nested then Crossed (3 Factors Only)"n ),
    Dispersion Chart Type( "Standard Deviation" ),
    Variance Components( 1 )
);
```

### [EWMA Control Chart](#ewma-control-chart)[](#ewma-control-chart "Click to copy url")

**Syntax:** EWMA Control Chart( Y( column ), \<Subgroup( column )\>, \<By( column )\>, \<Center Data( 1 )\> )

**Description:** Creates a chart that plots the exponentially weighted moving averages and a chart that plots either the individual observations or the subgroup means. An EWMA chart is also known as a feedback control chart.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Clips1.jmp" );
obj = dt << EWMA Control Chart( Y( :Gap ) );
```

### [Explore Missing Values](#explore-missing-values)[](#explore-missing-values "Click to copy url")

**Syntax:** Explore Missing Values( Y( columns ) )

**Description:** Find patterns of missing values and conduct imputation.

``` jsl
dt = Open( "$Sample_Data/Cities.jmp" );
obj = dt << Explore Missing Values( Y( :OZONE, :CO, :SO2, :NO, :PM10 ) );
```

### [Explore Outliers](#explore-outliers)[](#explore-outliers "Click to copy url")

**Syntax:** Explore Outliers( Y( columns ) )

**Description:** Identifies, explores, and manages outliers in univariate or multivariate data.

``` jsl
dt = Open( "$SAMPLE_DATA/Water Treatment.jmp" );
obj = dt << Explore Outliers( Y( Column Group( "Sensor Measurements" ) ) );
```

### [Explore Patterns](#explore-patterns)[](#explore-patterns "Click to copy url")

**Syntax:** Explore Patterns( Y( columns ) )

**Description:** Searches for unusual features in the data, including long runs, duplicate long sequences, unusual formatted values, and runs of linear relationships.

``` jsl
dt = Open( "$SAMPLE_DATA/Nicardipine Lab Patterns.jmp" );
obj = dt << Explore Patterns( Y( Column Group( "Laboratory Results" ) ) );
```

### [Factor Analysis](#factor-analysis)[](#factor-analysis "Click to copy url")

**Syntax:** Factor Analysis( Y( columns ) )

**Description:** Uncovers the underlying structure of data by extracting unobserved variables, or factors, that represent the common variability across observed variables. Factor rotation is used to increase their interpretability.

``` jsl
dt = Open( "$SAMPLE_DATA/Socioeconomic.jmp" );
obj = dt << Factor Analysis(
    Y(
        :Total Population, :Median School Years, :Total Employment, :Professional Services,
        :Median House Value
    ),
    Variance Scaling( "Correlations" ),
    Fit( "ML", "SMC", 2, "Varimax" )
);
```

### [Fatigue Model](#fatigue-model)[](#fatigue-model "Click to copy url")

**Syntax:** Fatigue Model( N( column ), X( column ), \<Freq( column )\>, \<Censor( column ), Censor Code( value )\> )

**Description:** Analyzes fatigue data, also known as S-N curve modeling.

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Metal Wire Z.jmp" );
obj = dt << Fatigue Model(
    N( :Cycles ),
    S( :Stress ),
    Censor( :Censoring Indicator ),
    Censor Code( "Runout" )
);
```

### [Fit Curve](#fit-curve)[](#fit-curve "Click to copy url")

**Syntax:** Fit Curve( Y( column ), X( column ) )

**Description:** Fits a variety of built-in nonlinear models.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/Bioassay.jmp" );
obj = dt << Fit Curve( Y( :Toxicity ), X( :log Conc ), Group( :formulation ) );
obj << Fit Logistic 4P;
```

### [Fit Life by X](#fit-life-by-x)[](#fit-life-by-x "Click to copy url")

**Syntax:** Fit Life by X( Y( column ), X( column ), Relationship( string ), Distribution( string ), \<Censor( column )\> )

**Description:** Analyzes the distribution of time-to-event data parameterized by a single regression factor. Analysis options include accelerated failure models, life distributions across groups, and transformations of regression factors.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Devalt.jmp" );
obj = dt << Fit Life by X(
    Y( :Hours ),
    X( :Temp ),
    Distribution( Lognormal ),
    Censor( :Censor ),
    Freq( :Weight ),
    Relationship( Arrhenius Celsius )
);
```

### [Fit Parametric Survival](#fit-parametric-survival)[](#fit-parametric-survival "Click to copy url")

**Syntax:** Fit Model( Y( columns ), Effects( columns ), Personality( "Parametric Survival" ), Censor( columns ) )

**Description:** Fits a general linear regression model to survival times. These models can be used for survival times that can be expressed as a function of one or more explanatory variables. Takes into account various survival distributions and censoring.

``` jsl
dt = Open( "$SAMPLE_DATA/VA Lung Cancer.jmp" );
obj = dt << Fit Model(
    Y( :Time ),
    Effects( :Age, :Diag Time ),
    Personality( "Parametric Survival" ),
    Distribution( "Weibull" ),
    Censor( :censor ),
    Run Model
);
```

### [Fit Proportional Hazards](#fit-proportional-hazards)[](#fit-proportional-hazards "Click to copy url")

**Syntax:** Fit Model( Y( columns ), Effects( columns ), Personality( "Proportional Hazard" ), Censor( columns ) )

**Description:** Fits a semiparametric regression model (the Cox proportional hazards model) to assess the effect of explanatory variables on survival times while taking censoring into account.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Fit Model(
    Y( :days ),
    Effects( :Group ),
    Personality( "Proportional Hazard" ),
    Censor( :Censor ),
    Run Model
);
```

### [Formula Depot](#formula-depot)[](#formula-depot "Click to copy url")

**Syntax:** Formula Depot

**Description:** A container for prediction models that supports model comparison, profiling, and scoring code generation. The Formula Depot is launched through the analyze menu, Publish commands in modeling platforms, Recode, and the Formula Editor.

``` jsl

fd1 = Formula Depot();
dt = Open( "$SAMPLE_DATA\Iris.jmp" );
model = dt << RunScript( "Nominal Logistic" );
model << Publish Probability Formulas;
fd_script = fd1 << Get Script;
Save Text File( "$TEMP\fd.jrp", Char( Name Expr( fd_script ) ) );
fd1 << Close Window;
Open( "$TEMP\fd.jrp" );
fd2 = Formula Depot[1];
```

### [Functional Data Explorer](#functional-data-explorer)[](#functional-data-explorer "Click to copy url")

**Syntax:** Functional Data Explorer( Y(column), X(column), ID(column) )

**Description:** Fits functional models using a B-Spline, P-Spline, Fourier, or Wavelets basis model. A functional principal components analysis can be performed on the functional model to extract important features from the data. There is also an option to perform functional principal components analysis directly on the data, without fitting a basis function model first.

``` jsl
dt = Open( "$SAMPLE_DATA/Functional Data/Weekly Weather Data.jmp" );
obj = dt << Functional Data Explorer( Y( :TMAX ), X( :Week of Year ), ID( :NAME ) );
```

### [Gaussian Process](#gaussian-process)[](#gaussian-process "Click to copy url")

**Syntax:** Gaussian Process( Y( column ), X( columns ) )

**Description:** Models the relationship between a continuous response and one or more continuous predictors as a spline with interpolation.

``` jsl
dt = Open( "$SAMPLE_DATA/2D Gaussian Process Example.jmp" );
obj = dt << Gaussian Process( Y( :Y ), X( :X1, :X2 ) );
```

### [Graph Builder](#graph-builder)[](#graph-builder "Click to copy url")

**Syntax:** Graph Builder( Variables( X(column ), Y( column ), \<Group X( column )\>, \<Group Y( column )\>, \<Shape( column )\>, \<Color( column )\>, \<Overlay( column )\>, \<Freq( column )\> ), \<Elements(...)\> ) )

**Description:** Provides an interactive graphical interface that enables you to explore your data. You can drag columns into graph zones to create a variety of graphs including scatterplots, contour plots, bar charts, area charts, box plots, histograms, heat maps, pie charts, treemaps, mosaic plots, and maps.

#### [100% stacked bar chart](#100-stacked-bar-chart)[](#100-stacked-bar-chart "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// 100% stacked bar chart, custom legend colors
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Age ), Y( :Cholesterol ), Overlay( :Alcohol Use ) ),
    Elements(
        Bar( X, Y, Legend( 55 ), Bar Style( "Stacked" ), Summary Statistic( "% of Factor" ) )
    ),
    SendToReport(
        Dispatch( {}, "Cholesterol", ScaleBox, {Max( 1 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                55,
                Properties( 0, {Fill Color( RGB Color( 0.9, 0.9, 0.9 ) )} ),
                Properties( 1, {Fill Color( RGB Color( 1.0, 0.8, 0.8 ) )} ),
                Properties( 2, {Fill Color( RGB Color( 1.0, 0.6, 0.6 ) )} ),
                Properties( 3, {Fill Color( RGB Color( 1.0, 0.3, 0.3 ) )} )
            )}
        )
    )
);
```

#### [Arrow lines, one per row](#arrow-lines-one-per-row)[](#arrow-lines-one-per-row "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Cholesterol.jmp" );
// arrow lines, one per row
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :April AM ),
        X( :April PM, Position( 1 ) ),
        Y( :June AM ),
        Y( :June PM, Position( 1 ) ),
        Overlay( :treatment )
    ),
    Elements(
        Line(
            X( 1 ),
            X( 2 ),
            Y( 1 ),
            Y( 2 ),
            Legend( 8 ),
            Ordering( "Within Row" ),
            Connection( "Arrow" )
        )
    )
);
```

#### [Axis summary table](#axis-summary-table)[](#axis-summary-table "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// caption axis table
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :sex ), Y( :height ) ),
    Elements(
        Bar( X, Y, Legend( 4 ) ),
        Caption Box(
            X,
            Y,
            Legend( 5 ),
            Summary Statistic( "Mean" ),
            Summary Statistic 2( "N" ),
            Location( "Axis Table" )
        )
    )
);
```

#### [Bar chart and smooth trend line combination](#bar-chart-and-smooth-trend-line-combination)[](#bar-chart-and-smooth-trend-line-combination "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Spring.jmp" );
// bar chart and smooth trend line combination, left and right y axes
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :April ), Y( :Temp ), Y( :Precip, Position( 1 ), Side( "Right" ) ) ),
    Elements(
        Points( X, Y( 1 ), Legend( 12 ) ),
        Smoother( X, Y( 1 ), Legend( 13 ) ),
        Bar( X, Y( 2 ), Legend( 16 ) )
    ),
    SendToReport(
        Dispatch( {}, "Precip", ScaleBox,
            {Format( "Best", 12 ), Max( 5 ), Inc( 1 ), Minor Ticks( 1 )}
        )
    )
);
```

#### [Binomial proportion confidence interval](#binomial-proportion-confidence-interval)[](#binomial-proportion-confidence-interval "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Bands Data.jmp" );
// binomial proportion confidence interval
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Show Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables( X( :customer ), Y( :Banding? ) ),
    Elements(
        Points( X, Y, Legend( 3 ) ),
        Line Of Fit( X, Y, Legend( 4 ), Means and Std Devs( 1 ) )
    ),
    Local Data Filter(
        Add Filter(
            columns( :customer ),
            Where( :customer == {"MODMAT", "REI", "ROSES", "SHEPLERS", "TARGET"} )
        )
    ),
    SendToReport(
        Dispatch( {}, "Banding?", ScaleBox,
            {Min( -0.07 ), Max( 1.07 ), Label Row( Show Major Grid( 1 ) )}
        )
    )
);
```

#### [Bubble chart with overlaid curves](#bubble-chart-with-overlaid-curves)[](#bubble-chart-with-overlaid-curves "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/SATByYear.jmp" );
// Smooth trend line, variable dot size, overlaid y variables, bubble chart. data filter
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :"% Taking (2004)"n ),
        Y( :SAT Verbal ),
        Y( :SAT Math, Position( 1 ) ),
        Size( :Population )
    ),
    Elements(
        Points( X, Y( 1 ), Y( 2 ), Legend( 7 ) ),
        Smoother( X, Y( 1 ), Y( 2 ), Legend( 8 ), Lambda( 0.45 ) )
    ),
    Local Data Filter( Add Filter( columns( :Year ), Where( :Year == 2004 ) ) ),
    SendToReport(
        Dispatch( {}, "% Taking (2004)", ScaleBox, {Format( "Percent", 12, 0 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 7, Properties( 0, {Marker Size( 6 )} ) )}
        )
    )
);
```

#### [Connected lines with overlaid dots](#connected-lines-with-overlaid-dots)[](#connected-lines-with-overlaid-dots "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Time Series/M3C Quarterly Wide Format.jmp" );
// connected lines with overlaid dots, custom markers, nested date axis
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Time ), Y( :N 646 ), Y( :N 647, Position( 1 ) ) ),
    Elements(
        Line( X, Y( 1 ), Y( 2 ), Legend( 10 ) ),
        Points( X, Y( 1 ), Y( 2 ), Legend( 11 ) )
    ),
    SendToReport(
        Dispatch( {}, "Time", ScaleBox,
            {Min( 2515958948 ), Max( 2872394250 ), Interval( "Quarter" ), Inc( 1 ),
            Minor Ticks( 0 ), Label Row Nesting( 2 ), Label Row( 1, Set Font Size( 12 ) )}
        ),
        Dispatch( {}, "N 646", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                10,
                Properties( 0, {Line Label Properties( {Last Label( 1 )} )} ),
                Properties( 1, {Line Label Properties( {Last Label( 1 )} )} )
            ), Legend Model(
                11,
                Base( 0, 0, 0, Item ID( "N 646", 1 ) ),
                Base( 1, 0, 1, Item ID( "N 647", 1 ) ),
                Properties( 0, {Marker( "FilledCircle" )} ),
                Properties( 1, {Marker( "Filled Up Triangle" )} )
            )}
        ),
        Dispatch( {}, "Graph Builder", FrameBox,
            {DispatchSeg(
                Line Seg( "Line (N 646)" ),
                Label Offset( "Last", 45, {2843799627.0183, 6317.56810988166} )
            ), DispatchSeg(
                Line Seg( "Line (N 647)" ),
                Label Offset( "Last", 45, {2857099451.70628, 4518.71614237549} )
            )}
        )
    )
);
```

#### [Contour plot and scatter plot points](#contour-plot-and-scatter-plot-points)[](#contour-plot-and-scatter-plot-points "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
// contour plot and scatter plot points, smoothing, alpha shapes for non-convex hull
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Labor ), Y( :Capital ), Color( :Difference ) ),
    Elements(
        Contour(
            X,
            Y,
            Legend( 9 ),
            Boundary( 0 ),
            Number of Levels( 7 ),
            Alpha( 5 ),
            Smoothness( 0.2 )
        ),
        Points( X, Y, Color( 0 ), Legend( 10 ) )
    )
);
```

#### [Coplot-style trellis grouping](#coplot-style-trellis-grouping)[](#coplot-style-trellis-grouping "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Design Experiment/Algorithm Data.jmp" );
// coplot style grouping using continuous grouping variables, smoother and scatter plot
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Alpha, Levels( 2 ) ),
        Y( :CPU Time ),
        Group X( :Beta, Levels( 2 ) ),
        Group Y( :Gamma, Levels( 2 ) ),
        Overlay( :Algorithm )
    ),
    Elements( Points( X, Y, Legend( 29 ) ), Smoother( X, Y, Legend( 30 ), Lambda( 0.25 ) ) )
);
```

#### [Independent charts using BY variable](#independent-charts-using-by-variable)[](#independent-charts-using-by-variable "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Financial.jmp" );
// by variable creates multiple Graph Builder instances
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :"Assets($Mil.)"n ), Y( :"Stockholder's Eq($Mil.)"n ), ),
    Elements( Points( X, Y, Legend( 17 ) ), Smoother( X, Y, Legend( 18 ) ) ),
    By( :Type )
);
```

#### [Left and right y axes](#left-and-right-y-axes)[](#left-and-right-y-axes "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Functional Data/Fermentation Process.jmp" );
// left and right y axes sharing a graph, overlaid lines
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Time ), Y( :pH ), Y( :Tank Level, Position( 1 ), Side( "Right" ) ) ),
    Elements( Line( X, Y( 1 ), Legend( 41 ) ), Line( X, Y( 2 ), Legend( 46 ) ) ),
    SendToReport( Dispatch( {}, "Time", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ) )
);
```

#### [Line with custom band interval](#line-with-custom-band-interval)[](#line-with-custom-band-interval "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// range area, custom interval, overlaid line, transparency
Graph Builder(
    Transform Column(
        "Quantile...=0.75[height][age]",
        Formula( Col Quantile( :height, 0.75, :age, :"@Exclude"n, :"@Filter"n ) )
    ),
    Transform Column(
        "Quantile...=0.25[height][age]",
        Formula( Col Quantile( :height, 0.25, :age, :"@Exclude"n, :"@Filter"n ) )
    ),
    Show Control Panel( 0 ),
    Variables(
        X( :age ),
        Y( :height ),
        Y( :"Quantile...=0.25[height][age]"n, Position( 1 ) ),
        Y( :"Quantile...=0.75[height][age]"n, Position( 1 ) )
    ),
    Elements(
        Area( X, Y( 2 ), Y( 3 ), Legend( 5 ), Area Style( "Range" ) ),
        Line( X, Y( 1 ), Legend( 6 ) )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                5,
                Level Name( 0, "IQR" ),
                Properties( 0, {Transparency( 0.33 )} )
            )}
        ),
        Dispatch( {}, "400", LegendBox, {Set Title( "" )} )
    )
);
```

#### [Linear regression panels](#linear-regression-panels)[](#linear-regression-panels "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Financial.jmp" );
// line of fit, regression, small multiples, custom group color, custom graph spacing
Graph Builder(
    Show Control Panel( 0 ),
    Grid Color( "Medium Light Gray" ),
    Grid Transparency( 0.25 ),
    Title Fill Color( "Medium Light Gray" ),
    Title Frame Color( "Medium Light Gray" ),
    Level Fill Color( {217, 217, 217} ),
    Level Frame Color( "Medium Light Gray" ),
    Level Spacing Color( "Medium Light Gray" ),
    Graph Spacing( 10 ),
    Variables( X( :"Assets($Mil.)"n ), Y( :"Stockholder's Eq($Mil.)"n ), Wrap( :Type ) ),
    Elements( Points( X, Y, Legend( 17 ) ), Line Of Fit( X, Y, Legend( 19 ) ) ),
    Local Data Filter(
        Add Filter( columns( :"Assets($Mil.)"n ), Where( :"Assets($Mil.)"n <= 60941 ) )
    )
);
```

#### [Mediterranean equal-area choropleth](#mediterranean-equal-area-choropleth)[](#mediterranean-equal-area-choropleth "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/World Demographics.jmp" );
// Mediterranean map, choropleth, equal area projection, grid lines
Graph Builder(
    Size( 1094, 586 ),
    Show Control Panel( 0 ),
    Variables( Color( :Total Median Age ), Shape( :Territory ) ),
    Elements( Map Shapes( Legend( 3 ) ) ),
    SendToReport(
        Dispatch( {}, "", ScaleBox,
            {Format( "Longitude DDD", "PUNDIR", 16 ), Min( -14.2917884823647 ),
            Max( 64.9684846475565 ), Inc( 20 ), Minor Ticks( 1 ),
            Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "", ScaleBox( 2 ),
            {Format( "Latitude DDD", "PUNDIR", 16 ), Min( 21.8020806509188 ),
            Max( 61.3932495299748 ), Inc( 10 ), Minor Ticks( 1 ),
            Label Row( Show Major Grid( 1 ) )}
        )
    )
);
```

#### [Multiple x axes](#multiple-x-axes)[](#multiple-x-axes "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Design Experiment/Algorithm Data.jmp" );
// mutiple x variables in separate panels, smoother with confidence intervals and scatter plot
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Alpha ), X( :Beta ), X( :Gamma ), Y( :CPU Time ), Overlay( :Algorithm ) ),
    Elements(
        Position( 1, 1 ),
        Points( X, Y, Legend( 39 ) ),
        Smoother( X, Y, Legend( 40 ), Lambda( 1.5 ), Confidence of Fit( 1 ) )
    ),
    Elements(
        Position( 2, 1 ),
        Points( X, Y, Legend( 41 ) ),
        Smoother( X, Y, Legend( 42 ), Lambda( 1.5 ), Confidence of Fit( 1 ) )
    ),
    Elements(
        Position( 3, 1 ),
        Points( X, Y, Legend( 43 ) ),
        Smoother( X, Y, Legend( 44 ), Lambda( 1.5 ), Confidence of Fit( 1 ) )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 40, Properties( 2, {Line Color( RGB Color( 0.4, 0.4, 0.4 ) )} ) )}
        )
    )
);
```

#### [Napoleon's March flow diagram](#napoleons-march-flow-diagram)[](#napoleons-march-flow-diagram "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Napoleons March.jmp" );
// flow diagram
Graph Builder(
    Show Control Panel( 0 ),
    Show X Axis( 0 ),
    Show Y Axis( 0 ),
    Show X Axis Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables(
        X( :Longitude ),
        Y( :Latitude ),
        Overlay( :Group ),
        Color( :Direction ),
        Size( :Army Size )
    ),
    Elements(
        Line( X, Y, Legend( 3 ), Ordering( "Row Order" ), Missing Values( "No Connection" ) )
    ),
    SendToReport(
        Dispatch( {}, "Longitude", ScaleBox,
            {Min( 26.71 ), Max( 34.9 ), Inc( 2.5 ), Minor Ticks( 0 ),
            Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "Latitude", ScaleBox,
            {Min( 53.32 ), Max( 56.61 ), Inc( 0.5 ), Minor Ticks( 1 ),
            Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                3,
                Properties( 0, {Line Width( 10 )} ),
                Properties( 1, {RGB Color( 1, 0.69, 0.49 )} ),
                Properties( 2, {RGB Color( 0.47, 0.47, 0.47 )} )
            )}
        ),
        Dispatch( {}, "graph title", TextEditBox,
            {Set Text( "Napoleon's March to Moscow" )}
        ),
        Dispatch( {}, "Graph Builder", FrameBox,
            {Background Map( Images( "Detailed Earth", Transparency( 0.75 ) ) )}
        )
    )
);
```

#### [Overlaid bivariate kernel density contours](#overlaid-bivariate-kernel-density-contours)[](#overlaid-bivariate-kernel-density-contours "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// overlaid bivariate kernel density contour
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Culmen Depth ), Y( :Culmen Length ), Overlay( :Species ) ),
    Elements(
        Contour( X, Y, Legend( 6 ), Line( 1 ), Number of Levels( 5 ), Smoothness( 0.2174 ) )
    )
);
```

#### [Overlaid empirical cumulative distribution function curves](#overlaid-empirical-cumulative-distribution-function-curves)[](#overlaid-empirical-cumulative-distribution-function-curves "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// CDF, empirical cumulative distribution function
Graph Builder(
    Transform Column(
        "Rank[Culmen Length]@Overlay",
        Formula(
            Col Rank( :Culmen Length, :"@Exclude"n, :"@Filter"n, :"@Graph"n, :"@Overlay"n )
             / Col Number(
                :Culmen Length,
                :"@Exclude"n,
                :"@Filter"n,
                :"@Graph"n,
                :"@Overlay"n
            )
        )
    ),
    Show Control Panel( 0 ),
    Legend Position( "Inside Bottom Right" ),
    Show Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables(
        X( :Culmen Length ),
        Y( :"Rank[Culmen Length]@Overlay"n ),
        Overlay( :Species )
    ),
    Elements( Line( X, Y, Legend( 15 ), Connection( "Step" ) ) ),
    SendToReport(
        Dispatch( {}, "Rank[Culmen Length]@Overlay", ScaleBox, {Max( 1.0117745954803 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                15,
                Level Name( 0, "Adelie" ),
                Level Name( 1, "Chinstrap" ),
                Level Name( 2, "Gentoo" )
            )}
        )
    )
);
```

#### [Panels with unaligned y axes](#panels-with-unaligned-y-axes)[](#panels-with-unaligned-y-axes "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/US Regional Population.jmp" );
// panels with unaligned y axes
Graph Builder(
    Transform Column( "Transform[Year]", Continuous, Formula( Num( :Year ) ) ),
    Show Control Panel( 0 ),
    Extend Axis to Zero( 10 ),
    Link Page Axes( "X Only" ),
    Replicate Linked Page Axes( 0 ),
    Variables(
        X( :"Transform[Year]"n ),
        Y( :Population ),
        Page( :Region, Levels per Row( 3 ) )
    ),
    Elements( Points( X, Y, Legend( 3 ) ), Smoother( X, Y, Legend( 4 ) ) ),
    Local Data Filter(
        Add Filter(
            columns( :Region ),
            Where(
                :Region == {"AR,LA,OK,TX", "Great Lakes", "KY,TN,AL,MS", "Midwest",
                "Mountain", "New England", "NY,NJ,PA", "Pacific", "South Atlantic"}
            )
        )
    ),
    SendToReport(
        Dispatch( {}, "Population", ScaleBox, {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 2 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 3 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 4 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 5 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 6 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 7 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 8 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 9 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 10 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Transform[Year]", TextEditBox, {Set Text( "Year" )} ),
        Dispatch( {}, "Transform[Year]", Text Edit Box( 2 ), {Set Text( "Year" )} ),
        Dispatch( {}, "Transform[Year]", Text Edit Box( 3 ), {Set Text( "Year" )} )
    )
);
```

#### [Parallel y axes, overlaid lines](#parallel-y-axes-overlaid-lines)[](#parallel-y-axes-overlaid-lines "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Functional Data/Fermentation Process.jmp" );
// parallel y axes, multiple y scales sharing a graph, overlaid lines
Graph Builder(
    Show Control Panel( 0 ),
    Parallel Axes( "Y Only" ),
    Variables(
        X( :Time ),
        Y( :Temp ),
        Y( :NH3 Feed ),
        Y( :Air ),
        Y( :Tank Level ),
        Y( :pH )
    ),
    Elements( Position( 1, 1 ), Line( X, Y, Legend( 37 ) ) ),
    Elements( Position( 1, 2 ), Line( X, Y, Legend( 39 ) ) ),
    Elements( Position( 1, 3 ), Line( X, Y, Legend( 40 ) ) ),
    Elements( Position( 1, 4 ), Line( X, Y, Legend( 41 ) ) ),
    Elements( Position( 1, 5 ), Line( X, Y, Legend( 42 ) ) ),
    SendToReport( Dispatch( {}, "Time", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ) )
);
```

#### [Points and smoother](#points-and-smoother)[](#points-and-smoother "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
```

#### [Scatter plot with marginal box plots](#scatter-plot-with-marginal-box-plots)[](#scatter-plot-with-marginal-box-plots "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// scatter plot with marginal box plots, custom graph sizes
Graph Builder(
    Transform Column( "dummy1", Nominal, Formula( 1 ) ),
    Transform Column( "dummy2", Nominal, Formula( 1 ) ),
    Show Control Panel( 0 ),
    Variables(
        X( :Delta 13 C ),
        X( :dummy1 ),
        Y( :dummy2 ),
        Y( :Delta 15 N ),
        Color( :Sex ),
        Size( :Body Mass )
    ),
    Relative Sizes( "X", [100 10] ),
    Relative Sizes( "Y", [10 100] ),
    Elements( Position( 1, 1 ), Box Plot( X, Y, Color( 0 ), Size( 0 ), Legend( 12 ) ) ),
    Elements( Position( 1, 2 ), Points( X, Y, Legend( 4 ) ) ),
    Elements( Position( 2, 1 ) ),
    Elements( Position( 2, 2 ), Box Plot( X, Y, Color( 0 ), Size( 0 ), Legend( 13 ) ) ),
    SendToReport(
        Dispatch( {}, "dummy1", ScaleBox, {Label Row( Show Major Labels( 0 ) )} ),
        Dispatch( {}, "dummy2", ScaleBox, {Label Row( Show Major Labels( 0 ) )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                4,
                Properties( 1, {Transparency( 0.75 )} ),
                Properties( 2, {Transparency( 0.75 )} )
            )}
        ),
        Dispatch( {}, "dummy1", TextEditBox, {Set Text( "" )} ),
        Dispatch( {}, "dummy2", TextEditBox, {Set Text( "" )} ),
        Dispatch( {}, "400", LegendBox,
            {Legend Position( {12, [1, -3], 4, [0, 3, 4], 13, [2, -3]} )}
        )
    )
);
```

#### [Variability chart](#variability-chart)[](#variability-chart "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Variability Data/2 Factors Nested.jmp" );
// variability chart, mean and range interval, nested axis
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Operator ), X( :Part, Position( 1 ) ), Y( :Y ) ),
    Elements(
        Points(
            X( 1 ),
            X( 2 ),
            Y,
            Legend( 3 ),
            Summary Statistic( "Mean" ),
            Error Interval( "Range" )
        )
    ),
    SendToReport(
        Dispatch( {}, "Operator", ScaleBox, {Label Row( 2, Show Major Grid( 1 ) )} )
    )
);
```

#### [Violin plots with quartiles](#violin-plots-with-quartiles)[](#violin-plots-with-quartiles "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// violin plots, overlaid median line and quartile intervals
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ) ),
    Elements(
        Contour( X, Y, Legend( 3 ) ),
        Bar(
            X,
            Y,
            Legend( 4 ),
            Bar Style( "Float" ),
            Summary Statistic( "Median" ),
            Error Interval( "Interquartile Range" )
        )
    )
);
```

#### [Wafer map](#wafer-map)[](#wafer-map "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Wafer Stacked.jmp" );
// wafer map, heat map, trellis, wrap arrangement
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :X_Die ), Y( :Y_Die ), Wrap( :Wafer ), Color( :Defects ) ),
    Elements( Heatmap( X, Y, Legend( 8 ) ) ),
    SendToReport(
        Dispatch( {}, "X_Die", ScaleBox, {Minor Ticks( 9 )} ),
        Dispatch( {}, "Y_Die", ScaleBox, {Minor Ticks( 9 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                8,
                Properties( 0, {gradient( {Color Theme( "White to Orange" )} )} )
            )}
        )
    )
);
```

### [Hierarchical Cluster](#hierarchical-cluster)[](#hierarchical-cluster "Click to copy url")

**Syntax:** Hierarchical Cluster( Y( columns ) )

**Description:** Clusters rows based on continuous or categorical variables. Hierarchical clustering begins by treating each row as its own cluster, then successively combining two clusters at a time.

``` jsl
dt = Open( "$SAMPLE_DATA/Birth Death Subset.jmp" );
obj = dt << Hierarchical Cluster( Y( :birth, :death ), Label( :country ) );
```

### [Item Analysis](#item-analysis)[](#item-analysis "Click to copy url")

**Syntax:** Item Analysis( Y( columns ) )

**Description:** Relates a trait or ability to an individual's probability of endorsing or correctly responding to an item.

``` jsl
dt = Open( "$SAMPLE_DATA/MathScienceTest.jmp" );
obj = Item Analysis( Y( :Q1, :Q2, :Q3, :Q4, :Q5, :Q6, :Q7, :Q8, :Q9 ) );
```

### [K Means Cluster](#k-means-cluster)[](#k-means-cluster "Click to copy url")

**Syntax:** K Means Cluster( Y( column(s) ), Number of Clusters( number ) )

**Description:** Clusters rows based on numeric variables in data tables with up to millions of rows. You must specify the number of clusters in advance.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << K Means Cluster(
    Y( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    Number of Clusters( 3 )
);
obj << Go;
```

### [K Nearest Neighbors](#k-nearest-neighbors)[](#k-nearest-neighbors "Click to copy url")

**Syntax:** K Nearest Neighbors(Y( column ), X( columns ))

**Description:** Predicts a continuous or categorical response based on the responses of the k nearest neighbors in the space of the X variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = K Nearest Neighbors(
    Y( :Species ),
    X( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    K( 10 )
);
```

### [Latent Class Analysis](#latent-class-analysis)[](#latent-class-analysis "Click to copy url")

**Syntax:** Latent Class Analysis( Y( column(s) ), Number of Clusters( number ) )

**Description:** Clusters rows based on categorical variables using multinomial mixtures. You must specify the number of latent classes (clusters) in advance.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Latent Class Analysis(
    Y( :sex, :marital status, :country, :size, :type ),
    Number of Clusters( 3 )
);
```

### [Life Distribution](#life-distribution)[](#life-distribution "Click to copy url")

**Syntax:** Life Distribution( Y( column(s) ) )

**Description:** Analyzes the distribution of time-to-event data. Can be used for modeling censored data, product lifetime, reliability, and competing causes.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
obj = dt << Life Distribution( Y( :Time ), Censor( :Censor ) );
```

### [Logistic](#logistic)[](#logistic "Click to copy url")

**Syntax:** Logistic( Y( columns ), X( columns ) )

**Description:** Models a categorical response with respect to a continuous variable. Analysis methods include logistic regression and ROC curves.

``` jsl
dt = Open( "$SAMPLE_DATA/Penicillin.jmp" );
obj = dt << Logistic( Y( :Response ), X( :"ln(dose)"n ), Freq( :Count ) );
```

### [Make Validation Column](#make-validation-column)[](#make-validation-column "Click to copy url")

**Syntax:** Make Validation Column( \<Stratification Columns(columns)\>, \<Grouping Columns(columns)\>, \<Cutpoint Column(column)\>, \<Cutpoint Batch ID(column)\> )

**Description:** Makes a column used to divide the data into training, validation, and test sets.

**Cutpoint Example**

``` jsl
dt = Open( "$SAMPLE_DATA/Functional Data/Weekly Weather Data.jmp" );
dt << Make Validation Column(
    Cutpoint Column( :Week of Year ),
    Cutpoint Batch ID( :ID ),
    Training Set( 0.60 ),
    Validation Set( 0.25 ),
    Test Set( 0.15 ),
    New Column Name( "Cutpoint Batch Validation" ),
    Go
);
```

**Stratification Example**

``` jsl
dt = Open( "$SAMPLE_DATA/Lipid Data.jmp" );
dt << Make Validation Column(
    Stratification Columns( :Sex ),
    Training Set( 0.50 ),
    Validation Set( 0.25 ),
    Test Set( 0.25 ),
    New Column Name( "Valid1" ),
    Random Seed( 1234 ),
    Go
);
```

### [Manage Limits](#manage-limits)[](#manage-limits "Click to copy url")

**Syntax:** Manage Limits( Process Variables( columns ) )

**Description:** Launches utility for managing quality limits for multiple columns at once. You can add, edit, and save limits to column properties.

``` jsl
dt = Open( "$SAMPLE_DATA/Semiconductor Capability.jmp" );
obj = dt << Manage Limits( Process Variables( dt << Get Column Group( "Processes" ) ) );
```

### [Marker Admixture](#marker-admixture)[](#marker-admixture "Click to copy url")

**Syntax:** Marker Admixture( Marker( columns ) )

**Description:** Estimates population admixture for individuals based on marker genotypes.

**JMP Version Added:** 19

**Example 1**

``` jsl

dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );
dt << Marker Admixture( Marker( Column Group( "Markers" ) ), Set(), Fit() );
```

**Example 2**

``` jsl

dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );
dt << Marker Admixture(
    Marker( Column Group( "Markers" ) ),
    Set(
        Missing Marker Imputation Method( "Specified" ),
        Estimation Method( "Fixed Parameter" ),
        Unthreaded( 1 ),
        Imputation Value( 1 ),
        Number of Ancestral Populations( 3 )
    ),
    Fit(
        Missing Marker Imputation Method( "Specified" ),
        Estimation Method( "Fixed Parameter" ),
        Unthreaded( 1 ),
        Imputation Value( 1 ),
        Number of Ancestral Populations( 3 )
    )
);
```

### [Marker Imputation](#marker-imputation)[](#marker-imputation "Click to copy url")

**Syntax:** Marker Imputation( Marker( columns ) )

**Description:** Imputes numeric missing marker genotypes.

**JMP Version Added:** 19

**Example 1**

``` jsl

dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );

//Set missing values for some markers
dt = Current Data Table();
Random Reset( 1234 );
markers = dt << Get Column Group( "Markers" );
markers = markers[Random Index( N Items( markers ), 15 )];
For Each( {col}, markers, col[Random Index( N Rows( dt ), Random Integer( 1, 20 ) )] = . );

//Run platform
dt << Marker Imputation(
    Marker( Column Group( "Markers" ) ),
    Ploidy( 2 ),
    Missing Marker Imputation Method( "LD-kNN" )
);
```

**Example 2**

``` jsl

dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );

//Set missing values for some markers
dt = Current Data Table();
Random Reset( 1234 );
markers = dt << Get Column Group( "Markers" );
markers = markers[Random Index( N Items( markers ), 15 )];
For Each( {col}, markers, col[Random Index( N Rows( dt ), Random Integer( 1, 20 ) )] = . );

//Run platform
obj = dt << Marker Imputation(
    Marker( Column Group( "Markers" ) ),
    Ploidy( 2 ),
    Set Random Seed( 0 ),
    Method( "Specified" ),
    Imputation Value( 1 )
);
```

### [Marker Relatedness](#marker-relatedness)[](#marker-relatedness "Click to copy url")

**Syntax:** Marker Relatedness( Marker( columns ) )

**Description:** Estimates several types of genomic relationship measures between pairs of individuals based genetic markers in both diploid and polyploid organisms.

**JMP Version Added:** 18

**Example 1**

``` jsl

dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );

//Run platform
dt << Marker Relatedness(
    Marker( Column Group( "Markers" ) ),
    Ploidy( 2 ),
    Set Random Seed( 12345 ),
    Missing Marker Imputation Method( "HWE Off" ),
    Kinship Type( "Identical by State" )
);
```

**Example 2**

``` jsl

dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );

//Run platform
obj = dt << Marker Relatedness(
    Marker( Column Group( "Markers" ) ),
    Ploidy( 2 ),
    Set Random Seed( 12345 ),
    Missing Marker Imputation Method( "HWE On" ),
    Kinship Type( "Identical by State" )
);
```

### [Marker Simulation](#marker-simulation)[](#marker-simulation "Click to copy url")

**Syntax:** Marker Simulation( Marker( columns ), Predictor Formula( columns ) )

**Description:** Simulates marker genotypes from parental crosses and computes related measures of breeding performance.

**JMP Version Added:** 17

**Example 1**

``` jsl

dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );

//Hide and Exclude Rows
dt << Clear Select << Clear Row States;
dt << Select Where( :Father == 0 & :Mother == 0 & Row() <= 100 );
dt << Invert Row Selection << Exclude;
dt << Clear Select;

//Run platform
dt << Marker Simulation(
    Marker( Column Group( "Markers" ) ),
    Predictor Formula(
        :Pred Formula Trait1, :Pred Formula Trait2, :Pred Formula Trait3,
        :Pred Formula Trait4, :"Probability( Disease Status=1 )"n
    ),
    Cross( :Sex ),
    Ploidy( 2 ),
    Number of Generations( 2 ),
    Number of Individuals per Cross( 10 ),
    Set Random Seed( 12345 ),
    Threshold to Make Line Plots( 1000 )
);
```

**Example 2**

``` jsl

dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );

//Hide and Exclude Rows
dt << Clear Select << Clear Row States;
dt << Select Where( :Father == 0 & :Mother == 0 & Row() <= 100 );
dt << Invert Row Selection << Exclude;
dt << Clear Select;

//Run platform
obj = dt << Marker Simulation(
    Marker( Column Group( "Markers" ) ),
    Predictor Formula(
        :Pred Formula Trait1, :Pred Formula Trait2, :Pred Formula Trait3,
        :Pred Formula Trait4, :"Probability( Disease Status=1 )"n
    ),
    Cross( :Sex ),
    Unthreaded( 1 ),
    Ploidy( 2 ),
    Number of Generations( 2 ),
    Number of Individuals per Cross( 10 ),
    Set Random Seed( 12345 ),
    Threshold to Make Line Plots( 1000 )
);
```

### [Marker Statistics](#marker-statistics)[](#marker-statistics "Click to copy url")

**Syntax:** Marker Statistics( Marker( columns ), With Marker( columns ) )

**Description:** Performs analysis on genetic marker data to compute measures such as minor allele frequency, Hardy-Weinberg equilibrium, and linkage disequilibrium.

**JMP Version Added:** 17

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );
dt << Marker Statistics( Marker( Column Group( "Markers" ) ), Ploidy( 2 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Life Sciences/Genotypes Pedigree.jmp" );
obj = dt << Marker Statistics(
    Marker( Column Group( "Markers" ) ),
    With Marker( Column Group( "Markers" ) ),
    Ploidy( 2 )
);
```

### [Matched Pairs](#matched-pairs)[](#matched-pairs "Click to copy url")

**Syntax:** Matched Pairs( Y( columns ), X( column ) )

**Description:** Compares the means of matched sets of variables using paired t tests or simple repeated measures analysis to account for correlation between responses.

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
obj = dt << Matched Pairs( X( :Dose ), Y( :BP 8M, :BP 8W ) );
```

### [MaxDiff](#maxdiff)[](#maxdiff "Click to copy url")

**Syntax:** MaxDiff( Profile DataTable( data table ), Profile ID( column ), Profile Effects( column(s) ), \<Response Data Table( data table )\>, \<Subject Data Table( data table )\>, \<Response Profile ID Chosen( column )\>, \<Response Subject ID( column)\>, \<Response Grouping( column(s) )\>, \<Response Profile ID Choices( column(s) )\>, \<Profile Grouping( column(s) )\>, \<Subject Subject ID( column )\>, \<Subject Effects( column(s) )\> )

**Description:** Creates a design to find the combination of product attributes that customers most prefer and least prefer.

``` jsl
dt = Open( "$SAMPLE_DATA/Potato Chip Combined.jmp" );
obj = dt << MaxDiff(
    One Table( 1 ),
    Subject ID( :Respondent ),
    Choice Set ID( :Choice Set ID ),
    Profile ID( :Response ),
    Profile Grouping( :Survey ID ),
    Profile Effects( :Profile ID ),
    Response Value Indicates Best( 1 ),
    Response Value Indicates Worst( -1 )
);
```

### [Mixture Profiler](#mixture-profiler)[](#mixture-profiler "Click to copy url")

**Syntax:** Mixture Profiler( Y( column1, column2, ... ) )

**Description:** Produces an interactive ternary plot that enables you to explore the contours of the saved prediction formulas for mixture models with three or more factors.

``` jsl
dt = Open( "$SAMPLE_DATA/Plasticizer.jmp" );
obj = dt << Mixture Profiler( Y( :Pred Formula Y ) );
```

### [Model Comparison](#model-comparison)[](#model-comparison "Click to copy url")

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

### [Model Driven Multivariate Control Chart](#model-driven-multivariate-control-chart)[](#model-driven-multivariate-control-chart "Click to copy url")

**Syntax:** Model Driven Multivariate Control Chart( Process( columns ) )

**Description:** Creates multivariate control charts based on principal components or partial least squares methods.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Flight Delays.jmp" );
obj = dt << Model Driven Multivariate Control Chart(
    Process( :AA, :CO, :DL, :F9, :FL, :NW, :UA, :US, :WN )
);
```

### [Model Screening](#model-screening)[](#model-screening "Click to copy url")

**Syntax:** Model Screening( Y( column ), X( columns ) )

**Description:** Fits many different predictive models, so that you can select the best.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
```

### [Multidimensional Scaling](#multidimensional-scaling)[](#multidimensional-scaling "Click to copy url")

**Syntax:** Multidimensional Scaling( Y( columns ) )

**Description:** Creates a visual representation of the pattern of proximities among a set of objects.

``` jsl
dt = Open( "$SAMPLE_DATA/Flight Distances.jmp" );
obj = dt << Multidimensional Scaling(
    Y(
        :Birmingham, :Boston, :Buffalo, :Chicago, :Cleveland, :Dallas, :Denver, :Detroit,
        :El Paso, :Houston, :Indianapolis, :Kansas City, :Los Angeles, :Louisville, :Memphis,
        :Miami, :Minneapolis, :New Orleans, :New York, :Omaha, :Philadelphia, :Phoenix,
        :Pittsburgh, :St. Louis, :Salt Lake City, :San Francisco, :Seattle, :Washington DC
    )
);
```

### [Multiple Correspondence Analysis](#multiple-correspondence-analysis)[](#multiple-correspondence-analysis "Click to copy url")

**Syntax:** Multiple Correspondence Analysis( Y( columns ), X( columns ) )

**Description:** Identifies associations between the levels of categorical variables. Multiple Correspondence Analysis is analogous to principal components analysis for categorical data.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Cereal.jmp" );
dt << Multiple Correspondence Analysis(
    Y( :Mfr, :"Hot/Cold"n, :Fiber Gr ),
    X( :Manufacturer )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Multiple Correspondence Analysis( Y( :country, :size, :type ) );
```

### [Multiple Factor Analysis](#multiple-factor-analysis)[](#multiple-factor-analysis "Click to copy url")

**Syntax:** Multiple Factor Analysis( MFABLocks({"Block 1", columns},{"Block 2", columns}) )

**Description:** Analyzes agreement among panelists in sensory data analysis.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
```

### [Multivariate](#multivariate)[](#multivariate "Click to copy url")

**Syntax:** Multivariate( Y( columns ) )

**Description:** Explores correlation and associations among numeric variables using a variety of multivariate analysis techniques. These techniques include both parametric and nonparametric measures of association, scatterplot matrices, principal components analysis, outlier analysis, and item reliability.

``` jsl
dt = Open( "$SAMPLE_DATA/Solubility.jmp" );
obj = Multivariate( Y( :Ether, :Chloroform, :Benzene, :Carbon Tetrachloride, :Hexane ) );
```

### [Multivariate Embedding](#multivariate-embedding)[](#multivariate-embedding "Click to copy url")

**Syntax:** Multivariate Embedding( Y( columns ) )

**Description:** Maps data from very high-dimensional spaces to a low-dimensional space, using the Uniform Manifold Approximation and Projection (UMAP) method or the t-Distributed Stochastic Neighbor Embedding (t-SNE) method. Many times, you want to map the data to either two or three dimensions so that the low-dimensional space can be easily visualized. Both methods try to preserve the local structure of the data, but UMAP is generally faster than t-SNE for large data sets.

**JMP Version Added:** 17

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Multivariate Embedding(
    Y( :Sepal length, :Sepal width, :Petal length, :Petal width )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
/* Parameters can be changed according to data features */
obj = dt << Multivariate Embedding(
    Y( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    Method( "t-SNE" ),
    Maximum Iterations( 1500 ),
    Perplexity( 15 ),
    Initial Principal Component Dimensions( 55 ),
    Random Seed( 2022 ),
    Output Dimensions( 3 )
);
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
/* by group example */
dt << New Column( "_bycol",
    Character,
    Nominal,
    set values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Multivariate Embedding(
    Y( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    By( _bycol )
);
```

### [Naive Bayes](#naive-bayes)[](#naive-bayes "Click to copy url")

**Syntax:** Naive Bayes( Y( column ), X( columns ), Method( "Naive Bayes" ) )

**Description:** Predicts group membership for a categorical variable based on the closeness of its predictor values to the predictor values for each group.

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Naive Bayes(
    Y( :Species ),
    X( :Sepal length, :Sepal width, :Petal length, :Petal width )
);
```

### [Neural](#neural)[](#neural "Click to copy url")

**Syntax:** Neural( Y( column ), X( columns ), \<Validation( column )\> )

**Description:** Predicts one or more response variables using a flexible function of the input variables. The flexible framework incorporates layering and s-shaped functions.

``` jsl
dt = Open( "$SAMPLE_DATA/Diabetes.jmp" );
obj = dt << Neural(
    Y( :Y ),
    X( :Age, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Go
);
```

### [New Table](#new-table)[](#new-table "Click to copy url")

**Syntax:** dt = New Table( name, \<visibility("private"\|"invisible"\|"visible")\>, \<Enable Filter Views(bool)\>, \<actions\> )

**Description:** Creates a new data table. "Invisible" hides the data table from view but lists it in the JMP Home Window. "Private" hides the table completely. "Visible" is the default, and creates a normal table that is visible and listed in the JMP Home Window. The optional actions arguments are any messages that data tables support.

``` jsl
dt = New Table( "Little Class",
    Add Rows( 3 ),
    New Column( "name", Character, Nominal, Set Values( {"KATIE", "LOUISE", "JANE"} ) ),
    New Column( "height", Continuous, Set Values( [59, 61, 55] ) )
);
```

### [Nonlinear](#nonlinear)[](#nonlinear "Click to copy url")

**Syntax:** Nonlinear( Y( column ), X( column with predictor formula ) )

**Description:** Fits nonlinear models using least squares or a custom loss function.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
```

### [Normal Mixtures](#normal-mixtures)[](#normal-mixtures "Click to copy url")

**Syntax:** Normal Mixtures( Y( column(s) ), Number of Clusters( number ) )

**Description:** Clusters rows based on numeric variables when your data come from a mixture of overlapping multivariate normal distributions. You must specify the number of clusters in advance.

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Normal Mixtures(
    Y( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    Number of Clusters( 3 )
);
obj << Go;
```

### [Normalization](#normalization)[](#normalization "Click to copy url")

**Syntax:** Normalization( Y( columns ) )

**Description:** Adjusts for technical biases and improves suitability for subsequent analysis

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Normalization( Y( :Sepal length, :Sepal width, :Petal length, :Petal width ) );
```

### [Notebook](#notebook)[](#notebook "Click to copy url")

**Syntax:** nb = Notebook( name\|number )

**Description:** Creates a new notebook, or returns the notebook with the provided name or index.

``` jsl

nb = Notebook();
```

### [Oneway](#oneway)[](#oneway "Click to copy url")

**Syntax:** Oneway( Y( columns ), X( columns ) )

**Description:** Models a continuous response across a set of categorical groups. Analysis methods include ANOVA, means comparisons, analysis of means, and quantile plots.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :Height ), X( :Age ) );
```

### [Open](#open)[](#open "Click to copy url")

**Syntax:** Open( filePath, \<data table options \| Excel import options \| text import options \| SAS import options \| HTML import options \| esriShapeFile import options \| PDF import options \| other file options \> )

**Description:** Opens a JMP file or imports another supported file type. The open data table option 'Invisible' hides the file from view but lists it in the JMP Home Window, 'Private' hides the file completely. The file option 'Select Columns' reads in only the specified columns, 'Ignore Columns' is the inverse of 'Select Columns', it does not read in the specified columns. The JMP file options 'Column Names Only' and 'Table Info' do not read in the data, nor create a data table. 'Column Names Only' returns the list of the data table's columns names, 'Table Info' returns the number of columns and rows in the data table. The options 'FIRST(n)'/'LAST(n)'/'RANDOM(n)' read in only n rows of the data table. If n is a number between 0 and 1, n is a fraction of the total number of rows in the data table.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp", ignore columns( "age" ) );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp", "Column Names Only" );
```

**Example 4**

``` jsl
info = Open( "$SAMPLE_DATA/probe.jmp", "Table Info" );
Print( info );
```

**Example 5**

``` jsl
info = Open( "$SAMPLE_DATA/SATByYear.jmp", random( 10 ) );
Print( info );
```

**Example 6**

``` jsl
info = Open( "$SAMPLE_DATA/SATByYear.jmp", First( 10 ) );
Print( info );
```

### [Parallel Plot](#parallel-plot)[](#parallel-plot "Click to copy url")

**Syntax:** Parallel Plot( Y( columns ), \<X( column )\> )

**Description:** Produces a plot of two or more variables with connecting line segments for each row.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/SAT.jmp" );
dt << Parallel Plot(
    Y(
        :"2004 Verbal"n, :"2004 Math"n, :"2003 Verbal"n, :"2003 Math"n, :"2002 Verbal"n,
        :"2002 Math"n, :"2001 Verbal"n, :"2001 Math"n, :"1999 Verbal"n, :"1999 Math"n,
        :"1994 Verbal"n, :"1994 Math"n, :"1997 Verbal"n, :"1997 Math"n, :"1992 Verbal"n,
        :"1992 Math"n
    )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Dogs.jmp" );
obj = dt << Parallel Plot( Y( :hist0, :hist1, :hist3, :hist5 ) );
```

### [Pareto Plot](#pareto-plot)[](#pareto-plot "Click to copy url")

**Syntax:** Pareto Plot( Cause( column ), \<X( column )\>, \<Subcategory( column )\>, \<Freq( column )\>, \<Weight( column )\> )

**Description:** Displays the relative frequency of items in a quality-related process in decreasing order. You can define one or more classification variables to create a comparative Pareto plot.

#### [Group](#group)[](#group "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot( Cause( :failure ), X( :clean ), Freq( :N ) );
```

#### [Simple](#simple)[](#simple "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure Raw Data.jmp" );
obj = dt << Pareto Plot( Cause( :failure ) );
```

#### [Subcategory](#subcategory)[](#subcategory "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failure2.jmp" );
obj = dt << Pareto Plot(
    Cause( :failure ),
    Subcategory( :clean ),
    Freq( :N ),
    Subcategory Bar Style( Stacked )
);
```

### [Partial Least Squares](#partial-least-squares)[](#partial-least-squares "Click to copy url")

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

### [Predictor Screening](#predictor-screening)[](#predictor-screening "Click to copy url")

**Syntax:** Predictor Screening( Y( columns ), X( columns ) )

**Description:** Identifies significant predictors from a large number of candidates by using bootstrap forest partitioning to evaluate the contribution of the predictors on the response.

``` jsl
dt = Open( "$SAMPLE_DATA/Bands Data.jmp" );
obj = dt << Predictor Screening( Y( :Banding? ), X( Column Group( "Predictors" ) ) );
```

### [Principal Components](#principal-components)[](#principal-components "Click to copy url")

**Syntax:** Principal Components( Y( columns ) )

**Description:** Models the variation in a set of variables in terms of a smaller number of independent linear combinations (principal components) of those variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Solubility.jmp" );
obj = dt << Principal Components(
    Y( :Ether, :Chloroform, :Benzene, :Carbon Tetrachloride, :Hexane )
);
```

### [Process Capability](#process-capability)[](#process-capability "Click to copy url")

**Syntax:** Process Capability( Process Variables (columns), \< Spec Limits() \> )

**Description:** Computes a process capability analysis for each process and creates graphs useful for analyzing the capability of multiple processes at one time. Specification limits can also be defined.

``` jsl
dt = Open( "$SAMPLE_DATA/Semiconductor Capability.jmp" );
obj = dt << Process Capability(
    Process Variables(
        :NPN1[:lot_id, :wafer], :PNP1[:lot_id, :wafer], :PNP2[:lot_id, :wafer],
        :NPN2[:lot_id, :wafer], :PNP3[:lot_id, :wafer]
    )
);
```

### [Process History Explorer](#process-history-explorer)[](#process-history-explorer "Click to copy url")

**Syntax:** Process History Explorer( Y( columns ),ID( columns), X( columns ), Step( columns ), Timestamp( columns ) )

**Description:** Identifies process steps associated with poor yield.

``` jsl
dt = Open( "$sample_data\Quality Control\Lot Wafer History.jmp" );
dt2 = Open( "$sample_data\Quality Control\Lot Wafer Yield.jmp" );
obj = dt << Process History Explorer(
    ID( :Lot, :Wafer ),
    X( :Tool, :Route ),
    Step( :Layer, :Operation ),
    Timestamp( :TimeIn, :TimeOut ),
    Yield Table( "Lot Wafer Yield" ),
    Yield Columns( "Yield" )
);
```

### [Process Screening](#process-screening)[](#process-screening "Click to copy url")

**Syntax:** Process Screening( Process Variables( columns ) )

**Description:** Examines many processes from several perspectives, including stability, capability, control chart tests, and shift (drift). Assists with the ability to focus on which processes need attention.

#### [Screen Count Processes with Alarm Graph for Environmental Monitoring](#screen-count-processes-with-alarm-graph-for-environmental-monitoring)[](#screen-count-processes-with-alarm-graph-for-environmental-monitoring "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Quality Control/Environmental Monitor Sim.jmp" );
obj = dt << Process Screening(
    Process Variables( :Count ),
    Grouping( :Type, :Grade, :Site ),
    Control Chart Type( "Count" ),
    Time( :Time ),
    Set Scrolling( 10 ), // table shows only the first 10 processes
    Alarm Graph( 1 ),
    Show Charts as Selected( 1 ),
    Select Where( Action >= 1 )
);
```

#### [Screen Many Processes with Grouping Column](#screen-many-processes-with-grouping-column)[](#screen-many-processes-with-grouping-column "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Semiconductor Capability.jmp" );
obj = dt << Process Screening(
    Process Variables( Column Group( "Processes" ) ),
    Grouping( :Site )
);
```

#### [Screen Many Processes with Individual-and-Moving-Range Control Chart Metrics](#screen-many-processes-with-individual-and-moving-range-control-chart-metrics)[](#screen-many-processes-with-individual-and-moving-range-control-chart-metrics "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Semiconductor Capability.jmp" );
obj = dt << Process Screening(
    Process Variables( Column Group( "Processes" ) ),
    Control Chart Type( "Indiv and MR" )
);
```

#### [Screen Many Processes with XBar-and-R Control Chart Metrics](#screen-many-processes-with-xbar-and-r-control-chart-metrics)[](#screen-many-processes-with-xbar-and-r-control-chart-metrics "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Semiconductor Capability.jmp" );
obj = dt << Process Screening(
    Process Variables( Column Group( "Processes" ) ),
    Control Chart Type( "XBar and R" )
);
```

#### [Screen Many Processes with XBar-and-S Control Chart Metrics](#screen-many-processes-with-xbar-and-s-control-chart-metrics)[](#screen-many-processes-with-xbar-and-s-control-chart-metrics "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Semiconductor Capability.jmp" );
obj = dt << Process Screening(
    Process Variables( Column Group( "Processes" ) ),
    Subgroup( :wafer ),
    Control Chart Type( "XBar and S" )
);
```

#### [Screen Nonnegative Continuous Data for Environmental Monitoring](#screen-nonnegative-continuous-data-for-environmental-monitoring)[](#screen-nonnegative-continuous-data-for-environmental-monitoring "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Quality Control/Environmental Monitor Sim.jmp" );
obj = dt << Process Screening(
    Process Variables( :Count ),
    Grouping( :Type, :Grade, :Site ),
    Control Chart Type( "Nonnegative Continuous" ),
    Time( :Time ),
    Set Scrolling( 10 ), // table shows only the first 10 processes
    Alarm Graph( 1 ),
    Show Charts as Selected( 1 )
);
```

#### [Screen Process with a 3-Way Chart (XBar-MR-and-R)](#screen-process-with-a-3-way-chart-xbar-mr-and-r)[](#screen-process-with-a-3-way-chart-xbar-mr-and-r "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Quality Control/Vial Fill Weights.jmp" );
obj = dt << Process Screening(
    Process Variables( :Fill Weight ),
    Subgroup( :Sample ),
    Control Chart Type( "XBar MR and R" ),
    Moving Range Limit Exceeded( 1 ),
    Chart Options as Selected( Dispersion Chart( 1 ) ),
    Show Charts as Selected( 1 ),
    RowStates( [0 1] )
);
```

#### [Screen Process with a 3-Way Chart (XBar-MR-and-S)](#screen-process-with-a-3-way-chart-xbar-mr-and-s)[](#screen-process-with-a-3-way-chart-xbar-mr-and-s "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Quality Control/Vial Fill Weights.jmp" );
obj = dt << Process Screening(
    Process Variables( :Fill Weight ),
    Subgroup( :Sample ),
    Control Chart Type( "XBar MR and S" ),
    Moving Range Limit Exceeded( 1 ),
    Show Charts as Selected( 1 ),
    RowStates( [0 1] )
);
```

#### [Screen Process with a Proportion Chart](#screen-process-with-a-proportion-chart)[](#screen-process-with-a-proportion-chart "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Quality Control/Electrical Component Defect Screening.jmp" );
obj = dt << Process Screening(
    Process Variables( :N Defective ),
    Control Chart Type( "Proportion" ),
    n Trials( :N Units ),
    Show Charts as Selected( 1 ),
    RowStates( [0 1] )
);
```

#### [Screen Processes to Show Control Charts for Selected Processes](#screen-processes-to-show-control-charts-for-selected-processes)[](#screen-processes-to-show-control-charts-for-selected-processes "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Semiconductor Capability.jmp" );
obj = dt << Process Screening(
    Process Variables( Column Group( "Processes" ) ),
    Control Chart Type( "Indiv and MR" ),
    Show Charts as Selected( 1 ),
    Select Where( Alarm Rate > 0.006 ),     // what selects in the table
    Filter Where( Alarm Rate > 0.005 )  // what shows in the table
);
```

#### [Screen Processes with Capability Goal Plot](#screen-processes-with-capability-goal-plot)[](#screen-processes-with-capability-goal-plot "Click to copy url")

``` jsl


dt = Open( "$SAMPLE_DATA/Semiconductor Capability.jmp" );
obj = dt << Process Screening(
    Process Variables( Column Group( "Processes" ) ),
    Set Scrolling( 10 ), // table shows only the first 10 processes
    Goal Plot( 1 )
);
```

#### [Screen Processes with Process Performance Graph](#screen-processes-with-process-performance-graph)[](#screen-processes-with-process-performance-graph "Click to copy url")

``` jsl


dt = Open( "$SAMPLE_DATA/Semiconductor Capability.jmp" );
obj = dt << Process Screening(
    Process Variables( Column Group( "Processes" ) ),
    Set Scrolling( 10 ), // table shows only the first 10 processes
    Process Performance Graph( 1 )
);
```

#### [Screen Processes with Process Potential Graph](#screen-processes-with-process-potential-graph)[](#screen-processes-with-process-potential-graph "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Quality Control/Coating.jmp" );
Column( "Weight" ) << Set Property(
    "Process Screening",
    {Centerline( 20.5 ), Specified Sigma( 1.5 ), Measurement Sigma( .8 )}
);
Column( "Weight" ) << Set Property( "Spec Limits", {LSL( 17 ), USL( 24 )} );
obj = dt << Process Screening(
    Process Variables( :Weight ),
    Subgroup( :Sample ),
    Control Chart Type( "XBar and R" ),
    Out of Spec Count( 0 ),
    Out of Spec Rate( 0 ),
    Latest Out of Spec( 0 ),
    Process Potential Graph( 1 )
);
```

#### [Screen Processes with Shift Detection](#screen-processes-with-shift-detection)[](#screen-processes-with-shift-detection "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Quality Control/Steam Turbine Current.jmp" );
obj = dt << Process Screening(
    Process Variables( :Fuel, :Steam Flow, :Steam Temp, :MW, :Cool Temp, :Pressure ),
    Control Chart Type( "Indiv and MR" ),
    Shift Graph( 1 ),
    Show Charts as Selected( 1 ),
    Select Where( Stability Index > 2 )
);
```

#### [Screen Processes with Specification Limits in a Separate Table](#screen-processes-with-specification-limits-in-a-separate-table)[](#screen-processes-with-specification-limits-in-a-separate-table "Click to copy url")

``` jsl

dt1 = Open( "$SAMPLE_DATA/Cities.jmp" );
dt2 = Open( "$SAMPLE_DATA/CitySpecLimits.jmp" );
obj = dt1 << Process Screening(
    Y( :OZONE, :CO, :SO2, :NO ),
    Use Limits Table(
        1,
        dt2,
        Process Variables( :Column 1 ),
        LSL( :_LSL ),
        USL( :_USL ),
        Target( :_Target ),
        Go
    )
);
```

### [Profiler](#profiler)[](#profiler "Click to copy url")

**Syntax:** Profiler( Y( column1, \<column2\>, ..., \<PredSE column1, PredSE column2\>, ... ), \<Expand\> )

**Description:** Produces an interactive graph that enables you to explore how a predicted response changes as you change factor settings. For each factor, the profiler shows prediction traces that are based on saved predictions formulas and linear constraints and illustrate how the response changes with respect to that factor. The Expand argument corresponds to the Expand Intermediate Formulas option in the launch window.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Profiler(
    Y(
        :Pred Formula ABRASION, :Pred Formula MODULUS, :Pred Formula ELONG,
        :Pred Formula HARDNESS
    ),
    Desirability Functions( 1 )
);
```

**Example 2**

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
colNum = N Items( dt << Get Column Names );
obj = dt << Fit Model(
    Validation( :Validation ),
    Y( :Y ),
    Effects( :Age, :Gender, :BMI, :BP, :Total Cholesterol ),
    Personality( "Standard Least Squares" ),
    Emphasis( "Effect Screening" ),
    Run()
);
obj << Save Columns( Prediction Formula( 1 ), StdErr Pred Formula( 1 ) );
obj << Close Window( 1 );
predCol = Column( dt, colNum + 1 );
stderrCol = Column( dt, colNum + 2 );
dt << Profiler(
    Y( predCol, stderrCol ),
    Profiler( 1, Confidence Intervals( 1 ), ),
    Use SE Formula( 1 )
);
```

**Example 3**

``` jsl
dt = Open( "$Sample_Data/Stochastic Optimization.jmp" );
dt << Profiler( Y( :Yield ), Profiler( 1, Desirability Functions( 1 ), ), Expand );
```

### [Recurrence Analysis](#recurrence-analysis)[](#recurrence-analysis "Click to copy url")

**Syntax:** Recurrence Analysis( Y( column ), Cost( column ), Label( column ), \<Grouping( column )\> )

**Description:** Analyzes how a recurring event is distributed over time, per system, or until the system goes out of service.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Bladder Cancer.jmp" );
obj = dt << Recurrence Analysis(
    Y( :Age ),
    Cost( :Cost ),
    Grouping( :Treatment Group ),
    Label( :Patient Number )
);
```

### [Reliability Forecast](#reliability-forecast)[](#reliability-forecast "Click to copy url")

**Syntax:** Reliability Forecast

**Description:** Predicts future failures based on observed data and future units at risk. The platform accepts several input formats. See each format for specification details.

#### [Dates Format](#dates-format)[](#dates-format "Click to copy url")

``` jsl

dt1 = Open( "$SAMPLE_DATA/Reliability/Small Production part1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Reliability/Small Production part2.jmp" );

obj = dt1 << Reliability Forecast(
    Input Format( Dates ),
    Production Data Table(
        dt1,
        Production Count( :Sold Quantity ),
        Timestamp( :Sold Month )
    ),
    Failure Data Table(
        dt2,
        Failure Time( :Return Month ),
        Timestamp( :Sold Month ),
        Failure Count( :Return Quantity )
    ),
    Life Time Unit( Month ),
    Show Legend( 1 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group( "" ),
        Risk Set( [2550, 2600, 2650, 2700, 2750, 2800, 2850] ),
        Future Risk Set(
            [3082.5, 3052.5, 3367.5, 3952.5, 3667, 3667],
            [3347740800, 3350160000, 3352579200, 3355257600, 3357849600, 3360528000]
        ),
        Forecast To( "02/2011" ),
        Distribution( Weibull ),
        Contract( 6, Month ),
        Forecast Type( Sequential ),
        Interval Type( Prediction Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 1 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
```

#### [Nevada Format](#nevada-format)[](#nevada-format "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
```

#### [Time to Event Format](#time-to-event-format)[](#time-to-event-format "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Small Production Time to Event.jmp" );
obj = dt << Reliability Forecast(
    Input Format( Time to Event ),
    Time to Event( :"Time (Month)"n, :Time Right ),
    Freq( :Freq ),
    Life Time Unit( Month ),
    Forecast Start( Informat( "03/01/2010", "Locale Date" ) ),
    Forecast(
        Group( "" ),
        Future Risk Set( [33, 33, 33], [3352924800, 3355516800, 3358195200] ),
        Forecast To( "09/01/2010" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( [1] ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( 0 ),
        Use Approximate Distribution( 1 )
    )
);
```

### [Reliability Growth](#reliability-growth)[](#reliability-growth "Click to copy url")

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

### [Repeated Measures Degradation](#repeated-measures-degradation)[](#repeated-measures-degradation "Click to copy url")

**Syntax:** Repeated Measures Degradation( Y( column ), Time( column ), \<X( column )\>, \<Freq( column )\>, \<Censor( column ), Censor Code( value )\> )

**Description:** Models repeated measures degradation data over time with random parameters.

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Device B.jmp" );
obj = dt << Repeated Measures Degradation(
    Y( :Power Drop ),
    Time( :Hours ),
    Label( :Device ),
    X( :Degrees C ),
    Reference Temperature( "Celsius", 195 ),
    Control( "Linear", "Linear", "First Order Kinetics Type 2" )
);
```

### [Response Screening](#response-screening)[](#response-screening "Click to copy url")

**Syntax:** Response Screening( Y( columns ), X( columns ) )

**Description:** Automates the process of conducting tests for linear model effects across a large number of responses. Test results and summary statistics are presented in data tables and plots. The false discovery rate (FDR) guards against incorrect declarations of significance. A robust estimation method reduces the sensitivity of tests to outliers.

#### [Response Screening in subgroups with volcano plot selected](#response-screening-in-subgroups-with-volcano-plot-selected)[](#response-screening-in-subgroups-with-volcano-plot-selected "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Life Sciences/Genotypes Pedigree.jmp" );
obj = dt << Response Screening(
    Y( :Trait1, :Trait2, :Trait3, :Trait4 ),
    X( :Father, :Mother, :Sex, :Disease Status ),
    Subgroup( Column Group( "Markers" ) ),
    Common Y Scale( 1 ),
    SendToReport( Dispatch( {}, "", TabListBox, {Set Selected( 4 )} ) )
);
```

#### [Response Screening of 4 Responses and 26 Prospective Predictors](#response-screening-of-4-responses-and-26-prospective-predictors)[](#response-screening-of-4-responses-and-26-prospective-predictors "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Baltic.jmp" );
obj = dt << Response Screening( Y( :ls, :ha, :dt ), X( Column Group( "Intensities" ) ) );
```

#### [Response Screening of Many Columns in Groups](#response-screening-of-many-columns-in-groups)[](#response-screening-of-many-columns-in-groups "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Life Sciences/Genotypes Pedigree.jmp" );
obj = dt << Response Screening(
    Y( Column Group( "Markers" ) ),
    X( :Trait1, :Trait2, :Trait3, :Trait4 ),
    Grouping( "Sex" )
);
```

#### [Response Screening of Many Columns on Each of Four Predictors](#response-screening-of-many-columns-on-each-of-four-predictors)[](#response-screening-of-many-columns-on-each-of-four-predictors "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Life Sciences/Genotypes Pedigree.jmp" );
obj = dt << Response Screening(
    Y( Column Group( "Markers" ) ),
    X( :Trait1, :Trait2, :Trait3, :Trait4 )
);
```

#### [Response Screening of Many Columns with Means Differences Volcano Plot](#response-screening-of-many-columns-with-means-differences-volcano-plot)[](#response-screening-of-many-columns-with-means-differences-volcano-plot "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Life Sciences/Genotypes Pedigree.jmp" );
obj = dt << Response Screening(
    Y( Column Group( "Markers" ) ),
    X( :Father, :Mother, :Sex, :Disease Status ),
    Common Y Scale( 1 ),
    Volcano Plots Use FDR Axis( 1 ),
    SendToReport(
        Dispatch( {}, "", TabListBox( 1 ), {Set Selected( 4 )} ),
        Dispatch( {}, "", TabListBox( 2 ), {Set Selected( 2 )} )
    )
);
```

#### [Response Screening Specified with Column Numbers](#response-screening-specified-with-column-numbers)[](#response-screening-specified-with-column-numbers "Click to copy url")

``` jsl

dt = Open( "$Sample_Data/Probe.jmp" );
obj = dt << Response Screening( X( :Process ), Y( Eval( 8 :: 108 ) ) );
```

#### [Response Screening with Robust Fitting](#response-screening-with-robust-fitting)[](#response-screening-with-robust-fitting "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Probe.jmp" );
obj = dt << Response Screening(
    Y( Column Group( "Responses" ) ),
    X( :Process ),
    Robust( 1 )
);
```

### [Scatterplot 3D](#scatterplot-3d)[](#scatterplot-3d "Click to copy url")

**Syntax:** Scatterplot 3D( Y( columns ) )

**Description:** Produces a rotating three-dimensional scatterplot for three or more variables. If you specify more than three variables, you can cycle through which variables are shown in the scatterplot.

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Scatterplot 3D( Y( :Sepal length, :Sepal width, :Petal length, :Petal width ) );
```

### [Scatterplot Matrix](#scatterplot-matrix)[](#scatterplot-matrix "Click to copy url")

**Syntax:** Scatterplot Matrix( Y( columns ), \<X( columns )\>, \<Group( column )\>, \<By( column )\> )

**Description:** Produces a grid of scatterplots that enables you to explore bivariate relationships. If no X variables are specified, the scatterplots are for all pairs of the Y variables. If one or more X variables are specified, the scatterplots are for the Y variables plotted against the X variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = dt << Scatterplot Matrix(
    Y( :Sepal length, :Sepal width, :Petal length, :Petal width )
);
```

### [Structural Equation Models](#structural-equation-models)[](#structural-equation-models "Click to copy url")

**Syntax:** Structural Equation Models( Model Variables ( columns ) )

**Description:** Provides a framework to fit a variety of models, including confirmatory factor analysis, path models with or without latent variables, measurement error models, and latent growth curve models.

**JMP Version Added:** 15

#### [Confirmatory Factor Analysis](#confirmatory-factor-analysis)[](#confirmatory-factor-analysis "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
```

#### [Higher Order Confirmatory Factor Analysis](#higher-order-confirmatory-factor-analysis)[](#higher-order-confirmatory-factor-analysis "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables(
        :Support_L, :Goal_L, :Work_L, :Interact_L, :Person_C, :Intra_C, :Inter_C, :General_S,
        :Growth_S, :Coworker_S, :Supervisor_S
    ),
    Fit(
        Model Name( "Higher Order CFA" ),
        New Latent( "Leadership", "Conflict", "Satisfaction", "General" ),
        Means(
            {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L, :Person_C, :Intra_C,
            :Inter_C, :General_S, :Growth_S, :Coworker_S, :Supervisor_S}}
        ),
        Loadings(
            {"Leadership", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}},
            {"Conflict", {:Person_C, :Intra_C, :Inter_C}, {1}},
            {"Satisfaction", {:General_S, :Growth_S, :Coworker_S, :Supervisor_S}, {1}},
            {"General", {"Leadership", "Conflict", "Satisfaction"}, {1}}
        ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {:Person_C, {:Person_C}},
            {:Intra_C, {:Intra_C}},
            {:Inter_C, {:Inter_C}},
            {:General_S, {:General_S}},
            {:Growth_S, {:Growth_S}},
            {:Coworker_S, {:Coworker_S}},
            {:Supervisor_S, {:Supervisor_S}},
            {"Leadership", {"Leadership"}},
            {"Conflict", {"Conflict"}},
            {"Satisfaction", {"Satisfaction"}},
            {"General", {"General"}}
        )
    )
);
```

#### [Linear Latent Growth Curve Model](#linear-latent-growth-curve-model)[](#linear-latent-growth-curve-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables(
        :Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
        :Multiple Choice Year4
    ),
    Fit(
        Model Name( "Linear Growth Curve Model" ),
        New Latent( "Intercept", "Slope" ),
        Means( {"Constant", {"Intercept", "Slope"}} ),
        Loadings(
            {"Intercept", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {1, 1, 1, 1}},
            {"Slope", {:Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
            :Multiple Choice Year4}, {0, 1, 2, 3}}
        ),
        Variances(
            {:Multiple Choice Year1, {:Multiple Choice Year1}, {"b1"}},
            {:Multiple Choice Year2, {:Multiple Choice Year2}, {"b1"}},
            {:Multiple Choice Year3, {:Multiple Choice Year3}, {"b1"}},
            {:Multiple Choice Year4, {:Multiple Choice Year4}, {"b1"}},
            {"Intercept", {"Intercept"}},
            {"Slope", {"Slope"}}
        ),
        Covariances( {"Intercept", {"Slope"}} ),
        Path Diagram Properties( Show Means( 1 ) )
    )
);
```

#### [Multiple Linear Regression with SEM](#multiple-linear-regression-with-sem)[](#multiple-linear-regression-with-sem "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables( :Satisfaction_Avg, :Support_L, :Goal_L, :Work_L ),
    Fit(
        Model Name( "Multiple Regression" ),
        Means( {"Constant", {:Satisfaction_Avg, :Support_L, :Goal_L, :Work_L}} ),
        Regressions(
            {:Support_L, {:Satisfaction_Avg}},
            {:Goal_L, {:Satisfaction_Avg}},
            {:Work_L, {:Satisfaction_Avg}}
        ),
        Variances(
            {:Satisfaction_Avg, {:Satisfaction_Avg}},
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}}
        ),
        Covariances( {:Support_L, {:Goal_L, :Work_L}}, {:Goal_L, {:Work_L}} ),

    )
);
```

#### [Path Analysis Model](#path-analysis-model)[](#path-analysis-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Online Consumer Data.jmp" );
dt << Structural Equation Models(
    Model Variables( :Privacy, :Reputation, :Trust, :Purchase Int ),
    Fit(
        Model Name( "Path Analysis with Observed Variables" ),
        Means( {"Constant", {:Privacy, :Reputation, :Trust, :Purchase Int}} ),
        Regressions(
            {:Privacy, {:Trust}},
            {:Reputation, {:Trust, :Purchase Int}},
            {:Trust, {:Purchase Int}}
        ),
        Variances(
            {:Privacy, {:Privacy}},
            {:Reputation, {:Reputation}},
            {:Trust, {:Trust}},
            {:Purchase Int, {:Purchase Int}}
        ),
        Covariances( {:Privacy, {:Reputation}} )
    )
);
```

#### [Path Analysis with Latent Variables](#path-analysis-with-latent-variables)[](#path-analysis-with-latent-variables "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables(
        :Support_L, :Goal_L, :Work_L, :Interact_L, :Person_C, :Intra_C, :Inter_C, :General_S,
        :Growth_S, :Coworker_S, :Supervisor_S
    ),
    Fit(
        Model Name( "Path Analysis with Latent Variables" ),
        New Latent( "Leadership", "Conflict", "Satisfaction" ),
        Means(
            {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L, :Person_C, :Intra_C,
            :Inter_C, :General_S, :Growth_S, :Coworker_S, :Supervisor_S}}
        ),
        Loadings(
            {"Leadership", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}},
            {"Conflict", {:Person_C, :Intra_C, :Inter_C}, {1}},
            {"Satisfaction", {:General_S, :Growth_S, :Coworker_S, :Supervisor_S}, {1}}
        ),
        Regressions(
            {"Leadership", {"Conflict", "Satisfaction"}},
            {"Conflict", {"Satisfaction"}}
        ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {:Person_C, {:Person_C}},
            {:Intra_C, {:Intra_C}},
            {:Inter_C, {:Inter_C}},
            {:General_S, {:General_S}},
            {:Growth_S, {:Growth_S}},
            {:Coworker_S, {:Coworker_S}},
            {:Supervisor_S, {:Supervisor_S}},
            {"Leadership", {"Leadership"}},
            {"Conflict", {"Conflict"}},
            {"Satisfaction", {"Satisfaction"}}
        )
    )
);
```

#### [Quadratic Latent Growth Curve Model](#quadratic-latent-growth-curve-model)[](#quadratic-latent-growth-curve-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables(
        :Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
        :Multiple Choice Year4
    ),
    Fit(
        Model Name( "Quadratic Growth Model" ),
        New Latent( "Intercept", "Slope", "QuadSlope" ),
        Means( {"Constant", {"Intercept", "Slope", "QuadSlope"}} ),
        Loadings(
            {"Intercept", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {1, 1, 1, 1}},
            {"Slope", {:Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
            :Multiple Choice Year4}, {0, 1, 2, 3}},
            {"QuadSlope", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {0, 1, 4, 9}}
        ),
        Variances(
            {:Multiple Choice Year1, {:Multiple Choice Year1}},
            {:Multiple Choice Year2, {:Multiple Choice Year2}},
            {:Multiple Choice Year3, {:Multiple Choice Year3}},
            {:Multiple Choice Year4, {:Multiple Choice Year4}},
            {"Intercept", {"Intercept"}},
            {"Slope", {"Slope"}},
            {"QuadSlope", {"QuadSlope"}}
        ),
        Covariances( {"Intercept", {"Slope", "QuadSlope"}}, {"Slope", {"QuadSlope"}} ),
        Path Diagram Properties( Show Means( 1 ) )
    )
);
```

#### [Simple Linear Regression with SEM](#simple-linear-regression-with-sem)[](#simple-linear-regression-with-sem "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Satisfaction_Avg ),
    Fit(
        Model Name( "Simple Regression" ),
        Means( {"Constant", {:Leadership_Avg, :Satisfaction_Avg}} ),
        Regressions( {:Leadership_Avg, {:Satisfaction_Avg}} ),
        Variances(
            {:Leadership_Avg, {:Leadership_Avg}},
            {:Satisfaction_Avg, {:Satisfaction_Avg}}
        )
    )
);
```

#### [Simple Mediation Model](#simple-mediation-model)[](#simple-mediation-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg, :Satisfaction_Avg ),
    Fit(
        Model Name( "Mediation Analysis" ),
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg, :Satisfaction_Avg}} ),
        Regressions(
            {:Leadership_Avg, {:Conflict_Avg, :Satisfaction_Avg}},
            {:Conflict_Avg, {:Satisfaction_Avg}}
        ),
        Variances(
            {:Leadership_Avg, {:Leadership_Avg}},
            {:Conflict_Avg, {:Conflict_Avg}},
            {:Satisfaction_Avg, {:Satisfaction_Avg}}
        )
    )
);
```

### [Support Vector Machines](#support-vector-machines)[](#support-vector-machines "Click to copy url")

**Syntax:** Support Vector Machines(Y( column ), X( columns ))

**Description:** Predicts a response based on the support vectors in the space of the X variables. One of the goals of the Support Vector Machines algorithm is to use training data to learn how to classify new data.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Iris.jmp" );
obj = Support Vector Machines(
    Y( :Species ),
    X( :Sepal length, :Sepal width, :Petal length, :Petal width )
);
```

### [Surface Plot](#surface-plot)[](#surface-plot "Click to copy url")

**Syntax:** Surface Plot( Columns() )

**Description:** Produces a rotating three-dimensional plot of points or a surface defined by a saved formula.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
obj = dt << Surface Plot(
    Columns(
        :Pred Formula ABRASION, :Pred Formula MODULUS, :Pred Formula ELONG,
        :Pred Formula HARDNESS
    )
);
```

### [Survival](#survival)[](#survival "Click to copy url")

**Syntax:** Survival( Y( columns ), Censor( column ), \<Grouping( column )\> )

**Description:** Calculates estimates of survival functions using the product-limit (Kaplan-Meier) method for one or more groups.

``` jsl
dt = Open( "$SAMPLE_DATA/Rats.jmp" );
obj = dt << Survival( Y( :days ), Censor( :Censor ), Grouping( :Group ) );
```

### [Tabulate](#tabulate)[](#tabulate "Click to copy url")

**Syntax:** Tabulate( Add Table( Column Table( Analysis Columns( column(s) )\|Grouping Columns( column(s))\|Statistics( )), Row Table( Analysis Columns( column(s) )\|Grouping Columns( column(s))\|Statistics( )) )

**Description:** Creates a custom table of summary statistics of one or more variables. The variables can be grouped by one or more classification columns. Enables you to build the summary table using drag and drop operations.

#### [Categories and stats](#categories-and-stats)[](#categories-and-stats "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :gender, :goals ), Statistics( N, Column % ) ),
        Row Table( Grouping Columns( :Grade, :Age ) )
    )
);
```

#### [Columns by Categories](#columns-by-categories)[](#columns-by-categories "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Row Table( Columns by Categories( :Grades, :Sports, :Looks, :Money ) ) )
);
```

#### [Frequency](#frequency)[](#frequency "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Freq( :Count ),
    Add Table( Row Table( Grouping Columns( :Causes ) ) )
);
```

#### [ID column](#id-column)[](#id-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    ID( :Division ),
    Set Format( Uniform Format( 10, 2 ) ),
    Add Table(
        Column Table(
            Statistics( Sum ),
            Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ),
            Pack(
                Analysis Columns( City MPG, Hwy MPG, Comb MPG ),
                Template( "^FIRST  (^OTHERS)", "/" )
            )
        ),
        Row Table( Grouping Columns( :Mfr Name ) )
    )
);
```

#### [Multiple response grouping columns](#multiple-response-grouping-columns)[](#multiple-response-grouping-columns "Click to copy url")

``` jsl
dt = Open( "$Sample_Data/Consumer Preferences.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :Floss Delimited ), Statistics( N, "% of Total"n ) ),
        Row Table( Grouping Columns( :Frequency of Teeth Cleaning, :Brush Delimited ) )
    )
);
```

#### [Multiple response page column](#multiple-response-page-column)[](#multiple-response-page-column "Click to copy url")

``` jsl
dt = Open( "$Sample_Data/Big Class Families.jmp" );
obj = Tabulate(
    Show Control Panel( 0 ),
    Page Column( :family cars( "Jeep" ) ),
    Add Table(
        Column Table( Analysis Columns( :height ), Statistics( N, "% of Total"n ) ),
        Row Table( Grouping Columns( :sex ) )
    )
);
```

#### [Multiple row and column tables](#multiple-row-and-column-tables)[](#multiple-row-and-column-tables "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :gender ) ),
        Column Table( Grouping Columns( :race ) ),
        Row Table( Grouping Columns( :goals ) ),
        Row Table( Grouping Columns( :"Urban/Rural"n ) )
    )
);
```

#### [Multiple row tables](#multiple-row-tables)[](#multiple-row-tables "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Row Table( Grouping Columns( :Grades ) ),
        Row Table( Grouping Columns( :Sports ) ),
        Row Table( Grouping Columns( :Looks ) ),
        Row Table( Grouping Columns( :Money ) )
    )
);
```

#### [Nested categories](#nested-categories)[](#nested-categories "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
```

#### [Packed columns](#packed-columns)[](#packed-columns "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Statistics( Sum, Max ),
            Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ),
            Pack(
                Analysis Columns( City MPG, Hwy MPG, Comb MPG ),
                Template( "^FIRST  (^OTHERS)", "/" )
            )
        ),
        Row Table( Grouping Columns( :Mfr Name, :Engine ) )
    )
);
```

#### [Page column](#page-column)[](#page-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Page Column( :Engine( "Gas" ) ),
    Add Table(
        Column Table( Analysis Columns( :City MPG, :Hwy MPG ), Statistics( Max ) ),
        Row Table( Grouping Columns( :Mfr Name ) )
    )
);
```

#### [Stacked grouping columns](#stacked-grouping-columns)[](#stacked-grouping-columns "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :marital status ),
            Add Aggregate Statistics( :marital status ),
            Analysis Columns( :age ),
            Statistics( Min, Max )
        ),
        Row Table(
            Grouping Columns( :sex, :country, :size ),
            Add Aggregate Statistics( :sex, :country, :size ),
            Stack Grouping Columns( 1 )
        )
    )
);
```

#### [Weight](#weight)[](#weight "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Physical Data.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Weight( :Weight ),
    Add Table(
        Column Table( Analysis Columns( :Horsepower ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Type ) )
    )
);
```

### [Ternary Plot](#ternary-plot)[](#ternary-plot "Click to copy url")

**Syntax:** Ternary Plot( Y( columns ) )

**Description:** Produces a two-dimensional plot of three mixture components that sum to a constant.

``` jsl
dt = Open( "$SAMPLE_DATA/Plasticizer.jmp" );
obj = dt << Ternary Plot( Y( :p1, :p2, :p3 ) );
```

### [Text Explorer](#text-explorer)[](#text-explorer "Click to copy url")

**Syntax:** Text Explorer( Text Columns( columns ) )

**Description:** Parses words from text in a column, counts them, associates them with other columns, saves indicators, and graphs relationships.

``` jsl
dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
obj = dt << Text Explorer( Text Columns( :Reasons Not to Floss ) );
```

### [Time Series](#time-series)[](#time-series "Click to copy url")

**Syntax:** Time Series( Y( column ) )

**Description:** Models a series of observations over equally spaced time points. Includes a time series plot, autocorrelations, variogram, spectral density, ARIMA, seasonal ARIMA, smoothing models, and forecasts.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
```

### [Time Series Forecast](#time-series-forecast)[](#time-series-forecast "Click to copy url")

**Syntax:** Time Series Forecast( Y( column ) )

**Description:** Fits and forecasts multiple time series using specified methods.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/M3C Quarterly.jmp" );
obj = dt << Time Series Forecast( Y( :Y ), Grouping( :Series ), Time( :Time ) );
```

### [Uplift](#uplift)[](#uplift "Click to copy url")

**Syntax:** Uplift( Y( column ), X( columns ), Treatment( column ) )

**Description:** Fits a recursive partition tree that selects splits to maximize treatment differences. The models identify groups of individuals who are most likely to respond to a treatment.

**Example 1**

``` jsl
dt = Open( "$Sample_Data/Hair Care Product.jmp" );
obj = Uplift(
    Y( :Purchase ),
    X( :Gender, :Age, :Hair Color, :U.S. Region, :Residence ),
    Treatment( :Promotion ),
    Split Best( 3 )
);
```

**Example 2**

``` jsl
dt = Open( "$Sample_Data/Hair Care Product.jmp" );
dt << Make Validation Column(
    Training Set( .6 ),
    Validation Set( .2 ),
    Test Set( .2 ),
    New Column Name( "Valid1" ),
    Go
);
obj = dt << Uplift(
    Y( :Purchase ),
    X( :Gender, :Age, :Hair Color, :U.S. Region, :Residence ),
    Treatment( :Promotion ),
    Validation( :Valid1 ),
    Split Best( 3 )
);
```

### [Variability Chart](#variability-chart_1)[](#variability-chart_1 "Click to copy url")

**Syntax:** Variability Chart( Y( column ), X( columns ) )

**Description:** Analyzes continuous measurements to determine how your measurement system is performing. You can also perform a gauge study to see measures of variation in your data.

#### [Crossed Effects Model](#crossed-effects-model)[](#crossed-effects-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/2 Factors Crossed.jmp" );
obj = dt << Variability Chart(
    Y( :Measurement ),
    Model( "Crossed" ),
    X( :Operator, :part# ),
    Variance Components( 1 )
);
```

#### [Crossed then Nested Effects Model](#crossed-then-nested-effects-model)[](#crossed-then-nested-effects-model "Click to copy url")

``` jsl
dt = New Table( "3 Factors Crossed then Nested",
    Add Rows( 81 ),
    New Column( "Operator",
        Character( 7 ),
        "Nominal",
        Set Values(
            {"Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara",
            "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara",
            "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara", "Clara",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo",
            "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Eduardo", "Jane", "Jane",
            "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane",
            "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane", "Jane",
            "Jane", "Jane", "Jane", "Jane", "Jane"}
        ),
        Set Display Width( 0 )
    ),
    New Column( "Instrument",
        Character( 1 ),
        "Nominal",
        Set Values(
            {"A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B",
            "B", "B", "C", "C", "C", "C", "C", "C", "C", "C", "C", "A", "A", "A", "A", "A",
            "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B", "B", "B", "C", "C", "C",
            "C", "C", "C", "C", "C", "C", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B",
            "B", "B", "B", "B", "B", "B", "B", "B", "C", "C", "C", "C", "C", "C", "C", "C",
            "C"}
        ),
        Set Display Width( 0 )
    ),
    New Column( "Part",
        Numeric,
        "Nominal",
        Format( "Best", 8 ),
        Set Values(
            [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9,
            10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16,
            16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23,
            23, 23, 24, 24, 24, 25, 25, 25, 26, 26, 26, 27, 27, 27]
        ),
        Set Display Width( 0 )
    ),
    New Column( "Y",
        Numeric,
        "Continuous",
        Format( "Best", 8 ),
        Set Values(
            [0.5, 0.6, 0.2, 0.8, 0.6, 0.6, 1.6, 1.1, 1, 0.4, 0.2, 0.1, 0.1, 0.5, 0, 0.3, 0.6,
            0.8, 0.1, 0.1, 0.2, 0.4, 0.9, 1.8, 0.1, 0.3, 0.4, 0.1, 0.3, 0.1, 0.9, 0.4, 0, 0.6,
            0.7, 0.7, 0.3, 0.1, 0.2, 0.3, 0.6, 0.2, 0.2, 0.4, 0.4, 0.8, 0.3, 0.3, 2.6, 0.4,
            1.6, 0.5, 0.3, 2.9, 0, 0, 0.5, 0.1, 0, 0.3, 0.5, 0, 0, 0.4, 0, 0.4, 0.3, 0.2, 0,
            0, 0.5, 0.1, 0.1, 0.2, 0.3, 1.1, 0.2, 0.1, 0.6, 0.3, 0.6]
        ),
        Set Display Width( 68 )
    )
);
obj = dt << Variability Chart(
    Y( :Y ),
    X( :Operator, :Instrument, :Part ),
    Model( "Crossed then Nested" ),
    Variance Components( 1 )
);
```

#### [Decide Later on Model](#decide-later-on-model)[](#decide-later-on-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/2 Factors Crossed.jmp" );
obj = dt << Variability Chart( Y( :Measurement ), X( :Operator, :part# ) );
```

#### [Main Effects Model](#main-effects-model)[](#main-effects-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/Wafer.jmp" );
obj = dt << Variability Chart(
    Y( :Y ),
    Model( "Main Effect" ),
    X( :Operator, :Wafer ),
    Variance Components( 1 )
);
```

#### [Nested Effects Model](#nested-effects-model)[](#nested-effects-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/2 Factors Nested.jmp" );
obj = dt << Variability Chart(
    Y( :Y ),
    Model( "Nested" ),
    X( :Operator, :Part ),
    Variance Components( 1 )
);
```

#### [Nested then Crossed Effects Model](#nested-then-crossed-effects-model)[](#nested-then-crossed-effects-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/3 Factors Nested & Crossed.jmp" );
obj = dt << Variability Chart(
    Y( :Y ),
    Model( "Nested then Crossed" ),
    X( :Operator, :Instrument, :Part ),
    Variance Components( 1 )
);
```

### [Virtual Join](#virtual-join)[](#virtual-join "Click to copy url")

**Syntax:** Virtual Join

**Description:** Links a main data table to an auxiliary data table through an ID column.

Enables the main table to access columns from the auxiliary table without physically joining the tables.

The Link ID column property marks a column in the auxiliary table as the ID column.

The Link Reference column property maps a column in the main table to the ID column in the auxiliary table.

Link Reference Property lets you set data table reference or the path of the data table that you want to link.

The option 'Use Linked Column Name' will build the linked columns with the source column name instead of the fully qualified unique name.

**Example 1**

``` jsl
cID = New Table( "Color IDs",
    Add Rows( 2 ),
    New Column( "ID", Numeric, Set Property( "Link ID", 1 ), Set Values( [1, 2] ) ),
    New Column( "color", Character, Set Values( {"magenta", "cyan"} ) )
);
cID << Save( "$temp\cID.jmp" );

Favs = New Table( "Favorite Colors",
    Add Rows( 4 ),
    New Column( "colorID",
        Numeric,
        Set Property( "Link Reference", Reference Table( "$temp\cID.jmp" ) ),
        Set Values( [1, 2, 1, 2] )
    ),
    New Column( "person", Character, Set Values( {"fred", "ralph", "artemus", "neil"} ) )
);

Favs:"color[colorID]"n << hide( 0 ); // show the color column in the table, it is hidden by default

Write( "\!n", Favs:person[2], " likes ", Favs:"color[colorID]"n[2] );

Favs:colorID[2] = 1; // change ralph's color by changing his color id
Write( "\!n", Favs:person[2], " likes ", Favs:"color[colorID]"n[2] );
Favs:"color[colorID]"n << hide( 1 ) << hide( 0 );

Write( "\!nRalph's color changed." );
```

**Example 2**

``` jsl
cID = New Table( "Color IDs",
    Add Rows( 2 ),
    New Column( "ID", Numeric, Set Values( [1, 2] ) ),
    New Column( "color", Character, Set Values( {"magenta", "cyan"} ) )
);

Favs = New Table( "Favorite Colors",
    Add Rows( 4 ),
    New Column( "colorID", Numeric, Set Values( [1, 2, 1, 2] ) ),
    New Column( "person", Character, Set Values( {"fred", "ralph", "artemus", "neil"} ) )
);
cID:ID << Set Property( "Link ID", 1 );
Favs:colorID << Set Property(
    "Link Reference",
    {Reference Table( cID ), options( "use linked column name" )}
);


Favs:color << hide( 0 ); // show the color column in the table, it is hidden by default

Write( "\!n", Favs:person[2], " likes ", Favs:color[2] ); // not Favs:"color[colorID]"n

Favs:colorID[2] = 1;    // change ralph's color by changing his color id
Write( "\!n", Favs:person[2], " likes ", Favs:color[2] );

Write( "\!nRalph's color changed." );
```

**Example 3**

``` jsl

cID = New Table( "Color IDs",
    Add Rows( 2 ),
    New Column( "ID", Numeric, Set Values( [1, 2] ) ),
    New Column( "color", Character, Set Values( {"magenta", "cyan"} ) )
);

Favs = New Table( "Favorite Colors",
    Add Rows( 4 ),
    New Column( "colorID", Numeric, Set Values( [1, 2, 1, 2] ) ),
    New Column( "person", Character, Set Values( {"fred", "ralph", "artemus", "neil"} ) )
);
cID:ID << Set Property( "Link ID", 1 );
Favs:colorID << Set Property(
    "Link Reference",
    {Reference Table( cID ), options( "use linked column name"(1), "auto open" )}
);

Favs2 = New Table( "More Favorites",
    Add Rows( 4 ),
    New Column( "ID", Numeric, Set Values( [1, 2, 3, 4] ) ),
    New Column( " person", Character, Set Values( {"susie", "james", "mark", "ami"} ) )
);

// A link ID and link reference can be assigned to the same column.  The option "Auto open" will  
// automatically open the linked tables for you when you open the main referencing table.
Favs2:ID << Set Property( "Link ID", 1 );
cID:ID << Set Property(
    "Link Reference",
    {Reference Table( Favs2 ), Options( "Use Linked Column Name"(1) )}
);

Favs:color << hide( 0 ); // Show the color column in the table, it is hidden by default
Favs:ID << hide( 0 );  // Show the ID column in the table, from More Favorites table
Write( "\!n", Favs:person[2], " likes ", Favs:color[2] ); // Not Favs:"color[colorID]"n

Favs:colorID[2] = 1;    // Change ralph's color by changing his color id
Write( "\!n", Favs:person[2], " likes ", Favs:color[2] );

Write( "\!nRalph's color changed." );
cid:person << hide( 0 );

Write( "\!n", cID:person[2], " likes ", Favs:color[4] );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Add Properties to Table](#add-properties-to-table)[](#add-properties-to-table "Click to copy url")

**Syntax:** obj \<\< Add Properties to Table

**Description:** Add the properties to the table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Properties( {2, 4} );
proplist = dt << Get Selected Properties();
dt2 = New Table( "Little Class" );
dt2 << Add Properties to Table( proplist );
```

### [Add Scripts to Table](#add-scripts-to-table)[](#add-scripts-to-table "Click to copy url")

**Syntax:** obj \<\< Add Scripts to Table

**Description:** This command is an alias of 'Add properties to table'.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Properties( {2, 4} );
proplist = dt << Get Selected Properties();
dt2 = New Table( "Little Class" );
dt2 << Add scripts to table( proplist );
```

### [Anonymize](#anonymize)[](#anonymize "Click to copy url")

**Syntax:** obj \<\< Anonymize( columns( columns ), \<Output Table( name )\> )

**Description:** Creates a new data table with unique identifiers removed.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << anonymize( columns( :name, :age ), output table name( "anonymized" ) );
```

### [Apply Columns List Filter To Data Grid](#apply-columns-list-filter-to-data-grid)[](#apply-columns-list-filter-to-data-grid "Click to copy url")

**Syntax:** obj \<\< Apply Columns List Filter To Data Grid( state=0\|1 )

**Description:** Turn on to apply filters in the data table Columns list to the data grid.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << Column Filter( Column Name( "tude" ) );
Wait( 1 );
dt << Apply Columns List Filter To Data Grid( 0 );
Wait( 1 );
dt << Apply Columns List Filter To Data Grid( 1 );
```

### [Apply Formula](#apply-formula)[](#apply-formula "Click to copy url")

**Syntax:** dt \<\< Apply Formula(\[Columns(\<col\|{cols}\|Group(col, count)\|\<group name\>, \[Ref(\<name\>)\], \[List Ref(\<name\>)\]\]+, \[Output(In Place\|In Place Formula\|New Formula(\<prefix\>\|New Static(\<prefix\>)\], \[Group(\<name\>)\])

**Description:** Use a formula to transform one or more columns and place the results (either as formulas or data) into new or existing columns.

At least one column group must be defined (a single column, an explicit list of columns, a run of columns, or an existing column group name).

The first group defined serves as the target if the output is 'in place'. If needed, you can specify a name in the formula that refers to the columns taken one at a time (Ref) or as a list of columns (ListRef).

Lastly, the output type can be specified, optionally with a name and group name for new columns.

**JMP Version Added:** 18

#### [New Data Columns/ListRef](#new-data-columnslistref)[](#new-data-columnslistref "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Data Table( "Big Class" ) << Apply Formula(
    Columns(
        Group( :height, 2 ),
        Ref( "_relative_from_height" ),
        ListRef( "height_to_weight" )
    ),
    Formula( _relative_from_height / Sum( height_to_weight ) ),
    Output( New Static )
);
```

#### [New Formula Columns/Grouping](#new-formula-columnsgrouping)[](#new-formula-columnsgrouping "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Apply Formula(
    Columns( Group( :height, 2 ), Ref( "_relative_from_height" ) ),
    Formula( _relative_from_height * 2 ),
    Output( New Formula( "result", Group( "output group" ) ) )
);
```

#### [Simple New Formula Column](#simple-new-formula-column)[](#simple-new-formula-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Data Table( "Big Class" ) << Apply Formula(
    Columns( :height ),
    Formula( :height / 5 ),
    Output( New Formula )
);
```

### [Begin Data Update](#begin-data-update)[](#begin-data-update "Click to copy url")

**Syntax:** obj \<\< Begin Data Update

**Description:** Holds all Update messages until the End Data Update command is reached. This is useful for updating many cells without interruption. This applies only to changes in data cells.

``` jsl
dt = Open( "$SAMPLE_DATA/Central Limit Theorem.jmp" );
dt << Add Rows( 2000 );
dt << Distribution( Column( :"N=1"n, :"N=5"n, :"N=10"n ) );
Wait();
dt << Begin Data Update;
dt << Add Rows( 2000 );
dt << End Data Update;
```

### [Checksum](#checksum)[](#checksum "Click to copy url")

**Syntax:** obj \<\< Checksum( \< Version(version) \>, \< Include(flags) \>, \< Exclude(flags) \> )

**Description:** Compute the table's checksum. Available flags include: "ColData", "ColName", "ColDataType", "ColModelingType", "ColFormat", "ColInFormat", "ColFormatWidth", "ColAttributes", "ColProperties", "ColListCheck", "ColRangeCheck", "ColCompact", "ColLabel", "ColHidden", "ColExclude", "ColSelection", "ColState", "ColDisplayWidth", "TableVariables", "TableScripts", "RowExclude", "RowHidden", "RowLabel", "RowColor", "RowMarker", "RowSelection", "RowState"

**JMP Version Added:** 18

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Checksum();
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Checksum( Exclude( "ColData" ) );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Checksum( Include( "ColData", "ColAttributes" ) );
```

**Example 4**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
flags = {"ColData", "ColAttributes"};
dt << Checksum( Include( flags ) );
```

### [Clear Cell Colors](#clear-cell-colors)[](#clear-cell-colors "Click to copy url")

**Syntax:** obj \<\< Clear Cell Colors

**Description:** Clear the cell color of the selected columns. If no columns are selected, cell colors of all columns are cleared.

**JMP Version Added:** 15

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:age << Color Cells( "Red" );
a = {1, 3, 5};
b = {2, 4, 6};
:height << color cells( {{"Red", a}, {"blue", b}} );
:weight << color cells( {{"blue", a}} );
Wait( 2 );
dt << Clear cell colors( {:height, :age} );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:age << Color Cells( "Red" );
a = {1, 3, 5};
b = {2, 4, 6};
:height << color cells( {{"Red", a}, {"blue", b}} );
:weight << color cells( {{"blue", a}} );
Wait( 2 );
dt << Clear cell colors();
```

### [Clear Column Selection](#clear-column-selection)[](#clear-column-selection "Click to copy url")

**Syntax:** obj \<\< Clear Column Selection

**Description:** Clears the column selection in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Go To( :BP 12F );
Wait( 2 );
dt << Clear Column Selection();
```

### [Clear Edit Lock](#clear-edit-lock)[](#clear-edit-lock "Click to copy url")

**Syntax:** obj \<\< Clear Edit Lock( \[ \<"Modify Cells"\>, \<"Add rows"\>, \<"Add Columns"\>, \<"Delete Rows"\>, \<"Delete Columns"\>\] )

**Description:** Allow specified operations on the data table which were previously disallowed.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Edit Lock( "Modify Cells", "Add Rows", "Delete Columns" );
:age << set selected( 1 );
:height << set selected( 1 );
Wait( 2 );
dt << Clear Edit Lock( "Delete Columns" );
```

### [Clear Properties Selection](#clear-properties-selection)[](#clear-properties-selection "Click to copy url")

**Syntax:** obj \<\< Clear Properties Selection( { property1, property2, ... )

**Description:** Deselect the specified table properties, where the list can be a list of property name or indices to the properties. If no list is given, deselect all the selected properties.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
list = {"Bivariate", "Logistic"};
proplist = dt << Select Properties();
Wait( 1 );
dt << clear properties selection( list );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
list = {"Bivariate", "Logistic"};
proplist = dt << Select Properties();
Wait( 1 );
dt << clear properties selecction();
```

### [Clone](#clone)[](#clone "Click to copy url")

**Syntax:** dt \<\< Clone( \< Table Name(name) \>, \< Copy Formulas(1\|0) \>, \< Eval Formulas(1\|0) \> )

**Description:** Create a copy of the data table

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dtClone = dt << Clone;
```

### [Close Data Grid](#close-data-grid)[](#close-data-grid "Click to copy url")

**Syntax:** obj \<\< Close Data Grid

**Description:** Close or open the data grid.

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Close Data Grid( 1 );
```

### [Close Side Panels](#close-side-panels)[](#close-side-panels "Click to copy url")

**Syntax:** obj \<\< Close Side Panels

**Description:** Close or open the data table's side panels.

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Close Side Panels( 1 );
```

### [Close summary panels](#close-summary-panels)[](#close-summary-panels "Click to copy url")

**Syntax:** obj \<\< Close summary panels

**Description:** Close or open the data table's summary panels.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Close Summary Panels( 1 );
```

### [Cluster](#cluster)[](#cluster "Click to copy url")

**Syntax:** obj \<\< Cluster

### [Collapse All Column Groups](#collapse-all-column-groups)[](#collapse-all-column-groups "Click to copy url")

**Syntax:** obj \<\< Collapse All Column Groups

**Description:** Collapses all column groups

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Group Columns( "Monday", BP 8M, 3 );
dt << Group Columns( "Wednesday", BP 8W, 3 );
dt << Group Columns( "Friday", BP 8F, 3 );
dt << Expand All Column Groups;
Wait( 2 );
dt << Collapse All Column Groups;
```

### [Column Filter](#column-filter)[](#column-filter "Click to copy url")

**Syntax:** obj \<\< Column Filter

**Description:** Retrieves object to manipulate active column filter for the table.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Lipid Data.jmp" );
dt << Expand All Column Groups;
dt:sex << Hide( 1 );

// Use immediately
dt << Column Filter( Column Name( "Weight|Wt", Regular Expression( 1 ) ) );
dt << Column Filter( Tags( {"Blood Measurements", "Good Measure"} ) );
dt << Column Filter( Tags( {"Blood Measurements", "Good Measure"}, Intersection( 1 ) ) );
dt << Column Filter( Column Name( "3" ), Tags( {"Blood Measurements"} ) );
dt << Column Filter( Clear );

// Return an object and send messages later
cf = dt << Column Filter;
cf << Column Name( "3yr" );
cf << Get Script;

// Related to (can also send to object)
dt << Show Hidden Columns in Columns List( 0 );
dt << Apply Columns List Filter to Data Grid( 0 );
```

### [Column Switcher](#column-switcher)[](#column-switcher "Click to copy url")

**Syntax:** obj \<\< Column Switcher(column reference, {column reference, ...}, \< Title(title) \>, \< Close Outline(0\|1) \>, \< Retain Axis Settings(0\|1) \>, \< Layout(0\|1) \>)

**Description:** Creates a standalone column switcher

**JMP Version Added:** 16

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Process Measurements.jmp" );
dt << Column Switcher(
    :Process 1,
    {:Process 1, :Process 3, :Process 4, :Process 5, :Process 6, :Process 7}
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "Bivariate",
    H List Box(
        cs = dt << Column Switcher( :age, {:age, :weight} ),
        V List Box(
            female = Bivariate( Y( :age ), X( :height ), Where( :sex == "F" ) ),
            male = Bivariate( Y( :age ), X( :height ), Where( :sex == "M" ) )
        )
    )
);
cs << Link Platform( female );
cs << Link Platform( male );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "Bivariate",
    H List Box(
        cs = dt << Column Switcher( :age, {:age, :weight} ),
        b = Bivariate( Y( :age ), X( :height ), by( :sex ) )
    )
);
cs << Link Platform( b[1] );
cs << Link Platform( b[2] );
```

### [Combine Columns](#combine-columns)[](#combine-columns "Click to copy url")

**Syntax:** obj \<\< Combine Columns

**Description:** Combine several columns into a single column, with each source column's values separated by the given delimiter.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
dt << Combine Columns(
    delimiter( "," ),
    Columns(
        :Brush After Waking Up, :Brush After Meal, :Brush Before Sleep, :Brush Another Time
    ),
    Selected Columns are Indicator Columns( 1 ),
    Column Name( "When to Brush" )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
dt << Combine Columns(
    delimiter( "," ),
    Columns(
        :Brush After Waking Up, :Brush After Meal, :Brush Before Sleep, :Brush Another Time
    ),
    Column Name( "When to Brush" )
);
```

### [Compare Data Tables](#compare-data-tables)[](#compare-data-tables "Click to copy url")

**Syntax:** obj \<\< Compare Data Tables( Compare with( Data Table( name )), \<Compare table variables and scripts( 0\|1)\>, \<show window\>,\<Compare columns attributes and properties( 0\|1)\>, \<Compare data( 0\|1 )\>, \<Show difference summary(0\|1)\>, \<Show difference plot(0\|1)\> )

**Description:** Compares two open data tables and reports differences between data, as well as metadata.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
dt << compare data tables( compare With( Data Table( "Students2" ) ) );
```

### [Compress File When Saved](#compress-file-when-saved)[](#compress-file-when-saved "Click to copy url")

**Syntax:** obj \<\< Compress File When Saved( state=0\|1 )

**Description:** Compress the file when saving the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Compress File When Saved( 1 );
```

### [Compress Selected Columns](#compress-selected-columns)[](#compress-selected-columns "Click to copy url")

**Syntax:** obj \<\< Compress Selected Columns( { column1, column2, ...} )

**Description:** Compresses each column into the most compact form.

Character data will be 1-byte if there are fewer than 255 levels.

Numeric data will be 1-byte if the data is between -127 and 127.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Compress Selected Columns( {:Age, :sex, :Height, :Weight} );
```

### [Concatenate](#concatenate)[](#concatenate "Click to copy url")

**Syntax:** obj \<\< Concatenate( \<Private\>, \<Invisible\>, Data Table( name ), \<Data Table(name), ...\> \<Label( column )\>, \<Output Table( name ) \| Append to first table\>, \<Keep Formulas\>, \<Create Source Column\> )

**Description:** Combines rows from several data tables and creates a new data table or appends the rows to the first data table.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Trial1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Trial2.jmp" );
dt << Concatenate( Data Table( "Trial2" ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Students.jmp" );
dt1 = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
dt << Concatenate(
    Data Table( dt1 ),
    Data Table( dt2 ),
    "Append to first table",
    "Create source column"
);
```

### [Copy Column Properties](#copy-column-properties)[](#copy-column-properties "Click to copy url")

**Syntax:** obj \<\< Copy Column Properties( \<column 1 column 2, ...\> )

**Description:** Copies to the clipboard the column properties of selected columns into a list of separate lists of properties. Optionally, you can specify a list of source columns instead of pre-selecting them in the data table.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
dt << Select Columns( :MODULUS, :ELONG );
dt << Copy Column Properties;
New Window( "Script", Script Box( "//Try Paste here
                     " ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
dt << Copy Column Properties( {:MODULUS, :ELONG} );
New Window( "Script", Script Box( "//Try Paste here
                     " ) );
```

### [Copy Selected Properties](#copy-selected-properties)[](#copy-selected-properties "Click to copy url")

**Syntax:** obj \<\< Copy Selected Properties

**Description:** Copy the selected table properties to the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << select properties( {"Distribution", "Oneway"} );
proplist = dt << Copy Selected Properties();
New Window( "Script", Script Box( "//Try Paste here
                     " ) );
```

### [Copy Table Script](#copy-table-script)[](#copy-table-script "Click to copy url")

**Syntax:** obj \<\< Copy Table Script( \<"No data"\> )

**Description:** Copies a script to re-create the data table. The resultant script includes all the table scripts stored in the data table. Optionally, add the keyword "No Data" to omit data from the script.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Copy Table Script();
New Window( "Script", Script Box( "//Try Paste here
                     " ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Copy Table Script( "No Data" );
New Window( "Script", Script Box( "//Try Paste here
                     " ) );
```

### [Debug Script](#debug-script)[](#debug-script "Click to copy url")

**Syntax:** obj \<\< Debug Script( name )

**Description:** Debugs a named script stored as a property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Debug Script( "Distribution" );
```

### [Decision Tree](#decision-tree)[](#decision-tree "Click to copy url")

**Syntax:** obj \<\< Decision Tree

### [Define Tag](#define-tag)[](#define-tag "Click to copy url")

**Syntax:** Define Tag(\<name\>, \[Color(\<color\>)\], \[Symbol(\<symbol char\>)\], \[Description(\<text\>)\], \[Replace(\<existing tag name\>)\])

**Description:** Create or update a column tag definition on the table. If the tag doesn't exist, create it. Optionally assign color, symbol, and other attributes.

**JMP Version Added:** 19

#### [Color, Symbol, or None](#color-symbol-or-none)[](#color-symbol-or-none "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Define Tag( "ID1", Color( Red ) );
dt << Define Tag( "ID2", Symbol( "\!UD83D\!UDCCB" ) );
dt << Define Tag( "ID3" );
```

#### [New Tag](#new-tag)[](#new-tag "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Define Tag( "ID", Color( Blue ) );
```

#### [Replace](#replace)[](#replace "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Define Tag( "ID", Color( Red ) );
:height << Set Property( "Tags", {"ID"} );
dt << Define Tag( "Identifier", Replace( "ID" ), Color( Blue ) );
:height << Get Property( "Tags" );
```

### [Delete Columns](#delete-columns)[](#delete-columns "Click to copy url")

**Syntax:** obj \<\< Delete Columns( \<column\>, \<column\>, ... )

**Description:** Deletes the specified column(s). If no argument is specified, deletes selected columns in the data table.

**JMP Version Added:** 14

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:height << Set Selected;
Wait( 2 );
dt << Delete Columns();
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
dt << Delete Columns( :Height );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
cols = {"height", "weight"};
Wait( 2 );
dt << Delete Columns( cols );
```

### [Delete Filter View](#delete-filter-view)[](#delete-filter-view "Click to copy url")

**Syntax:** obj \<\< Delete Filter View( name \| obj )

**Description:** Delete the given filter view.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv dream = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
fv male = dt << New Filter View(
    "Male",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Sex ), Where( :Sex == "MALE" ) ) )
);
Wait( 1 );
dt << Delete Filter View( fv dream );
dt << Delete Filter View( "Male" );
```

### [Delete Scripts](#delete-scripts)[](#delete-scripts "Click to copy url")

**Syntax:** obj \<\< Delete Scripts( \<script\| {script 1, script 2, script 3, ...} \> )

**Description:** Deletes the specified scripts from the data table.

**JMP Version Added:** 14

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Table Script(
    "New Script",
    Distribution( Column( :Height, :Weight ), By( :sex ) )
);
Wait( 2 );
dt << Delete Scripts( "New Script" );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
list = {"Bivariate", "Logistic"};
Wait( 2 );
dt << Delete Scripts( list );
```

### [Delete Table Property](#delete-table-property)[](#delete-table-property "Click to copy url")

**Syntax:** obj \<\< Delete Table Property

**Description:** Alias for Delete Scripts.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Table Script(
    "New Script",
    Distribution( Column( :Height, :Weight ), By( :sex ) )
);
Wait( 2 );
dt << Delete Table Property( "New Script" );
```

### [Delete Table Variable](#delete-table-variable)[](#delete-table-variable "Click to copy url")

**Syntax:** obj \<\< Delete Table Variable( name )

**Description:** Deletes a table variable stored in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Table Variable( "Days", 42 );
Wait( 2 );
dt << Delete Table Variable( "Days" );
```

### [Delete Tag](#delete-tag)[](#delete-tag "Click to copy url")

**Syntax:** Delete Tag(\<tag\>\|{\<tag\>, \<tag\>, ...}, \[force(0\|1)

**Description:** Delete a tag from the table. Tags will not be deleted if any columns still use them, unless the Force(1) flag is provided.

**JMP Version Added:** 19

#### [Delete tag](#delete-tag_1)[](#delete-tag_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Define Tag( "ID" );
Wait( 3 );
dt << Delete Tag( "ID" );
```

#### [Force delete](#force-delete)[](#force-delete "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Define Tag( "ID" );
:height << Set Property( "Tags", {"ID"} );
Wait( 3 );
dt << Delete Tag( "ID", Force( 1 ) );
```

### [Deselect Column Group](#deselect-column-group)[](#deselect-column-group "Click to copy url")

**Syntax:** obj \<\< Deselect Column Group( name of group \| list of names )

**Description:** Deselect the column groups. If the column group is omitted, all column groups will be deselected.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << group columns( "xy", {:X, :y} );
dt << group columns( "pollutants", :Ozone :: :Lead );
dt << select column group();
Wait( 2 );
dt << deselect column group( "pollutants" );
```

### [Disable Undo](#disable-undo)[](#disable-undo "Click to copy url")

**Syntax:** obj \<\< Disable Undo( state=0\|1 )

**Description:** When the option is set, any operation on the data table cannot be undone.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << disable undo( 1 );
```

### [End Data Update](#end-data-update)[](#end-data-update "Click to copy url")

**Syntax:** obj \<\< End Data Update

**Description:** Sends all Update messages held since the Begin Data Update command was issued. This is useful for updating many cells without interruption. This applies only to changes in data cells.

``` jsl
dt = Open( "$SAMPLE_DATA/Central Limit Theorem.jmp" );
dt << Add Rows( 2000 );
dt << Distribution( Column( :"N=1"n, :"N=5"n, :"N=10"n ) );
Wait();
dt << Begin Data Update;
dt << Add Rows( 2000 );
dt << End Data Update;
```

### [Exclude Columns](#exclude-columns)[](#exclude-columns "Click to copy url")

**Syntax:** obj \<\< Exclude Columns( \< 0\|1 \> \| \< { column1, column2, ... } \> )

**Description:** Excludes the columns from any analysis run

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Exclude Columns( 1, {:Age, :Name} );
```

### [Exit Filter View](#exit-filter-view)[](#exit-filter-view "Click to copy url")

**Syntax:** obj \<\< Exit Filter View

**Description:** Return to the unfiltered view. If already in the unfiltered view, this has no effect.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
dt << New Filter View(
    "Dream",
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Wait( 1 );
dt << Exit Filter View;
```

### [Expand All Column Groups](#expand-all-column-groups)[](#expand-all-column-groups "Click to copy url")

**Syntax:** obj \<\< Expand All Column Groups

**Description:** Expands all column groups

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Group Columns( "Monday", BP 8M, 3 );
dt << Group Columns( "Wednesday", BP 8W, 3 );
dt << Group Columns( "Friday", BP 8F, 3 );
dt << Collapse All Column Groups;
Wait( 2 );
dt << Expand All Column Groups;
```

### [Fit Model](#fit-model)[](#fit-model "Click to copy url")

**Syntax:** Fit Model( Y( columns ), Effects( columns ), Personality( "Standard Least Squares" ) )

**Description:** Fits linear regression models, including analysis of variance, logistic regression, variance components, penalized regression, stepwise regression, MANOVA, and survival models.

``` jsl
dt = Open( "$SAMPLE_DATA/Drug.jmp" );
dt << Fit Model(
    Y( :y ),
    Effects( :Drug, :x ),
    Personality( "Standard Least Squares" ),
    Run Model()
);
```

### [Get Active Filter View](#get-active-filter-view)[](#get-active-filter-view "Click to copy url")

**Syntax:** fv = obj \<\< Get Active Filter View

**Description:** Get the active filter view. Returns a FilterView object.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
dt << New Filter View(
    "Dream",
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
fv active = dt << Get Active Filter View;
Show( fv active << Get Name );
```

### [Get All Columns As Matrix](#get-all-columns-as-matrix)[](#get-all-columns-as-matrix "Click to copy url")

**Syntax:** obj \<\< Get All Columns As Matrix

**Description:** Returns the data table as a matrix. Character columns are numbered according to the sorted levels, starting at 1.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
m = dt << Get All Columns As Matrix();
Show( m );
```

### [Get As Report](#get-as-report)[](#get-as-report "Click to copy url")

**Syntax:** obj \<\< Get As Report

**Description:** Returns a report of the data table.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
jmp_report = New Window( "Big Class",
    Text Box( "Big Class" ),
    H List Box( Outline Box( "Big Class", dt << Get As Report ) ), 

);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Where( :Age < 14 );
dt << Select Columns( :name, :age, :height );
jmp_report = New Window( "Big Class",
    Text Box( "Big Class" ),
    H List Box( Outline Box( "Big Class", dt << Get As Report ) ), 

);
```

### [Get Cell Height](#get-cell-height)[](#get-cell-height "Click to copy url")

**Syntax:** obj \<\< Get Cell Height

**Description:** Get a row's display height.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
ht = dt << Get Cell Height;
```

### [Get Column Group](#get-column-group)[](#get-column-group "Click to copy url")

**Syntax:** obj \<\< Get Column Group( name of column group \| list of names )

**Description:** Returns the list of the columns in the column group.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << group columns( "xy", {:X, :y} );
dt << group columns( "pollutants", :Ozone :: :Lead );
dt << get column group( "xy" );
```

### [Get Column Groups Names](#get-column-groups-names)[](#get-column-groups-names "Click to copy url")

**Syntax:** obj \<\< Get Column Groups Names

**Description:** Returns the names of the columns groups.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << group columns( "xy", {:X, :y} );
dt << group columns( "pollutants", :Ozone :: :Lead );
dt << get column groups names;
```

### [Get Column Names](#get-column-names)[](#get-column-names "Click to copy url")

**Syntax:** obj \<\< Get Column Names( \<Numeric\|Character\|RowState\>, \<Continuous\|Ordinal\|Nominal\>,\<String\> )

**Description:** Returns the column names in the data table. If the string keyword is used, strings are returned.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
n = dt << Get Column Names();
Show( n );
CNames = dt << Get Column Names( Continuous );
Show( CNames );
SNames = dt << Get Column Names( String );
Show( SNames );
```

### [Get Column Reference](#get-column-reference)[](#get-column-reference "Click to copy url")

**Syntax:** obj \<\< Get Column Reference( list of column names )

**Description:** Returns the column reference of the strings in the list

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
refList = dt << Get Column Reference( {"sex", "age"} );
Show( refList );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
a = {1, 3, 4};
refList = dt << Get Column Reference( a );
Show( refList );
```

### [Get Edit Lock](#get-edit-lock)[](#get-edit-lock "Click to copy url")

**Syntax:** obj \<\< Get Edit Lock

**Description:** Get the list of disallowed operations on the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Edit Lock( "Add Rows", "Delete Columns" );
Wait( 2 );
dt << Get Edit Lock();
```

### [Get Excluded Columns](#get-excluded-columns)[](#get-excluded-columns "Click to copy url")

**Syntax:** obj \<\< Get Excluded Columns

**Description:** Returns the currently excluded columns in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:Name << Exclude;
exCols = dt << Get Excluded Columns;
Show( exCols );
```

### [Get Excluded Rows](#get-excluded-rows)[](#get-excluded-rows "Click to copy url")

**Syntax:** obj \<\< Get Excluded Rows

**Description:** Returns the currently excluded rows in the data table. Prefer Where.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( 1 );
dt << Select Rows( 5 );
dt << Exclude();
r1 = dt << Get Excluded Rows();
r2 = Where( Excluded() );
Show( r1, r2 );
```

### [Get Filter View](#get-filter-view)[](#get-filter-view "Click to copy url")

**Syntax:** fv = obj \<\< Get Filter View( name \| \<\<Temporary \| \<\<Unfiltered )

**Description:** Get a filter view by name, or get one of the special filter views by using \<\<Temporary or \<\<Unfiltered. If a filter view by the given name does not exist, returns Empty().

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
fv dream = dt << Get Filter View( "Dream" );
Show( fv dream << Get Name );
Show( (dt << Get Filter View( <<Unfiltered )) << Get Name );
```

### [Get Filter Views](#get-filter-views)[](#get-filter-views "Click to copy url")

**Syntax:** { fv, ... } = obj \<\< Get Filter Views( \< Temporary(0\|1) \>, \< Unfiltered(0\|1) \> )

**Description:** Get a list of all filter views. By default, the temporary and unfiltered views are not included.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv dream = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
fvs = dt << Get Filter Views( Unfiltered( 1 ), Temporary( 1 ) );
Show( fvs << Get Name );
```

### [Get Header Height](#get-header-height)[](#get-header-height "Click to copy url")

**Syntax:** obj \<\< Get Header Height

**Description:** Get column header's display height

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
ht = dt << Get Header Height;
```

### [Get Hidden Columns](#get-hidden-columns)[](#get-hidden-columns "Click to copy url")

**Syntax:** obj \<\< Get Hidden Columns

**Description:** Returns the columns currently hidden in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:Weight << Hide;
hidCols = dt << Get Hidden Columns;
Show( hidCols );
```

### [Get Hidden Rows](#get-hidden-rows)[](#get-hidden-rows "Click to copy url")

**Syntax:** obj \<\< Get Hidden Rows

**Description:** Returns the currently hidden rows in the data table. Prefer Where.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( 1 );
dt << Select Rows( 5 );
dt << Hide();
r1 = dt << Get Hidden Rows();
r2 = Where( Hidden() );
Show( r1, r2 );
```

### [Get Label Columns](#get-label-columns)[](#get-label-columns "Click to copy url")

**Syntax:** obj \<\< Get Label Columns

**Description:** Returns the columns used to label rows.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
labelCols = dt << Get Label Columns;
Show( labelCols );
```

### [Get Labeled Rows](#get-labeled-rows)[](#get-labeled-rows "Click to copy url")

**Syntax:** obj \<\< Get Labeled Rows

**Description:** Returns the currently labeled rows in the data table. Prefer Where.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( 1 );
dt << Select Rows( 5 );
dt << Label();
r1 = dt << Get Labeled Rows();
r2 = Where( Labeled() );
Show( r1, r2 );
```

### [Get Lock](#get-lock)[](#get-lock "Click to copy url")

**Syntax:** obj \<\< Get Lock( state=0\|1 )

**Description:** Checks whether the data table is locked.

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
a = dt << get lock();
Show( a );
Wait( 1 );
dt << Lock Data Table( 1 );
a = dt << get lock();
Show( a );
```

### [Get MM SAS DATA Step for Formula Columns](#get-mm-sas-data-step-for-formula-columns)[](#get-mm-sas-data-step-for-formula-columns "Click to copy url")

**Syntax:** obj \<\< Get MM SAS DATA Step for Formula Columns

**Description:** Creates Model Manager SAS DATA step code corresponding to formula columns in a JMP data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "Ratio", Formula( :height / :weight ) );
dt << Get MM SAS Data Step for Formula Columns;
```

### [Get Name](#get-name)[](#get-name "Click to copy url")

**Syntax:** obj \<\< Get Name( \<"Ignore Extension"\> )

**Description:** Returns the display name of the data table. With the optional argument 'Ignore Extension', the command returns the name of the data table without the extension

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
n = dt << Get Name();
Show( n );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
n = dt << Get Name( "Ignore Extension" );
Show( n );
```

### [Get Path](#get-path)[](#get-path "Click to copy url")

**Syntax:** obj \<\< Get Path

**Description:** Returns the complete path of the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
path = dt << Get Path();
Show( path );
```

### [Get Property](#get-property)[](#get-property "Click to copy url")

**Syntax:** obj \<\< Get Property( name )

**Description:** Returns the named property in the data table as a script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = dt << Get Property( "Distribution" );
Show( s );
```

### [Get Row ID Width](#get-row-id-width)[](#get-row-id-width "Click to copy url")

**Syntax:** obj \<\< Get Row ID Width

**Description:** Get row ID area's display width

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
ht = dt << Get Row ID Width;
```

### [Get Row States](#get-row-states)[](#get-row-states "Click to copy url")

**Syntax:** obj \<\< Get Row States

**Description:** Returns a vector containing encoded row state values for every row in the data table. Note that encoded row state values cannot be used as a row state structure in row state functions like Color Of. See Example 2 for a way you can use the vector directly.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Cereal.jmp" );
rs = dt << Get Row States;
Show( rs );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Cereal.jmp" );
rs = dt << GetRowStates;
w = Marker Of( As Row State( rs[3] ) );
dt2 = Open( "$SAMPLE_DATA/Big Class.jmp" );
Row State( dt2, 5 ) = Marker State( w );
```

### [Get Rows Where](#get-rows-where)[](#get-rows-where "Click to copy url")

**Syntax:** obj \<\< Get Rows Where

**Description:** Returns the rows in the data table matching the where criteria. Prefer Where instead.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r1 = dt << Get Rows Where( :sex == "M" );
r2 = Where( :sex == "M" );
Show( r1, r2 );
```

### [Get SAS DATA Step for Formula Columns](#get-sas-data-step-for-formula-columns)[](#get-sas-data-step-for-formula-columns "Click to copy url")

**Syntax:** obj \<\< Get SAS DATA Step for Formula Columns

**Description:** Creates SAS DATA step code corresponding to formula columns in a JMP data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "Ratio", Formula( :height / :weight ) );
dt << Get SAS Data Step for Formula Columns;
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script( \<script name\> )

**Description:** Returns the requested script. If the script name is omitted, returns a text representation of the data table together with all scripts stored in the data.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = dt << Get Script;
New Window( "Script", Script Box( Char( Name Expr( s ) ) ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = dt << Get Script( "Distribution" );
```

### [Get Script Group](#get-script-group)[](#get-script-group "Click to copy url")

**Syntax:** obj \<\< Get Script Group( name of script group )

**Description:** Returns the list of scripts in the group.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << group scripts( "VL", {"Set Sex Value Labels", "Set Age Value Labels"} );
gb = dt << get script group( "GB" );
Wait( 1 );
dt << run script( gb[2] );
```

### [Get Script Groups Names](#get-script-groups-names)[](#get-script-groups-names "Click to copy url")

**Syntax:** obj \<\< Get Script Groups Names

**Description:** Returns the list of names of script groups.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << group scripts( "VL", {"Set Sex Value Labels", "Set Age Value Labels"} );
gb = dt << get script groups names;
```

### [Get Scroll Locked Columns](#get-scroll-locked-columns)[](#get-scroll-locked-columns "Click to copy url")

**Syntax:** obj \<\< Get Scroll Locked Columns

**Description:** Returns the columns currently locked from scrolling in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:Name << Scroll Lock;
lockCols = dt << Get Scroll Locked Columns;
Show( lockCols );
```

### [Get Selected Columns](#get-selected-columns)[](#get-selected-columns "Click to copy url")

**Syntax:** obj \<\< Get Selected Columns

**Description:** Returns the names of the selected columns in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Go To( :weight );
names = dt << Get Selected Columns;
Show( names );
```

### [Get Selected Properties](#get-selected-properties)[](#get-selected-properties "Click to copy url")

**Syntax:** obj \<\< Get Selected Properties( \<{list of properties}\> )

**Description:** Get the selected table properties (variable and scripts) into a list. Instead of selecting, you can use an optional list to specify the properties to get.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Properties( {2, 4} );
proplist = dt << Get Selected Properties();
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
proplist = dt << Get Selected Properties( {2, 4} );
```

### [Get Selected Rows](#get-selected-rows)[](#get-selected-rows "Click to copy url")

**Syntax:** obj \<\< Get Selected Rows

**Description:** Returns the currently selected rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( 1 );
dt << Select Rows( 5 );
r = dt << Get Selected Rows();
Show( r );
```

### [Get Table Script Names](#get-table-script-names)[](#get-table-script-names "Click to copy url")

**Syntax:** obj \<\< Get Table Script Names

**Description:** Returns the names of all the properties in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
names = dt << Get Table Script Names;
Show( names );
```

### [Get Table Variable](#get-table-variable)[](#get-table-variable "Click to copy url")

**Syntax:** obj \<\< Get Table Variable( name )

**Description:** Returns the value of a specified table variable in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Table Variable( "Days", 42 );
var = dt << Get Table Variable( "Days" );
Show( var );
```

### [Get Table Variable Names](#get-table-variable-names)[](#get-table-variable-names "Click to copy url")

**Syntax:** obj \<\< Get Table Variable Names

**Description:** Returns the names of all the variables in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Lung Cancer.jmp" );
names = dt << Get Table Variable Names;
Show( names );
```

### [Get Tagged Columns](#get-tagged-columns)[](#get-tagged-columns "Click to copy url")

**Syntax:** obj \<\< Get Tagged Columns( tag\|{tag1, tag2, ...}, \[Intersection\] )

**Description:** Returns the list of the columns matching the supplied tags. If intersection is requested, only the columns containing all listed tags are returned.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt:Ozone << setProperty( "Tags", {"Air Pollution Levels"} );
dt:CO << setProperty( "Tags", {"Air Pollution Levels"} );
dt:SO2 << setProperty( "Tags", {"Air Pollution Levels"} );
dt:NO << setProperty( "Tags", {"Air Pollution Levels"} );
dt:PM10 << setProperty( "Tags", {"Air Pollution Levels"} );
dt:Lead << setProperty( "Tags", {"Air Pollution Levels"} );
dt << Get Tagged Columns( "Air Pollution Levels" );
```

### [Get Transforms](#get-transforms)[](#get-transforms "Click to copy url")

**Syntax:** dt \<\< Get Transforms()

**Description:** Retrieve the list of transform columns associated with this data table.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Transform Column( "A", Formula( :B + 1 ) );
dt << Transform Column( "B", Formula( :height + 1 ) );
Show( dt << Get Transforms() );
dt << Delete Columns( {:A, :B} );
```

### [Get as Matrix](#get-as-matrix)[](#get-as-matrix "Click to copy url")

**Syntax:** obj \<\< Get as Matrix( \<list of columns by name\>, \<list of columns by number\>, \<column range\> )

**Description:** Returns the specified columns in the data table as a matrix. The default is all numeric columns.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
m = dt << Get As Matrix();
Show( m );
x = dt << GetAsMatrix( {4, 5} );
Show( x );
```

### [Group Columns](#group-columns)[](#group-columns "Click to copy url")

**Syntax:** obj \<\< Group Columns( first column, number ) obj \<\< Group Columns( {column1, column2, ...}) obj \<\< Group Columns(group name \| Path({\<a\>, \<b\>, ...}), {column1, column2, ...}) obj \<\< Group Columns( group name \| Path({\<a\>, \<b\>, ...}), first column, number )

**Description:** Groups a list of columns.

#### [Add to group](#add-to-group)[](#add-to-group "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
Wait( 1 );
theGroup = dt << Group Columns( "BP", :BP 8M :: :BP 8W );
Wait( 2 );
// add to theGroup
theGroup = dt << Group Columns( theGroup, {:BP 12W} );
```

#### [Nested group](#nested-group)[](#nested-group "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
Wait( 1 );
dt << Group Columns( Path( {"Groups", "BP8"} ), :BP 8M :: :BP 8W );
```

#### [Using count](#using-count)[](#using-count "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
Wait( 1 );
group = dt << Group Columns( BP 8M, 9 );
```

### [Group Scripts](#group-scripts)[](#group-scripts "Click to copy url")

**Syntax:** obj \<\< Group Scripts({ script1, script2, ...}) obj \<\< Group Scripts(group name \| Path({\<a\>, \<b\>, ...}), {script1, script1, ...})

**Description:** Group a list of scripts.

**JMP Version Added:** 14

#### [Nested group](#nested-group_1)[](#nested-group_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    Path( {"GB", "Sample Graphs"} ),
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
```

#### [Simple group](#simple-group)[](#simple-group "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
```

### [Has Column](#has-column)[](#has-column "Click to copy url")

**Syntax:** dt \<\< Has Column( name, \< Exact Match(1\|0) \> )

**Description:** Inquire whether the data table has a column with the given name.

**JMP Version Added:** 18

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Has Column( "weight" );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Show(
    dt << Has Column( "Weight" ),
    dt << Has Column( "Weight", Exact Match( 1 ) ),
    dt << Has Column( "a g e" ),
    dt << Has Column( "a g e", Exact Match( 1 ) )
);
```

### [Has data view](#has-data-view)[](#has-data-view "Click to copy url")

**Syntax:** obj \<\< Has data view

**Description:** Returns true if the data table has a visible window opened.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << Has Data View();
```

### [Hide Columns](#hide-columns)[](#hide-columns "Click to copy url")

**Syntax:** obj \<\< Hide Columns( \< 0\|1 \> \| \< { column1, column2, ... } \> )

**Description:** Hides the columns in the data grid

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Hide Columns( 1, {:Age, :Name} );
```

### [Is Dirty](#is-dirty)[](#is-dirty "Click to copy url")

**Syntax:** obj \<\< Is Dirty

**Description:** Inquire whether the data table has been modified.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
a = dt << is Dirty;
Show( a );
dt << add rows( 5 );
b = dt << is dirty;
Show( b );
```

### [Is Linked Subset](#is-linked-subset)[](#is-linked-subset "Click to copy url")

**Syntax:** obj \<\< Is Linked Subset

**Description:** Inquire whether the data table is a linked subset

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
linkedSubset = dt << Subset( All Rows, Link To Original Data Table( 1 ) );
subset = dt << Subset( All Rows );
Show( dt << Is Linked Subset, linkedSubset << Is Linked Subset, subset << Is Linked Subset );
```

### [JMP Query Builder](#jmp-query-builder)[](#jmp-query-builder "Click to copy url")

**Syntax:** obj \<\< JMP Query Builder

**Description:** Builds a query for one or more JMP data tables.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << JMP Query Builder();
```

### [Join](#join)[](#join "Click to copy url")

**Syntax:** obj \<\< Join( \<Private\>, \<Invisible\>,With( Data Table( name )), By Matching Columns( column1 = column2, ...), Selected( columns ), SelectedWith( columns ), \<Drop Multiples( 0\|1, 0\|1 )\>, \<Include nonmatches( 0\|1, 0\|1 )\>,\<Copy formula( 0\|1 )\>, \<Suppress Formula Evaluation\>, \<Update\>, \<Merge Same Name Columns\>, \<Preserve Main Table Order\> )

**Description:** Combines multiple data tables into one new data table. The data can be combined by row assignment, matching column values, or in a Cartesian fashion.

``` jsl
dt = Open( "$SAMPLE_DATA/Trial1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Little.jmp" );
dt << Join(
    With( Data Table( "Little" ) ),
    Select( :popcorn, :oil amt, :batch, :yield ),
    SelectWith( :yield ),
    By Matching Columns( :popcorn = :popcorn, :batch = :batch, :oil amt = :oil )
);
```

### [Journal](#journal)[](#journal "Click to copy url")

**Syntax:** obj \<\< Journal

**Description:** Makes a journal from the data table. Only the data grid is included, not notes, variables, or scripts.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Journal();
```

### [Journal Link](#journal-link)[](#journal-link "Click to copy url")

**Syntax:** dt \<\< Journal Link( \< Save( \<filepath\> ) \| Embed( ) \>, \< Button Name( "Ben") \> )

**Description:** Appends a data table link-button to a journal. Use embed() or save(), but not both. Embed() has no options. Save() option is similar to dt\<\<save(). Use ButtonName() to override the button label. Returns new link-button.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Journal Link(); // assumes the table can be saved at its current location; button gets name from table
dt << Journal Link( Embed() ); // embed JSL script to re-create table; button gets name from table
dt << Journal Link(
    Save( "$temp/DeleteMe1.jmp" ),
    ButtonName( "Fancy Name for Temporary File" )
);
// even more fancy...
button = dt << Journal Link( Save( "$temp/DeleteMe2.jmp" ), ButtonName( "" ) ); // no text name
button << UnderlineStyle( 0 ); // not using the link-style appearance
button << SetIcon( "DataTableFile" ); // add an icon
button << SibAppend( Text Box( "Pick Me!" ), "Horizontal" ); // append a label
// save it with a prompt...you can change the name in the save-as dialog...or cancel
dt << Journal Link( Save( "" ) ); // prompt for path and save table; button gets name from prompt
Close( dt, "NoSave" );
```

### [Last Modified](#last-modified)[](#last-modified "Click to copy url")

**Syntax:** obj \<\< Last Modified

**Description:** Returns the date of the last saved modification to the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
date = dt << Last Modified();
Show( date );
```

### [Lock Data Table](#lock-data-table)[](#lock-data-table "Click to copy url")

**Syntax:** obj \<\< Lock Data Table( state=0\|1 )

**Description:** Locks the data table so values cannot be edited or added.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Lock Data Table( 1 );
// Now try changing a value in the data table.
```

### [MSA Variability Chart](#msa-variability-chart)[](#msa-variability-chart "Click to copy url")

**Syntax:** obj \<\< MSA Variability Chart( Y( column ), X( columns ) )

**Description:** Displays a variability chart showing how a measurement varies across categories and performs analysis examining how the mean and variance change across the categories.

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/2 Factors Crossed.jmp" );
dt << Variability Chart( Y( :Measurement ), X( :Operator, :part# ) );
```

### [Make Indicator Columns](#make-indicator-columns)[](#make-indicator-columns "Click to copy url")

**Syntax:** obj \<\< Make Indicator Columns

**Description:** Convert a nominal or ordinal column to as many columns as the number of categories. The column names of the resultant columns are the categories of the source column. The values of the resultant columns are zeroes or ones.

``` jsl
dt = Open( "$SAMPLE_DATA/Animals.jmp" );
dt << Make Indicator Columns( columns( {:species, :season} ) );
```

### [Make RowState Handler](#make-rowstate-handler)[](#make-rowstate-handler "Click to copy url")

**Syntax:** rs = dt \<\< Make RowState Handler( function(a) )

**Description:** Creates a row state handler to the data table. The argument of the function holds the rows whose row states get changed.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
f = Function( {a}, Print( a ) );
rs = dt << make row state handler( f );
dt << Select Rows( 1 );
dt << Select Rows( 5 );
```

### [Make SAS DATA Step](#make-sas-data-step)[](#make-sas-data-step "Click to copy url")

**Syntax:** sd = dt \<\< Make SAS Data Step( ) sd = dt \<\< Make SAS Data Step( SaveJMPMetadata(true) )

**Description:** Returns the data table as a SAS DATA step.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
sd = dt << Make SAS Data Step();
Show( sd );
```

### [Make SAS DATA Step Window](#make-sas-data-step-window)[](#make-sas-data-step-window "Click to copy url")

**Syntax:** sd = dt \<\< Make SAS Data Step Window( ) sd = dt \<\< Make SAS Data Step Window( SaveJMPMetadata(true) )

**Description:** Opens a new window of type sas and creates a SAS DATA step from the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
sd = dt << Make SAS Data Step Window();
```

### [Merge Referenced Data](#merge-referenced-data)[](#merge-referenced-data "Click to copy url")

**Syntax:** obj \<\< Merge Referenced Data

**Description:** Makes the table stand-alone by merging the data from the source table to the referenced columns and unlinking them. The Link Reference property of the referencing columns is also removed.

``` jsl
dt1 = Open( "$SAMPLE_DATA\Pizza Profiles.jmp" );
dt2 = Open( "$SAMPLE_DATA\Pizza Responses.jmp" );
dt1:ID << Set Property( "Link ID", 1 );
dt2:Choice << Set Property( "Link Reference", Reference Table( dt1 ) );
dt2:Choice1 << Set Property( "Link Reference", Reference Table( dt1 ) );
dt2:Choice2 << Set Property( "Link Reference", Reference Table( dt1 ) );
dt2 << Merge Referenced Data();
```

### [Missing Data Pattern](#missing-data-pattern)[](#missing-data-pattern "Click to copy url")

**Syntax:** obj \<\< Missing Data Pattern( columns( columns ), \<Output Table( name )\> )

**Description:** Finds patterns of missing values in the data table and creates a table of each pattern and its frequency.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << Missing Data Pattern(
    columns( :POP, :Max deg. F Jan, :OZONE, :CO, :SO2, :NO, :PM10, :Lead )
);
```

### [Move Column Group](#move-column-group)[](#move-column-group "Click to copy url")

**Syntax:** obj \<\< Move Column Group( name of group \| Path({\<a\>, \<b\>, ...}), to first \| to last \| after(column) \| after(group) \| after(Path({\<a\>, \<b\>, ...})) )

**Description:** Move the column group to specified location. If the column group name is omitted, all groups are moved.

#### [After group](#after-group)[](#after-group "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << group columns( "xy", {:X, :y} );
dt << group columns( "pollutants", :Ozone :: :Lead );
dt << move column group( "Pollutants", after( "xy" ) );
```

#### [Move all](#move-all)[](#move-all "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << group columns( "xy", {:X, :y} );
dt << group columns( "pollutants", :Ozone :: :Lead );
dt << move column group( to first );
```

#### [To first](#to-first)[](#to-first "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << group columns( "xy", {:X, :y} );
dt << group columns( "pollutants", :Ozone :: :Lead );
dt << move column group( "xy", to first );
```

### [Move Script Group](#move-script-group)[](#move-script-group "Click to copy url")

**Syntax:** obj \<\< Move Script Group( name of group \| Path({\<a\>, \<b\>, ...}), to first \| to last \| after(script) \| after(group) \| after(Path({\<a\>, \<b\>, ...})) )

**Description:** Move the script group to specified location. If the script group name is omitted, all groups are moved.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << group scripts( "VL", {"Set Sex Value Labels", "Set Age Value Labels"} );
Wait( 1 );
dt << move script group( "VL", after( "Oneway" ) );
Wait( 1 );
dt << move script group( "GB", after( "VL" ) );
Wait( 1 );
dt << move script group( "VL", after( Path( {"GB"} ) ) );
Wait( 1 );
dt << move script group( to first );
```

### [Move Selected Scripts](#move-selected-scripts)[](#move-selected-scripts "Click to copy url")

**Syntax:** obj \<\< Move Selected Scripts( script\|list of scripts\|group\|Path({\<a\>, \<b\>, ...}), to first \| to last \| after(script) \| after(group) \| after(Path({\<a\>, \<b\>, ...})) )

**Description:** Move the scripts to specified location.

**JMP Version Added:** 14

#### [After group](#after-group_1)[](#after-group_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << Move Selected scripts( {"Logistic"}, after( "GB" ) );
```

#### [Move Group](#move-group)[](#move-group "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    Path( {"GB", "Graphs"} ),
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << Move Selected scripts( Path( {"GB", "Graphs"} ), after( "Contingency" ) );
```

#### [To first](#to-first_1)[](#to-first_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Move Selected scripts(
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"},
    to first
);
```

### [Move down](#move-down)[](#move-down "Click to copy url")

**Syntax:** obj \<\< Move down

**Description:** Replaces the values in the first row of the data table with the column names and replaces the column names with default sequencing names.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Move down;
```

### [Move up](#move-up)[](#move-up "Click to copy url")

**Syntax:** obj \<\< Move up

**Description:** Replaces the column names with the values in the first row of the data table.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Move up;
```

### [Move up and append](#move-up-and-append)[](#move-up-and-append "Click to copy url")

**Syntax:** obj \<\< Move up and append

**Description:** Replaces the column names by appending the values in the first row of the data table to the corresponding column names.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Move up and append;
```

### [New Data Box](#new-data-box)[](#new-data-box "Click to copy url")

**Syntax:** obj \<\< New Data Box( \< \<\<Enable Filter Views(0\|1) \> )

**Description:** Makes a data table view in a display box tree. Changes the current data table to the given data table. The optional Enable Filter Views argument controls whether the view allows filter views; the default is to allow them.

``` jsl
dtA = Open( "$SAMPLE_DATA/Big Class.jmp", invisible );
New Window( "school",
    H List Box(
        dtA << New Data Box(),
        Text Box(),
        dtA << Distribution(
            ContinuousDistribution( Column( :weight ) ),
            NominalDistribution( Column( :age ) )
        )
    )
);
dtA = 0;
```

### [New Data View](#new-data-view)[](#new-data-view "Click to copy url")

**Syntax:** obj \<\< New Data View

**Description:** Makes a new view of the data table. This view is linked to the original in that anything highlighted or changed will affect the original. This is useful when you need to scroll to different parts of the same table.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << New Data View();
```

### [New Filter View](#new-filter-view)[](#new-filter-view "Click to copy url")

**Syntax:** fv = dt \<\< New Filter View( \< name \>, \< Copy From(name\|obj) \>, \< Temporary(0\|1) \>, \< Active(0\|1) \>, \< DataFilter(expr) \>)

**Description:** Create a new filter view. The created FilterView object is returned. The new filter view will be active by default. If you do not name the filter view, it is temporary, unless you set Temporary to zero.

**JMP Version Added:** 19

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
dt << New Filter View(
    "Dream",
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
dt << New Filter View(
    "Dream Inverse",
    Data Filter(
        Data Filter(
            Inverse( 1 ),
            Add Filter( Columns( :Island ), Where( :Island == "Dream" ) )
        )
    )
);
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    Data Filter( Add Filter( Columns( :Sex ), Where( Is Missing( :Sex ) ) ) )
);
dt << New Filter View( "Unknown Sex", CopyFrom( fv ), Active( 0 ) );
```

### [New Script](#new-script)[](#new-script "Click to copy url")

**Syntax:** New Property( name, script ) New Script( name, script )

**Description:** Creates and sets a new property in the data table as a script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Script( "New Script", Distribution( Column( :Height, :Weight ), By( :sex ) ) );
```

### [New Table Variable](#new-table-variable)[](#new-table-variable "Click to copy url")

**Syntax:** obj \<\< New Table Variable( name, number )

**Description:** Creates and sets a new variable in the data table as a constant value. If there is an existing variable with the same name, a number is appended to the name of the new variable to make it unique. The similar command Set Table Variable is recommended for most cases.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Table Variable( "Days", 42 );
```

### [OC Curves](#oc-curves)[](#oc-curves "Click to copy url")

**Syntax:** obj \<\< OC Curves

**Description:** Creates a graph that plots the probability of not detecting a shift in process as a function of the size of the shift.

**JMP Version Added:** 16

### [Partition](#partition)[](#partition "Click to copy url")

**Syntax:** obj \<\< Partition( Y( column ), X( column(s) ) )

**Description:** Constructs a decision tree by recursively partitioning the data according to a relationship between the predictor and response values. Both the response and predictors can be either continuous or categorical.

``` jsl
dt = Open( "$SAMPLE_DATA/Diabetes.jmp" );
dt << Partition(
    Y( :Y ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Split Best( 3 )
);
```

### [Paste Column Properties](#paste-column-properties)[](#paste-column-properties "Click to copy url")

**Syntax:** obj \<\< Paste Column Properties

**Description:** Pastes from the clipboard multiple lists of column properties to multiple columns. Optionally, you can specify a list of target columns instead of selecting them in the data table.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
dt << Copy Column Properties( {:MODULUS, :ELONG} );
dt2 = New Table( "test it",
    New Column( "T1", numeric, continuous ),
    New Column( "T2", numeric, continuous ),
    New Column( "T3", numeric, continuous ),
    Add Rows( 10 )
);
dt2 << Paste Column Properties( {:T1, :T3} );
```

### [Recode](#recode)[](#recode "Click to copy url")

**Syntax:** obj \<\< Recode

**Description:** Recode the old values of selected columns to new values.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Go To( :weight );
dt << Recode;
```

### [Recode Column](#recode-column)[](#recode-column "Click to copy url")

**Syntax:** obj \<\< Recode Column(\<source column reference\>, {\<transform\>, ...}, \<Update Properties(0\|1)\>, \<By Word(Delimiters(\<chars\>)\>, Target Column(\<column reference\> \| \<column name\>))

**Description:** Apply the listed transformations to each value from the source column and store the result in the original column or specified target column. The By Word option splits supplied character data into smaller input values. Once the input values are determined, the transformations are applied to those values separately.

Special JSL variables are populated during the execution of the command:

    _rcNow is the current value of the input after the previous transformation(s).

    _rcOrig is the original value of the input.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = New Column( :age );
col << Data Type( "Character" );
dt << Recode Column(
    :age,
    {If( _rcNow >= 17, "Older", _rcNow >= 15, "Middle", "Younger" )},
    Target Column( col )
);
```

### [Rename Column Group](#rename-column-group)[](#rename-column-group "Click to copy url")

**Syntax:** obj \<\< Rename Column Group( oldname \| Path({\<a\>, \<b\>, ...}), newname )

**Description:** Rename the column group.

#### [Nested Group](#nested-group_2)[](#nested-group_2 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << group columns( Path( {"xy", "Cols"} ), {:X, :y} );
Wait( 1 );
dt << rename column group( Path( {"xy"} ), "XY" );
dt << rename column group( Path( {"XY", "Cols"} ), "Columns" );
```

#### [Simple Group](#simple-group_1)[](#simple-group_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << group columns( "xy", {:X, :y} );
dt << group columns( "pollutants", :Ozone :: :Lead );
Wait( 1 );
dt << rename column group( "xy", "coordinates" );
```

### [Rename Script Group](#rename-script-group)[](#rename-script-group "Click to copy url")

**Syntax:** obj \<\< Rename Script Group( oldname \| Path({\<a\>, \<b\>, ...}), newname )

**Description:** Rename the script group

**JMP Version Added:** 14

#### [Nested group](#nested-group_3)[](#nested-group_3 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    Path( {"GB", "Graphs"} ),
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << rename script group( Path( {"GB", "Graphs"} ), "My Graphs" );
```

#### [Simple group](#simple-group_2)[](#simple-group_2 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << rename script group( "GB", "GraphBuilders" );
```

### [Rename Table Property](#rename-table-property)[](#rename-table-property "Click to copy url")

**Syntax:** obj \<\< Rename Table Property( old name, new name )

**Description:** Renames the specified Table Property.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Script( "New Script", Distribution( Column( :Height, :Weight ), By( :sex ) ) );
Wait( 1 );
dt << Rename Table Property( "New Script", "Great Script" );
```

### [Rename Table Script](#rename-table-script)[](#rename-table-script "Click to copy url")

**Syntax:** obj \<\< Rename Table Script( old name, new name )

**Description:** Renames the specified Table Script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Script( "New Script", Distribution( Column( :Height, :Weight ), By( :sex ) ) );
Wait( 1 );
dt << Rename Table Script( "New Script", "Great Script" );
```

### [Rename Table Variable](#rename-table-variable)[](#rename-table-variable "Click to copy url")

**Syntax:** obj \<\< Rename Table Variable( old name, new name )

**Description:** Renames a specified Table Variable.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Table Variable( "Days", 42 );
Wait( 2 );
dt << Rename Table Variable( "Days", "Hours" );
```

### [Rerun Formulas](#rerun-formulas)[](#rerun-formulas "Click to copy url")

**Syntax:** obj \<\< Rerun Formulas

**Description:** Re-evaluates all column formulas in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Central Limit Theorem.jmp" );
dt << Add Rows( 100 );
dt << Rerun Formulas;
```

### [Reset Transforms](#reset-transforms)[](#reset-transforms "Click to copy url")

**Syntax:** dt \>\> Reset Transforms()

**Description:** When transform columns are accessed, they cache their data for future calls. This function removes that data. The data will be recreated if the column is accessed again.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Reset Transforms();
```

### [Revert](#revert)[](#revert "Click to copy url")

**Syntax:** obj \<\< Revert

**Description:** Reverts any changes to the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Row States(
    [33, 33, 33, 33, 33, 97, 97, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 768]
);
Wait( 2 );
dt << revert();
```

### [Run Formulas](#run-formulas)[](#run-formulas "Click to copy url")

**Syntax:** obj \<\< Run Formulas

**Description:** Performs all pending formula evaluations. Not all formulas will be evaluated.

``` jsl
dt = Open( "$SAMPLE_DATA/Central Limit Theorem.jmp" );
dt << Add Rows( 10000 );
dt << Run Formulas();
Distribution( Column( :"N=1"n, :"N=5"n, :"N=10"n ) );
```

### [Run Script](#run-script)[](#run-script "Click to copy url")

**Syntax:** obj \<\< Run Script( name )

**Description:** Runs a named script stored as a property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Run Script( "Distribution" );
```

### [Save](#save)[](#save "Click to copy url")

**Syntax:** obj \<\< Save( \<filepath\>, \<file type\> ) obj \<\< Save As( filepath, \<file type\> )

**Description:** Saves the data table to any supported format. Supported formats include .jmp, .xls, .xlsx, .txt, .csv, .tsv, .xpt, .v8xpt, .stx, .sqlite, .db, .sqlite3, and .db3. Some formats are supported only on Windows. See Using JMP for details.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Save( "$temp\deleteme Big Class.jmp" ); // explicit location
If( dt << Save( "" ),
    Write( "\!nsaved to " || (dt << GetPath) ),
    Write( "\!nsave canceled" )
); // prompt
dt << Save( "$temp\deleteme Big Class.csv" ); // convert to CSV format
Close( dt, "NoSave" );
```

### [Save As](#save-as)[](#save-as "Click to copy url")

**Syntax:** obj \<\< Save( \<filepath\>, \<file type\> ) obj \<\< Save As( filepath, \<file type\> )

**Description:** Saves the data table to any supported format. Supported formats include .jmp, .xls, .xlsx, .txt, .csv, .tsv, .xpt, .v8xpt, .stx, .sqlite, .db, .sqlite3, and .db3. Some formats are supported only on Windows. See Using JMP for details.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Save( "$temp\deleteme Big Class.jmp" ); // explicit location
If( dt << Save( "" ),
    Write( "\!nsaved to " || (dt << GetPath) ),
    Write( "\!nsave canceled" )
); // prompt
dt << Save( "$temp\deleteme Big Class.csv" ); // convert to CSV format
Close( dt, "NoSave" );
```

### [Save Database](#save-database)[](#save-database "Click to copy url")

**Syntax:** obj \<\< Save Database( connectInfo, TableName )

**Description:** Saves the data table back to a database.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Save Database( "Connect Dialog", "My_Class" );
```

### [Screen Predictors](#screen-predictors)[](#screen-predictors "Click to copy url")

**Syntax:** obj \<\< Screen Predictors

**Description:** This is an alias and old name for Predictor Screening

``` jsl
dt = Open( "$SAMPLE_DATA/Bands Data.jmp" );
obj = dt << Predictor Screening( Y( :Banding? ), X( Column Group( "Predictors" ) ) );
```

### [Select Column Group](#select-column-group)[](#select-column-group "Click to copy url")

**Syntax:** obj \<\< Select Column Group( name of group \| list of names )

**Description:** Select the column groups.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << group columns( "xy", {:X, :y} );
dt << group columns( "pollutants", :Ozone :: :Lead );
dt << select column group( "xy", "pollutants" );
```

### [Select Properties](#select-properties)[](#select-properties "Click to copy url")

**Syntax:** obj \<\< Select Properties( { property1, property2, ... )

**Description:** Select the specified table properties, where the list can be a list of property name or indices to the properties.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
proplist = dt << Select Properties( {2, 4} );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
proplist = dt << Select Properties( {"Bivariate", "Logistic"} );
```

### [Select Script Group](#select-script-group)[](#select-script-group "Click to copy url")

**Syntax:** obj \<\< Select Script Group( \<name of group \| { group1, group2, ...} \> )

**Description:** Select the script groups. If no script group is given, all groups are selected.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << group scripts( "VL", {"Set Sex Value Labels", "Set Age Value Labels"} );
Wait( 1 );
dt << select script group( "VL" );
```

### [Select Scripts](#select-scripts)[](#select-scripts "Click to copy url")

**Syntax:** obj \<\< Select Scripts( \<name of script \| { script1, script2, ...} \> )

**Description:** Select the named scripts.

**JMP Version Added:** 14

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << group scripts( "VL", {"Set Sex Value Labels", "Set Age Value Labels"} );
Wait( 1 );
dt << select scripts( {"Distribution", "Graph Builder Heat Map"} );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << group scripts( "VL", {"Set Sex Value Labels", "Set Age Value Labels"} );
Wait( 1 );
a = dt << get script group( "GB" );
dt << select scripts( a );
```

### [Select columns](#select-columns)[](#select-columns "Click to copy url")

**Syntax:** obj \<\< Select columns( \<column\>, \<column\>, ... )

**Description:** Select the specified columns. To select all columns, use the keyword 'All'.

**JMP Version Added:** 14

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
dt << Select Columns( :Height );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
dt << Select Columns( "All" );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
clist = {:Height, :Weight};
dt << Select Columns( clist );
```

### [Sequencing Variants Toolset](#sequencing-variants-toolset)[](#sequencing-variants-toolset "Click to copy url")

**Syntax:** obj \<\< Sequencing Variants Toolset

**Description:** Interface to Sequencing Variants Toolset Add-in Platform

### [Set Active Filter View](#set-active-filter-view)[](#set-active-filter-view "Click to copy url")

**Syntax:** obj \<\< Set Active Filter View( name \| obj )

**Description:** Set the active filter view

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Wait( 1 );
dt << Set Active Filter View( "Dream" );
```

### [Set Cell Height](#set-cell-height)[](#set-cell-height "Click to copy url")

**Syntax:** obj \<\< Set Cell Height( number )

**Description:** Set the display height of each data table cell.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Cell Height( 20 );
```

### [Set Dirty](#set-dirty)[](#set-dirty "Click to copy url")

**Syntax:** obj \<\< Set Dirty( state=0\|1 )

**Description:** Marks the data table as changed, even though no change has occurred. This is helpful for causing a prompt to save on closing.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Dirty();
```

### [Set Edit Lock](#set-edit-lock)[](#set-edit-lock "Click to copy url")

**Syntax:** obj \<\< Set Edit Lock( \[ \<"Modify Cells"\>, \<"Add rows"\>, \<"Add Columns"\>, \<"Delete Rows"\>, \<"Delete Columns"\>\] )

**Description:** Disallow specified operations on the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Edit Lock( "Add Rows", "Delete Columns" );
```

### [Set Header Height](#set-header-height)[](#set-header-height "Click to copy url")

**Syntax:** obj \<\< Set Header Height( number )

**Description:** Set column header's display height

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Header Height( 20 );
```

### [Set Label Columns](#set-label-columns)[](#set-label-columns "Click to copy url")

**Syntax:** obj \<\< Set Label Columns( column(s) )

**Description:** Assigns a label role to selected columns in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
Wait( 1 );
dt << Set Label Columns( :City, :State );
```

### [Set Matrix](#set-matrix)[](#set-matrix "Click to copy url")

**Syntax:** obj \<\< Set Matrix( \[ matrix with rows separated by commas \] )

**Description:** Creates a data table from a matrix.

``` jsl
dt = New Table( "B" );
dt << Set Matrix( [12 59 95, 12 61 123, 12 55 74, 12 66 145] );
```

### [Set Name](#set-name)[](#set-name "Click to copy url")

**Syntax:** obj \<\< Set Name( new TableName )

**Description:** Changes the name of the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Name( "New Class" );
```

### [Set Property](#set-property)[](#set-property "Click to copy url")

**Syntax:** obj \<\< Set Property( name, script )

**Description:** Creates and sets a new property in the data table as a script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Property( "New Script", Distribution( Column( :Height, :Weight ), By( :sex ) ) );
```

### [Set Row ID Width](#set-row-id-width)[](#set-row-id-width "Click to copy url")

**Syntax:** obj \<\< Set Row ID Width( number )

**Description:** Set row ID area's display width

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Row ID Width( 80 );
```

### [Set Row States](#set-row-states)[](#set-row-states "Click to copy url")

**Syntax:** obj \<\< Set Row States( \[state1, state2, ... stateN\] )

**Description:** Sets the Row States for all rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Row States(
    [33, 33, 33, 33, 33, 97, 97, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 768]
);
```

### [Set Scroll Lock Columns](#set-scroll-lock-columns)[](#set-scroll-lock-columns "Click to copy url")

**Syntax:** obj \<\< Set Scroll Lock Columns( column(s) )

**Description:** Locks selected columns in the data table from scrolling. To indicate that a column is locked, the background color changes.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << Set Scroll Lock Columns( :City );
```

### [Set Table Variable](#set-table-variable)[](#set-table-variable "Click to copy url")

**Syntax:** obj \<\< Set Table Variable( name, number )

**Description:** Creates and sets a new variable in the data table as a constant value. An existing variable with the same name will be overwritten.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Set Table Variable( "Days", 42 );
```

### [Show Header Filter Icons](#show-header-filter-icons)[](#show-header-filter-icons "Click to copy url")

**Syntax:** obj \<\< Show Header Filter Icons( state=0\|1 )

**Description:** Show or hide the filter icons on columns in the current filter view.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Lipid Data.jmp" );
dt << Show Header Filter Icons( 0 );
```

### [Show Header Graphs](#show-header-graphs)[](#show-header-graphs "Click to copy url")

**Syntax:** obj \<\< Show Header Graphs( state=0\|1 )

**Description:** Show or hide the header graphs in the data table display.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Lipid Data.jmp" );
dt << Show Header Graphs( 0 );
```

### [Show Header Groups](#show-header-groups)[](#show-header-groups "Click to copy url")

**Syntax:** obj \<\< Show Header Groups( state=0\|1 )

**Description:** Show or hide the column groups in the data table display.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Lipid Data.jmp" );
dt << Show Header Groups( 0 );
```

### [Show Header Statistics](#show-header-statistics)[](#show-header-statistics "Click to copy url")

**Syntax:** obj \<\< Show Header Statistics( state=0\|1 )

**Description:** Show or hide the header statistics in the data table display.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Lipid Data.jmp" );
dt << Show Header Statistics( 0 );
```

### [Show Header Tags](#show-header-tags)[](#show-header-tags "Click to copy url")

**Syntax:** obj \<\< Show Header Tags( state=0\|1 )

**Description:** Show or hide the column tags in the data table display.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Lipid Data.jmp" );
dt << Show Header Tags( 0 );
```

### [Show Hidden Columns In Columns List](#show-hidden-columns-in-columns-list)[](#show-hidden-columns-in-columns-list "Click to copy url")

**Syntax:** obj \<\< Show Hidden Columns In Columns List( state=0\|1 )

**Description:** Turn off to omit Hidden columns from the data table Columns list. These columns never show in the data grid.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << Hide Columns( 1, {:"pop- m"n, :Max deg. F Jan, :X, :Y} );
Wait( 1 );
dt << Show Hidden Columns In Columns List( 0 );
```

### [Show Transforms](#show-transforms)[](#show-transforms "Click to copy url")

**Syntax:** dt \<\< Show Transforms()

**Description:** Print information to the log about the transform columns associated with this data table and its platforms. This is informational and the format might change. It should not be parsed.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Transform Column( "A", Formula( :height + 1 ) );
dt << Show Transforms();
dt << Delete Columns( :A );
```

### [Sort](#sort)[](#sort "Click to copy url")

**Syntax:** obj \<\< Sort( \<Private\>, \<Invisible\>, \<Replace table\>, By( column ), Order( ascending\|descending ) )

**Description:** Creates a new data table that is sorted by specified columns in either ascending or descending order.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Sort( By( :name ), Order( Ascending ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Sort( replace table, By( :name ), Order( Ascending ) );
```

### [Split](#split)[](#split "Click to copy url")

**Syntax:** obj \<\< Split( Split( columns ), Split by( column ), \<Group(column)\>, \<Private\>\|\<Invisible\>, \<Remaining Columns( Keep All \| Drop All \| Drop( columns ) \| Keep( columns ) )\>, \<Copy formula( 0\|1 )\>, \<Suppress formula evaluation( 0\|1 )\>, \<Sort by Column Property\>, \<Output Table( "name" )\> )

**Description:** Creates a new data table that maps several rows of one column into one row in several columns.

``` jsl
dt = Open( "$SAMPLE_DATA/Restaurant Tips.jmp" );
:Day of Week << set property( "Row Order Levels", 1 );
dt << Split(
    Split By( :Day of Week ),
    Split( :Bill Amount ),
    Sort by Column Property,
    remaining columns( drop all )
);
```

### [Stack](#stack)[](#stack "Click to copy url")

**Syntax:** obj \<\< Stack( \<Private\>, \<Invisible\>, columns( columns ), \<Source Label Column( string )\>, \<Stacked Data Column( string )\>, \<Copy formula( 0\|1 )\>, \<Number of Series(n)\>, \<Contiguous\>, \<Drop All Other Columns(1) \| Name("Non-stacked columns")(Keep( col1, ... )) \| Name("Non-stacked columns")(Drop( col1, ... ))\>, \<Output Table( "name" )\>) )

**Description:** Creates a new data table with values from multiple columns stacked into a single column.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Dogs.jmp" );
dt << Stack(
    columns( :LogHist0, :LogHist1, :LogHist3, :LogHist5 ),
    Source Label Column( "Time" ),
    Stacked Data Column( "Log Hist" )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Stack(
    columns( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    ,
    Number of Series( 3 ),
    Contiguous,
    Source Label Column( "Day" ),
    Stacked Data Column( "BP" )
);
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Stack(
    columns( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    ,
    Number of Series( 3 ),
    Source Label Column( "Time" ),
    Stacked Data Column( "BP" )
);
```

### [Subscribe](#subscribe)[](#subscribe "Click to copy url")

**Syntax:** obj \<\< Subscribe( Key( \<"client"\> ), OnDeleteColumns\| OnAddColumns\| OnAddRows\| OnDeleteRows\| OnRenameColumn \| OnClose \| OnSave \| OnRename (function) )

**Description:** Subscribes to get messages regarding changes in the data table. Key is the subscription name, so that it can be referenced. The optional parameter, client, will trigger a close confirmation when a close is attempted on the data table. Function can either be the name of a previously defined function, or the function itself. On Close only requires one argument to the function, the data table. The other messages require an additional argument, either a list of columns or number of rows affected. Each subscription remains in effect until you unsubscribe.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Subscribe( "name1"("client"), On Close( Print( "Closing Data Table" ) ) );
f = Function( {dtab, oldname},
    Print( "oldname", oldname );
    Print( "new name", dtab << getname() );
);
fsave = Function( {dtab, newpathname},
    Print( "new path name", newpathname );
    Print( "new name", dtab << getname() );
);
dt << Subscribe( "name1", On Rename( f ) );
dt << Subscribe( "name1", On Save( fsave ) );
fcols = Function( {dtab, b},
    n = N Items( b );
    dtname = (dtab << getname());
    Print( dtname );
    Print( n );
    For( i = 1, i <= n, i++,
        colname = (b[i] << getname());
        Print( colname );
    );
);
dt << Subscribe( "name2", On Delete Columns( fcols ) ); 
//Try deleting a column, then close the data table.
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
f = Function( {dtab, col, oldname},
    Print( dtab << getname() );
    Print( "new column name", (col << getname()) );
    Print( "old name", oldname );
);
sub = dt << Subscribe( "", OnRenameColumn( f ) );
Column( dt, 1 ) << set name( "test" );
Wait( 1 );
dt << unsubscribe( sub, on rename column );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
delRowsFn = Function( {a, b, rows},
    dtname = (a << Get Name());
    Print( dtname );
    Print( b );
    Print Matrix( rows );
);
addRowsFn = Function( {a, b, insert},
    dtname = (a << Get Name());
    Print( dtname );
    Print( b );
    Print( insert );
);
dt << subscribe( "Test Delete", onDeleteRows( delRowsFn, 3 ) );
dt << subscribe( "Test Add", onAddRows( addRowsFn, 3 ) );
// Try deleting some rows and adding new ones.
```

### [Subset](#subset)[](#subset "Click to copy url")

**Syntax:** obj \<\< Subset( \<Private\>, \<Invisible\>, \<Selected columns\>, \<Columns(column list)\>, \<All rows \| Selected Rows \| Filtered Rows(where clause) \| Rows(\[number, number, ...\])\>, \<By(column list)\>, \<Sampling Rate(fraction)\>, \<Sample Size(integer)\>, \<Stratify(column list)\>, \<Link to original data table(0\|1)\>, \<Copy formula(0\|1)\>, \<Suppress Formula Evaluation\>, \<Keep by columns\> )

**Description:** Creates a new data table from the selected rows and columns of the source data table. You can also randomly select rows to subset.

#### [By](#by)[](#by "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Subset( By( :sex ), Keep by columns );
```

#### [Filtered Rows](#filtered-rows)[](#filtered-rows "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Subset( Filtered Rows( :age == 14 & Contains( :name, "E" ) ) );
```

#### [Rows](#rows)[](#rows "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Subset( Rows( [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40] ) );
```

#### [Stratified Sample](#stratified-sample)[](#stratified-sample "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Subset( Sample Size( 10 ), Stratify( :sex ) );
```

### [Summary](#summary)[](#summary "Click to copy url")

**Syntax:** obj \<\< Summary( \<Private\>, \<Invisible\>, FREQ(column \| "none"), WEIGHT(column \| "none"),Group( columns ),Subgroup(columns), \<N (column)\>, \<Mean( column )\>, \<Std Dev( column )\>, \<Min( column )\>, \<Max( column )\>, \<Range( column )\>, \<Sum( column )\>, \<CV( column )\>...,Include marginal statistics, Link to original data table (0\|1),statistics column name format( "stat(column)" \| "column" \| "stat of column" \| "column stat" \| "stat") )

**Description:** Creates a new data table of summary statistics. If specified, there is a row for each level of a grouping variable or each combination of levels of multiple grouping variables.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Summary(
    Group( :Age ),
    subgroup( :sex ),
    Mean( :Height ),
    Include marginal statistics
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Summary(
    Group( :Age ),
    Mean( :Height ),
    statistics column name format( "stat of column" )
);
```

### [Suppress Formula Eval](#suppress-formula-eval)[](#suppress-formula-eval "Click to copy url")

**Syntax:** obj \<\< Suppress Formula Eval( state=0\|1 )

**Description:** Suppresses or enables formula evaluation. This is useful for faster adding of rows, running multiple analyses, and sorting.

``` jsl
dt = Open( "$SAMPLE_DATA/Central Limit Theorem.jmp" );
dt << Add Rows( 2000 );
dt << Suppress Formula Eval( 1 );
dt << Add Rows( 2000 );
dt << Suppress Formula Eval( 0 );
```

### [Text to Columns](#text-to-columns)[](#text-to-columns "Click to copy url")

**Syntax:** obj \<\< Text to Columns( delimiters(\<"separator"\>, \<TAB\>, \<NEWLINE\>), columns(column1, column2, ...) )

**Description:** Convert a column of strings with embedded delimiter into separate columns. The resultant columns can be indicator columns. Delimiters can be any character, the key word TAB, or the key word NEWLINE.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
dt << Text To Columns( delimiter( "," ), columns( :Brush Delimited ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
dt << Text To Columns(
    delimiter( "," ),
    columns( :Brush Delimited ),
    Make Indicator Columns( 1 )
);
```

### [Torch Deep Learning](#torch-deep-learning)[](#torch-deep-learning "Click to copy url")

**Syntax:** obj \<\< Torch Deep Learning

**Description:** Interface to Torch Deep Learning Add-in Platform

### [Transform Column](#transform-column)[](#transform-column "Click to copy url")

**Syntax:** dt \<\< Transform Column(\<name\>, Formula(\<expression\>), \[Replace(0\|1)\], \[Private(0\|1)\], \[Random Seed(\<n\>)\], \[Numeric\|Character\|Expression\], \[Continuous\|Nominal\|Ordinal\|Unstructured Text\], \[column properties\]

**Description:** Create a transform column associated with the target table. The transform column can be accessed like a real column.

    Name: Name of the column

    Formula: The formula that defines the data in the transform column

    Replace: With this flag, a transform defined with the same name as an existing transform will replace the existing transform. Without this flag, the existing transform will be returned if it is equivalent; otherwise the name of the new column will be changed to be distinct.

    Private: With this flag, the column will not show up in column selector lists

    Data type: Optionally specify the data type. If not specified, it will be inferred from the first row.

    Modeling type: Optionally specify the modeling type. If not specified, the default for the data type will be used

    Column Properties: These are any standard column properties you wish to set. You can also set them on the column after it is created.

**JMP Version Added:** 16

#### [Nested](#nested)[](#nested "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Transform Column( "A", Formula( :B + 1 ) );
dt << Transform Column( "B", Formula( :height + 1 ) );
Show( :A[1] );
dt << Delete Columns( {:A, :B} );
```

#### [Random](#random)[](#random "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Transform Column( "Predictable", Formula( Random Uniform() ), Random Seed( 314 ) );
dt << Transform Column( "Random", Formula( Random Uniform() ) );
Show( :Predictable[1], :Random[1] );
dt << Delete Columns( {:Predictable, :Random} );
```

#### [Simple](#simple_1)[](#simple_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Transform Column( "A", Formula( :height + 1 ) );
Show( :A[1] );
dt << Delete Columns( :A );
```

### [Transpose](#transpose)[](#transpose "Click to copy url")

**Syntax:** obj \<\< Transpose( \<Private\>, \<Invisible\>,columns( columns ), By( column ), \<Label( column )\>, \<Output Table( name )\> )

**Description:** Creates a new data table from the source table where the rows and columns are interchanged.

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Transpose(
    columns( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    By( :Dose ),
    Label( :Subject )
);
```

### [Type 1 Gauge](#type-1-gauge)[](#type-1-gauge "Click to copy url")

**Syntax:** obj \<\< Type 1 Gauge( Y( column ) )

**Description:** Analyzes measurement systems on continuous data using the Type 1 Gauge method to evaluate the capability of a measurement process on one part.

``` jsl
dt = Open( "$SAMPLE_DATA/Variability Data/Type 1 Gauge MSA.jmp" );
dt << Type 1 Gauge(
    Y( :Y1, :Y2, :Y3 ),
    Type 1 Gauge Metadata(
        :Y1( Tolerance Range( 2 ), Reference( 50.014 ), Resolution( .001 ) ),
        :Y2( Tolerance Range( 6 ), Reference( 24.9 ), Resolution( .01 ) ),
        :Y3( Tolerance Range( 5 ), Reference( 10 ), Resolution( .0005 ) )
    )
);
```

### [Ungroup Columns](#ungroup-columns)[](#ungroup-columns "Click to copy url")

**Syntax:** obj \<\< Ungroup Columns( {column1, column2, ...} \| Column Group( group name ) )

**Description:** Ungroups a list of columns.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Group Columns( "Monday", BP 8M, 3 );
dt << Group Columns( "Wednesday", BP 8W, 3 );
dt << Group Columns( "Friday", BP 8F, 3 );
Wait( 2 );
dt << Ungroup Columns();
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Group Columns( "Monday", BP 8M, 3 );
dt << Group Columns( "Wednesday", BP 8W, 3 );
dt << Group Columns( "Friday", BP 8F, 3 );
Wait( 2 );
dt << Ungroup Columns( Column Group( "Monday" ) );
```

### [Ungroup Scripts](#ungroup-scripts)[](#ungroup-scripts "Click to copy url")

**Syntax:** obj \<\< Ungroup Scripts( name of script group \| list of scripts )

**Description:** Ungroup a list of scripts. If scripts are not given, selected scripts will be detached from its group. All of the groups will be removed from their grouping if no script is given and no script is selected.

**JMP Version Added:** 14

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << group scripts( "VL", {"Set Sex Value Labels", "Set Age Value Labels"} );
Wait( 1 );
dt << ungroup scripts( "VL" );
Wait( 1 );
dt << ungroup scripts( {"Graph Builder Line and Bar Charts", "Graph Builder Heat Map"} );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group scripts(
    "GB",
    {"Graph Builder Smoother Line", "Graph Builder Line and Bar Charts",
    "Graph Builder Line Chart", "Graph Builder Heat Map"}
);
dt << group scripts( "VL", {"Set Sex Value Labels", "Set Age Value Labels"} );
Wait( 1 );
dt << select scripts( {"Graph Builder Smoother Line", "Graph Builder Line Chart"} );
Wait( 1 );
dt << ungroup scripts();
```

### [Unsubscribe](#unsubscribe)[](#unsubscribe "Click to copy url")

**Syntax:** obj \<\< Unsubscribe( Key, OnDeleteColumns\| OnAddColumns\| OnAddRows\| OnDeleteRows\| OnClose \| OnColRename \| All )

**Description:** Cancel previous subscription to the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Subscribe( "myname", On Close( Print( "Closing Data table" ) ) );
dt << Unsubscribe( "myname", On Close );
```

### [Update](#update)[](#update "Click to copy url")

**Syntax:** obj \<\< Update( With( Data Table( name )), Match Columns( column1 = column2, ...), Selected( columns ), Add columns from Update table(\<ALL\>, \<NONE\>, \<{column1, column2, ...}\>), Replace columns in main table(\<ALL\>, \<NONE\>, \<{column1, column2, ...}\>), \<Ignore missing\> )

**Description:** Merges a table of updated data into the original data table by adding or replacing selected columns.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Trial1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Little.jmp" );
dt << Update(
    With( Data Table( "Little" ) ),
    Match Columns( :popcorn = :popcorn, :batch = :batch, :oil amt = :oil )
);
```

**Example 2**

``` jsl

dt1 = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt2 = New Table( "Little Class",
    Add Rows( 3 ),
    New Column( "name", Character, Nominal, Set Values( {"KATIE", "ALFRED", "HENRY"} ) ),
    New Column( "height", Continuous, Set Values( [999, 999, 999] ) ),
    New Column( "weight", Continuous, Set Values( [999, 999, 999] ) ),
    New Column( "RANK", Continuous, Set Values( [3, 1, 2] ) ),
    New Column( "CODE", Continuous, Set Values( [0, 1, 1] ) )
);
dt1 << Update(
    With( Data Table( "Little Class" ) ),
    Match Columns( :name = :name ),
    Add columns from Update table( {:RANK} ),
    Replace columns in Main Table( {:height} )
);
```

**Example 3**

``` jsl

dt1 = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt2 = New Table( "Little Class",
    Add Rows( 3 ),
    New Column( "name", Character, Nominal, Set Values( {"KATIE", "ALFRED", "HENRY"} ) ),
    New Column( "height", Continuous, Set Values( [999, 999, 999] ) ),
    New Column( "weight", Continuous, Set Values( [999, 999, 999] ) ),
    New Column( "RANK", Continuous, Set Values( [3, 1, 2] ) ),
    New Column( "CODE", Continuous, Set Values( [0, 1, 1] ) )
);
dt1 << Update(
    With( Data Table( "Little Class" ) ),
    Match Columns( :name = :name ),
    Add columns from Update table( {:RANK} )
);
```

### [Update From Database](#update-from-database)[](#update-from-database "Click to copy url")

**Syntax:** obj \<\< Update From Database( connectInfo )

**Description:** Updates the data in the table with data re-imported from the database.

``` jsl
dt = Open Database( "DSN=somedb; UID=userid;pwd=PW", "SELECT * FROM DB.TABLE" );
dt << Update From Database( "Connect Dialog" );
```

### [XGBoost](#xgboost)[](#xgboost "Click to copy url")

**Syntax:** obj \<\< XGBoost

**Description:** Experimental interface to XGBoost for stochastic gradient boosting predictive modeling.

### [set private](#set-private)[](#set-private "Click to copy url")

**Syntax:** obj \<\< set private( \<1\|0\> )

**Description:** Make the table private. A private table is omitted from the data table list and subscriptions.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Show( Get Data Table List() );
Wait( 1 );

dt << Set Private;
Show( Get Data Table List() );
Wait( 1 );

dt << Set Private( 0 );
Show( Get Data Table List() );
Wait( 1 );

Close( dt, No Save );
```

## [Column Scripting](#column-scripting)[](#column-scripting "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Add Column Properties](#add-column-properties)[](#add-column-properties "Click to copy url")

**Syntax:** obj \<\< Add Column Properties

**Description:** Adds properties to the selected column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Age << Add Column Properties( List Check( {17, 16, 15, 14, 13, 12} ) );
```

#### [Add From Row States](#add-from-row-states)[](#add-from-row-states "Click to copy url")

**Syntax:** obj \<\< Add From Row States

**Description:** Updates a row state column with any currently used row state changes that are not the default state.

``` jsl
dt = Open( "$SAMPLE_DATA/Birth Death.jmp" );
dt << New Column( "Row State Col", Row State, Copy from Row States );
dt << Select Rows( 1 );
dt << Select Rows( 5 );
dt << Exclude();
col = Column( "Row State Col" );
col << Add From Row States();
```

#### [Add To Row States](#add-to-row-states)[](#add-to-row-states "Click to copy url")

**Syntax:** obj \<\< Add To Row States

**Description:** Copies all row state values in a column that are not the default state to the currently used row state in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Pickles.jmp" );
col = Column( "Time Marker" );
col << Copy To Row States();
col[5] = Color State( "Red" );
Wait( 2 );
col << Add To Row States();
```

#### [Codes to Labels](#codes-to-labels)[](#codes-to-labels "Click to copy url")

**Syntax:** :col \<\< Codes To Labels(\<AssociativeArray\>\|\<ListOfAssignments\>)

**Description:** Make a column of character values using value labels corresponding to the original codes.

**JMP Version Added:** 17

**Example 1**

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
:age << Value Labels(
    {12 = "12!", 13 = "13!", 14 = "14!", 15 = "15!", 16 = "16!", 17 = "17!"}
);
:age << Codes to Labels;
```

**Example 2**

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
:sex << Labels to Codes( ["F" => 1, "M" => 2] );
:sex << Codes To Labels( [1 => "Female", 2 => "Male"] );
```

**Example 3**

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
:sex << Labels to Codes( ["F" => 1.5, "M" => 2.5] );
:sex << Codes To Labels( {1.5 = "Female", 2.5 = "Male"} );
```

#### [Color Cell by Value](#color-cell-by-value)[](#color-cell-by-value "Click to copy url")

**Syntax:** obj \<\< Color Cell by Value( state=0\|1 )

**Description:** Changes the display color for cells in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Age << Set Property(
    "Value Colors",
    {12 = -13977430, 13 = -3780930, 14 = -4157407, 15 = -13596965, 16 = -2210961, 17 =
    -10562523}
);
Wait( 1 );
:Age << Color Cell by Value( 1 );
```

#### [Color Cells](#color-cells)[](#color-cells "Click to copy url")

**Syntax:** obj \<\< Color Cells( color, \<row \| { row1, row2, ...} \> )

**Description:** Color the cells in the column with the specified color. If rows are not given, the same color is applied to the entire column.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Age << Color Cells( "Red" );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
a = {1, 3, 5};
:Age << Color Cells( "Red", a );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
a = {1, 3, 5};
b = {2, 4, 6};
:height << color cells( {{"Red", a}, {"blue", b}} );
```

#### [Compact](#compact)[](#compact "Click to copy url")

**Syntax:** :col \<\< Compact( \<1\|0\> )

**Description:** Changes a character column's internals so it only stores one copy of each value, potentially saving memory and speeding up some operations. The optional Save Format controls the format in which the column is saved. The condensed format is smaller and faster to load, but the table cannot be opened in JMP 17 and earlier. The Default format uses the save format preference.

**JMP Version Added:** 18

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Air Traffic.jmp" );
:Airline << Compact();
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Air Traffic.jmp" );
:Airline << Compact();
:Airline << Get Compact;
```

#### [Convert to Table Column](#convert-to-table-column)[](#convert-to-table-column "Click to copy url")

**Syntax:** obj \<\< Convert to Table Column

**Description:** Adds the transform column to the data table.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Transform Column( "New Col", Formula( 1 ) );
:NewCol << Convert to Table Column();
```

#### [Copy from Row States](#copy-from-row-states)[](#copy-from-row-states "Click to copy url")

**Syntax:** obj \<\< Copy from Row States

**Description:** Copies all row state values currently used in the data table to a column.

``` jsl
dt = Open( "$SAMPLE_DATA/Birth Death.jmp" );
dt << New Column( "Row State Col", Row State, Copy from Row States );
```

#### [Copy to Row States](#copy-to-row-states)[](#copy-to-row-states "Click to copy url")

**Syntax:** obj \<\< Copy to Row States

**Description:** Copies all row state values in a column to the currently used row state in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Pickles.jmp" );
col = Column( "Time Marker" );
Wait( 2 );
col << Copy To Row States();
```

#### [Data Type](#data-type)[](#data-type "Click to copy url")

**Syntax:** obj \<\< Data Type( "Numeric"\|"Character"\|"Expression"\|"Row State", \<Format("format string")\>, \<Input Format("format string")\>, \<1\|2\|4\>, \< \<\<Fail On Conversion Error \>, \< \<\<Return Failed Rows \> )

**Description:** Sets the data type for the column. Using the optional arguments, you can also set the format, input format, and the width in bytes if the column is numeric. Fail On Conversion Error aborts the data type change if any values fail to convert. This is especially useful when converting a character column to a numeric column. Return Failed Rows returns a list containing indices of the rows that failed to convert.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "Time",
    "Character",
    "Nominal",
    Set Values( {"13:32", "20:10", "20:12", "14:56"} )
);
Wait( 2 );
dt:Time << Set Data Type( "Numeric", Format( "h:m", 12 ), Input Format( "h:m" ) );
dt:Time << Set Modeling Type( "Continuous" );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
dt:Age << Set Data Type( "Character" );
dt:Height << Set Data Type( "Numeric", 2 );
```

**Example 3**

``` jsl
dt = New Table( "My Table",
    New Column( "col1",
        Character,
        "Nominal",
        Set Values( {"123", "456", "abc", "789", "", "def"} )
    )
);
r = dt:col1 << Set Data Type( "Numeric", <<Fail On Conversion Error, <<Return Failed Rows );
Show( r );
```

**Example 4**

``` jsl
dt = New Table( "My Table",
    New Column( "col1",
        Character,
        "Nominal",
        Set Values( {"123", "456", "abc", "789", "", "def"} )
    )
);
r = dt:col1 << Set Data Type( "Numeric", <<Return Failed Rows );
Show( r );
```

#### [Delete Formula](#delete-formula)[](#delete-formula "Click to copy url")

**Syntax:** obj \<\< Delete Formula

**Description:** Deletes any formula in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Bank Loan.jmp" );
:Time << Delete Formula;
```

#### [Delete Property](#delete-property)[](#delete-property "Click to copy url")

**Syntax:** obj \<\< Delete Property( property name )

**Description:** Deletes the named property from the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Bank Loan.jmp" );
:Time << Delete Property( "Spec Limits" );
```

#### [Eval Formula](#eval-formula)[](#eval-formula "Click to copy url")

**Syntax:** obj \<\< Eval Formula

**Description:** Evaluates the formula in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = New Column( "Ratio" );
col << Set Formula( :Height / :Weight );
col << Eval Formula;
```

#### [Format](#format)[](#format "Click to copy url")

**Syntax:** obj \<\< Format( "Best\|Fixed Dec...", \<width\>, \<dec\>, \<"Use Thousands Separator"\> ) obj \<\< Format( "mdy\|ddmmyy\|Long Date...", width ) obj \<\< Format( "Format Pattern", pattern ) obj \<\< Format("Currency", \<Country symbol\>, \<width\>, \<"Use Thousands Separator"\> ) obj \<\< Format("Use Thousands Separator" )

**Description:** Sets the format used for displaying data in the column. Available formats include all items in the Column Info dialog under format.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Height << Format( "Fixed Dec", 6, 3 );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/XYZ Stock Averages (plots).jmp" );
:Date << Format( "ddMonyyyy", 9 );
:DJI High << Format( "Currency" );
:DJI Close << Format( "best", "Use Thousands Separator", 10, 0 );
:DJI Low << Format( "Fixed Dec", "Use Thousands Separator", 10, 2 );
```

**Example 3**

``` jsl
dt = New Table( "hour24_times",
    Add Rows( 3 ),
    New Column( "time",
        Continuous,
        Format( "Format Pattern", "<hh24><:><mm><:><ss>" ),
        Set Values( {"01:23:45", "18:19:20", "23:45:01"} )
    )
);
```

#### [Formula](#formula)[](#formula "Click to copy url")

**Syntax:** obj \<\< Set Formula( formula ) obj \<\< Formula( formula )

**Description:** Sets the formula in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = New Column( "Ratio" );
col << Set Formula( :Height / :Weight );
```

#### [Get Column Properties](#get-column-properties)[](#get-column-properties "Click to copy url")

**Syntax:** obj \<\< Get Column Properties

**Description:** Copies all properties defined in the selected columns.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
:HARDNESS << Get Column Properties();
```

#### [Get Compact](#get-compact)[](#get-compact "Click to copy url")

**Syntax:** obj \<\< Get Compact

**Description:** Is compact set on the column

**JMP Version Added:** 18

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Air Traffic.jmp" );
Show( :Airline << Get Compact );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Air Traffic.jmp" );
:Airline << Compact();
Show( :Airline << Get Compact );
```

#### [Get Data Table](#get-data-table)[](#get-data-table "Click to copy url")

**Syntax:** obj \<\< Get Data Table

**Description:** Gets the column's data table.

**JMP Version Added:** 14

``` jsl
dt1 = Open( "$SAMPLE_DATA/Big Class.jmp" );
c = Column( dt1, "Age" );
Show( c << Get Name, c << Get Data Table );
```

#### [Get Data Type](#get-data-type)[](#get-data-type "Click to copy url")

**Syntax:** obj \<\< Get Data Type( \<"English"\> )

**Description:** Returns the data type for the column. If the keyword "English" is omitted, the data type is returned in the language that JMP is running in.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
which = dt:Age << Get Data Type;
Show( which );
```

#### [Get Data Type Length](#get-data-type-length)[](#get-data-type-length "Click to copy url")

**Syntax:** obj \<\< Get Data Type Length( \<English\> )

**Description:** Returns the data type and data length of the column. Only the data type is returned if the data length is not fixed, like most character columns.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
which = dt:Age << Get Data Type Length;
Show( which );
```

**Example 2**

``` jsl
dt = New Table( "Little Class",
    Add Rows( 3 ),
    New Column( "name", Character( 8 ), Nominal, Set Values( {"KATIE", "CAROL", "MARTHA"} ) ),
    New Column( "Age", Numeric( 2 ), Set Values( [12, 14, 16] ) )
);
nameTypeLength = dt:Name << Get Data Type Length;
ageTypeLength = dt:Age << Get Data Type Length;
Show( nameTypeLength, ageTypeLength );
```

#### [Get Display Width](#get-display-width)[](#get-display-width "Click to copy url")

**Syntax:** obj \<\< Get Display Width

**Description:** Get column's display width.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 0 );
w = :Height << Get Display Width;
```

#### [Get Excluded](#get-excluded)[](#get-excluded "Click to copy url")

**Syntax:** obj \<\< Get Excluded

**Description:** Returns 1 if the column is excluded

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = :Weight << Get excluded;
Show( s );
```

#### [Get Field Width](#get-field-width)[](#get-field-width "Click to copy url")

**Syntax:** obj \<\< Get Field Width

**Description:** Returns the field width used for displaying data in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
width = :Height << Get Field Width;
Show( width );
```

#### [Get Format](#get-format)[](#get-format "Click to copy url")

**Syntax:** obj \<\< Get Format

**Description:** Returns the format for the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
f = :Height << Get Format;
Show( f );
```

#### [Get Formula](#get-formula)[](#get-formula "Click to copy url")

**Syntax:** obj \<\< Get Formula

**Description:** Returns the formula in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = New Column( "Ratio" );
col << Set Formula( :Height / :Weight );
col << Eval Formula;
result = col << Get Formula;
Show( result );
```

#### [Get Group Name](#get-group-name)[](#get-group-name "Click to copy url")

**Syntax:** obj \<\< Get Group Name

**Description:** Return the group name or path of the group containing this column, if any.

**JMP Version Added:** 19

**Nested Group**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Group Columns( "XYZ", :sex, 3 );
dt << Group Columns( Path( "XYZ", "Measures" ), :height, 2 );
Show( :height << Get Group Name );
```

**Simple Group**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Group Columns( :height, 2 );
Show( :height << Get Group Name );
```

#### [Get Header Background Color](#get-header-background-color)[](#get-header-background-color "Click to copy url")

**Syntax:** obj \<\< Get Header Background Color

**Description:** Get the header color

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:height << Set Header Background Color( "Light Red" );
Show( :height << Get Header Background Color );
```

#### [Get Header Chart Type](#get-header-chart-type)[](#get-header-chart-type "Click to copy url")

**Syntax:** obj \<\< Get Header Chart Type

**Description:** Gets the type of chart displayed in the data table column header.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Show( :height << Get Header Chart Type );
```

#### [Get Header Text Color](#get-header-text-color)[](#get-header-text-color "Click to copy url")

**Syntax:** obj \<\< Get Header Text Color

**Description:** Get the header text color

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:height << Set Header Text Color( "Dark Purple" );
Show( :height << Get Header Text Color );
```

#### [Get Hidden](#get-hidden)[](#get-hidden "Click to copy url")

**Syntax:** obj \<\< Get Hidden

**Description:** Returns 1 if the column is hidden

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = :Weight << Get hidden;
Show( s );
```

#### [Get Initial Data](#get-initial-data)[](#get-initial-data "Click to copy url")

**Syntax:** obj \<\< Get Initial Data

**Description:** Get the value or the expression used to initialize column's data.

``` jsl
dt = New Table( "MyDt" );
dt << Add Rows( 5 );
Column( dt, 1 ) << set initial data( Log( 1 ) );
Column( dt, 1 ) << get initial data;
```

#### [Get Input Format](#get-input-format)[](#get-input-format "Click to copy url")

**Syntax:** obj \<\< Get Input Format

**Description:** Returns the format used for inputting and storing the data for the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
f = :Date << Get Input Format;
Show( f );
```

#### [Get Labeled](#get-labeled)[](#get-labeled "Click to copy url")

**Syntax:** obj \<\< Get Labeled

**Description:** Returns 1 if the column is labeled

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = :Weight << Get labeled;
Show( s );
```

#### [Get List Check](#get-list-check)[](#get-list-check "Click to copy url")

**Syntax:** obj \<\< Get List Check

**Description:** Returns the List Check, if defined in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Movies.jmp" );
prop = :Type << Get List Check;
Show( prop );
```

#### [Get Lock](#get-lock_1)[](#get-lock_1 "Click to copy url")

**Syntax:** obj \<\< Get Lock

**Description:** Returns true if a column is locked.

``` jsl
dt = Open( "$SAMPLE_DATA/Cytometry.jmp" );
lock = :Prin1 << Get Lock;
Show( lock );
```

#### [Get Modeling Type](#get-modeling-type)[](#get-modeling-type "Click to copy url")

**Syntax:** obj \<\< Get Modeling Type( \<"English"\> )

**Description:** Returns the modeling type for the column. If the keyword "English" is omitted, the modeling type is returned in the language that JMP is running in.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
which = :Age << Get Modeling Type;
Show( which );
```

#### [Get Name](#get-name_1)[](#get-name_1 "Click to copy url")

**Syntax:** obj \<\< Get Name

**Description:** Returns the name of the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col name = Column( 4 ) << Get Name;
Show( col name );
```

#### [Get Properties List](#get-properties-list)[](#get-properties-list "Click to copy url")

**Syntax:** obj \<\< Get Properties List

**Description:** Get the list of names of all the properties for this column

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
:HARDNESS << Get Properties List();
```

#### [Get Property](#get-property_1)[](#get-property_1 "Click to copy url")

**Syntax:** obj \<\< Get Property( Notes\| Range Check\| List Check\| Missing Value Codes\| Value Labels\| Value Scores \| Value Order \| Value Colors\| Color Gradient\| Axis\| Units\| Response Limits\| Design Role\| Coding\| Mixture\| Factor Changes \| Spec Limits\| Control Limits\| Process Screening \| Sigma\| Process Capability Distribution\| MSA \| Distribution \| Time Frequency\| Map Role\| Super Categories \| Multiple Response \| Target Level \| Control Level\| Profit Matrix \| Expression Role \| Event Handler \| Link ID \| Link Reference \| Next In Hierarchy )

**Description:** Returns specific properties, if defined in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Bank Loan.jmp" );
prop = :Credit Check << Get Property( "Axis" );
Show( prop );
```

#### [Get Range Check](#get-range-check)[](#get-range-check "Click to copy url")

**Syntax:** obj \<\< Get Range Check

**Description:** Returns the Range Check, if defined in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Height << Range Check( LE LT( 48, 75 ) );
check = :Height << Get Range Check;
Show( check );
```

#### [Get Role](#get-role)[](#get-role "Click to copy url")

**Syntax:** obj \<\< Get Role( \<"English"\> )

**Description:** Returns the role for the column. If the keyword "English" is omitted, the role is returned in the language that JMP is running in.

``` jsl
dt = Open( "$SAMPLE_DATA/Penicillin.jmp" );
which = :Count << Get Role();
Show( which );
```

#### [Get Script](#get-script_1)[](#get-script_1 "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Returns the script to recreate the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = :Age << Get Script;
Show( s );
```

#### [Get Scroll Locked](#get-scroll-locked)[](#get-scroll-locked "Click to copy url")

**Syntax:** obj \<\< Get Scroll Locked

**Description:** Returns 1 if the column is scroll locked

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = :Weight << Get Scroll locked;
Show( s );
```

#### [Get Selected](#get-selected)[](#get-selected "Click to copy url")

**Syntax:** obj \<\< Get Selected

**Description:** Returns 1 if the column is selected.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = :Weight << Get Selected;
Show( s );
```

#### [Get Stored Values](#get-stored-values)[](#get-stored-values "Click to copy url")

**Syntax:** obj \<\< Get Stored Values

**Description:** Returns the values in the columns without Missing Values Codes conversion

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Height << Set Property( "Missing Value Codes", 65 );
valuesMatrix = :Height << Get Stored Values;
Show( valuesMatrix );
valuesList = :Height << GetStoredValues(
    Format(/* a numeric column will be list of character items if a format is supplied, see format function */
        "Currency",
        "EUR",
        2,
        <<use locale(
            0 /* ignore locale and use period for decimal.  the default is 1: use the locale. */
        )
    )
);
Show( valuesList );
```

#### [Get Use Value Labels](#get-use-value-labels)[](#get-use-value-labels "Click to copy url")

**Syntax:** obj \<\< Get Use Value Labels

**Description:** Returns the state of the Use Value Labels flag.

``` jsl
dt = Open( "$SAMPLE_DATA/CrabSatellites.jmp" );
flag = :Color << Get Use Value Labels;
Show( flag );
```

#### [Get Value Labels](#get-value-labels)[](#get-value-labels "Click to copy url")

**Syntax:** obj \<\< Get Value Labels

**Description:** Returns the value labels, if defined in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/CrabSatellites.jmp" );
values = :Color << Get Value Labels;
Show( values );
```

#### [Get Values](#get-values)[](#get-values "Click to copy url")

**Syntax:** obj \<\< Get Values

**Description:** Returns the values in the column.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
valuesMatrix = :Height << Get Values;
Show( valuesMatrix );
valuesList = :Height << GetValues(
    Format(/* a numeric column will be list of character items if a format is supplied, see format function */
        "Currency",
        "EUR",
        2,
        <<use locale(
            0 /* ignore locale and use period for decimal.  the default is 1: use the locale. */
        )
    )
);
Show( valuesList );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Height << Set Property( "Missing Value Codes", 65 );
valuesMatrix = :Height << Get Values;
Show( valuesMatrix );
valuesList = :Height << GetValues(
    Format(/* a numeric column will be list of character items if a format is supplied, see format function */
        "Currency",
        "EUR",
        2,
        <<use locale(
            0 /* ignore locale and use period for decimal.  the default is 1: use the locale. */
        )
    )
);
Show( valuesList );
```

#### [Ignore Errors](#ignore-errors)[](#ignore-errors "Click to copy url")

**Syntax:** obj \<\< Ignore Errors( state=0\|1 )

**Description:** Set the flag to ignore errors when a column formula is being evaluated

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = New Column( "Ratio" );
col << Set Formula( :Height / :Weight );
col << ignore errors( true );
```

#### [Input Format](#input-format)[](#input-format "Click to copy url")

**Syntax:** obj \<\< Input Format( format ) obj \<\< Input Format( "Format Pattern", pattern )

**Description:** Sets the format used for inputting and storing the data for the column. This is often used for date and time formats.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
:Date << Input Format( "ddmmyyyy" );
```

**Example 2**

``` jsl
dt = New Table( "duration_table",
    Add Rows( 3 ),
    New Column( "durations",
        Continuous,
        Format( "Format Pattern", "<Hour><:><mm><:><ss>" ),
        Input Format( "Format Pattern", "<Hour>h <mm>m <ss>s" ),
        Set Values( {"65h 43m 21s", "12h 34m 56s", "4h 32m 10s"} )
    )
);
```

#### [Is Transform Column](#is-transform-column)[](#is-transform-column "Click to copy url")

**Syntax:** obj \<\< Is Transform Column

**Description:** Returns 1 if the column is a transform column, 0 otherwise.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:height << Is Transform Column();
```

#### [IsTransformedOnSASExport](#istransformedonsasexport)[](#istransformedonsasexport "Click to copy url")

**Syntax:** obj \<\< IsTransformedOnSASExport

**Description:** Returns true if the data in the resulting SAS dataset for this column will be changed upon exporting to SAS. Note: This applies only to date columns, as dates are stored differently in SAS and JMP.

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
flag = :Date << Is Transformed On SAS Export;
Show( flag );
```

#### [Labels to Codes](#labels-to-codes)[](#labels-to-codes "Click to copy url")

**Syntax:** :col \<\< Labels to Codes(\<AssociativeArray\>\|\<ListOfAssignments\>)

**Description:** Make a column of numeric codes with value labels corresponding to the original character values.

**JMP Version Added:** 17

**Example 1**

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
:sex << Labels to Codes;
```

**Example 2**

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
:sex << Labels to Codes( ["F" => 10, "M" => 20] );
```

**Example 3**

``` jsl
dt = Open( "$Sample_Data/Big Class.jmp" );
:sex << Labels to Codes( {"F" = 10, "M" = 20} );
```

#### [Lock](#lock)[](#lock "Click to copy url")

**Syntax:** obj \<\< Lock

**Description:** Locks the column from any further changes.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Age << Lock( 1 );
```

#### [Preselect Role](#preselect-role)[](#preselect-role "Click to copy url")

**Syntax:** obj \<\< Preselect Role( "No Role"\|"X"\|"Y"\|"Weight"\|"Freq"\|"Validation" )

**Description:** Assigns a preselected role to the data table column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Weight << Preselect Role( "Y" );
```

#### [Remove Value Labels](#remove-value-labels)[](#remove-value-labels "Click to copy url")

**Syntax:** obj \<\< Remove Value Labels

**Description:** Removes any value labels defined in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/CrabSatellites.jmp" );
:Color << Remove Value Labels;
```

#### [Reset Transform](#reset-transform)[](#reset-transform "Click to copy url")

**Syntax:** obj \<\< Reset Transform

**Description:** Removes the cached data for the transform column. Accessing column data will rebuild the cache. Use this to reduce memory or to allow recalculation if the formula depends on external information.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
global:a = 2;
dt << Transform Column( "sqrt[height]", Formula( global:a * Sqrt( :height ) ) );
Show( :"sqrt[height]"n[1] );
global:a = 3;
:"sqrt[height]"n << Reset Transform();
Show( :"sqrt[height]"n[1] );
```

#### [Set Data Type](#set-data-type)[](#set-data-type "Click to copy url")

**Syntax:** obj \<\< Set Data Type( "Numeric"\|"Character"\|"Expression"\|"Row State", \<Format("format string")\>, \<Input Format("format string")\>, \<1\|2\|4\>, \< \<\<Fail On Conversion Error \>, \< \<\<Return Failed Rows \> )

**Description:** Sets the data type for the column. Using the optional arguments, you can also set the format, input format, and the width in bytes if the column is numeric. Fail On Conversion Error aborts the data type change if any values fail to convert. This is especially useful when converting a character column to a numeric column. Return Failed Rows returns a list containing indices of the rows that failed to convert.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "Time",
    "Character",
    "Nominal",
    Set Values( {"13:32", "20:10", "20:12", "14:56"} )
);
Wait( 2 );
dt:Time << Set Data Type( "Numeric", Format( "h:m", 12 ), Input Format( "h:m" ) );
dt:Time << Set Modeling Type( "Continuous" );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
dt:Age << Set Data Type( "Character" );
dt:Height << Set Data Type( "Numeric", 2 );
```

**Example 3**

``` jsl
dt = New Table( "My Table",
    New Column( "col1",
        Character,
        "Nominal",
        Set Values( {"123", "456", "abc", "789", "", "def"} )
    )
);
r = dt:col1 << Set Data Type( "Numeric", <<Fail On Conversion Error, <<Return Failed Rows );
Show( r );
```

**Example 4**

``` jsl
dt = New Table( "My Table",
    New Column( "col1",
        Character,
        "Nominal",
        Set Values( {"123", "456", "abc", "789", "", "def"} )
    )
);
r = dt:col1 << Set Data Type( "Numeric", <<Return Failed Rows );
Show( r );
```

#### [Set Display Width](#set-display-width)[](#set-display-width "Click to copy url")

**Syntax:** obj \<\< Set Display Width( number )

**Description:** Change column's display width.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 0 );
w = :Height << Get Display Width;
:Height << Set Display Width( 2 * w );
```

#### [Set Each Value](#set-each-value)[](#set-each-value "Click to copy url")

**Syntax:** obj \<\< Set Each Value( number )

**Description:** Sets all the values in a column to a constant.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "X" );
dt:X << Set Each Value( 5 );
```

#### [Set Excluded](#set-excluded)[](#set-excluded "Click to copy url")

**Syntax:** obj \<\< Set Excluded

**Description:** Excludes the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Weight << Set excluded;
```

#### [Set Field Width](#set-field-width)[](#set-field-width "Click to copy url")

**Syntax:** obj \<\< Set Field Width( number )

**Description:** Sets the field width used for displaying data in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Height << Set Field Width( 20 );
```

#### [Set Formula](#set-formula)[](#set-formula "Click to copy url")

**Syntax:** obj \<\< Set Formula( formula ) obj \<\< Formula( formula )

**Description:** Sets the formula in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = New Column( "Ratio" );
col << Set Formula( :Height / :Weight );
```

#### [Set Header Background Color](#set-header-background-color)[](#set-header-background-color "Click to copy url")

**Syntax:** obj \<\< Set Header Background Color

**Description:** Set the header color. Set to "None" to use the default color

**JMP Version Added:** 18

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:height << Set Header Background Color( "Light Red" );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:height << Set Header Background Color( {250, 200, 150} );
```

#### [Set Header Chart Type](#set-header-chart-type)[](#set-header-chart-type "Click to copy url")

**Syntax:** obj \<\< Set Header Chart Type

**Description:** Sets the type of chart to display in the data table column header.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:height << Set Header Chart Type( "Run Chart" );
```

#### [Set Header Text Color](#set-header-text-color)[](#set-header-text-color "Click to copy url")

**Syntax:** obj \<\< Set Header Text Color

**Description:** Set the header text color. Set to "None" to use the default color

**JMP Version Added:** 18

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:height << Set Header Text Color( "Dark Purple" );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:height << Set Header Text Color( {100, 50, 100} );
```

#### [Set Hidden](#set-hidden)[](#set-hidden "Click to copy url")

**Syntax:** obj \<\< Set Hidden

**Description:** Hides the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Weight << Set hidden;
```

#### [Set Initial Data](#set-initial-data)[](#set-initial-data "Click to copy url")

**Syntax:** obj \<\< Set Initial Data

**Description:** Initialize the column's data with any constant, or a simple expression.

**Example 1**

``` jsl
dt = New Table( "MyDt", New Column(), New Column() );
dt << Add Rows( 5 );
Column( dt, 1 ) << set initial data( Today() );
Column( dt, 2 ) << set initial data( 99 );
```

**Example 2**

``` jsl
dt = New Table( "MyDt" );
dt << Add Rows( 5 );
Column( dt, 1 ) << set initial data( Log( 1 ) );
```

#### [Set Labeled](#set-labeled)[](#set-labeled "Click to copy url")

**Syntax:** obj \<\< Set Labeled

**Description:** Use the column's data value for label.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Weight << Set labeled;
```

#### [Set Modeling Type](#set-modeling-type)[](#set-modeling-type "Click to copy url")

**Syntax:** obj \<\< Set Modeling Type( "None"\|"Continuous"\|"Ordinal"\|"Nominal"\|"Row State"\|"Multiple Response"\|"Unstructured Text"\|"Vector" )

**Description:** Sets the modeling type for the data table column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Age << Set Modeling Type( "Continuous" );
```

#### [Set Name](#set-name_1)[](#set-name_1 "Click to copy url")

**Syntax:** obj \<\< Set Name( name )

**Description:** Sets the column name.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Age << Set Name( "Time" );
```

#### [Set Property](#set-property_1)[](#set-property_1 "Click to copy url")

**Syntax:** obj \<\< Set Property( Notes \| List Check \| Range Check \| Axis \| Spec Limits \| Control Limits \| Sigma \| Process Capability Distribution \| Coding \| Mixture \| Design Role \| Response Limits \| Units \| Value Order \| Value Labels \| Value Scores \| Row Order Levels \| Distribution \| Time Frequency \| Value Colors \| Color Gradient \| Missing Value Codes \| Factor Change \| Map Role \| Supercategories \| Multiple Response \| Profit Matrix \| Informative Missing \| Expression Role \| Link ID \| Link Reference \| Event Handler \| Custom Property, {argument list} )

**Description:** Sets properties in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Weight << Set Property( "Units", lbs );
```

#### [Set Scroll Locked](#set-scroll-locked)[](#set-scroll-locked "Click to copy url")

**Syntax:** obj \<\< Set Scroll Locked

**Description:** Scroll locks the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Weight << Set Scroll locked;
```

#### [Set Selected](#set-selected)[](#set-selected "Click to copy url")

**Syntax:** obj \<\< Set Selected( state=0\|1 )

**Description:** Selects the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Height << Set Selected( 1 );
```

#### [Set Use for Marker](#set-use-for-marker)[](#set-use-for-marker "Click to copy url")

**Syntax:** obj \<\< Set Use for Marker

**Description:** Use the values in this column as the markers in a graph. Expression columns with pictures or character columns with IDs might work well.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Name << Set Use for Marker;
```

#### [Set Values](#set-values)[](#set-values "Click to copy url")

**Syntax:** obj \<\< Set Values( \[ value1, value2, value3, ... \] )

**Description:** Sets the values in a column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Column( "X" );
:X << Set Values(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
);
```

#### [SetLock](#setlock)[](#setlock "Click to copy url")

**Syntax:** obj \<\< SetLock

**Description:** Locks the column from any further changes.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Age << Lock( 1 );
```

#### [Suppress Eval](#suppress-eval)[](#suppress-eval "Click to copy url")

**Syntax:** obj \<\< Suppress Eval( state=0\|1 )

**Description:** Set the flag to suppress evaluation of the formula in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = New Column( "Ratio" );
col << Set Formula( :Height / :Weight );
col << suppress eval( true );
```

#### [Use Value Labels](#use-value-labels)[](#use-value-labels "Click to copy url")

**Syntax:** obj \<\< Use Value Labels( state=0\|1 )

**Description:** Substitutes value labels defined in the column in all output.

``` jsl
dt = Open( "$SAMPLE_DATA/CrabSatellites.jmp" );
:Color << Use Value Labels( 1 );
Distribution( Column( :Color ) );
```

#### [Value Labels](#value-labels)[](#value-labels "Click to copy url")

**Syntax:** obj \<\< Value Labels( { value1 = "label1", value2 = "label2", ... } )

**Description:** Sets the Value Labels

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:sex << Value Labels( {"F" = "Female", "M" = "Male"} );
```

## [Data Table Cols](#data-table-cols)[](#data-table-cols "Click to copy url")

### [Associated Constructors](#associated-constructors_1)[](#associated-constructors_1 "Click to copy url")

#### [Column](#column)[](#column "Click to copy url")

**Syntax:** y = Column( name\|number ); y = Column( dataTable, name\|number, \<"formatted"\> )

**Description:** Returns a reference to the specified data table column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = Column( "height" );
```

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Add Multiple Columns](#add-multiple-columns)[](#add-multiple-columns "Click to copy url")

**Syntax:** obj \<\< Add Multiple Columns( Column prefix, number of columns, \<before first\|after last\|after(column)\>, Character\|Numeric\|Row State, \<fieldwidth(number)\> )

**Description:** Creates multiple new columns in the current data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Add Multiple Columns( "Date", 5, Character );
```

#### [Clear Column Selection](#clear-column-selection_1)[](#clear-column-selection_1 "Click to copy url")

**Syntax:** obj \<\< Clear Column Selection

**Description:** Clears the column selection in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Go To( :BP 12F );
Wait( 2 );
dt << Clear Column Selection();
```

#### [Clone Formula Column](#clone-formula-column)[](#clone-formula-column "Click to copy url")

**Syntax:** obj \<\< Clone Formula Column( column, n, \<Substitute Column Reference( column1, list )\> )

**Description:** Creates n new formula columns based on the given column. Column references to column1 from the original formula will be replaced by each column in list for all n columns. Use multiple Substitute Column Reference arguments when replacing more than one column reference from the original formula.

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << New Column( "Day 1", Formula( (:BP 8M + :BP 12M + :BP 6M) / 3 ) );
list1 = {:BP 8W, :BP 8F};
list2 = {:BP 12W, :BP 12F};
list3 = {:BP 6W, :BP 6F};
dt << Clone Formula Column(
    "Day 1",
    2,
    Substitute Column Reference( :BP 8M, list1 ),
    Substitute Column Reference( :BP 12M, list2 ),
    Substitute Column Reference( :BP 6M, list3 )
);
```

#### [Columns Manager](#columns-manager)[](#columns-manager "Click to copy url")

**Syntax:** obj \<\< Columns Manager

**Description:** Invoke the Columns Manager on the current table, showing properties and statistics for the columns.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col1 = dt << Columns Manager;
```

#### [Combine Columns](#combine-columns_1)[](#combine-columns_1 "Click to copy url")

**Syntax:** obj \<\< Combine Columns

**Description:** Combine a set of columns into a delimited (multiple response) column.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
dt << Combine Columns(
    delimiter( "," ),
    Columns(
        :Brush After Waking Up, :Brush After Meal, :Brush Before Sleep, :Brush Another Time
    ),
    Selected Columns are Indicator Columns( 1 ),
    Column Name( "When to Brush" )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
dt << Combine Columns(
    delimiter( "," ),
    Columns(
        :Brush After Waking Up, :Brush After Meal, :Brush Before Sleep, :Brush Another Time
    ),
    Column Name( "When to Brush" )
);
```

#### [Compress Selected Columns](#compress-selected-columns_1)[](#compress-selected-columns_1 "Click to copy url")

**Syntax:** obj \<\< Compress Selected Columns( { column1, column2, ... )

**Description:** Compresses each column into the most compact form.

Character data will be 1-byte if there are fewer than 255 levels.

Numeric data will be 1-byte if the data is between -127 and 127.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Compress Selected Columns( {:Age, :sex, :Height, :Weight} );
```

#### [Exclude/Unexclude](#excludeunexclude)[](#excludeunexclude "Click to copy url")

**Syntax:** obj \<\< Exclude( 0\|1 )

**Description:** Excludes the column from any analysis run.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:Name << Exclude( 1 );
```

#### [Formula](#formula_1)[](#formula_1 "Click to copy url")

**Syntax:** obj \<\< Formula

**Description:** Sets a formula in the column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col1 = dt << New Column( "Ratio", Numeric, Continuous );
col1 << Formula( :height / :weight );
```

#### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Preselect Role( Freq )

**Description:** Assigns the Freq role to the data table column

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = Column( "weight" );
col << Preselect Role( "freq" );
```

#### [Go to](#go-to)[](#go-to "Click to copy url")

**Syntax:** obj \<\< Go to( column name\|column number )

**Description:** Selects and moves to the specified column in the current data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
dt << Go to( :BP 12F );
```

#### [Hide/Unhide](#hideunhide)[](#hideunhide "Click to copy url")

**Syntax:** obj \<\< Hide( 0\|1 )

**Description:** Hides the column in the data grid.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:Age << Hide( 1 );
```

#### [Invert Column Selection](#invert-column-selection)[](#invert-column-selection "Click to copy url")

**Syntax:** obj \<\< Invert Column Selection( \<list of columns\> )

**Description:** Inverts the current column selection. If a list of columns is given, the columns that are not in the list will be selected.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:age << Set Selected( 1 );
dt:height << Set Selected( 1 );
Wait( 1 );
b = dt << Invert Column Selection;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
a = {:height, :weight};
b = dt << Invert Column Selection( a );
```

#### [Label/Unlabel](#labelunlabel)[](#labelunlabel "Click to copy url")

**Syntax:** obj \<\< Label( 0\|1 )

**Description:** Sets this column as a label for identification. Values in the column will appear on a graphs when a point is selected.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:Age << Label( 1 );
```

#### [Make Indicator Columns](#make-indicator-columns_1)[](#make-indicator-columns_1 "Click to copy url")

**Syntax:** obj \<\< Make Indicator Columns

**Description:** Make a set of indicator columns from the selected column

``` jsl
dt = Open( "$SAMPLE_DATA/Animals.jmp" );
dt << Make Indicator Columns( columns( {:species, :season} ) );
```

#### [Move Selected Columns](#move-selected-columns)[](#move-selected-columns "Click to copy url")

**Syntax:** obj \<\< Move Selected Columns( column\|column list, To first\|To last\|After(column)\|after(group)\|after(Path({\<a\>, \<b\>, ...}) )

**Description:** Moves selected columns in the data table.

**After column**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Go To( :Age );
Wait( 2 );
dt << Move Selected Columns( After( :sex ) );
```

**After group**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << group Columns( "Measures", {:height, :weight} );
dt << Go To( :Age );
Wait( 2 );
dt << Move Selected Columns( After( "Measures" ) );
```

**Input list**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Move Selected Columns( {:height, :weight}, After( :name ) );
```

**To last**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Go To( :Age );
Wait( 2 );
dt << Move Selected Columns( To last );
```

#### [New Column](#new-column)[](#new-column "Click to copy url")

**Syntax:** obj \<\< New Column( \<name\>, \<data type\>, \<modeling type\>, \<Format()\>, \<Formula()\>, \<Set Property()\>, \<Set Values()\>, \<Like()\> )

**Description:** Creates a new column in the current data table.

**Like**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "like name", Like( :name ) );
```

**New Table**

``` jsl
New Table( "test",
    Add Rows( 5 ),
    New Column( "name",
        Character( 8 ),
        Nominal,
        Set Values( {"KATIE", "LOUISE", "JANE", "JACLYN", "LILLIE"} )
    ),
    New Column( "age",
        Numeric,
        Ordinal,
        Format( "Fixed Dec", Use thousands separator( 0 ), 5, 0 ),
        Set Values( [12, 12, 12, 12, 12] )
    ),
    New Column( "code",
        Character( 2 ),
        Nominal,
        Set Values( {"AA", "AA", "BB", "BB", "AA"} )
    )
);
```

**Simple**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "X", Formula( Random Uniform() ) );
```

#### [New Formula Column](#new-formula-column)[](#new-formula-column "Click to copy url")

**Syntax:** dt \<\< New Formula Column(Operation(name, \<Category(name)\>), Columns(columns), \<Group By(columns)\>)

**Description:** Create a formula column in the table, using the columns specified and applying the operation and optional grouping columns. The operation category can be specified if necessary to disambiguate the operation name. Returns a list of column references to the created columns.

**JMP Version Added:** 17

**Group By**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Formula Column(
    Operation( "Mean" ),
    Columns( :height, :weight ),
    Group By( :age )
);
```

**Log 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Formula Column( Operation( "Log 2" ), Columns( :height, :weight ) );
```

#### [Next Selected Column](#next-selected-column)[](#next-selected-column "Click to copy url")

**Syntax:** obj \<\< Next Selected Column

**Description:** Go to the next selected column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:age << Set Selected( 1 );
dt:height << Set Selected( 1 );
Wait( 1 );
dt << Next Selected Column;
Wait( 2 );
dt << Next Selected Column;
```

#### [No Role](#no-role)[](#no-role "Click to copy url")

**Syntax:** obj \<\< Preselect Role( No Role )

**Description:** Removes the assigned role from the data table column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Weight << Preselect Role( "No Role" );
```

#### [Original Order](#original-order)[](#original-order "Click to copy url")

**Syntax:** obj \<\< Original Order

**Description:** Moves columns back to their original order in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Go To( :Age );
dt << Move Selected Columns( To last );
Wait( 2 );
dt << Original Order();
```

#### [Paste Column Properties](#paste-column-properties_1)[](#paste-column-properties_1 "Click to copy url")

**Syntax:** obj \<\< Paste Column Properties

**Description:** Pastes from the clipboard multiple lists of column properties to multiple columns. Optionally, you can specify a list of target columns instead of selecting them in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Tiretread.jmp" );
dt << Copy Column Properties( {:MODULUS, :ELONG} );
dt2 = New Table( "test it",
    New Column( "T1", numeric, continuous ),
    New Column( "T2", numeric, continuous ),
    New Column( "T3", numeric, continuous ),
    Add Rows( 10 )
);
dt2 << Paste Column Properties( {:T1, :T3} );
```

#### [Previous Selected Column](#previous-selected-column)[](#previous-selected-column "Click to copy url")

**Syntax:** obj \<\< Previous Selected Column

**Description:** Go to the previously selected column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:age << Set Selected( 1 );
dt:height << Set Selected( 1 );
Wait( 1 );
dt << Next Selected Column;
dt << Next Selected Column;
Wait( 2 );
dt << Previous Selected Column;
```

#### [Reorder by Data Type](#reorder-by-data-type)[](#reorder-by-data-type "Click to copy url")

**Syntax:** obj \<\< Reorder by Data Type

**Description:** Reorders columns in the data table sorting by data type.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
Wait( 1 );
dt << Reorder By Data Type();
```

#### [Reorder by Modeling Type](#reorder-by-modeling-type)[](#reorder-by-modeling-type "Click to copy url")

**Syntax:** obj \<\< Reorder by Modeling Type

**Description:** Reorders columns in the data table sorting by modeling type.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
Wait( 1 );
dt << Reorder By Modeling Type();
```

#### [Reorder by Name](#reorder-by-name)[](#reorder-by-name "Click to copy url")

**Syntax:** obj \<\< Reorder by Name

**Description:** Reorders columns in the data table sorting by column name.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
Wait( 1 );
dt << Reorder By Name();
```

#### [Reverse Order](#reverse-order)[](#reverse-order "Click to copy url")

**Syntax:** obj \<\< Reverse Order

**Description:** Reverses the order of columns in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
Wait( 1 );
dt << Reverse Order();
```

#### [Set Label Columns](#set-label-columns_1)[](#set-label-columns_1 "Click to copy url")

**Syntax:** obj \<\< Set Label Columns( column(s) )

**Description:** Assigns a label role to selected columns in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
Wait( 1 );
dt << Set Label Columns( :City, :State );
```

#### [Set Scroll Lock Columns](#set-scroll-lock-columns_1)[](#set-scroll-lock-columns_1 "Click to copy url")

**Syntax:** obj \<\< Set Scroll Lock Columns( column(s) )

**Description:** Locks selected columns in the data table from scrolling. To indicate that a column is locked, the background color changes.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dt << Set Scroll Lock Columns( :City );
```

#### [Text to Columns](#text-to-columns_1)[](#text-to-columns_1 "Click to copy url")

**Syntax:** obj \<\< Text to Columns

**Description:** Make a set of text columns or indicator columns from a delimited text column

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
dt << Text To Columns( delimiter( "," ), columns( :Brush Delimited ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Consumer Preferences.jmp" );
dt << Text To Columns(
    delimiter( "," ),
    columns( :Brush Delimited ),
    Make Indicator Columns( 1 )
);
```

#### [Use for Marker](#use-for-marker)[](#use-for-marker "Click to copy url")

**Syntax:** obj \<\< UseForMarker( 0\|1 )

**Description:** Use the values in this column as the markers in a graph. Expression columns with pictures or character columns with IDs might work well.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:Name << UseForMarker( 1 );
```

#### [Validation](#validation)[](#validation "Click to copy url")

**Syntax:** obj \<\< Preselect Role( Validation)

**Description:** Assigns the Validation role to the data table column

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = Column( "age" );
col << Preselect Role( "Validation" );
```

#### [Weight](#weight_1)[](#weight_1 "Click to copy url")

**Syntax:** obj \<\< Preselect Role( Weight )

**Description:** Assigns the Weight role to the data table column

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt:Weight << Preselect Role( "weight" );
```

#### [X](#x)[](#x "Click to copy url")

**Syntax:** obj \<\< Preselect Role( X )

**Description:** Assigns the X role to the data table column

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
col = Column( "weight" );
col << Preselect Role( "X" );
```

#### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Preselect Role( Y )

**Description:** Assigns the Y role to the data table column

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
:Weight << Preselect Role( "Y" );
```

## [Data Table Rows](#data-table-rows)[](#data-table-rows "Click to copy url")

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [Add Rows](#add-rows)[](#add-rows "Click to copy url")

**Syntax:** obj \<\< Add Rows( \<n\>, \<At Start\|At End\|After(m)\> \| {list of (column name = value) pairs}) )

**Description:** Adds n rows, at start, at end, or after row m to the data table.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Add Rows( 3, after( 5 ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Add Rows( {name = "David", age = 15} );
```

#### [Clear Row States](#clear-row-states)[](#clear-row-states "Click to copy url")

**Syntax:** obj \<\< Clear Row States

**Description:** Clears from all rows the states, including selected, excluded, hidden, markers, labels, and colors.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [5, 7, 8, 10, 12, 15] );
Wait( 2 );
dt << Clear Row States;
```

#### [Clear Select](#clear-select)[](#clear-select "Click to copy url")

**Syntax:** obj \<\< Clear Select

**Description:** Clears or deselects the selected rows.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [5, 7, 8, 10] );
Wait( 2 );
dt << Clear Select();
```

#### [Clear Selected Row States](#clear-selected-row-states)[](#clear-selected-row-states "Click to copy url")

**Syntax:** obj \<\< Clear Selected Row States

**Description:** Clears from the selected rows the states, including selected, excluded, hidden, markers, labels, and colors.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Select Rows( [5, 6, 7, 8, 9, 10] );
r << Exclude;
r << clear select;
r << Select Rows( [5, 6] );
Wait( 1 );
dt << Clear Selected Row States;
```

#### [Color Rows by Row State](#color-rows-by-row-state)[](#color-rows-by-row-state "Click to copy url")

**Syntax:** obj \<\< Color Rows by Row State

**Description:** Displays or hides in the cells of the data table, the color assigned in the row state.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Color by Column( :Age );
Wait( 2 );
dt << Color Rows by Row State;
```

#### [Color by Column](#color-by-column)[](#color-by-column "Click to copy url")

**Syntax:** obj \<\< Color by Column( column, \<Color( number )\>, \<Color Theme( color theme )\>, \< Continuous scale(0\|1)\>, \<Reverse scale(0\|1)\>, \<Excluded Row( 0\|1 ), \<Make window with legend\> )

**Description:** Assigns a color for each row in the data table based on the value of the column specified.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Color by Column( :Age );
```

#### [Color or Mark by Column](#color-or-mark-by-column)[](#color-or-mark-by-column "Click to copy url")

**Syntax:** obj \<\< Color or Mark by Column( column, \<Color( number )\>, \<Color Theme( color theme )\>, \<Marker Theme( standard\|hollow\|solid\|paired\|classic\|alphanumeric )\> )

**Description:** Associate colors or markers with the values of a specified column

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Color or Mark by Column( :Age );
```

#### [Colors](#colors)[](#colors "Click to copy url")

**Syntax:** obj \<\< Colors( color )

**Description:** Colors the selected rows in all graphical output containing markers.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Run Script( "Bivariate" );
Wait( 1 );
dt << Select Where( :sex == "F" );
Wait( 1 );
dt << Colors( "Red" );
```

#### [Data Filter](#data-filter)[](#data-filter "Click to copy url")

**Syntax:** obj \<\< Data Filter( \<Location(x,y)\>, \<"Close Outline"\>, \<"Local"\>, \<Inverse(0\|1)\>, \<Show Columns Selector(0\|1)\>, \<Title(string)\>, \<Save And Restore Current Row States(0\|1)\>, \<Conditional(0\|1)\>, \<Auto Clear(0\|1)\>, \<Group By AND(0\|1)\>, \<Show Histograms And Bars(0\|1)\>, \<Count Excluded Rows(0\|1)\>, \<Mode(...)\>, \<Add Filter(Columns(...), Where(...), Display(...), \<Select Missing(cols)\>, \<Order By Count(cols)\>)\>, \<Favorites(...)\>, \<Animation(...)\> )

**Description:** Creates or shows a Data Filter, where you interactively select complex subsets of data. The Mode option determines which row states are affected by selection in the filter. The Add Filter command will add a filter group with the given Columns and Where clauses. When multiple filter groups are present, the combined behavior is determined by the Group By AND option. If the Local keyword is given, the filter can be embedded in a report to filter one or more platforms without affecting other reports.

**Global Data Filter**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Data Filter(
    Location( {218, 114} ),
    Mode( Select( 0 ), Show( 1 ), Include( 1 ) ),
    Add Filter(
        columns( :age, :height ),
        Where( :age == {13, 14, 15} ),
        Where( :height >= 65 & :height <= 70 )
    ),
    Add Filter( columns( :weight ), Where( :weight >= 64 & :weight <= 100 ) )
);
```

**Local Data Filter**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "Local Data Filter",
    Data Filter Context Box(
        H List Box(
            dt << Data Filter(
                Local,
                Mode( Show( 1 ), Include( 1 ) ),
                Add Filter(
                    columns( :age, :height ),
                    Where( :age == {13, 14, 15} ),
                    Where( :height >= 65 & :height <= 70 )
                ),
                Add Filter( columns( :weight ), Where( :weight >= 64 & :weight <= 100 ) )
            ),
            dt << Run Script( "Bivariate" ),
            dt << Run Script( "Distribution" )
        )
    )
);
```

#### [Data View](#data-view)[](#data-view "Click to copy url")

**Syntax:** obj \<\< Data View

**Description:** Makes a new data view of the currently selected rows.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Where( :age < 14 );
dt << Data View;
```

#### [Delete Rows](#delete-rows)[](#delete-rows "Click to copy url")

**Syntax:** obj \<\< Delete Rows

**Description:** Deletes the selected row(s).

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [5, 7, 8, 10] );
Wait( 2 );
r = dt << Delete Rows;
Show( r );
```

#### [Exclude/Unexclude](#excludeunexclude_1)[](#excludeunexclude_1 "Click to copy url")

**Syntax:** obj \<\< Exclude/Unexclude

**Description:** Excludes the selected rows from contributing to calculations.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Select Rows( [5, 7, 8, 10] );
r << Exclude;
```

#### [Get Rows](#get-rows)[](#get-rows "Click to copy url")

**Syntax:** obj \<\< Get Rows( number )

**Description:** returns a list of column values for the specified rows

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Get Rows( 3 );
dt << Get Rows( {1, 2, 3} );
```

#### [Go to Row](#go-to-row)[](#go-to-row "Click to copy url")

**Syntax:** obj \<\< Go to Row( row number )

**Description:** Returns a row object, moves to the specified row, selects the row and highlights it.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Go To Row( 5 );
```

#### [Hide and Exclude](#hide-and-exclude)[](#hide-and-exclude "Click to copy url")

**Syntax:** obj \<\< Hide and Exclude

**Description:** Hides the selected rows from appearing on graphs and excludes them from contributing to calculations.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Select Rows( [5, 7, 8, 10] );
r << Hide and Exclude;
```

#### [Hide/Unhide](#hideunhide_1)[](#hideunhide_1 "Click to copy url")

**Syntax:** obj \<\< Hide/Unhide

**Description:** Hides the selected rows from appearing on graphs.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Go To Row( 12 );
r << Hide;
```

#### [Insert Rows](#insert-rows)[](#insert-rows "Click to copy url")

**Syntax:** obj \<\< Insert Rows

**Description:** Inserts rows before selected rows. Has no effect if no rows are selected.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [3, 4, 5] );
dt << Insert Rows;
```

#### [Invert Row Selection](#invert-row-selection)[](#invert-row-selection "Click to copy url")

**Syntax:** obj \<\< Invert Row Selection

**Description:** Inverts the current row selection.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Select Where( :Age < 14 );
Wait( 2 );
r << Invert Row Selection;
```

#### [Label/Unlabel](#labelunlabel_1)[](#labelunlabel_1 "Click to copy url")

**Syntax:** obj \<\< Label/Unlabel

**Description:** Labels the selected rows in all graphical output containing markers.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Go To Row( 5 );
r << Label;
```

#### [Marker by Column](#marker-by-column)[](#marker-by-column "Click to copy url")

**Syntax:** obj \<\< Marker by Column( column, \<Marker( number )\>, \<Marker Theme( standard \| hollow \| solid \| paired \| classic \| alphanumeric )\>, \<Color theme( string )\>, \< Continuous scale(0\|1)\>, \<Reverse scale(0\|1)\>, \<Excluded Row( 0\|1 ), \<Make window with legend\> )

**Description:** Assigns a marker for each row in the data table based on the value of the column specified.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Marker by Column( :sex );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/big class.jmp" );
dt << Marker By Column(
    :age,
    Marker( 1 ),
    Color theme( "White to Red" ),
    Marker Theme( "alphanumeric" ),
    Reverse Scale( 1 ),
    Make Window With Legend
);
```

#### [Markers](#markers)[](#markers "Click to copy url")

**Syntax:** obj \<\< Markers( marker )

**Description:** Changes the markers for the selected rows in all graphical output containing markers.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Select Where( :sex == "M" );
r << Markers( "+" );
```

#### [Move Rows](#move-rows)[](#move-rows "Click to copy url")

**Syntax:** obj \<\< Move Rows( At Start\|At End\|After(n) )

**Description:** Moves the selected rows up or down in the data table to the specified new location.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Select Rows( [5, 7, 8, 10] );
Wait( 2 );
r << Move Rows( At Start );
```

#### [Name Selection in Column](#name-selection-in-column)[](#name-selection-in-column "Click to copy url")

**Syntax:** obj \<\< Name Selection in Column( Column Name( name ), Selected( string ), Unselected( string ) )

**Description:** Creates a new categorical column with two values, one each for the selected and nonselected rows.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Where( :Age < 14 );
dt << Name Selection in Column(
    Column Name( "Younger" ),
    Selected( "Yes" ),
    Unselected( "No" )
);
```

#### [Next Selected](#next-selected)[](#next-selected "Click to copy url")

**Syntax:** obj \<\< Next Selected

**Description:** Highlights the next row in the group of selected rows.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Select Rows( [5, 7, 8, 10] );
Wait( 2 );
r << Next Selected;
```

#### [Previous Selected](#previous-selected)[](#previous-selected "Click to copy url")

**Syntax:** obj \<\< Previous Selected

**Description:** Highlights the previous row in the group of selected rows.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Select Rows( [5, 7, 8, 10] );
Wait( 2 );
r << Previous Selected;
```

#### [Row Editor](#row-editor)[](#row-editor "Click to copy url")

**Syntax:** obj \<\< Row Editor

**Description:** Opens the Row Editor dialog for the selected row(s).

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
r = dt << Select Rows( [5, 7, 8, 10] );
r << Row Editor();
```

#### [Row Selection](#row-selection)[](#row-selection "Click to copy url")

**Syntax:** obj \<\< Row Selection( Select Where(condition), \< current selection("extend" \| "restrict" \| "clear")\>, \<Dialog("Keep Dialog Open")\>, \<Match Case(0\|1)\> )

**Description:** Selects all rows that meet the defined condition, with option to extend or restrict existing selections, option to execute the selection or just show the dialog. When Match Case is omitted, the default is a case-sensitive match.

**JMP Version Added:** 15

**Example 1**

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Row Selection( Select where( :age < 15 ) );
```

**Example 2**

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Row Selection( Select where( :age < 15 ) );
Wait( 2 );
dt << Row Selection( Select where( :age == 15 ), current selection( "extend" ) );
```

**Example 3**

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Row Selection( Select where( :age < 15 ) );
dt << Row Selection(
    Select where( :sex == "M" ),
    current selection( "restrict" ),
    Dialog( "keep dialog open" )
);
```

**Example 4**

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Row Selection( Select where( :name == "jane" ), Match Case( 0 ) );
```

#### [Select All Matching Cells](#select-all-matching-cells)[](#select-all-matching-cells "Click to copy url")

**Syntax:** obj \<\< Select All Matching Cells

**Description:** Selects in all open data tables, all rows where the values in the column selected match one of the values for the rows selected in that column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students.jmp" );
dt << Select Rows( [1, 2, 3, 4] );
dt << Go To( :Height );
Wait( 2 );
dt << Select All Matching Cells();
```

#### [Select All Rows](#select-all-rows)[](#select-all-rows "Click to copy url")

**Syntax:** obj \<\< Select All Rows

**Description:** Selects all the rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select All Rows;
```

#### [Select Dominant](#select-dominant)[](#select-dominant "Click to copy url")

**Syntax:** obj \<\< Select Dominant( {column1, column2, ...},{0\|1, 0\|1, ...} )

**Description:** Selects all rows based on the high (1) or low (0) values of the Pareto Frontier.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Go To( :height );
dt << Select Dominant( {:height, :weight}, {0, 0} );
```

#### [Select Duplicate Rows](#select-duplicate-rows)[](#select-duplicate-rows "Click to copy url")

**Syntax:** obj \<\< Select Duplicate Rows( \<match(column1, column2, ...)\> )

**Description:** Selects duplicate rows and matches on the selected columns. If no match columns are given, rows are matched on all columns of the table. Returns the number of duplicate rows.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select duplicate rows( Match( :age, :height ) );
```

#### [Select Excluded](#select-excluded)[](#select-excluded "Click to copy url")

**Syntax:** obj \<\< Select Excluded

**Description:** Selects all excluded rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [5, 7, 8, 10, 15] );
dt << Exclude( 1 );
dt << Clear Select;
Wait( 2 );
dt << Select Excluded;
```

#### [Select Hidden](#select-hidden)[](#select-hidden "Click to copy url")

**Syntax:** obj \<\< Select Hidden

**Description:** Selects all hidden rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [5, 7, 8, 10, 15] );
dt << Hide( 1 );
dt << Clear Select;
Wait( 2 );
dt << Select Hidden;
```

#### [Select Labeled](#select-labeled)[](#select-labeled "Click to copy url")

**Syntax:** obj \<\< Select Labeled

**Description:** Selects all labeled rows in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [5, 7, 8, 10, 15] );
dt << Label( 1 );
dt << Clear Select;
Wait( 2 );
dt << Select Labeled;
```

#### [Select Matching Cells](#select-matching-cells)[](#select-matching-cells "Click to copy url")

**Syntax:** obj \<\< Select Matching Cells

**Description:** Selects all rows where the values in the column selected match one of the values for the rows selected in that column.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [1, 2, 3, 4] );
dt << Go To( :Height );
Wait( 2 );
dt << Select Matching Cells();
```

#### [Select Randomly](#select-randomly)[](#select-randomly "Click to copy url")

**Syntax:** obj \<\< Select Randomly( number \| probability \| Sample Size( number ) \| Sampling Rate( probability ) )

**Description:** Selects a specified fraction of rows randomly.

**Probability**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Randomly( 0.3 );
```

**Sample Size**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Randomly( Sample Size( 12 ) );
```

**Sampling Rate**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Randomly( Sampling Rate( 0.3 ) );
```

#### [Select Rows](#select-rows)[](#select-rows "Click to copy url")

**Syntax:** obj \<\< Select Rows( \[row1, row2, ...\] )

**Description:** Selects the specified rows.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [5, 7, 8, 10] );
```

#### [Select Where](#select-where)[](#select-where "Click to copy url")

**Syntax:** obj \<\< Select Where( condition, \< current selection("extend" \| "restrict" \| "clear")\> )

**Description:** The options are extending or restricting selections, executing the selection, or showing only the dialog.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Where( :Age < 14 );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Where( :Age == 14 );
Wait( 0 );
dt << Select Where( :sex == "M", current selection( "extend" ) );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Where( Contains( :name, "AR" ) );
```

## [Filter Views](#filter-views)[](#filter-views "Click to copy url")

### [Item Messages](#item-messages_4)[](#item-messages_4 "Click to copy url")

#### [Get Data Filter](#get-data-filter)[](#get-data-filter "Click to copy url")

**Syntax:** expr = obj \<\< Get Data Filter

**Description:** Returns the filter view's filter definition

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Show( fv << Get Data Filter );
```

#### [Get Data Table](#get-data-table_1)[](#get-data-table_1 "Click to copy url")

**Syntax:** data table = obj \<\< Get Data Table

**Description:** Returns the table that owns the filter view

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Show( fv << Get Data Table );
```

#### [Get Name](#get-name_2)[](#get-name_2 "Click to copy url")

**Syntax:** string = obj \<\< Get Name

**Description:** Get the name of the filter view

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Show( fv << Get Name );
```

#### [Get Show Hidden Rows](#get-show-hidden-rows)[](#get-show-hidden-rows "Click to copy url")

**Syntax:** 0\|1 = obj \<\< Get Show Hidden Rows

**Description:** Returns the show hidden rows setting for this filter view

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Show Hidden Rows( 1 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Show( fv << Get Show Hidden Rows );
```

#### [Get Type](#get-type)[](#get-type "Click to copy url")

**Syntax:** obj \<\< Get Type

**Description:** Get the type of the filter view; one of: "Unfiltered", "Filtered", or "TemporaryFiltered".

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Show( fv << Get Type, fv << Is Temporary, fv << Is Unfiltered );
```

#### [Is Locked](#is-locked)[](#is-locked "Click to copy url")

**Syntax:** 0\|1 = obj \<\< Is Locked

**Description:** Returns the lock setting for this filter view

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Lock( 1 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Show( fv << Is Locked );
```

#### [Is Temporary](#is-temporary)[](#is-temporary "Click to copy url")

**Syntax:** 0\|1 = obj \<\< Is Temporary

**Description:** Returns 1 if the filtered view is a temporary filter view

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Show( fv << Get Type, fv << Is Temporary, fv << Is Unfiltered );
```

#### [Is Unfiltered](#is-unfiltered)[](#is-unfiltered "Click to copy url")

**Syntax:** 0\|1 = obj \<\< Is Unfiltered

**Description:** Returns 1 if the filtered view is the unfiltered filter view

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Show( fv << Get Type, fv << Is Temporary, fv << Is Unfiltered );
```

#### [Lock](#lock_1)[](#lock_1 "Click to copy url")

**Syntax:** obj \<\< Lock( 0\|1 )

**Description:** Prevent editing this filter view.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
fv << Lock( 1 );
Show( fv << Is Locked );
```

#### [Set Data Filter](#set-data-filter)[](#set-data-filter "Click to copy url")

**Syntax:** obj \<\< Set Data Filter( expr )

**Description:** Changes the filter definition of the filter view. The filter definition of the unfiltered view cannot be changed

**JMP Version Added:** 19

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View( "Dream", Active( 0 ) );
fv << Set Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) );
Show( fv << Get Data Filter );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View( "Dream", Active( 0 ) );
fv << Set Data Filter(
    Data Filter(
        Inverse( 1 ),
        Add Filter( Columns( :Island ), Where( :Island == "Dream" ) )
    )
);
Show( fv << Get Data Filter );
```

#### [Set Name](#set-name_2)[](#set-name_2 "Click to copy url")

**Syntax:** string = obj \<\< Set Name( name )

**Description:** Changes the name of the filter view. The names of the unfiltered view and the temporary filtered view cannot be changed.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
Show( fv << Set Name( "Dream Penguins" ) );
Show( fv << Get Name );
```

#### [Show Hidden Rows](#show-hidden-rows)[](#show-hidden-rows "Click to copy url")

**Syntax:** obj \<\< Show Hidden Rows( 0\|1 )

**Description:** Changes the show hidden rows setting for this filter view.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Penguins.jmp" );
fv = dt << New Filter View(
    "Dream",
    Active( 0 ),
    Show Hidden Rows( 1 ),
    Data Filter( Add Filter( Columns( :Island ), Where( :Island == "Dream" ) ) )
);
fv << Show Hidden Rows( 0 );
Show( fv << Get Show Hidden Rows );
```

[ Previous](Data%20Filter.html "Data Filter") [Next ](Datafeed.html "Datafeed")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
