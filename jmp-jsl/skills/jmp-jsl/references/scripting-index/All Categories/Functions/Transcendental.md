# Transcendental

*Source: [https://jsl.jmp.com/All%20Categories/Functions/Transcendental.html](https://jsl.jmp.com/All%20Categories/Functions/Transcendental.html)*

---

# [Transcendental](#transcendental)[](#transcendental "Click to copy url")

### [Arrhenius](#arrhenius)[](#arrhenius "Click to copy url")

**Syntax:** y = Arrhenius( tempC )

**Description:** Returns the non-specific component of the Arrhenius relationship that is then multiplied by the activation energy in the Arrhenius equation. Returns 11604.5181215503 / (tempC + 273.15).

**JMP Version Added:** Before version 14

``` jsl
Arrhenius( 100 );
```

### [Arrhenius Inv](#arrhenius-inv)[](#arrhenius-inv "Click to copy url")

**Syntax:** tempC = Arrhenius Inv( y )

**Description:** Returns the inverse of the Arrhenius function, which is (11604.5181215503 / y) - 273.15.

**JMP Version Added:** Before version 14

``` jsl
Arrhenius Inv( 100 );
```

### [Beta](#beta)[](#beta "Click to copy url")

**Syntax:** z = Beta( x, y )

**Description:** Returns Beta function of x and y, defined as Gamma( x ) \* Gamma( y ) / Gamma( x + y ).

**JMP Version Added:** Before version 14

``` jsl
Beta( 5, 4 );
```

### [Box Cox Inverse Transform](#box-cox-inverse-transform)[](#box-cox-inverse-transform "Click to copy url")

**Syntax:** x = Box Cox Inverse Transform( y, lambda )

**Description:** Returns the inverse Box-Cox transformation of the argument.

**JMP Version Added:** 19

``` jsl
Box Cox Inverse Transform( 3, 2 );
```

### [Box Cox Transform](#box-cox-transform)[](#box-cox-transform "Click to copy url")

**Syntax:** y = Box Cox Transform( x, lambda )

**Description:** Returns the Box-Cox transformation of the argument.

**JMP Version Added:** 19

``` jsl
Box Cox Transform( 3, 2 );
```

### [Cytometry Logicle](#cytometry-logicle)[](#cytometry-logicle "Click to copy url")

**Syntax:** y = Cytometry Logicle( x, T, W, M, A )

**Description:** Compute cytometry logicle transformation.

**JMP Version Added:** Before version 14

``` jsl
Cytometry Logicle( 100, 10000, .15, .45, 0 );
```

### [Cytometry Logicle Inverse](#cytometry-logicle-inverse)[](#cytometry-logicle-inverse "Click to copy url")

**Syntax:** x = Cytometry Logicle Inverse( y, T, W, M, A )

**Description:** Compute inverse cytometry logicle transformation.

**JMP Version Added:** Before version 14

``` jsl
Cytometry Logicle Inverse( 100, 10000, .15, .45, 0 );
```

### [Digamma](#digamma)[](#digamma "Click to copy url")

**Syntax:** y = Digamma( x )

**Description:** Returns the digamma function evaluated at x, where the digamma function is the derivative of the logarithm of the gamma function.

**JMP Version Added:** Before version 14

``` jsl
Digamma( 5 );
```

### [Exp](#exp)[](#exp "Click to copy url")

**Syntax:** y = Exp( \<x=1\> )

**Description:** Returns e raised to the x power. Argument can be a number, matrix, or list of numbers.

**JMP Version Added:** Before version 14

``` jsl
Round( Exp( 1 ), 5 );
```

### [ExpM1](#expm1)[](#expm1 "Click to copy url")

**Syntax:** y = ExpM1( x )

**Description:** Returns a more accurate calculation of Exp(x)-1 when x is very small.

**JMP Version Added:** Before version 14

``` jsl
Show( ExpM1( 1.1e-18 ), Exp( 1.1e-18 ) - 1 );
```

### [FFT](#fft)[](#fft "Click to copy url")

**Syntax:** ret = FFT( L, \<\<inverse( 0 ), \<\<multivariate( 0 ), \<\<scale( 1.0 ) )

**Description:** Conducts Fast Fourier Transformation (FFT) on argument L, a required list consisting of real and imaginary parts of the data in matrix forms. If L consists of only one matrix, the matrix is considered to be the real part. If L consists of two matrices, the first is the real part, and the second is the imaginary part. The two matrices must have the same dimensions and must have more than one row. There are three optional arguments. The inverse argument determines whether to conduct inverse FFT. The multivariate argument determines whether to conduct spatial or multivariate FFT. The scale argument determines the constant by which the return values should be multiplied. Return value is a list of two matrices with the same dimensions as the first input argument.

**JMP Version Added:** Before version 14

``` jsl
FFT( {[1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 2, 3, 6, 6, 2, 2, 2, 3, 3, 3]} );
A = [1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 2, 3, 6, 6, 2, 2, 2, 3, 3, 3];
res = FFT( {A} );
res = FFT( {A}, <<Inverse( 1 ) );
res = FFT( {A}, <<multivariate( 1 ) );
res = FFT( FFT( {A} ), <<Inverse( 1 ), <<scale( 1 / 20 ) );
B = FFT( {A} );
FFT( B, <<Inverse( 1 ), <<scale( 1 / 20 ) );
Afun = Function( {},
    [1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 2, 3, 6, 6, 2, 2, 2, 3, 3, 3]
);
FFT( FFT( {Afun()} ), <<Inverse( 1 ), <<scale( 1 / 20 ) );
Afun = Function( {},
    {[1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 2, 3, 6, 6, 2, 2, 2, 3, 3, 3]}
);
FFT( FFT( Afun() ), <<Inverse( 1 ), <<scale( 1 / 20 ) );
A = [1 3, 2 4, 3 1, 4 3, 4 5, 5 2, 5 7, 6 9, 7 5, 7 3, 2 7, 3 4, 6 7, 6 4, 2 7, 2 4, 2 6, 3 5,
3 6, 3 1];
res = FFT( {A} );
res = FFT( {A}, <<multivariate( 1 ) );
res = FFT( FFT( {A} ), <<Inverse( 1 ), <<scale( 1 / 40 ) );
res = FFT(
    FFT( {A}, <<multivariate( 1 ) ),
    <<multivariate( 1 ),
    <<Inverse( 1 ),
    <<scale( 1 / 20 )
);
A = [1 3 1,
2 4 3,
3 1 2,
4 3 3,
4 5 9,
5 2 8,
5 7 6,
6 9 5,
7 5 3,
7 3 2,
2 7 1,
3 4 3,
6 7 3,
6 4 2,
2 7 4,
2 4 1,
2 6 5,
3 5 1,
3 6 2,
3 1 9];
res = FFT( {A} );
res = FFT( {A}, <<multivariate( 1 ) );
FFT( FFT( {A} ), <<Inverse( 1 ), <<scale( 1 / 60 ) );
fin = FFT(
    FFT( {A}, <<multivariate( 1 ) ),
    <<Inverse( 1 ),
    <<multivariate( 1 ),
    <<scale( 1 / 20 )
);
Show( fin );
```

### [Factorial](#factorial)[](#factorial "Click to copy url")

**Syntax:** y = Factorial( x )

**Description:** Returns the factorial of x, which is the same as Gamma( x + 1 ). If x is an integer, the result is the product 1 \* 2 \* ... \* x.

**JMP Version Added:** Before version 14

``` jsl
Factorial( 5 );
```

### [Fit Transform To Normal](#fit-transform-to-normal)[](#fit-transform-to-normal "Click to copy url")

**Syntax:** result = Fit Transform To Normal( Distribution(name), Y(vector), \<Freq(vector)\> )

**Description:** Fits a transformation to normality for a vector of data. This includes the Johnson Sl, Johnson Sb, Johnson Su, and GLog distributions. The function returns a list containing parameter estimates, covariance matrix, log-likelihood, AICc, a convergence message, and transformed values.

**JMP Version Added:** Before version 14

``` jsl
datavec = [-3.7975076, 0.48221038, -1.3082712, -1.860647, -6.9470789, -17.237024, -19.470857,
-6.1855986, 2.16525629, -30.990061];
freqvec = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2];
As Table( datavec || freqvec );
Column( 1 ) << set name( "x" );
Column( 2 ) << set name( "freq vec" );
Distribution(
    Freq( :freq vec ),
    Continuous Distribution( Column( :x ), Fit Distribution( GLog ) )
);
results = Fit Transform To Normal( Distribution( "glog" ), Y( datavec ), freq( freqvec ) );
Show( results );
```

### [Gamma](#gamma)[](#gamma "Click to copy url")

**Syntax:** y = Gamma( x, \<limit\> )

**Description:** Returns Gamma function of x, defined as the integral of z^(x-1)\*exp(-z) dz from 0 to ∞. If limit is present, an incomplete Gamma is computed using that limit of integration.

**JMP Version Added:** Before version 14

``` jsl
Gamma( 5 );
```

### [LGamma](#lgamma)[](#lgamma "Click to copy url")

**Syntax:** y = LGamma( x )

**Description:** Returns the natural logarithm of the Gamma function of x. Useful when Gamma(x) is too large to use directly.

**JMP Version Added:** Before version 14

``` jsl
LGamma( 5 );
```

### [Ln](#ln)[](#ln "Click to copy url")

**Syntax:** y = Ln( x )

**Description:** Returns the natural logarithm of x.

**JMP Version Added:** Before version 14

``` jsl
Ln( Exp( 2 ) );
```

### [Log](#log)[](#log "Click to copy url")

**Syntax:** y = Log( x, \<b\> )

**Description:** Returns the base-b logarithm of x or the natural logarithm of x if b is not specified.

**JMP Version Added:** Before version 14

``` jsl
Log( 256, 2 );
```

### [Log10](#log10)[](#log10 "Click to copy url")

**Syntax:** y = Log10( x )

**Description:** Returns the base 10 logarithm of x.

**JMP Version Added:** Before version 14

``` jsl
Log10( 100 );
```

### [Log1P](#log1p)[](#log1p "Click to copy url")

**Syntax:** y = Log1P( x )

**Description:** Returns a more accurate calculation of Log(1 + x) when x is very small.

**JMP Version Added:** Before version 14

``` jsl
Log1P( 1e-6 );
```

### [Logist](#logist)[](#logist "Click to copy url")

**Syntax:** y = Logist( x )

**Description:** Returns 1 / (1 + Exp( -x )), which converts a number in the domain -∞...+∞ into range 0...1. The Logist() function is useful in logistic regression.

**JMP Version Added:** Before version 14

``` jsl
Logist( 2 );
```

### [Logist Percent](#logist-percent)[](#logist-percent "Click to copy url")

**Syntax:** y = Logist Percent( x )

**Description:** Logist function with result scaled 0 to 100.

**JMP Version Added:** Before version 14

``` jsl
Logist Percent( 10 );
```

### [Logit](#logit)[](#logit "Click to copy url")

**Syntax:** y = Logit( p )

**Description:** Returns the logit of p, which is defined as log(p / (1 - p)).

**JMP Version Added:** Before version 14

``` jsl
Logit( 0.95 );
```

### [Logit Percent](#logit-percent)[](#logit-percent "Click to copy url")

**Syntax:** y = Logit Percent( p )

**Description:** Logit function with argument 0 to 100, rather than 0 to 1.

**JMP Version Added:** Before version 14

``` jsl
Logit Percent( 95.0 );
```

### [N Choose K](#n-choose-k)[](#n-choose-k "Click to copy url")

**Syntax:** m = N Choose K( n, k )

**Description:** Returns n! / (k! \* (n - k)!), which is the number of ways to choose k items out of n, ignoring order.

**JMP Version Added:** Before version 14

``` jsl
N Choose K( 5, 3 );
```

### [Power](#power)[](#power "Click to copy url")

**Syntax:** z = x ^ y; z = Power( x, \<y=2\> )

**Description:** Returns x raised to the y power. If x is negative, y must be an integer.

**JMP Version Added:** Before version 14

``` jsl
Power( 2, 5 );
```

### [Root](#root)[](#root "Click to copy url")

**Syntax:** y = Root( x, \<n=2\> )

**Description:** Returns the nth root of x.

**JMP Version Added:** Before version 14

``` jsl
Round( Root( 2, 3 ), 4 ) /* cube root */;
```

### [SHASHInv](#shashinv)[](#shashinv "Click to copy url")

**Syntax:** x = SHASHInv( z, gamma, delta, theta, sigma )

**Description:** Transforms a standard normal variable to a sinh-arcsinh (SHASH) distributed variable.

**JMP Version Added:** 14

``` jsl
gamma = 1;
delta = .5;
theta = -1;
sigma = 2;
x = 3;
result1 = SHASHTrans( x, gamma, delta, theta, sigma );
x1 = SHASHInv( result1, gamma, delta, theta, sigma );
x2 = SinH( (ArcSinH( result1 ) - gamma) / delta ) * sigma + theta;
Show( x1, x2 );
```

### [SHASHTrans](#shashtrans)[](#shashtrans "Click to copy url")

**Syntax:** z = SHASHTrans( x, gamma, delta, theta, sigma )

**Description:** Transforms a sinh-arcsinh (SHASH) distributed variable to a standard normal distributed variable. The SHASH transformation can be used to create more normally distributed data.

**JMP Version Added:** 14

``` jsl
gamma = 1;
delta = .5;
theta = -1;
sigma = 2;
x = 3;
result1 = SHASHTrans( x, gamma, delta, theta, sigma );
result2 = SinH( gamma + delta * ArcSinH( (x - theta) / sigma ) );
Show( result1, result2 );
```

### [SbInv](#sbinv)[](#sbinv "Click to copy url")

**Syntax:** x = SbInv( z, gamma, delta, theta, sigma )

**Description:** Transforms a standard normal variable to a double bounded Johnson variable.

**JMP Version Added:** Before version 14

``` jsl
SbInv( 1.96, 1.5, 2, 1, 2 );
```

### [SbTrans](#sbtrans)[](#sbtrans "Click to copy url")

**Syntax:** z = SbTrans( x, gamma, delta, theta, sigma )

**Description:** Transforms a double bounded Johnson variable to a standard normal variable.

**JMP Version Added:** Before version 14

``` jsl
Round( SbTrans( 2.114, 1.5, 2, 1, 2 ), 2 );
```

### [Scheffe Cubic](#scheffe-cubic)[](#scheffe-cubic "Click to copy url")

**Syntax:** y = Scheffe Cubic( x1, x2 )

**Description:** Evaluates as x1\*x2\*(x1-x2); used to support modeling notation for cubic mixture models.

**JMP Version Added:** Before version 14

``` jsl
Scheffe Cubic( [1, -1, 1, -1, 1], [-1, -1, 1, 1, -1] );
```

### [SlInv](#slinv)[](#slinv "Click to copy url")

**Syntax:** x = SlInv( z, gamma, delta, theta, \<sigma=1\> )

**Description:** Transforms a standard normal variable to a Johnson SL variable.

**JMP Version Added:** Before version 14

``` jsl
SlInv( 1.96, 1.5, 2, 1 );
```

### [SlTrans](#sltrans)[](#sltrans "Click to copy url")

**Syntax:** z = SlTrans( x, gamma, delta, theta, \<sigma=1\> )

**Description:** Transforms a Johnson SL variable to a standard normal variable.

**JMP Version Added:** Before version 14

``` jsl
Round( SlTrans( 2.259, 1.5, 2, 1 ), 2 );
```

### [Sqrt](#sqrt)[](#sqrt "Click to copy url")

**Syntax:** y = Sqrt( x )

**Description:** Returns the positive square root of the x argument, which can be a number, matrix, or list of numbers.

**JMP Version Added:** Before version 14

``` jsl
Round( Sqrt( 2 ), 4 );
```

### [Squash](#squash)[](#squash "Click to copy url")

**Syntax:** y = Squash( x )

**Description:** Returns 1 / (1 + Exp( x )), which converts a number in the domain -∞...+∞ into range 1...0. The Squash() function is useful in logistic regression.

**JMP Version Added:** Before version 14

``` jsl
Squash( 10 );
```

### [Squish](#squish)[](#squish "Click to copy url")

**Syntax:** y = Logist( x )

**Description:** Returns 1 / (1 + Exp( -x )), which converts a number in the domain -∞...+∞ into range 0...1. The Logist() function is useful in logistic regression.

**JMP Version Added:** Before version 14

``` jsl
Logist( 2 );
```

### [SuInv](#suinv)[](#suinv "Click to copy url")

**Syntax:** x = SuInv( z, gamma, delta, theta, sigma )

**Description:** Transforms a standard normal variable to an unbounded Johnson variable.

**JMP Version Added:** Before version 14

``` jsl
SuInv( 1.96, 1.5, 2, 1, 2 );
```

### [SuTrans](#sutrans)[](#sutrans "Click to copy url")

**Syntax:** z = SuTrans( x, gamma, delta, theta, sigma )

**Description:** Transforms an unbounded Johnson variable to a standard normal variable.

**JMP Version Added:** Before version 14

``` jsl
Round( SuTrans( 1.46, 1.5, 2, 1, 2 ), 2 );
```

### [Trigamma](#trigamma)[](#trigamma "Click to copy url")

**Syntax:** y = Trigamma( x )

**Description:** Returns the trigamma function evaluated at x, where the trigamma function is the derivative of the digamma function.

**JMP Version Added:** Before version 14

``` jsl
Trigamma( 5 );
```

[ Previous](Statistical.html "Statistical") [Next ](Trigonometric.html "Trigonometric")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
