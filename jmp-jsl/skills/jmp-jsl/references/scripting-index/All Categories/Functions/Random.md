# Random

*Source: [https://jsl.jmp.com/All%20Categories/Functions/Random.html](https://jsl.jmp.com/All%20Categories/Functions/Random.html)*

---

# [Random](#random)[](#random "Click to copy url")

### [Col Shuffle](#col-shuffle)[](#col-shuffle "Click to copy url")

**Syntax:** y = Col Shuffle(\<byVar, \<Excluded( Row State() )\>, ...\>)

**Description:** Returns a random integer between 1 and the number of rows of the current data table. When used in a column formula, Col Shuffle() creates a random ordering of row numbers with each row number appearing only once. The ordering is cached internally so that multiple evaluations are efficient.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "Shuffle 1", Numeric, Continuous, Set Formula( Col Shuffle() ) );
dt << New Column( "Shuffle 2", Numeric, Continuous, Set Formula( Col Shuffle() ) );
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "Shuffle", Numeric, Continuous, Set Formula( Col Shuffle( :age ) ) );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Clear Row States << Select Rows( Index( 1, 10 ) ) << Exclude;
dt << New Column( "Col Shuffle for each Sex", Formula( Col Shuffle( :height, :sex ) ) );
dt << New Column( "Col Shuffle for each Sex grouped by Excluded",
    Formula( Col Shuffle( :height, :sex, Excluded( Row State() ) ) )
);
```

### [Make KFold Formula](#make-kfold-formula)[](#make-kfold-formula "Click to copy url")

**Syntax:** y = Make KFold Formula( folds, Y Columns( cols ), \<\<Stratification Columns( cols ), \<\<Grouping Columns( cols ) )

**Description:** Generates a validation column with folds levels when used in a column formula. This JSL function is primarily used by the Make Validation Column platform to generate formula columns.

**JMP Version Added:** 17

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "KFold Validation",
    "Numeric",
    "Nominal",
    Formula( Make KFold Formula( 5, <<Y Columns( :height ) ) )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "Stratified KFold",
    "Numeric",
    "Nominal",
    Formula(
        Make KFold Formula( 4, <<Y Columns( :height ), <<Stratification Columns( :sex ) )
    )
);
```

### [Make Validation Formula](#make-validation-formula)[](#make-validation-formula "Click to copy url")

**Syntax:** y = Make Validation Formula( rates, \<\<Stratification Columns( cols ), \<\<Grouping Columns( cols ), \<\<Cutpoint Column ( col ), \<\<Cutpoint Batch ID( col ), \<\<Determine cutpoints using( "Proportions"\|"Numbers of Rows"\|"Fixed Time or Date"\|"Elapsed Time" ), \<\<Assign Extra Rows( "To Training"\|"To Validation"\|"To Test" ) )

**Description:** Generates a two-level or three-level validation column when used in a column formula. The rates argument is a 3 by 1 matrix that contains the training, validation, and test rates, respectively. This JSL function is primarily used by the Make Validation Column platform to generate formula columns.

**JMP Version Added:** 15

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "Validation",
    "Numeric",
    "Nominal",
    Formula( Make Validation Formula( [.6, .4, 0] ) ),
    Set Property( "Value Labels", {0 = "Training", 1 = "Validation"} )
);
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "Validation",
    "Numeric",
    "Nominal",
    Formula( Make Validation Formula( [.6, .2, .2], <<Stratification Columns( :age ) ) ),
    Set Property( "Value Labels", {0 = "Training", 1 = "Validation", 2 = "Test"} )
);
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Functional Data/Weekly Weather Data.jmp" );
dt << New Column( "Validation",
    "Numeric",
    "Nominal",
    Formula(
        Make Validation Formula(
            [20, 10, 4],
            <<Cutpoint Column( :Week of Year ),
            <<Cutpoint Batch ID( :ID ),
            <<Determine cutpoints using( "Numbers of Rows" )
        )
    ),
    Set Property( "Value Labels", {0 = "Training", 1 = "Validation", 2 = "Test"} )
);
```

### [Polytope Uniform Random](#polytope-uniform-random)[](#polytope-uniform-random "Click to copy url")

**Syntax:** points = Random Linearly Constrained Uniform( numSamples, A, b, L, U, neq, nle, nge, \<nwarm=200\>, \<nstride=25\>, \<tol=1e-8\>, \<G\>, \<LC\>, \<UC\> )

**Description:** Generates a random sample subject to linear constraints, variable bound constraints, and cardinality constraints on specified component subgroup variables. The numSamples argument specifies the number of random points to be generated. The A argument is the linear constraint coefficient matrix. The b argument is the vector of right hand side values of the linear constraints. The L and U arguments are vectors of the lower and upper bounds for the variables, respectively. The neq, nle, and nge arguments are the number of equality constraints, the number of less than or equal constraints, and the number of greater than or equal constraints, respectively. The nwarm argument is the number of warm-up repetitions before points are written to the output matrix. The nstride argument is the number of repetitions between each point that is written to the output matrix. The tol argument is the tolerance. The G argument is a vector of indices that assigns the variables to constrained component subgroups where missing or zero values do not belong to a constrained subgroup. The LC and UC arguments are the lower and upper cardinality constraints for the constrained component subgroups, respectively. Note that the constraints must be listed as equality first, less than or equal next, and greater than or equal last.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
A = [1 1 1, 1 2 0];
b = [1, 0.5];
L = [0, 0, 0.1];
U = [1, 1, 1];
points = Random Linearly Constrained Uniform( 2000, A, b, L, U, 1, 0, 1, 300, 50 );
dt = As Table( points );
tobj = Report( Ternary Plot( X( :Col1, :Col2, :Col3 ) ) );
tfr = tobj[scalebox( 1 )] << clone box;
New Window( "Example: Random Linearly Constrained Uniform",
    Outline Box( "Points on a Ternary Plot", tfr ),
    Outline Box( "Constraints",
        Text Box( "X1 + x2 + x3 = 1" ),
        Text Box( "X2 + 2*x2 >= 0.5" )
    ),
    Outline Box( "Variable Bounds",
        Text Box( "0 <= x1 <= 1" ),
        Text Box( "0 <= x2 <= 1" ),
        Text Box( ".1 < x3 <= 1" )
    )
);
Close( dt, no save );
Show( "see new window for example output" );
```

