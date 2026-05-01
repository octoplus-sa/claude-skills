# Time Series

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Time%20Series.html](https://jsl.jmp.com/All%20Categories/Objects/Time%20Series.html)*

---

# [Time Series](#time-series)[](#time-series "Click to copy url")

## [ARIMA](#arima)[](#arima "Click to copy url")

### [Item Messages](#item-messages)[](#item-messages "Click to copy url")

#### [Actual](#actual)[](#actual "Click to copy url")

**Syntax:** obj \<\< Actual( state=0\|1 )

**Description:** Selects the Actual data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Actual( 1 ), Save Columns );
```

#### [Autocorrelations](#autocorrelations)[](#autocorrelations "Click to copy url")

**Syntax:** obj \<\< Autocorrelations( state=0\|1 )

**Description:** Displays or hides the autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Confidence Intervals](#confidence-intervals)[](#confidence-intervals "Click to copy url")

**Syntax:** obj \<\< Confidence Intervals( number )

#### [Create SAS Job](#create-sas-job)[](#create-sas-job "Click to copy url")

**Syntax:** obj \<\< Create SAS Job

**Description:** Creates a SAS Job to launch SAS and run the analysis in PROC ARIMA.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Create SAS Job;
```

#### [Innovations](#innovations)[](#innovations "Click to copy url")

**Syntax:** obj \<\< Innovations( state=0\|1 )

**Description:** On by default.

**JMP Version Added:** 16

#### [Lower Confidence Limit](#lower-confidence-limit)[](#lower-confidence-limit "Click to copy url")

**Syntax:** obj \<\< Lower Confidence Limit( state=0\|1 )

**Description:** Selects the Lower 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Lower Confidence Limit( 1 ), Save Columns );
```

#### [No Constrain](#no-constrain)[](#no-constrain "Click to copy url")

**Syntax:** obj \<\< No Constrain( state=0\|1 )

**Description:** Lifts the constraint on the autoregressive parameters to always remain within the stable region and the moving average parameters within the invertible region when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Constrain( 1 ) );
```

#### [No Intercept](#no-intercept)[](#no-intercept "Click to copy url")

**Syntax:** obj \<\< No Intercept( state=0\|1 )

**Description:** Sets the intercept to zero when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Intercept( 1 ) );
```

#### [Partial Autocorrelations](#partial-autocorrelations)[](#partial-autocorrelations "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelations( state=0\|1 )

**Description:** Displays or hides the partial autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Partial Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Plot](#plot)[](#plot "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Displays or hides the residual statistics plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Plot( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Predicted](#predicted)[](#predicted "Click to copy url")

**Syntax:** obj \<\< Predicted( state=0\|1 )

**Description:** Selects the Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Predicted( 1 ), Save Columns );
```

#### [Prediction Interval](#prediction-interval)[](#prediction-interval "Click to copy url")

**Syntax:** obj \<\< Prediction Interval( level )

**Description:** Sets the size of the confidence interval about the prediction for the ARIMA model. The default size is 0.95.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, Forecasting Interval( 0.99 ) );
```

#### [Remove Fit](#remove-fit)[](#remove-fit "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Residuals](#residuals)[](#residuals "Click to copy url")

**Syntax:** obj \<\< Residuals( state=0\|1 )

**Description:** Selects the Residuals values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Residuals( 1 ), Save Columns );
```

#### [Save Columns](#save-columns)[](#save-columns "Click to copy url")

**Syntax:** obj \<\< Save Columns

**Description:** Creates a new data table containing the actual and predicted values together with standard errors, residuals and 95% prediction intervals about the response. This option is available for all ARIMA, Smoothing, and Transfer Function models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Columns;
```

#### [Save Prediction Formula](#save-prediction-formula)[](#save-prediction-formula "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the Prediction Formula to a new column in the data table. This option is available for all ARIMA and Smoothing models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Prediction Formula;
```

#### [Show Confidence Interval](#show-confidence-interval)[](#show-confidence-interval "Click to copy url")

**Syntax:** obj \<\< Show Confidence Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Confidence Interval( 0 );
```

#### [Show Points](#show-points)[](#show-points "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides points on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Show Points( 1 ) );

(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Show Prediction Interval](#show-prediction-interval)[](#show-prediction-interval "Click to copy url")

**Syntax:** obj \<\< Show Prediction Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Prediction Interval( 0 );
```

#### [Std Error of Predicted](#std-error-of-predicted)[](#std-error-of-predicted "Click to copy url")

**Syntax:** obj \<\< Std Error of Predicted( state=0\|1 )

**Description:** Selects the Standard Error of Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Std Error of Predicted( 1 ), Save Columns );
```

#### [Time](#time)[](#time "Click to copy url")

**Syntax:** obj \<\< Time( state=0\|1 )

**Description:** Selects the Time data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ), Time ID( :Date ) );
obj << Arima( 1, 0, 0, Time( 0 ), Save Columns );
```

#### [Upper Confidence Limit](#upper-confidence-limit)[](#upper-confidence-limit "Click to copy url")

**Syntax:** obj \<\< Upper Confidence Limit( state=0\|1 )

**Description:** Selects the Upper 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Upper Confidence Limit( 1 ), Save Columns );
```

#### [Variogram](#variogram)[](#variogram "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Variogram( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Time Series](#time-series_1)[](#time-series_1 "Click to copy url")

**Syntax:** Time Series( Y( column ) )

**Description:** Models a series of observations over equally spaced time points. Includes a time series plot, autocorrelations, variogram, spectral density, ARIMA, seasonal ARIMA, smoothing models, and forecasts.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
```

## [Columns](#columns)[](#columns "Click to copy url")

### [By](#by)[](#by "Click to copy url")

**Syntax:** obj \<\< By( column(s) )

