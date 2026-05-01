# Nonlinear

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Nonlinear.html](https://jsl.jmp.com/All%20Categories/Objects/Nonlinear.html)*

---

# [Nonlinear](#nonlinear)[](#nonlinear "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Nonlinear](#nonlinear_1)[](#nonlinear_1 "Click to copy url")

**Syntax:** Nonlinear( Y( column ), X( column with predictor formula ) )

**Description:** Fits nonlinear models using least squares or a custom loss function.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
```

## [Columns](#columns)[](#columns "Click to copy url")

### [By](#by)[](#by "Click to copy url")

**Syntax:** obj = Nonlinear(...\<By( column(s) )\>...)

**Description:** Performs a separate analysis for each level of the specified column.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Nonlinear(
    Y( :pop ),
    X( :"X-formula"n ),
    Finish(),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
```

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj = Nonlinear(...\<Freq( column )\>...)

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish(), Freq( :_freqcol ) );
```

### [Group](#group)[](#group "Click to copy url")

**Syntax:** obj = Nonlinear(...\<Group( column )\>...)

**Description:** Specifies a grouping variable. The fitted model has separate parameters for each level of the grouping variable.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/Bioassay.jmp" );
dt << Run Script( "Fit Curve" );                     

obj = dt << Nonlinear(
    Y( :Toxicity ),
    X( :Toxicity Predictor Formula ),
    Group( :Formulation ),
    Newton,
    Finish
);
```

### [Loss](#loss)[](#loss "Click to copy url")

**Syntax:** obj = Nonlinear(...\<Loss( column )\>...)

**Description:** Specifies a formula column that contains a loss function.

``` jsl
dt = Open( "$SAMPLE_DATA/Ship Damage.jmp" );
obj = dt << Nonlinear(
    X( :model ),
    Loss( :Poisson ),
    Loss is Neg LogLikelihood( 1 ),
    Newton,
    Finish
);
```

### [Predictor Formula](#predictor-formula)[](#predictor-formula "Click to copy url")

**Syntax:** obj = Nonlinear(...\<Predictor Formula( column )\>...)

**Description:** Specifies a column that contains either the X variable or a model formula with parameters.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
```

### [Response](#response)[](#response "Click to copy url")

**Syntax:** obj = Nonlinear(...\<Response( column )\>...)

**Description:** Specifies the response variable.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
```

### [Weight](#weight)[](#weight "Click to copy url")

**Syntax:** obj = Nonlinear(...\<Weight( column )\>...)

**Description:** Specifies a column whose values assign a weight to each row for the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_weightcol", Numeric, Continuous, Set Each Value( Random Beta( 1, 1 ) ) );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish(), Weight( :_weightcol ) );
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** obj = Nonlinear(...\<X( column )\>...)

**Description:** Specifies a column that contains either the X variable or a model formula with parameters.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj = Nonlinear(...\<Y( column )\>...)

**Description:** Specifies the response variable.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Accept Current Estimates](#accept-current-estimates)[](#accept-current-estimates "Click to copy url")

**Syntax:** obj \<\< Accept Current Estimates

**Description:** Produces the solution report using the current estimates, even if the estimates did not converge.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Parameter Bounds( B0( 15, . ) ) );
obj << Finish;
obj << Accept Current Estimates;
```

### [CL Alpha](#cl-alpha)[](#cl-alpha "Click to copy url")

**Syntax:** obj \<\< CL Alpha( number=.05 )

**Description:** Specifies the alpha level for the confidence limits for the parameter estimates. ".05" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << CL Alpha( .01 );
obj << Confidence Limits;
```

### [CL Limit](#cl-limit)[](#cl-limit "Click to copy url")

**Syntax:** obj \<\< CL Limit( number=.00001 )

**Description:** Specifies the convergence criterion that is used to calculate the confidence limits for the parameter estimates. ".00001" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << CL Limit( .002 );
obj << Confidence Limits;
```

### [Confidence Limits](#confidence-limits)[](#confidence-limits "Click to copy url")

**Syntax:** obj \<\< Confidence Limits

**Description:** Computes confidence intervals for all of the parameter estimates.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Confidence Limits;
```