**Example 2**

``` jsl

A = [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1];
b = [100];
L = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
U = [100 100 95 90 100 85 100 90 60 70 75 70 75 100 95 60 80 95 100 100];
nwarm = 100;
nstride = 100;
tol = 1e-8;
// Index the constrained subgroups.  Index = 0 is not in a constrained subgroup.
G = [0 0 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 0 0];
// Lower cardinality constraints for the constrained subgroups
LC = [1 1];
// Upper cardinality constraints for the constrained subgroups
UC = [3 5];
points = Random Linearly Constrained Uniform(
    100,
    A,
    b,
    L,
    U,
    1,
    0,
    0,
    nwarm,
    nstride,
    tol,
    G,
    LC,
    UC
);
dt = As Table( points );
```

### [Random Beta](#random-beta)[](#random-beta "Click to copy url")

**Syntax:** y = Random Beta( alpha, beta, \<theta=0\>, \<sigma=1\> )

**Description:** Returns a random number from a beta distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Beta( 1, 1 );
//produce a vector of random numbers
v = J( 1, 10, Random Beta( 1, 1 ) );
//show results
Show( x, v );
```

### [Random Beta Binomial](#random-beta-binomial)[](#random-beta-binomial "Click to copy url")

**Syntax:** y = Random Beta Binomial( n, p, \<delta=0\> )

**Description:** Returns a random number from a beta binomial distribution for n trials with probability p and correlation delta.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Beta Binomial( 14, .5, .2 );
//produce a vector of random numbers
v = J( 1, 10, Random Beta Binomial( 14, .5, .2 ) );
//show results
Show( x, v );
```

### [Random Binomial](#random-binomial)[](#random-binomial "Click to copy url")

**Syntax:** y = Random Binomial( n, p )

**Description:** Returns a random number from a binomial distribution with n trials and event probability p.

**JMP Version Added:** Before version 14

``` jsl
exrbinp = 0.5;
exrbinn = 40;
exrbinlsz = Log( 1000 );
New Window( "Example: Random Binomial and Empirical Distribution",
    exrbiny = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( 0, 40 ),
        Pen Color( "red" ),
        Pen Size( 2 );
        exrbinsz = Round( Exp( exrbinlsz ) );
        exrbinsamp = J( Round( exrbinsz ), 1, . );
        exrbinfreq = J( Round( exrbinn + 1 ), 1, . );
        For( exrbink = 1, exrbink <= Round( exrbinsz ), exrbink++,
            exrbinsamp[exrbink] = Random Binomial( exrbinn, exrbinp )
        );
        For( exrbink = 0, exrbink <= Round( exrbinn ), exrbink++,
            exrbinfreq[exrbink + 1] = Sum( exrbinsamp <= exrbink ) / Round( exrbinsz )
        );
        For( exrbink = 0, exrbink < Round( exrbinn ), exrbink++,
            H Line(
                exrbink,
                exrbink + 1,
                Binomial Distribution( exrbinp, Round( exrbinn ), exrbink )
            );
            V Line(
                exrbink + 1,
                Binomial Distribution( exrbinp, Round( exrbinn ), exrbink ),
                Binomial Distribution( exrbinp, Round( exrbinn ), exrbink + 1 )
            );
        );
        Pen Color( "blue" );
        For( exrbink = 1, exrbink <= Round( exrbinn ), exrbink++,
            H Line( exrbink - 1, exrbink, exrbinfreq[exrbink] );
            V Line( exrbink, exrbinfreq[exrbink], exrbinfreq[exrbink + 1] );
        );
        Text(
            {0.5, 0.9},
            "n=",
            Round( exrbinn ),
            " p=",
            Round( exrbinp, 2 ),
            " size=",
            Round( exrbinsz )
        );
    ),
    H List Box(
        Slider Box( Log( 10 ), Log( 5000 ), exrbinlsz, exrbiny << reshow ),
        Text Box( " random sample size" )
    )
);
```

### [Random Category](#random-category)[](#random-category "Click to copy url")

**Syntax:** y = Random Category( probabilityA, resultA, probabilityB, resultB, resultElse )