**Description:** Performs a separate analysis for each level of the specified column.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Time Series(
    Y( :steel shipments ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
```

### [Input List](#input-list)[](#input-list "Click to copy url")

**Syntax:** obj \<\< Input List( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
```

### [Time ID](#time-id)[](#time-id "Click to copy url")

**Syntax:** obj \<\< Time ID( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** obj \<\< X( column )

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
```

## [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

### [AR Coefficients](#ar-coefficients)[](#ar-coefficients "Click to copy url")

**Syntax:** obj \<\< AR Coefficients( state=0\|1 )

**Description:** Displays or hides the autocorrelation coefficient plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << AR Coefficients( 1 );
```

### [ARIMA](#arima_1)[](#arima_1 "Click to copy url")

**Syntax:** obj \<\< ARIMA( p, d, q, \<No Intercept( 0\|1 )\>, \<No Constrain( 0\|1 )\>, \<Confidence Intervals( level )\> )

**Description:** Fits an ARIMA model. Set order p,d, and q for an ARIMA(p,d,q) model. Set level for values other than 0.95.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << arima( 1, 0, 0 );
obj << arima( 1, 0, 0, No Intercept( 1 ), No Constrain( 1 ), Confidence Intervals( 0.99 ) );
```

### [ARIMA Model Group](#arima-model-group)[](#arima-model-group "Click to copy url")

**Syntax:** obj \<\< ARIMA Model Group( AR(p0,p1),Diff(d0,d1),MA(q0,q1),Seasonal AR(P0,P1),Seasonal Diff(D0,D1),Seasonal MA(Q0,Q1),Seasonal Period(S0,S1),Confidence Intervals(C),Intercept(1),Constrain fit(1) )

**Description:** Fit a set of ARIMA models whose orders are in specified ranges.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << ARIMA Model Group( AR( 0, 2 ), MA( 0, 2 ) );
```

### [Autocorrelation](#autocorrelation)[](#autocorrelation "Click to copy url")

**Syntax:** obj \<\< Autocorrelation( state=0\|1 )

**Description:** Displays or hides the autocorrelation plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Autocorrelation( 1 );
```

### [Autocorrelation Lags](#autocorrelation-lags)[](#autocorrelation-lags "Click to copy url")

**Syntax:** obj = Time Series(...Autocorrelation Lags( number=25 )...)

**Description:** Set launch option for the maximum number of periods between points used in computing autocorrelations. "25" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ), Autocorrelation Lags( 10 ) );
```

### [Combine and Save Forecasts from Models](#combine-and-save-forecasts-from-models)[](#combine-and-save-forecasts-from-models "Click to copy url")

**Syntax:** obj \<\< Combine and Save Forecasts from Models

**Description:** Creates a new data table with the combined results from all model fits in the report.

**JMP Version Added:** 16

### [Connecting Lines](#connecting-lines)[](#connecting-lines "Click to copy url")

**Syntax:** obj \<\< Connecting Lines( state=0\|1 )

**Description:** Displays or hides connected lines in the basic time series plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Connecting Lines( 1 );
```

### [Cross Correlation](#cross-correlation)[](#cross-correlation "Click to copy url")

**Syntax:** obj \<\< Cross Correlation( state=0\|1 )

**Description:** Displays or hides the cross correlation plot.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = dt << Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Cross Correlation( 1 );
```

### [Damped-Trend Linear Exponential Smoothing](#damped-trend-linear-exponential-smoothing)[](#damped-trend-linear-exponential-smoothing "Click to copy url")

**Syntax:** obj \<\< Damped-Trend Linear Exponential Smoothing( Zero to One\|Unconstrained\|Stable Invertible\|Custom( (Damping\|Level)( Unconstrained\| Bounded( lower, upper )\| Fixed( value ) )), \<Confidence Intervals(level)\> )

**Description:** Fits a damped trend smoothing model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
Time Series(
    Y( :Steel Shipments ),
    "Damped-Trend Linear Exponential Smoothing"n( Zero to One )
);
```

### [Difference](#difference)[](#difference "Click to copy url")

**Syntax:** obj \<\< Difference( d, \<D\>, \<S\> )

**Description:** Computes the differenced series and produces graphs of the autocorrelations and partial autocorrelations of the differenced series. The differenced series is given by (1-B)^d \* (1-B^S)^D \* y_t , where y_t is the time series, B is the backshift operator defined by B \* y_t = y\_(t-1), d is the nonseasonal differencing order, D is the seasonal differencing order, and S is the number of observations per period.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Difference( 1 );
obj << Difference( 1, 1, 12 );
```

### [Double Exponential Smoothing](#double-exponential-smoothing)[](#double-exponential-smoothing "Click to copy url")

**Syntax:** obj \<\< Double Exponential Smoothing( Zero to One\|Unconstrained\|Stable Invertible\|Custom( Level( Unconstrained\| Bounded( lower, upper )\| Fixed( value ) )), \<Confidence Intervals(level)\> )

**Description:** Invoke fitting a double exponential smoothing model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
Time Series(
    Y( :Steel Shipments ),
    Double Exponential Smoothing( Zero to One ),
    Double Exponential Smoothing( Unconstrained ),
    Double Exponential Smoothing( Stable Invertible ),
    Double Exponential Smoothing( Custom( Level( Bounded( 0.8, 1 ) ) ) ),
    Double Exponential Smoothing( Custom( Level( Fixed( 0 ) ) ) ),
    Double Exponential Smoothing( Custom( Level( Unconstrained ) ) )
);
```

### [Fit Recommended ETS](#fit-recommended-ets)[](#fit-recommended-ets "Click to copy url")

**Syntax:** obj \<\< Fit Recommended ETS( Period( m ),Constrained( "Yes"\|"No" ) )

**Description:** Fits all recommended state space smoothing models.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Seriesg.jmp" );
obj = dt << Time Series( Y( :Passengers ) );
obj << Fit Recommended ETS( Period( 12 ), Constrained( "Yes" ) );
```

### [Forecast Periods](#forecast-periods)[](#forecast-periods "Click to copy url")

**Syntax:** obj = Time Series(...Forecast Periods( number=25 )...)

**Description:** Set launch option for the number of steps ahead in forecasting report. "25" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ), Forecast Periods( 10 ) );
obj << ARIMA( 1, 0, 0 );
```

### [Forecast on Holdback](#forecast-on-holdback)[](#forecast-on-holdback "Click to copy url")

**Syntax:** obj = Time Series(...Forecast on Holdback( state=0\|1 )...)

**Description:** Determines whether the forecasts are made on future observations or on the holdback observations. If this option is selected, the forecasts are made on the holdback set that is determined by the number specified in the Forecast Periods option.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ), Forecast on Holdback( 1 ) );
obj << arima( 1, 0, 0 );
obj << Number of Forecast Periods( 100 );
```

### [Generate Simulation](#generate-simulation)[](#generate-simulation "Click to copy url")

**Syntax:** obj \<\< Generate Simulation( id, seed, length, n )

**Description:** Generates a data table of multiple future trajectories of a fitted model. Returns the table reference.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << arima( 1, 0, 0 );
dt = obj << Generate Simulation( 1, 11111, 100, 5 );
```

### [Get Model Specs](#get-model-specs)[](#get-model-specs "Click to copy url")

**Syntax:** obj \<\< Get Model Specs

**Description:** Returns a named list of model results, each of which is named by model specification. Included in the output are estimates and standard errors. Available for ARIMA, Seasonal ARIMA, all smoothing models and Transfer Function Models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Seriesg.jmp" );
obj = dt << Time Series( Y( :Log Passengers ) );
obj << Seasonal ARIMA( 0, 1, 1, 0, 1, 1, 12, No Intercept( 1 ) );
l = obj << Get Model Specs;
Show( l );
```

### [Get Models](#get-models)[](#get-models "Click to copy url")

**Syntax:** obj \<\< Get Models

**Description:** Returns a named list of model results, each of which is named by model descriptions. Included in the output are estimates and standard errors. Available for ARIMA, Seasonal ARIMA, all smoothing models and Transfer Function Models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Seriesg.jmp" );
obj = dt << Time Series( Y( :Log Passengers ) );
obj << Seasonal ARIMA( 0, 1, 1, 0, 1, 1, 12, No Intercept( 1 ) );
l = obj << Get Models;
Show( l );
```

### [Hide All Reports](#hide-all-reports)[](#hide-all-reports "Click to copy url")

**Syntax:** obj \<\< Hide All Reports

**Description:** Hides all of the models that are listed in the Model Comparison table from the report window.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Seriesg.jmp" );
obj = dt << Time Series( Y( :Passengers ) );
obj << Fit Recommended ETS( Period( 12 ), Constrained( "Yes" ) );
obj << Hide All Model Reports;
```

### [Input Series](#input-series)[](#input-series "Click to copy url")

**Syntax:** obj \<\< Input Series( Column, \<ARIMA( )\>\| \<Prewhitening( )\> ... )

**Description:** Groups messages sent to the input series. Note: requires an Input List variable be specified.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = dt << Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Input Series( :Input Gas Rate, ARIMA( 1, 0, 0 ) );
```

### [Keep Best Models](#keep-best-models)[](#keep-best-models "Click to copy url")

**Syntax:** obj \<\< Keep Best Models( "AIC"\|"SBC" )

**Description:** Retains the best models among individual model classes and removes the remaining models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Seriesg.jmp" );
obj = dt << Time Series( Y( :Passengers ) );
obj << Fit Recommended ETS( Period( 12 ), Constrained( "Yes" ) );
Wait( 1 );
obj << Keep Best Models( "AIC" );
```

### [Lambda for Box-Cox](#lambda-for-box-cox)[](#lambda-for-box-cox "Click to copy url")

**Syntax:** obj = Time Series(...Lambda for Box-Cox( number=0 )...)

**Description:** Specifies the lambda parameter used for the Box-Cox transformation of the original data. "0" by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series(
    Y( :Steel Shipments ),
    Name( "Use Box-Cox Transformation" )(1),
    Name( "Lambda for Box-Cox" )(0)
);
obj << arima( 1, 0, 0 );
obj << Number of Forecast Periods( 100 );
```

### [Linear Exponential Smoothing](#linear-exponential-smoothing)[](#linear-exponential-smoothing "Click to copy url")

**Syntax:** obj \<\< Linear Exponential Smoothing( Zero to One\|Unconstrained\|Stable Invertible\|Custom( (Trend\|Level)( Unconstrained\| Bounded( lower, upper )\| Fixed( value ) )), \<Confidence Intervals(level)\> )

**Description:** Fits a linear exponential smoothing model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
Time Series(
    Y( :Steel Shipments ),
    Linear Exponential Smoothing( Zero to One ),
    Linear Exponential Smoothing( Unconstrained ),
    Linear Exponential Smoothing( Stable Invertible ),
    Linear Exponential Smoothing(
        Custom( Level( Bounded( 0.8, 1 ) ), Trend( Bounded( 0.7, 0.9 ) ) )
    ),
    Linear Exponential Smoothing( Custom( Level( Fixed( 0 ) ), Trend( Fixed( .3 ) ) ) ),
    Linear Exponential Smoothing( Custom( Level( Unconstrained ), Trend( Fixed( .4 ) ) ) )
);
```

### [Maximum Iterations](#maximum-iterations)[](#maximum-iterations "Click to copy url")

**Syntax:** obj \<\< Maximum Iterations( maxIter=250 )

**Description:** Reset the maximum number of iterations for future optimizations used in ARIMA model fitting. "250" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Maximum Iterations( 2 );
obj << ARIMA( 1, 0, 0 );
```

### [Mean Line](#mean-line)[](#mean-line "Click to copy url")

**Syntax:** obj \<\< Mean Line( state=0\|1 )

**Description:** Displays or hides the mean line in the basic time series plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Mean Line( 1 );
```

### [Model Comparison Report](#model-comparison-report)[](#model-comparison-report "Click to copy url")

**Syntax:** obj \<\< Model Comparison Report

**Description:** Configures the Model Comparison report settings.

### [Number of Forecast Periods](#number-of-forecast-periods)[](#number-of-forecast-periods "Click to copy url")

**Syntax:** obj \<\< Number of Forecast Periods( number )

**Description:** Resets the number of forecast periods and updates the forecasting report.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << arima( 1, 0, 0 );
obj << Number of Forecast Periods( 100 );
```

### [Partial Autocorrelation](#partial-autocorrelation)[](#partial-autocorrelation "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelation( state=0\|1 )

**Description:** Displays or hides the partial autocorrelation plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Partial Autocorrelation( 1 );
```

### [Prewhitening](#prewhitening)[](#prewhitening "Click to copy url")

**Syntax:** obj \<\< Prewhitening( Order(p, d, q), Seasonal(P, D, Q, S) )

**Description:** Sets the prewhitening order.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = dt << Time Series(
    Y( :Output CO2 ),
    Input List( :Input Gas Rate ),
    Input Series(
        :Input Gas Rate,
        Prewhitening( Order( 1, 0, 0 ), Seasonal( 0, 0, 0, 12 ) )
    )
);
```

### [Remove All Simulation](#remove-all-simulation)[](#remove-all-simulation "Click to copy url")

**Syntax:** obj \<\< Remove All Simulation

**Description:** Removes all simulated future trajectories.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << arima( 1, 0, 0 );
obj << arima( 2, 0, 0 );
obj << Simulate More( 1, 2 );
obj << Simulate More( 2, 3 );
obj << Remove All Simulation;
```

### [Remove Cycle](#remove-cycle)[](#remove-cycle "Click to copy url")

**Syntax:** obj \<\< Remove Cycle( Units per Cycle( number ), Has Constant( 0\|1 ) )

**Description:** Estimates the cyclic component using a cosine function and then removes it from the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Monthly Sales.jmp" );
obj = dt << Time Series( Y( :Sales ) );
obj << Remove Cycle( Units per Cycle( 12 ), Has Constant( 1 ) );
```

### [Remove Fit](#remove-fit_1)[](#remove-fit_1 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

### [Remove Linear Trend](#remove-linear-trend)[](#remove-linear-trend "Click to copy url")

**Syntax:** obj \<\< Remove Linear Trend

**Description:** Estimates the linear trend and then removes it from the data.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Monthly Sales.jmp" );
obj = dt << Time Series( Y( :Sales ) );
obj << Remove Linear Trend;
```

### [Remove Model Simulation](#remove-model-simulation)[](#remove-model-simulation "Click to copy url")

**Syntax:** obj \<\< Remove Model Simulation( id )

**Description:** Removes simulated future trajectories of a fitted model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << arima( 1, 0, 0 );
obj << arima( 2, 0, 0 );
obj << Simulate More( 1, 2 );
obj << Simulate More( 2, 3 );
obj << Remove Model Simulation( 1 );
```

### [Save Spectral Density](#save-spectral-density)[](#save-spectral-density "Click to copy url")

**Syntax:** obj \<\< Save Spectral Density

**Description:** Save spectral density to a table.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Save Spectral Density;
```

### [Seasonal ARIMA](#seasonal-arima)[](#seasonal-arima "Click to copy url")

**Syntax:** obj \<\< Seasonal ARIMA( p, d, q, P, D, Q, S, \<No Intercept( 0\|1 )\>, \<No Constrain( 0\|1 )\>, \<Confidence Intervals( level )\> )

**Description:** Fits a seasonal ARIMA model. Set order p,d,q,P,D,Q,and S for an ARIMA(p,d,q)(P,D,Q)S model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << seasonal arima( 1, 0, 0, 1, 0, 0, 12 );
obj << seasonal arima(
    1,
    0,
    0,
    1,
    0,
    0,
    12,
    No Intercept( 1 ),
    No Constrain( 1 ),
    Confidence Intervals( 0.99 )
);
```

### [Seasonal Exponential Smoothing](#seasonal-exponential-smoothing)[](#seasonal-exponential-smoothing "Click to copy url")

**Syntax:** obj \<\< Seasonal Exponential Smoothing( Zero to One\|Unconstrained\|Custom( (Level\| Seasonal)( Unconstrained\| Bounded( lower, upper )\| Fixed( value ) )), \<Confidence Intervals(level)\> )

**Description:** Fits a seasonal exponential smoothing model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
Time Series(
    Y( :Steel Shipments ),
    Seasonal Exponential Smoothing(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Seasonal( Bounded( 0, 1 ) ) )
    )
);
```

### [Set Seed](#set-seed)[](#set-seed "Click to copy url")

**Syntax:** obj \<\< Set Seed( seed )

**Description:** Sets random seed.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << arima( 1, 0, 0 );
obj << Set Seed( 1111 );
obj << Simulate Once( 1 );
obj << Set Seed( 1111 );
obj << Simulate Once( 1 );
```

### [Show Box-Cox Transformation Plot](#show-box-cox-transformation-plot)[](#show-box-cox-transformation-plot "Click to copy url")

**Syntax:** obj \<\< Show Box-Cox Transformation Plot( state=0\|1 )

**JMP Version Added:** 16

### [Show Lag Plot](#show-lag-plot)[](#show-lag-plot "Click to copy url")

**Syntax:** obj \<\< Show Lag Plot( state=0\|1 )

### [Show Points](#show-points_1)[](#show-points_1 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Displays or hides points in the basic time series plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Show Points( 1 );
```

### [Simple Exponential Smoothing](#simple-exponential-smoothing)[](#simple-exponential-smoothing "Click to copy url")

**Syntax:** obj \<\< Simple Exponential Smoothing( Zero to One\|Unconstrained\|Stable Invertible\|Custom( Level( Unconstrained\| Bounded( lower, upper )\| Fixed( value ) )), \<Confidence Intervals(level)\> )

**Description:** Fits a simple exponential smoothing model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
Time Series(
    Y( :Steel Shipments ),
    Simple Exponential Smoothing( Zero to One ),
    Simple Exponential Smoothing( Unconstrained ),
    Simple Exponential Smoothing( Stable Invertible ),
    Simple Exponential Smoothing( Custom( Level( Bounded( 0.8, 1 ) ) ) ),
    Simple Exponential Smoothing( Custom( Level( Fixed( 0 ) ) ) ),
    Simple Exponential Smoothing( Custom( Level( Unconstrained ) ) )
);
```

### [Simple Moving Average](#simple-moving-average)[](#simple-moving-average "Click to copy url")

**Syntax:** obj \<\< Simple Moving Average

**Description:** Invoke a simple moving average specification dialog and fit a model, if there are no additional arguments. Pass arguments to the simple moving average model scriptable. Return value is the simple moving average model scriptable handle. See Simple Moving Average scriptable for arguments details.

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
obj = dt << Time Series( Y( :Close ) );
sma = obj << Simple Moving Average;
sma << Add Model( 10 );
```

### [Simple Moving Average Centering Method](#simple-moving-average-centering-method)[](#simple-moving-average-centering-method "Click to copy url")

**Syntax:** obj \<\< Simple Moving Average Centering Method( "No Centering"\|"Centered"\|"Centered and Double Smoothed for Even Number of Terms" )

### [Simulate More](#simulate-more)[](#simulate-more "Click to copy url")

**Syntax:** obj \<\< Simulate More( id, n )

**Description:** Simulates multiple future trajectories of a fitted model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << arima( 1, 0, 0 );
obj << arima( 2, 0, 0 );
obj << Simulate More( 1, 2 );
obj << Simulate More( 2, 3 );
```

### [Simulate Once](#simulate-once)[](#simulate-once "Click to copy url")

**Syntax:** obj \<\< Simulate Once( id )

**Description:** Simulates one future trajectory of a fitted model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << arima( 1, 0, 0 );
obj << arima( 2, 0, 0 );
obj << Simulate Once( 1 );
obj << Simulate Once( 2 );
```

### [Spectral Density](#spectral-density)[](#spectral-density "Click to copy url")

**Syntax:** obj \<\< Spectral Density( state=0\|1 )

**Description:** Displays or hides the spectral density graphs.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Spectral Density( 1 );
```

### [State Space Smoothing](#state-space-smoothing)[](#state-space-smoothing "Click to copy url")

**Syntax:** obj \<\< State Space Smoothing( Error Type( "Additive"\|"Multiplicative" ),Trend Type( "None"\|"Additive"\|"Multiplicative" ),Seasonal Type( "None"\|"Additive"\|"Multiplicative" ),Damped( "Yes"\|"No" ),Period( m ),Constrained( "Yes"\|"No" ) )

**Description:** Fits a state space smoothing model.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Seriesg.jmp" );
obj = dt << Time Series( Y( :Passengers ) );
obj << State Space Smoothing(
    Error Type( "Multiplicative" ),
    Trend Type( "Additive" ),
    Seasonal Type( "Multiplicative" ),
    Damped( "No" ),
    Period( 12 ),
    Constrained( "Yes" )
);
```

### [Time Series Graph](#time-series-graph)[](#time-series-graph "Click to copy url")

**Syntax:** obj \<\< Time Series Graph( state=0\|1 )

**Description:** Turn on or off the basic time series plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Time Series Graph( 1 );
```

### [Transfer Function](#transfer-function)[](#transfer-function "Click to copy url")

**Syntax:** obj \<\< Transfer Function( Order(p, d, q), Seasonal(P, D, Q, S), input1(Order(p, d, q), Seasonal(P, D, Q, S), Lag(lag)), \<input2(Order(p, d, q), Seasonal(P, D, Q, S), Lag(lag))\>, ..., \<No Intercept(flag1)\>, \<No Constrain(flag2)\>, \<Alternative Parameterization( flag3 )\>, \<Confidence Intervals( level )\>, \<Number of Forecast Periods( nAhead )\> )

**Description:** Fits a Transfer Function model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = dt << Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) )
);
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    No Intercept( 1 ),
    Alternative Parameterization( 1 ),
    Confidence Intervals( 0.99 ),
    Number of Forecast Periods( 10 )
);
```

### [Use Box-Cox Transformation](#use-box-cox-transformation)[](#use-box-cox-transformation "Click to copy url")

**Syntax:** obj = Time Series(...Use Box-Cox Transformation( state=0\|1 )...)

**Description:** Transforms the original data using a Box-Cox transformation with the lambda that is specified in the Lambda for Box-Cox option. If this option is selected, all analyses in the Time Series report are performed on the transformed data.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ), Name( "Use Box-Cox Transformation" )(1) );
obj << arima( 1, 0, 0 );
obj << Number of Forecast Periods( 100 );
```

### [Variogram](#variogram_1)[](#variogram_1 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the variogram plot in the Time Series Basic Diagnostics report.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :Steel Shipments ) );
obj << Variogram( 1 );
```

