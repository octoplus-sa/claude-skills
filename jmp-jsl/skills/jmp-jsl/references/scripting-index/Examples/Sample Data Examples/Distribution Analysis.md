# Distribution Analysis

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Distribution%20Analysis.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Distribution%20Analysis.html)*

---

# [Distribution Analysis](#distribution-analysis)[](#distribution-analysis "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Perform a contingency analysis](#perform-a-contingency-analysis)[](#perform-a-contingency-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Alcohol.jmp");
// Contingency
Contingency(
    Y( :Relapsed ),
    X( :Alcohol Consumption ),
    Freq( :Count ),
    Contingency Table(
        Count( 1 ),
        Total %( 1 ),
        Col %( 1 ),
        Row %( 1 ),
        Expected( 0 ),
        Deviation( 0 ),
        Cell Chi Square( 0 )
    )
);
```

### [Generate distributions of nominal variables](#generate-distributions-of-nominal-variables)[](#generate-distributions-of-nominal-variables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/AdverseR.jmp");
// Distribution
Distribution(
    Nominal Distribution(
        Column( :TREATMENT GROUP ),
        Mosaic Plot( 1 ),
        Histogram( 1 )
    ),
    Nominal Distribution(
        Column( :ADVERSE REACTION ),
        Mosaic Plot( 1 ),
        Histogram( 1 )
    ),
    Nominal Distribution(
        Column( :ADR SEVERITY ),
        Mosaic Plot( 1 ),
        Histogram( 1 )
    )
);
```

### [Build a repeated measures model](#build-a-repeated-measures-model)[](#build-a-repeated-measures-model "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Animals.jmp");
// Repeated Measures Model
Fit Model(
    Y( :miles ),
    Effects(
        :species,
        :subject[:species] & Random,
        :season, :species * :season
    ),
    Personality(
        "Standard Least Squares"
    ),
    Run
);
```

### [Generate an attribute chart](#generate-an-attribute-chart)[](#generate-an-attribute-chart "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Attribute Gauge.jmp");
// Attribute Chart
Attribute Chart(
    Y( :A, :B, :C ),
    X( :Part ),
    Standard( :Standard ),
    Effectiveness Report( 1 )
);
```

### [Perform distribution analysis](#perform-distribution-analysis)[](#perform-distribution-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/BabySleep.jmp");
// side by side
Distribution(
    y( Awake, Asleep ),
    quantiles( 0 )
);
```

### [Perform a t-test on matched pairs data](#perform-a-t-test-on-matched-pairs-data)[](#perform-a-t-test-on-matched-pairs-data "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/BabySleep.jmp");
// paired t-test
(
Matched Pairs(
    y( Awake, Asleep ),
    Reference Frame( 1 )
) << report)[AxisBox( 1 )] << Revert Axis;
```

### [Perform a paired t-test using the bivariate platform](#perform-a-paired-t-test-using-the-bivariate-platform)[](#perform-a-paired-t-test-using-the-bivariate-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/BabySleep.jmp");
// bivariate
Bivariate(
    x( Awake ),
    Y( Asleep ),
    Paired T Test
);
```

### [Build a partial least squares model using nipals method](#build-a-partial-least-squares-model-using-nipals-method)[](#build-a-partial-least-squares-model-using-nipals-method "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Baltic.jmp");
// Partial Least Squares
Partial Least Squares(
    Y( :ls, :ha, :dt ),
    X(
        :v1, :v2, :v3, :v4, :v5, :v6, :v7,
        :v8, :v9, :v10, :v11, :v12, :v13,
        :v14, :v15, :v16, :v17, :v18,
        :v19, :v20, :v21, :v22, :v23,
        :v24, :v25, :v26, :v27
    ),
    Fit(
        Method( NIPALS ),
        Initial Number of Factors( 15 )
    )
);
```

### [Set modeling type column property](#set-modeling-type-column-property)[](#set-modeling-type-column-property "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Big Class Families.jmp");
// Set Categorical
:sibling ages <<
Set Modeling Type( "Ordinal" );
:sports << Set Modeling Type( "Nominal" );
:countries visited <<
Set Modeling Type( "Nominal" );
:family cars <<
Set Modeling Type( "Nominal" );
```

### [Perform distribution analysis on columns with multiple response data](#perform-distribution-analysis-on-columns-with-multiple-response-data)[](#perform-distribution-analysis-on-columns-with-multiple-response-data "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Big Class Families.jmp");
// Distribution
Distribution(
    Y(
        :sibling ages, :sports,
        :countries visited, :family cars
    )
);
```

### [Generate distribution analysis with a continuous and nominal data columns](#generate-distribution-analysis-with-a-continuous-and-nominal-data-columns)[](#generate-distribution-analysis-with-a-continuous-and-nominal-data-columns "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Big Class.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :weight )
    ),
    Nominal Distribution(
        Column( :age )
    )
);
```

### [Perform oneway analysis with means and mean diamonds](#perform-oneway-analysis-with-means-and-mean-diamonds)[](#perform-oneway-analysis-with-means-and-mean-diamonds "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Big Class.jmp");
// Oneway
Oneway(
    Y( :height ),
    X( :sex ),
    Means( 1 ),
    Mean Diamonds( 1 )
);
```

### [Generate distribution analysis](#generate-distribution-analysis)[](#generate-distribution-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Blood Pressure by Time.jmp");
// side by side
Distribution(
    y( BP AM, BP PM ),
    quantiles( 0 )
);
```

### [Example jsl to add new rows to a table](#example-jsl-to-add-new-rows-to-a-table)[](#example-jsl-to-add-new-rows-to-a-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cherts.jmp");
// Add New Rows
Current Data Table() <<
Add Rows(
    {:location name = "Lanesboro", :Al =
    3866, :Mn = 15.56, :Na = 262.95, :Br
     = 0.88, :Ce = 0.45, :Co = 0.31, :Cr
     = 10.57, :Cs = 0.26, :Eu = 0.04, :Fe
     = 433.86, :Hf = 0.15, :La = 0.28,
    :Sc = 0.12, :sm = 0.03, :U = 0.75},
    {:location name = "Stockton", :al =
    2789.16, :Mn = 6.6, :Na = 208.6, :Br
     = 0.45, :Ce = 0.4, :Co = 0.28, :Cr
     = 11.76, :Cs = 0.25, :Eu = 0.04, :Fe
     = 342.8, :Hf = 0.08, :La = 0.12, :Sc
     = 0.05, :Sm = 0.02, :U = 0.63}
);
```

### [Example variable clustering](#example-variable-clustering)[](#example-variable-clustering "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cherts.jmp");
// Cluster Variables
Cluster Variables(
    Y(
        :Al, :Mn, :Na, :Br, :Ce, :Co, :Cr,
        :Cs, :Eu, :Fe, :Hf, :La, :Sc, :Sm,
        :U
    ),
    SendToReport(
        Dispatch( {},
            "Standardized Components",
            OutlineBox,
            {Close( 1 )}
        )
    )
);
```

### [Generate distribution analysis](#generate-distribution-analysis_1)[](#generate-distribution-analysis_1 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Coffee Shop Purchases.jmp");
// Distribution
Distribution(
    Nominal Distribution(
        Column( :Customer )
    ),
    Nominal Distribution(
        Column( :Beverage )
    )
);
```

### [Generate distribution analysis with fitted normal distribution](#generate-distribution-analysis-with-fitted-normal-distribution)[](#generate-distribution-analysis-with-fitted-normal-distribution "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cola Heart Rate.jmp");
// Distribution 2
Distribution(
    Stack( 1 ),
    Continuous Distribution(
        Column( :Heart Rate ),
        Horizontal Layout( 1 ),
        Vertical( 0 ),
        Fit Distribution( Normal ),
        Fit Distribution( Smooth Curve )
    ),
    By( :"Time (Raw)"n )
);
```

### [Perform categorical analysis with crosstab transposed and test for response homogeneity](#perform-categorical-analysis-with-crosstab-transposed-and-test-for-response-homogeneity)[](#perform-categorical-analysis-with-crosstab-transposed-and-test-for-response-homogeneity "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Consumer Preferences.jmp");
// Career by Age Group
Categorical(
    X( :Age Group ),
    Responses(
        :I am working on my career
    ),
    Crosstab Transposed( 1 ),
    Legend( 0 ),
    Test Response Homogeneity( 1 )
);
```

### [Perform categorical analysis with crosstab transposed and test for response homogeneity](#perform-categorical-analysis-with-crosstab-transposed-and-test-for-response-homogeneity_1)[](#perform-categorical-analysis-with-crosstab-transposed-and-test-for-response-homogeneity_1 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Consumer Preferences.jmp");
// Home Needs Improve by School Children
Categorical(
    X( :School Age Children ),
    Responses(
        :
        My home needs some major improvements
    ),
    Crosstab Transposed( 1 ),
    Legend( 0 ),
    Test Response Homogeneity( 1 )
);
```

### [Generate a gaussian process model](#generate-a-gaussian-process-model)[](#generate-a-gaussian-process-model "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Algorithm Data.jmp");
// Model
Gaussian Process(
    Y( :CPU Time ),
    X(
        :Alpha, :Beta, :Gamma, :Algorithm,
        :Compiler
    ),
    Set Correlation Function(
        "Gaussian"
    ),
    Fast GASP( 1 ),
    Block Size( 50 )
);
```

### [Build a predictive model to analyze the impact of ingredient combinations on cake taste using the Fit Model platform.](#build-a-predictive-model-to-analyze-the-impact-of-ingredient-combinations-on-cake-taste-using-the-fit-model-platform)[](#build-a-predictive-model-to-analyze-the-impact-of-ingredient-combinations-on-cake-taste-using-the-fit-model-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Cake Data.jmp");
// Model
Fit Model(
    Effects(
        :Cocoa & RS & Mixture,
        :Sugar & RS & Mixture,
        :Flour & RS & Mixture,
        :Butter & RS & Mixture,
        :Milk & RS & Mixture
    ),
    Y( :Taste ),
    No Intercept( 1 )
);
```

### [Conduct a screening analysis on a design experiment dataset to evaluate the influence of multiple predictor variables on a response variable.](#conduct-a-screening-analysis-on-a-design-experiment-dataset-to-evaluate-the-influence-of-multiple-predictor-variables-on-a-response-variable)[](#conduct-a-screening-analysis-on-a-design-experiment-dataset-to-evaluate-the-influence-of-multiple-predictor-variables-on-a-response-variable "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Piepel.jmp");
// Screening
Screening( Y( :Y ), X( :X1, :X2, :X3 ) );
```