**Description:** Returns a random category given pairs of probability and result expressions. A random uniform number is generated and compared to the probability arguments to determine which result argument is returned.

**JMP Version Added:** Before version 14

``` jsl
Random Category( .2, "A", .3, "B", .4, "C", "D" );
```

### [Random Cauchy](#random-cauchy)[](#random-cauchy "Click to copy url")

**Syntax:** y = Random Cauchy()

**Description:** Returns a random number from a Cauchy distribution with a median of zero.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Cauchy();
//produce a vector of random numbers
v = J( 1, 10, Random Cauchy() );
//show results
Show( x, v );
```

### [Random ChiSquare](#random-chisquare)[](#random-chisquare "Click to copy url")

**Syntax:** y = Random ChiSquare( df, \<nonCentrality=0\> )

**Description:** Returns a random number from a Chi-Square distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random ChiSquare( 2 );
//produce a vector of random numbers
v = J( 1, 10, Random ChiSquare( 2 ) );
//show results
Show( x, v );
```

### [Random ExGaussian](#random-exgaussian)[](#random-exgaussian "Click to copy url")

**Syntax:** y = Random ExGaussian( location, scale, shape)

**Description:** Returns a random number from an ExGaussian distribution.

**JMP Version Added:** 18

``` jsl

//produce a single random number
x = Random ExGaussian( 0, .5, .25 );
//produce a vector of random numbers
v = J( 1, 10, Random ExGaussian( 0, .5, .25 ) );
//show results
Show( x, v );
```

### [Random Exp](#random-exp)[](#random-exp "Click to copy url")

**Syntax:** y = Random Exp()

**Description:** Returns a random number from an exponential distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Exp();
//produce a vector of random numbers
v = J( 1, 10, Random Exp() );
//show results
Show( x, v );
```

### [Random F](#random-f)[](#random-f "Click to copy url")

**Syntax:** y = Random F( dfnum, dfden, \<nonCentrality=0\> )

**Description:** Returns a random number from an F distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random F( 2, 2 );
//produce a vector of random numbers
v = J( 1, 10, Random F( 2, 2 ) );
//show results
Show( x, v );
```

### [Random Frechet](#random-frechet)[](#random-frechet "Click to copy url")

**Syntax:** y = Random Frechet( \<mu=0\>, \<sigma=1\> )

**Description:** Returns a random number from a Fréchet distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Frechet( 10, 5 );
//produce a vector of random numbers
v = J( 1, 10, Random Frechet( 10, 5 ) );
//show results
Show( x, v );
```

### [Random GLog](#random-glog)[](#random-glog "Click to copy url")

**Syntax:** y = Random GLog( mu, sigma, lambda )

**Description:** Returns a random number from a generalized logarithm distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random GLog( 4, 1, 0.1 );
//produce a vector of random numbers
v = J( 1, 10, Random GLog( 4, 1, 0.1 ) );
//show results
Show( x, v );
```

### [Random Gamma](#random-gamma)[](#random-gamma "Click to copy url")

**Syntax:** y = Random Gamma( alpha, \<scale=1\> )

**Description:** Returns a random number from a gamma distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Gamma( 1 );
//produce a vector of random numbers
v = J( 1, 10, Random Gamma( 1 ) );
//show results
Show( x, v );
```

### [Random Gamma Poisson](#random-gamma-poisson)[](#random-gamma-poisson "Click to copy url")

**Syntax:** y = Random Gamma Poisson( lambda, \<sigma=1\> )

**Description:** Returns a random number from a gamma Poisson distribution with parameters lambda and sigma.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Gamma Poisson( 3, 2 );
//produce a vector of random numbers
v = J( 1, 10, Random Gamma Poisson( 3, 2 ) );
//show results
Show( x, v );
```

### [Random GenGamma](#random-gengamma)[](#random-gengamma "Click to copy url")

**Syntax:** y = Random GenGamma( \<mu=0\>, \<sigma=1\>, \<lambda=0\> )

