# Probability Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 223-253).

## Index (line numbers in this file)

- `Beta Density()` — L135
- `Beta Distribution()` — L156
- `Beta Quantile()` — L167
- `Cauchy Density()` — L178
- `Cauchy Distribution()` — L199
- `Cauchy Quantile()` — L214
- `ChiSquare Density()` — L234
- `ChiSquare Distribution()` — L258
- `ChiSquare Log CDistribution()` — L279
- `ChiSquare Log Density()` — L285
- `ChiSquare Log Distribution()` — L290
- `ChiSquare Noncentrality()` — L295
- `ChiSquare Quantile()` — L311
- `Dunnett P Value()` — L321
- `Dunnett Quantile()` — L332
- `ExGaussian Density()` — L346
- `ExGaussian Distribution()` — L367
- `ExGaussian Quantile()` — L380
- `Exp Density()` — L398
- `Exp Distribution()` — L411
- `Exp Quantile()` — L422
- `Exponential Density()` — L399
- `Exponential Distribution()` — L412
- `Exponential Quantile()` — L423
- `F Density()` — L440
- `F Distribution()` — L485
- `F Log CDistribution()` — L491
- `F Log Density()` — L503
- `F Log Distribution()` — L509
- `F Noncentrality()` — L515
- `F Power()` — L523
- `F Quantile()` — L565
- `F Sample Size()` — L570
- `FDR Adjust()` — L610
- `Frechet Density()` — L623
- `Frechet Distribution()` — L641
- `Frechet Quantile()` — L656
- `GLog Density()` — L799
- `GLog Distribution()` — L828
- `GLog Quantile()` — L849
- `Gamma Density()` — L674
- `Gamma Distribution()` — L688
- `Gamma Log CDistribution()` — L694
- `Gamma Log Density()` — L699
- `Gamma Log Distribution()` — L703
- `Gamma Quantile()` — L707
- `GenGamma Density()` — L718
- `GenGamma Distribution()` — L753
- `GenGamma Quantile()` — L787
- `IGamma()` — L689
- `Johnson Sb Density()` — L855
- `Johnson Sb Distribution()` — L876
- `Johnson Sb Quantile()` — L893
- `Johnson Sl Density()` — L904
- `Johnson Sl Distribution()` — L931
- `Johnson Sl Quantile()` — L956
- `Johnson Su Density()` — L970
- `Johnson Su Distribution()` — L991
- `Johnson Su Quantile()` — L1007
- `LEV Density()` — L1024
- `LEV Distribution()` — L1041
- `LEV Quantile()` — L1054
- `LogGenGamma Density()` — L1073
- `LogGenGamma Distribution()` — L1103
- `LogGenGamma Quantile()` — L1140
- `Logistic Density()` — L1150
- `Logistic Distribution()` — L1169
- `Logistic Quantile()` — L1186
- `Loglogistic Density()` — L1205
- `Loglogistic Distribution()` — L1230
- `Loglogistic Quantile()` — L1246
- `Lognormal Density()` — L1264
- `Lognormal Distribution()` — L1280
- `Lognormal Quantile()` — L1293
- `Normal Biv Distribution()` — L1297
- `Normal Density()` — L1305
- `Normal Distribution()` — L1326
- `Normal Log CDistribution()` — L1352
- `Normal Log Density()` — L1356
- `Normal Log Distribution()` — L1361
- `Normal Mixture Density()` — L1369
- `Normal Mixture Distribution()` — L1375
- `Normal Mixture Quantile()` — L1381
- `Normal Quantile()` — L1387
- `Probit()` — L1388
- `SEV Density()` — L1395
- `SEV Distribution()` — L1416
- `SEV Quantile()` — L1429
- `SHASH Density()` — L1445
- `SHASH Distribution()` — L1470
- `SHASH Quantile()` — L1487
- `Tukey HSD P Value()` — L1565
- `Tukey HSD Quantile()` — L1576
- `Weibull Density()` — L1593
- `Weibull Distribution()` — L1610
- `Weibull Quantile()` — L1624
---

JSL Functions, Operators, and Messages
Probability Functions

223

Newton-Raphson method is used when an analytical derivative is found for the Hessian.
Otherwise, the Symmetric-Rank One method (SR1), a quasi-Newton method, is used.
Messages
<<Max Iter(int) An integer that specifies the maximum number of iterations to be

performed. The default maximum number of iterations is 250.
<<Tolerance(p) p sets the tolerance for the convergence criterion. The default tolerance
is 10-8.
<<Details("both" | "displaySteps" | "returnDetails") Specifies what output is
returned. If ʺdisplayStepsʺ is specified, step-by-step results of the optimization appear
in the Log window. If ʺreturnDetailsʺ is specified, the function returns a list that
contains the final values for the objective value, number of iterations, gradient, and
Hessian. Specify ʺbothʺ to get the return value and the results in the Log.
<<Gradient(exprList) Specifies a list of expressions that define the analytical gradient
that is used for the optimization. Each expression in the list represents a derivative of
the expression expr.
<<Hessian(exprList) Specifies a list of expressions that define the analytical Hessian
that is used for the optimization. Each expression in the list represents the upper
triangular portion of the Hessian matrix in row-major order.
<<Method(NR | SR1) Specifies either the Newton-Raphson (NR) method or the
Symmetric-Rank One (SR1) method for the optimization method.
<<UseNumericDeriv("true") Specifies that the optimization use a numeric
approximation.

Probability Functions
Beta Density(x, alpha, beta, <theta=0>, <sigma=1>)
Description

