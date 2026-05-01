# Probability

*Source: [https://jsl.jmp.com/All%20Categories/Functions/Probability.html](https://jsl.jmp.com/All%20Categories/Functions/Probability.html)*

---

# [Probability](#probability)[](#probability "Click to copy url")

### [Beta Density](#beta-density)[](#beta-density "Click to copy url")

**Syntax:** y = Beta Density( q, alpha, beta, \<theta=0\>, \<sigma=1\> )

**Description:** Returns the density at q for a beta distribution, where q is in the interval theta to theta + sigma, alpha and beta are shape parameters, and theta and sigma are threshold and range parameters, respectively.

**JMP Version Added:** Before version 14

``` jsl
alpha = 0.5;
beta = 0.5;
New Window( "Example: Beta Density",
    y = Graph Box(
        Y Scale( 0, 2.5 ),
        X Scale( 0, 1 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Beta Density( q, alpha, beta ), q );
        Text( {0.55, 2.2}, "\!U03B1=", Round( alpha, 2 ), " \!U03B2=", Round( beta, 2 ) );
    ),
    H List Box( Slider Box( 0, 10, alpha, y << reshow ), Text Box( " \!U03B1" ) ),
    H List Box( Slider Box( 0, 10, beta, y << reshow ), Text Box( " \!U03B2" ) )
);
```

### [Beta Distribution](#beta-distribution)[](#beta-distribution "Click to copy url")

**Syntax:** p = Beta Distribution( q, alpha, beta, \<theta=0\>, \<sigma=1\> )

**Description:** Returns the probability that a beta distributed random variable is less than q, where alpha and beta are shape parameters and theta and sigma are threshold and range parameters, respectively.

**JMP Version Added:** Before version 14

``` jsl
alpha = 0.5;
beta = 0.5;
New Window( "Example: Beta Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 1 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Beta Distribution( q, alpha, beta ), q );
        Text( {0.1, 0.9}, "\!U03B1=", Round( alpha, 2 ), " \!U03B2=", Round( beta, 2 ) );
    ),
    H List Box( Slider Box( 0, 10, alpha, y << reshow ), Text Box( " \!U03B1" ) ),
    H List Box( Slider Box( 0, 10, beta, y << reshow ), Text Box( " \!U03B2" ) )
);
```

### [Beta Quantile](#beta-quantile)[](#beta-quantile "Click to copy url")

**Syntax:** q = Beta Quantile( p, alpha, beta, \<theta=0\>, \<sigma=1\> )

**Description:** Returns the quantile from a Beta distribution, the value for which the probability is p that a random value would be lower, where alpha and beta are shape parameters and theta and sigma are threshold and range parameters, respectively.

**JMP Version Added:** Before version 14

``` jsl
Beta Quantile( 0.95, 2, 5 );
```

### [Cauchy Density](#cauchy-density)[](#cauchy-density "Click to copy url")

**Syntax:** y = Cauchy Density( q, \<center\>, \<scale\> )

**Description:** Returns the density at q of a Cauchy distribution with center mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: Cauchy Density",
    y = Graph Box(
        Y Scale( 0, .4 ),
        X Scale( -6, 6 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Cauchy Density( q ), q );
    )
);
```

### [Cauchy Distribution](#cauchy-distribution)[](#cauchy-distribution "Click to copy url")

**Syntax:** p = Cauchy Distribution( q, \<center\>, \<scale\> )

**Description:** Returns the probability that a Cauchy distributed random variable is less than q.

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: Cauchy Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -6, 6 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Cauchy Distribution( q ), q );
    )
);
```

### [Cauchy Quantile](#cauchy-quantile)[](#cauchy-quantile "Click to copy url")

**Syntax:** q = Cauchy Quantile( p, \<center\>, \<scale\> )

