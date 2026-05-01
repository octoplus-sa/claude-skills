# Model Screening

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Model%20Screening.html](https://jsl.jmp.com/All%20Categories/Objects/Model%20Screening.html)*

---

# [Model Screening](#model-screening)[](#model-screening "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Model Screening](#model-screening_1)[](#model-screening_1 "Click to copy url")

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

## [Columns](#columns)[](#columns "Click to copy url")

### [By](#by)[](#by "Click to copy url")

**Syntax:** obj \<\< By( column(s) )

**Description:** Performs a separate analysis for each level of the specified column.

**JMP Version Added:** 16

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
```

### [Factor](#factor)[](#factor "Click to copy url")

**Syntax:** obj \<\< Factor( column(s) )

**JMP Version Added:** 16

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
```

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

**JMP Version Added:** 16

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Freq( :_freqcol )
);
```

### [Response](#response)[](#response "Click to copy url")

**Syntax:** obj \<\< Response( column(s) )

**JMP Version Added:** 16

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
```

### [Validation](#validation)[](#validation "Click to copy url")

**Syntax:** obj \<\< Validation( column )

**JMP Version Added:** 16

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
```

### [Weight](#weight)[](#weight "Click to copy url")

**Syntax:** obj \<\< Weight( column )

**Description:** Specifies a column whose values assign a weight to each row for the analysis.

**JMP Version Added:** 16

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_weightcol", Numeric, Continuous, Set Each Value( Random Beta( 1, 1 ) ) );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Weight( :_weightcol )
);
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** obj \<\< X( column(s) )

**JMP Version Added:** 16

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

**JMP Version Added:** 16

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Add Quadratics](#add-quadratics)[](#add-quadratics "Click to copy url")

**Syntax:** obj = Model Screening(...Add Quadratics( state=0\|1 )...)

**Description:** Adds effects for the squares of continuous variables to linear modeling fits.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :LTG, :BMI, :BP, :Glucose, :HDL ),
    Add Quadratics( 1 )
);
```

### [Add Two Way Interactions](#add-two-way-interactions)[](#add-two-way-interactions "Click to copy url")

**Syntax:** obj = Model Screening(...Add Two Way Interactions( state=0\|1 )...)

**Description:** Adds all two-way interaction effects to linear modeling fits.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :LTG, :BMI, :BP, :Glucose, :HDL ),
    Add Two Way Interactions( 1 )
);
```

### [Additional Methods](#additional-methods)[](#additional-methods "Click to copy url")

**Syntax:** obj = Model Screening(...Additional Methods( state=0\|1 )...)

**Description:** Calls several additional methods in the Generalized Regression platform in addition to Lasso: Forward Selection, Pruned Forward Selection, Elastic Net, and Ridge.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Additional Methods( 1 )
);
```

### [Boosted Tree](#boosted-tree)[](#boosted-tree "Click to copy url")

**Syntax:** obj = Model Screening(...Boosted Tree( state=0\|1 )...)

**Description:** Builds a decision tree that is a sequence of smaller trees to predict a response. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 1 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 )
);
```

### [Bootstrap Forest](#bootstrap-forest)[](#bootstrap-forest "Click to copy url")

**Syntax:** obj = Model Screening(...Bootstrap Forest( state=0\|1 )...)

**Description:** Builds a collection of decision trees using random sampling and averages the results to predict a response. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 1 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 )
);
```

### [Cardinality of Predictors](#cardinality-of-predictors)[](#cardinality-of-predictors "Click to copy url")

**Syntax:** obj \<\< Cardinality of Predictors( state=0\|1 )