Returns the probability density function (pdf) evaluated at x of the beta distribution. The
pdf is parameterized as follows:
1
f  x  = -------------------------------------------  x –    – 1   +  – x   – 1
B      +  – 1
where B(·) is the Beta function.
Arguments
x A quantile at which the pdf is evaluated. x must be between theta and theta + sigma.
alpha, beta Shape parameters  and , which must both be greater than 0.
theta Optional threshold parameter . The default is 0.
sigma Optional scale parameter , which must be greater than 0. The default is 1.

Probability Functions

Notes

The beta distribution is useful for modeling the probabilistic behavior of random variables
that are constrained to fall in the interval [0, 1], such as proportions.
Beta Distribution(x, alpha, beta, <theta=0>, <sigma=1>)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the beta distribution.
The cdf uses the same parameterization as the Beta Density() function.
Arguments
x A quantile at which the cdf is evaluated. x must be between theta and theta + sigma.
alpha, beta Shape parameters  and , which must both be greater than 0.
theta Optional threshold parameter . The default is 0.
sigma Optional scale parameter , which must be greater than 0. The default is 1.

Beta Quantile(p, alpha, beta, <theta=0>, <sigma=1>)
Description

Returns the pth quantile from a beta distribution with shape arguments alpha and beta.
The quantile function does not have a closed form equation.
Arguments
p The probability of the quantile desired. p must be between 0 and 1.
alpha, beta Shape parameters  and , which must both be greater than 0.
theta Optional threshold parameter . The default is 0.
sigma Optional scale parameter , which must be greater than 0. The default is 1.

Cauchy Density(q, <center=0>, <scale=1>)
Description

Returns the probability density function (pdf) evaluated at q of a Cauchy distribution. The
pdf is parameterized as follows:
1
1
f  q  = ------- -----------------------------
q– 2
1 +  ------------
  
Arguments
q A quantile at which the pdf is evaluated.
center Optional location parameter . The default is 0.
scale Optional scale parameter, , which must be greater than 0. The default is 1.

JSL Functions, Operators, and Messages
Probability Functions

225

Cauchy Distribution(q, <center=0>, <scale=1>)
Description

Returns the cumulative distribution function (cdf) probability that a Cauchy distributed
random variable is less than q. The cdf is parameterized as follows:
x–
1 1
F  q  = --- + --- arctan  ------------
  
2 
Arguments
q A quantile at which the cdf is evaluated.
center Optional location parameter . The default is 0.
scale Optional scale parameter, , which must be greater than 0. The default is 1.

Cauchy Quantile(p, <center=0>, <scale=1>)
Description

Returns the pth quantile from a Cauchy distribution. The pth quantile is the value for which
the probability is p that a random value would be less than or equal to p. The quantile
function is parameterized as follows:
F

–1

1
 p  =  tan   p + --- + 

2

Arguments
p The probability of the quantile desired. p must be between 0 and 1.
center Optional location parameter . The default is 0.
scale Optional scale parameter , which must be greater than 0. The default is 1.

ChiSquare Density(q, df, <nc=0>)
Description

Returns the probability density function (pdf) evaluated at q of the chi-square distribution.
The pdf is parameterized as follows:


r

  2
f  q  = exp  –   2   ----------------- f n + 2r  q 
r!
r=0

where fn+2r(q) is the density of a central chi-square distribution with n+2r degrees of
freedom.
Arguments
q A quantile at which the pdf is evaluated. q must be greater than or equal to 0.

Probability Functions

df The degrees of freedom n, which must be greater than 0.
nc Optional noncentrality parameter  which must be nonnegative. The default is 0.

ChiSquare Distribution(q, df, <nc=0>)
Description

Returns cumulative distribution function at quantile x for chi-square with df degrees of
freedom centered at nc. The cdf is parameterized as follows:


r

  2
F  q  = exp  –   2   ----------------- F n + 2r  q  ,
r!
r=0

where Fn+2r(q) is the cumulative distribution of a central chi-square distribution with n+2r
degrees of freedom.
Arguments
q A quantile at which the cdf is evaluated. q must be greater than or equal to 0.
df The degrees of freedom n, must be greater than 0.
nc The optional noncentrality parameter  must be nonnegative. The default is 0.

ChiSquare Log CDistribution(x, df, <nc=0>)
Description

Returns the log of (1 - value), where value is the cumulative distribution function
evaluated at x of the chi-square distribution with df degrees of freedom and noncentrality
parameter nc.
ChiSquare Log Density(x, df, <nc=0>)
Description

Returns the log of the value of the probability density function evaluated at x of the
chi-square distribution with df degrees of freedom and noncentrality parameter nc.
ChiSquare Log Distribution(x, df, <nc=0>)
Description

Returns the log of the value of the cumulative distribution function evaluated at quantile x
of the chi-square distribution with df degrees of freedom and noncentrality parameter nc.
ChiSquare Noncentrality(x, df, prob)
Description

Returns the chi-square distribution noncentrality parameter nc that satisfies the following:

JSL Functions, Operators, and Messages
Probability Functions

227

prob = ChiSquare Distribution(x, df, nc)
Arguments
x A quantile at which the cdf is evaluated.
df The degrees of freedom n, which must be greater than 0.
prob The probability of the quantile desired; prob must be between 0 and 1.

ChiSquare Quantile(p, df, <nc=0>)
Description

Returns the pth quantile from a chi-square distribution with df degrees of freedom,
centered at nc. The quantile function does not have a closed form equation.
Arguments
p The probability of the quantile desired. p must be between 0 and 1.
df The degrees of freedom n, which must be greater than 0.
nc Optional noncentrality parameter  which must be nonnegative. The default is 0.

Dunnett P Value(q, nTrt, dfe, <lambdaVec=.>)
Description

