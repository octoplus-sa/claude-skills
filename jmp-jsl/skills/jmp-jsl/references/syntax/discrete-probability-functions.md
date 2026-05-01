# Discrete Probability Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 85-90).

## Index (line numbers in this file)

- `Beta Binomial Distribution()` — L50
- `Beta Binomial Probability()` — L65
- `Beta Binomial Quantile()` — L113
- `Binomial Distribution()` — L127
- `Binomial Probability()` — L144
- `Binomial Quantile()` — L160
- `Binomial()` — L117
- `Gamma Poisson Distribution()` — L171
- `Gamma Poisson Probability()` — L188
- `Gamma Poisson Quantile()` — L222
- `Hypergeometric Distribution()` — L241
- `Hypergeometric Probability()` — L257
- `Neg Binomial Distribution()` — L277
- `Neg Binomial Probability()` — L292
- `Poisson Distribution()` — L316
- `Poisson Probability()` — L328
- `Poisson()` — L226
- `Week Of Year()` — L33
- `Year()` — L44
---

JSL Functions, Operators, and Messages
Discrete Probability Functions

85

Week Of Year(date, <ruleN>)
Description

Returns the week of the year that contains a date-time value. Three rules determine when
the first week of the year begins.
– With rule 1 (the default), weeks start on Sunday, with the first Sunday of the year being
week 2. Week 1 is a partial week or empty.
– With rule 2, the first Sunday begins with week 1, with previous days being week 0.
– With rule 3, the ISO-8601 week number is returned. Weeks start on Monday. Week 1 is
the first week of the year with four days in that year. It is possible for the first or last
three days of the year to belong to the neighboring year’s week number.
Year(date)
Description

Returns an integer representation for the year of date.

Discrete Probability Functions
Beta Binomial Distribution(k, p, n, delta)
Description

Returns the cumulative distribution function (cdf) of the beta binomial distribution. This is
the probability that a beta binomially distributed random variable is less than or equal to
k. The cdf is calculated as the summation of the beta binomial pmf for values of X from 0
to k.
Arguments

k The count of interest. k must be an integer.
p The probability of success for each trial, which must be between 0 and 1.
n The number of trials, which must be greater than 1.
delta The overdispersion parameter, which must be between Maximum[-p/(n-p-1),
-(1-p)/(n-2+p)] and 1. When the overdispersion parameter is zero, the distribution
reduces to Binomial(n, p).
Beta Binomial Probability(k, p, n, delta)
Description

Returns the probability mass function (pmf) of the beta binomial distribution. This is the
probability that a beta binomially distributed random variable is equal to k. The pmf is
parameterized as follows:

Discrete Probability Functions

1
1
1
  --- – 1  k + p  --- – 1  n – k +  1 – p   --- – 1









n
P  X = k ;p n   =   --------------------------------------------------------------------------------------------------------------------------- k
1
1
1
 p  --- – 1   1 – p   --- – 1   n + --- – 1



 


Arguments

k The count of interest. k must be an integer.
p The probability of success for each trial, which must be between 0 and 1.
n The number of trials, which must be greater than 1.
delta The overdispersion parameter , which must be between Maximum[-p/(n-p-1),
-(1-p)/(n-2+p)] and 1. When the overdispersion parameter is zero, the distribution
reduces to Binomial(n, p).
Notes

The beta binomial distribution results from assuming that X| follows a Binomial(n,)
distribution and  follows a Beta(p(1-)/,(1-p)(1-)/) distribution. It is useful when the
data are a combination of several Binomial distributions that each have different
probabilities of success.
Beta Binomial Quantile(p, n, delta, cumprob)
Description

Returns the smallest integer quantile for which the cumulative probability of the Beta
Binomial(p, n, delta) distribution is larger than or equal to cumprob.
Arguments

p The probability of success for each trial. p must be between 0 and 1.
n The number of trials, which must be greater than 1.
delta The overdispersion parameter , which must be between Maximum[-p/(n-p-1),
-(1-p)/(n-2+p)] and 1. When the overdispersion parameter is zero, the distribution
reduces to Binomial(n, p).
cumprob The cumulative probability of the quantile desired. cumprob must be between 0
and 1.
Binomial Distribution(p, n, k)
Description

Returns the cumulative distribution function (cdf) of the binomial distribution. This is the
probability that a binomially distributed random variable is less than or equal to k. The cdf
is calculated as the summation of the binomial pmf for values of X from 0 to k.
Arguments

p The probability of success for each trial. p must be between 0 and 1.

JSL Functions, Operators, and Messages
Discrete Probability Functions

87

n The number of trials.
k The number of successes, which must be less than or equal to n.
Binomial Probability(p, n, k)
Description

Returns the probability mass function (pmf) of the binomial distribution. This is the
probability that a binomially distributed variable is equal to k. The pmf is parameterized
as follows:
n–k
n k
P  X = k ;p n  =   p  1 – p 
 k

Arguments

p The probability of success for each trial. p must be between 0 and 1.
n The number of trials.
k The number of successes, which must be less than or equal to n.
Binomial Quantile(p, n, cumprob)
Description