### [Contour Profiler](#contour-profiler)[](#contour-profiler "Click to copy url")

**Syntax:** obj \<\< Contour Profiler( state=0\|1 )

**Description:** Shows or hides the contour profiler, which shows the contours of the response graphically for two factors at a time.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
Wait( 0 );
obj << Contour Profiler( 1 );
```

### [Custom Estimate](#custom-estimate)[](#custom-estimate "Click to copy url")

**Syntax:** obj \<\< Custom Estimate( expression )

**Description:** Estimates a user-specified function of the parameters. The expression and the standard error of the expression are calculated using the current parameter estimates.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
obj << Custom Estimate( B0 + A + D );
```

### [Custom Estimation Profiler](#custom-estimation-profiler)[](#custom-estimation-profiler "Click to copy url")

**Syntax:** obj \<\< Custom Estimation Profiler( Custom Estimation( {initial values}, expression ), \<Transformation( "Log"\|"Logit"\|"None" ), Profiler( script )\> )

**Description:** Enables you to construct a profiler for a custom expression. Enter an expression that involves parameters and at least one factor. By default, the Transformation option is set to None.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/Logistic w Loss.jmp" );
obj = dt << Nonlinear(
    Loss( :Loss ),
    Expand Intermediate Formulas( 1 ),
    Loss is Neg LogLikelihood( 1 ),
    Newton,
    Finish,
    Plot( 0 ),
    Custom Estimation Profiler(
        Custom Estimation( {x = 30}, 1 / (1 + Exp( b0 + b1 * x )) ),
        Transformation( "Logit" ),
        Profiler(
            1,
            Confidence Intervals( 1 ),
            Term Value(
                x(
                    140,
                    Min( -37.4344314814814 ),
                    Max( 392.622262689059 ),
                    Lock( 0 ),
                    Show( 1 )
                )
            )
        )
    )
);
```

### [Custom Inverse Prediction](#custom-inverse-prediction)[](#custom-inverse-prediction "Click to copy url")

**Syntax:** obj \<\< Custom Inverse Prediction( Response( l1, l2, ... ), \<Term Value( column( number ) )\> )

**Description:** Estimates an X value for each specified response value. Standard errors and confidence limits for the estimated X values are also calculated.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
Wait( 0 );
obj << Custom Inverse Prediction( Response( 100, 150, 200 ) );
```

### [Delta](#delta)[](#delta "Click to copy url")

**Syntax:** obj \<\< Delta( number=5.0e-6 )

**Description:** Specifies the delta value that is used in the Numeric Derivatives Only option. "5.0e-6" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ) );
obj << Numeric Derivatives Only( 1 );
obj << Delta( 0.2 );
obj << Finish;
```

### [Expand Intermediate Formulas](#expand-intermediate-formulas)[](#expand-intermediate-formulas "Click to copy url")

**Syntax:** obj \<\< Expand Intermediate Formulas( state=0\|1 )

**Description:** Uses expanded intermediate formulas in solving and in the formulas saved. This affects formulas in the output when the model is dependent on a column with a formula, as it will look through to the original columns.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/Logit Model w Loss1.jmp" );
obj = dt << Nonlinear(
    Loss( :Loss ),
    Show Prediction Expression( 1 ),
    Expand Intermediate Formulas( 1 ),
    Finish
);
```

### [Finish](#finish)[](#finish "Click to copy url")

**Syntax:** obj \<\< Finish

**Description:** Begins the fitting process and only moves to the next command if the solution has converged or finished. In scripts, the Finish option is recommended instead of the Go option.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Finish;
obj << Profiler;
```

### [Get CI](#get-ci)[](#get-ci "Click to copy url")

**Syntax:** obj \<\< Get CI

**Description:** Returns the confidence intervals for the parameter estimates. Note: The Confidence Intervals option must be selected before the Get CI option is specified.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Confidence Limits;
G = obj << Get CI;
Show( G );
```

### [Get Corr](#get-corr)[](#get-corr "Click to copy url")

**Syntax:** obj \<\< Get Corr

**Description:** Returns the correlation of the estimates.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
G = obj << Get Corr;
Show( G );
```

### [Get Cov](#get-cov)[](#get-cov "Click to copy url")

**Syntax:** obj \<\< Get Cov

**Description:** Returns the covariance of the estimates.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
G = obj << Get Cov;
Show( G );
```

### [Get Estimates](#get-estimates)[](#get-estimates "Click to copy url")

**Syntax:** obj \<\< Get Estimates

**Description:** Returns the parameter estimates.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
G = obj << Get Estimates;
Show( G );
```

### [Get Parameter Names](#get-parameter-names)[](#get-parameter-names "Click to copy url")

**Syntax:** obj \<\< Get Parameter Names

**Description:** Returns the parameter names.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
G = obj << Get Parameter Names;
Show( G );
```

### [Get SSE](#get-sse)[](#get-sse "Click to copy url")

**Syntax:** obj \<\< Get SSE

**Description:** Returns the sum of squares error (SSE).

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
G = obj << Get SSE;
Show( G );
```

### [Get Std Errors](#get-std-errors)[](#get-std-errors "Click to copy url")

**Syntax:** obj \<\< Get Std Errors

**Description:** Returns the standard errors of the parameter estimates.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
G = obj << Get Std Errors;
Show( G );
```

### [Go](#go)[](#go "Click to copy url")

**Syntax:** obj \<\< Go

**Description:** Begins iterating in the background to find the nonlinear solution. In scripts, the Finish option is recommended instead of the Go option.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Go;
```

### [Gradient Limit](#gradient-limit)[](#gradient-limit "Click to copy url")

**Syntax:** obj \<\< Gradient Limit( number=1e-6 )

**Description:** Specifies the stop limit value for the gradient criterion. "1e-6" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Gradient Limit( 0.0002 );
obj << Finish;
```

### [Iteration Limit](#iteration-limit)[](#iteration-limit "Click to copy url")

**Syntax:** obj \<\< Iteration Limit( number=60 )

**Description:** Specifies the maximum number of iterations. "60" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Iteration Limit( 10 );
obj << Finish;
```

### [Iteration Log](#iteration-log)[](#iteration-log "Click to copy url")

**Syntax:** obj \<\< Iteration Log( state=0\|1 )

**Description:** Shows or hides the Iterations table. Once this option is selected, the platform records subsequent iterations in the table.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ) );
obj << Iteration Log( 1 );
obj << Finish;
obj << Plot( 0 );
Report( obj )["Iterations"] << Close( 0 );
```

### [Lock Parameter](#lock-parameter)[](#lock-parameter "Click to copy url")

**Syntax:** obj \<\< Lock Parameter( Name, ... )

**Description:** Locks individual parameters at a specified value so they remain constant during the iteration process.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Set Parameter( B0 = 0.2 );
obj << Lock Parameter( B0 );
obj << Finish;
```

### [Loss is Neg LogLikelihood](#loss-is-neg-loglikelihood)[](#loss-is-neg-loglikelihood "Click to copy url")

**Syntax:** obj \<\< Loss is Neg LogLikelihood( state=0\|1 )

**Description:** Assumes that the sum of the specified loss formula is the negative log-likelihood and uses chi-square statistics instead of F statistics in the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/Logit Model w Loss1.jmp" );
obj = dt << Nonlinear(
    Loss( :Loss ),
    Show Prediction Expression( 1 ),
    Expand Intermediate Formulas( 1 )
);
obj << Loss is Neg LogLikelihood( 0 );
obj << Finish;
```

### [Newton](#newton)[](#newton "Click to copy url")

**Syntax:** obj \<\< Newton

**Description:** Specifies either Gauss-Newton (for regular least squares) or Newton-Raphson (for models that contain loss functions) as the optimization method.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ) );
obj << Newton;
obj << Finish;
```

### [Numeric Chain Deriv Delta](#numeric-chain-deriv-delta)[](#numeric-chain-deriv-delta "Click to copy url")

**Syntax:** obj \<\< Numeric Chain Deriv Delta( =1e-5 )

**Description:** Specifies the delta parameter used when approximating the derivative of a nonlinear formula that does not have a built-in derivative. "1e-5" by default.

**JMP Version Added:** 14

### [Numeric Derivatives Only](#numeric-derivatives-only)[](#numeric-derivatives-only "Click to copy url")

**Syntax:** obj \<\< Numeric Derivatives Only( state=0\|1 )

**Description:** Specifies that only numeric derivatives are used in the fitting method.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ) );
obj << Numeric Derivatives Only( 1 );
obj << Finish;
```