**Description:** Returns the quantile from a Cauchy distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: Cauchy Quantile",
    Graph Box(
        Y Scale( -6, 6 ),
        X Scale( 0, 1 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Cauchy Quantile( p ), p );
    )
);
```

### [ChiSquare Density](#chisquare-density)[](#chisquare-density "Click to copy url")

**Syntax:** p = ChiSquare Density( q, df, \<nonCentrality=0\> )

**Description:** Returns the density at q of a Chi-square distribution with df degrees of freedom.

**JMP Version Added:** Before version 14

``` jsl
cdedf = 2;
New Window( "Example: ChiSquare Density",
    cdey = Graph Box(
        Y Scale( 0, 0.4 ),
        X Scale( 0, 10 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( ChiSquare Density( cdeq, cdedf ), cdeq );
        Text( {7, 0.35}, "df=", Round( cdedf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 0.5, 10, cdedf, cdey << reshow ) )
);
```

### [ChiSquare Distribution](#chisquare-distribution)[](#chisquare-distribution "Click to copy url")

**Syntax:** p = ChiSquare Distribution( q, df, \<nonCentrality=0\> )

**Description:** Returns the probability that a Chi-square distributed random variable is less than q.

**JMP Version Added:** Before version 14

``` jsl
cdidf = 2;
New Window( "Example: ChiSquare Distribution",
    cdiy = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 10 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( ChiSquare Distribution( cdiq, cdidf ), cdiq );
        Text( {1, 0.9}, "df=", Round( cdidf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 0.5, 10, cdidf, cdiy << reshow ) )
);
```

### [ChiSquare Log CDistribution](#chisquare-log-cdistribution)[](#chisquare-log-cdistribution "Click to copy url")

**Syntax:** y = ChiSquare Log CDistribution( x, df, \<nonCentrality=0\> )

**Description:** Returns the log of 1 - Chi-square distribution.

**JMP Version Added:** Before version 14

``` jsl
clcdidf = 2;
New Window( "Example: ChiSquare Log CDistribution",
    clcdiy = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( 0, 10 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( ChiSquare Log CDistribution( clcdiq, clcdidf ), clcdiq );
        Text( {1, -0.9}, "df=", Round( clcdidf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 1, 10, clcdidf, clcdiy << reshow ) )
);
```

### [ChiSquare Log Density](#chisquare-log-density)[](#chisquare-log-density "Click to copy url")

**Syntax:** y = ChiSquare Log Density( x, df, \<nonCentrality=0\> )

**Description:** Returns the log of the Chi-square probability density.

**JMP Version Added:** Before version 14

``` jsl
cldedf = 1;
New Window( "Example: ChiSquare Log Density",
    cldey = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( 0, 10 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( ChiSquare Log Density( cldeq, cldedf ), cldeq );
        Text( {7, -0.35}, "df=", Round( cldedf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 0.5, 10, cldedf, cldey << reshow ) )
);
```

### [ChiSquare Log Distribution](#chisquare-log-distribution)[](#chisquare-log-distribution "Click to copy url")

**Syntax:** y = ChiSquare Log Distribution( x, df, \<nonCentrality=0\> )

**Description:** Returns the log of the Chi-square distribution.

**JMP Version Added:** Before version 14

``` jsl
cldidf = 2;
New Window( "Example: ChiSquare Log Distribution",
    cldiy = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( 0, 10 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( ChiSquare Log Distribution( cldiq, cldidf ), cldiq );
        Text( {1, -0.9}, "df=", Round( cldidf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 1, 10, cldidf, cldiy << reshow ) )
);
```

### [ChiSquare Noncentrality](#chisquare-noncentrality)[](#chisquare-noncentrality "Click to copy url")

**Syntax:** nc = ChiSquare Noncentrality( x, df, prob )

**Description:** Returns the noncentrality parameter nc such that prob is equal to the probability that a Chi-square distributed random variable with df degrees of freedom is less than x.

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: ChiSquare Noncentrality",
    chincgr = Graph Box(
        Y Scale( 0.01, 0.99 ),
        X Scale( 0.01, 0.99 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( ChiSquare Noncentrality( 3, 2, ChiSquare Distribution( 3, 2, q ) ), q );
    )
);
ChiSquare Noncentrality( 3, 2, ChiSquare Distribution( 3, 2, 0.5 ) );
```

### [ChiSquare Quantile](#chisquare-quantile)[](#chisquare-quantile "Click to copy url")

**Syntax:** q = ChiSquare Quantile( p, df, \<nonCentrality=0\> )

**Description:** Returns the quantile from a Chi-Square distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
ChiSquare Quantile( 0.15, 5 );
```

### [Dunnett P value](#dunnett-p-value)[](#dunnett-p-value "Click to copy url")

**Syntax:** p = Dunnett P value( q, nTrt, dfe, \<lambdaVec = .\> )

**Description:** Returns the p-value from Dunnett's multiple comparisons test, where q is the test statistic, nTrt is the number of treatments being compared to the control group, dfe is the error degrees of freedom (based on the total study sample), and the optional lambdaVec is a vector of parameters, which by default are set to 1/sqrt(2).

**JMP Version Added:** Before version 14

``` jsl
Dunnett P value( 1.67623, 3, 11 );
```

### [Dunnett Quantile](#dunnett-quantile)[](#dunnett-quantile "Click to copy url")

**Syntax:** q = Dunnett Quantile( 1-alpha, nTrt, dfe, \<lambdaVec = .\> )

**Description:** Returns the quantile needed in Dunnett's multiple comparisons test, where 1-alpha is the confidence level, nTrt is the number of treatments being compared to the control group, dfe is the error degrees of freedom (based on the total study sample), and the optional lambdaVec is a vector of parameters, which by default are set to 1/sqrt(2).

**JMP Version Added:** Before version 14

``` jsl
Dunnett Quantile( 0.95, 3, 11 );
```

### [ExGaussian Density](#exgaussian-density)[](#exgaussian-density "Click to copy url")

**Syntax:** y = ExGaussian Density( x, location, scale, shape )

**Description:** Returns the density at x of an ExGaussian distribution.

**JMP Version Added:** 18

``` jsl
New Window( "Example: ExGaussian Density",
    y = Graph Box(
        Y Scale( 0, .2 ),
        X Scale( -2, 15 ),
        XName( "x" ),
        Pen Color( "red" );
        Y Function( ExGaussian Density( x, 0, .5, .25 ), x );
    )
);
```

### [ExGaussian Distribution](#exgaussian-distribution)[](#exgaussian-distribution "Click to copy url")

**Syntax:** y = ExGaussian Distribution( x, location, scale, shape )

**Description:** Returns the probability that an ExGaussian distributed random variable is less than x.

**JMP Version Added:** 18

``` jsl
New Window( "Example: ExGaussian Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -2, 15 ),
        XName( "x" ),
        Pen Color( "red" );
        Y Function( ExGaussian Distribution( x, 0, .5, .25 ), x );
    )
);
```

### [ExGaussian Quantile](#exgaussian-quantile)[](#exgaussian-quantile "Click to copy url")

**Syntax:** q = ExGaussian Quantile( p, mu, sigma, lambda )

**Description:** Returns the quantile from an ExGaussian distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** 18

``` jsl
New Window( "Example: ExGaussian Quantile",
    Graph Box(
        Y Scale( -2, 15 ),
        X Scale( 0, 1 ),
        XName( "p" ),
        Pen Color( "red" );
        Y Function( ExGaussian Quantile( p, 0, .5, .25 ), p );
    )
);
```

### [Exp Density](#exp-density)[](#exp-density "Click to copy url")

**Syntax:** y = Exp Density( x, \<theta=1\> )

**Description:** Returns the density at x of an exponential distribution with parameter theta.

**JMP Version Added:** 14

``` jsl
New Window( "Example: Exp Density",
    y = Graph Box(
        Y Scale( 0, 0.45 ),
        X Scale( 0, 4 ),
        XName( "x" ),
        Pen Color( "red" );
        Y Function( Exp Density( x, 2 ), x );
    )
);
```

### [Exp Distribution](#exp-distribution)[](#exp-distribution "Click to copy url")

**Syntax:** p = Exp Distribution( x, \<theta=1\> )

**Description:** Returns the probability that an exponentially distributed random variable is less than x.

**JMP Version Added:** 14

``` jsl
New Window( "Example: Exp Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 4 ),
        XName( "x" ),
        Pen Color( "red" );
        Y Function( Exp Distribution( x, 2 ), x );
    )
);
```

### [Exp Quantile](#exp-quantile)[](#exp-quantile "Click to copy url")

**Syntax:** q = Exp Quantile( p, \<theta=1\> )

**Description:** Returns the quantile from an exponential distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** 14

``` jsl
New Window( "Example: Exp Quantile",
    y = Graph Box(
        Y Scale( 0, 4 ),
        X Scale( 0, 1 ),
        Pen Color( "red" );
        Y Function( Exp Quantile( qq, 2 ), qq );
    )
);
```

### [Exponential Density](#exponential-density)[](#exponential-density "Click to copy url")

**Syntax:** y = Exponential Density( x, \<theta=1\> )

**Description:** Returns the density at x of an exponential distribution with parameter theta.

**JMP Version Added:** 17

``` jsl
New Window( "Example: Exponential Density",
    y = Graph Box(
        Y Scale( 0, 0.45 ),
        X Scale( 0, 4 ),
        XName( "x" ),
        Pen Color( "red" );
        Y Function( Exponential Density( x, 2 ), x );
    )
);
```

### [Exponential Distribution](#exponential-distribution)[](#exponential-distribution "Click to copy url")

**Syntax:** p = Exponential Distribution( x, \<theta=1\> )

**Description:** Returns the probability that an exponentially distributed random variable is less than x.

**JMP Version Added:** 17

``` jsl
New Window( "Example: Exponential Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 4 ),
        XName( "x" ),
        Pen Color( "red" );
        Y Function( Exponential Distribution( x, 2 ), x );
    )
);
```

### [Exponential Quantile](#exponential-quantile)[](#exponential-quantile "Click to copy url")

**Syntax:** q = Exponential Quantile( p, \<theta=1\> )

**Description:** Returns the quantile from an exponential distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** 17

``` jsl
New Window( "Example: Exponential Quantile",
    y = Graph Box(
        Y Scale( 0, 4 ),
        X Scale( 0, 1 ),
        Pen Color( "red" );
        Y Function( Exponential Quantile( qq, 2 ), qq );
    )
);
```

### [F Density](#f-density)[](#f-density "Click to copy url")

**Syntax:** y = F Density( q, dfnum, dfden, \<nonCentrality=0\> )

**Description:** Returns the density at q of an F distribution with dfn and dfd degrees of freedom.

**JMP Version Added:** Before version 14

``` jsl
fdedfn = 2;
fdedfd = 2;
New Window( "Example: F Density",
    fdey = Graph Box(
        Y Scale( 0, 0.8 ),
        X Scale( 0, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( F Density( fdeq, fdedfn, fdedfd ), fdeq );
        Text( {2.5, 0.7}, "dfn=", Round( fdedfn, 2 ), " dfd=", Round( fdedfd, 2 ) );
    ),
    H List Box( Text Box( "dfn " ), Slider Box( 1, 10, fdedfn, fdey << reshow ) ),
    H List Box( Text Box( "dfd " ), Slider Box( 1, 10, fdedfd, fdey << reshow ) )
);
```

### [F Distribution](#f-distribution)[](#f-distribution "Click to copy url")

**Syntax:** y = F Distribution( q, dfnum, dfden, \<nonCentrality=0\> )

**Description:** Returns the probability that an F distributed random variable is less than q.

**JMP Version Added:** Before version 14

``` jsl
fdidfn = 5;
fdidfd = 5;
New Window( "Example: F Distribution",
    fdiy = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 10 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( F Distribution( fdiq, fdidfn, fdidfd ), fdiq );
        Text( {0.5, 0.9}, "dfn=", Round( fdidfn, 2 ), " dfd=", Round( fdidfd, 2 ) );
    ),
    H List Box( Text Box( "dfn " ), Slider Box( 0.5, 10, fdidfn, fdiy << reshow ) ),
    H List Box( Text Box( "dfd " ), Slider Box( 0.5, 10, fdidfd, fdiy << reshow ) )
);
```

### [F Log CDistribution](#f-log-cdistribution)[](#f-log-cdistribution "Click to copy url")

**Syntax:** y = F Log CDistribution( x, dfnum, dfden, \<nonCentrality=0\> )

**Description:** Returns the log of 1 - F Distribution.

**JMP Version Added:** Before version 14

``` jsl
flcddfn = 5;
flcddfd = 5;
New Window( "Example: F Log CDistribution",
    flcdy = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( 0, 10 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( F Log CDistribution( flcdq, flcddfn, flcddfd ), flcdq );
        Text( {0.5, -0.9}, "dfn=", Round( flcddfn, 2 ), " dfd=", Round( flcddfd, 2 ) );
    ),
    H List Box( Text Box( "dfn " ), Slider Box( 1, 10, flcddfn, flcdy << reshow ) ),
    H List Box( Text Box( "dfd " ), Slider Box( 1, 30, flcddfd, flcdy << reshow ) )
);
```

### [F Log Density](#f-log-density)[](#f-log-density "Click to copy url")

**Syntax:** y = F Log Density( x, dfnum, dfden, \<nonCentrality=0\> )

**Description:** Returns the log of the F probability density.

**JMP Version Added:** Before version 14

``` jsl
fldedfn = 1;
fldedfd = 1;
New Window( "Example: F Log Density",
    fldey = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( 0, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( F Log Density( fldeq, fldedfn, fldedfd ), fldeq );
        Text( {2.5, -0.7}, "dfn=", Round( fldedfn, 2 ), " dfd=", Round( fldedfd, 2 ) );
    ),
    H List Box( Text Box( "dfn " ), Slider Box( 1, 10, fldedfn, fldey << reshow ) ),
    H List Box( Text Box( "dfd " ), Slider Box( 1, 10, fldedfd, fldey << reshow ) )
);
```

### [F Log Distribution](#f-log-distribution)[](#f-log-distribution "Click to copy url")

**Syntax:** y = F Log Distribution( x, dfnum, dfden, \<nonCentrality=0\> )

**Description:** Returns the log of the F distribution.

**JMP Version Added:** Before version 14

``` jsl
flddfn = 5;
flddfd = 5;
New Window( "Example: F Log Distribution",
    fldy = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( 0, 10 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( F Log Distribution( fldq, flddfn, flddfd ), fldq );
        Text( {0.5, -0.9}, "dfn=", Round( flddfn, 2 ), " dfd=", Round( flddfd, 2 ) );
    ),
    H List Box( Text Box( "dfn " ), Slider Box( 1, 10, flddfn, fldy << reshow ) ),
    H List Box( Text Box( "dfd " ), Slider Box( 1, 30, flddfd, fldy << reshow ) )
);
```

### [F Noncentrality](#f-noncentrality)[](#f-noncentrality "Click to copy url")

**Syntax:** nc = F Noncentrality( x, dfnum, dfden, prob )

**Description:** Solves for the noncentrality parameter nc such that prob = F Distribution( x, ndf, ddf, nc ).

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: F Noncentrality",
    fncgr = Graph Box(
        Y Scale( 0.01, 0.99 ),
        X Scale( 0.01, 0.99 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( F Noncentrality( 3, 2, 5, F Distribution( 3, 2, 5, q ) ), q );
    )
);
F Noncentrality( 3, 2, 5, F Distribution( 3, 2, 5, 0.4 ) );
```

### [F Power](#f-power)[](#f-power "Click to copy url")

**Syntax:** p = F Power( alpha, dfh, dfm, d, n )

**Description:** Calculates the power of an F Test, where alpha is the significance level, dfh is the hypothesis degrees of freedom, dfm is the degrees of freedom in the whole model, d is the squared effect size, SSH/(n\*sigma^2) where SSH is the sum of squares for the hypothesis, and n is the total number of observations. Note that for the ANOVA model, d = Sum(a\[i\]^2)/(k \* sigma^2) where a\[i\] are effects and k is the number of means.

**JMP Version Added:** Before version 14

``` jsl
alpha = 0.05;
obs = 25;
dfh = 5;
dfm = 5;
d = 1;
New Window( "Example: F Power (alpha=.05,dfh=5,dfm=5)",
    fpdigr = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( 0, 1 ),
        YName( "Power" ),
        XName( "d" ),
        Pen Color( "red" );
        Y Function( F Power( alpha, dfh, dfm, d, obs ), d );
        Text( {0.75, 0.1}, "obs=", Round( obs ) );
    ),
    H List Box( Text Box( "obs" ), Slider Box( 10, 100, obs, fpdigr << reshow ) )
);
```

### [F Quantile](#f-quantile)[](#f-quantile "Click to copy url")

**Syntax:** q = F Quantile( p, dfnum, dfden, \<nonCentrality=0\> )

**Description:** Returns the quantile from an F distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
F Quantile( 0.7, 5, 3 );
```

### [F Sample Size](#f-sample-size)[](#f-sample-size "Click to copy url")

**Syntax:** n = F Sample Size( alpha, dfh, dfm, d, power )

**Description:** Calculates the sample size, where alpha is the significance level, dfh is the hypothesis degrees of freedom, dfm is the degrees of freedom in the whole model, d is the squared effect size, SSH/(n\*sigma^2) where SSH is the sum of squares for the hypothesis, and power is the power desired. Note that for the ANOVA model, d = Sum(a\[i\]^2)/(k \* sigma^2) where a\[i\] are effects and k is the number of means.

**JMP Version Added:** Before version 14

``` jsl
alpha = 0.05;
pow = 0.6;
dfh = 5;
dfm = 5;
d = 1;
New Window( "Example: F Sample Size (alpha=.05,dfh=5,dfm=5)",
    fpdigr = Graph Box(
        Y Scale( 0, 50 ),
        X Scale( 0.5, 5 ),
        YName( "Sample Size" ),
        XName( "d" ),
        Pen Color( "red" );
        Y Function( F Sample Size( alpha, dfh, dfm, d, pow ), d );
        Text( {0.75, 0.2}, "power=", Round( pow, 2 ) );
    ),
    H List Box( Text Box( "power" ), Slider Box( 0.2, 0.95, pow, fpdigr << reshow ) )
);
```

### [FDR Adjust](#fdr-adjust)[](#fdr-adjust "Click to copy url")

**Syntax:** y = FDR Adjust( matrix )

**Description:** Returns the false discovery rate adjustment for the specified p-values using the Benjamini-Hochberg method.

**JMP Version Added:** 19

``` jsl
FDR Adjust( [0.5, 0.2, 0.05, 0.01] );
```

### [Frechet Density](#frechet-density)[](#frechet-density "Click to copy url")

**Syntax:** y = Frechet Density( x, mu, sigma )

**Description:** Returns the density at x of a Fréchet distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = .5;
New Window( "Example: Frechet Density",
    y = Graph Box(
        Y Scale( 0, .06 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( Frechet Density( x, mu, sig ), x );
        Text( {0, .055}, "mu=", Round( mu, 2 ) );
        Text( {0, .045}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 4, mu, y << reshow ), Text Box( "mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( "sig" ) ), 

);
```

### [Frechet Distribution](#frechet-distribution)[](#frechet-distribution "Click to copy url")

**Syntax:** p = Frechet Distribution( x, mu, sigma )

**Description:** Returns the probability at x of a Fréchet distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = .5;
New Window( "Example: Frechet Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( Frechet Distribution( x, mu, sig ), x );
        Text( {0.1, 0.9}, "mu=", Round( mu, 2 ) );
        Text( {0.1, 0.8}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 4, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( " sig" ) )
);
```

### [Frechet Quantile](#frechet-quantile)[](#frechet-quantile "Click to copy url")

**Syntax:** q = Frechet Quantile( p, mu, sigma )

**Description:** Returns the quantile at p of a Fréchet distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = .5;
qq = .5;
New Window( "Example: Frechet Quantile",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( Frechet Distribution( qq, mu, sig ), qq );
        Pen Color( "blue" );
        V Line( Frechet Quantile( qq, mu, sig ), 0, 1 );
        Text(
            {0.1, 0.9},
            " mu=",
            Round( mu, 2 ),
            " sig=",
            Round( sig, 2 ),
            " quantile=",
            Round( qq, 2 )
        );
    ),
    H List Box( Slider Box( 0, 4, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( " sig" ) ),
    H List Box( Slider Box( 0.01, 0.99, qq, y << reshow ), Text Box( " quantile" ) )
);
```

### [GLog Density](#glog-density)[](#glog-density "Click to copy url")

**Syntax:** y = GLog Density( q, mu, sigma, lambda )

**Description:** Returns the density at q of a generalized logarithm distribution with location mu, scale sigma, and shape lambda.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sigma = 1;
lambda = 1;
New Window( "Example: GLog Density",
    gdey = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -10, 10 ),
        XName( "y" ),
        Pen Color( "red" );
        Y Function( GLog Density( y, mu, sigma, lambda ), y );
        Text( {-9, 0.9}, "\!U03BC=", Round( mu, 4 ), " \!U03C3=", Round( sigma, 4 ) );
        Text( {-9, 0.8}, "\!U03BB=", Round( lambda, 4 ) );
    ),
    H List Box( Slider Box( -5, 5, mu, gdey << reshow ), Text Box( " \!U03BC" ) ),
    H List Box( Slider Box( 0, 4, sigma, gdey << reshow ), Text Box( " \!U03C3" ) ),
    H List Box( Slider Box( 0, 10, lambda, gdey << reshow ), Text Box( " \!U03BB" ) )
);
```

### [GLog Distribution](#glog-distribution)[](#glog-distribution "Click to copy url")

**Syntax:** p = GLog Distribution( q, mu, sigma, lambda )

**Description:** Returns the probability that a generalized logarithm distributed random variable is less than q.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sigma = 1;
lambda = 1;
New Window( "Example: Glog Distribution",
    gdey = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -20, 20 ),
        XName( "y" ),
        Pen Color( "red" );
        Y Function( GLog Distribution( y, mu, sigma, lambda ), y );
        Text( {-9, 0.9}, "\!U03BC=", Round( mu, 4 ), " \!U03C3=", Round( sigma, 4 ) );
        Text( {-9, 0.8}, "\!U03BB=", Round( lambda, 4 ) );
    ),
    H List Box( Slider Box( -5, 5, mu, gdey << reshow ), Text Box( " \!U03BC" ) ),
    H List Box( Slider Box( 0, 4, sigma, gdey << reshow ), Text Box( " \!U03C3" ) ),
    H List Box( Slider Box( 0, 10, lambda, gdey << reshow ), Text Box( " \!U03BB" ) )
);
```