Returns the smallest integer quantile for which the cumulative probability of the
Binomial(p, n) distribution is larger than or equal to cumprob.
Arguments

p The probability of success for each trial. p must be between 0 and 1.
n The number of trials.
cumprob The cumulative probability of the quantile desired. cumprob must be between 0
and 1.
Gamma Poisson Distribution(k, lambda, sigma)
Description

Returns the cumulative distribution function (cdf) of the gamma-Poisson distribution.
This is the probability that a gamma-Poisson distributed random variable is less than or
equal to k. The cdf is calculated as the summation of the gamma-Poisson pmf for values of
X from 0 to k.
Arguments

k The count of interest. k must be an integer.
lambda The shape parameter , which much be greater than 0. This is the mean of the
distribution.
sigma The overdispersion parameter , which must be greater than or equal to 1. When
the overdispersion parameter is 1, the distribution reduces to a Poisson() distribution.

Discrete Probability Functions

Gamma Poisson Probability(k, lambda, sigma)
Description

Returns the probability mass function (pmf) of the gamma-Poisson distribution. This is the
probability that a gamma-Poisson distributed random variable is equal to k. The pmf is
parameterized as follows:


  k + ------------
–  ------------

 – 1   – 1 k    – 1 
P  X = k ;   = -------------------------------------------  ------------ 






  k + 1   ------------
  – 1
where (·) is the Gamma function.
Arguments

k The count of interest. k must be an integer.
lambda The shape parameter , which much be greater than 0. This is the mean of the
distribution.
sigma The overdispersion parameter , which must be greater than or equal to 1. When
the overdispersion parameter is 1, the distribution reduces to a Poisson() distribution.
Notes

The gamma Poisson distribution results from assuming that X| follows a Poisson()
distribution and  follows a Gamma(/(-1),-1) distribution. It is useful when the data
are a combination of several Poisson() distributions that each have different values of .
Gamma Poisson Quantile(lambda, sigma, cumprob)
Description

Returns the smallest integer quantile for which the cumulative probability of the Gamma
Poisson(lambda, sigma) distribution is larger than or equal to cumprob.
Arguments

lambda The shape parameter , which much be greater than 0. This is the mean of the
distribution.
sigma The overdispersion parameter , which must be greater than or equal to 1. When
the overdispersion parameter is 1, the distribution reduces to a Poisson() distribution.
cumprob The cumulative probability of the quantile desired. cumprob must be between 0
and 1.

JSL Functions, Operators, and Messages
Discrete Probability Functions

89

Hypergeometric Distribution(N, K, n, x, <r>)
Description

Returns the cumulative distribution function (cdf) of the hypergeometric distribution. This
is the probability that a hypergeometrically distributed random variable is less than or
equal to x. The cdf is calculated as the summation of the hypergeometric pmf for values of
X from 0 to x.
Required Arguments

N The population size.
k The number of items in the category of interest.
n The sample size.
x The count of interest, which must be less than or equal to n and k.
Optional Argument

r The odds ratio.
Hypergeometric Probability(N, k, n, x, <r>)
Description

Returns the probability mass function (pmf) of the hypergeometric distribution. This is the
probability that a hypergeometrically distributed random variable is equal to x. The pmf is
parameterized as follows:
 k  N – k
 x  n – x 
P  X = x ;N n k  = --------------------------- n – x  N – k
 N
 n
Required Arguments

N The population size.
k The number of items in the category of interest.
n The sample size.
x The count of interest, which must be less than or equal to n and k.
Optional Argument

r The odds ratio.
Neg Binomial Distribution(p, n, k)
Description

Returns the cumulative distribution function (cdf) of the negative binomial distribution.
This is the probability that a negative binomially distributed random variable is less than
or equal to k. The cdf is calculated as the summation of the negative binomial pmf for
values of X from 0 to k.

Discrete Probability Functions

Arguments

p The probability of success for each trial. p must be between 0 and 1.
n The number of successes.
k The number of failures before the nth success.
Neg Binomial Probability(p, n, k)
Description

Returns the probability mass function (pmf) of the negative binomial distribution. This is
the probability that a negative binomially distributed random variable is equal to k. The
pmf is parameterized as follows:
P  X = k ;p n  = 


k
n + k – 1 n
p 1 – p

k

Arguments

p The probability of success for each trial. p must be between 0 and 1.
n The number of successes.
k The number of failures before the nth success.
Notes

The return value of the pmf is the probability of observing the nth success after k failures
have occurred.
Poisson Distribution(lambda, k)
Description

Returns the cumulative distribution function (cdf) of the Poisson distribution. This is the
probability that a Poisson distributed random variable with mean lambda is less than or
equal to k. The cdf is calculated as the summation of the Poisson pmf for values of X from 0
to k.
Arguments

k The number of events in a given time interval. k must be an integer.
lambda The shape parameter , which much be greater than 0. This is the mean of the
distribution.
Poisson Probability(lambda, k)
Description

Returns the probability mass function (pmf) of the Poisson distribution. This is the
probability that a Poisson distributed random variable with mean lambda is equal to k.
The pmf is parameterized as follows:
