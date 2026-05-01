# Statistical Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 311-326).

## Index (line numbers in this file)

- `<< Color or Mark by Column` — L125
- `<< Graph Builder` — L126
- `<< New Column` — L525
- `ARIMA Forecast()` — L149
- `After()` — L347
- `Arc Finder()` — L107
- `Before()` — L344
- `Best Partition()` — L168
- `ByVar()` — L434
- `Col Cumulative Sum()` — L179
- `Col Max()` — L202
- `Col Maximum()` — L201
- `Col Mean()` — L224
- `Col Median()` — L251
- `Col Min()` — L276
- `Col Minimum()` — L275
- `Col Mode()` — L304
- `Col Moving Average()` — L328
- `Col N Missing()` — L367
- `Col Number()` — L395
- `Col Quantile()` — L419
- `Col Rank()` — L454
- `Col Simple Exponential Smoothing()` — L487
- `Col Standardize()` — L504
- `Col Std Dev()` — L540
- `Col Sum()` — L564
- `Cumulative Sum()` — L181
- `Distribution()` — L607
- `Elements()` — L130
- `Excluded()` — L196
- `Fit Censored()` — L595
- `Fit Circle()` — L633
- `Formula()` — L530
- `Freq()` — L818
- `Group()` — L114
- `Hier Clust()` — L649
- `HoldParm()` — L618
- `IRT Ability()` — L657
- `KDE()` — L667
- `LenthPSE()` — L690
- `Max Number Arcs()` — L123
- `Max Radius Error()` — L120
- `Max Radius()` — L119
- `Max()` — L697
- `Maximum()` — L699
- `Mean()` — L706
- `Median()` — L714
- `Min Arc Points()` — L121
- `Min Distance()` — L117
- `Min Radius()` — L118
- `Min()` — L719
- `Minimum()` — L721
- `Moving Average()` — L329
- `N Missing()` — L728
- `Normal Tolerance Factor()` — L732
- `Number()` — L738
- `Product()` — L742
- `Quantile()` — L753
- `Range()` — L759
- `Robust PCA()` — L764
- `SSQ()` — L796
- `Size()` — L127
- `Std Dev()` — L784
- `Stored Value()` — L220
- `Sum()` — L568
- `Summarize YByX()` — L817
- `Summarize()` — L801
- `Summation()` — L834
- `Variables()` — L128
- `Weight()` — L615
- `Weighting()` — L339
- `X()` — L115
- `Y()` — L116
- `YHigh()` — L612
- `YLow()` — L608
- `Z()` — L617
---

JSL Functions, Operators, and Messages
Statistical Functions

311

memory until they are explicitly closed, reducing the amount of memory that is
available to JMP. To explicitly close the hidden data table, call Close(dt), where dt is
the data table reference.
scalar (Optional) Indicates that the query returns a single value.
sqlStatement Required. The SQL statement, most likely a SELECT statement. The
statement must be the last argument.
Example

The following example selects all data for students who are older than 14 years of age.
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
result = Query( Table( dt, "t1" ), "SELECT * FROM t1 WHERE age > 14;" );

See Also

“SQL Functions Available for JMP Queries”

Statistical Functions
Arc Finder(X(col), Y(col), Group(lot, wafer))
Description

Finds arcs in the point data and creates a new column that identifies the arcs.
Example
dt = Open( "$SAMPLE_DATA/Wafer Stacked.jmp" );
Arc Finder(
Group( :Lot, :Wafer ),
X( :X_Die ),
Y( :Y_Die ),
Min Distance( 12 ), // minimum distance among 3 points to seed an arc
Min Radius( 15 ), // minimum radius of the acceptable arc
Max Radius( 2000 ), // maximum radius of acceptable arc
Max Radius Error( 2 ), // how close a point needs to be added
Min Arc Points( 5 ), // how many points to define an arc
Number of Searches( 500 ), // how many random probes of data
Max Number Arcs( 3 ) // number of arcs searched for
);
dt << Color or Mark by Column( :Arc Number );
dt << Graph Builder(
Size( 1539, 921 ),
Variables( X( :X_Die ), Y( :Y_Die ), Wrap( :Lot_Wafer Label ), Color( :Arc
Number ) ),
Elements( Points( X, Y, Legend( 6 ) ) )
);

Statistical Functions

Notes

•

The function is scaled for data that have a range of 30 to 50 units.

•