### [Winters Method](#winters-method)[](#winters-method "Click to copy url")

**Syntax:** obj \<\< Winters Method( Zero to One\|Unconstrained\|Custom( (Level\|Seasonal\|Trend)( Unconstrained\| Seasonal\| Bounded( lower, upper )\| Fixed( value ) )), \<Confidence Intervals(level)\> )

**Description:** Fits a smoothing model using Winter's method.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom(
            Level( Bounded( 0, 1 ) ),
            Trend( Bounded( 0, 1 ) ),
            Seasonal( Bounded( 0, 1 ) )
        )
    )
);
```

### [X11](#x11)[](#x11 "Click to copy url")

**Syntax:** obj \<\< X11( Additive\|Multiplicative )

**Description:** Removes trend and seasonal effects using the X-11 method developed by the US Bureau of the Census.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Monthly Sales.jmp" );
obj = dt << Time Series( X( :Date ), Y( :Sales ) );
obj << X11( Additive );
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
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
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
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Time Series(
    Y( :steel shipments ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
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
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Time Series(
    Y( :steel shipments ),
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
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
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
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
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
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
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
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
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
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Time Series(
    Y( :steel shipments ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Time Series(
    Y( :steel shipments ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Time Series(
    Y( :steel shipments ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Time Series(
    Y( :steel shipments ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Time Series(
    Y( :steel shipments ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
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
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = dt << Time Series( Y( :steel shipments ) );
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

**Syntax:** obj = Time Series(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

## [Damped-Trend Linear Exponential Smoothing](#damped-trend-linear-exponential-smoothing_1)[](#damped-trend-linear-exponential-smoothing_1 "Click to copy url")

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Actual](#actual_1)[](#actual_1 "Click to copy url")

**Syntax:** obj \<\< Actual( state=0\|1 )

**Description:** Selects the Actual data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Actual( 1 ), Save Columns );
```