Returns the p-value from Dunnett’s multiple comparisons test.
Arguments
q A number that is the test statistic.
nTrt The number of treatments being compared to the control treatment.
dfe The error degrees of freedom.
lambdaVec A vector of parameters. If lambdaVec is missing (.), each of the parameters is

set to 1/Sqrt(2).
Dunnett Quantile(1-alpha, nTrt, dfe, <lambdaVec=.>)
Description

Returns the quantile used in Dunnett’s multiple comparisons test.
Arguments
1-alpha A number that is the confidence level.
nTrt The number of treatments being compared to the control treatment.
dfe The error degrees of freedom.
lambdaVec A vector of parameters. If lambdaVec is missing (.), each of the parameters is

set to 1/Sqrt(2).

Probability Functions

ExGaussian Density(x, mu, sigma, lambda)
Description

Returns the probability density function (pdf) evaluated at x of the exponentially modified
Gaussian distribution. The pdf is parameterized as follows:
2

2

  2 +  – 2x 
x –  – 
 exp --------------------------------------------  ---------------------------
2
Arguments
x A quantile at which the pdf is evaluated.
mu The mean of the normal distribution.
sigma The standard deviation of the normal distribution. sigma must be greater than 0.
lambda The  parameter of the exponential distribution. lambda must be greater than 0.

Note: The parameterization in the ExGaussian Density function uses the reciprocal of the
parameterization that is used in the Exponential Density function.
ExGaussian Distribution(x, mu, sigma, lambda)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the exponentially
modified Gaussian distribution.
Arguments
x A quantile at which the cdf is evaluated.
mu The mean of the normal distribution.
sigma The standard deviation of the normal distribution. sigma must be greater than 0.
lambda The  parameter of the exponential distribution. lambda must be greater than 0.

Note: The parameterization in the ExGaussian Distribution function uses the reciprocal of the
parameterization that is used in the Exponential Distribution function.
ExGaussian Quantile(p, mu, sigma, lambda)
Description

Returns the pth quantile from an exponentially modified Gaussian distribution.
Arguments
p The probability of the quantile desired. p must be between 0 and 1.
mu The mean of the normal distribution.
sigma The standard deviation of the normal distribution. sigma must be greater than 0.

JSL Functions, Operators, and Messages
Probability Functions

229

lambda The  parameter of the exponential distribution. lambda must be greater than 0.

Note: The parameterization in the ExGaussian Quantile function uses the reciprocal of the
parameterization that is used in the Exponential Quantile function.
Exp Density(x, <theta=1>)
Exponential Density(x, <theta=1>)
Description

Returns the probability density function (pdf) evaluated at x of the exponential
distribution. The pdf is parameterized as follows:
1
f  x  = --- exp  – x   

Arguments
x A quantile at which the pdf is evaluated. x must be greater than or equal to 0.
theta Optional scale parameter , which must be greater than 0. The default is 1.

Exp Distribution(x, <theta=1>)
Exponential Distribution(x, <theta=1>)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the exponential
distribution. The cdf is parameterized as follows:
F  x  = 1 – exp  – x   
Arguments
x A quantile at which the cdf is evaluated. x must be greater than or equal to 0.
theta Optional scale parameter , which must be greater than 0. The default is 1.

Exp Quantile(p, <theta=1>)
Exponential Quantile(p, <theta=1>)
Description

Returns the pth quantile from an exponential distribution with scale parameter theta. The
quantile function is parameterized as follows:
F

–1

 p  = – log  1 – p 

Probability Functions

Arguments
p The probability of the quantile desired. p must be between 0 and 1.
theta Optional scale parameter , which must be greater than 0. The default is 1.

F Density(x, dfnum, dfden, <nc=0>)
Description

Returns the probability density function (pdf) evaluated at x for the F distribution with
numerator and denominator degrees of freedom dfnum and dfden, with optional
noncentrality parameter nc.


r

v1
----- + r
 v 1 2


  2
f  x  = exp  –   2   --------------------------------------  -----
v2 v1
 v 2
r = 0 B  ----- ----- + r r!
2 2


v1 + v2 
–  ---------------- + r v 1
----- – 1 + r
2
v1 
2

 1 + ----- x
v2 


x

where B(·) is the Beta function.
Arguments
x A quantile at which the pdf is evaluated. x must be greater than 0.
dfnum The degrees of freedom, v1, of the chi-square distribution in the numerator of the

F-distribution. dfnum must be greater than 0.
dfden The degrees of freedom, v2, of the chi-square distribution in the denominator of the
F-distribution. dfden must be greater than 0.
nc Optional noncentrality parameter  which must be nonnegative. The default is 0.
F Distribution(x, dfnum, dfden, <nc=0>)
Description

Returns the cumulative distribution function (cdf) evaluated at x for the F distribution
with numerator and denominator degrees of freedom dfnum and dfden and noncentrality
parameter nc.
F Log CDistribution(x, dfnum, dfden, <nc=0>)
Description

Returns the log of (1 - value), where value is the cumulative distribution function
evaluated at x of the F distribution with numerator and denominator degrees of freedom
dfnum and dfden, with optional noncentrality parameter nc.

JSL Functions, Operators, and Messages
Probability Functions

231

F Log Density(x, dfnum, dfden, <nc=0>)
Description

Returns the log of the value of the probability density function (pdf) evaluated at x for the
F distribution with numerator and denominator degrees of freedom dfnum and dfden,
with optional noncentrality parameter nc.
F Log Distribution(x, dfnum, dfden, <nc=0>)
Description