### [Obj Change Limit](#obj-change-limit)[](#obj-change-limit "Click to copy url")

**Syntax:** obj \<\< Obj Change Limit( number=1e-15 )

**Description:** Specifies the stop limit value for the objective change criterion. "1e-15" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Obj Change Limit( 1e-10 );
obj << Finish;
```

### [Parameter Bounds](#parameter-bounds)[](#parameter-bounds "Click to copy url")

**Syntax:** obj \<\< Parameter Bounds( \<parameter name( lower, upper )\> )

**Description:** Sets bounds on the specified parameters.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ) );
obj << Parameter Bounds( B0( 0, . ) );
obj << Finish;
```

### [Parameter Contour Profiler](#parameter-contour-profiler)[](#parameter-contour-profiler "Click to copy url")

**Syntax:** obj \<\< Parameter Contour Profiler( state=0\|1 )

**Description:** Shows or hides a contour profiler that profiles the SSE or loss as a function of the parameters.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
Wait( 0 );
obj << Parameter Contour Profiler( 1 );
```

### [Parameter Profiler](#parameter-profiler)[](#parameter-profiler "Click to copy url")

**Syntax:** obj \<\< Parameter Profiler( state=0\|1 )

**Description:** Shows or hides a prediction profiler that profiles the SSE or loss as a function of the parameters.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
Wait( 0 );
obj << Parameter Profiler( 1 );
```

### [Parameter Surface Profiler](#parameter-surface-profiler)[](#parameter-surface-profiler "Click to copy url")

**Syntax:** obj \<\< Parameter Surface Profiler( state=0\|1 )

**Description:** Shows or hides a three-dimensional surface plot that profiles the SSE or loss as a function of the parameters. This option is available only for models that contain two or more parameters.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
Wait( 0 );
obj << Parameter Surface Profiler( 1 );
```

### [Plot](#plot)[](#plot "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Shows or hides a graph that plots the prediction formula as a function of exactly one other variable. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ) );
Wait( 1 );
obj << Plot( 0 );
obj << Finish;
```

### [Profile Likelihood](#profile-likelihood)[](#profile-likelihood "Click to copy url")

**Syntax:** obj \<\< Profile Likelihood( state=0\|1 )

**Description:** Shows or hides a plot of the relative likelihood function, scaled to have a maximum value of one, across values of a single parameter while all other parameters are optimized to minimize the loss function. This option is available only when the Nonlinear platform is launched with a loss function that contains two or more parameters.

``` jsl
dt = Open( "$Sample_Data/Reliability/Fan.jmp" );
dt << New Column( "Unconstrained Weibull Loss",
    formula(
        Parameter(
            {mu = 10, logSigma = 0},
            If(
                Censor == 0, -Log( Weibull Density( Time, 1 / Exp( logSigma ), Exp( mu ) ) ),
                Censor == 1,
                    -Log( 1 - Weibull Distribution( Time, 1 / Exp( logSigma ), Exp( mu ) ) )
            )
        )
    )
);
obj = dt << Nonlinear(
    Loss( :Unconstrained Weibull Loss ),
    Numeric Derivatives Only( 1 ),
    Loss is Neg LogLikelihood( 1 ),
    Newton,
    Finish
);
Wait( 0 );
obj << Profile Likelihood( 1 );
```

### [Profile Likelihood Contour](#profile-likelihood-contour)[](#profile-likelihood-contour "Click to copy url")

**Syntax:** obj \<\< Profile Likelihood Contour( state=0\|1 )

**Description:** Shows or hides the likelihood confidence contours for the relative likelihood function across two parameters while all other parameters are optimized to minimize the loss function. This option is available only when the Nonlinear platform is launched with a loss function that contains three or more parameters.