**Description:** Shows or hides a report of the number of levels and how many parameters are used in the linear model fit for each categorical predictor.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Equity.jmp" );
Model Screening(
    Y( :BAD ),
    Validation( :Validation ),
    X(
        :LOAN, :MORTDUE, :VALUE, :REASON, :JOB, :YOJ, :DEROG, :DELINQ, :CLAGE, :NINQ, :CLNO,
        :DEBTINC
    ),
    Neural( 0 ),
    Bootstrap Forest( 0 ),
    Generalized Regression( 0 ),
    Support Vector Machines( 0 ),
    Cardinality of Predictors( 1 )
);
```

### [Decision Threshold](#decision-threshold)[](#decision-threshold "Click to copy url")

**Syntax:** obj \<\< Decision Threshold( state = 0\|1, Set Probability Threshold( number ) )

**Description:** Shows or hides the distribution of fitted probabilities and actual versus predicted tables for each model. You can change the probability threshold to explore how different thresholds affect the classification results.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y Binary ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 1 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Neural( 1 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 1 ),
    Generalized Regression( 1 ),
    Decision Threshold( 1 )
);
```

### [Decision Tree](#decision-tree)[](#decision-tree "Click to copy url")

**Syntax:** obj = Model Screening(...Decision Tree( state=0\|1 )...)

**Description:** Builds a decision tree to predict a response. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 1 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 )
);
```

### [Discriminant](#discriminant)[](#discriminant "Click to copy url")

**Syntax:** obj = Model Screening(...Discriminant( state=0\|1 )...)

**Description:** Classifies categorical group membership based on continuous variables. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Iris.jmp" );
Make Validation Column( Validation Set( .3 ), Training Set( .7 ), Go );
obj = Model Screening(
    Y( :Species ),
    Validation( :Validation ),
    X( :Sepal length, :Sepal width, :Petal length, :Petal width ),
    Discriminant( 1 ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 0 ),
    Generalized Regression( 0 )
);
```

### [Elapsed Time](#elapsed-time)[](#elapsed-time "Click to copy url")

**Syntax:** obj \<\< Elapsed Time( state=0\|1 )

**Description:** Shows or hides a report that contains the total elapsed time that was spent fitting each method.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Elapsed Time( 1 )
);
```

### [Fit Least Squares](#fit-least-squares)[](#fit-least-squares "Click to copy url")

**Syntax:** obj = Model Screening(...Fit Least Squares( state=0\|1 )...)

**Description:** Fits a linear regression model for a continuous response. Techniques include regression, analysis of variance, analysis of covariance, mixed models, and analysis of designed experiments. The Emphasis option enables you to specify the report layout. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 1 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 )
);
```

### [Fit Stepwise](#fit-stepwise)[](#fit-stepwise "Click to copy url")

**Syntax:** obj = Model Screening(...Fit Stepwise( state=0\|1 )...)

**Description:** Fits stepwise regression models, which facilitate variable selection for standard least squares and ordinal logistic models, as well as nominal logistic models with a binary response. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 1 ),
    Generalized Regression( 0 )
);
```

### [Generalized Regression](#generalized-regression)[](#generalized-regression "Click to copy url")

**Syntax:** obj = Model Screening(...Generalized Regression( state=0\|1 )...)

**Description:** Fits generalized linear models using penalized regression techniques, which help automate variable selection in a way that avoids overfitting. The penalized regression techniques include the lasso, the adaptive lasso, the elastic net, the adaptive elastic net, and ridge regression. The response distributions can accommodate continuous, categorical, count, and time-to-event response data. This is the recommended personality for most regression settings. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 1 )
);
```

### [Informative Missing](#informative-missing)[](#informative-missing "Click to copy url")

**Syntax:** obj = Model Screening(...Informative Missing( state=0\|1 )...)

**Description:** Enables the informative missing option for all platforms.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Equity.jmp" );
Model Screening(
    Y( :BAD ),
    Validation( :Validation ),
    X(
        :LOAN, :MORTDUE, :VALUE, :REASON, :JOB, :YOJ, :DEROG, :DELINQ, :CLAGE, :NINQ, :CLNO,
        :DEBTINC
    ),
    Neural( 0 ),
    Informative Missing( 1 )
);
```

### [K Fold Crossvalidation](#k-fold-crossvalidation)[](#k-fold-crossvalidation "Click to copy url")

**Syntax:** obj = Model Screening(...K Fold Crossvalidation( state=0\|1 )...)

**Description:** Partitions the data randomly into K parts or folds. A model is fit to the data K times, each time with a different fold held out as a crossvalidation set.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    K Fold Crossvalidation( 1 ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Neural( 0 ),
    Support Vector Machines( 0 )
);
```