**Description:** Returns a random number from an extended generalized gamma distribution with parameters mu, sigma, and lambda.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random GenGamma( 2, 1.25 );
//produce a vector of random numbers
v = J( 1, 10, Random GenGamma( 2, 1.25 ) );
//show results
Show( x, v );
```

### [Random Geometric](#random-geometric)[](#random-geometric "Click to copy url")

**Syntax:** y = Random Geometric( p )

**Description:** Returns a random number of non-events until an event occurs, for events with probability p.

**JMP Version Added:** Before version 14

``` jsl
exrgeop = 0.1;
exrgeolsz = Log( 300 );
New Window( "Example: Random Geometric and Empirical Distribution",
    exrgeoy = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( -1, 50 ),
        Pen Color( "red" ),
        Pen Size( 1 );
        exrgeosz = Round( Exp( exrgeolsz ) );
        exrgeosamp = J( Round( exrgeosz ), 1, . );
        exrgeofreq = J( Round( 50 + 1 ), 1, . );
        For( exrgeok = 1, exrgeok <= Round( exrgeosz ), exrgeok++,
            exrgeosamp[exrgeok] = Random Geometric( exrgeop )
        );
        For( exrgeok = 0, exrgeok <= 50, exrgeok++,
            exrgeofreq[exrgeok + 1] = Sum( exrgeosamp <= exrgeok ) / Round( exrgeosz )
        );
        exrgeotmp1 = 0;
        exrgeotmp2 = 0;
        For( exrgeok = 0, exrgeok < 50, exrgeok++,
            exrgeotmp2 = exrgeotmp2 + (1 - exrgeop) ^ exrgeok * exrgeop;
            H Line( exrgeok, exrgeok + 1, exrgeotmp2 );
            V Line( exrgeok, exrgeotmp1, exrgeotmp2 );
            exrgeotmp1 = exrgeotmp2;
        );
        Pen Color( "blue" );
        For( exrgeok = 0, exrgeok < 50, exrgeok++,
            H Line( exrgeok, exrgeok + 1, exrgeofreq[exrgeok + 1] );
            V Line( exrgeok + 1, exrgeofreq[exrgeok + 1], exrgeofreq[exrgeok + 2] );
        );
        Text( {10, 0.2}, " p=", Round( exrgeop, 2 ), " sample size=", Round( exrgeosz ) );
    ),
    H List Box(
        Slider Box( Log( 10 ), Log( 5000 ), exrgeolsz, exrgeoy << reshow ),
        Text Box( " random sample size" )
    )
);
```

### [Random Index](#random-index)[](#random-index "Click to copy url")

**Syntax:** x = Random Index( n, k )

**Description:** Returns a k by 1 matrix of random integers between 1 and n with no duplicates.

**JMP Version Added:** Before version 14

``` jsl
Random Index( 100, 5 );
```

### [Random Integer](#random-integer)[](#random-integer "Click to copy url")

**Syntax:** y = Random Integer( n ); Random Integer( k, n )

**Description:** Returns a random integer between 1 and n (or between k and n) inclusive.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Integer( 1, 10 );
//produce a vector of random numbers
v = J( 1, 10, Random Integer( 1, 10 ) );
//show results
Show( x, v );
```

### [Random Johnson Sb](#random-johnson-sb)[](#random-johnson-sb "Click to copy url")

**Syntax:** y = Random Johnson Sb( gamma, delta, theta, sigma )

**Description:** Returns a random number from a Johnson Sb distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Johnson Sb( 0.5, 1, 1, 1 );
//produce a vector of random numbers
v = J( 1, 10, Random Johnson Sb( 0.5, 1, 1, 1 ) );
//show results
Show( x, v );
```

### [Random Johnson Sl](#random-johnson-sl)[](#random-johnson-sl "Click to copy url")

**Syntax:** y = Random Johnson Sl( gamma, delta, theta, \<sigma=1\> )

**Description:** Returns a random number from a Johnson Sl distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Johnson Sl( 0.5, 1, 1, 1 );
//produce a vector of random numbers
v = J( 1, 10, Random Johnson Sl( 0.5, 1, 1, 1 ) );
//show results
Show( x, v );
```

### [Random Johnson Su](#random-johnson-su)[](#random-johnson-su "Click to copy url")

**Syntax:** y = Random Johnson Su( gamma, delta, theta, sigma )

**Description:** Returns a random number from a Johnson Su distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Johnson Su( 0.5, 1, 1, 1 );
//produce a vector of random numbers
v = J( 1, 10, Random Johnson Su( 0.5, 1, 1, 1 ) );
//show results
Show( x, v );
```

### [Random LEV](#random-lev)[](#random-lev "Click to copy url")

**Syntax:** y = Random LEV( \<mu=0\>, \<sigma=1\> )

**Description:** Returns a random number from a LEV distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random LEV( 10, 5 );
//produce a vector of random numbers
v = J( 1, 10, Random LEV( 10, 5 ) );
//show results
Show( x, v );
```

### [Random Linearly Constrained Uniform](#random-linearly-constrained-uniform)[](#random-linearly-constrained-uniform "Click to copy url")

**Syntax:** points = Random Linearly Constrained Uniform( numSamples, A, b, L, U, neq, nle, nge, \<nwarm=200\>, \<nstride=25\>, \<tol=1e-8\>, \<G\>, \<LC\>, \<UC\> )

**Description:** Generates a random sample subject to linear constraints, variable bound constraints, and cardinality constraints on specified component subgroup variables. The numSamples argument specifies the number of random points to be generated. The A argument is the linear constraint coefficient matrix. The b argument is the vector of right hand side values of the linear constraints. The L and U arguments are vectors of the lower and upper bounds for the variables, respectively. The neq, nle, and nge arguments are the number of equality constraints, the number of less than or equal constraints, and the number of greater than or equal constraints, respectively. The nwarm argument is the number of warm-up repetitions before points are written to the output matrix. The nstride argument is the number of repetitions between each point that is written to the output matrix. The tol argument is the tolerance. The G argument is a vector of indices that assigns the variables to constrained component subgroups where missing or zero values do not belong to a constrained subgroup. The LC and UC arguments are the lower and upper cardinality constraints for the constrained component subgroups, respectively. Note that the constraints must be listed as equality first, less than or equal next, and greater than or equal last.

**JMP Version Added:** 20

**Example 1**

``` jsl
A = [1 1 1, 1 2 0];
b = [1, 0.5];
L = [0, 0, 0.1];
U = [1, 1, 1];
points = Random Linearly Constrained Uniform( 2000, A, b, L, U, 1, 0, 1, 300, 50 );
dt = As Table( points );
tobj = Report( Ternary Plot( X( :Col1, :Col2, :Col3 ) ) );
tfr = tobj[scalebox( 1 )] << clone box;
New Window( "Example: Random Linearly Constrained Uniform",
    Outline Box( "Points on a Ternary Plot", tfr ),
    Outline Box( "Constraints",
        Text Box( "X1 + x2 + x3 = 1" ),
        Text Box( "X2 + 2*x2 >= 0.5" )
    ),
    Outline Box( "Variable Bounds",
        Text Box( "0 <= x1 <= 1" ),
        Text Box( "0 <= x2 <= 1" ),
        Text Box( ".1 < x3 <= 1" )
    )
);
Close( dt, no save );
Show( "see new window for example output" );
```

**Example 2**

``` jsl

A = [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1];
b = [100];
L = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
U = [100 100 95 90 100 85 100 90 60 70 75 70 75 100 95 60 80 95 100 100];
nwarm = 100;
nstride = 100;
tol = 1e-8;
// Index the constrained subgroups.  Index = 0 is not in a constrained subgroup.
G = [0 0 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 0 0];
// Lower cardinality constraints for the constrained subgroups
LC = [1 1];
// Upper cardinality constraints for the constrained subgroups
UC = [3 5];
points = Random Linearly Constrained Uniform(
    100,
    A,
    b,
    L,
    U,
    1,
    0,
    0,
    nwarm,
    nstride,
    tol,
    G,
    LC,
    UC
);
dt = As Table( points );
```

### [Random LogGenGamma](#random-loggengamma)[](#random-loggengamma "Click to copy url")

**Syntax:** y = Random LogGenGamma( \<mu=0\>, \<sigma=1\>, \<lambda=0\> )

**Description:** Returns a random number from a log generalized gamma distribution with parameters mu, sigma, and lambda.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random LogGenGamma( 2, 1.25 );
//produce a vector of random numbers
v = J( 1, 10, Random LogGenGamma( 2, 1.25 ) );
//show results
Show( x, v );
```

### [Random Logistic](#random-logistic)[](#random-logistic "Click to copy url")

**Syntax:** y = Random Logistic( \<mu=0\>, \<sigma=1\> )

**Description:** Returns a random number from a logistic distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Logistic( 15, 1 );
//produce a vector of random numbers
v = J( 1, 10, Random Logistic( 15, 1 ) );
//show results
Show( x, v );
```

### [Random Loglogistic](#random-loglogistic)[](#random-loglogistic "Click to copy url")

**Syntax:** y = Random Loglogistic( \<mu=0\>, \<sigma=1\> )

**Description:** Returns a random number from a loglogistic distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Loglogistic( 15, 1 );
//produce a vector of random numbers
v = J( 1, 10, Random Loglogistic( 15, 1 ) );
//show results
Show( x, v );
```

### [Random Lognormal](#random-lognormal)[](#random-lognormal "Click to copy url")

**Syntax:** y = Random Lognormal( \<mu=0\>, \<sigma=1\> )

**Description:** Returns a random number from a lognormal distribution with location parameter mu and scale parameter sigma.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl

//produce a single random number
x = Random Lognormal( -1, 1.5 );
//produce a vector of random numbers
v = J( 1, 10, Random Lognormal( -1, 1.5 ) );
//show results
Show( x, v );
```

**Example 2**

``` jsl
exrlnn = 30;
New Window( "Example: Random Lognormal and Empirical Distribution",
    exrlny = Graph Box(
        Y Scale( -0.05, 1.05 ),
        X Scale( -.05, 10 ),
        Pen Color( "red" );
        exranlnorm = J( Round( exrlnn ), 1, . );
        For( k = 1, k <= Round( exrlnn ), k++,
            exranlnorm[k] = Random Lognormal( -1, 1.5 )
        );
        exranlnorm = Sort Ascending( exranlnorm );
        H Line( 0, exranlnorm[1], 0 );
        For( k = 2, k <= Round( exrlnn ), k++,
            H Line( exranlnorm[k - 1], exranlnorm[k], (k - 1) / Round( exrlnn ) )
        );
        H Line( exranlnorm[Round( exrlnn )], 10, 1.0 );
        Pen Color( "blue" );
        Y Function( Normal Distribution( Log( tdeq ), -1, 1.5 ), tdeq );
        Text( {-4, 0.8}, " n=", Round( exrlnn ) );
    ),
    H List Box( Slider Box( 10, 2000, exrlnn, exrlny << reshow ), Text Box( " n" ) )
);
```

### [Random Multivariate Normal](#random-multivariate-normal)[](#random-multivariate-normal "Click to copy url")

**Syntax:** y = Random Multivariate Normal( mean, covar, \<nrows=1\>)

**Description:** Returns a random nrows by p matrix from a multivariate normal distribution with mean vector mean and (positive semi-definite) covariance matrix covar, where p is defined as the number of rows of covar.

**JMP Version Added:** 15

``` jsl
meanvec = 1 :: 3;
covar = [1 .6 .6, .6 1 .6, .6 .6 1];
randmvnRow = Random Multivariate Normal( meanvec, covar );
randmvnMat = Random Multivariate Normal( meanvec, covar, 10 );
```