``` jsl
dt = Open( "$Sample_Data/Reliability/Fan.jmp" );
dt << New Column( "Partial Unconstrained DS Weibull Loss",
    formula(
        Parameter(
            {mu = 10, logSigma = 0, p = 0.5},
            If(
                p < 0 | p > 1, .,
                Censor == 0,
                    -Log( p * Weibull Density( Time, 1 / Exp( logSigma ), Exp( mu ) ) ),
                Censor == 1,
                    -Log(
                        1 - p * Weibull Distribution( Time, 1 / Exp( logSigma ), Exp( mu ) )
                    )
            )
        )
    )
);
obj = dt << Nonlinear(
    Loss( :Partial Unconstrained DS Weibull Loss ),
    Numeric Derivatives Only( 1 ),
    Loss is Neg LogLikelihood( 1 ),
    Newton,
    Finish
);
Wait( 0 );
obj << Profile Likelihood Contour( 1 );
```

### [Profiler](#profiler)[](#profiler "Click to copy url")

**Syntax:** obj \<\< Profiler( state=0\|1 )

**Description:** Shows or hides the prediction profiler, which is used to graphically explore the prediction equation by slicing it one factor at a time. The prediction profiler contains features for optimization.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
obj << Profiler( 1 );
```

### [QuasiNewton BFGS](#quasinewton-bfgs)[](#quasinewton-bfgs "Click to copy url")

**Syntax:** obj \<\< QuasiNewton BFGS

**Description:** Specifies QuasiNewton BFGS as the optimization method. This method is best for large numbers of parameters.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ) );
obj << QuasiNewton BFGS;
obj << Finish;
```

### [QuasiNewton SR1](#quasinewton-sr1)[](#quasinewton-sr1 "Click to copy url")

**Syntax:** obj \<\< QuasiNewton SR1

**Description:** Specifies QuasiNewton SR1 as the optimization method. This method avoids recalculating the derivatives at each iteration.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ) );
obj << QuasiNewton SR1;
obj << Finish;
```

### [Relative Gradient](#relative-gradient)[](#relative-gradient "Click to copy url")

**Syntax:** obj \<\< Relative Gradient( number=1e-6 )

**Description:** Specifies the stop limit value for the relative gradient criterion. "1e-6" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Relative Gradient( 0.0001 );
obj << Finish;
```

### [Remember Solution](#remember-solution)[](#remember-solution "Click to copy url")

**Syntax:** obj \<\< Remember Solution( name )

**Description:** Creates a report called Remembered Models, which contains the current parameter estimates and summary statistics. Results of multiple models can be remembered and compared.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
obj << Remember Solution( "New Model" );
```

### [Reset](#reset)[](#reset "Click to copy url")

**Syntax:** obj \<\< Reset

**Description:** Resets the convergence criterion after solving. This option is useful when trying to refit the model with different starting values.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Set Parameter( B0 = 0.2 );
obj << Finish;
Wait( 2 );
obj << Reset;
```

### [Revert To Original Parameters](#revert-to-original-parameters)[](#revert-to-original-parameters "Click to copy url")

**Syntax:** obj \<\< Revert To Original Parameters

**Description:** Resets the current values of the parameters in the Control Panel to the original values.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
Wait( 1 );
obj << Revert to Original Parameters;
```

### [SSE Grid](#sse-grid)[](#sse-grid "Click to copy url")

**Syntax:** obj \<\< SSE Grid

**Description:** Creates a grid of values around the solution estimates and computes the error sum of squares for each value.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
obj << SSE Grid;
```

### [Save Estimates](#save-estimates)[](#save-estimates "Click to copy url")

**Syntax:** obj \<\< Save Estimates

**Description:** Saves the current parameter estimates to the parameter values in the formula column.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
Wait( 1 );
obj << Save Estimates;
```

### [Save Estimates To Table](#save-estimates-to-table)[](#save-estimates-to-table "Click to copy url")

**Syntax:** obj \<\< Save Estimates To Table

**Description:** Creates a new data table that contains the parameter estimates.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Estimates To Table;
```