### [Fit a linear regression model with multiple factors and categorical effects using the Fit Model platform.](#fit-a-linear-regression-model-with-multiple-factors-and-categorical-effects-using-the-fit-model-platform)[](#fit-a-linear-regression-model-with-multiple-factors-and-categorical-effects-using-the-fit-model-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Wine Data.jmp");
// Model
Fit Model(
    Effects(
        :Rater, :Variety, :Field,
        :"De-Stem"n, :Yeast, :Temperature,
        :Press, :Barrel Age,
        :Barrel Seasoning, :Filtering
    ),
    Y( :Rating )
);
```

### [Fit an ordinal logistic regression model to predict an ordinal response variable using multiple predictor effects in the Fit Model platform.](#fit-an-ordinal-logistic-regression-model-to-predict-an-ordinal-response-variable-using-multiple-predictor-effects-in-the-fit-model-platform)[](#fit-an-ordinal-logistic-regression-model-to-predict-an-ordinal-response-variable-using-multiple-predictor-effects-in-the-fit-model-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Diabetes.jmp");
// Logistic for Y Ordinal
Fit Model(
    Y( :Y Ordinal ),
    Effects(
        :Age, :Gender, :BMI, :BP,
        :Total Cholesterol, :LDL, :HDL,
        :TCH, :LTG, :Glucose
    ),
    Personality( "Ordinal Logistic" ),
    Run( Likelihood Ratio Tests( 1 ) )
);
```

### [Create a control chart with individual measurement, no center line, and no control limits.](#create-a-control-chart-with-individual-measurement-no-center-line-and-no-control-limits)[](#create-a-control-chart-with-individual-measurement-no-center-line-and-no-control-limits "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/DiceRolls.jmp");
// Plot Results
Control Chart(
    KSigma( 3 ),
    Range Span( 1 ),
    Chart Col(
        :Average,
        Individual Measurement(
            Show Center Line( 0 ),
            Show Control Limits( 0 )
        )
    )
);
```

### [Analyze the distribution of Quack's Weight Change and Quick's Weight Change columns in the Diet.jmp data table, performing a test of mean for each column.](#analyze-the-distribution-of-quacks-weight-change-and-quicks-weight-change-columns-in-the-dietjmp-data-table-performing-a-test-of-mean-for-each-column)[](#analyze-the-distribution-of-quacks-weight-change-and-quicks-weight-change-columns-in-the-dietjmp-data-table-performing-a-test-of-mean-for-each-column "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Diet.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :Quack's Weight Change ),
        Test Mean( 0 )
    ),
    Continuous Distribution(
        Column( :Quick's Weight Change ),
        Test Mean( 0 )
    )
);
```

### [Analyze the distribution of continuous data in the Drug Toxicity dataset using the Distribution platform.](#analyze-the-distribution-of-continuous-data-in-the-drug-toxicity-dataset-using-the-distribution-platform)[](#analyze-the-distribution-of-continuous-data-in-the-drug-toxicity-dataset-using-the-distribution-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Drug Toxicity.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :Toxicity )
    )
);
```

### [Analyze the distribution of categorical variables using the Distribution platform.](#analyze-the-distribution-of-categorical-variables-using-the-distribution-platform)[](#analyze-the-distribution-of-categorical-variables-using-the-distribution-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Employee Taste.jmp");
// Distribution
Distribution(
    Nominal Distribution( Column( :TV ) ),
    Nominal Distribution(
        Column( :Film )
    ),
    Nominal Distribution(
        Column( :Art )
    ),
    Nominal Distribution(
        Column( :Restaurant )
    )
);
```

### [Perform a Cartesian join between two data tables using the 'Join' function.](#perform-a-cartesian-join-between-two-data-tables-using-the-join-function)[](#perform-a-cartesian-join-between-two-data-tables-using-the-join-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Species2.jmp");
// Cartesian join
Open( "$SAMPLE_DATA/Species1.jmp" ) <<
Join(
    With( Data Table( "Species2" ) ),
    Cartesian Join
);
```

### [Fit a linear regression model to analyze the effect of various ingredients and conditions on the strength of bread dough.](#fit-a-linear-regression-model-to-analyze-the-effect-of-various-ingredients-and-conditions-on-the-strength-of-bread-dough)[](#fit-a-linear-regression-model-to-analyze-the-effect-of-various-ingredients-and-conditions-on-the-strength-of-bread-dough "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Flrpaste.jmp");
// Model
Fit Model(
    Effects(
        :Liquid, :Sugar, :Flour, :Sifted,
        :Type, :Temp, :Salt, :Clamp,
        :Coat
    ),
    Y( :Strength )
);
```

### [Fit a multiple regression model with interactions between predictors using the Fit Model platform.](#fit-a-multiple-regression-model-with-interactions-between-predictors-using-the-fit-model-platform)[](#fit-a-multiple-regression-model-with-interactions-between-predictors-using-the-fit-model-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Functional Data/Simple Linear Functional Data.jmp");
// Model
Fit Model(
    Effects(
        :X1, :X2, :X3, :X1 * :X2,
        :X1 * :X3, :X2 * :X3
    ),
    Y( :Y )
);
```

### [Perform multivariate analysis of variance (MANOVA) using the Fit Model platform with Distance and Durability as response variables and Brand as a fixed effect.](#perform-multivariate-analysis-of-variance-manova-using-the-fit-model-platform-with-distance-and-durability-as-response-variables-and-brand-as-a-fixed-effect)[](#perform-multivariate-analysis-of-variance-manova-using-the-fit-model-platform-with-distance-and-durability-as-response-variables-and-brand-as-a-fixed-effect "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Golf Balls.jmp");
// MANOVA
Fit Model(
    Y( :Distance, :Durability ),
    Effects( :Brand ),
    Personality( "Manova" ),
    Run
);
```

### [Perform association analysis of products using the Association Analysis platform.](#perform-association-analysis-of-products-using-the-association-analysis-platform)[](#perform-association-analysis-of-products-using-the-association-analysis-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Grocery Purchases.jmp");
// Association Analysis of Product
Association Analysis(
    Item( :Product ),
    ID( :Customer ID )
);
```

### [Create a bivariate analysis with a fit line, quadratic fit, cubic fit, and cubic spline in the Bivariate platform.](#create-a-bivariate-analysis-with-a-fit-line-quadratic-fit-cubic-fit-and-cubic-spline-in-the-bivariate-platform)[](#create-a-bivariate-analysis-with-a-fit-line-quadratic-fit-cubic-fit-and-cubic-spline-in-the-bivariate-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Growth.jmp");
// Bivariate
Bivariate(
    Y( :ratio ),
    X( :age ),
    Fit Line,
    Fit Polynomial( 2 ),
    Fit Polynomial( 3 ),
    Fit Spline( 1000 )
);
```

### [Create a variability chart with nested model analysis using EMS, REML, and Bayesian methods, incorporating standard deviation and gauge RR reports.](#create-a-variability-chart-with-nested-model-analysis-using-ems-reml-and-bayesian-methods-incorporating-standard-deviation-and-gauge-rr-reports)[](#create-a-variability-chart-with-nested-model-analysis-using-ems-reml-and-bayesian-methods-incorporating-standard-deviation-and-gauge-rr-reports "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Hardware Surface Unit Data.jmp");
// Variability Chart
Variability Chart(
    Y( :X ),
    X( :Ship event, :Lot ),
    Model( "Nested" ),
    Max Iter( 100 ),
    Conv Limit( 0.00000001 ),
    Number Integration Abscissas( 128 ),
    Number Function Evals( 65536 ),
    Analysis Type(
        "Choose best analysis (EMS REML Bayesian)"n
    ),
    Std Dev Chart( 1 ),
    Gauge RR Report( 1 )
);
```

### [Generate a Pareto Plot to identify the primary causes of surface quality issues from the Hardware Surface Unit Data.](#generate-a-pareto-plot-to-identify-the-primary-causes-of-surface-quality-issues-from-the-hardware-surface-unit-data)[](#generate-a-pareto-plot-to-identify-the-primary-causes-of-surface-quality-issues-from-the-hardware-surface-unit-data "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Hardware Surface Unit Data.jmp");
// Pareto Plot
Pareto Plot( Cause( :surface quality ) );
```

### [Generate a Shewhart Poisson control chart for a binary surface quality variable using the Control Chart Builder platform.](#generate-a-shewhart-poisson-control-chart-for-a-binary-surface-quality-variable-using-the-control-chart-builder-platform)[](#generate-a-shewhart-poisson-control-chart-for-a-binary-surface-quality-variable-using-the-control-chart-builder-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Hardware Surface Unit Data.jmp");
// Control Chart Builder 3
Control Chart Builder(
    Size( 524, 450 ),
    Show Control Panel( 0 ),
    Show Capability( 0 ),
    Class( Shewhart Attribute ),
    Variables( Y( :surface quality ) ),
    Chart(
        Points( Statistic( "Count" ) ),
        Limits( Sigma( "Poisson" ) )
    )
);
```

### [Perform univariate distribution analysis on nominal and continuous variables.](#perform-univariate-distribution-analysis-on-nominal-and-continuous-variables)[](#perform-univariate-distribution-analysis-on-nominal-and-continuous-variables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Htwt12.jmp");
// Distribution
Distribution(
    Nominal Distribution(
        Column( :Gender )
    ),
    Continuous Distribution(
        Column( :Height )
    )
);
```

### [Perform a one-way analysis of a dataset with Height as the dependent variable and Gender as the independent variable, including mean calculations and mean diamond plots.](#perform-a-one-way-analysis-of-a-dataset-with-height-as-the-dependent-variable-and-gender-as-the-independent-variable-including-mean-calculations-and-mean-diamond-plots)[](#perform-a-one-way-analysis-of-a-dataset-with-height-as-the-dependent-variable-and-gender-as-the-independent-variable-including-mean-calculations-and-mean-diamond-plots "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Htwt15.jmp");
// Oneway
Oneway(
    Y( :Height ),
    X( :Gender ),
    Means( 1 ),
    Box Plots( 0 ),
    Mean Diamonds( 1 )
);
```

### [Fit Johnson Su distribution to continuous data.](#fit-johnson-su-distribution-to-continuous-data)[](#fit-johnson-su-distribution-to-continuous-data "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/JohnsonSuExample.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :x ),
        Fit Distribution( Johnson Su )
    )
);
```

### [Create a loss function template using the Extreme Value distribution with parameters λ and δ .](#create-a-loss-function-template-using-the-extreme-value-distribution-with-parameters-and)[](#create-a-loss-function-template-using-the-extreme-value-distribution-with-parameters-and "Click to copy url")

``` jsl
// Extreme Value.jsl
///////////////////////////////////////////////////////////////////////////////////////////////////////////
// JSL to create a loss function template of Extreme value            //
///////////////////////////////////////////////////////////////////////////////////////////////////////////

dt= new table ("Extreme value");
dt<<New Column("Time", Numeric,continuous);   
dt<<New Column("Censor", Numeric,continuous);
dt<<New Column("Extreme value", Numeric,continuous);
col=column( "Extreme value");
col<<formula(  Parameter({lambda=3.26944897591195, delta=0.94478144505066}, -IfMZ( :Censor==0, ((-Log(delta))-Exp((Log( :Time/100)-lambda)/delta))+(Log( :Time)/100-lambda)/delta, -Exp((Log( :Time/100)-lambda)/delta))) );
```