### [GLog Quantile](#glog-quantile)[](#glog-quantile "Click to copy url")

**Syntax:** q = GLog Quantile( p, mu, sigma, lambda )

**Description:** Returns the quantile from a generalized logarithm distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sigma = 1;
lambda = 1;
p = 0.4;
New Window( "Example: GLog Quantile",
    gdey = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -20, 20 ),
        XName( "y" ),
        Pen Color( "red" );
        Y Function( GLog Distribution( x, mu, sigma, lambda ), x );
        Pen Color( "Blue" );
        V Line( GLog Quantile( p, mu, sigma, lambda ), 0, 1 );
        Text(
            {-9, 0.9},
            "\!U03BC=",
            Round( mu, 4 ),
            " \!U03C3=",
            Round( sigma, 4 ),
            " \!U03BB=",
            Round( lambda, 4 )
        );
        Text( {-9, 0.8}, "p=", Round( p, 3 ) );
        Text( {-9, 0.7}, "quantile= ", Round( GLog Quantile( p, mu, sigma, lambda ), 2 ) );
    ),
    H List Box( Slider Box( -2, 2, mu, gdey << reshow ), Text Box( " \!U03BC" ) ),
    H List Box( Slider Box( 0, 4, sigma, gdey << reshow ), Text Box( " \!U03C3" ) ),
    H List Box( Slider Box( 0, 10, lambda, gdey << reshow ), Text Box( " \!U03BB" ) ),
    H List Box( Slider Box( 0.01, 0.99, p, gdey << reshow ), Text Box( " p" ) )
);
```

### [Gamma Density](#gamma-density)[](#gamma-density "Click to copy url")

**Syntax:** y = Gamma Density( q, \<alpha=1\>, \<scale=1\>, \<threshold=0\> )

**Description:** Returns the density at q of a Gamma probability distribution, where the alpha shape parameter argument must be positive.

**JMP Version Added:** Before version 14

``` jsl
gdealpha = Log( 1.5 );
New Window( "Example: Gamma Density",
    gdey = Graph Box(
        Y Scale( 0, 0.5 ),
        X Scale( 0, 12 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Gamma Density( gdeq, Exp( gdealpha ) ), gdeq );
        Text( {9, 0.45}, "\!U03B1=", Round( Exp( gdealpha ), 2 ) );
    ),
    H List Box(
        Slider Box( Log( 0.1 ), Log( 12 ), gdealpha, gdey << reshow ),
        Text Box( " \!U03B1" )
    )
);
```

### [Gamma Distribution](#gamma-distribution)[](#gamma-distribution "Click to copy url")

**Syntax:** p = Gamma Distribution( q, \<alpha=1\>, \<scale=1\>, \<threshold=0\> )

**Description:** Returns the probability that a Gamma distributed random variable is less than q, where the alpha shape parameter argument must be positive. IGamma() is an alias name to Gamma Distribution(). The Gamma Distribution() function is equivalent to Gamma(alpha,q)/Gamma(alpha).

**JMP Version Added:** Before version 14

``` jsl
gdialpha = Log( 1.5 );
New Window( "Example: Gamma Distribution",
    gdiy = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 12 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Gamma Distribution( gdiq, Exp( gdialpha ) ), gdiq );
        Text( {1, 0.9}, "\!U03B1=", Round( Exp( gdialpha ), 2 ) );
    ),
    H List Box(
        Slider Box( Log( 0.1 ), Log( 12 ), gdialpha, gdiy << reshow ),
        Text Box( " \!U03B1" )
    )
);
```

### [Gamma Log CDistribution](#gamma-log-cdistribution)[](#gamma-log-cdistribution "Click to copy url")

**Syntax:** p = Gamma Log CDistribution( x, \<alpha=1\>, \<scale=1\>, \<threshold=0\> )

**Description:** Returns the log of 1 - Gamma distribution.

**JMP Version Added:** Before version 14

``` jsl
glcdialpha = Log( 1.5 );
New Window( "Example: Gamma Log CDistribution",
    glcdiy = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( 0, 12 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Gamma Log CDistribution( glcdiq, Exp( glcdialpha ) ), glcdiq );
        Text( {1, -0.9}, "\!U03B1=", Round( Exp( glcdialpha ), 2 ) );
    ),
    H List Box(
        Slider Box( Log( 0.1 ), Log( 12 ), glcdialpha, glcdiy << reshow ),
        Text Box( " \!U03B1" )
    )
);
```

### [Gamma Log Density](#gamma-log-density)[](#gamma-log-density "Click to copy url")

**Syntax:** y = Gamma Log Density( x, \<alpha=1\>, \<scale=1\>, \<threshold=0\> )

**Description:** Returns the log of the Gamma probability density.

**JMP Version Added:** Before version 14

``` jsl
gldealpha = Log( 1.5 );
New Window( "Example: Gamma Log Density",
    gldey = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( 0, 12 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Gamma Log Density( gldeq, Exp( gldealpha ) ), gldeq );
        Text( {9, -0.45}, "\!U03B1=", Round( Exp( gldealpha ), 2 ) );
    ),
    H List Box(
        Slider Box( Log( 0.1 ), Log( 12 ), gldealpha, gldey << reshow ),
        Text Box( " \!U03B1" )
    )
);
```

### [Gamma Log Distribution](#gamma-log-distribution)[](#gamma-log-distribution "Click to copy url")

**Syntax:** p = Gamma Log Distribution( x, \<alpha=1\>, \<scale=1\>, \<threshold=0\> )

**Description:** Returns the log of the Gamma distribution.

**JMP Version Added:** Before version 14

``` jsl
gldialpha = Log( 1.5 );
New Window( "Example: Gamma Log Distribution",
    gldiy = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( 0, 12 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Gamma Log Distribution( gldiq, Exp( gldialpha ) ), gldiq );
        Text( {1, -0.9}, "\!U03B1=", Round( Exp( gldialpha ), 2 ) );
    ),
    H List Box(
        Slider Box( Log( 0.1 ), Log( 12 ), gldialpha, gldiy << reshow ),
        Text Box( " \!U03B1" )
    )
);
```

### [Gamma Quantile](#gamma-quantile)[](#gamma-quantile "Click to copy url")

**Syntax:** q = Gamma Quantile( p, \<alpha=1\>, \<scale=1\>, \<threshold=0\> )

**Description:** Returns the quantile from a Gamma distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
Gamma Quantile( 0.75, 4 );
```

### [GenGamma Density](#gengamma-density)[](#gengamma-density "Click to copy url")

**Syntax:** y = GenGamma Density( x, mu, sigma, lambda )