### [Save Indiv Confid Limit Formula](#save-indiv-confid-limit-formula)[](#save-indiv-confid-limit-formula "Click to copy url")

**Syntax:** obj \<\< Save Indiv Confid Limit Formula

**Description:** Saves new formula columns to the data table. The new columns contain the formulas to calculate the confidence interval for an individual prediction. This is a confidence interval of an individual response value for a given X value.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Indiv Confid Limit Formula;
```

### [Save Indiv Confid Limits](#save-indiv-confid-limits)[](#save-indiv-confid-limits "Click to copy url")

**Syntax:** obj \<\< Save Indiv Confid Limits

**Description:** Saves new columns to the data table. The new columns contain the asymptotic confidence limits for an individual prediction. This is the confidence interval of an individual response value at a given X value.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Indiv Confid Limits;
```

### [Save Inverse Prediction Formula](#save-inverse-prediction-formula)[](#save-inverse-prediction-formula "Click to copy url")

**Syntax:** obj \<\< Save Inverse Prediction Formula

**Description:** Saves new formula columns to the data table. The new columns contain the formulas for the inverse prediction of the model, the standard error of an inverse prediction, and the standard error of an individual inverse prediction.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Inverse Prediction Formula;
```

### [Save Pred Confid Limit Formula](#save-pred-confid-limit-formula)[](#save-pred-confid-limit-formula "Click to copy url")

**Syntax:** obj \<\< Save Pred Confid Limit Formula

**Description:** Saves new formula columns to the data table. The new columns contain the formulas to calculate the confidence interval for a model prediction. This is a confidence interval for the average response value at a given X value.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Pred Confid Limit Formula;
```

### [Save Pred Confid Limits](#save-pred-confid-limits)[](#save-pred-confid-limits "Click to copy url")

**Syntax:** obj \<\< Save Pred Confid Limits

**Description:** Saves new columns to the data table. The new columns contain the asymptotic confidence limits for the model prediction. This is the confidence interval for the average response value at a given X value.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Pred Confid Limits;
```

### [Save Prediction Formula](#save-prediction-formula)[](#save-prediction-formula "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves a new formula column to the data table. The new column contains the prediction formula using the current parameter estimates.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Prediction Formula;
```

### [Save Residual Formula](#save-residual-formula)[](#save-residual-formula "Click to copy url")

**Syntax:** obj \<\< Save Residual Formula

**Description:** Saves a new formula column to the data table. The new column contains the formula for computing the residuals.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Residual Formula;
```

### [Save Specific Solving Formula](#save-specific-solving-formula)[](#save-specific-solving-formula "Click to copy url")

**Syntax:** obj \<\< Save Specific Solving Formula( \<column to solve for, {name1=expr1, ...}, Save Formula for Std Error Mean, Save Formula for Std Error Individual\> )

**Description:** Saves new formula columns to the data table. The new columns contain formulas for the prediction and standard error for evaluating an X variable given the response variable and either other X values in the data or a constant.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Specific Solving Formula;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Specific Solving Formula( :year, {:pop = 200}, Save Formula for Std Error Mean );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Specific Solving Formula( :pop, Save Formula for Std Error Individual );
```

### [Save Std Error of Individual](#save-std-error-of-individual)[](#save-std-error-of-individual "Click to copy url")

**Syntax:** obj \<\< Save Std Error of Individual

**Description:** Saves a new formula column to the data table. The new column contains the formula of the standard error for an individual prediction. This is the standard error for predicting an individual response value for a given X value.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Std Error of Individual;
```

### [Save Std Error of Predicted](#save-std-error-of-predicted)[](#save-std-error-of-predicted "Click to copy url")

**Syntax:** obj \<\< Save Std Error of Predicted

**Description:** Saves a new formula column to the data table. The new column contains the formula of the standard error for a model prediction. This is the standard error for predicting the average response value for a given X value.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish );
obj << Save Std Error of Predicted;
```

### [Second Deriv Method](#second-deriv-method)[](#second-deriv-method "Click to copy url")

**Syntax:** obj \<\< Second Deriv Method( state=0\|1 )