The function is suitable only for data that are subset to the interesting defect points.

•

It is not suitable when the density of points is high.

ARIMA Forecast(column, length, model, estimates, from, to)
Description

Determines the forecasted values for the specified rows of the specified column using the
specified model and estimates.
Returns

A vector of forecasted values for column within the range defined by from and to.
Arguments
column A data table column.
length Number of rows within the column to use.
model Messages for Time Series model options.
estimates A list of named values that matches the messages sent to ARIMA Forecast().

If you perform an ARIMA Forecast and save the script, the estimates are part of the
script.
from, to Define the range of values. Typically, from is between 1 and to, inclusive. If
from is less than or equal to 0, and if from is less than or equal to to, the results include
filtered predictions.
Best Partition(xindices, yindices, <<Ordered, <<Continuous Y,
<<Continuous X)
Description

Experimental function to determine the optimal grouping.
Returns

A list.
Arguments
xindices, yindices Same-dimension matrices.

Col Cumulative Sum(name, <By var, <Excluded(Row State())>, ...>,
<<Freq(freqCol))
Cumulative Sum(name)
Description

Returns the cumulative sum for the current row. Col Cumulative Sum supports By
columns, which do not need to be sorted.

JSL Functions, Operators, and Messages
Statistical Functions

313

Arguments
name A column name.
By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
<<Freq(freqCol) (Optional) Specifies the column that contains the frequency of
occurrences for each value, which is used to weight the values in the calculation.
Col Maximum(name, <By var, <Excluded(Row State())>, ...>)
Col Max(name)
Description

Calculates the maximum value across all rows of the specified column. The result is
internally cached to speed up multiple evaluations.
Returns

The maximum value that appears in the column.
Arguments
name A column name.
By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Mean(name, <By var, <Excluded(Row State())>, ...>, <<Freq(freqCol))
Description

Calculates the mean across all rows of the specified column. The result is internally cached
to speed up multiple evaluations.
Returns

The mean of the column.
Argument
name A column name.
By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.

Statistical Functions

Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
<<Freq(freqCol) (Optional) Specifies the column that contains the frequency of
occurrences for each value, which is used to weight the values in the calculation.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Median(name, <By var, <Excluded(Row State())>, ...>, <<Freq(freqCol))
Description

Calculates the median across all rows of the specified column. The ordering is cached
internally to speed up multiple evaluations.
Returns

The median of the column.
Argument
name A column name.
By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
<<Freq(freqCol) (Optional) Specifies the column that contains the frequency of
occurrences for each value, which is used to weight the values in the calculation.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Minimum(name, <By var, <Excluded(Row State())>, ...>)
Col Min(name)
Description

Calculates the minimum value across all rows of the specified column. The result is
internally cached to speed up multiple evaluations.
Returns

The minimum value that appears in the column.

JSL Functions, Operators, and Messages
Statistical Functions

315

Argument
name A column name.
By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Mode(name, <By var, <Excluded(Row State())>, ...>, <<Freq(freqCol))
Description

Calculates the mode across all rows of the specified column. The ordering is cached
internally to speed up multiple evaluations.
Returns

The mode of the column.
Argument
name A column name.
By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
<<Freq(freqCol) (Optional) Specifies the column that contains the frequency of
occurrences for each value, which is used to weight the values in the calculation.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Moving Average(name, options, <By var, <Excluded(Row State())>, ...>)
Moving Average(name, options)
Description

Returns the moving average over a given interval based at the current row. Col Moving
Average supports By columns.

Statistical Functions

Arguments
name A column name.
Weighting(1|0|n) Required positional argument. Determines how the values are

weighted. 1 indicates uniform weighting. 0 indicates incremental weighting (a ramp or
triangle). Any other number is the parameter for an exponential moving average
(EWMA or EMA).
Before(1|0|n) Positional argument. Controls the size of the range (or window) by
including the specified number of items before the current item in the average (in
addition to the current item). The default value, -1, means all of the preceding items.
After(1|0|n) Positional argument. Controls the size of the range (or window) by
including the specified number of items after the current item in the average (in
addition to the current item). The default value, 0, means no following items.
Partial Window is Missing Boolean positional argument. Controls how missing
values are treated. By default, missing values are ignored. 0 computes the average of
partial windows.
By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the
calculation.
Examples
// equal weighting of a five-item lagging range
Col Moving Average( x, 1, 4 );
// ramp weighting of all preceding items
Col Moving Average( x, 0 );
// triangle weighting of a five-item centered range
Col Moving Average( x, 0, 2, 2 );
// exponential weighting of all preceding items
Col Moving Average( x, 0.25 );