#### [Autocorrelations](#autocorrelations_1)[](#autocorrelations_1 "Click to copy url")

**Syntax:** obj \<\< Autocorrelations( state=0\|1 )

**Description:** Displays or hides the autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Confidence Intervals](#confidence-intervals_1)[](#confidence-intervals_1 "Click to copy url")

**Syntax:** obj \<\< Confidence Intervals( number )

#### [Create SAS Job](#create-sas-job_1)[](#create-sas-job_1 "Click to copy url")

**Syntax:** obj \<\< Create SAS Job

**Description:** Creates a SAS Job to launch SAS and run the analysis in PROC ARIMA.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Create SAS Job;
```

#### [Innovations](#innovations_1)[](#innovations_1 "Click to copy url")

**Syntax:** obj \<\< Innovations( state=0\|1 )

**Description:** On by default.

**JMP Version Added:** 16

#### [Lower Confidence Limit](#lower-confidence-limit_1)[](#lower-confidence-limit_1 "Click to copy url")

**Syntax:** obj \<\< Lower Confidence Limit( state=0\|1 )

**Description:** Selects the Lower 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Lower Confidence Limit( 1 ), Save Columns );
```

#### [No Constrain](#no-constrain_1)[](#no-constrain_1 "Click to copy url")

**Syntax:** obj \<\< No Constrain( state=0\|1 )

**Description:** Lifts the constraint on the autoregressive parameters to always remain within the stable region and the moving average parameters within the invertible region when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Constrain( 1 ) );
```

#### [No Intercept](#no-intercept_1)[](#no-intercept_1 "Click to copy url")

**Syntax:** obj \<\< No Intercept( state=0\|1 )

**Description:** Sets the intercept to zero when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Intercept( 1 ) );
```

#### [Partial Autocorrelations](#partial-autocorrelations_1)[](#partial-autocorrelations_1 "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelations( state=0\|1 )

**Description:** Displays or hides the partial autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Partial Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Plot](#plot_1)[](#plot_1 "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Displays or hides the residual statistics plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Plot( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Predicted](#predicted_1)[](#predicted_1 "Click to copy url")

**Syntax:** obj \<\< Predicted( state=0\|1 )

**Description:** Selects the Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Predicted( 1 ), Save Columns );
```

#### [Prediction Interval](#prediction-interval_1)[](#prediction-interval_1 "Click to copy url")

**Syntax:** obj \<\< Prediction Interval( level )

**Description:** Sets the size of the confidence interval about the prediction for the ARIMA model. The default size is 0.95.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, Forecasting Interval( 0.99 ) );
```

#### [Remove Fit](#remove-fit_2)[](#remove-fit_2 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Residuals](#residuals_1)[](#residuals_1 "Click to copy url")

**Syntax:** obj \<\< Residuals( state=0\|1 )

**Description:** Selects the Residuals values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Residuals( 1 ), Save Columns );
```

#### [Save Columns](#save-columns_1)[](#save-columns_1 "Click to copy url")

**Syntax:** obj \<\< Save Columns

**Description:** Creates a new data table containing the actual and predicted values together with standard errors, residuals and 95% prediction intervals about the response. This option is available for all ARIMA, Smoothing, and Transfer Function models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Columns;
```

#### [Save Prediction Formula](#save-prediction-formula_1)[](#save-prediction-formula_1 "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the Prediction Formula to a new column in the data table. This option is available for all ARIMA and Smoothing models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Prediction Formula;
```

#### [Show Confidence Interval](#show-confidence-interval_1)[](#show-confidence-interval_1 "Click to copy url")

**Syntax:** obj \<\< Show Confidence Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Confidence Interval( 0 );
```

#### [Show Points](#show-points_2)[](#show-points_2 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides points on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Show Points( 1 ) );

(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Show Prediction Interval](#show-prediction-interval_1)[](#show-prediction-interval_1 "Click to copy url")

**Syntax:** obj \<\< Show Prediction Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Prediction Interval( 0 );
```

#### [Std Error of Predicted](#std-error-of-predicted_1)[](#std-error-of-predicted_1 "Click to copy url")

**Syntax:** obj \<\< Std Error of Predicted( state=0\|1 )

**Description:** Selects the Standard Error of Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Std Error of Predicted( 1 ), Save Columns );
```

#### [Time](#time_1)[](#time_1 "Click to copy url")

**Syntax:** obj \<\< Time( state=0\|1 )

**Description:** Selects the Time data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ), Time ID( :Date ) );
obj << Arima( 1, 0, 0, Time( 0 ), Save Columns );
```

#### [Upper Confidence Limit](#upper-confidence-limit_1)[](#upper-confidence-limit_1 "Click to copy url")

**Syntax:** obj \<\< Upper Confidence Limit( state=0\|1 )

**Description:** Selects the Upper 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Upper Confidence Limit( 1 ), Save Columns );
```

#### [Variogram](#variogram_2)[](#variogram_2 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Variogram( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

## [Difference](#difference_1)[](#difference_1 "Click to copy url")

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [Autocorrelation](#autocorrelation_1)[](#autocorrelation_1 "Click to copy url")

**Syntax:** obj \<\< Autocorrelation( state=0\|1 )

**Description:** Displays or hides the Autocorrelation in the Difference report. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Difference( 1, 0, 0, Autocorrelation( 1 ) );
```

#### [Connecting Lines](#connecting-lines_1)[](#connecting-lines_1 "Click to copy url")

**Syntax:** obj \<\< Connecting Lines( state=0\|1 )

**Description:** Displays or hides the lines connecting the points on the Difference Graph. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Difference( 1, 0, 0, Connecting Lines( 1 ) );
```

#### [Difference Graph](#difference-graph)[](#difference-graph "Click to copy url")

**Syntax:** obj \<\< Difference Graph( state=0\|1 )

**Description:** Displays or hides the Difference Graph. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Difference( 1, 0, 0, Difference Graph( 1 ) );
```

#### [Mean Line](#mean-line_1)[](#mean-line_1 "Click to copy url")

**Syntax:** obj \<\< Mean Line( state=0\|1 )

**Description:** Displays or hides the mean line on the Difference Graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Difference( 1, 0, 0, Mean Line( 1 ) );
```

#### [Partial Autocorrelation](#partial-autocorrelation_1)[](#partial-autocorrelation_1 "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelation( state=0\|1 )

**Description:** Displays or hides the Partial Autocorrelation in the Difference report. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Difference( 1, 0, 0, Partial Autocorrelation( 1 ) );
```

#### [Remove Fit](#remove-fit_3)[](#remove-fit_3 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Save](#save)[](#save "Click to copy url")

**Syntax:** obj \<\< Save

**Description:** Saves the Difference values in a new column in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Difference( 1, 0, 0, Save );
```

#### [Show Points](#show-points_3)[](#show-points_3 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Displays or hides the points on the Difference Graph. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Difference( 1, 0, 0, Show Points( 1 ) );
```

#### [Variogram](#variogram_3)[](#variogram_3 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram in the Difference report.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Difference( 1, 0, 0, Variogram( 1 ) );
```

## [Double (Brown) Exponential Smoothing](#double-brown-exponential-smoothing)[](#double-brown-exponential-smoothing "Click to copy url")

### [Item Messages](#item-messages_4)[](#item-messages_4 "Click to copy url")

#### [Actual](#actual_2)[](#actual_2 "Click to copy url")

**Syntax:** obj \<\< Actual( state=0\|1 )

**Description:** Selects the Actual data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Actual( 1 ), Save Columns );
```

#### [Autocorrelations](#autocorrelations_2)[](#autocorrelations_2 "Click to copy url")

**Syntax:** obj \<\< Autocorrelations( state=0\|1 )

**Description:** Displays or hides the autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Confidence Intervals](#confidence-intervals_2)[](#confidence-intervals_2 "Click to copy url")

**Syntax:** obj \<\< Confidence Intervals( number )

#### [Create SAS Job](#create-sas-job_2)[](#create-sas-job_2 "Click to copy url")

**Syntax:** obj \<\< Create SAS Job

**Description:** Creates a SAS Job to launch SAS and run the analysis in PROC ARIMA.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Create SAS Job;
```

#### [Innovations](#innovations_2)[](#innovations_2 "Click to copy url")

**Syntax:** obj \<\< Innovations( state=0\|1 )

**Description:** On by default.

**JMP Version Added:** 16

#### [Lower Confidence Limit](#lower-confidence-limit_2)[](#lower-confidence-limit_2 "Click to copy url")

**Syntax:** obj \<\< Lower Confidence Limit( state=0\|1 )