Returns the log of the value of the cumulative distribution function (cdf) evaluated at x for
the F distribution with numerator and denominator degrees of freedom dfnum and dfden
and noncentrality parameter nc.
F Noncentrality(x, dfnum, dfden, prob)
Description

Returns the F distribution noncentrality parameter nc that satisfies the following:
prob = F Distribution(x, dfnum, dfden, nc)
See Also

“F Distribution(x, dfnum, dfden, <nc=0>)”
F Power(alpha, dfh, dfm, d, n)
Description

Returns the power from a given situation involving an F test or a t test.
Arguments
alpha The significance level of the test. alpha must be between 0 and 1.
dfh The hypothesis degrees of freedom. dfh must be greater than 0.
dfm The degrees of freedom in the whole model. dfm must be greater than 0.
d The squared effect size, defined as 2/2. In this equation, 2 is the error variance and 2

is defined as follows:
2

 = x –  2

for a one-sample t test

2

 x 1 – x 2  for a two-sample t test
 = ----------------------4
2

Probability Functions

2

 =

k x – x
i

2

 -------------------k

for a k-sample F test

i=1

n The total number of observations. n must be greater than dfm.

F Quantile(x, dfnum, dfden, <nc=0>)
Description

Returns the pth quantile from the F distribution with numerator and denominator degrees
of freedom dfnum and dfden and noncentrality parameter nc.
F Sample Size(alpha, dfh, dfm, d, power)
Description

Returns the sample size from a given situation involving an F test or a t test.
Arguments
alpha The significance level of the test. alpha must be between 0 and 1.
dfh The hypothesis degrees of freedom. dfh must be greater than 0.
dfm The degrees of freedom in the whole model. dfm must be greater than 0.
d The squared effect size, defined as 2/2. In this equation, 2 is the error variance and 2

is defined as follows:
2

 = x –  2

for a one-sample t test

2

 x 1 – x 2  for a two-sample t test
 = ----------------------4
2

2

 =

k x – x
i

2

 -------------------k

for a k-sample F test

i=1

power The desired power for the test.

FDR Adjust(matrix)
Description

Returns the false discovery rate (FDR) adjustment for the specified p-values using the
Benjamini-Hochberg method. See Predictive and Specialized Modeling.
Argument
matrix A matrix of p-values.

JSL Functions, Operators, and Messages
Probability Functions

233

Frechet Density(x, mu, sigma)
Description

Returns the probability density function (pdf) evaluated at x of the Fréchet distribution.
The pdf is parameterized as follows:
log  x  –  1
log  x  – 
f  x  = exp – exp  – --------------------------- exp  – -------------------------- -----
 x