### [Random Negative Binomial](#random-negative-binomial)[](#random-negative-binomial "Click to copy url")

**Syntax:** y = Random Negative Binomial( r, p )

**Description:** Returns a random number of non-events until r events occur, for events with probability p.

**JMP Version Added:** Before version 14

``` jsl
exnbpp = 0.3;
exnbpn = 20;
exnbrn = Random Negative Binomial( 20, 0.3 );
New Window( "Example: Neg Binomial Probability",
    exnbpy = Graph Box(
        Y Scale( 0, 0.04 ),
        X Scale( -1, 100 ),
        Pen Color( "red" ),
        Pen Size( 2 );
        For( exnbpk = 0, exnbpk < 1000, exnbpk++,
            V Line( exnbpk, 0, Neg Binomial Probability( exnbpp, exnbpn, exnbpk ) )
        );
        Pen Color( "blue" );,
        Pen Size( 4 ),
        V Line( exnbrn, 0, Neg Binomial Probability( exnbpp, exnbpn, exnbrn ) );
        Text( {1, 0.035}, "n=", Round( exnbpn ), " p=", Round( exnbpp, 2 ) );
        Text(
            {1, 0.030},
            "x=",
            Round( exnbrn, 2 ),
            " Prob=",
            Round( Neg Binomial Probability( exnbpp, exnbpn, exnbrn ), 2 )
        );
    ),
    H List Box(
        Button Box( "Generate a Random Negative Binomial Number",
            exnbrn = Random Negative Binomial( 20, 0.3 );
            exnbpy << reshow;
        )
    )
);
```

### [Random Normal](#random-normal)[](#random-normal "Click to copy url")

**Syntax:** y = Random Normal( \<mu=0\>, \<sigma=1\> )

**Description:** Returns a random number from a normal distribution with mean mu and standard deviation sigma.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl

//produce a single random number
x = Random Normal();
//produce a vector of random numbers
v = J( 1, 10, Random Normal() );
//show results
Show( x, v );
```

**Example 2**

``` jsl
exGcoordX = J( 50, 1, . );
exGcoordY = J( 50, 1, . );
For( k = 1, k <= 50, k++,
    exGcoordX[k] = Random Uniform( -5, 5 )
);
For( k = 1, k <= 50, k++,
    exGcoordY[k] = exGcoordX[k] + Random Normal()
);
New Window( "Random Normal, Linear Regression, and Outlier",
    V List Box(
        Graph Box(
            framesize( 600, 300 ),
            X Scale( -10, 10 ),
            Y Scale( 1.5 * Min( exGcoordY ), 1.5 * Max( exGcoordY ) ),
            double buffer,
            exsx = Sum( exGcoordX ),
            exsy = Sum( exGcoordY ),
            exsxx = Sum( (exGcoordX) ^ 2 );
            exsxy = Sum( exGcoordX :* exGcoordY );
            exbeta1 = (100 * exsxy - exsx * exsy) / (100 * exsxx - exsx * exsx);
            exbeta0 = (exsy - exbeta1 * exsx) / 100;
            exx1 = Min( exGcoordX );
            exy1 = exbeta0 + exbeta1 * Min( exGcoordX );
            exx2 = Max( exGcoordX );
            exy2 = exbeta0 + exbeta1 * Max( exGcoordX );
            Line( {exx1, exy1}, {exx2, exy2} );
            Marker Size( 5 );
            Drag Marker( exGcoordX, exGcoordY );
            Drag Text( [-7], [-5], "drag any marker" );
        )
    )
);
```

### [Random Normal Mixture](#random-normal-mixture)[](#random-normal-mixture "Click to copy url")

**Syntax:** y = Random Normal Mixture( meanvec, sdvec, probvec )

**Description:** Returns a random number from a normal mixture distribution with group means meanvec, group standard deviations sdvec, and group probabilities probvec.

**JMP Version Added:** Before version 14

``` jsl
dt = New Table( "Example",
    New Column( "Rand NM",
        set formula( Random Normal Mixture( [-3, 3], [1, 1], [.3, .7] ) )
    )
);
dt << add rows( 1000 );
Distribution( Continuous Distribution( Column( :Rand NM ), Vertical( 0 ) ) );
```

### [Random Poisson](#random-poisson)[](#random-poisson "Click to copy url")

**Syntax:** y = Random Poisson( lambda )

**Description:** Returns a random number from a Poisson distribution.

**JMP Version Added:** Before version 14

``` jsl
exrpoilambda = 20;
exrpoilsz = Log( 300 );
New Window( "Example: Random Poisson and Empirical Distribution",
    exrpoiy = Graph Box(
        Y Scale( 0, 1.05 ),
        X Scale( -1, 50 ),
        Pen Color( "red" ),
        Pen Size( 1 );
        exrpoisz = Round( Exp( exrpoilsz ) );
        exrpoisamp = J( Round( exrpoisz ), 1, . );
        exrpoifreq = J( Round( 50 + 1 ), 1, . );
        For( exrpoik = 1, exrpoik <= Round( exrpoisz ), exrpoik++,
            exrpoisamp[exrpoik] = Random Poisson( exrpoilambda )
        );
        For( exrpoik = 0, exrpoik <= 50, exrpoik++,
            exrpoifreq[exrpoik + 1] = Sum( exrpoisamp <= exrpoik ) / Round( exrpoisz )
        );
        exrpoitmp1 = 0;
        exrpoitmp2 = 0;
        For( exrpoik = 0, exrpoik < 50, exrpoik++,
            H Line( exrpoik, exrpoik + 1, Poisson Distribution( exrpoilambda, exrpoik ) );
            V Line(
                exrpoik + 1,
                Poisson Distribution( exrpoilambda, exrpoik ),
                Poisson Distribution( exrpoilambda, exrpoik + 1 )
            );
        );
        Pen Color( "blue" );
        For( exrpoik = 0, exrpoik < 50, exrpoik++,
            H Line( exrpoik, exrpoik + 1, exrpoifreq[exrpoik + 1] );
            V Line( exrpoik + 1, exrpoifreq[exrpoik + 1], exrpoifreq[exrpoik + 2] );
        );
        Text(
            {10, 0.2},
            " \!U03BB=",
            Round( exrpoilambda, 2 ),
            " sample size=",
            Round( exrpoisz )
        );
    ),
    H List Box(
        Slider Box( Log( 10 ), Log( 5000 ), exrpoilsz, exrpoiy << reshow ),
        Text Box( " random sample size" )
    )
);
```

### [Random Reset](#random-reset)[](#random-reset "Click to copy url")

**Syntax:** Random Reset( seed number )

**Description:** Restarts the random sequences with a new seed.

**JMP Version Added:** Before version 14

``` jsl
Random Reset( 1 );
Random Normal();
```

### [Random SEV](#random-sev)[](#random-sev "Click to copy url")

**Syntax:** y = Random SEV( \<mu=0\>, \<sigma=1\> )

**Description:** Returns a random number from a SEV distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random SEV( 50, 5 );
//produce a vector of random numbers
v = J( 1, 10, Random SEV( 50, 5 ) );
//show results
Show( x, v );
```