**Description:** Returns the density at x of an extended generalized gamma probability distribution with parameters mu, sigma, and lambda.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sigma = 1;
lambda = 1;
New Window( "Example: GenGamma Density",
    gdey = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -5, 10 ),
        XName( "y" ),
        Pen Color( "red" );
        Y Function( GenGamma Density( y, mu, sigma, lambda ), y );
        Text( {-4, 0.9}, "\!U03BC=", Round( mu, 4 ), " \!U03C3=", Round( sigma, 4 ) );
        Text( {-4, 0.8}, "\!U03BB=", Round( lambda, 4 ) );
    ),
    H List Box( Slider Box( -5, 5, mu, gdey << reshow ), Text Box( "\!U03BC" ) ),
    H List Box( Slider Box( 0, 4, sigma, gdey << reshow ), Text Box( "\!U03C3" ) ),
    H List Box( Slider Box( 0, 10, lambda, gdey << reshow ), Text Box( "\!U03BB" ) )
);
```

### [GenGamma Distribution](#gengamma-distribution)[](#gengamma-distribution "Click to copy url")

**Syntax:** p = GenGamma Distribution( x, mu, sigma, lambda )

**Description:** Returns the probability that an extended generalized gamma distributed random variable (with parameters mu, sigma, and lambda) is less than x.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sigma = 1;
lambda = 1;
New Window( "Example: GenGamma Distribution",
    gdey = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -10, 20 ),
        XName( "y" ),
        Pen Color( "red" );
        Y Function( GenGamma Distribution( y, mu, sigma, lambda ), y );
        Text( {-9, 0.9}, "\!U03BC=", Round( mu, 4 ), " \!U03C3=", Round( sigma, 4 ) );
        Text( {-9, 0.8}, "\!U03BB=", Round( lambda, 4 ) );
    ),
    H List Box( Slider Box( -5, 5, mu, gdey << reshow ), Text Box( "\!U03BC" ) ),
    H List Box( Slider Box( 0, 4, sigma, gdey << reshow ), Text Box( "\!U03C3" ) ),
    H List Box( Slider Box( 0, 10, lambda, gdey << reshow ), Text Box( "\!U03BB" ) )
);
```

### [GenGamma Quantile](#gengamma-quantile)[](#gengamma-quantile "Click to copy url")

**Syntax:** q = GenGamma Quantile( p, mu, sigma, lambda )

**Description:** Returns the quantile from an extended generalized gamma distribution (with parameters mu, sigma, and lambda), the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sigma = 1;
lambda = 1;
p = 0.4;
New Window( "Example: GenGamma Quantile",
    gdey = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -10, 20 ),
        XName( "y" ),
        Pen Color( "red" );
        Y Function( GenGamma Distribution( x, mu, sigma, lambda ), x );
        Pen Color( "Blue" );
        V Line( GenGamma Quantile( p, mu, sigma, lambda ), 0, 1 );
        Text(
            {-9, 0.9},
            "\!U03BC=",
            Round( mu, 4 ),
            " \!U03C3=",
            Round( sigma, 4 ),
            " \!U03BB=",
            Round( lambda, 4 )
        );
        Text( {-9, 0.8}, "p=", Round( p, 3 ) );
        Text(
            {-9, 0.7},
            "quantile= ",
            Round( GenGamma Quantile( p, mu, sigma, lambda ), 2 )
        );
    ),
    H List Box( Slider Box( -2, 2, mu, gdey << reshow ), Text Box( "\!U03BC" ) ),
    H List Box( Slider Box( 0, 4, sigma, gdey << reshow ), Text Box( "\!U03C3" ) ),
    H List Box( Slider Box( 0, 10, lambda, gdey << reshow ), Text Box( "\!U03BB" ) ),
    H List Box( Slider Box( 0.01, 0.99, p, gdey << reshow ), Text Box( " p" ) )
);
```

### [IGamma](#igamma)[](#igamma "Click to copy url")

**Syntax:** p = Gamma Distribution( q, \<alpha=1\>, \<scale=1\>, \<threshold=0\> )

**Description:** Returns the probability that a Gamma distributed random variable is less than q, where the alpha shape parameter argument must be positive. IGamma() is an alias name to Gamma Distribution(). The Gamma Distribution() function is equivalent to Gamma(alpha,q)/Gamma(alpha).

**JMP Version Added:** Before version 14

``` jsl
gdialpha = Log( 1.5 );
New Window( "Example: Gamma Distribution",
    gdiy = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 12 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Gamma Distribution( gdiq, Exp( gdialpha ) ), gdiq );
        Text( {1, 0.9}, "\!U03B1=", Round( Exp( gdialpha ), 2 ) );
    ),
    H List Box(
        Slider Box( Log( 0.1 ), Log( 12 ), gdialpha, gdiy << reshow ),
        Text Box( " \!U03B1" )
    )
);
```

### [Johnson Sb Density](#johnson-sb-density)[](#johnson-sb-density "Click to copy url")

**Syntax:** y = Johnson Sb Density( q, gamma, delta, theta, sigma )

**Description:** Returns the density at q of a Johnson Sb distribution, where q is in the interval theta to theta + sigma, delta\>0 and gamma between -∞ and +∞ are shape parameters, sigma\>0 is a scale parameter, and theta between -∞ and +∞ is a threshold parameter. Note: theta is the lower endpoint of the distribution and sigma is the range of the support of the distribution.

**JMP Version Added:** Before version 14

``` jsl
gamma = 0.5;
delta = 0.5;
theta = 0.5;
sigma = 1;
New Window( "Example: Johnson Sb Density",
    jsbp = Graph Box(
        Y Scale( 0, 5.5 ),
        X Scale( 0.2, 1.8 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Johnson Sb Density( q, gamma, delta, theta, sigma ), q );
        Text(
            {0.5, 4.5},
            "\!U03B3=",
            Round( gamma, 2 ),
            " \!U03B4=",
            Round( delta, 2 ),
            " \!U03B8=",
            Round( theta, 2 ),
            " \!U03C3=",
            Round( sigma, 2 )
        );
    ),
    H List Box( Slider Box( 0, 1, gamma, jsbp << reshow ), Text Box( " \!U03B3" ) ),
    H List Box( Slider Box( 0, 2, delta, jsbp << reshow ), Text Box( " \!U03B4" ) ),
    H List Box( Slider Box( -2, 2, theta, jsbp << reshow ), Text Box( " \!U03B8" ) ),
    H List Box( Slider Box( 0, 10, sigma, jsbp << reshow ), Text Box( " \!U03C3" ) )
);
```

### [Johnson Sb Distribution](#johnson-sb-distribution)[](#johnson-sb-distribution "Click to copy url")

**Syntax:** p = Johnson Sb Distribution( q, gamma, delta, theta, sigma )

**Description:** Returns the probability that a Johnson Sb distributed random variable is less than q. (Note: see the Johnson Sb Density() function for parameter descriptions.)

**JMP Version Added:** Before version 14

``` jsl
gamma = 0.5;
delta = 0.5;
theta = 0.5;
sigma = 3;
New Window( "Example: Johnson Sb Distribution",
    jsbc = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0.2, 3.8 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Johnson Sb Distribution( q, gamma, delta, theta, sigma ), q );
        Text(
            {0.3, 0.8},
            "\!U03B3=",
            Round( gamma, 2 ),
            " \!U03B4=",
            Round( delta, 2 ),
            " \!U03B8=",
            Round( theta, 2 ),
            " \!U03C3=",
            Round( sigma, 2 )
        );
    ),
    H List Box( Slider Box( 0, 1, gamma, jsbc << reshow ), Text Box( " \!U03B3" ) ),
    H List Box( Slider Box( 0, 1, delta, jsbc << reshow ), Text Box( " \!U03B4" ) ),
    H List Box( Slider Box( 0, 1, theta, jsbc << reshow ), Text Box( " \!U03B8" ) ),
    H List Box( Slider Box( 0, 4, sigma, jsbc << reshow ), Text Box( " \!U03C3" ) )
);
```

### [Johnson Sb Quantile](#johnson-sb-quantile)[](#johnson-sb-quantile "Click to copy url")

**Syntax:** q = Johnson Sb Quantile( p, gamma, delta, theta, sigma )

**Description:** Returns the quantile from a Johnson Sb distribution, the value for which the probability is p that a random value would be lower. (Note: p is the first parameter. See the Johnson Sb Density() function for parameter descriptions.)

**JMP Version Added:** Before version 14

``` jsl
Johnson Sb Quantile( 0.5, 0.5, 1, 1, 1 );
```

### [Johnson Sl Density](#johnson-sl-density)[](#johnson-sl-density "Click to copy url")

**Syntax:** y = Johnson Sl Density( q, gamma, delta, theta, \<sigma=1\> )

**Description:** Returns the density at q of a Johnson Sl distribution, where q is in the interval theta to +∞, delta\>0 and gamma between -∞ and +∞ are shape parameters, sigma equal to +1 or -1 is a scale parameter, and theta between -∞ and +∞ is a threshold parameter. Note: When sigma = 1, theta is the lower bound on the distribution, and when sigma=-1, theta is the upper bound. Also, positive sigma implies positive skew, and negative sigma implies negative skew.

**JMP Version Added:** Before version 14

``` jsl
gamma = 0.5;
delta = 1;
theta = 0;
sigma = 1;
New Window( "Example: Johnson Sl Density",
    jslp = Graph Box(
        Y Scale( 0, 1.5 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Johnson Sl Density( q, gamma, delta, theta, sigma ), q );
        Text(
            {-1, 1.1},
            "\!U03B3=",
            Round( gamma, 2 ),
            " \!U03B4=",
            Round( delta, 2 ),
            " \!U03B8=",
            Round( theta, 2 )
        );
    ),
    jslpcb = Check Box(
        {"\!U03C3 = +1 (Note: When unchecked \!U03C3 = -1)"},
        <<set( 1 ),
        sigma = [-1, 1][((jslpcb << get()) + 1)];
        jslp << reshow;
    ),
    H List Box( Slider Box( -15, 15, gamma, jslp << reshow ), Text Box( " \!U03B3" ) ),
    H List Box( Slider Box( 0, 10, delta, jslp << reshow ), Text Box( " \!U03B4" ) ),
    H List Box( Slider Box( -5, 5, theta, jslp << reshow ), Text Box( " \!U03B8" ) )
);
```

### [Johnson Sl Distribution](#johnson-sl-distribution)[](#johnson-sl-distribution "Click to copy url")

**Syntax:** p = Johnson Sl Distribution( q, gamma, delta, theta, \<sigma=1\> )

**Description:** Returns the probability that a Johnson Sl distributed random variable is less than q. (Note: see the Johnson Sl Density() function for parameter descriptions.)

**JMP Version Added:** Before version 14

``` jsl
gamma = 0.5;
delta = 1;
theta = 0;
sigma = 1;
New Window( "Example: Johnson Sl Distribution",
    jslc = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Johnson Sl Distribution( q, gamma, delta, theta, sigma ), q );
        Text(
            {-1, 0.9},
            "\!U03B3=",
            Round( gamma, 2 ),
            " \!U03B4=",
            Round( delta, 2 ),
            " \!U03B8=",
            Round( theta, 2 )
        );
    ),
    jslccb = Check Box(
        {"\!U03C3 = +1 (Note: When unchecked \!U03C3 = -1)"},
        <<set( 1 ),
        sigma = [-1, 1][((jslccb << get()) + 1)];
        jslc << reshow;
    ),
    H List Box( Slider Box( -15, 15, gamma, jslc << reshow ), Text Box( " \!U03B3" ) ),
    H List Box( Slider Box( 0, 10, delta, jslc << reshow ), Text Box( " \!U03B4" ) ),
    H List Box( Slider Box( -5, 5, theta, jslc << reshow ), Text Box( " \!U03B8" ) )
);
```

### [Johnson Sl Quantile](#johnson-sl-quantile)[](#johnson-sl-quantile "Click to copy url")

**Syntax:** q = Johnson Sl Quantile( p, gamma, delta, theta, \<sigma=1\> )

**Description:** Returns the quantile from a Johnson Sl distribution, the value for which the probability is p that a random value would be lower. (Note: p is the first parameter. See the Johnson Sl Density() function for parameter descriptions.)

**JMP Version Added:** Before version 14

``` jsl
Johnson Sl Quantile( 0.5, 0.5, 1, 1, 1 );
```

### [Johnson Su Density](#johnson-su-density)[](#johnson-su-density "Click to copy url")

**Syntax:** y = Johnson Su Density( q, gamma, delta, theta, sigma )

**Description:** Returns the density at q of a Johnson Su distribution, where q is between -∞ and +∞, delta\>0 and gamma between -∞ and +∞ are shape parameters, sigma\>0 is a scale parameter, and theta between -∞ and +∞ is a threshold parameter.

**JMP Version Added:** Before version 14

``` jsl
gamma = 0.5;
delta = 1;
theta = 1;
sigma = 1;
New Window( "Example: Johnson Su Density",
    y = Graph Box(
        Y Scale( 0, 1.5 ),
        X Scale( -2, 2 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Johnson Su Density( q, gamma, delta, theta, sigma ), q );
        Text(
            {-1, 1.3},
            "\!U03B3=",
            Round( gamma, 2 ),
            " \!U03B4=",
            Round( delta, 2 ),
            " \!U03B8=",
            Round( theta, 2 ),
            " \!U03C3=",
            Round( sigma, 2 )
        );
    ),
    H List Box( Slider Box( 0, 1, gamma, y << reshow ), Text Box( " \!U03B3" ) ),
    H List Box( Slider Box( 0, 2, delta, y << reshow ), Text Box( " \!U03B4" ) ),
    H List Box( Slider Box( 0, 2, theta, y << reshow ), Text Box( " \!U03B8" ) ),
    H List Box( Slider Box( 0, 2, sigma, y << reshow ), Text Box( " \!U03C3" ) )
);
```

### [Johnson Su Distribution](#johnson-su-distribution)[](#johnson-su-distribution "Click to copy url")

**Syntax:** p = Johnson Su Distribution( q, gamma, delta, theta, sigma )

**Description:** Returns the probability that a Johnson Su distributed random variable is less than q. (Note: see the Johnson Su Density() function for parameter descriptions.)

**JMP Version Added:** Before version 14

``` jsl
gamma = 0.5;
delta = 1;
theta = 1;
sigma = 1;
New Window( "Example: Johnson Su Distribution",
    jsuc = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -2, 2 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Johnson Su Distribution( q, gamma, delta, theta, sigma ), q );
        Text(
            {-1, 0.9},
            "\!U03B3=",
            Round( gamma, 2 ),
            " \!U03B4=",
            Round( delta, 2 ),
            " \!U03B8=",
            Round( theta, 2 ),
            " \!U03C3=",
            Round( sigma, 2 )
        );
    ),
    H List Box( Slider Box( 0, 1, gamma, jsuc << reshow ), Text Box( " \!U03B3" ) ),
    H List Box( Slider Box( 0, 2, delta, jsuc << reshow ), Text Box( " \!U03B4" ) ),
    H List Box( Slider Box( 0, 2, theta, jsuc << reshow ), Text Box( " \!U03B8" ) ),
    H List Box( Slider Box( 0, 2, sigma, jsuc << reshow ), Text Box( " \!U03C3" ) )
);
```

### [Johnson Su Quantile](#johnson-su-quantile)[](#johnson-su-quantile "Click to copy url")

**Syntax:** q = Johnson Su Quantile( p, gamma, delta, theta, sigma )

**Description:** Returns the quantile from a Johnson Su distribution, the value for which the probability is p that a random value would be lower. (Note: p is the first parameter. See the Johnson Su Density() function for parameter descriptions.)

**JMP Version Added:** Before version 14

``` jsl
Johnson Su Quantile( 0.5, 0.5, 1, 1, 1 );
```

### [LEV Density](#lev-density)[](#lev-density "Click to copy url")

**Syntax:** y = LEV Density( x, mu, sigma )

**Description:** Returns the density at x of a largest extreme distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 10;
sig = 5;
New Window( "Example: LEV Density",
    y = Graph Box(
        Y Scale( 0, .08 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( LEV Density( x, mu, sig ), x );
        Text( {0, .055}, "mu=", Round( mu, 2 ) );
        Text( {0, .045}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 100, mu, y << reshow ), Text Box( "mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( "sig" ) ), 

);
```