### [K Nearest Neighbors](#k-nearest-neighbors)[](#k-nearest-neighbors "Click to copy url")

**Syntax:** obj = Model Screening(...K Nearest Neighbors( state=0\|1 )...)

**Description:** Predicts a response based on the responses of the k nearest neighbors. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 1 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 )
);
```

### [K for K Fold](#k-for-k-fold)[](#k-for-k-fold "Click to copy url")

**Syntax:** obj = Model Screening(...K for K Fold( number=5 )...)

**Description:** Specifies the number of folds for K Fold Crossvalidation. The default is 5 and K must be greater than 1. "5" by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    K Fold Crossvalidation( 1 ),
    K for K Fold( 6 ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Neural( 0 ),
    Support Vector Machines( 0 )
);
```

### [K for Nested](#k-for-nested)[](#k-for-nested "Click to copy url")

**Syntax:** obj = Model Screening(...K for Nested( number=5 )...)

**Description:** Specifies the number of folds for Nested Crossvalidation. The default is 5 and K must be greater than 1. "5" by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Nested Crossvalidation( 1 ),
    K for Nested( 3 ),
    L for Nested( 4 ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Neural( 0 ),
    Support Vector Machines( 0 )
);
```

### [L for Nested](#l-for-nested)[](#l-for-nested "Click to copy url")

**Syntax:** obj = Model Screening(...L for Nested( number=4 )...)

**Description:** Specifies the number of inner folds for Nested Crossvalidation. The default is 4 and L must be greater than 1. "4" by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Nested Crossvalidation( 1 ),
    K for Nested( 5 ),
    L for Nested( 4 ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Neural( 0 ),
    Support Vector Machines( 0 )
);
```

### [Log Methods](#log-methods)[](#log-methods "Click to copy url")

**Syntax:** obj = Model Screening(...Log Methods( state=0\|1 )...)

### [Logistic Regression](#logistic-regression)[](#logistic-regression "Click to copy url")

**Syntax:** obj = Model Screening(...Logistic Regression( state=0\|1 )...)

**Description:** Fits a logistic regression model of nominal response categories for both continuous and categorical predictors. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y Binary ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 1 ),
    Generalized Regression( 0 )
);
```

### [Model NParm Limit](#model-nparm-limit)[](#model-nparm-limit "Click to copy url")

**Syntax:** obj \<\< Model NParm Limit( number=450 )

**Description:** Specifies the number of parameters above which the modeling platforms are not run. "450" by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Add Two Way Interactions( 1 ),
    Add Quadratics( 1 ),
    Model NParm Limit( 40 ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Fit Least Squares( 1 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 0 ),
    Generalized Regression( 0 )
);
```

### [Naive Bayes](#naive-bayes)[](#naive-bayes "Click to copy url")

**Syntax:** obj = Model Screening(...Naive Bayes( state=0\|1 )...)

**Description:** Predicts group membership for a categorical variable.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y Binary ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 1 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 0 ),
    Generalized Regression( 0 ), 

);
```

### [Nested Crossvalidation](#nested-crossvalidation)[](#nested-crossvalidation "Click to copy url")

**Syntax:** obj = Model Screening(...Nested Crossvalidation( state=0\|1 )...)

**Description:** Partitions the data randomly into K equal parts and then further partitions all but one of those parts into L equal parts.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Nested Crossvalidation( 1 ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Neural( 0 ),
    Support Vector Machines( 0 )
);
```

### [Neural](#neural)[](#neural "Click to copy url")

**Syntax:** obj = Model Screening(...Neural( state=0\|1 )...)