**Description:** Selects the Lower 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Lower Confidence Limit( 1 ), Save Columns );
```

#### [No Constrain](#no-constrain_2)[](#no-constrain_2 "Click to copy url")

**Syntax:** obj \<\< No Constrain( state=0\|1 )

**Description:** Lifts the constraint on the autoregressive parameters to always remain within the stable region and the moving average parameters within the invertible region when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Constrain( 1 ) );
```

#### [No Intercept](#no-intercept_2)[](#no-intercept_2 "Click to copy url")

**Syntax:** obj \<\< No Intercept( state=0\|1 )

**Description:** Sets the intercept to zero when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Intercept( 1 ) );
```

#### [Partial Autocorrelations](#partial-autocorrelations_2)[](#partial-autocorrelations_2 "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelations( state=0\|1 )

**Description:** Displays or hides the partial autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Partial Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Plot](#plot_2)[](#plot_2 "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Displays or hides the residual statistics plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Plot( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Predicted](#predicted_2)[](#predicted_2 "Click to copy url")

**Syntax:** obj \<\< Predicted( state=0\|1 )

**Description:** Selects the Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Predicted( 1 ), Save Columns );
```

#### [Prediction Interval](#prediction-interval_2)[](#prediction-interval_2 "Click to copy url")

**Syntax:** obj \<\< Prediction Interval( level )

**Description:** Sets the size of the confidence interval about the prediction for the ARIMA model. The default size is 0.95.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, Forecasting Interval( 0.99 ) );
```

#### [Remove Fit](#remove-fit_4)[](#remove-fit_4 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Residuals](#residuals_2)[](#residuals_2 "Click to copy url")

**Syntax:** obj \<\< Residuals( state=0\|1 )

**Description:** Selects the Residuals values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Residuals( 1 ), Save Columns );
```

#### [Save Columns](#save-columns_2)[](#save-columns_2 "Click to copy url")

**Syntax:** obj \<\< Save Columns

**Description:** Creates a new data table containing the actual and predicted values together with standard errors, residuals and 95% prediction intervals about the response. This option is available for all ARIMA, Smoothing, and Transfer Function models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Columns;
```

#### [Save Prediction Formula](#save-prediction-formula_2)[](#save-prediction-formula_2 "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the Prediction Formula to a new column in the data table. This option is available for all ARIMA and Smoothing models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Prediction Formula;
```

#### [Show Confidence Interval](#show-confidence-interval_2)[](#show-confidence-interval_2 "Click to copy url")

**Syntax:** obj \<\< Show Confidence Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Confidence Interval( 0 );
```

#### [Show Points](#show-points_4)[](#show-points_4 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides points on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Show Points( 1 ) );

(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Show Prediction Interval](#show-prediction-interval_2)[](#show-prediction-interval_2 "Click to copy url")

**Syntax:** obj \<\< Show Prediction Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Prediction Interval( 0 );
```

#### [Std Error of Predicted](#std-error-of-predicted_2)[](#std-error-of-predicted_2 "Click to copy url")

**Syntax:** obj \<\< Std Error of Predicted( state=0\|1 )

**Description:** Selects the Standard Error of Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Std Error of Predicted( 1 ), Save Columns );
```

#### [Time](#time_2)[](#time_2 "Click to copy url")

**Syntax:** obj \<\< Time( state=0\|1 )

**Description:** Selects the Time data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ), Time ID( :Date ) );
obj << Arima( 1, 0, 0, Time( 0 ), Save Columns );
```

#### [Upper Confidence Limit](#upper-confidence-limit_2)[](#upper-confidence-limit_2 "Click to copy url")

**Syntax:** obj \<\< Upper Confidence Limit( state=0\|1 )

**Description:** Selects the Upper 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Upper Confidence Limit( 1 ), Save Columns );
```

#### [Variogram](#variogram_4)[](#variogram_4 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Variogram( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

## [Linear (Holt) Exponential Smoothing](#linear-holt-exponential-smoothing)[](#linear-holt-exponential-smoothing "Click to copy url")

### [Item Messages](#item-messages_5)[](#item-messages_5 "Click to copy url")

#### [Actual](#actual_3)[](#actual_3 "Click to copy url")

**Syntax:** obj \<\< Actual( state=0\|1 )

**Description:** Selects the Actual data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Actual( 1 ), Save Columns );
```

#### [Autocorrelations](#autocorrelations_3)[](#autocorrelations_3 "Click to copy url")

**Syntax:** obj \<\< Autocorrelations( state=0\|1 )

**Description:** Displays or hides the autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Confidence Intervals](#confidence-intervals_3)[](#confidence-intervals_3 "Click to copy url")

**Syntax:** obj \<\< Confidence Intervals( number )

#### [Create SAS Job](#create-sas-job_3)[](#create-sas-job_3 "Click to copy url")

**Syntax:** obj \<\< Create SAS Job

**Description:** Creates a SAS Job to launch SAS and run the analysis in PROC ARIMA.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Create SAS Job;
```

#### [Innovations](#innovations_3)[](#innovations_3 "Click to copy url")

**Syntax:** obj \<\< Innovations( state=0\|1 )

**Description:** On by default.

**JMP Version Added:** 16

#### [Lower Confidence Limit](#lower-confidence-limit_3)[](#lower-confidence-limit_3 "Click to copy url")

**Syntax:** obj \<\< Lower Confidence Limit( state=0\|1 )

**Description:** Selects the Lower 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Lower Confidence Limit( 1 ), Save Columns );
```

#### [No Constrain](#no-constrain_3)[](#no-constrain_3 "Click to copy url")

**Syntax:** obj \<\< No Constrain( state=0\|1 )

**Description:** Lifts the constraint on the autoregressive parameters to always remain within the stable region and the moving average parameters within the invertible region when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Constrain( 1 ) );
```

#### [No Intercept](#no-intercept_3)[](#no-intercept_3 "Click to copy url")

**Syntax:** obj \<\< No Intercept( state=0\|1 )

**Description:** Sets the intercept to zero when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Intercept( 1 ) );
```

#### [Partial Autocorrelations](#partial-autocorrelations_3)[](#partial-autocorrelations_3 "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelations( state=0\|1 )

**Description:** Displays or hides the partial autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Partial Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Plot](#plot_3)[](#plot_3 "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Displays or hides the residual statistics plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Plot( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Predicted](#predicted_3)[](#predicted_3 "Click to copy url")

**Syntax:** obj \<\< Predicted( state=0\|1 )

**Description:** Selects the Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Predicted( 1 ), Save Columns );
```

#### [Prediction Interval](#prediction-interval_3)[](#prediction-interval_3 "Click to copy url")

**Syntax:** obj \<\< Prediction Interval( level )

**Description:** Sets the size of the confidence interval about the prediction for the ARIMA model. The default size is 0.95.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, Forecasting Interval( 0.99 ) );
```

#### [Remove Fit](#remove-fit_5)[](#remove-fit_5 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Residuals](#residuals_3)[](#residuals_3 "Click to copy url")

**Syntax:** obj \<\< Residuals( state=0\|1 )

**Description:** Selects the Residuals values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Residuals( 1 ), Save Columns );
```

#### [Save Columns](#save-columns_3)[](#save-columns_3 "Click to copy url")

**Syntax:** obj \<\< Save Columns

**Description:** Creates a new data table containing the actual and predicted values together with standard errors, residuals and 95% prediction intervals about the response. This option is available for all ARIMA, Smoothing, and Transfer Function models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Columns;
```

#### [Save Prediction Formula](#save-prediction-formula_3)[](#save-prediction-formula_3 "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the Prediction Formula to a new column in the data table. This option is available for all ARIMA and Smoothing models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Prediction Formula;
```

#### [Show Confidence Interval](#show-confidence-interval_3)[](#show-confidence-interval_3 "Click to copy url")

**Syntax:** obj \<\< Show Confidence Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Confidence Interval( 0 );
```

#### [Show Points](#show-points_5)[](#show-points_5 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides points on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Show Points( 1 ) );

(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Show Prediction Interval](#show-prediction-interval_3)[](#show-prediction-interval_3 "Click to copy url")

**Syntax:** obj \<\< Show Prediction Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Prediction Interval( 0 );
```

#### [Std Error of Predicted](#std-error-of-predicted_3)[](#std-error-of-predicted_3 "Click to copy url")

**Syntax:** obj \<\< Std Error of Predicted( state=0\|1 )

**Description:** Selects the Standard Error of Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Std Error of Predicted( 1 ), Save Columns );
```

#### [Time](#time_3)[](#time_3 "Click to copy url")

**Syntax:** obj \<\< Time( state=0\|1 )

**Description:** Selects the Time data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ), Time ID( :Date ) );
obj << Arima( 1, 0, 0, Time( 0 ), Save Columns );
```

#### [Upper Confidence Limit](#upper-confidence-limit_3)[](#upper-confidence-limit_3 "Click to copy url")

**Syntax:** obj \<\< Upper Confidence Limit( state=0\|1 )

**Description:** Selects the Upper 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Upper Confidence Limit( 1 ), Save Columns );
```

#### [Variogram](#variogram_5)[](#variogram_5 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Variogram( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

## [Seasonal ARIMA](#seasonal-arima_1)[](#seasonal-arima_1 "Click to copy url")

### [Item Messages](#item-messages_6)[](#item-messages_6 "Click to copy url")

#### [Actual](#actual_4)[](#actual_4 "Click to copy url")

**Syntax:** obj \<\< Actual( state=0\|1 )