### [LEV Distribution](#lev-distribution)[](#lev-distribution "Click to copy url")

**Syntax:** p = LEV Distribution( x, mu, sigma )

**Description:** Returns the probability at x of a largest extreme distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 10;
sig = 5;
New Window( "Example: LEV Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( LEV Distribution( x, mu, sig ), x );
        Text( {0.1, 0.9}, "mu=", Round( mu, 2 ) );
        Text( {0.1, 0.8}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 100, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( " sig" ) )
);
```

### [LEV Quantile](#lev-quantile)[](#lev-quantile "Click to copy url")

**Syntax:** q = LEV Quantile( p, mu, sigma )

**Description:** Returns the quantile at p of a largest extreme distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 10;
sig = 5;
qq = .5;
New Window( "Example: LEV Quantile",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( LEV Distribution( qq, mu, sig ), qq );
        Pen Color( "blue" );
        V Line( LEV Quantile( qq, mu, sig ), 0, 1 );
        Text(
            {0.1, 0.9},
            " mu=",
            Round( mu, 2 ),
            " sig=",
            Round( sig, 2 ),
            " quantile=",
            Round( qq, 2 )
        );
    ),
    H List Box( Slider Box( 0, 80, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( " sig" ) ),
    H List Box( Slider Box( 0.01, 0.99, qq, y << reshow ), Text Box( " quantile" ) )
);
```

### [LogGenGamma Density](#loggengamma-density)[](#loggengamma-density "Click to copy url")

**Syntax:** y = LogGenGamma Density( x, mu, sigma, lambda )

**Description:** Returns the density at x of a log generalized gamma probability distribution with parameters mu, sigma, and lambda.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sigma = 1;
lambda = 1;
New Window( "Example: LogGenGamma Density",
    gdey = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -10, 10 ),
        XName( "y" ),
        Pen Color( "red" );
        Y Function( LogGenGamma Density( y, mu, sigma, lambda ), y );
        Text( {-9, 0.9}, "\!U03BC=", Round( mu, 4 ), " \!U03C3=", Round( sigma, 4 ) );
        Text( {-9, 0.8}, "\!U03BB=", Round( lambda, 4 ) );
    ),
    H List Box( Slider Box( -5, 5, mu, gdey << reshow ), Text Box( "\!U03BC" ) ),
    H List Box( Slider Box( 0, 4, sigma, gdey << reshow ), Text Box( "\!U03C3" ) ),
    H List Box( Slider Box( 0, 10, lambda, gdey << reshow ), Text Box( "\!U03BB" ) )
);
```

### [LogGenGamma Distribution](#loggengamma-distribution)[](#loggengamma-distribution "Click to copy url")

**Syntax:** p = LogGenGamma Distribution( x, mu, sigma, lambda )

**Description:** Returns the probability that a log generalized gamma distributed random variable (with parameters mu, sigma, and lambda) is less than x.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sigma = 1;
lambda = 1;
New Window( "Example: LogGenGamma Distribution",
    gdey = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -20, 20 ),
        XName( "y" ),
        Pen Color( "red" );
        Y Function( LogGenGamma Distribution( y, mu, sigma, lambda ), y );
        Text( {-9, 0.9}, "\!U03BC=", Round( mu, 4 ), " \!U03C3=", Round( sigma, 4 ) );
        Text( {-9, 0.8}, "\!U03BB=", Round( lambda, 4 ) );
    ),
    H List Box( Slider Box( -5, 5, mu, gdey << reshow ), Text Box( "\!U03BC" ) ),
    H List Box( Slider Box( 0, 4, sigma, gdey << reshow ), Text Box( "\!U03C3" ) ),
    H List Box( Slider Box( 0, 10, lambda, gdey << reshow ), Text Box( "\!U03BB" ) )
);
```

### [LogGenGamma Quantile](#loggengamma-quantile)[](#loggengamma-quantile "Click to copy url")

**Syntax:** q = LogGenGamma Quantile( p, mu, sigma, lambda )

**Description:** Returns the quantile from a log generalized gamma distribution (with parameters mu, sigma, and lambda), the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sigma = 1;
lambda = 1;
p = 0.4;
New Window( "Example: LogGenGamma Quantile",
    gdey = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -20, 20 ),
        XName( "y" ),
        Pen Color( "red" );
        Y Function( LogGenGamma Distribution( x, mu, sigma, lambda ), x );
        Pen Color( "Blue" );
        V Line( LogGenGamma Quantile( p, mu, sigma, lambda ), 0, 1 );
        Text(
            {-19, 0.9},
            "\!U03BC=",
            Round( mu, 4 ),
            " \!U03C3=",
            Round( sigma, 4 ),
            " \!U03BB=",
            Round( lambda, 4 )
        );
        Text( {-19, 0.8}, "p=", Round( p, 3 ) );
        Text(
            {-19, 0.7},
            "quantile= ",
            Round( LogGenGamma Quantile( p, mu, sigma, lambda ), 2 )
        );
    ),
    H List Box( Slider Box( -2, 2, mu, gdey << reshow ), Text Box( "\!U03BC" ) ),
    H List Box( Slider Box( 0, 4, sigma, gdey << reshow ), Text Box( "\!U03C3" ) ),
    H List Box( Slider Box( 0, 10, lambda, gdey << reshow ), Text Box( "\!U03BB" ) ),
    H List Box( Slider Box( 0.01, 0.99, p, gdey << reshow ), Text Box( " p" ) )
);
```

### [Logistic Density](#logistic-density)[](#logistic-density "Click to copy url")

**Syntax:** y = Logistic Density( x, mu, sigma )

**Description:** Returns the density at x of a logistic distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = .2;
New Window( "Example: Logistic Density",
    y = Graph Box(
        Y Scale( 0, 2 ),
        X Scale( -10, 10 ),
        Pen Color( "red" );
        Y Function( Logistic Density( x, mu, sig ), x );
        Text( {0, 1.8}, "mu=", Round( mu, 2 ) );
        Text( {0, 1.6}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( -4, 4, mu, y << reshow ), Text Box( "mu" ) ),
    H List Box( Slider Box( 0.01, 2, sig, y << reshow ), Text Box( "sig" ) ), 

);
```