### [Fit a nominal logistic regression model to analyze the effect of smoking on lung cancer.](#fit-a-nominal-logistic-regression-model-to-analyze-the-effect-of-smoking-on-lung-cancer)[](#fit-a-nominal-logistic-regression-model-to-analyze-the-effect-of-smoking-on-lung-cancer "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Lung Cancer Choice.jmp");
// Model
Fit Model(
    Freq( :Count ),
    Y( :Lung Cancer ),
    Effects( :Smoker ),
    Personality( "Nominal Logistic" )
);
```

### [Calculate distribution statistics for nominal variables with frequencies.](#calculate-distribution-statistics-for-nominal-variables-with-frequencies)[](#calculate-distribution-statistics-for-nominal-variables-with-frequencies "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Mb-dist.jmp");
// Distribution
Distribution(
    Freq( :Count ),
    Nominal Distribution(
        Column( :TYPE )
    )
);
```

### [Open the main data table and simultaneously open the Profile and Subject tables.](#open-the-main-data-table-and-simultaneously-open-the-profile-and-subject-tables)[](#open-the-main-data-table-and-simultaneously-open-the-profile-and-subject-tables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Pizza Responses.jmp");
// Open Profile and Subject Tables
Open( "$Sample_Data/Pizza Subjects.jmp" );
Open( "$Sample_Data/Pizza Profiles.jmp" );
```

### [Calculate factor score correlations for specified variables in the Online Consumer Data table using the Multivariate platform with row-wise estimation method and display the results in a square matrix format with scatterplot matrix and shaded ellipses.](#calculate-factor-score-correlations-for-specified-variables-in-the-online-consumer-data-table-using-the-multivariate-platform-with-row-wise-estimation-method-and-display-the-results-in-a-square-matrix-format-with-scatterplot-matrix-and-shaded-ellipses)[](#calculate-factor-score-correlations-for-specified-variables-in-the-online-consumer-data-table-using-the-multivariate-platform-with-row-wise-estimation-method-and-display-the-results-in-a-square-matrix-format-with-scatterplot-matrix-and-shaded-ellipses "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Online Consumer Data.jmp");
// Factor Score Correlations
Multivariate(
    Y(
        :Privacy, :Security, :Reputation,
        :Trust, :Purchase Int
    ),
    Estimation Method( "Row-wise" ),
    Matrix Format( "Square" ),
    Scatterplot Matrix(
        Density Ellipses( 0 ),
        Shaded Ellipses( 0 )
    ),
    Color Map on Correlations( 1 )
);
```

### [Perform logistic regression on the O-Ring Failure data table, predicting the Response variable using Temperature as the predictor, and calculate the inverse prediction for a Response value of 0.00063.](#perform-logistic-regression-on-the-o-ring-failure-data-table-predicting-the-response-variable-using-temperature-as-the-predictor-and-calculate-the-inverse-prediction-for-a-response-value-of-000063)[](#perform-logistic-regression-on-the-o-ring-failure-data-table-predicting-the-response-variable-using-temperature-as-the-predictor-and-calculate-the-inverse-prediction-for-a-response-value-of-000063 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/O-Ring Failure.jmp");
// Logistic
Logistic(
    Y( Response ),
    X( Temperature ),
    Inverse Prediction(
        Response( 0.00063 )
    )
);
```

### [Perform Partial Least Squares regression with Y variable log RAI and multiple X variables including :S1, :L1, :P1, :S2, :L2, :P2, :S3, :L3, :P3, :S4, :L4, :P4, :S5, :L5, :P5 using the Partial Least Squares function.](#perform-partial-least-squares-regression-with-y-variable-log-rai-and-multiple-x-variables-including-s1-l1-p1-s2-l2-p2-s3-l3-p3-s4-l4-p4-s5-l5-p5-using-the-partial-least-squares-function)[](#perform-partial-least-squares-regression-with-y-variable-log-rai-and-multiple-x-variables-including-s1-l1-p1-s2-l2-p2-s3-l3-p3-s4-l4-p4-s5-l5-p5-using-the-partial-least-squares-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Penta.jmp");
// Partial Least Squares
Partial Least Squares(
    Y( :log RAI ),
    X(
        :S1, :L1, :P1, :S2, :L2, :P2, :S3,
        :L3, :P3, :S4, :L4, :P4, :S5, :L5,
        :P5
    ),
    Go
);
```

### [Construct a choice model using the One Table option, Subject ID, Choice Set ID, Profile ID, and Profile Effects for Crust, Cheese, and Topping from the Pizza Combined.jmp dataset. Additionally, enable Firth Bias-Adjusted Estimates and Likelihood Ratio Tests.](#construct-a-choice-model-using-the-one-table-option-subject-id-choice-set-id-profile-id-and-profile-effects-for-crust-cheese-and-topping-from-the-pizza-combinedjmp-dataset-additionally-enable-firth-bias-adjusted-estimates-and-likelihood-ratio-tests)[](#construct-a-choice-model-using-the-one-table-option-subject-id-choice-set-id-profile-id-and-profile-effects-for-crust-cheese-and-topping-from-the-pizza-combinedjmp-dataset-additionally-enable-firth-bias-adjusted-estimates-and-likelihood-ratio-tests "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Pizza Combined.jmp");
// Choice
Choice(
    One Table( 1 ),
    Subject ID( :Subject ),
    Choice Set ID( :Trial ),
    Profile ID( :Indicator ),
    Profile Effects(
        :Crust, :Cheese, :Topping
    ),
    "Firth Bias-Adjusted Estimates"n( 1 ),
    Likelihood Ratio Tests( 1 )
);
```

### [Imperative sentence: Create a bivariate plot of the edge variable against the nub variable using the Bivariate platform.](#imperative-sentence-create-a-bivariate-plot-of-the-edge-variable-against-the-nub-variable-using-the-bivariate-platform)[](#imperative-sentence-create-a-bivariate-plot-of-the-edge-variable-against-the-nub-variable-using-the-bivariate-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Pollen.jmp");
// Bivariate
Bivariate( Y( :edge ), X( :nub ) );
```

### [Create a bivariate plot to visualize the relationship between F Rate 60+ and F Rate 0-19 from the PopAgeGroup data table.](#create-a-bivariate-plot-to-visualize-the-relationship-between-f-rate-60-and-f-rate-0-19-from-the-popagegroup-data-table)[](#create-a-bivariate-plot-to-visualize-the-relationship-between-f-rate-60-and-f-rate-0-19-from-the-popagegroup-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/PopAgeGroup.jmp");
// Gender Portion
Bivariate(
    Y( :"F Rate 60+"n ),
    X( :"F Rate 0-19"n ),
    SendToReport(
        Dispatch( {}, "Bivar Plot",
            FrameBox,
            {Frame Size( 706, 434 ),
            Marker Drawing Mode( "Fast" )
            }
        )
    )
);
```

### [Exclude the last 100 rows of data from the current active data table.](#exclude-the-last-100-rows-of-data-from-the-current-active-data-table)[](#exclude-the-last-100-rows-of-data-from-the-current-active-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Polyethylene Process.jmp");
// Set currrent data as excluded
dt = Current Data Table();
lastRow = N Rows( dt );
For( i = 101, i <= lastRow, i++,
    Row State( i ) = Excluded State( 1 )
);
```

### [Generate distribution analysis for continuous variables in the specified data table using the Distribution platform.](#generate-distribution-analysis-for-continuous-variables-in-the-specified-data-table-using-the-distribution-platform)[](#generate-distribution-analysis-for-continuous-variables-in-the-specified-data-table-using-the-distribution-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Primes.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :Prime )
    ),
    Continuous Distribution(
        Column( :Delta )
    ),
    Continuous Distribution(
        Column( :DeltaDelta )
    )
);
```

### [Create a U Chart with a Weighted Moving Average Chart (UWMA) for a sample data table in the Quality Control platform.](#create-a-u-chart-with-a-weighted-moving-average-chart-uwma-for-a-sample-data-table-in-the-quality-control-platform)[](#create-a-u-chart-with-a-weighted-moving-average-chart-uwma-for-a-sample-data-table-in-the-quality-control-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Clips1.jmp");
// UWMA Chart
Control Chart(
    Sample Label( :Status ),
    Sample Size( 5 ),
    K Sigma( 3 ),
    Moving Average Span( 2 ),
    Chart Col( :Gap, UWMA )
);
```

### [Build a control chart for a quality control process using the Control Chart Builder function .](#build-a-control-chart-for-a-quality-control-process-using-the-control-chart-builder-function)[](#build-a-control-chart-for-a-quality-control-process-using-the-control-chart-builder-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Combined.jmp");
// Control Chart Builder
Control Chart Builder(
    Show Capability( 0 ),
    Variables(
        Subgroup( :Run ),
        Y( :Length )
    ),
    Chart( Position( 1 ) ),
    Chart( Position( 2 ) )
);
```

### [Construct a control chart using the Control Chart Builder platform with DAY as the subgroup variable and DIAMETER as the response variable, displaying both the average and range subgroups with connecting lines and sigma limits.](#construct-a-control-chart-using-the-control-chart-builder-platform-with-day-as-the-subgroup-variable-and-diameter-as-the-response-variable-displaying-both-the-average-and-range-subgroups-with-connecting-lines-and-sigma-limits)[](#construct-a-control-chart-using-the-control-chart-builder-platform-with-day-as-the-subgroup-variable-and-diameter-as-the-response-variable-displaying-both-the-average-and-range-subgroups-with-connecting-lines-and-sigma-limits "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Diameter.jmp");
// Control Chart Builder
Control Chart Builder(
    Show Control Panel( 0 ),
    Variables(
        "Subgroup"(:DAY), "Y"(:DIAMETER)
    ),
    Chart(
        Position( 1 ),
        Points( Statistic( "Average" ) ),
        Limits( Sigma( "Range" ) ),
        Connecting Line( 1 )
    ),
    Chart(
        Position( 2 ),
        Points( Statistic( "Range" ) ),
        Limits( Sigma( "Range" ) ),
        Connecting Line( 1 )
    )
);
```

### [Generate a C Chart using the Control Chart Builder function to visualize defect counts per unit.](#generate-a-c-chart-using-the-control-chart-builder-function-to-visualize-defect-counts-per-unit)[](#generate-a-c-chart-using-the-control-chart-builder-function-to-visualize-defect-counts-per-unit "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Fabric.jmp");
// Control Chart Builder: C Chart
Control Chart Builder(
    Show Control Panel( 0 ),
    Class( "Shewhart Attribute" ),
    Variables(
        Subgroup( :Bolt ),
        Y( :Flaws )
    ),
    Chart(
        Points( Statistic( "Count" ) ),
        Limits( Sigma( "Poisson" ) )
    )
);
```

### [Generate a Pareto plot displaying the top causes of failures using categorical variables and frequency counts.](#generate-a-pareto-plot-displaying-the-top-causes-of-failures-using-categorical-variables-and-frequency-counts)[](#generate-a-pareto-plot-displaying-the-top-causes-of-failures-using-categorical-variables-and-frequency-counts "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Failure3ID.jmp");
// Pareto Plot
Pareto Plot(
    Cause( :failure ),
    X( :clean, :date ),
    Freq( :N )
);
```