**Description:** Selects the Actual data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Actual( 1 ), Save Columns );
```

#### [Autocorrelations](#autocorrelations_4)[](#autocorrelations_4 "Click to copy url")

**Syntax:** obj \<\< Autocorrelations( state=0\|1 )

**Description:** Displays or hides the autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Confidence Intervals](#confidence-intervals_4)[](#confidence-intervals_4 "Click to copy url")

**Syntax:** obj \<\< Confidence Intervals( number )

#### [Create SAS Job](#create-sas-job_4)[](#create-sas-job_4 "Click to copy url")

**Syntax:** obj \<\< Create SAS Job

**Description:** Creates a SAS Job to launch SAS and run the analysis in PROC ARIMA.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Create SAS Job;
```

#### [Innovations](#innovations_4)[](#innovations_4 "Click to copy url")

**Syntax:** obj \<\< Innovations( state=0\|1 )

**Description:** On by default.

**JMP Version Added:** 16

#### [Lower Confidence Limit](#lower-confidence-limit_4)[](#lower-confidence-limit_4 "Click to copy url")

**Syntax:** obj \<\< Lower Confidence Limit( state=0\|1 )

**Description:** Selects the Lower 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Lower Confidence Limit( 1 ), Save Columns );
```

#### [No Constrain](#no-constrain_4)[](#no-constrain_4 "Click to copy url")

**Syntax:** obj \<\< No Constrain( state=0\|1 )

**Description:** Lifts the constraint on the autoregressive parameters to always remain within the stable region and the moving average parameters within the invertible region when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Constrain( 1 ) );
```

#### [No Intercept](#no-intercept_4)[](#no-intercept_4 "Click to copy url")

**Syntax:** obj \<\< No Intercept( state=0\|1 )

**Description:** Sets the intercept to zero when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Intercept( 1 ) );
```

#### [Partial Autocorrelations](#partial-autocorrelations_4)[](#partial-autocorrelations_4 "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelations( state=0\|1 )

**Description:** Displays or hides the partial autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Partial Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Plot](#plot_4)[](#plot_4 "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Displays or hides the residual statistics plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Plot( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Predicted](#predicted_4)[](#predicted_4 "Click to copy url")

**Syntax:** obj \<\< Predicted( state=0\|1 )

**Description:** Selects the Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Predicted( 1 ), Save Columns );
```

#### [Prediction Interval](#prediction-interval_4)[](#prediction-interval_4 "Click to copy url")

**Syntax:** obj \<\< Prediction Interval( level )

**Description:** Sets the size of the confidence interval about the prediction for the ARIMA model. The default size is 0.95.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, Forecasting Interval( 0.99 ) );
```

#### [Remove Fit](#remove-fit_6)[](#remove-fit_6 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Residuals](#residuals_4)[](#residuals_4 "Click to copy url")

**Syntax:** obj \<\< Residuals( state=0\|1 )

**Description:** Selects the Residuals values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Residuals( 1 ), Save Columns );
```

#### [Save Columns](#save-columns_4)[](#save-columns_4 "Click to copy url")

**Syntax:** obj \<\< Save Columns

**Description:** Creates a new data table containing the actual and predicted values together with standard errors, residuals and 95% prediction intervals about the response. This option is available for all ARIMA, Smoothing, and Transfer Function models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Columns;
```

#### [Save Prediction Formula](#save-prediction-formula_4)[](#save-prediction-formula_4 "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the Prediction Formula to a new column in the data table. This option is available for all ARIMA and Smoothing models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Prediction Formula;
```

#### [Show Confidence Interval](#show-confidence-interval_4)[](#show-confidence-interval_4 "Click to copy url")

**Syntax:** obj \<\< Show Confidence Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Confidence Interval( 0 );
```

#### [Show Points](#show-points_6)[](#show-points_6 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides points on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Show Points( 1 ) );

(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Show Prediction Interval](#show-prediction-interval_4)[](#show-prediction-interval_4 "Click to copy url")

**Syntax:** obj \<\< Show Prediction Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Prediction Interval( 0 );
```

#### [Std Error of Predicted](#std-error-of-predicted_4)[](#std-error-of-predicted_4 "Click to copy url")

**Syntax:** obj \<\< Std Error of Predicted( state=0\|1 )

**Description:** Selects the Standard Error of Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Std Error of Predicted( 1 ), Save Columns );
```

#### [Time](#time_4)[](#time_4 "Click to copy url")

**Syntax:** obj \<\< Time( state=0\|1 )

**Description:** Selects the Time data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ), Time ID( :Date ) );
obj << Arima( 1, 0, 0, Time( 0 ), Save Columns );
```

#### [Upper Confidence Limit](#upper-confidence-limit_4)[](#upper-confidence-limit_4 "Click to copy url")

**Syntax:** obj \<\< Upper Confidence Limit( state=0\|1 )

**Description:** Selects the Upper 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Upper Confidence Limit( 1 ), Save Columns );
```

#### [Variogram](#variogram_6)[](#variogram_6 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Variogram( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

## [Seasonal Exponential Smoothing](#seasonal-exponential-smoothing_1)[](#seasonal-exponential-smoothing_1 "Click to copy url")

### [Item Messages](#item-messages_7)[](#item-messages_7 "Click to copy url")

#### [Actual](#actual_5)[](#actual_5 "Click to copy url")

**Syntax:** obj \<\< Actual( state=0\|1 )

**Description:** Selects the Actual data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Actual( 1 ), Save Columns );
```

#### [Autocorrelations](#autocorrelations_5)[](#autocorrelations_5 "Click to copy url")

**Syntax:** obj \<\< Autocorrelations( state=0\|1 )

**Description:** Displays or hides the autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Confidence Intervals](#confidence-intervals_5)[](#confidence-intervals_5 "Click to copy url")

**Syntax:** obj \<\< Confidence Intervals( number )

#### [Create SAS Job](#create-sas-job_5)[](#create-sas-job_5 "Click to copy url")

**Syntax:** obj \<\< Create SAS Job

**Description:** Creates a SAS Job to launch SAS and run the analysis in PROC ARIMA.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Create SAS Job;
```

#### [Innovations](#innovations_5)[](#innovations_5 "Click to copy url")

**Syntax:** obj \<\< Innovations( state=0\|1 )

**Description:** On by default.

**JMP Version Added:** 16

#### [Lower Confidence Limit](#lower-confidence-limit_5)[](#lower-confidence-limit_5 "Click to copy url")

**Syntax:** obj \<\< Lower Confidence Limit( state=0\|1 )

**Description:** Selects the Lower 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Lower Confidence Limit( 1 ), Save Columns );
```

#### [No Constrain](#no-constrain_5)[](#no-constrain_5 "Click to copy url")

**Syntax:** obj \<\< No Constrain( state=0\|1 )

**Description:** Lifts the constraint on the autoregressive parameters to always remain within the stable region and the moving average parameters within the invertible region when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Constrain( 1 ) );
```

#### [No Intercept](#no-intercept_5)[](#no-intercept_5 "Click to copy url")

**Syntax:** obj \<\< No Intercept( state=0\|1 )

**Description:** Sets the intercept to zero when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Intercept( 1 ) );
```

#### [Partial Autocorrelations](#partial-autocorrelations_5)[](#partial-autocorrelations_5 "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelations( state=0\|1 )

**Description:** Displays or hides the partial autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Partial Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Plot](#plot_5)[](#plot_5 "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Displays or hides the residual statistics plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Plot( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Predicted](#predicted_5)[](#predicted_5 "Click to copy url")

**Syntax:** obj \<\< Predicted( state=0\|1 )

**Description:** Selects the Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Predicted( 1 ), Save Columns );
```

#### [Prediction Interval](#prediction-interval_5)[](#prediction-interval_5 "Click to copy url")

**Syntax:** obj \<\< Prediction Interval( level )

**Description:** Sets the size of the confidence interval about the prediction for the ARIMA model. The default size is 0.95.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, Forecasting Interval( 0.99 ) );
```

#### [Remove Fit](#remove-fit_7)[](#remove-fit_7 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Residuals](#residuals_5)[](#residuals_5 "Click to copy url")

**Syntax:** obj \<\< Residuals( state=0\|1 )

**Description:** Selects the Residuals values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Residuals( 1 ), Save Columns );
```

#### [Save Columns](#save-columns_5)[](#save-columns_5 "Click to copy url")

**Syntax:** obj \<\< Save Columns

**Description:** Creates a new data table containing the actual and predicted values together with standard errors, residuals and 95% prediction intervals about the response. This option is available for all ARIMA, Smoothing, and Transfer Function models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Columns;
```

#### [Save Prediction Formula](#save-prediction-formula_5)[](#save-prediction-formula_5 "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the Prediction Formula to a new column in the data table. This option is available for all ARIMA and Smoothing models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Prediction Formula;
```

#### [Show Confidence Interval](#show-confidence-interval_5)[](#show-confidence-interval_5 "Click to copy url")

**Syntax:** obj \<\< Show Confidence Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Confidence Interval( 0 );
```

#### [Show Points](#show-points_7)[](#show-points_7 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides points on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Show Points( 1 ) );

(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Show Prediction Interval](#show-prediction-interval_5)[](#show-prediction-interval_5 "Click to copy url")

**Syntax:** obj \<\< Show Prediction Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Prediction Interval( 0 );
```

#### [Std Error of Predicted](#std-error-of-predicted_5)[](#std-error-of-predicted_5 "Click to copy url")

**Syntax:** obj \<\< Std Error of Predicted( state=0\|1 )

**Description:** Selects the Standard Error of Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Std Error of Predicted( 1 ), Save Columns );
```

#### [Time](#time_5)[](#time_5 "Click to copy url")

**Syntax:** obj \<\< Time( state=0\|1 )

**Description:** Selects the Time data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ), Time ID( :Date ) );
obj << Arima( 1, 0, 0, Time( 0 ), Save Columns );
```

#### [Upper Confidence Limit](#upper-confidence-limit_5)[](#upper-confidence-limit_5 "Click to copy url")

**Syntax:** obj \<\< Upper Confidence Limit( state=0\|1 )

**Description:** Selects the Upper 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Upper Confidence Limit( 1 ), Save Columns );
```