**Description:** Predicts one or more response variables using a flexible function of the input variables. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 1 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 )
);
```

### [Partial Least Squares](#partial-least-squares)[](#partial-least-squares "Click to copy url")

**Syntax:** obj = Model Screening(...Partial Least Squares( state=0\|1 )...)

**Description:** Fits a model to one or more response variables using latent factors. This permits models to be fit when explanatory variables are highly correlated, or when there are more explanatory variables than there are observations.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 ),
    Partial Least Squares( 1 )
);
```

### [Plot Actual by Predicted](#plot-actual-by-predicted)[](#plot-actual-by-predicted "Click to copy url")

**Syntax:** obj \<\< Plot Actual by Predicted( state=0\|1 )

**Description:** Overlays Actual by Predicted points from several model fits.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 1 ),
    Boosted Tree( 1 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 1 ),
    Generalized Regression( 1 ),
    Plot Actual by Predicted( 1 )
);
```

### [Precision Recall Curve](#precision-recall-curve)[](#precision-recall-curve "Click to copy url")

**Syntax:** obj \<\< Precision Recall Curve( state=0\|1 )

**Description:** Shows or hides overlaid precision-recall curves for all of the model fits. There are separate plots for the Training, Validation, and Test sets.

**JMP Version Added:** 16

``` jsl

dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = dt << Model Screening(
    Y( :Y Binary ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Neural( 1 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 1 ),
    Generalized Regression( 1 ),

);
obj << Precision Recall Curve( 1 );
```

### [Predictor Properties](#predictor-properties)[](#predictor-properties "Click to copy url")

**Syntax:** obj \<\< Predictor Properties( state=0\|1 )

**Description:** Available if you hold down the shift button, for each platform called, shows information about supported interfaces.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Predictor Properties( 1 )
);
```

### [Profiler](#profiler)[](#profiler "Click to copy url")

**Syntax:** obj \<\< Profiler( state=0\|1 )

**Description:** Shows or hides prediction profilers for each type of model fit. This option is available only for continuous responses.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 1 ),
    K Nearest Neighbors( 0 ),
    Neural( 1 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 1 ),
    Profiler( 1 )
);
```

### [ROC Curve](#roc-curve)[](#roc-curve "Click to copy url")

**Syntax:** obj \<\< ROC Curve( state=0\|1 )

**Description:** Shows or hides overlaid Receiver Operating Characteristic (ROC) curves for all of the model fits. There are separate plots for the Training, Validation, and Test sets.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y Binary ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Neural( 1 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 1 ),
    Generalized Regression( 1 ),
    ROC Curve( 1 )
);
```

### [Remove Live Reports](#remove-live-reports)[](#remove-live-reports "Click to copy url")

**Syntax:** obj = Model Screening(...Remove Live Reports( state=0\|1 )...)

**Description:** Removes the individual model platform reports from the Model Screening report window. You can use this option to free up memory for further work.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    K Fold Crossvalidation( 1 ),
    Remove Live Reports( 1 ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Neural( 0 ),
    Support Vector Machines( 0 )
);
```

### [Repeated K Fold](#repeated-k-fold)[](#repeated-k-fold "Click to copy url")

**Syntax:** obj = Model Screening(...Repeated K Fold( number=0 )...)

**Description:** Specifies the number of times the K Fold Crossvalidation or Nested Crossvalidation process is repeated. "0" by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Repeated K Fold( 2 ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Neural( 0 ),
    Support Vector Machines( 0 )
);
```

### [SVM NRow Limit](#svm-nrow-limit)[](#svm-nrow-limit "Click to copy url")

**Syntax:** obj \<\< SVM NRow Limit( number=10000 )