Col N Missing(name, <By var, <Excluded(Row State())>, ...>)
Description

Calculates the number of missing values across all rows of the specified column. The
result is internally cached to speed up multiple evaluations.
Returns

The number of missing values in the column.
Argument
name A column name.

JSL Functions, Operators, and Messages
Statistical Functions

317

By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Number(name, <By var, <Excluded(Row State())>, ...>, <<Freq(freqCol))
Description

Calculates the number of nonmissing values across all rows of the specified column. The
result is internally cached to speed up multiple evaluations.
Returns

The number of nonmissing values in the column.
Argument
name A column name.
By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
<<Freq(freqCol) (Optional) Specifies the column that contains the frequency of
occurrences for each value, which is used to weight the values in the calculation.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Quantile(name, p, <ByVar, <Excluded(Row State())>, ...>,
<<Freq(freqCol))
Description

Calculates the specified quantile p across all rows of the specified column. The result is
internally cached to speed up multiple evaluations.
Returns

The value of the quantile.

Statistical Functions

Argument
name A column name.
p A specified quantile p between 0 and 1.
ByVar (Optional) A By group.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
<<Freq(freqCol) (Optional) Specifies the column that contains the frequency of

occurrences for each value, which is used to weight the values in the calculation.
Example
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Col Quantile( :height, .5 );
63

63 is the 50th percentile, or the median, of all rows in the height column.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Rank(column, <ByVar, <Excluded(Row State())>, ...>,
<<tie("average"|"arbitrary"|"row"|"minimum"))
Description

Ranks each row’s value, from 1 for the lowest value to the number of columns for the
highest value. Ties are broken arbitrarily by default.
Arguments
column The column to be ranked.
ByVar (Optional) A By variable to compute statistics across groups of rows.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
<<tie Determines how the tie is broken. A tie occurs when the values being ranked are
the same. For the data [33 55 77 55], 33 has rank 1 and 77 has rank 4, and the
question is how to assign ranking for the 55s. average reports the average of the
possible rankings, 2.5, for both 55s. arbitrary matches JMP 12 behavior by assigning
the possible rankings in an unspecified order, which could be 2 and 3 or 3 and 2. row
assigns the ranks in the order that they originally appear. (The first 55 would be 2 and
the second 55 would be 3.)
minimum gives both values the lowest possible rank, 2.

JSL Functions, Operators, and Messages
Statistical Functions

319

Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Simple Exponential Smoothing(column, alpha, <ByVar> )
Description

Returns the simple exponential smoothing prediction for the current row using smoothing
weight alpha.
Arguments
column The column of time series observations.
alpha The smoothing weight.
ByVar (Optional) A By variable to compute predictions across groups of rows. By

variables do not need to be presorted.
Notes

The predicted value for row t is given by the following:
Predicted[t] = alpha * Observed[t-1] + (1-alpha) * Predicted[t-1]

By definition, Predicted[1] = Observed[1].
Col Standardize(name,<By var, <Excluded(Row State())>, ...>)
Description

Calculates the column mean divided by the standard deviation across all rows of the
specified column.
Returns

The standardized mean.
Argument
name A column name.
By var (Optional) A By variable to compute statistics across groups of rows. If a By

variable is specified, the values are standardized against the mean and standard
deviation of their corresponding By variable group.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the
calculation.
Notes

Standardizing centers the variable by its sample standard deviation. Thus, the following
commands are equivalent:
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "stdht", Formula( Col Standardize( height ) ) );

Statistical Functions

dt << New Column( "stdht2",
Formula( (height - Col Mean( height )) / Col Std Dev( height ) )
);

Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Std Dev(name,<By var, <Excluded(Row State())>, ...>, <<Freq(freqCol))
Description

Calculates the standard deviation across rows in a column. The result is internally cached
to speed up multiple evaluations.
Returns

The standard deviation.
Argument
name A column name.
By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
<<Freq(freqCol) (Optional) Specifies the column that contains the frequency of
occurrences for each value, which is used to weight the values in the calculation.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Col Sum(name,<By var, <Excluded(Row State())>, ...>, <<Freq(freqCol))
Description