#### [Variogram](#variogram_7)[](#variogram_7 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Variogram( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

## [Simple Exponential Smoothing](#simple-exponential-smoothing_1)[](#simple-exponential-smoothing_1 "Click to copy url")

### [Item Messages](#item-messages_8)[](#item-messages_8 "Click to copy url")

#### [Actual](#actual_6)[](#actual_6 "Click to copy url")

**Syntax:** obj \<\< Actual( state=0\|1 )

**Description:** Selects the Actual data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Actual( 1 ), Save Columns );
```

#### [Autocorrelations](#autocorrelations_6)[](#autocorrelations_6 "Click to copy url")

**Syntax:** obj \<\< Autocorrelations( state=0\|1 )

**Description:** Displays or hides the autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Confidence Intervals](#confidence-intervals_6)[](#confidence-intervals_6 "Click to copy url")

**Syntax:** obj \<\< Confidence Intervals( number )

#### [Create SAS Job](#create-sas-job_6)[](#create-sas-job_6 "Click to copy url")

**Syntax:** obj \<\< Create SAS Job

**Description:** Creates a SAS Job to launch SAS and run the analysis in PROC ARIMA.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Create SAS Job;
```

#### [Innovations](#innovations_6)[](#innovations_6 "Click to copy url")

**Syntax:** obj \<\< Innovations( state=0\|1 )

**Description:** On by default.

**JMP Version Added:** 16

#### [Lower Confidence Limit](#lower-confidence-limit_6)[](#lower-confidence-limit_6 "Click to copy url")

**Syntax:** obj \<\< Lower Confidence Limit( state=0\|1 )

**Description:** Selects the Lower 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Lower Confidence Limit( 1 ), Save Columns );
```

#### [No Constrain](#no-constrain_6)[](#no-constrain_6 "Click to copy url")

**Syntax:** obj \<\< No Constrain( state=0\|1 )

**Description:** Lifts the constraint on the autoregressive parameters to always remain within the stable region and the moving average parameters within the invertible region when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Constrain( 1 ) );
```

#### [No Intercept](#no-intercept_6)[](#no-intercept_6 "Click to copy url")

**Syntax:** obj \<\< No Intercept( state=0\|1 )

**Description:** Sets the intercept to zero when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Intercept( 1 ) );
```

#### [Partial Autocorrelations](#partial-autocorrelations_6)[](#partial-autocorrelations_6 "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelations( state=0\|1 )

**Description:** Displays or hides the partial autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Partial Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Plot](#plot_6)[](#plot_6 "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Displays or hides the residual statistics plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Plot( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Predicted](#predicted_6)[](#predicted_6 "Click to copy url")

**Syntax:** obj \<\< Predicted( state=0\|1 )

**Description:** Selects the Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Predicted( 1 ), Save Columns );
```

#### [Prediction Interval](#prediction-interval_6)[](#prediction-interval_6 "Click to copy url")

**Syntax:** obj \<\< Prediction Interval( level )

**Description:** Sets the size of the confidence interval about the prediction for the ARIMA model. The default size is 0.95.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, Forecasting Interval( 0.99 ) );
```

#### [Remove Fit](#remove-fit_8)[](#remove-fit_8 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Residuals](#residuals_6)[](#residuals_6 "Click to copy url")

**Syntax:** obj \<\< Residuals( state=0\|1 )

**Description:** Selects the Residuals values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Residuals( 1 ), Save Columns );
```

#### [Save Columns](#save-columns_6)[](#save-columns_6 "Click to copy url")

**Syntax:** obj \<\< Save Columns

**Description:** Creates a new data table containing the actual and predicted values together with standard errors, residuals and 95% prediction intervals about the response. This option is available for all ARIMA, Smoothing, and Transfer Function models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Columns;
```

#### [Save Prediction Formula](#save-prediction-formula_6)[](#save-prediction-formula_6 "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the Prediction Formula to a new column in the data table. This option is available for all ARIMA and Smoothing models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Prediction Formula;
```

#### [Show Confidence Interval](#show-confidence-interval_6)[](#show-confidence-interval_6 "Click to copy url")

**Syntax:** obj \<\< Show Confidence Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Confidence Interval( 0 );
```

#### [Show Points](#show-points_8)[](#show-points_8 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides points on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Show Points( 1 ) );

(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Show Prediction Interval](#show-prediction-interval_6)[](#show-prediction-interval_6 "Click to copy url")

**Syntax:** obj \<\< Show Prediction Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Prediction Interval( 0 );
```

#### [Std Error of Predicted](#std-error-of-predicted_6)[](#std-error-of-predicted_6 "Click to copy url")

**Syntax:** obj \<\< Std Error of Predicted( state=0\|1 )

**Description:** Selects the Standard Error of Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Std Error of Predicted( 1 ), Save Columns );
```

#### [Time](#time_6)[](#time_6 "Click to copy url")

**Syntax:** obj \<\< Time( state=0\|1 )

**Description:** Selects the Time data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ), Time ID( :Date ) );
obj << Arima( 1, 0, 0, Time( 0 ), Save Columns );
```

#### [Upper Confidence Limit](#upper-confidence-limit_6)[](#upper-confidence-limit_6 "Click to copy url")

**Syntax:** obj \<\< Upper Confidence Limit( state=0\|1 )

**Description:** Selects the Upper 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Upper Confidence Limit( 1 ), Save Columns );
```

#### [Variogram](#variogram_8)[](#variogram_8 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Variogram( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

## [Simple Moving Average](#simple-moving-average_1)[](#simple-moving-average_1 "Click to copy url")

### [Item Messages](#item-messages_9)[](#item-messages_9 "Click to copy url")

#### [Add Model](#add-model)[](#add-model "Click to copy url")

**Syntax:** obj \<\< Add Model( Window Width, \<Centered\> )

**Description:** Add a simple moving average model. Model is identified by moving window width. The optional argument indicates whether the average is centered.

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
obj = Time Series( Y( :Close ), Simple Moving Average( Add Model( 5 ) ) );
sma = obj << Simple Moving Average( Add Model( 10 ) );
sma << Add Model( 15, Centered );
```

#### [Connecting Lines](#connecting-lines_2)[](#connecting-lines_2 "Click to copy url")

**Syntax:** obj \<\< Connecting Lines( \<1\|0\> )

**Description:** Graph option for displaying connected lines.

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
obj = Time Series( Y( :Close ), Simple Moving Average( Add Model( 5 ) ) );
sma = obj << Simple Moving Average( Connecting Lines );
```

#### [Get Results](#get-results)[](#get-results "Click to copy url")

**Syntax:** obj \<\< Get Results

**Description:** Return all simple moving average models as a JSL object.

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
obj = Time Series( Y( :Close ), Simple Moving Average( Add Model( 5 ) ) );
resultobj = obj << Simple Moving Average( Get Result );
```

#### [Remove Model](#remove-model)[](#remove-model "Click to copy url")

**Syntax:** obj \<\< Remove Model( Window Width, \<Centered\> )

**Description:** Remove a simple moving average model. Model is identified by moving window width.

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
obj = Time Series( Y( :Close ), Simple Moving Average( Add Model( 5 ) ) );
obj << Simple Moving Average( Remove Model( 5 ) );
```

#### [Remove Report](#remove-report)[](#remove-report "Click to copy url")

**Syntax:** obj \<\< Remove Report

**JMP Version Added:** 16

#### [Save to Data Table](#save-to-data-table)[](#save-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save to Data Table

**Description:** Save all simple moving average models to a data table, and return the data table handle

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
obj = Time Series( Y( :Close ), Simple Moving Average( Add Model( 5 ) ) );
resultdt = obj << Simple Moving Average( Save to Data Table );
```

#### [Show Points](#show-points_9)[](#show-points_9 "Click to copy url")

**Syntax:** obj \<\< Show Points( \<1\|0\> )

**Description:** Graph option for displaying points.

``` jsl
dt = Open( "$SAMPLE_DATA/Stock Prices.jmp" );
obj = Time Series( Y( :Close ), Simple Moving Average( Add Model( 5 ) ) );
sma = obj << Simple Moving Average( Show Points( 0 ) );
```

## [Transfer Function Model](#transfer-function-model)[](#transfer-function-model "Click to copy url")

### [Item Messages](#item-messages_10)[](#item-messages_10 "Click to copy url")

#### [Alternative Parameterization](#alternative-parameterization)[](#alternative-parameterization "Click to copy url")

**Syntax:** obj \<\< Alternative Parameterization( state=0\|1 )

**Description:** Specifies whether the general regression coefficient is factored out of the numerator polynomials.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) )
);
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Alternative Parameterization( 1 )
);
```

#### [Autocorrelations](#autocorrelations_7)[](#autocorrelations_7 "Click to copy url")

**Syntax:** obj \<\< Autocorrelations( state=0\|1 )

**Description:** Displays or hides the autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Autocorrelations( 1 )
);
(obj << report)["Residuals"] << Close( 0 );
```

#### [Compute Objective](#compute-objective)[](#compute-objective "Click to copy url")

**Syntax:** obj \<\< Compute Objective

#### [Create SAS Job](#create-sas-job_7)[](#create-sas-job_7 "Click to copy url")

**Syntax:** obj \<\< Create SAS Job

**Description:** Creates a SAS Job to launch SAS and run the analysis in PROC ARIMA.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Create SAS Job
);
```

#### [Import New Inputs](#import-new-inputs)[](#import-new-inputs "Click to copy url")

**Syntax:** obj \<\< Import New Inputs

**JMP Version Added:** 16

#### [Maximum Iterations](#maximum-iterations_1)[](#maximum-iterations_1 "Click to copy url")

**Syntax:** obj \<\< Maximum Iterations( number )

**Description:** Specifies the maximum number of iterations.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) )
);
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Maximum Iterations( 10 )
);
```