### [Perform Categorical Multivariate ID Analysis using the Freq, ID, X, Multiple Response by ID, and Sample Size functions.](#perform-categorical-multivariate-id-analysis-using-the-freq-id-x-multiple-response-by-id-and-sample-size-functions)[](#perform-categorical-multivariate-id-analysis-using-the-freq-id-x-multiple-response-by-id-and-sample-size-functions "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Failure3ID.jmp");
// Cat MultID
Categorical(
    Freq( :N ),
    ID( :ID ),
    X( :clean ),
    Multiple Response by ID( :failure ),
    Sample Size( :SampleSize )
);
```

### [Create a Pareto plot to visualize the rate of occurrences for different causes across various processes in the Quality Control data table.](#create-a-pareto-plot-to-visualize-the-rate-of-occurrences-for-different-causes-across-various-processes-in-the-quality-control-data-table)[](#create-a-pareto-plot-to-visualize-the-rate-of-occurrences-for-different-causes-across-various-processes-in-the-quality-control-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Failuressize.jmp");
// Pareto Plot - Rate
Pareto Plot(
    Cause( :Causes ),
    X( :Process ),
    Freq( :Count ),
    Per Unit Rates( 1 ),
    Test Rates Across Groups( 1 ),
    Cause[1] << Colors( "Red" ),
    Cause[2] << Colors( "Purple" ),
    Cause[4] << Colors( "BlueGreen" ),
    Cause[5] << Colors( "Yellow" ),
    Cause[6] << Colors( "Blue" ),
    Cause[7] << Colors( "Orange" )
);
```

### [Generate a normal quantile plot for a continuous distribution analysis of the Hours between Burnouts column in the Fan Burnout data table using the Distribution platform .](#generate-a-normal-quantile-plot-for-a-continuous-distribution-analysis-of-the-hours-between-burnouts-column-in-the-fan-burnout-data-table-using-the-distribution-platform)[](#generate-a-normal-quantile-plot-for-a-continuous-distribution-analysis-of-the-hours-between-burnouts-column-in-the-fan-burnout-data-table-using-the-distribution-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Fan Burnout.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :Hours between Burnouts ),
        Normal Quantile Plot( 1 )
    )
);
```

### [Generate individual and moving range control charts using the Control Chart Builder platform.](#generate-individual-and-moving-range-control-charts-using-the-control-chart-builder-platform)[](#generate-individual-and-moving-range-control-charts-using-the-control-chart-builder-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Fan Burnout.jmp");
// Control Chart Builder Individual and Moving Range Charts
Control Chart Builder(
    Show Control Panel( 0 ),
    Variables(
        Subgroup( :Burnout ),
        Y( :Hours between Burnouts )
    ),
    Chart(
        Position( 1 ),
        Limits( Spec Limits( 1 ) )
    ),
    Chart( Position( 2 ) ),
    SendToReport(
        Dispatch( {}, "Burnout", ScaleBox,
            {Min( 0 ), Max( 26 ),
            Inc( 2 ), Minor Ticks( 0 )}
        )
    )
);
```

### [Sort the data table by the Shuffle column in ascending order, creating a new output table called Sort of Join of Chocolate Factory with Untitled 3 by Shuffle.](#sort-the-data-table-by-the-shuffle-column-in-ascending-order-creating-a-new-output-table-called-sort-of-join-of-chocolate-factory-with-untitled-3-by-shuffle)[](#sort-the-data-table-by-the-shuffle-column-in-ascending-order-creating-a-new-output-table-called-sort-of-join-of-chocolate-factory-with-untitled-3-by-shuffle "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Fancy Chocolate Factory.jmp");
// Source
Data Table(
    "Join of Chocolate Factory with Untitled 3"
) << Sort(
    By( :Shuffle ),
    Order( Ascending ),
    Output Table(
        "Sort of Join of Chocolate Factory with Untitled 3 by Shuffle"
    )
);
```

### [Perform principal component analysis (PCA) on variables using the on Correlations option.](#perform-principal-component-analysis-pca-on-variables-using-the-on-correlations-option)[](#perform-principal-component-analysis-pca-on-variables-using-the-on-correlations-option "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Flight Delays.jmp");
// Principal Components
Principal Components(
    Y(
        :AA, :CO, :DL, :F9, :FL, :NW, :UA,
        :US, :WN
    ),
    Estimation Method( "Default" ),
    "on Correlations"
);
```

### [Create a Model-Driven Multivariate Control Chart using historical data.](#create-a-model-driven-multivariate-control-chart-using-historical-data)[](#create-a-model-driven-multivariate-control-chart-using-historical-data "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Flight Delays.jmp");
// Original data with historical
Model Driven Multivariate Control Chart(
    Process(
        :AA, :CO, :DL, :F9, :FL, :NW, :UA,
        :US, :WN
    ),
    Time ID( :Flight date ),
    Historical Data End at Row( 16 ),
    Score Plot(
        Score Ellipse Coverage( 0.95 )
    )
);
```

### [Create a Cusum Chart to monitor the weight process with specified control parameters.](#create-a-cusum-chart-to-monitor-the-weight-process-with-specified-control-parameters)[](#create-a-cusum-chart-to-monitor-the-weight-process-with-specified-control-parameters "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Oil1 Cusum.jmp");
// Cusum Chart
Control Chart(
    Sample Size( :hour ),
    H( 2 ),
    Chart Col(
        :weight,
        CUSUM(
            Two sided( 1 ),
            Target( 8.1 ),
            Delta( 1 ),
            Sigma( 0.05 ),
            Head Start( 0.05 )
        )
    )
);
```

### [Construct a multivariate control chart using the Multivariate Control Chart function .](#construct-a-multivariate-control-chart-using-the-multivariate-control-chart-function)[](#construct-a-multivariate-control-chart-using-the-multivariate-control-chart-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Thickness.jmp");
// Multivariate Control Chart
Multivariate Control Chart(
    Y(
        :Thickness 01, :Thickness 02,
        :Thickness 03, :Thickness 04,
        :Thickness 05, :Thickness 06,
        :Thickness 07, :Thickness 08,
        :Thickness 09, :Thickness 10,
        :Thickness 11, :Thickness 12
    ),
    T Square Partitioned( 1 ),
    Principal Components( 1 ),
    Set Alpha Level(
        0.00270000000000004
    )
);
```

### [Construct an NP Chart using the Control Chart Builder to analyze the number of defective items in subgroups with varying lot sizes.](#construct-an-np-chart-using-the-control-chart-builder-to-analyze-the-number-of-defective-items-in-subgroups-with-varying-lot-sizes)[](#construct-an-np-chart-using-the-control-chart-builder-to-analyze-the-number-of-defective-items-in-subgroups-with-varying-lot-sizes "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Washers.jmp");
// Control Chart Builder: NP Chart
Control Chart Builder(
    Show Control Panel( 0 ),
    Class( "Shewhart Attribute" ),
    Variables(
        Subgroup( :Lot ),
        Y( :"# defective"n ),
        n Trials( :Lot Size )
    ),
    Chart(
        Points( Statistic( "Count" ) ),
        Limits( Sigma( "Binomial" ) )
    )
);
```

### [Perform a detailed Recurrence Analysis on bladder cancer data by fitting a multi-state model, calculating cost, comparing different treatment groups, and labeling patients.](#perform-a-detailed-recurrence-analysis-on-bladder-cancer-data-by-fitting-a-multi-state-model-calculating-cost-comparing-different-treatment-groups-and-labeling-patients)[](#perform-a-detailed-recurrence-analysis-on-bladder-cancer-data-by-fitting-a-multi-state-model-calculating-cost-comparing-different-treatment-groups-and-labeling-patients "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Reliability/Bladder Cancer.jmp");
// Recurrence Analysis
Recurrence Analysis(
    Y( :Age ),
    Cost( :Cost ),
    Grouping( :Treatment Group ),
    Label( :Patient Number ),
    Plot MCF Differences( 1 )
);
```

### [Create a survival analysis using time cycles, censor status, and grouping variables.](#create-a-survival-analysis-using-time-cycles-censor-status-and-grouping-variables)[](#create-a-survival-analysis-using-time-cycles-censor-status-and-grouping-variables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Reliability/Blenders.jmp");
// Survival
Survival(
    Y( :Time Cycles ),
    Censor( :Censor ),
    Grouping( :Group )
);
```

### [Perform reliability growth analysis using the Piecewise Weibull NHPP model for change point detection on the BrakeReliability data set.](#perform-reliability-growth-analysis-using-the-piecewise-weibull-nhpp-model-for-change-point-detection-on-the-brakereliability-data-set)[](#perform-reliability-growth-analysis-using-the-piecewise-weibull-nhpp-model-for-change-point-detection-on-the-brakereliability-data-set "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Reliability/BrakeReliability.jmp");
// Reliability Growth
Reliability Growth(
    Input Format( Dates ),
    Timestamp( :Date ),
    Event Count( :Fixes ),
    Piecewise Weibull NHPP Change Point Detection
);
```

### [Fit a Parametric Survival Model using the LogNormal distribution with the Personality set to Parametric Survival and include the effect of variable x.](#fit-a-parametric-survival-model-using-the-lognormal-distribution-with-the-personality-set-to-parametric-survival-and-include-the-effect-of-variable-x)[](#fit-a-parametric-survival-model-using-the-lognormal-distribution-with-the-personality-set-to-parametric-survival-and-include-the-effect-of-variable-x "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Reliability/Devalt.jmp");
// Parametric Survival Model
Fit Model(
    Weight( :Censor ),
    Freq( :Weight ),
    Y( :Hours ),
    Censor( :Censor ),
    Censor Code( 1 ),
    Effects( :x ),
    Personality( "Parametric Survival" ),
    Distribution( LogNormal )
);
```

### [Fit Parametric Survival model using LogNormal distribution and perform Likelihood Ratio Tests and Estimate Time Quantile analysis.](#fit-parametric-survival-model-using-lognormal-distribution-and-perform-likelihood-ratio-tests-and-estimate-time-quantile-analysis)[](#fit-parametric-survival-model-using-lognormal-distribution-and-perform-likelihood-ratio-tests-and-estimate-time-quantile-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Reliability/Comptime.jmp");
// Fit Parametric Survival
obj =
Fit Model(
    Y( :ExecTime ),
    Effects( :Load ),
    Personality( "Parametric Survival" ),
    Distribution( LogNormal ),
    Run
);
obj << Likelihood Ratio Tests( 1 );
obj <<
Estimate Time Quantile(
    :Load = 5,
    [0.1],
    Alpha( 0.05 )
);
```

### [Analyze and visualize the distribution of tip percentages by server in the Restaurant Tips dataset using the Distribution platform.](#analyze-and-visualize-the-distribution-of-tip-percentages-by-server-in-the-restaurant-tips-dataset-using-the-distribution-platform)[](#analyze-and-visualize-the-distribution-of-tip-percentages-by-server-in-the-restaurant-tips-dataset-using-the-distribution-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Restaurant Tips.jmp");
// Distribution: Tip % by Server
Distribution(
    Stack( 1 ),
    Continuous Distribution(
        Column( :Tip Percentage ),
        Horizontal Layout( 1 ),
        Vertical( 0 )
    ),
    By( :Server )
);
```