Calculates the sum across rows in a column. Calculating all missing values (Col
Sum(.,.)) returns missing. The result is internally cached to speed up multiple
evaluations.
Returns

The sum.
Argument
name A column name.

JSL Functions, Operators, and Messages
Statistical Functions

321

By var (Optional) A By variable to compute statistics across groups of rows. Use the By
variable in a column formula or in a For Each Row() function.
Excluded(Row State()) (Optional) Ensures excluded rows are not used in the

calculation.
<<Freq(freqCol) (Optional) Specifies the column that contains the frequency of
occurrences for each value, which is used to weight the values in the calculation.
Notes

If a data value is assigned by a column property (such as Missing Value Codes), use Col
Stored Value() to base the calculation on the value stored in the column instead.
See Also

“Col Stored Value(<dt>, col, <row>)”
Fit Censored(Distribution("name"), YLow(vector) | Y(Vector),
<YHigh(vector)>, <Weight(vector)>, <X(matrix)>, <Z(matrix)>,
<HoldParm(vector)>, <Use random sample to compute initial values(percent)>,
<Use first N observations to compute initial values(nobs)>)
Description

Fits a distribution using censored data.
Returns

A list that contains parameter estimates, the covariance matrix, the log-likelihood, the
AICc, the BIC, and a convergence message. See Fitting Linear Models.
Arguments
Distribution("name") The quoted name of the distribution to fit.
YLow(vector) | Y(Vector) If you do not have censoring, then use Y and an array of
your data, and do not specify YHigh. If you do have censoring, then specify YLow and
YHigh as the lower and upper censoring values, respectively.
Optional Arguments
YHigh(vector) A vector that contains the upper censoring values. Specify this only if

you have censoring and also specify YLow.
Weight(vector) A vector that contains the weight values.
X(matrix) The regression design matrix for location.
Z(matrix) The regression design matrix for scale.
HoldParm(vector) An array of specified parameters. The parameters should be

nonmissing where they are to be held fixed, and missing where the are to be estimated.
This is primarily used to test hypotheses that certain parameters are zero or some other
specific value.
Use random sample to compute initial values(percent) A percent of the
observations to be used in the computation of the initial values. Specify this if the data
vector is large.

Statistical Functions

Use first N observations to compute initial values(nobs) A number of

observations at the start of the data vector to be used in the computation of the initial
values. Specify this if the data vector is large.
Fit Circle(Xvec, Yvec)
Description

Fits a circle that best goes through three or more points using a least squares approach. If
only three points are specified, a direct solution can be found, and the sum of squared
errors is zero.
Returns

A list that contains the X and Y coordinates of the center point of the circle, the length of
the radius, and the sum of squared errors.
Arguments
Xvec Vector of X coordinates of three or more points.
Yvec Vector of Y coordinates of three or more points.
Syntax
{Xcenter, yCenter, radius, SSE} = Fit Circle(Xvec, Yvec)

Hier Clust(x)
Description

Returns the clustering history for a hierarchical clustering using Ward’s method (without
standardizing data).
Argument
x A data matrix.

IRT Ability(Q1, <Q2, Q3, ... Qn,> parmMatrix)
Description

Returns scores for the latent variable in an item response theory model with n binary items
and a matrix of known parameters. The parameter matrix should contain as many rows as
there are parameters in the model and as many columns as there are items in the analysis.
Arguments
Q1, Q2, ..., Qn A set of n binary items.
parmMatrix A matrix of parameters from an item response theory model.

KDE(vector, <named arguments>)
Description

Returns a kernel density estimator with automatic bandwidth selection.

JSL Functions, Operators, and Messages
Statistical Functions

323

Argument
vector A vector.
Optional Named Arguments
<<weights Must be a vector of the same length as vector, and can contain any
nonnegative real numbers. Weights represents frequencies, counts, or similar concepts.
<<bandwidth(n) A nonnegative real number. Enter a value of 0 to use the bandwidth

selection argument.
<<bandwidth scale(n) A positive real number.
<<bandwidth selection(n) n must be 0, 1, 2, or 3, corresponding to Sheather and Jones,
Normal Reference, Silverman rule of thumb, or Oversmoother, respectively.
<<kernel(n) n must be 0, 1, 2, 3, or 4, corresponding to Gaussian, Epanechnikov,
Biweight, Triangular, or Rectangular, respectively.
LenthPSE(x)
Description

Returns Lenth’s pseudo-standard error of the values within a vector.
Argument
x A vector.