### [Logistic Distribution](#logistic-distribution)[](#logistic-distribution "Click to copy url")

**Syntax:** p = Logistic Distribution( x, mu, sigma )

**Description:** Returns the probability at x of a logistic distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = .2;
New Window( "Example: Logistic Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -10, 10 ),
        Pen Color( "red" );
        Y Function( Logistic Distribution( x, mu, sig ), x );
        Text( {0.1, 0.9}, "mu=", Round( mu, 2 ) );
        Text( {0.1, 0.8}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( -4, 4, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0.01, 2, sig, y << reshow ), Text Box( " sig" ) )
);
```

### [Logistic Quantile](#logistic-quantile)[](#logistic-quantile "Click to copy url")

**Syntax:** q = Logistic Quantile( p, mu, sigma )

**Description:** Returns the quantile at p of a logistic distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = .2;
qq = .5;
New Window( "Example: Logistic Quantile",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -10, 10 ),
        Pen Color( "red" );
        Y Function( Logistic Distribution( qq, mu, sig ), qq );
        Pen Color( "blue" );
        V Line( Logistic Quantile( qq, mu, sig ), 0, 1 );
        Text(
            {0.1, 0.9},
            " mu=",
            Round( mu, 2 ),
            " sig=",
            Round( sig, 2 ),
            " quantile=",
            Round( qq, 2 )
        );
    ),
    H List Box( Slider Box( -4, 4, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0.01, 2, sig, y << reshow ), Text Box( " sig" ) ),
    H List Box( Slider Box( 0.01, 0.99, qq, y << reshow ), Text Box( " quantile" ) )
);
```

### [Loglogistic Density](#loglogistic-density)[](#loglogistic-density "Click to copy url")

**Syntax:** y = Loglogistic Density( x, mu, sigma )

**Description:** Returns the density at x of a loglogistic distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = .2;
New Window( "Example: Loglogistic Density",
    y = Graph Box(
        Y Scale( 0, .06 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( Loglogistic Density( x, mu, sig ), x );
        Text( {0, .055}, "mu=", Round( mu, 2 ) );
        Text( {0, .045}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 4, mu, y << reshow ), Text Box( "mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( "sig" ) ), 

);
```

### [Loglogistic Distribution](#loglogistic-distribution)[](#loglogistic-distribution "Click to copy url")

**Syntax:** p = Loglogistic Distribution( x, mu, sigma )

**Description:** Returns the probability at x of a loglogistic distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = .2;
New Window( "Example: Loglogistic Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( Loglogistic Distribution( x, mu, sig ), x );
        Text( {0.1, 0.9}, "mu=", Round( mu, 2 ) );
        Text( {0.1, 0.8}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 4, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( " sig" ) )
);
```

### [Loglogistic Quantile](#loglogistic-quantile)[](#loglogistic-quantile "Click to copy url")

**Syntax:** q = Loglogistic Quantile( p, mu, sigma )

**Description:** Returns the quantile at p of a loglogistic distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = .2;
qq = .5;
New Window( "Example: Loglogistic Quantile",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( Loglogistic Distribution( qq, mu, sig ), qq );
        Pen Color( "blue" );
        V Line( Loglogistic Quantile( qq, mu, sig ), 0, 1 );
        Text(
            {0.1, 0.9},
            " mu=",
            Round( mu, 2 ),
            " sig=",
            Round( sig, 2 ),
            " quantile=",
            Round( qq, 2 )
        );
    ),
    H List Box( Slider Box( 0, 4, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( " sig" ) ),
    H List Box( Slider Box( 0.01, 0.99, qq, y << reshow ), Text Box( " quantile" ) )
);
```

### [Lognormal Density](#lognormal-density)[](#lognormal-density "Click to copy url")

**Syntax:** y = Lognormal Density( x, mu, sigma )

**Description:** Returns the density at x of a lognormal distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = 1;
New Window( "Example: Lognormal Density",
    y = Graph Box(
        Y Scale( 0, .15 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( Lognormal Density( x, mu, sig ), x );
        Text( {0, .14}, "mu=", Round( mu, 2 ) );
        Text( {0, .12}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 4, mu, y << reshow ), Text Box( "mu" ) ),
    H List Box( Slider Box( 0, 2, sig, y << reshow ), Text Box( "sig" ) ), 

);
```

### [Lognormal Distribution](#lognormal-distribution)[](#lognormal-distribution "Click to copy url")

**Syntax:** p = Lognormal Distribution( x, mu, sigma )

**Description:** Returns the probability at x of a lognormal distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = 1;
New Window( "Example: Lognormal Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( Lognormal Distribution( x, mu, sig ), x );
        Text( {0.1, 0.9}, "mu=", Round( mu, 2 ) );
        Text( {0.1, 0.8}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 4, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 2, sig, y << reshow ), Text Box( " sig" ) )
);
```

### [Lognormal Quantile](#lognormal-quantile)[](#lognormal-quantile "Click to copy url")

**Syntax:** q = Lognormal Quantile( p, mu, sigma )

**Description:** Returns the quantile at p of a lognormal distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 0;
sig = 1;
qq = .5;
New Window( "Example: Lognormal Quantile",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( Lognormal Distribution( qq, mu, sig ), qq );
        Pen Color( "blue" );
        V Line( Lognormal Quantile( qq, mu, sig ), 0, 1 );
        Text(
            {0.1, 0.9},
            " mu=",
            Round( mu, 2 ),
            " sig=",
            Round( sig, 2 ),
            " quantile=",
            Round( qq, 2 )
        );
    ),
    H List Box( Slider Box( 0, 4, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 3, sig, y << reshow ), Text Box( " sig" ) ),
    H List Box( Slider Box( 0.01, 0.99, qq, y << reshow ), Text Box( " quantile" ) )
);
```

### [Normal Biv Distribution](#normal-biv-distribution)[](#normal-biv-distribution "Click to copy url")

**Syntax:** y = Normal Biv Distribution( x, y, r, \<mu1=0\>, \<s1=1\>, \<mu2=0\>, \<s2=1\> )

**Description:** Computes the probability that an observation (X, Y) is less than or equal to (x, y) with correlation coefficient r where X is marginally normally distributed with mean mu1 and standard deviation s1 and Y is marginally normally distributed with mean mu2 and standard deviation s2. If mu1, s1, mu2, and s2 are not given, the function assumes the standard normal bivariate distribution with mu1=0, s1=1, mu2=0, and s2=1.

**JMP Version Added:** Before version 14

``` jsl
Normal Biv Distribution( -2, -2, .5, 1, 1.5, -1, 2 );
```

### [Normal Density](#normal-density)[](#normal-density "Click to copy url")

**Syntax:** y = Normal Density( q, \<mu=0\>, \<sigma=1\> )

**Description:** Returns the density at q of a Normal distribution with mean mu and standard deviation sigma.

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: Normal Density",
    y = Graph Box(
        Y Scale( 0, 0.45 ),
        X Scale( -4, 4 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Normal Density( q ), q );
    )
);
```

### [Normal Distribution](#normal-distribution)[](#normal-distribution "Click to copy url")

**Syntax:** p = Normal Distribution( q, \<mu=0\>, \<sigma=1\> )

**Description:** Returns the probability that a normally distributed random variable is less than q.

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: Normal Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -4, 4 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Normal Distribution( q ), q );
    )
);
```

### [Normal Log CDistribution](#normal-log-cdistribution)[](#normal-log-cdistribution "Click to copy url")

**Syntax:** y = Normal Log CDistribution( x, \<mean=0\>, \<std dev=1\> )

**Description:** Returns the log of 1 - Normal distribution at x with mean mu and standard deviation sigma.

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: Normal Log CDistribution",
    nlcdiy = Graph Box(
        Y Scale( -10, 0.05 ),
        X Scale( -4, 4 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Normal Log CDistribution( q ), q );
    )
);
```

### [Normal Log Density](#normal-log-density)[](#normal-log-density "Click to copy url")

**Syntax:** y = Normal Log Density( x, \<mu=0\>, \<sigma=1\>)

**Description:** Returns the log of the Normal probability density at x with mean mu and standard deviation sigma.

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: Normal Log Density",
    nldey = Graph Box(
        Y Scale( -9, 0.05 ),
        X Scale( -4, 4 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Normal Log Density( q ), q );
    )
);
```

### [Normal Log Distribution](#normal-log-distribution)[](#normal-log-distribution "Click to copy url")

**Syntax:** y = Normal Log Distribution( x, \<mean=0\>, \<std dev=1\> )