Arguments
x A quantile at which the pdf is evaluated. x must be greater than 0.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Frechet Distribution(x, mu, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the Fréchet
distribution. The cdf is parameterized as follows:
log  x  – 
F  x  = exp – exp  – ---------------------------



Arguments
x A quantile at which the cdf is evaluated. x must be greater than 0.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Frechet Quantile(p, mu, sigma)
Description

Returns the pth quantile from a Fréchet distribution with location mu and scale sigma. The
quantile function is parameterized as follows:
F

–1

 p  = exp  –  log  – log  p   +  

Arguments
p The probability of the quantile desired. p must be between 0 and 1.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Probability Functions

Gamma Density(x, <alpha=1>, <scale=1>, <threshold=0>)
Description

Returns the probability density function (pdf) evaluated at x of the Gamma distribution.
The pdf is parameterized as follows:
1
f  x  = -------------------  x –    – 1 exp  –  x –     
    
Arguments
x A quantile at which the pdf is evaluated. x must be greater than .
alpha Optional shape parameter  which must be greater than 0. The default is 1.
scale Optional scale parameter , which must be greater than 0. The default is 1.
threshold Optional threshold parameter . The default is 0.

Gamma Distribution(x, <alpha=1>, <scale=1>, <threshold=0>)
IGamma(x, <alpha=1, scale=1, threshold=0>)
Description

Returns the cumulative distribution function (cdf) evaluated at quantile x for the gamma
distribution with parameters alpha, scale, and threshold.
Gamma Log CDistribution(x, <alpha=1>, <scale=1>, <threshold=0>)
Description

Same as Log(1 – Gamma Distribution(x, alpha)) except that it has a much greater
range.
Gamma Log Density(x, <alpha=1>, <scale=1>, <threshold=0>)
Description

Same as Log(Gamma Density(x, alpha)) except that it has a much greater range.
Gamma Log Distribution(x, <alpha=1>, <scale=1>, <threshold=0>)
Description

Same as Log(Gamma Distribution(x, alpha)) except that it has a much greater range.
Gamma Quantile(p, <alpha=1>, <scale=1>, threshold>)
Description

Returns the pth quantile from the gamma distribution with the alpha, scale, and
threshold parameters given.

JSL Functions, Operators, and Messages
Probability Functions

235

GenGamma Density(x, mu, sigma, lambda)
Description

Returns the probability density function (pdf) evaluated at x of an extended generalized
gamma probability distribution. The pdf is parameterized as follows:

–2

 ----- x  lg   + log    ;
fx = 
1
 ----- x  nor   




–2



if   0
if  = 0

where = [log(x) – ]/. Note that the following is the pdf for the standardized log-gamma
variable with shape parameter  > 0:
1
 lg  z ;  = ------------ exp  z – exp  z  

Note that nor(·) is the standard normal pdf.
Arguments
x A quantile at which the pdf is evaluated. x must be greater than 0.
mu The location parameter 
sigma The scale parameter , which must be greater than 0.
lambda A shape parameter .

GenGamma Distribution(x, mu, sigma, lambda)
Description

Returns the cumulative distribution function (cdf) of the extended generalized gamma
distribution. The cdf is parameterized as follows:

–2
–2
  lg   + log    ;  

F  x  =   nor   

 1 –    + log   – 2  ;  – 2 

lg

if   0
if  = 0
if   0

where = [log(x) – ]/. Note that the following is the cdf for the standardized log-gamma
variable with shape parameter  > 0:
 lg  z ;  =  I  exp  z  ; 

Probability Functions

where I[·] denotes the incomplete gamma function. Note that nor(·) is the standard
normal cdf.
Arguments
x A quantile at which the cdf is evaluated. x must be greater than 0.
mu The location parameter 
sigma The scale parameter , which must be greater than 0.
lambda A shape parameter .

GenGamma Quantile(p, mu, sigma, lambda)
Description

Returns the pth quantile from an extended generalized gamma distribution with
parameters mu, sigma, and lambda. The quantile function does not have a closed form
equation.
Arguments
p The probability of the quantile desired. p must be between 0 and 1.
mu The location parameter 
sigma The scale parameter , which must be greater than 0.
lambda A shape parameter .

GLog Density(x, mu, sigma, lambda)
Description

Returns the probability density function (pdf) evaluated at x of a generalized logarithmic
distribution. The pdf is parameterized as follows:
1

x + x2 + 2
x + x2 + 2
f  x  =   --- log  -------------------------------- –   -----------------------------------------------------------

2

  x 2 +  2 + x x 2 +  2 
where (·) is the standard normal pdf.
Arguments
x A quantile at which the pdf is evaluated.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.
lambda A shape parameter , which must be greater than 0.
Notes

When the shape parameter is equal to zero, the distribution reduces to a Lognormal(, ).

JSL Functions, Operators, and Messages
Probability Functions

237

GLog Distribution(x, mu, sigma, lambda)
Description

Returns the probability that a generalized logarithmically distribution random variable is
less than x. The cdf is parameterized as follows:
1

x + x2 + 2
F  x  =   --- log  -------------------------------- –  


2


where (·) is the standard normal cdf.
Arguments
x A quantile at which the cdf is evaluated.
mu The location parameter 
sigma The scale parameter , which must be greater than 0.
lambda A shape parameter , which must be greater than 0.

GLog Quantile(p, mu, sigma, lambda)
Description

Returns the pth quantile from a generalized logarithmic distribution.
IGamma()
See “Gamma Distribution(x, <alpha=1>, <scale=1>, <threshold=0>)”.
Johnson Sb Density(q, gamma, delta, theta, sigma)
Description

Returns the probability density function (pdf) evaluated at q of a Johnson Sb distribution.
The pdf is parameterized as follows:
q–

f  q  =   +  ln  --------------------------  ------------------------------------------------
  –  q –     q –     –  q –   
where (·) is the standard normal pdf.
Arguments
q A quantile at which the pdf is evaluated. q must be in the interval theta to theta +

sigma.
gamma Shape parameter .
delta Shape parameter , which must be greater than 0.
theta Location parameter .
sigma Scale parameter , which must be greater than 0.

Probability Functions

Johnson Sb Distribution(q, gamma, delta, theta, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at q of a Johnson Sb
distribution. The pdf is parameterized as follows:
q–
F  q  =   +  ln  --------------------------
  –  q –  
where (·) is the standard normal cdf.
Arguments
q A quantile at which the cdf is evaluated. q must be in the interval theta to theta +

sigma.
gamma Shape parameter .
delta Shape parameter , which must be greater than 0.
theta Location parameter .
sigma Scale parameter , which must be greater than 0.
Johnson Sb Quantile(p, gamma, delta, theta, sigma)
Description

Returns the pth quantile from a Johnson Sb distribution.
Arguments
p The probability of the quantile desired. p must be between 0 and 1.
gamma Shape parameter .
delta Shape parameter , which must be greater than 0.
theta Location parameter .
sigma Scale parameter , which must be greater than 0.

Johnson Sl Density(x, gamma, delta, theta, sigma)
Description

Returns the probability density function (pdf) evaluated at x of a Johnson Sl distribution.
The pdf is parameterized as follows:

x–
f  x  = ---------------   +  ln  ------------
  
x–
where (·) is the standard normal pdf.
Arguments
x A quantile at which the pdf is evaluated. x must be greater than theta if sigma is 1 and

less than theta if sigma is -1.

JSL Functions, Operators, and Messages
Probability Functions

239

gamma Shape parameter .
delta Shape parameter , which must be greater than 0.
theta Location parameter .
sigma Parameter  that indicates if the distribution is skewed positively or negatively.
sigma must be equal to either +1 (skewed positively) or -1 (skewed negatively).

Johnson Sl Distribution(q, gamma, delta, theta, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at q of a Johnson Sl
distribution.

– 
   +  ln  x----------- , =1
  

Fx  = 

 x – - ,  = – 1
 1 –   +  ln  ---------- 

where (·) is the standard normal cdf.
Arguments
q A quantile at which the cdf is evaluated. q must be greater than theta if sigma is 1 and

less than theta if sigma is -1.
gamma Shape parameter .
delta Shape parameter , which must be greater than 0.
theta Location parameter .
sigma Parameter that defines if the distribution is skewed positively or negatively.
Sigma must be equal to either +1 (skewed positively) or -1 (skewed negatively).
Johnson Sl Quantile(p, gamma, delta, theta, sigma)
Description

Returns the pth quantile from a Johnson Sl distribution.
Arguments
p The probability of the quantile desired. p must be between 0 and 1.
gamma Shape parameter .
delta Shape parameter , which must be greater than 0.
theta Location parameter .
sigma Parameter  that defines if the distribution is skewed positively or negatively.
Sigma must be equal to either +1 (skewed positively) or -1 (skewed negatively).

Probability Functions

Johnson Su Density(x, gamma, delta, theta, sigma)
Description

Returns the probability density function (pdf) evaluated at x of a Johnson Su distribution.
The pdf is parameterized as follows:

x –  2 –1  2
x–
f  x  = --- 1 +  ------------
  +  sinh– 1  ------------
  
  

where (·) is the standard normal pdf.
Arguments
x A quantile at which the pdf is evaluated.
gamma Shape parameter .
delta Shape parameter , which must be greater than 0.
theta Location parameter .
sigma Scale parameter , which must be greater than 0.

Johnson Su Distribution(q, gamma, delta, theta, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at q of a Johnson Su
distribution. The cdf is parameterized as follows:
x–
F  x  =   +  sinh– 1  ------------
  
where (·) is the standard normal cdf.
Arguments
q A quantile at which the cdf is evaluated.
gamma Shape parameter .
delta Shape parameter , which must be greater than 0.
theta Location parameter .
sigma Scale parameter , which must be greater than 0.

Johnson Su Quantile(p, gamma, delta, theta, sigma)
Description

Returns the pth quantile from a Johnson Su distribution.
Arguments
p The probability of the quantile desired. p must be between 0 and 1.
gamma Shape parameter .

JSL Functions, Operators, and Messages
Probability Functions

241

delta Shape parameter , which must be greater than 0.
theta Location parameter .
sigma Scale parameter , which must be greater than 0.

LEV Density(x, mu, sigma)
Description

Returns the probability density function (pdf) evaluated at x of the largest extreme value
distribution with location mu and scale sigma. The pdf is parameterized as follows:
1
x–
x–
f  x  = --- exp – ------------ – exp  – ------------
  


Arguments
x A quantile at which the pdf is evaluated.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

LEV Distribution(x, mu, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the largest extreme
value distribution with location mu and scale sigma. The cdf is parameterized as follows:
x–
F  x  = exp – exp  – ------------
  
Arguments
x A quantile at which the cdf is evaluated. x must be greater than sigma
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

LEV Quantile(p, mu, sigma)
Description

Returns the pth quantile from a largest extreme value distribution with location mu and
scale sigma. The quantile function is parameterized as follows:
F

–1

 p  = –  log  – log  p   + 

Arguments
p The probability of the quantile desired. p must be between 0 and 1.
mu The location parameter .

Probability Functions

sigma The scale parameter , which must be greater than 0.

LogGenGamma Density(x, mu, sigma, lambda)
Description

Returns the probability density function (pdf) evaluated at x of a log generalized gamma
probability distribution with parameters mu, sigma, and lambda. The pdf is
parameterized as follows:

–2 –2

 ----   lg   + log    ; 
fx = 
 --1-    
  nor


if   0
if  = 0

where = [x – ]/. Note that the following is the pdf for the log-gamma variable with
shape parameter  > 0:
1
 lg  z ;  = ------------ exp  z – exp  z  
 
Note that nor(·) is the standard normal pdf.
Arguments
x A quantile at which the pdf is evaluated.
mu The location parameter 
sigma The scale parameter , which must be greater than 0.
lambda A shape parameter .

LogGenGamma Distribution(x, mu, sigma, lambda)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the log generalized
gamma distributed random variable (with parameters mu, sigma, and lambda) The cdf is
parameterized as follows:

–2 –2
  lg   + log    ; 

F  x  =   nor   

 1 –    + log   – 2  ;  – 2 

lg

if   0
if  = 0
if   0

where = [x – ]/. Note that the following is the cdf for the log-gamma variable with
shape parameter  > 0:

JSL Functions, Operators, and Messages
Probability Functions

243

 lg  z ;  =  I  exp  z  ; 
where I[·] denotes the incomplete gamma function. Note that nor(·) is the standard
normal cdf.
Arguments
x A quantile at which the cdf is evaluated.
mu The location parameter 
sigma The scale parameter , which must be greater than 0.
lambda A shape parameter .

LogGenGamma Quantile(p, mu, sigma, lambda)
Description

Returns the pth quantile from a log generalized gamma distribution.
Arguments
p The probability of the quantile desired. p must be between 0 and 1.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.
lambda A shape parameter .

Logistic Density(x, mu, sigma)
Description

Returns the probability density function (pdf) evaluated at x of a logistic distribution with
location mu and scale sigma. The pdf is parameterized as follows:
x–
exp  – ------------

 
1
f  x  = --- ------------------------------------------------
x– 2
1 + exp  – ------------
  
Arguments
x A quantile at which the pdf is evaluated.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Logistic Distribution(x, mu, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the logistic
distribution with location mu and scale sigma. The cdf is parameterized as follows:

Probability Functions

1
F  x  = ---------------------------------------------x–
1 + exp  – ------------
  
Arguments
x A quantile at which the cdf is evaluated. x must be greater than .
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Logistic Quantile(p, mu, sigma)
Description

Returns the pth quantile from a logistic distribution with location mu and scale sigma. The
quantile function is parameterized as follows:
F

–1

1
 p  = – log  --- – 1 + 
p


Arguments
p The probability of the quantile desired. p must be between 0 and 1.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Loglogistic Density(x, mu, sigma)
Description

Returns the probability density function (pdf) evaluated at x of a loglogistic distribution
with location mu and scale sigma. The pdf is parameterized as follows:
log  x  – 
exp  --------------------------

1
f  x  = ------ ----------------------------------------------------------x
log  x  –  2
1 + exp  --------------------------



Arguments
x A quantile at which the pdf is evaluated.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

JSL Functions, Operators, and Messages
Probability Functions

245

Loglogistic Distribution(x, mu, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the loglogistic
distribution with location mu and scale sigma. The cdf is parameterized as follows:
1
F  x  = ------------------------------------------------------log
 x  – -
1 + exp  – ------------------------


Arguments
x A quantile at which the cdf is evaluated.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Loglogistic Quantile(p, mu, sigma)
Description

Returns the pth quantile from a loglogistic distribution with location mu and scale sigma.
The quantile function is parameterized as follows:
F

–1

 p  = exp –  log  1--- – 1 + 
p


Arguments
p The probability of the quantile desired. p must be between 0 and 1.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Lognormal Density(x, mu, sigma)
Description

Returns the probability density function (pdf) evaluated at x of a lognormal distribution
with location mu and scale sigma. The pdf is parameterized as follows:
1 log  x  – 
f  x  = ---  -------------------------x

where (·) is the standard normal pdf.
Arguments
x A quantile at which the pdf is evaluated. x must be greater than or equal to 0.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Probability Functions

Lognormal Distribution(x, mu, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at x of a lognormal
distribution with location mu and scale sigma. The cdf is parameterized as follows:
log  x  – 
F  x  =  -------------------------
where (·) is the standard normal cdf.
Arguments
x A quantile at which the pdf is evaluated. x must be greater than or equal to 0.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

Lognormal Quantile(x, mu, sigma)
Description

Returns the pth quantile of a lognormal distribution with location mu and scale sigma.
Normal Biv Distribution(x, y, r, <mu1>, <s1>, <mu2>, <s2>)
Description

Computes the probability that an observation (X, Y) is less than or equal to (x, y) with
correlation coefficient r where X is individually normally distributed with mean mu1 and
standard deviation s1 and Y is individually normally distributed with mean mu2 and
standard deviation s2. If mu1, s1, mu2, and s2 are not given, the function assumes the
standard normal bivariate distribution with mu1=0, s1=1, mu2=0, and s2=1.
Normal Density(x, <mean=0>, <stddev=1>)
Description

Returns the probability density function (pdf) evaluated at x for the normal distribution
with mean and stddev. The pdf is parameterized as follows:
1
 x –   2f  x  = ----------------- exp – ------------------2 2
2 2
Arguments
x A quantile at which the pdf is evaluated.
mu Optional location parameter . The default is 0.
sigma Optional scale parameter , which must be greater than 0. The default is 1.

JSL Functions, Operators, and Messages
Probability Functions

247

Notes

The normal distribution is bell shaped and symmetrical.
Normal Distribution(x, <mean=0>, <stddev=1>)
Description

Returns the cumulative distribution function (cdf) evaluated at x for the normal
distribution with mean and stddev. The cdf is parameterized as follows:
x–
F  x  =   ------------
  
Note that (·) is the standard normal cdf, defined as follows:
x

2

1
t
  x  = ----------  exp  – ---- dt

2
2
0

Arguments
x A quantile at which the pdf is evaluated.
mu Optional location parameter . The default is 0.
sigma Optional scale parameter , which must be greater than 0. The default is 1.

Normal Log CDistribution(x, <mean=0>, <std dev=1>)
Description

Returns 1 - log (value) of the distribution function at quantile x for the normal distribution.
Normal Log Density(x, <mean=0>, <stddev=1>)
Description

Returns the log of the value of the density function at quantile x for the normal
distribution with mean and stddev. The default mean is 0. The default stddev is 1.
Normal Log Distribution(x, <mean=0>, <std dev=1>)
Description

Returns the log of the value of the distribution function at quantile x for the normal
distribution.

Probability Functions

Normal Mixture Density(q, mean, stdev, probability)
Description

Returns the density at q of a normal mixture distribution with group means mean, group
standard deviations stdev, and group probabilities probability. The mean, stdev, and
probability arguments are all vectors of the same size.
Normal Mixture Distribution(q, mean, stdev, probability)
Description

Returns the probability that a normal mixture distributed variable with group means
mean, group standard deviations stdev, and group probabilities probability is less
than q. The mean, stdev, and probability arguments are all vectors of the same size.
Normal Mixture Quantile(p, mean, stdev, probability)
Description

Returns the pth quantile, the values for which the probability is p that a random value
would be lower. The mean, stdev, and probability arguments are all vectors of the
same size.
Normal Quantile(p, <mean=0>, <stddev=1>)
Probit(p, <mean=0>, <stddev=1>)
Description

Returns the pth quantile from the normal distribution with mean and stddev. The default
mean is 0. the default stddev is 1.
Probit()
See “Normal Quantile(p, <mean=0>, <stddev=1>)”.
SEV Density(x, mu, sigma)
Description

Returns the probability density function (pdf) evaluated at x of the smallest extreme
distribution with location mu and scale sigma. The pdf is parameterized as follows:
1
– 
– - – exp  x----------f  x  = --- exp x----------  


Arguments
x A quantile at which the pdf is evaluated.

JSL Functions, Operators, and Messages
Probability Functions

249

mu The location parameter .
sigma The scale parameter , which must be greater than 0.

SEV Distribution(x, mu, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the smallest extreme
distribution with location mu and scale sigma. The cdf is parameterized as follows:
x–
F  x  = 1 – exp – exp  ------------
  
Arguments
x A quantile at which the cdf is evaluated. x must be greater than .
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

SEV Quantile(p, mu, sigma)
Description

Returns the pth quantile of the smallest extreme distribution with location mu and scale
sigma. The quantile function is parameterized as follows:
F

–1

 p  =  log  – log  1 – p   + 

Arguments
p The probability of the quantile desired. p must be between 0 and 1.
mu The location parameter .
sigma The scale parameter , which must be greater than 0.

SHASH Density(x, gamma, delta, theta, sigma)
Description

Returns the probability density function (pdf) evaluated at x of a sinh-arcsinh (SHASH)
distribution. The pdf is parameterized as follows:
 cosh  w 
f  x  = -------------------------------------   sinh  w  
2
2
 + x – 
where
(·) is the standard normal pdf

Probability Functions

x–
w =  +  sinh–1  ------------
  
Arguments
x A quantile at which the pdf is evaluated.
gamma The shape parameter .
delta The shape parameter , which must be greater than 0.
theta The location parameter .
sigma The scale parameter , which must be greater than 0.

SHASH Distribution(x, gamma, delta, theta, sigma)
Description

Returns the cumulative distribution function (cdf) evaluated at x of the sinh-arcsinh
(SHASH) distribution. The cdf is parameterized as follows:
x–
F  x  =  sinh   +  sinh– 1  ------------ 

  
where (·) is the standard normal cdf.
Arguments
x A quantile at which the cdf is evaluated.
gamma The shape parameter .
delta The shape parameter , which must be greater than 0.
theta The location parameter .
sigma The scale parameter , which must be greater than 0.

SHASH Quantile(p, gamma, delta, theta, sigma)
Description

Returns the pth quantile from a sinh-arcsinh (SHASH) distribution (with parameters
gamma, delta, theta, and sigma).
Arguments
p The probability of the quantile desired. p must be between 0 and 1.
gamma The shape parameter .
delta The shape parameter , which must be greater than 0.
theta The location parameter .
sigma The scale parameter , which must be greater than 0.

JSL Functions, Operators, and Messages
Probability Functions

251

Students t Density()
See “t Density(x, df, <nc=0>)”.
Students t Distribution()
See “t Distribution(q, df, <nc=0>)”.
Students t Quantile()
See “t Quantile(p, df, <nc=0>)”.
t Density(x, df, <nc=0>)
Students t Density(x, df, <nc=0>)
Description

Returns the probability density function (pdf) evaluated at x of the Student’s t distribution
with degrees of freedom df. The pdf is parameterized as follows:
+1
  + 1-
  ------------
 2  1
2 –  ----------2 
x
f  x  = ---------------------- ---------- 1 + -----


  ---
 2
Arguments
x A quantile at which the pdf is evaluated.
df The degrees of freedom , which must be greater than or equal to 1.
nc The optional noncentrality parameter , which must be nonnegative. The default is 0.

t Distribution(q, df, <nc=0>)
Students t Distribution(q, df, <nc=0>)
Description

Returns the probability that a Student’s t distributed random variable is less than q. nc
defaults to 0.
t Log CDistribution(x, df, <nc=0>)
Description

Returns 1 - log (value) of the normal distribution function at quantile x for the t
distribution.

Probability Functions

t Log Density(x, df, <nc=0>)
Description

Returns the log of the value of the density function at quantile x for the t distribution.
t Log Distribution(x, df, <nc=0>)
Description

Returns the log of the value of the distribution function at quantile x for the t distribution.
t Noncentrality(x, df, prob)
Description

Returns the t distribution noncentrality parameter nc that satisfies the following:
prob = T Distribution(x, df, nc)
t Quantile(p, df, <nc=0>)
Students t Quantile(p, df, <nc=0>)
Description

Returns the pth quantile from the Student’s t distribution with degrees of freedom df. nc
defaults to 0.
Tukey HSD P Value(q, n, dfe)
Description

Returns the p-value from Tukey’s HSD multiple comparisons test.
Arguments
q The test statistic. The test statistic that is specified is Tukey’s adjusted critical value,

which is the quantile of Tukey’s studentized range distribution divided by the square
root of 2.
n The number of groups in the study.
dfe The error degrees of freedom, based on the total study sample.
Tukey HSD Quantile(1-alpha, n, dfe)
Description

Returns the quantile used in Tukey’s HSD multiple comparisons test. The quantile that is
returned is Tukey’s adjusted critical value, which is the quantile of Tukey’s studentized
range distribution divided by the square root of 2.
Arguments
1-alpha The confidence level.

JSL Functions, Operators, and Messages
Probability Functions

253

n The number of groups in the study.
dfe The error degrees of freedom, based on the total study sample.

Weibull Density(x, shape, <scale=1>, <threshold=0>)
Description

Returns the probability density function (pdf) evaluated at x of the Weibull distribution.
The pdf is parameterized as follows:
 x– –1
x– 
f  x  = ---  ------------
exp –  ------------
  
  
Arguments
x A quantile the pdf is evaluated at. x must be greater than threshold.
shape Shape parameter , which must be greater than 0.
scale Optional scale parameter , which must be greater than 0. The default is 1.
threshold Optional threshold parameter . The default is 0.

Weibull Distribution(x, shape, <scale=1>, <threshold=0>)
Description

Returns the cumulative distribution function (cdf) at x of the Weibull distribution. The cdf
is parameterized as follows:
x– 
F  x  = 1 – exp –  ------------
  
Arguments
x A quantile at which the pdf is evaluated. x must be greater than threshold.
shape Shape parameter , which must be greater than 0.
scale Optional scale parameter , which must be greater than 0. The default is 1.
threshold Optional threshold parameter . The default is 0.

Weibull Quantile(p, shape, <scale=1>, <threshold=0>)
Description

Returns the pth quantile from the Weibull distribution with the parameters given. The
quantile function is calculated as follows:

F

–1

--1

 p  =   ln  1 – p   + 