Max()
See “Maximum(var1, var2, ...)”.
Maximum(var1, var2, ...)
Max(var1, var2, ...)
Description

Returns the maximum value of the arguments or of the values within a single matrix or list
argument. If multiple arguments are specified, they must be all numeric values or all
quoted strings.
Mean(var1, var2, ...)
Description

Returns the arithmetic mean of the arguments or of the values within a single matrix or list
argument.

Statistical Functions

Median(var1, var2, ...)
Description

Returns the median of the arguments or of the values within a single matrix or list
argument.
Min()
See “Minimum(var1, var2, ...)”.
Minimum(var1, var2, ...)
Min(var1, var2, ...)
Description

Returns the minimum value of the arguments or of the values within a single matrix
argument. If multiple arguments are specified, they must be either all numeric values or
all quoted strings.
N Missing(expression)
Description

Rowwise number of missing values in variables specified.
Normal Tolerance Factor(1-alpha, p, n, <One Sided>)
Description

Constructs the tolerance factor that is used to construct a 1-alpha confidence interval to
contain proportion p of the means with sample size n from the normal distribution. The
optional argument enables you to request the factor for a one-sided tolerance interval.
Number(var1, var2, ...)
Description

Rowwise number of nonmissing values in variables specified.
Product(i=initialValue, limitValue, bodyExpr)
Description

Multiplies the results of bodyExpr over all i until the limitValue and returns a single
product.

JSL Functions, Operators, and Messages
Statistical Functions

325

Quantile(p, arguments)
Description

Returns the pth quantile of the arguments. The first argument can be a scalar or a matrix of
values between 0 and 1. The remaining arguments can also be specified as values within a
single matrix or list argument. See Basic Analysis.
Range(var1, var2, ...)
Description

Returns the minimum and maximum values of the arguments. The result is returned as a
two-element row vector that contains the minimum and the maximum.
Robust PCA(X, <Lambda(2/sqrt(max(nrow, ncol)))>, <tolerance=1e-10>,
<maxit(75)>, <Center(1)>, <Scale(1)>)
Description

Performs a sequence of singular value decompositions and thresholding steps to
decompose the data matrix into a low-rank matrix and a sparse matrix of residuals.
Returns
A The low-rank matrix estimation.
E The sparse matrix of residuals.
S A vector of singular values.
Arguments
X A data matrix.
Lambda Specifies a value greater than 0 that determines the sparsity of the matrix of

residuals. For larger values of Lambda, the matrix of residuals is more sparse.
tolerance The convergence criterion.
maxit The maximum number of SVD iterations.
Center Centers the data prior to performing the SVD iterations.
Scale Scales the data prior to performing the SVD iterations

Std Dev(var1, var2, ...)
Description

Rowwise standard deviation of the variables specified.
Sum(var1, var2, ...)
Description

Rowwise sum of the variables specified. Calculating all missing values (Sum(.,.))returns
missing.

Statistical Functions

SSQ(x1, ...)
Description

Returns the sum of squares of all elements. Takes numbers, matrices, or lists as arguments
and returns a scalar number. Skips missing values.
Summarize(<dt>, <by>, <count>, <sum>, <mean>, <min>, <max>, <stddev>,
<corr>, <quantile>, <first>)
Description

Gathers summary statistics for a data table and stores them in global variables.
Returns

None.
Arguments
dt Optional positional argument: a reference to a data table. If this argument is not in the

form of an assignment, then it is considered a data table expression.
All other arguments are optional and can be included in any order. Typically, each
argument is assigned to a variable so you can display or manipulate the values further.
name=By(col | list | Eval) Using a BY variable changes the output from single
values for each statistic to a list of values for each group in the BY variable.
Summarize YByX(X(<x columns>, Y (<y columns>), Group(<grouping columns>),
Freq(<freq column>), Weight(<weight column>))
Description

Calculates all Fit Y by X combinations on large-scale data sets.
Returns

A data table of p-values and logworth values for each Y and X combination.
Arguments
X(col) The factor columns used in the fit model.
Y(col) The response columns used in the fit model.
Group(gcol) The group of columns used in the fit model.
Freq(col) The frequency (for each row) column used in the fit model.
Weight(col) The importance (or influence) column used in the fit model.
Notes

Performs the same function as the Response Screening platform.
Summation(init, limitvalue, body)
Description

Summation sums the results of the body statement(s) over all i to return a single value.