**Description:** Specifies that the fitting method use second derivatives.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Second Deriv Method( 1 ), Finish );
```

### [Set Parameter](#set-parameter)[](#set-parameter "Click to copy url")

**Syntax:** obj \<\< Set Parameter( name=expr, ... )

**Description:** Sets one or more parameter values prior to fitting the model. This is useful for both fixing a parameter at a particular value and for setting starting values.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Set Parameter( B0 = 0.2 );
Wait( 2 );
obj << Finish;
```

### [Show Derivatives](#show-derivatives)[](#show-derivatives "Click to copy url")

**Syntax:** obj \<\< Show Derivatives

**Description:** Shows the derivatives of the nonlinear formula in the log.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ) );
obj << Show Derivatives;
```

### [Show Prediction Expression](#show-prediction-expression)[](#show-prediction-expression "Click to copy url")

**Syntax:** obj \<\< Show Prediction Expression( state=0\|1 )

**Description:** Shows or hides the prediction model or the loss function in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/Logit Model w Loss1.jmp" );
obj = dt << Nonlinear(
    Loss( :Loss ),
    Show Prediction Expression( 1 ),
    Expand Intermediate Formulas( 1 ),
    Finish
);
```

### [Step](#step)[](#step "Click to copy url")

**Syntax:** obj \<\< Step

**Description:** Takes one iteration step toward solving the nonlinear model.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Step;
Wait( 1 );
obj << Step;
```

### [Stop](#stop)[](#stop "Click to copy url")

**Syntax:** obj \<\< Stop

**Description:** Interrupts the nonlinear model fitting process and stops it at the current iteration.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Go;
obj << Stop;
```

### [Surface Profiler](#surface-profiler)[](#surface-profiler "Click to copy url")

**Syntax:** obj \<\< Surface Profiler( state=0\|1 )

**Description:** Shows or hides a three-dimensional surface plot. This option is available only for models with two or more X variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ), Finish );
Wait( 0 );
obj << Surface Profiler( 1 );
```

### [Unlock Parameter](#unlock-parameter)[](#unlock-parameter "Click to copy url")

**Syntax:** obj \<\< Unlock Parameter( Name, ... )

**Description:** Unlocks the specified parameters. Use this option on previously locked factors so that they are free to change during the iteration process.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
obj = dt << Nonlinear( Y( :"log($ value)"n ), X( :Model ) );
obj << Set Parameter( B0 = 0.2 );
obj << Lock Parameter( B0, A, D );
obj << Finish;
Wait( 2 );
obj << Unlock Parameter( B0, A );
obj << Finish;
```

### [Unthreaded](#unthreaded)[](#unthreaded "Click to copy url")

**Syntax:** obj \<\< Unthreaded( state=0\|1 )

**Description:** Runs the iterations in the main computational thread.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/Algae Mitscherlich.jmp" );
obj = dt << Nonlinear( Y( :Algae density ), X( :Mitscherlich ) );
obj << Unthreaded( 1 );
obj << Finish;
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
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Nonlinear(
    Y( :pop ),
    X( :"X-formula"n ),
    Finish(),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
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
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Nonlinear(
    Y( :pop ),
    X( :"X-formula"n ),
    Finish(),
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
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
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
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
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
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
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
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
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
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Nonlinear(
    Y( :pop ),
    X( :"X-formula"n ),
    Finish(),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Nonlinear(
    Y( :pop ),
    X( :"X-formula"n ),
    Finish(),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Nonlinear(
    Y( :pop ),
    X( :"X-formula"n ),
    Finish(),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Nonlinear(
    Y( :pop ),
    X( :"X-formula"n ),
    Finish(),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Nonlinear(
    Y( :pop ),
    X( :"X-formula"n ),
    Finish(),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
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
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Nonlinear Examples/US Population.jmp" );
obj = dt << Nonlinear( Y( :pop ), X( :"X-formula"n ), Finish() );
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

**Syntax:** obj = Nonlinear(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

[ Previous](NodeGraphBox.html "NodeGraphBox") [Next ](Normal%20Mixtures.html "Normal Mixtures")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