### [Perform one-way analysis of variance comparing Fahrenheit temperatures across different types of spaces, featuring post-hoc comparisons, ANOM charts, box plots, and comparison circles.](#perform-one-way-analysis-of-variance-comparing-fahrenheit-temperatures-across-different-types-of-spaces-featuring-post-hoc-comparisons-anom-charts-box-plots-and-comparison-circles)[](#perform-one-way-analysis-of-variance-comparing-fahrenheit-temperatures-across-different-types-of-spaces-featuring-post-hoc-comparisons-anom-charts-box-plots-and-comparison-circles "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/S4 Temps.jmp");
// Oneway - Type of Space
Oneway(
    Y( :fahrenheit ),
    X( :type of space ),
    Each Pair(
        1,
        LSD Threshold Matrix( 0 ),
        Ordered Differences Report( 0 )
    ),
    ANOM( 1 ),
    Box Plots( 1 ),
    Comparison Circles( 1 )
);
```

### [Create a control chart using the moving average with specifications limits.](#create-a-control-chart-using-the-moving-average-with-specifications-limits)[](#create-a-control-chart-using-the-moving-average-with-specifications-limits "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Stock Averages.jmp");
// Control Chart Builder: Moving Average
Control Chart Builder(
    Variables(
        Subgroup( :Date ),
        Y( :Moving Average )
    ),
    Chart(
        Position( 1 ),
        Limits( Spec Limits( 1 ) )
    ),
    Chart( Position( 2 ) ),
    Show Control Panel( 0 )
);
```

### [Build a linear regression model using the Fit Model function with multiple predictors.](#build-a-linear-regression-model-using-the-fit-model-function-with-multiple-predictors)[](#build-a-linear-regression-model-using-the-fit-model-function-with-multiple-predictors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Supersaturated.jmp");
// Model
Fit Model(
    Effects(
        :X1, :X2, :X3, :X4, :X5, :X6, :X7,
        :X8, :X9, :X10, :X11, :X12, :X13,
        :X14, :X15, :X16, :X17, :X18
    ),
    Y( :Y ),
    Personality(
        "Standard Least Squares"
    ),
    Emphasis( "Minimal Report" )
);
```

### [Perform a one-way ANOVA analysis on typing speed data by brand.](#perform-a-one-way-anova-analysis-on-typing-speed-data-by-brand)[](#perform-a-one-way-anova-analysis-on-typing-speed-data-by-brand "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Typing Data.jmp");
// Oneway
Oneway(
    Y( :speed ),
    X( :brand ),
    Means( 1 ),
    All Pairs( 1 )
);
```

### [Perform Multiple Correspondence Analysis on a dataset with Year as the dependent variable, Region and ID as supplementary variables, and Population as the frequency variable, including chi-square measures and totals in the cross tables.](#perform-multiple-correspondence-analysis-on-a-dataset-with-year-as-the-dependent-variable-region-and-id-as-supplementary-variables-and-population-as-the-frequency-variable-including-chi-square-measures-and-totals-in-the-cross-tables)[](#perform-multiple-correspondence-analysis-on-a-dataset-with-year-as-the-dependent-variable-region-and-id-as-supplementary-variables-and-population-as-the-frequency-variable-including-chi-square-measures-and-totals-in-the-cross-tables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/US Regional Population.jmp");
// Multiple Correspondence Analysis
Multiple Correspondence Analysis(
    Y( :Year ),
    X( :Region ),
    Freq( :Population ),
    Supplementary ID( :ID ),
    Cross Table(
        Cell Chi Square( 0 ),
        Show Total( 1 )
    ),
    Cross Table of Supplementary Rows(
        Cell Chi Square( 0 ),
        Show Total( 1 )
    )
);
```

### [Generate a distribution analysis report, including nominal distribution analysis for the 'Year' column with horizontal layout, and by group for the 'Region' column.](#generate-a-distribution-analysis-report-including-nominal-distribution-analysis-for-the-year-column-with-horizontal-layout-and-by-group-for-the-region-column)[](#generate-a-distribution-analysis-report-including-nominal-distribution-analysis-for-the-year-column-with-horizontal-layout-and-by-group-for-the-region-column "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/US Regional Population.jmp");
// Distribution
Distribution(
    Stack( 1 ),
    Weight( :Population ),
    Nominal Distribution(
        Column( :Year ),
        Horizontal Layout( 1 ),
        Vertical( 0 )
    ),
    By( :Region )
);
```

### [Perform a Variability Chart analysis for crossed and nested factors.](#perform-a-variability-chart-analysis-for-crossed-and-nested-factors)[](#perform-a-variability-chart-analysis-for-crossed-and-nested-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Variability Data/3 Factors Crossed & Nested.jmp");
// Variability Chart - Crossed & Nested
Variability Chart(
    Y( :Y ),
    X( :Operator, :Instrument, :Part ),
    Show Points( 1 ),
    Std Dev Chart( 1 )
);
```

### [Perform a Gauge R&R analysis using a Variability Chart with nested and crossed factors.](#perform-a-gauge-rr-analysis-using-a-variability-chart-with-nested-and-crossed-factors)[](#perform-a-gauge-rr-analysis-using-a-variability-chart-with-nested-and-crossed-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Variability Data/3 Factors Nested & Crossed.jmp");
// Gauge R&R
Variability Chart(
    Y( :Y ),
    X( :Operator, :Instrument, :Part ),
    Model( "Nested then Crossed" ),
    Connect Cell Means( 1 ),
    Mean of Std Dev( 1 )
);
```

### [Construct a variability chart to analyze the process variation using crossed model for the response variable.](#construct-a-variability-chart-to-analyze-the-process-variation-using-crossed-model-for-the-response-variable)[](#construct-a-variability-chart-to-analyze-the-process-variation-using-crossed-model-for-the-response-variable "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Variability Data/Gasket.jmp");
// Variability Chart
Variability Chart(
    Y( :Y ),
    Model( "Crossed" ),
    X( :Operator, :Part ),
    Analysis Type(
        "Choose best analysis (EMS REML)"
    ),
    Variability Analysis(
        :Y,
        Connect Cell Means( 1 ),
        Show Grand Mean( 1 ),
        XBar Control Limits( 1 ),
        S Control Limits( 1 ),
        Mean of Std Dev( 1 ),
        "Gauge R&R Report"n( 1 )
    )
);
```

### [Perform a Type 1 Gauge Analysis on variable Y1 with specified tolerance and reference values. Type 1 Gauge() function is used to generate the analysis, and Type 1 Gauge Metadata() function is used to define the parameters such as Lower Tolerance, Upper Tolerance, Reference, and Resolution.](#perform-a-type-1-gauge-analysis-on-variable-y1-with-specified-tolerance-and-reference-values-type-1-gauge-function-is-used-to-generate-the-analysis-and-type-1-gauge-metadata-function-is-used-to-define-the-parameters-such-as-lower-tolerance-upper-tolerance-reference-and-resolution)[](#perform-a-type-1-gauge-analysis-on-variable-y1-with-specified-tolerance-and-reference-values-type-1-gauge-function-is-used-to-generate-the-analysis-and-type-1-gauge-metadata-function-is-used-to-define-the-parameters-such-as-lower-tolerance-upper-tolerance-reference-and-resolution "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Variability Data/Type 1 Gauge MSA.jmp");
// Type 1 Gauge of Y1
Type 1 Gauge(
    Y( :Y1 ),
    Type 1 Gauge Metadata(
        :
        Y1(
            Lower Tolerance( 49.014 ),
            Upper Tolerance( 51.014 ),
            Reference( 50.014 ),
            Resolution( 0.001 )
        )
    ),
    Type 1 Gauge Analysis( "Y1" )
);
```

### [Perform EMP Measurement Systems Analysis using Crossed Model, Dispersion Chart with Range, and include Average and Dispersion Charts.](#perform-emp-measurement-systems-analysis-using-crossed-model-dispersion-chart-with-range-and-include-average-and-dispersion-charts)[](#perform-emp-measurement-systems-analysis-using-crossed-model-dispersion-chart-with-range-and-include-average-and-dispersion-charts "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Variability Data/Wafer.jmp");
// EMP Measurement Systems Analysis
EMP Measurement Systems Analysis(
    Y( :Y ),
    X( :Operator ),
    Part( :Wafer ),
    Model( "Crossed" ),
    Dispersion Chart Type( "Range" ),
    Average Chart( 1 ),
    Dispersion Chart( 1 )
);
```

### [Analyze continuous data by performing a distribution analysis on the weight column in the Weight Measurements data table.](#analyze-continuous-data-by-performing-a-distribution-analysis-on-the-weight-column-in-the-weight-measurements-data-table)[](#analyze-continuous-data-by-performing-a-distribution-analysis-on-the-weight-column-in-the-weight-measurements-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Weight Measurements.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :weight )
    )
);
```

### [Generate a tabulated report with grouping columns](#generate-a-tabulated-report-with-grouping-columns)[](#generate-a-tabulated-report-with-grouping-columns "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Auto Raw Data.jmp");
// Tabulate (Summary)
Tabulate(
    Set Format(
        Sum(
            Premium USD( 15, 95 ),
            Claim USD( 15, 95 )
        )
    ),
    Add Table(
        Column Table(
            Analysis Columns(
                :Premium USD
            ),
            Statistics( N, Sum )
        ),
        Column Table(
            Analysis Columns(
                :Claim USD
            ),
            Statistics( N, Sum )
        ),
        Row Table(
            Grouping Columns(
                :Branch, :Zone
            )
        )
    )
);
```

### [Fit a standard least squares model with a prediction profiler](#fit-a-standard-least-squares-model-with-a-prediction-profiler)[](#fit-a-standard-least-squares-model-with-a-prediction-profiler "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Auto Raw Data.jmp");
// Fit Model (Claim USD)
Fit Model(
    Y( :Claim USD ),
    Effects(
        :AgeClass, :"City(Y/N)"n,
        :Rating Class
    ),
    Personality(
        "Standard Least Squares"
    ),
    Emphasis( "Minimal Report" ),
    Run(
        Profiler(
            1,
            Confidence Intervals( 1 ),
            Term Value(
                AgeClass( "Elder" ),
                "City(Y/N)"n( "N" ),
                Rating Class( "A" )
            )
        ),
        :Claim USD <<
        {Plot Actual by Predicted( 0 ),
        Plot Regression( 0 ),
        Plot Residual by Predicted( 0 ),
        Plot Effect Leverage( 0 )},
        SendToReport(
            Dispatch(
                {"Response Claim USD",
                "Prediction Profiler"},
                "10000", ScaleBox,
                {
                Format(
                    "Currency",
                    "USD",
                    15,
                    0
                ), Max( 8000 ),
                Inc( 1000 )}
            )
        )
    )
);
```