**Description:** Specifies the number of rows above which Support Vector Machines are not run. "10000" by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Equity.jmp" );
Model Screening(
    Y( :BAD ),
    Validation( :Validation ),
    X(
        :LOAN, :MORTDUE, :VALUE, :REASON, :JOB, :YOJ, :DEROG, :DELINQ, :CLAGE, :NINQ, :CLNO,
        :DEBTINC
    ),
    Decision Tree( 1 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 1 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 ),
    SVM NRow Limit( 6000 )
);
```

### [Save Folded Prediction Formula](#save-folded-prediction-formula)[](#save-folded-prediction-formula "Click to copy url")

**Syntax:** obj \<\< Save Folded Prediction Formula

**Description:** Saves new columns to the original data table. The new columns contain a leak-free prediction formula for K Fold Crossvalidation. For each row, the formula avoids using model fits that were trained using that row.

### [Save KFold Results Table](#save-kfold-results-table)[](#save-kfold-results-table "Click to copy url")

**Syntax:** obj \<\< Save KFold Results Table

**Description:** Saves the information in the Summary Across the Folds report to a new data table.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    K Fold Crossvalidation( 1 ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 1 ),
    Boosted Tree( 1 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 1 ),
    Save KFold Results Table
);
```

### [Save Prediction Formulas](#save-prediction-formulas)[](#save-prediction-formulas "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formulas

**Description:** Saves the prediction formulas to the data table.

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 1 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Fit Least Squares( 1 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 0 ),
    Generalized Regression( 0 )
);
obj << Select Fit( "Training", "Best" );
obj << Save Prediction Formulas;
```

### [Save Results Table](#save-results-table)[](#save-results-table "Click to copy url")

**Syntax:** obj \<\< Save Results Table

**Description:** Saves the information in the Validation report to a new data table. If there is a test set, the information in the Test report is also saved to a new data table.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Save Results Table
);
```

### [Select Fit](#select-fit)[](#select-fit "Click to copy url")

**Syntax:** \<\<Select Fit( Training \| Validation \| Test \| Summary \| Clear All, Clear \| Dominant \| Best(\<number\>), \| Largest(name,\<number\>) \| Smallest(name,\<number\>) \| Where(expression) )

**Description:** Select fits in various reports based on specified criteria. This option is available only in JSL.

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
obj << Select Fit( Validation, Largest( "RSquare", 2 ) );
```

### [Set Probability Threshold](#set-probability-threshold)[](#set-probability-threshold "Click to copy url")

**Syntax:** obj \<\< Set Probability Threshold( number=0.5 )

**Description:** Specifies the number of parameters above which the modeling platforms are not run. "0.5" by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y Binary ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 1 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 1 ),
    Generalized Regression( 1 ),
    Decision Threshold( 1 ),
    Set Probability Threshold( .2 )
);
```

### [Set Random Seed](#set-random-seed)[](#set-random-seed "Click to copy url")

**Syntax:** obj = Model Screening(...Set Random Seed( number )...)

**Description:** Specifies a random seed to reproduce the results for future launches of the platform.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Set Random Seed( 123454321 )
);
```

### [Show Methods in Log](#show-methods-in-log)[](#show-methods-in-log "Click to copy url")

**Syntax:** obj = Model Screening(...Show Methods in Log( state=0\|1 )...)

**Description:** Writes out a progress message to the log each time a fitting platform is called.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y Binary ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Log Methods( 1 )
);
```

### [Show Profit](#show-profit)[](#show-profit "Click to copy url")

**Syntax:** obj \<\< Show Profit( state=0\|1 )