**Description:** Returns the log of the Normal distribution at x with mean mu and standard deviation sigma.

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: Normal Log Distribution",
    nldiy = Graph Box(
        Y Scale( -10, 0.05 ),
        X Scale( -4, 4 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Normal Log Distribution( q ), q );
    )
);
```

### [Normal Mixture Density](#normal-mixture-density)[](#normal-mixture-density "Click to copy url")

**Syntax:** y = Normal Mixture Density(q, meanvec, sdvec, probvec)

**Description:** Returns the density at q of a normal mixture distribution with group means meanvec, group standard deviations sdvec, and group probabilities probvec. Here meanvec, sdvec, and probvec are all vectors of the same size.

**JMP Version Added:** Before version 14

``` jsl
mu1 = -2;
mu2 = 2;
sigma1 = 1;
sigma2 = 4;
p1 = .5;
t1 = mu1 |/ mu2;
t2 = sigma1 |/ sigma2;
t3 = p1 |/ (1 - p1);
New Window( "Univariate Normal Mixture Density",
    clty = Graph Box(
        Y Scale( 0, 0.4 ),
        X Scale( -8, 8 ),
        Pen Color( "red" ),
        Pen Size( 2 );
        t1 = mu1 |/ mu2;
        t2 = sigma1 |/ sigma2;
        t3 = p1 |/ (1 - p1);
        Y Function(
            Normal Mixture Density( y, mu1 |/ mu2, sigma1 |/ sigma2, p1 |/ (1 - p1) ),
            y
        );
        Text( {-7, .37}, "Mean1=", Round( mu1, 2 ) );
        Text( {-2, .37}, "Mean2=", Round( mu2, 2 ) );
        Text( {-7, .34}, "SD1=", Round( sigma1, 2 ) );
        Text( {-2, .34}, "SD2=", Round( sigma2, 2 ) );
        Text( {-7, .31}, "P1=", Round( p1, 2 ) );
        Text( {-2, .31}, "P2=", Round( 1 - p1, 2 ) );
    ),
    H List Box( Slider Box( -3, 3, mu1, clty << reshow ), Text Box( " Mean 1" ) ),
    H List Box( Slider Box( -3, 3, mu2, clty << reshow ), Text Box( " Mean 2" ) ),
    H List Box( Slider Box( .1, 9, sigma1, clty << reshow ), Text Box( " Std Dev 1" ) ),
    H List Box( Slider Box( .1, 9, sigma2, clty << reshow ), Text Box( " Std Dev 2" ) ),
    H List Box( Slider Box( 0, 1, p1, clty << reshow ), Text Box( " P 1" ) ), 

);
```

### [Normal Mixture Distribution](#normal-mixture-distribution)[](#normal-mixture-distribution "Click to copy url")

**Syntax:** y = Normal Mixture Distribution(q, meanvec, sdvec, probvec)

**Description:** Returns the probability that a normal mixture distributed variable with group means meanvec, group standard deviations sdvec, and group probabilities probvec is less than q. Here meanvec, sdvec, and probvec are all vectors of the same size.

**JMP Version Added:** Before version 14

``` jsl
mu1 = -2;
mu2 = 2;
sigma1 = 1;
sigma2 = 4;
p1 = .5;
New Window( "Univariate Normal Mixture Distribution",
    clty = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( -8, 8 ),
        Pen Color( "red" ),
        Pen Size( 2 );
        Y Function(
            Normal Mixture Distribution( y, mu1 |/ mu2, sigma1 |/ sigma2, p1 |/ (1 - p1) ),
            y
        );
        Text( {-7, .95}, "Mean1=", Round( mu1, 2 ) );
        Text( {-2, .95}, "Mean2=", Round( mu2, 2 ) );
        Text( {-7, .85}, "SD1=", Round( sigma1, 2 ) );
        Text( {-2, .85}, "SD2=", Round( sigma2, 2 ) );
        Text( {-7, .75}, "P1=", Round( p1, 2 ) );
        Text( {-2, .75}, "P2=", Round( 1 - p1, 2 ) );
    ),
    H List Box( Slider Box( -3, 3, mu1, clty << reshow ), Text Box( " Mean 1" ) ),
    H List Box( Slider Box( -3, 3, mu2, clty << reshow ), Text Box( " Mean 2" ) ),
    H List Box( Slider Box( .1, 9, sigma1, clty << reshow ), Text Box( " Std Dev 1" ) ),
    H List Box( Slider Box( .1, 9, sigma2, clty << reshow ), Text Box( " Std Dev 2" ) ),
    H List Box( Slider Box( 0, 1, p1, clty << reshow ), Text Box( " P 1" ) ), 

);
```

### [Normal Mixture Quantile](#normal-mixture-quantile)[](#normal-mixture-quantile "Click to copy url")

**Syntax:** q = Normal Mixture Quantile(p, meanvec, sdvec, probvec)

**Description:** Returns the quantile from a normal mixture distribution, the values for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
extqdf = 1;
extqqq = 0.5;
mu1 = -1;
mu2 = 1;
sigma1 = 1;
sigma2 = 4;
p1 = .3;
New Window( "Example: Normal Mixture Quantile",
    extqgr = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Pen Size( 2 );
        Y Function(
            Normal Mixture Distribution( q, mu1 |/ mu2, sigma1 |/ sigma2, p1 |/ (1 - p1) ),
            q
        );
        Pen Color( "blue" );
        V Line(
            Normal Mixture Quantile( extqqq, mu1 |/ mu2, sigma1 |/ sigma2, p1 |/ (1 - p1) ),
            0,
            1
        );
        Text( {-4.5, 0.9}, " quantile=", Round( extqqq, 2 ) );
    ),
    H List Box( Slider Box( 0.01, 0.99, extqqq, extqgr << reshow ), Text Box( " quantile" ) ),
    H List Box( Slider Box( -3, 3, mu1, extqgr << reshow ), Text Box( " Mean 1" ) ),
    H List Box( Slider Box( -3, 3, mu2, extqgr << reshow ), Text Box( " Mean 2" ) ),
    H List Box( Slider Box( .1, 9, sigma1, extqgr << reshow ), Text Box( " Std Dev 1" ) ),
    H List Box( Slider Box( .1, 9, sigma2, extqgr << reshow ), Text Box( " Std Dev 2" ) ),
    H List Box( Slider Box( 0, 1, p1, extqgr << reshow ), Text Box( " P 1" ) ), 

);
```

### [Normal Quantile](#normal-quantile)[](#normal-quantile "Click to copy url")

**Syntax:** q = Normal Quantile( p, \<mu=0\>, \<sigma=1\> ); q = Probit( p )

**Description:** Returns the quantile from a Normal distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
Normal Quantile( 0.9 );
```

### [Probit](#probit)[](#probit "Click to copy url")

**Syntax:** q = Normal Quantile( p, \<mu=0\>, \<sigma=1\> ); q = Probit( p )

**Description:** Returns the quantile from a Normal distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
Normal Quantile( 0.9 );
```

### [SEV Density](#sev-density)[](#sev-density "Click to copy url")

**Syntax:** y = SEV Density( x, mu, sigma )