### [Fit a partial least squares model using the nipals method](#fit-a-partial-least-squares-model-using-the-nipals-method)[](#fit-a-partial-least-squares-model-using-the-nipals-method "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Body Fat.jmp");
// Partial Least Squares
Partial Least Squares(
    Y( :Percent body fat ),
    X(
        :"Age (years)"n, :"Weight (lbs)"n,
        :"Height (inches)"n,
        :"Neck circumference (cm)"n,
        :"Chest circumference (cm)"n,
        :"Abdomen circumference (cm)"n,
        :"Hip circumference (cm)"n,
        :"Thigh circumference (cm)"n,
        :"Knee circumference (cm)"n,
        :"Ankle circumference (cm)"n,
        :
        "Biceps (extended) circumference (cm)"n,
        :"Forearm circumference (cm)"n,
        :"Wrist circumference (cm)"n
    ),
    Validation( :Validation ),
    Initial Number of Factors( 13 ),
    Fit(
        Method( NIPALS ),
        Number of Factors( 7 ),
        Variable Importance Plot( 1 )
    )
);
```

### [Perform distribution analysis](#perform-distribution-analysis_1)[](#perform-distribution-analysis_1 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cars 1993.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :"City Mileage (MPG)"n ),
        Normal Quantile Plot( 1 ),
        Stem and Leaf( 1 )
    ),
    Continuous Distribution(
        Column(
            :"Highway Mileage (MPG)"n
        ),
        Normal Quantile Plot( 1 ),
        Stem and Leaf( 1 )
    ),
    SendToReport(
        Dispatch( {"City Mileage (MPG)"},
            "Distrib Histogram", FrameBox,
            Background Color( 2 )
        ),
        Dispatch(
            {"Highway Mileage (MPG)"},
            "Distrib Histogram", FrameBox,
            Background Color( 2 )
        )
    )
);
```

### [Generate life distribution analysis](#generate-life-distribution-analysis)[](#generate-life-distribution-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Censor Labels.jmp");
// Life Distribution
Life Distribution(
    Y( :Start Time, :End Time ),
    Freq( :Count ),
    Confidence Interval Method( Wald ),
    <<Set Scale( Nonparametric ),
    Interval Type( Simultaneous ),
    <<Set Scriptables( {} ),
    SendToReport(
        Dispatch( {}, "Event Plot",
            OutlineBox,
            {Close( 0 )}
        ),
        Dispatch( {"Event Plot"},
            "Life Distribution", FrameBox,
            {Frame Size( 401, 285 )}
        ),
        Dispatch( {},
            "Compare Distributions",
            OutlineBox,
            {Close( 1 )}
        )
    )
);
```

### [Generate distribution analysis with normal quantile plot](#generate-distribution-analysis-with-normal-quantile-plot)[](#generate-distribution-analysis-with-normal-quantile-plot "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Circuit Board Production.jmp");
// Distribution
Distribution(
    Automatic Recalc( 1 ),
    Nominal Distribution(
        Column( :Day of Week )
    ),
    Continuous Distribution(
        Column( :Time ),
        Normal Quantile Plot( 1 )
    ),
    SendToReport(
        Dispatch( {}, "Distrib Nom Hist",
            FrameBox,
            {DispatchSeg( Hist Seg( 1 ) )
            }
        ),
        Dispatch( {}, "Distrib Histogram",
            FrameBox,
            {DispatchSeg( Hist Seg( 1 ) )
            }
        ),
        Dispatch( {}, "5", ScaleBox,
            {Scale( "Linear" ),
            Min( 0.0533333333333334 ),
            Max( 0.946666666666666 ),
            Inc( 0.08 ), Minor Ticks( 0 ),
            Show Major Grid( 1 ),
            Rotated Labels(
                "Horizontal"
            )}
        ),
        Dispatch( {}, "Quantiles",
            OutlineBox,
            {Close( 1 )}
        )
    )
);
```

### [Generate process capability analysis with specified limits and a goal plot](#generate-process-capability-analysis-with-specified-limits-and-a-goal-plot)[](#generate-process-capability-analysis-with-specified-limits-and-a-goal-plot "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cities.jmp");
// Process Capability
Process Capability(
    Process Variables(
        :OZONE, :CO, :SO2, :NO
    ),
    Spec Limits(
        OZONE(
            LSL( 0 ),
            Target( 0.05 ),
            USL( 0.1 )
        ),
        CO(
            LSL( 5 ),
            Target( 10 ),
            USL( 20 )
        ),
        SO2(
            LSL( 0 ),
            Target( 0.03 ),
            USL( 0.08 )
        ),
        NO(
            LSL( 0 ),
            Target( 0.025 ),
            USL( 0.6 )
        )
    ),
    Goal Plot( 1, Shade Levels( 1 ) )
);
```

### [Perform categorical analysis with crosstab transposed and test for response homogeneity](#perform-categorical-analysis-with-crosstab-transposed-and-test-for-response-homogeneity_2)[](#perform-categorical-analysis-with-crosstab-transposed-and-test-for-response-homogeneity_2 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Consumer Preferences.jmp");
// Categorical Several
Categorical(
    X( :Age Group, :School Age Children ),
    Grouping Option(
        "Each Individually"
    ),
    Responses(
        :I am working on my career
    ),
    Responses(
        :
        My home needs some major improvements
    ),
    Responses(
        :
        I have vast interests outside of work
    ),
    Responses(
        :I come from a large family
    ),
    Crosstab Transposed( 1 ),
    Legend( 0 ),
    Test Response Homogeneity( 1 )
);
```

### [Fit a standard linear regression model to predict Annual Salary Z, incorporating Gender, Length Of Service, and Performance as effects, and suppress detailed diagnostic plots.](#fit-a-standard-linear-regression-model-to-predict-annual-salary-z-incorporating-gender-length-of-service-and-performance-as-effects-and-suppress-detailed-diagnostic-plots)[](#fit-a-standard-linear-regression-model-to-predict-annual-salary-z-incorporating-gender-length-of-service-and-performance-as-effects-and-suppress-detailed-diagnostic-plots "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Employee Master.jmp");
// Fit Model - Annual Salary Z
Fit Model(
    Y( :Annual Salary Z ),
    Effects(
        :Gender, :Length Of Service,
        :Performance
    ),
    Personality(
        "Standard Least Squares"
    ),
    Emphasis( "Minimal Report" ),
    Run(
        :Annual Salary Z <<
        {Summary of Fit( 1 ),
        Analysis of Variance( 1 ),
        Parameter Estimates( 1 ),
        Scaled Estimates( 0 ),
        Plot Actual by Predicted( 0 ),
        Plot Regression( 0 ),
        Plot Residual by Predicted( 0 ),
        Plot Studentized Residuals( 0 ),
        Plot Effect Leverage( 0 ),
        Plot Residual by Normal Quantiles(
            0
        ), Box Cox Y Transformation( 0 )}
    ),
    SendToReport(
        Dispatch(
            {"Response Annual Salary Z"},
            "Effect Tests", OutlineBox,
            {Close( 0 )}
        )
    )
);
```

### [Partition a dataset into clusters using the initial splits and set validation portion.](#partition-a-dataset-into-clusters-using-the-initial-splits-and-set-validation-portion)[](#partition-a-dataset-into-clusters-using-the-initial-splits-and-set-validation-portion "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Hardware Surface Unit Data.jmp");
// Partition 3
Partition(
    Y( :surface quality ),
    X(
        :Part, :Lot, :X, :Y, :Z, :Radius,
        :Center, :Gap, :Slot Width,
        :Slot Length, :Slot Depth, :color
    ),
    Validation Portion( 0.5 ),
    Show Split Prob( 1 ),
    Show Split Count( 1 ),
    Split History( 1 ),
    Informative Missing( 1 ),
    Column Contributions( 1 ),
    Initial Splits(
        :Y < 248.8,
        {:Part == {32}, {}, {:Radius <
        10.6}}
    )
);
```

### [Analyze the distribution of actual impurity levels using a lognormal fit and assess process capability with a specified upper specification limit of 2.5.](#analyze-the-distribution-of-actual-impurity-levels-using-a-lognormal-fit-and-assess-process-capability-with-a-specified-upper-specification-limit-of-25)[](#analyze-the-distribution-of-actual-impurity-levels-using-a-lognormal-fit-and-assess-process-capability-with-a-specified-upper-specification-limit-of-25 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Impurity Process Capability with Detection Limits.jmp");
// Distribution Lognormal Capability
Distribution(
    Continuous Distribution(
        Column( :Actual Impurity ),
        Quantiles( 0 ),
        Summary Statistics( 0 ),
        Always use column properties( 1 ),
        Histogram( 0 ),
        Vertical( 0 ),
        Outlier Box Plot( 0 ),
        Fit Lognormal(
            Process Capability(
                LSL( . ),
                Target( . ),
                USL( 2.5 ),
                Show as Graph Reference Lines
            )
        ),
        Process Capability( 0 )
    ),
    Column Switcher(
        :Actual Impurity,
        {:Actual Impurity,
        :"1.0 Limited Impurity"n,
        :"1.5 Limited Impurity"n,
        :"2.0 Limited Impurity"n,
        :"2.5 Limited Impurity"n}
    )
);
```

### [Analyze the distributions of categorical and continuous variables in the Nicardipine dataset using the Distribution() function .](#analyze-the-distributions-of-categorical-and-continuous-variables-in-the-nicardipine-dataset-using-the-distribution-function)[](#analyze-the-distributions-of-categorical-and-continuous-variables-in-the-nicardipine-dataset-using-the-distribution-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Nicardipine.jmp");
// Distributions
Distribution(
    Nominal Distribution(
        Column(
            :Body System or Organ Class
        ),
        Order By( "Count Ascending" )
    ),
    Nominal Distribution(
        Column( :"Severity/Intensity"n )
    ),
    Nominal Distribution(
        Column( :Serious Event )
    ),
    Continuous Distribution(
        Column( :Age )
    ),
    Nominal Distribution(
        Column( :Sex )
    ),
    Nominal Distribution(
        Column( :Race )
    ),
    Nominal Distribution(
        Column( :Death Description ),
        Order By( "Count Ascending" )
    )
);
```