**Description:** Shows or hides the expected profit for each model using the specified Profit Matrix for the response levels.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
Column( "Y Binary" ) << Set Property(
    "Profit Matrix", {[1 - 1, -0.3333333 1, . .], {"Low", "High", "Undecided"}}
);
obj = Model Screening(
    Y( :Y Binary ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Neural( 1 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 1 ),
    Generalized Regression( 1 ),
    Show Profit( 1 )
);
```

### [Show Scripts](#show-scripts)[](#show-scripts "Click to copy url")

**Syntax:** obj \<\< Show Scripts( state=0\|1 )

**Description:** For each platform called, shows options added to launch script.

**JMP Version Added:** 19

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Bootstrap Forest( 1, {Number Trees( 80 ), Number Terms( 5 )} ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Show Scripts( 1 )
);
```

### [Specify Profit Matrix](#specify-profit-matrix)[](#specify-profit-matrix "Click to copy url")

**Syntax:** obj \<\< Specify Profit Matrix

**Description:** Enables you to specify profits or costs associated with correct or incorrect classification decisions.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Model Screening(
    Y( :marital status ),
    X( :sex, :age, :country, :type, :size ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Naive Bayes( 0 ),
    Neural( 1 ),
    Support Vector Machines( 0 ),
    Fit Stepwise( 0 ),
    Logistic Regression( 1 ),
    Generalized Regression( 1 ),
    Specify Profit Matrix( [0 -1, -0.6 0, . .], "Married", "Single", "Undecided" ),
    Show Profit( 1 )
);
```

### [Support Vector Machines](#support-vector-machines)[](#support-vector-machines "Click to copy url")

**Syntax:** obj = Model Screening(...Support Vector Machines( state=0\|1 )...)

**Description:** Predicts a response based on the support vectors in the space of the X variables. On by default.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 1 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 )
);
```

### [Time Limit Each](#time-limit-each)[](#time-limit-each "Click to copy url")

**Syntax:** obj = Model Screening(...Time Limit Each( number )...)

**Description:** Specifies a time limit in seconds for each fit. For platforms that support early stopping, the best estimates up to that point are provided.

**JMP Version Added:** 16

``` jsl

Open( "$Sample_Data/Equity.jmp" );
Model Screening(
    Y( :BAD ),
    Validation( :Validation ),
    X(
        :LOAN, :MORTDUE, :VALUE, :REASON, :JOB, :YOJ, :DEROG, :DELINQ, :CLAGE, :NINQ, :CLNO,
        :DEBTINC
    ),
    Time Limit Each( 1 )
);
```

### [Use Two Way Splits for K Fold](#use-two-way-splits-for-k-fold)[](#use-two-way-splits-for-k-fold "Click to copy url")

**Syntax:** obj = Model Screening(...Use Two Way Splits for K Fold( state=0\|1 )...)

**Description:** Uses only training and validation splits instead of training, validation, and test splits.

**JMP Version Added:** 19

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    K Fold Crossvalidation( 1 ),
    Use Two Way Splits for K Fold( 1 ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Neural( 0 ),
    Support Vector Machines( 0 )
);
```

### [XGBoost](#xgboost)[](#xgboost "Click to copy url")

**Syntax:** obj = Model Screening(...XGBoost( state=0\|1 )...)

**Description:** Invokes XGBoost for gradient boosting if you have the XGBoost add-in. This option appears only if the add-in is installed.

``` jsl

Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    Decision Tree( 0 ),
    Bootstrap Forest( 0 ),
    Boosted Tree( 0 ),
    K Nearest Neighbors( 0 ),
    Neural( 0 ),
    Support Vector Machines( 0 ),
    Fit Least Squares( 0 ),
    Fit Stepwise( 0 ),
    Generalized Regression( 0 ),
    XGBoost( 1 )
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

### [Automatic Recalc](#automatic-recalc)[](#automatic-recalc "Click to copy url")

**Syntax:** obj \<\< Automatic Recalc( state=0\|1 )

**Description:** Redoes the analysis automatically for exclude and data changes. If the Automatic Recalc option is turned on, you should consider using Wait(0) commands to ensure that the exclude and data changes take effect before the recalculation.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
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
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
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
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
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
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
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
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
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
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
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
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
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
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
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
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$Sample_Data/Diabetes.jmp" );
obj = Model Screening(
    Y( :Y ),
    Validation( :Validation ),
    X( :Age, :Gender, :BMI, :BP, :Total Cholesterol, :LDL, :HDL, :TCH, :LTG, :Glucose )
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

**Syntax:** obj = Model Screening(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

[ Previous](Model%20Driven%20Multivariate%20Control%20Chart.html "Model Driven Multivariate Control Chart") [Next ](Multidimensional%20Scaling.html "Multidimensional Scaling")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