#### [No Constrain](#no-constrain_7)[](#no-constrain_7 "Click to copy url")

**Syntax:** obj \<\< No Constrain( state=0\|1 )

**Description:** Removes the constraints on the AR and MA coefficients.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) )
);
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    No Constrain( 1 )
);
```

#### [No Intercept](#no-intercept_7)[](#no-intercept_7 "Click to copy url")

**Syntax:** obj \<\< No Intercept( state=0\|1 )

**Description:** Sets the Intercept to zero.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) )
);
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    No Intercept( 1 )
);
```

#### [Number of Forecast Periods](#number-of-forecast-periods_1)[](#number-of-forecast-periods_1 "Click to copy url")

**Syntax:** obj \<\< Number of Forecast Periods( number )

**Description:** Specifies the number of periods for forecasting.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) )
);
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Number of Forecast Periods( 10 )
);
```

#### [Partial Autocorrelations](#partial-autocorrelations_7)[](#partial-autocorrelations_7 "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelations( state=0\|1 )

**Description:** Displays or hides the partial autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Partial Autocorrelations( 1 )
);
(obj << report)["Residuals"] << Close( 0 );
```

#### [Plot](#plot_7)[](#plot_7 "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Displays or hides the residual statistics plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Plot( 1 )
);
(obj << report)["Residuals"] << Close( 0 );
```

#### [Prediction Interval](#prediction-interval_7)[](#prediction-interval_7 "Click to copy url")

**Syntax:** obj \<\< Prediction Interval( number )

**Description:** Sets the level of the confidence intervals displayed.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) )
);
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    :Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Confidence Intervals( 0.99 )
);
```

#### [Remove Fit](#remove-fit_9)[](#remove-fit_9 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Save Columns](#save-columns_7)[](#save-columns_7 "Click to copy url")

**Syntax:** obj \<\< Save Columns

**Description:** Creates a new data table containing the actual and predicted values together with standard errors, residuals and 95% prediction intervals about the response. This option is available for all ARIMA, Smoothing, and Transfer Function models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Save Columns
);
```

#### [Variogram](#variogram_9)[](#variogram_9 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/SeriesJ.jmp" );
obj = Time Series( Y( :Output CO2 ), Input List( :Input Gas Rate ) );
obj << Transfer Function(
    Order( 2, 0, 0 ),
    Seasonal( 0, 0, 0, 0 ),
    Input Gas Rate( Order( 2, 0, 2 ), Seasonal( 0, 0, 0, 0 ), Lag( 3 ) ),
    Variogram( 1 )
);
(obj << report)["Residuals"] << Close( 0 );
```

## [Winters Method (Additive)](#winters-method-additive)[](#winters-method-additive "Click to copy url")

### [Item Messages](#item-messages_11)[](#item-messages_11 "Click to copy url")

#### [Actual](#actual_7)[](#actual_7 "Click to copy url")

**Syntax:** obj \<\< Actual( state=0\|1 )

**Description:** Selects the Actual data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Actual( 1 ), Save Columns );
```

#### [Autocorrelations](#autocorrelations_8)[](#autocorrelations_8 "Click to copy url")

**Syntax:** obj \<\< Autocorrelations( state=0\|1 )

**Description:** Displays or hides the autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Confidence Intervals](#confidence-intervals_7)[](#confidence-intervals_7 "Click to copy url")

**Syntax:** obj \<\< Confidence Intervals( number )

#### [Create SAS Job](#create-sas-job_8)[](#create-sas-job_8 "Click to copy url")

**Syntax:** obj \<\< Create SAS Job

**Description:** Creates a SAS Job to launch SAS and run the analysis in PROC ARIMA.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Create SAS Job;
```

#### [Innovations](#innovations_7)[](#innovations_7 "Click to copy url")

**Syntax:** obj \<\< Innovations( state=0\|1 )

**Description:** On by default.

**JMP Version Added:** 16

#### [Lower Confidence Limit](#lower-confidence-limit_7)[](#lower-confidence-limit_7 "Click to copy url")

**Syntax:** obj \<\< Lower Confidence Limit( state=0\|1 )

**Description:** Selects the Lower 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Lower Confidence Limit( 1 ), Save Columns );
```

#### [No Constrain](#no-constrain_8)[](#no-constrain_8 "Click to copy url")

**Syntax:** obj \<\< No Constrain( state=0\|1 )

**Description:** Lifts the constraint on the autoregressive parameters to always remain within the stable region and the moving average parameters within the invertible region when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Constrain( 1 ) );
```

#### [No Intercept](#no-intercept_8)[](#no-intercept_8 "Click to copy url")

**Syntax:** obj \<\< No Intercept( state=0\|1 )

**Description:** Sets the intercept to zero when launching an ARIMA model.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, No Intercept( 1 ) );
```

#### [Partial Autocorrelations](#partial-autocorrelations_8)[](#partial-autocorrelations_8 "Click to copy url")

**Syntax:** obj \<\< Partial Autocorrelations( state=0\|1 )

**Description:** Displays or hides the partial autocorrelations plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Partial Autocorrelations( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Plot](#plot_8)[](#plot_8 "Click to copy url")

**Syntax:** obj \<\< Plot( state=0\|1 )

**Description:** Displays or hides the residual statistics plot. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Plot( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Predicted](#predicted_7)[](#predicted_7 "Click to copy url")

**Syntax:** obj \<\< Predicted( state=0\|1 )

**Description:** Selects the Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Predicted( 1 ), Save Columns );
```

#### [Prediction Interval](#prediction-interval_8)[](#prediction-interval_8 "Click to copy url")

**Syntax:** obj \<\< Prediction Interval( level )

**Description:** Sets the size of the confidence interval about the prediction for the ARIMA model. The default size is 0.95.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 1, 0, Forecasting Interval( 0.99 ) );
```

#### [Remove Fit](#remove-fit_10)[](#remove-fit_10 "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 16

#### [Residuals](#residuals_7)[](#residuals_7 "Click to copy url")

**Syntax:** obj \<\< Residuals( state=0\|1 )

**Description:** Selects the Residuals values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Residuals( 1 ), Save Columns );
```

#### [Save Columns](#save-columns_8)[](#save-columns_8 "Click to copy url")

**Syntax:** obj \<\< Save Columns

**Description:** Creates a new data table containing the actual and predicted values together with standard errors, residuals and 95% prediction intervals about the response. This option is available for all ARIMA, Smoothing, and Transfer Function models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Columns;
```

#### [Save Prediction Formula](#save-prediction-formula_7)[](#save-prediction-formula_7 "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formula

**Description:** Saves the Prediction Formula to a new column in the data table. This option is available for all ARIMA and Smoothing models.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Arima( 1, 0, 0 );
obj2 << Save Prediction Formula;
```

#### [Show Confidence Interval](#show-confidence-interval_7)[](#show-confidence-interval_7 "Click to copy url")

**Syntax:** obj \<\< Show Confidence Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Confidence Interval( 0 );
```

#### [Show Points](#show-points_10)[](#show-points_10 "Click to copy url")

**Syntax:** obj \<\< Show Points( state=0\|1 )

**Description:** Shows or hides points on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Show Points( 1 ) );

(obj << report)["Model Comparison"] << Close( 1 );
```

#### [Show Prediction Interval](#show-prediction-interval_7)[](#show-prediction-interval_7 "Click to copy url")

**Syntax:** obj \<\< Show Prediction Interval( state=0\|1 )

**Description:** Shows or hides prediction intervals on the Time Series Forecast Plot. This option is available for all ARIMA and Smoothing models. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj2 = obj << Simple Exponential Smoothing( Zero to One );
obj2 << Show Prediction Interval( 0 );
```

#### [Std Error of Predicted](#std-error-of-predicted_7)[](#std-error-of-predicted_7 "Click to copy url")

**Syntax:** obj \<\< Std Error of Predicted( state=0\|1 )

**Description:** Selects the Standard Error of Predicted values data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Std Error of Predicted( 1 ), Save Columns );
```

#### [Time](#time_7)[](#time_7 "Click to copy url")

**Syntax:** obj \<\< Time( state=0\|1 )

**Description:** Selects the Time data column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ), Time ID( :Date ) );
obj << Arima( 1, 0, 0, Time( 0 ), Save Columns );
```

#### [Upper Confidence Limit](#upper-confidence-limit_7)[](#upper-confidence-limit_7 "Click to copy url")

**Syntax:** obj \<\< Upper Confidence Limit( state=0\|1 )

**Description:** Selects the Upper 95% Confidence Limit values column for saving with the Save Columns command. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series( Y( :Steel Shipments ) );
obj << Arima( 1, 0, 0, Upper Confidence Limit( 1 ), Save Columns );
```

#### [Variogram](#variogram_10)[](#variogram_10 "Click to copy url")

**Syntax:** obj \<\< Variogram( state=0\|1 )

**Description:** Displays or hides the Variogram.

``` jsl
dt = Open( "$SAMPLE_DATA/Time Series/Steel Shipments.jmp" );
obj = Time Series(
    Y( :Steel Shipments ),
    Winters Method(
        12,
        Custom( Level( Bounded( 0, 1 ) ), Trend( Bounded( 0, 1 ) ) ),
        Variogram( 1 )
    )
);
(obj << report)["Residuals"] << Close( 0 );
(obj << report)["Model Comparison"] << Close( 1 );
```

[ Previous](Time%20Series%20Forecast.html "Time Series Forecast") [Next ](Titled%20List%20Box.html "Titled List Box")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