### [Analyze and visualize the distribution of multiple continuous columns related to olive oil components and the subregion category in the Distribution platform.](#analyze-and-visualize-the-distribution-of-multiple-continuous-columns-related-to-olive-oil-components-and-the-subregion-category-in-the-distribution-platform)[](#analyze-and-visualize-the-distribution-of-multiple-continuous-columns-related-to-olive-oil-components-and-the-subregion-category-in-the-distribution-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Olive Oil.jmp");
// Distribution
Distribution(
    Uniform Scaling( 1 ),
    Continuous Distribution(
        Column( :palmitic )
    ),
    Continuous Distribution(
        Column( :palmitoleic )
    ),
    Continuous Distribution(
        Column( :stearic )
    ),
    Continuous Distribution(
        Column( :oleic )
    ),
    Continuous Distribution(
        Column( :linoleic )
    ),
    Continuous Distribution(
        Column( :linolenic )
    ),
    Continuous Distribution(
        Column( :arachidic )
    ),
    Continuous Distribution(
        Column( :eicosenoic )
    ),
    Nominal Distribution(
        Column( :Subregion ),
        Show Percents( 1 ),
        Mosaic Plot( 1 )
    )
);
```

### [Perform a bivariate analysis with jittering and label offset settings for maximum January temperature points.](#perform-a-bivariate-analysis-with-jittering-and-label-offset-settings-for-maximum-january-temperature-points)[](#perform-a-bivariate-analysis-with-jittering-and-label-offset-settings-for-maximum-january-temperature-points "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Pollutants Map.jmp");
// Bivariate
Bivariate(
    Y( :Y ),
    X( :X ),
    SendToReport(
        Dispatch( {},
            "Bivariate Fit of Y By X",
            OutlineBox,
            {
            Set Title(
                "Highlight Maximum January Temperature Points and Label Them"
            )}
        ),
        Dispatch( {}, "Bivar Plot",
            FrameBox,
            {Frame Size( 476, 313 ),
            DispatchSeg(
                Marker Seg( 1 ),
                label offset(
                    {503, 25, 5},
                    {566, -15, 29}
                )
            )}
        )
    )
);
```

### [Perform a MaxDiff analysis for flavor preference using the Potato Chip Responses, Profiles, and Subjects data tables .](#perform-a-maxdiff-analysis-for-flavor-preference-using-the-potato-chip-responses-profiles-and-subjects-data-tables)[](#perform-a-maxdiff-analysis-for-flavor-preference-using-the-potato-chip-responses-profiles-and-subjects-data-tables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Potato Chip Responses.jmp");
// MaxDiff for Flavor
Open(
    "$Sample_Data/Potato Chip Subjects.jmp"
);
Open(
    "$Sample_Data/Potato Chip Profiles.jmp"
);
MaxDiff(
    Response Data Table(
        Data Table(
            "Potato Chip Responses"
        )
    ),
    Profile DataTable(
        Potato Chip Profiles
    ),
    Subject DataTable(
        Data Table(
            "Potato Chip Subjects"
        )
    ),
    Response Subject ID( :Respondent ),
    Response Profile ID Choices(
        :Choice 1, :Choice 2, :Choice 3
    ),
    Profile ID( :Profile ID ),
    Profile Effects( :Flavor ),
    Subject Subject ID( :Respondent ),
    Subject Effects(
        :Citizenship, :Gender
    ),
    "Firth Bias-adjusted Estimates"n( 1 ),
    Response Best Option( :Best Profile ),
    Response Worst Option(
        :Worst Profile
    )
);
```

### [Perform distribution analysis on specified columns in the Presidential Elections data table with uniform scaling and custom axis settings for continuous distributions.](#perform-distribution-analysis-on-specified-columns-in-the-presidential-elections-data-table-with-uniform-scaling-and-custom-axis-settings-for-continuous-distributions)[](#perform-distribution-analysis-on-specified-columns-in-the-presidential-elections-data-table-with-uniform-scaling-and-custom-axis-settings-for-continuous-distributions "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Presidential Elections.jmp");
// Distribution
Distribution(
    Uniform Scaling( 1 ),
    Continuous Distribution(
        Column( :"1980"n ),
        Axis Settings(
            Scale( Linear ),
            Format( Best ),
            Min( 20 ),
            Max( 65 ),
            Inc( 5 )
        )
    ),
    Continuous Distribution(
        Column( :"1984"n ),
        Axis Settings(
            Scale( Linear ),
            Format( Best ),
            Min( 20 ),
            Max( 65 ),
            Inc( 5 )
        )
    ),
    Continuous Distribution(
        Column( :"1996"n ),
        Axis Settings(
            Scale( Linear ),
            Format( Best ),
            Min( 20 ),
            Max( 65 ),
            Inc( 5 )
        )
    )
);
```

### [Generate a P chart for the proportion of defective units using week subgroups with a Binomial distribution in the Control Chart Builder platform.](#generate-a-p-chart-for-the-proportion-of-defective-units-using-week-subgroups-with-a-binomial-distribution-in-the-control-chart-builder-platform)[](#generate-a-p-chart-for-the-proportion-of-defective-units-using-week-subgroups-with-a-binomial-distribution-in-the-control-chart-builder-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Electrical Component Defect Screening.jmp");
// P chart of N Defective Week Subgrouping
Control Chart Builder(
    Size( 534, 450 ),
    Show Control Panel( 0 ),
    Class( Shewhart Attribute ),
    Variables(
        Subgroup( :Week ),
        Y( :N Defective ),
        n Trials( :N Units )
    ),
    Chart(
        Points(
            Statistic( "Proportion" )
        ),
        Limits( Sigma( "Binomial" ) )
    ),
    SendToReport(
        Dispatch( {}, "N Defective",
            ScaleBox,
            {Min( -0.000843572386136978 ),
            Max( 0.1 ), Inc( 0.01 ),
            Minor Ticks( 1 )}
        )
    )
);
```

### [Create a P' Chart to Monitor Proportions of Defectives with Laney P' Adjustment, Grouping Data by Week Subgroup Size.](#create-a-p-chart-to-monitor-proportions-of-defectives-with-laney-p-adjustment-grouping-data-by-week-subgroup-size)[](#create-a-p-chart-to-monitor-proportions-of-defectives-with-laney-p-adjustment-grouping-data-by-week-subgroup-size "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Electrical Component Defect Screening.jmp");
// P' chart of N Defective Week Subgrouping
Control Chart Builder(
    Size( 534, 450 ),
    Show Control Panel( 0 ),
    Class( Shewhart Attribute ),
    Variables(
        Subgroup( :Week ),
        Y( :N Defective ),
        n Trials( :N Units )
    ),
    Chart(
        Points(
            Statistic( "Proportion" )
        ),
        Limits(
            Sigma( "Laney P Prime" )
        )
    ),
    SendToReport(
        Dispatch( {}, "N Defective",
            ScaleBox,
            {Min( -0.000843572386136978 ),
            Max( 0.1 ), Inc( 0.01 ),
            Minor Ticks( 1 )}
        )
    )
);
```

### [Create a Laney P' chart of N Defective using the Control Chart Builder with specified subgroup and variable configurations.](#create-a-laney-p-chart-of-n-defective-using-the-control-chart-builder-with-specified-subgroup-and-variable-configurations)[](#create-a-laney-p-chart-of-n-defective-using-the-control-chart-builder-with-specified-subgroup-and-variable-configurations "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Electrical Component Defect Screening.jmp");
// P' chart of N Defective
Control Chart Builder(
    Size( 622, 305 ),
    Show Control Panel( 0 ),
    Class( Shewhart Attribute ),
    Variables(
        Subgroup( :Week ),
        Subgroup(
            :Weekday,
            Position( 1 )
        ),
        Y( :N Defective ),
        n Trials( :N Units )
    ),
    Chart(
        Points(
            Statistic( "Proportion" )
        ),
        Limits(
            Sigma( "Laney P Prime" )
        )
    ),
    SendToReport(
        Dispatch( {}, "N Defective",
            ScaleBox,
            {Min( -0.00188665487286776 ),
            Max( 0.140225884611048 ),
            Inc( 0.02 ), Minor Ticks( 0 )
            }
        )
    )
);
```

### [Construct an Individual Moving Range (IMR) chart with multiple control limits in the Control Chart Builder platform.](#construct-an-individual-moving-range-imr-chart-with-multiple-control-limits-in-the-control-chart-builder-platform)[](#construct-an-individual-moving-range-imr-chart-with-multiple-control-limits-in-the-control-chart-builder-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Engine Temperature Sensor.jmp");
// IMR Chart
Control Chart Builder(
    Show Capability( 0 ),
    Variables( Y( :Y ) ),
    Chart(
        Position( 1 ),
        Limits( Sigma( Moving Range ) ),
        Warnings(
            Test 1( 1 ),
            Test 2( 1 ),
            Test 3( 1 ),
            Test 4( 1 ),
            Test 5( 1 ),
            Test 6( 1 ),
            Test 7( 1 ),
            Test 8( 1 )
        )
    ),
    Chart(
        Position( 2 ),
        Limits( Sigma( Moving Range ) )
    )
);
```

### [Generate a Short Run DNOM chart using Control Chart Builder, with subgroups defined by Box, and variables for % Cocoa and Product. The chart includes product-level statistics for different types of chocolates, setting targets and sigmas accordingly.](#generate-a-short-run-dnom-chart-using-control-chart-builder-with-subgroups-defined-by-box-and-variables-for-cocoa-and-product-the-chart-includes-product-level-statistics-for-different-types-of-chocolates-setting-targets-and-sigmas-accordingly)[](#generate-a-short-run-dnom-chart-using-control-chart-builder-with-subgroups-defined-by-box-and-variables-for-cocoa-and-product-the-chart-includes-product-level-statistics-for-different-types-of-chocolates-setting-targets-and-sigmas-accordingly "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Fancy Chocolate Factory.jmp");
// Short Run DNOM
Control Chart Builder(
    Show Product Separators( 0 ),
    Class( Short Run ),
    Variables(
        Subgroup( :Box ),
        Y( :"% Cocoa"n ),
        Part( :Product )
    ),
    Chart(
        Position( 2 ),
        Points(
            Statistic( "Range Centered" )
        )
    ),
    Product Statistics(
        :
        "% Cocoa"n(
            Product Level(
                Milk Chocolate(
                    Target( 37 ),
                    Sigma(
                        3.76288031574307
                    )
                ),
                Dark Chocolate(
                    Target( 70 ),
                    Sigma(
                        1.75728682873715
                    )
                ),
                Extra Dark Chocolate(
                    Target( 85 ),
                    Sigma(
                        1.00725971457878
                    )
                )
            )
        )
    )
);
```

### [Execute a Short Run Standardized Control Chart with Product Separators and Target Specifications for the % Cocoa variable using the Control Chart Builder function.](#execute-a-short-run-standardized-control-chart-with-product-separators-and-target-specifications-for-the-cocoa-variable-using-the-control-chart-builder-function)[](#execute-a-short-run-standardized-control-chart-with-product-separators-and-target-specifications-for-the-cocoa-variable-using-the-control-chart-builder-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Fancy Chocolate Factory.jmp");
// Short Run Standardized
Control Chart Builder(
    Show Product Separators( 0 ),
    Class( Short Run ),
    Variables(
        Subgroup( :Box, Position( 1 ) ),
        Y( :"% Cocoa"n ),
        Part( :Product )
    ),
    Chart(
        Position( 1 ),
        Points(
            Statistic( "Standardized" )
        ),
        Warnings( Test 1( 1 ) )
    ),
    Chart(
        Position( 2 ),
        Points(
            Statistic( "Standardized" )
        )
    ),
    Product Statistics(
        :
        "% Cocoa"n(
            Product Level(
                Milk Chocolate(
                    Target( 37 ),
                    Sigma( 3.5 )
                ),
                Dark Chocolate(
                    Target( 70 ),
                    Sigma( 1.5 )
                ),
                Extra Dark Chocolate(
                    Target( 85 ),
                    Sigma( 1 )
                )
            )
        )
    )
);
```