### [Random SHASH](#random-shash)[](#random-shash "Click to copy url")

**Syntax:** y = Random SHASH( gamma, delta, theta, sigma )

**Description:** Returns a random number from the sinh-arcsinh (SHASH) distribution.

**JMP Version Added:** 14

**Example 1**

``` jsl

//produce a single random number
x = Random SHASH( 0, 1, 0, 1 );
//produce a vector of random numbers
v = J( 1, 10, Random SHASH( 0, 1, 0, 1 ) );
//show results
Show( x, v );
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

### [Random Seed State](#random-seed-state)[](#random-seed-state "Click to copy url")

**Syntax:** Random Seed State( \<seed state\> )

**Description:** Retrieves or restores the random seed state to or from a blob object.

**JMP Version Added:** Before version 14

``` jsl
r = Random Seed State();
Random Seed State( r );
```

### [Random Shuffle](#random-shuffle)[](#random-shuffle "Click to copy url")

**Syntax:** y = Random Shuffle( matrix )

**Description:** Returns the matrix with the elements shuffled into a random order.

**JMP Version Added:** Before version 14

``` jsl
exA = [1 2 6, 3 5 8];
Random Shuffle( exA );
```

### [Random Triangular](#random-triangular)[](#random-triangular "Click to copy url")

**Syntax:** y = Random Triangular( a, b, c ); y = Random Triangular( b, c ); y = Random Triangular( b )

**Description:** Returns a random number from a triangular distribution with lower limit a, mode b, and upper limit c. Random Triangular(b,c) is equivalent to Random Triangular(0,b,c). Random Triangular(b) is equivalent to Random Triangular(0,b,1).

**JMP Version Added:** Before version 14

``` jsl
Random Reset( 13579 );
x = Random Triangular( 0.8 );
Random Reset( 13579 );
y = Random Triangular( 0, 0.8, 1 );
Show( x, y );
```

### [Random Uniform](#random-uniform)[](#random-uniform "Click to copy url")

**Syntax:** y = Random Uniform( \<min\>, \<max\> )

**Description:** Returns a random number from a uniform distribution between min and max, exclusive.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl

//produce a single random number
x = Random Uniform( 1, 10 );
//produce a vector of random numbers
v = J( 1, 10, Random Uniform( 1, 10 ) );
//show results
Show( x, v );
```

**Example 2**

``` jsl
Random Uniform( 1, 10 );
```

### [Random Weibull](#random-weibull)[](#random-weibull "Click to copy url")

**Syntax:** y = Random Weibull( beta, \<alpha=1\> )