**Description:** Returns the density at x of a smallest extreme distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 50;
sig = 5;
New Window( "Example: SEV Density",
    y = Graph Box(
        Y Scale( 0, .06 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( SEV Density( x, mu, sig ), x );
        Text( {0, .055}, "mu=", Round( mu, 2 ) );
        Text( {0, .045}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 100, mu, y << reshow ), Text Box( "mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( "sig" ) ), 

);
```

### [SEV Distribution](#sev-distribution)[](#sev-distribution "Click to copy url")

**Syntax:** p = SEV Distribution( x, mu, sigma )

**Description:** Returns the probability at x of a smallest extreme distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 50;
sig = 5;
New Window( "Example: SEV Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( SEV Distribution( x, mu, sig ), x );
        Text( {0.1, 0.9}, "mu=", Round( mu, 2 ) );
        Text( {0.1, 0.8}, "sig=", Round( sig, 2 ) );
    ),
    H List Box( Slider Box( 0, 100, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( " sig" ) )
);
```

### [SEV Quantile](#sev-quantile)[](#sev-quantile "Click to copy url")

**Syntax:** q = SEV Quantile( p, mu, sigma )

**Description:** Returns the quantile at p of a smallest extreme distribution with location mu and scale sigma.

**JMP Version Added:** Before version 14

``` jsl
mu = 50;
sig = 5;
qq = .5;
New Window( "Example: SEV Quantile",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 60 ),
        Pen Color( "red" );
        Y Function( SEV Distribution( qq, mu, sig ), qq );
        Pen Color( "blue" );
        V Line( SEV Quantile( qq, mu, sig ), 0, 1 );
        Text(
            {0.1, 0.9},
            " mu=",
            Round( mu, 2 ),
            " sig=",
            Round( sig, 2 ),
            " quantile=",
            Round( qq, 2 )
        );
    ),
    H List Box( Slider Box( 0, 80, mu, y << reshow ), Text Box( " mu" ) ),
    H List Box( Slider Box( 0, 10, sig, y << reshow ), Text Box( " sig" ) ),
    H List Box( Slider Box( 0.01, 0.99, qq, y << reshow ), Text Box( " quantile" ) )
);
```

### [SHASH Density](#shash-density)[](#shash-density "Click to copy url")

**Syntax:** d = SHASH Density( x, gamma, delta, theta, sigma )

**Description:** Returns the density at x of a sinh-arcsinh (SHASH) distribution. The SHASH transformation can be used to create more normally distributed data.

**JMP Version Added:** 14

**Example 1**

``` jsl
SHASH Density( 0, -1, 2, -2, 3 );
```

#### [SHASH Transformation](#shash-transformation)[](#shash-transformation "Click to copy url")

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

### [SHASH Distribution](#shash-distribution)[](#shash-distribution "Click to copy url")

**Syntax:** p = SHASH Distribution( q, gamma, delta, theta, sigma )

**Description:** Returns the probability that a sinh-arcsinh (SHASH) distributed random variable is less than q. The SHASH transformation can be used to create more normally distributed data.

**JMP Version Added:** 14

**Example 1**

``` jsl
gamma = 0.5;
delta = 1;
theta = 1;
sigma = 1;
New Window( "Example: SHASH Distribution",
    jsuc = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -2, 2 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( SHASH Distribution( q, gamma, delta, theta, sigma ), q );
        Text(
            {-1, 0.9},
            "\!U03B3=",
            Round( gamma, 2 ),
            " \!U03B4=",
            Round( delta, 2 ),
            " \!U03B8=",
            Round( theta, 2 ),
            " \!U03C3=",
            Round( sigma, 2 )
        );
    ),
    H List Box( Slider Box( 0, 1, gamma, jsuc << reshow ), Text Box( " \!U03B3" ) ),
    H List Box( Slider Box( 0, 2, delta, jsuc << reshow ), Text Box( " \!U03B4" ) ),
    H List Box( Slider Box( 0, 2, theta, jsuc << reshow ), Text Box( " \!U03B8" ) ),
    H List Box( Slider Box( 0, 2, sigma, jsuc << reshow ), Text Box( " \!U03C3" ) )
);
```

#### [SHASH Transformation](#shash-transformation_1)[](#shash-transformation_1 "Click to copy url")

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

### [SHASH Quantile](#shash-quantile)[](#shash-quantile "Click to copy url")

**Syntax:** q = SHASH Quantile( p, gamma, delta, theta, sigma )

**Description:** Returns the quantile from a sinh-arcsinh (SHASH) distribution, the value for which the probability is p that a random value would be lower. The SHASH transformation can be used to create more normally distributed data.

**JMP Version Added:** 14

**Example 1**

``` jsl
SHASH Quantile( .5, 1, 2, 3, 1 );
```

#### [SHASH Transformation](#shash-transformation_2)[](#shash-transformation_2 "Click to copy url")

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

### [Students t Density](#students-t-density)[](#students-t-density "Click to copy url")

**Syntax:** p = t Density( q, df, \<nonCentrality=0\> )

**Description:** Returns the density function of Student's t.

**JMP Version Added:** Before version 14

``` jsl
tdedf = 1;
New Window( "Example: Students t Density",
    tdegr = Graph Box(
        Y Scale( -.05, 0.45 ),
        X Scale( -8, 8 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Density( tdeq, Exp( tdedf ) ), tdeq );
        H Line( 2, 3, 0.3 );
        Pen Color( "blue" );
        Y Function( Normal Density( tdeq ), tdeq );
        H Line( 2, 3, 0.25 );
        Text( {2, 0.35}, "df=", Round( Exp( tdedf ), 2 ) );
        Text( {3.5, 0.3}, "Student t" );
        Text( {3.5, 0.25}, "Normal" );
    ),
    H List Box(
        Text Box( "df " ),
        Slider Box( Log( 0.1 ), Log( 1000 ), tdedf, tdegr << reshow )
    )
);
```

### [Students t Distribution](#students-t-distribution)[](#students-t-distribution "Click to copy url")

**Syntax:** p = t Distribution( q, df, \<nonCentrality=0\> )

**Description:** Returns the probability that a Student's t distributed random variable is less than q.

**JMP Version Added:** Before version 14

``` jsl
tdidf = 1;
New Window( "Example: Students t Distribution",
    tdigr = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Distribution( tdiq, tdidf ), tdiq );
        Text( {-4.5, 0.9}, "df=", Round( tdidf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 1, 10, tdidf, tdigr << reshow ) )
);
```

### [Students t Quantile](#students-t-quantile)[](#students-t-quantile "Click to copy url")

**Syntax:** q = t Quantile( p, df, \<nonCentrality=0\> )

**Description:** Returns the quantile from a Student's t distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
extqdf = 1;
extqqq = 0.5;
New Window( "Example: Students t Quantile",
    extqgr = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Distribution( q, Round( extqdf ) ), q );
        Pen Color( "blue" );
        V Line( t Quantile( extqqq, Round( extqdf ) ), 0, 1 );
        Text( {-4.5, 0.9}, "df=", Round( extqdf, 2 ), " quantile=", Round( extqqq, 2 ) );
    ),
    H List Box( Slider Box( 1, 30, extqdf, extqgr << reshow ), Text Box( " df" ) ),
    H List Box( Slider Box( 0.01, 0.99, extqqq, extqgr << reshow ), Text Box( " quantile" ) ), 

);
```

### [Tukey HSD P value](#tukey-hsd-p-value)[](#tukey-hsd-p-value "Click to copy url")

**Syntax:** p = Tukey HSD P value( q, nGroups, dfe )

**Description:** Returns the p-value from Tukey's HSD multiple comparisons test, where q is the test statistic, nGroups is the number of groups in the study, and dfe is the error degrees of freedom (based on the total study sample).

Note that q is Tukey's adjusted critical value, which is the quantile of Tukey's studentized range distribution divided by the sqrt(2).

**JMP Version Added:** Before version 14

``` jsl
Tukey HSD P value( 3.73, 6, 34 );
```

### [Tukey HSD Quantile](#tukey-hsd-quantile)[](#tukey-hsd-quantile "Click to copy url")

**Syntax:** q = Tukey HSD Quantile( 1-alpha, nGroups, dfe )

**Description:** Returns the quantile needed in Tukey's HSD multiple comparisons test, where 1-alpha is the confidence level, nGroups is the number of groups in the study, and dfe is the error degrees of freedom (based on the total study sample).

Note that q is Tukey's adjusted critical value, which is the quantile of Tukey's studentized range distribution divided by the sqrt(2).

**JMP Version Added:** Before version 14

``` jsl
alpha = 0.05;
dfe = 5;
Tukey HSD Quantile( 1 - alpha, 20, dfe );
New Window( "Example: Tukey HSD Quantile",
    tdigr = Graph Box(
        Y Scale( 2, 8 ),
        X Scale( 2.5, 15.5 ),
        YName( "Tukey HSD Quantile" ),
        XName( "Groups" ),
        Pen Color( "red" );
        For( i = 3, i <= 15, i++,
            V Line( i, 0, Tukey HSD Quantile( 1 - alpha, i, dfe ) )
        );
        Text( {3, 7}, "dfe=", Round( dfe, 2 ) );
    ),
    H List Box( Text Box( "dfe" ), Slider Box( 3, 10, dfe, tdigr << reshow ) )
);
```

### [Weibull Density](#weibull-density)[](#weibull-density "Click to copy url")

**Syntax:** y = Weibull Density( x, shape, \<scale=1\>, \<threshold=0\> )

**Description:** Returns the density at x of a Weibull probability distribution with a shape parameter and optional scale parameter.

**JMP Version Added:** Before version 14

``` jsl
shape = 0.5;
New Window( "Example: Weibull Density",
    y = Graph Box(
        Y Scale( 0, 2 ),
        X Scale( 0, 1.5 ),
        XName( "x" ),
        Pen Color( "red" );
        Y Function( Weibull Density( x, shape ), x );
        Text( {1.1, 1.8}, " shape=", Round( shape, 2 ) );
    ),
    H List Box( Slider Box( 0, 5, shape, y << reshow ), Text Box( " shape" ) )
);
```

### [Weibull Distribution](#weibull-distribution)[](#weibull-distribution "Click to copy url")

**Syntax:** p = Weibull Distribution( x, shape, \<scale=1\>, \<threshold=0\> )

**Description:** Returns the probability that a Weibull distributed random variable (with a shape parameter and optional scale parameter) is less than x.

**JMP Version Added:** Before version 14

``` jsl
shape = 2;
New Window( "Example: Weibull Distribution",
    y = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( 0, 2 ),
        XName( "x" ),
        Pen Color( "red" );
        Y Function( Weibull Distribution( x, shape ), x );
        Text( {0.1, 0.9}, " shape=", Round( shape, 2 ) );
    ),
    H List Box( Slider Box( 0, 5, shape, y << reshow ), Text Box( " shape" ) )
);
```

### [Weibull Quantile](#weibull-quantile)[](#weibull-quantile "Click to copy url")

**Syntax:** q = Weibull Quantile( p, beta, \<alpha=1\>, \<threshold=0\> )

**Description:** Returns the quantile from a Weibull distribution, the value for which the probability is p that a random value would be lower, where beta and alpha are the shape and scale parameters, respectively.

**JMP Version Added:** Before version 14

``` jsl
exwqbeta = 2;
exwqqq = 0.5;
New Window( "Example: Weibull Quantile",
    exwqy = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( 0, 2 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( Weibull Distribution( exwqq, exwqbeta ), exwqq );
        Pen Color( "blue" );
        V Line( Weibull Quantile( exwqqq, exwqbeta ), 0, 1 );
        Text(
            {0.1, 0.9},
            " \!U03B2=",
            Round( exwqbeta, 2 ),
            " quantile=",
            Round( exwqqq, 2 )
        );
    ),
    H List Box( Slider Box( 0, 5, exwqbeta, exwqy << reshow ), Text Box( " \!U03B2" ) ),
    H List Box( Slider Box( 0.01, 0.99, exwqqq, exwqy << reshow ), Text Box( " quantile" ) )
);
```

### [t Density](#t-density)[](#t-density "Click to copy url")

**Syntax:** p = t Density( q, df, \<nonCentrality=0\> )

**Description:** Returns the density function of Student's t.

**JMP Version Added:** Before version 14

``` jsl
tdedf = 1;
New Window( "Example: Students t Density",
    tdegr = Graph Box(
        Y Scale( -.05, 0.45 ),
        X Scale( -8, 8 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Density( tdeq, Exp( tdedf ) ), tdeq );
        H Line( 2, 3, 0.3 );
        Pen Color( "blue" );
        Y Function( Normal Density( tdeq ), tdeq );
        H Line( 2, 3, 0.25 );
        Text( {2, 0.35}, "df=", Round( Exp( tdedf ), 2 ) );
        Text( {3.5, 0.3}, "Student t" );
        Text( {3.5, 0.25}, "Normal" );
    ),
    H List Box(
        Text Box( "df " ),
        Slider Box( Log( 0.1 ), Log( 1000 ), tdedf, tdegr << reshow )
    )
);
```

### [t Distribution](#t-distribution)[](#t-distribution "Click to copy url")

**Syntax:** p = t Distribution( q, df, \<nonCentrality=0\> )

**Description:** Returns the probability that a Student's t distributed random variable is less than q.

**JMP Version Added:** Before version 14

``` jsl
tdidf = 1;
New Window( "Example: Students t Distribution",
    tdigr = Graph Box(
        Y Scale( 0, 1 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Distribution( tdiq, tdidf ), tdiq );
        Text( {-4.5, 0.9}, "df=", Round( tdidf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 1, 10, tdidf, tdigr << reshow ) )
);
```

### [t Log CDistribution](#t-log-cdistribution)[](#t-log-cdistribution "Click to copy url")

**Syntax:** y = t Log CDistribution( x, df, \<nc\> )

**Description:** Returns the log of 1 - t distribution.

**JMP Version Added:** Before version 14

``` jsl
tlcdidf = 1;
New Window( "Example: Students t Log CDistribution",
    tlcdigr = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Log CDistribution( tlcdiq, tlcdidf ), tlcdiq );
        Text( {-4.5, -0.9}, "df=", Round( tlcdidf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 1, 10, tlcdidf, tlcdigr << reshow ) )
);
```

### [t Log Density](#t-log-density)[](#t-log-density "Click to copy url")

**Syntax:** y = t Log Density( x, df, \<nc\> )

**Description:** Returns the log of the t probability density.

**JMP Version Added:** Before version 14

``` jsl
tldedf = 1;
New Window( "Example: Students t Log Density",
    tldegr = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Log Density( tldeq, tldedf ), tldeq );
        Text( {2.5, -0.35}, "df=", Round( tldedf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 0.5, 10, tldedf, tldegr << reshow ) )
);
```

### [t Log Distribution](#t-log-distribution)[](#t-log-distribution "Click to copy url")

**Syntax:** y = t Log Distribution( x, df, \<nc\> )

**Description:** Returns the log of the t distribution.

**JMP Version Added:** Before version 14

``` jsl
tldidf = 1;
New Window( "Example: Students t Log Distribution",
    tldigr = Graph Box(
        Y Scale( -4, 0.05 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Log Distribution( tldiq, tldidf ), tldiq );
        Text( {-4.5, -0.9}, "df=", Round( tldidf, 2 ) );
    ),
    H List Box( Text Box( "df " ), Slider Box( 1, 10, tldidf, tldigr << reshow ) )
);
```

### [t Noncentrality](#t-noncentrality)[](#t-noncentrality "Click to copy url")

**Syntax:** nc = t Noncentrality( x, df, prob )

**Description:** Solves for the noncentrality parameter of a Student's t distribution such that prob = t Distribution( x, df, nc ).

**JMP Version Added:** Before version 14

``` jsl
New Window( "Example: t Noncentrality",
    tncgr = Graph Box(
        Y Scale( 0.01, 0.99 ),
        X Scale( 0.01, 0.99 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Distribution( 3, 2, t Noncentrality( 3, 2, q ) ), q );
    )
);
t Distribution( 3, 2, t Noncentrality( 3, 2, 0.5 ) );
```

### [t Quantile](#t-quantile)[](#t-quantile "Click to copy url")

**Syntax:** q = t Quantile( p, df, \<nonCentrality=0\> )

**Description:** Returns the quantile from a Student's t distribution, the value for which the probability is p that a random value would be lower.

**JMP Version Added:** Before version 14

``` jsl
extqdf = 1;
extqqq = 0.5;
New Window( "Example: Students t Quantile",
    extqgr = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( -5, 5 ),
        XName( "q" ),
        Pen Color( "red" );
        Y Function( t Distribution( q, Round( extqdf ) ), q );
        Pen Color( "blue" );
        V Line( t Quantile( extqqq, Round( extqdf ) ), 0, 1 );
        Text( {-4.5, 0.9}, "df=", Round( extqdf, 2 ), " quantile=", Round( extqqq, 2 ) );
    ),
    H List Box( Slider Box( 1, 30, extqdf, extqgr << reshow ), Text Box( " df" ) ),
    H List Box( Slider Box( 0.01, 0.99, extqqq, extqgr << reshow ), Text Box( " quantile" ) ), 

);
```

[ Previous](PI%20Server.html "PI Server") [Next ](Programming.html "Programming")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