### [Create a Control Chart Builder with a specified subgroup, response variable, and phase variable, and customize the limits and appearance using the Sigma Moving Range method.](#create-a-control-chart-builder-with-a-specified-subgroup-response-variable-and-phase-variable-and-customize-the-limits-and-appearance-using-the-sigma-moving-range-method)[](#create-a-control-chart-builder-with-a-specified-subgroup-response-variable-and-phase-variable-and-customize-the-limits-and-appearance-using-the-sigma-moving-range-method "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Phase Historical Data.jmp");
// Control Chart Builder
Control Chart Builder(
    Show Capability( 0 ),
    Variables(
        Subgroup( :Run ),
        Y( :Force ),
        Phase( :Site )
    ),
    Chart(
        Position( 1 ),
        Limits( Sigma( "Moving Range" ) )
    ),
    Chart(
        Position( 2 ),
        Limits( Sigma( "Moving Range" ) )
    ),
    SendToReport(
        Dispatch( {},
            "Control Chart Builder",
            FrameBox,
            {
            DispatchSeg(
                Text Seg( 4 ),
                {Line Color( "None" ),
                Fill Color( "None" )}
            ),
            DispatchSeg(
                Text Seg( 5 ),
                {Line Color( "None" ),
                Fill Color( "None" )}
            ),
            DispatchSeg(
                Text Seg( 6 ),
                {Line Color( "None" ),
                Fill Color( "None" )}
            )}
        )
    )
);
```

### [Create an Individual Measurement Chart using Control Chart Builder, displaying both Individual and Moving Range statistics.](#create-an-individual-measurement-chart-using-control-chart-builder-displaying-both-individual-and-moving-range-statistics)[](#create-an-individual-measurement-chart-using-control-chart-builder-displaying-both-individual-and-moving-range-statistics "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Pickles.jmp");
// Individual Measurement Chart
Control Chart Builder(
    Show Control Panel( 0 ),
    Variables( "Y"(:Acid) ),
    Chart(
        Position( 1 ),
        Points(
            Statistic( "Individual" )
        ),
        Limits( Sigma( "Moving Range" ) ),
        Connecting Line( 1 )
    ),
    Chart(
        Position( 2 ),
        Points(
            Statistic( "Moving Range" )
        ),
        Limits( Sigma( "Moving Range" ) ),
        Connecting Line( 1 )
    )
);
```

### [Perform principal components analysis on a dataset containing thickness measurements using the Row-wise estimation method, on covariances, with eigenvalues calculation and arrow lines in the PCA summary plots. Adjust the frame size of the PCA summary plots to 200x200.](#perform-principal-components-analysis-on-a-dataset-containing-thickness-measurements-using-the-row-wise-estimation-method-on-covariances-with-eigenvalues-calculation-and-arrow-lines-in-the-pca-summary-plots-adjust-the-frame-size-of-the-pca-summary-plots-to-200x200)[](#perform-principal-components-analysis-on-a-dataset-containing-thickness-measurements-using-the-row-wise-estimation-method-on-covariances-with-eigenvalues-calculation-and-arrow-lines-in-the-pca-summary-plots-adjust-the-frame-size-of-the-pca-summary-plots-to-200x200 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Thickness.jmp");
// Principal Components
Principal Components(
    Y(
        :Thickness 01, :Thickness 02,
        :Thickness 03, :Thickness 04,
        :Thickness 05, :Thickness 06,
        :Thickness 07, :Thickness 08,
        :Thickness 09, :Thickness 10,
        :Thickness 11, :Thickness 12
    ),
    Estimation Method( "Row-wise" ),
    on Covariances,
    Eigenvalues( 1 ),
    Arrow Lines( 1 ),
    SendToReport(
        Dispatch( {"Summary Plots"},
            "PCA Summary Plots", FrameBox,
            {Frame Size( 200, 200 )}
        ),
        Dispatch( {"Summary Plots"},
            "PCA Summary Plots",
            FrameBox( 2 ),
            {Frame Size( 200, 200 )}
        )
    )
);
```

### [Analyze data from an appliance using a Weibull distribution to perform a life distribution analysis.](#analyze-data-from-an-appliance-using-a-weibull-distribution-to-perform-a-life-distribution-analysis)[](#analyze-data-from-an-appliance-using-a-weibull-distribution-to-perform-a-life-distribution-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Reliability/Appliance.jmp");
// Life Distribution
Life Distribution(
    Y( :Time Cycles ),
    Failure Cause( :Cause Code ),
    Failure Distribution by Cause(
        Weibull
    ),
    Comparison Criterion( AICc ),
    Allow failure mode to use ZI distributions(
        0
    ),
    Allow failure mode to use TH distributions(
        0
    ),
    Allow failure mode to use DS distributions(
        0
    ),
    Allow failure mode to use fixed parameter models(
        0
    ),
    Allow failure mode to use Bayesian models(
        0
    )
);
```

### [Perform cumulative damage analysis using the Ramp Stress model, Weibull distribution, and Inverse Power relationship.](#perform-cumulative-damage-analysis-using-the-ramp-stress-model-weibull-distribution-and-inverse-power-relationship)[](#perform-cumulative-damage-analysis-using-the-ramp-stress-model-weibull-distribution-and-inverse-power-relationship "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Reliability/CD Ramp Stress.jmp");
// Cumulative Damage
Open(
    "$SAMPLE_DATA/Reliability/CD Ramp Stress Pattern.jmp"
);
Cumulative Damage(
    Model Type( "Ramp Stress" ),
    Time to Event Data Table(
        "CD Ramp Stress",
        Time to Event( :Time ),
        Censor( :Censor ),
        Pattern ID( :Pattern ID )
    ),
    Ramp Stress Pattern Data Table(
        "CD Ramp Stress Pattern",
        Intercept( :intercept ),
        Slope( :slope ),
        Pattern ID( :Pattern ID )
    ),
    Relationship( "Inverse Power" ),
    Distribution( "Weibull" )
);
```

### [Perform a Cumulative Damage analysis using the Sinusoid Stress model in the Reliability platform, specifying the Weibull distribution and inverse power relationship for the failure data.](#perform-a-cumulative-damage-analysis-using-the-sinusoid-stress-model-in-the-reliability-platform-specifying-the-weibull-distribution-and-inverse-power-relationship-for-the-failure-data)[](#perform-a-cumulative-damage-analysis-using-the-sinusoid-stress-model-in-the-reliability-platform-specifying-the-weibull-distribution-and-inverse-power-relationship-for-the-failure-data "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Reliability/CD Sinusoid Stress.jmp");
// Cumulative Damage
Open(
    "$SAMPLE_DATA/Reliability/CD Sinusoid Stress Pattern.jmp"
);
Cumulative Damage(
    Model Type( "Sinusoid Stress" ),
    Time to Event Data Table(
        "CD Sinusoid Stress",
        Time to Event( :Time ),
        Censor( :Censor ),
        Pattern ID( :Pattern ID )
    ),
    Sinusoid Stress Pattern Data Table(
        "CD Sinusoid Stress Pattern",
        Level( :level ),
        Amplitude( :amplitude ),
        Period( :period ),
        Phase( :phase ),
        Pattern ID( :Pattern ID )
    ),
    Relationship( "Inverse Power" ),
    Distribution( "Weibull" )
);
```

### [Perform cumulative damage analysis using step stress modeling with an inverse power relationship and Weibull distribution.](#perform-cumulative-damage-analysis-using-step-stress-modeling-with-an-inverse-power-relationship-and-weibull-distribution)[](#perform-cumulative-damage-analysis-using-step-stress-modeling-with-an-inverse-power-relationship-and-weibull-distribution "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Reliability/CD Step Stress.jmp");
// Cumulative Damage
Open(
    "$SAMPLE_DATA/Reliability/CD Step Stress Pattern.jmp"
);
Cumulative Damage(
    Model Type( "Step Stress" ),
    Time to Event Data Table(
        "CD Step Stress",
        Time to Event( :Time ),
        Censor( :Censor ),
        Pattern ID( :Pattern ID )
    ),
    Step Stress Pattern Data Table(
        "CD Step Stress Pattern",
        Stress Duration( :Duration ),
        Stress( :Stress ),
        Pattern ID( :Pattern ID )
    ),
    Relationship( "Inverse Power" ),
    Distribution( "Weibull" ),
    Pattern Continuation( "Terminate" )
);
```

### [Split the Y variable by Quadrant in the Wafer Quadrants data set and fit a Standard Least Squares regression model to the resulting subsets, adjusting for the Layout effect.](#split-the-y-variable-by-quadrant-in-the-wafer-quadrants-data-set-and-fit-a-standard-least-squares-regression-model-to-the-resulting-subsets-adjusting-for-the-layout-effect)[](#split-the-y-variable-by-quadrant-in-the-wafer-quadrants-data-set-and-fit-a-standard-least-squares-regression-model-to-the-resulting-subsets-adjusting-for-the-layout-effect "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Wafer Quadrants.jmp");
// Split Y by Quadrant
dt = Split(
    Split By( :Quadrant ),
    Split( :Y ),
    Remaining Columns(
        Keep( :Wafer ID, :Layout )
    ),
    Sort by Column Property
);
dt <<
New Script(
    "Model",
    Fit Model(
        Y(
            :"High, High"n, :"High, Low"n,
            :"Low, High"n, :"Low, Low"n
        ),
        Effects( :Layout ),
        Keep dialog open( 1 ),
        Personality(
            "Standard Least Squares"
        ),
        Emphasis( "Minimal Report" )
    )
);
```

### [Analyze the distribution of GDP per Capita for multiple countries using continuous and histogram distribution plots.](#analyze-the-distribution-of-gdp-per-capita-for-multiple-countries-using-continuous-and-histogram-distribution-plots)[](#analyze-the-distribution-of-gdp-per-capita-for-multiple-countries-using-continuous-and-histogram-distribution-plots "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/World Demographics.jmp");
// Distribution: GDP per Capita
Distribution(
    Continuous Distribution(
        Column( :GDP per Capita ),
        Vertical( 0 )
    ),
    SendToReport(
        Dispatch( {"GDP per Capita"},
            "Distrib Outlier Box",
            FrameBox,
            {Frame Size( 208, 76 ),
            Marker Size( 2 ),
            DispatchSeg(
                Marker Seg( 1 ),
                label offset(
                    {5, -68, -27},
                    {6, -29, 38},
                    {7, 17, 29},
                    {8, -72, -26}
                )
            )}
        ),
        Dispatch( {"GDP per Capita"},
            "Distrib Histogram", FrameBox,
            {Frame Size( 208, 82 )}
        )
    )
);
```

[ Previous](Dimensionality%20Reduction.html "Dimensionality Reduction") [Next ](Fit%20Model.html "Fit Model")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