**Description:** Returns a random number from a Weibull distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random Weibull( 3, 20 );
//produce a vector of random numbers
v = J( 1, 10, Random Weibull( 3, 20 ) );
//show results
Show( x, v );
```

### [Random ZI Negative Binomial](#random-zi-negative-binomial)[](#random-zi-negative-binomial "Click to copy url")

**Syntax:** y = Random ZI Negative Binomial( lambda, sigma, pi )

**Description:** Returns a random number from a zero-inflated Negative Binomial distribution with location parameter lambda, scale parameter sigma, and zero inflation parameter pi.

**JMP Version Added:** 19

**Example 1**

``` jsl
exnbpp = 0.3;
exnbpn = 20;
rnb = Random ZI Negative Binomial( 25, .5, .05 );
New Window( "Example: Zero Inflated Negative Binomial",
    exnbpy = Graph Box(
        Y Scale( 0, 0.075 ),
        X Scale( -1, 100 ),
        Pen Color( "red" ),
        Pen Size( 2 );
        For( i = 0, i < 100, i++,
            V Line( i, 0, ZI Negative Binomial Probability( i, 25, .5, .05 ) )
        );
        Pen Color( "blue" );,
        Pen Size( 4 ),
        V Line( rnb, 0, ZI Negative Binomial Probability( rnb, 25, .5, .05 ) );
        Text(
            {25, 0.06},
            "lambda=",
            Round( 25 ),
            ", sigma=",
            Round( .5, 2 ),
            ", pi=",
            Round( .05, 2 )
        );
        Text(
            {25, 0.05},
            "x=",
            Round( rnb, 2 ),
            ", Prob=",
            Round( ZI Negative Binomial Probability( rnb, 25, .5, .05 ), 4 )
        );
    ),
    H List Box(
        Button Box( "Generate a Random Zero Inflated Negative Binomial Number",
            rnb = Random ZI Negative Binomial( 25, .5, .05 );
            exnbpy << reshow;
        )
    )
);
```

**Example 2**

``` jsl
Random Reset( 19 );
dt = As Table( J( 1000, 1, Random ZI Negative Binomial( 5, 2, .2 ) ) );
Column( 1 ) << set name( "Random ZiNB" );
dt << Distribution(
    Continuous Distribution(
        Column( :Random ZiNB ),
        Vertical( 0 ),
        Fit ZI Negative Binomial,
        CDF Plot( 1 )
    )
);
```

### [Random ZI Poisson](#random-zi-poisson)[](#random-zi-poisson "Click to copy url")

**Syntax:** y = Random ZI Poisson Binomial( lambda, pi )

**Description:** Returns a random number from a zero-inflated Poisson distribution with location parameter lambda and zero inflation parameter pi.

**JMP Version Added:** 19

**Example 1**

``` jsl
exnbpp = 0.3;
exnbpn = 20;
rp = Random ZI Poisson( 20, .05 );
New Window( "Example: Zero Inflated Poisson",
    exnbpy = Graph Box(
        Y Scale( 0, 0.1 ),
        X Scale( -1, 60 ),
        Pen Color( "red" ),
        Pen Size( 2 );
        For( i = 0, i < 100, i++,
            V Line( i, 0, ZI Poisson Probability( i, 20, .05 ) )
        );
        Pen Color( "blue" );,
        Pen Size( 4 ),
        V Line( rp, 0, ZI Poisson Probability( rp, 20, .05 ) );
        Text( {30, 0.06}, "lambda=", Round( 20 ), ", pi=", Round( .05, 2 ) );
        Text(
            {30, 0.05},
            "x=",
            Round( rp, 2 ),
            ", Prob=",
            Round( ZI Poisson Probability( rp, 20, .05 ), 4 )
        );
    ),
    H List Box(
        Button Box( "Generate a Random Zero Inflated Poisson Number",
            rp = Random ZI Poisson( 20, .05 );
            exnbpy << reshow;
        )
    )
);
```

**Example 2**

``` jsl
Random Reset( 19 );
dt = As Table( J( 1000, 1, Random ZI Poisson( 5, .2 ) ) );
Column( 1 ) << set name( "Random ZIP" );
dt << Distribution(
    Continuous Distribution(
        Column( :Random ZIP ),
        Vertical( 0 ),
        Fit ZI Poisson,
        CDF Plot( 1 )
    )
);
```

### [Random t](#random-t)[](#random-t "Click to copy url")

**Syntax:** y = Random t( df, \<nonCentrality=0\> )

**Description:** Returns a random number from an t distribution.

**JMP Version Added:** Before version 14

``` jsl

//produce a single random number
x = Random t( 2 );
//produce a vector of random numbers
v = J( 1, 10, Random t( 2 ) );
//show results
Show( x, v );
```

### [Resample Freq](#resample-freq)[](#resample-freq "Click to copy url")

**Syntax:** Resample Freq( \<rate=1\>, \<column\> )

**Description:** Generates a frequency count for sampling with replacement, useful for bootstrap samples. With no arguments, the function generates a 100% resample. The rate argument specifies the rate of resampling. If the column argument is specified, the sample size chosen is rate multiplied by the sum of the specified column. A negative rate signals that fractional frequencies are allowed.

**JMP Version Added:** Before version 14

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
New Column( "Freq", numeric, formula( Resample Freq() ) );
New Window( "w", theBox = V List Box() );
For( i = 1, i <= 30, i++,
    Column( "Freq" ) << EvalFormula;
    theBox << append(
        V List Box( Bivariate( Y( :height ), X( :weight ), Freq( :Freq ), Fit Line( 1 ) ) )
    );
);
newDt = theBox["Parameter Estimates", Table Box( 1 )] << MakeCombinedDataTable;
newDt << Distribution( Y( :Estimate ), By( :Term ), Horizontal Layout( 1 ) );
theBox << CloseWindow;
```

[ Previous](R.html "R") [Next ](Row%20State.html "Row State")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
