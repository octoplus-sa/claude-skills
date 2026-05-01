# Matrix

*Source: [https://jsl.jmp.com/All%20Categories/Functions/Matrix.html](https://jsl.jmp.com/All%20Categories/Functions/Matrix.html)*

---

# [Matrix](#matrix)[](#matrix "Click to copy url")

### [Add Vectors BLAS](#add-vectors-blas)[](#add-vectors-blas "Click to copy url")

**Syntax:** z = Add Vectors BLAS( x, y, alpha )

**JMP Version Added:** 17

``` jsl
x = [1, 2, 3, 4];
y = [5, 6, 7, 8];
alpha = 0.5;
z = Add Vectors BLAS( x, y, alpha );
```

### [All](#all)[](#all "Click to copy url")

**Syntax:** y = All( x, ... )

**Description:** Returns 1 if all elements are nonzero, zero otherwise.

**JMP Version Added:** Before version 14

``` jsl
All( [1 2 3] );
```

### [Any](#any)[](#any "Click to copy url")

**Syntax:** y = Any( x, ... )

**Description:** Returns 1 if any element is nonzero, zero otherwise.

**JMP Version Added:** Before version 14

``` jsl
Any( [1 0 2] );
```

### [B Spline Coef](#b-spline-coef)[](#b-spline-coef "Click to copy url")

**Syntax:** coef = B Spline Coef( x, Internal Knot Grid, \<degree = 3\>, \<KnotEndPoints = min(x) \|\| max(x)\> )

**Description:** Returns the matrix of B-Spline coefficients. Internal Knot Grid is either the number of desired knot points based on percentiles of x or a vector specifying the internal knot points. Optional parameter degree specifies the degree of the B-splines with a default of 3. Optional parameter KnotEndPoints takes a 2x1 matrix containing \[lower, upper\] locations for the knots on the boundary. The knot end points default to the min and max of x. The second example demonstrates how B-spline coefficients can be used as the design matrix in a linear model.

**JMP Version Added:** 14

**Example 1**

``` jsl
B Spline Coef( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2 );
B Spline Coef( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 7] );
```

**Example 2**

``` jsl
xx = (0 :: 10)`;
yy = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0];
designMat = B Spline Coef( xx, 2 );
Linear Regression( yy, designMat, <<nointercept );
```

### [CDF](#cdf)[](#cdf "Click to copy url")

**Syntax:** {QuantVec, CumProbVec} = CDF( Y )

**Description:** Returns values of the empirical cumulative probability distribution function for vector or list Y. Cumulative probability is the proportion of data values less than or equal to the corresponding entry in vector QuantVec

**JMP Version Added:** Before version 14

``` jsl
/* Generate random values, Normal(0,1) */
Y = J( 150, 1, Random Normal() );

/* CDF function */
{Quant, CumProb} = CDF( Y ); 

/* Draw empirical and theorical CDF */
New Window( "Empirical CDF",
    Graph Box(
        X Scale( -3, 3 ),
        Y Scale( 0, 1 ),
        Pen Color( "red" );
        For( i = 2, i <= N Row( Quant ), i++,
            H Line( Quant[i - 1], Quant[i], CumProb[i] );
            V Line( Quant[i - 1], CumProb[i - 1], CumProb[i] );
        );
        i = N Row( Quant );
        V Line( Quant[i], CumProb[i], 1 );
        Pen Color( "blue" );
        Y Function( Normal Distribution( q ), q );
    )
);
```

### [Chol Update](#chol-update)[](#chol-update "Click to copy url")

**Syntax:** L2 = Chol Update( L, V, C )

**Description:** Returns an updated Cholesky root of A+V\*C\*V' where C is an m by m symmetric matrix and V is an n by m matrix. The argument L must be the Cholesky root of an n by n matrix A.

**JMP Version Added:** Before version 14

``` jsl
/* The inner product of a design matrix */
exS = [16 1 0 11 -1 12,
1 11 -1 1 -1 1,
0 -1 12 -1 1 0,
11 1 -1 11 -1 9,
-1 -1 1 -1 9 -1,
12 1 0 9 -1 12];
/* Conduct the Cholesky decomposition */
exAchol = Cholesky( exS );

/* Two column vectors to be applied to change the design matrix */
exV = [1 1, 0 0, 0 1, 0 0, 0 0, 0 1];

/* The first column vector is added to one of the rows in the design matrix */
/* The second column vector is subtracted from one of the rows in the design matrix */
exC = [1 0, 0 -1];

/* Update the Cholesky decomposition manually */
exAnew = exS + exV * exC * exV`;
exAcholnew = Cholesky( exAnew );

/* Update the Cholesky decomposition more efficiently */
exAcholnew_test = Chol Update( exAchol, exV, exC );

/* Results are the same */
Show( exAcholnew_test );
Show( exAcholnew );
```

### [Cholesky](#cholesky)[](#cholesky "Click to copy url")

**Syntax:** L = Cholesky( A )

**Description:** Returns the Cholesky decomposition of a positive semi-definite matrix. L is a lower triangular matrix such that L\*L\` = A.

**JMP Version Added:** Before version 14

``` jsl
Cholesky( [1 2, 2 13] );
```

### [Correlation](#correlation)[](#correlation "Click to copy url")

**Syntax:** y = Correlation( x , \< \<\<"Pairwise" \>, \< \<\<"Shrink" \>, \< \<\<Freq(vector) \>, \< \<\<Weight(vector) \> )

**Description:** Returns the correlation matrix of the matrix argument x. The "Pairwise" argument handles missing values in pairwise rather than rowwise fashion. The "Shrink" argument reduces the off-diagonal elements by a factor that is determined using the method described in Schafer and Strimmer, 2005. The Freq and Weight arguments specify vectors of frequency or weight values, respectively.

**JMP Version Added:** Before version 14

``` jsl
Correlation( [1 3 5, 3 2 6, 5 6 1] );
```

### [Covariance](#covariance)[](#covariance "Click to copy url")

**Syntax:** y = Covariance( x , \< \<\<"Pairwise" \>, \< \<\<"Shrink" \>, \< \<\<Freq(vector) \>, \< \<\<Weight(vector) \> )

**Description:** Returns the covariance matrix of the matrix argument x. The "Pairwise" argument handles missing values in pairwise rather than rowwise fashion. The "Shrink" argument reduces the off-diagonal elements by a factor that is determined using the method described in Schafer and Strimmer, 2005. The Freq and Weight arguments specify vectors of frequency or weight values, respectively.

**JMP Version Added:** Before version 14

``` jsl
Covariance( [1 3 5, 3 2 6, 5 6 1] );
```

### [Design](#design)[](#design "Click to copy url")

**Syntax:** y = Design( v, \< levelsList\|\<\<Levels, \<\<ElseMissing \> )

**Description:** Creates a design matrix that contains a column of 1s and 0s for each unique value of the argument. Use the levelsList argument to specify a list of the levels for the design matrix. If the \<\<Levels argument is specified, the return value is a list that contains the design matrix and a list of the levels. If the \<\<ElseMissing argument is specified, missing values are placed in the design matrix for values in the v argument that do not appear in the levelsList. Otherwise, 0s are placed in the design matrix.

**JMP Version Added:** Before version 14

``` jsl
/* example that Design(...) takes one argument */
exLevels = [1, 2, 3, 2, 1];
Show( Design( exLevels ) );
/* Also see DesignNom, DesignOrd */

/* example that Design(...) takes two arguments */
Show( Design( 3, {1, 2, 3} ) );
Show( Design( [1 2], {1, 2, 3} ) );
exLevels = [1, 2, 3, 2, 1, 2, 3];
Show( Design( exLevels, {1, 2, 3} ) );
Show( Design( {"a", "b"}, {"a", "b", "c"} ) );

/* example that Design(...) takes three arguments */
Show( Design( [1, 2, 3, 4, 5], {1, 2, 3, 4}, <<ElseMissing ) );
Show( Design( [1, 2, 3, 4, 5], {1, 2, 3, 4} ) );
```

### [Design Last](#design-last)[](#design-last "Click to copy url")

**Syntax:** y = Design Last( v, \< levelsList, \<\<ElseMissing \> )

**Description:** Creates a design matrix that contains a column of 1s and 0s for all but the last of the unique values of the argument. The last level is coded as a row of 0s. If the levelsList argument is specified, the last level is the last level in levelsList. Otherwise, the last level is defined as the largest value in v. If the \<\<Levels argument is specified, the return value is a list that contains the design matrix and a list of the levels. If the \<\<ElseMissing argument is specified, missing values are placed in the design matrix for values in the v argument that do not appear in the levelsList. Otherwise, 0s are placed in the design matrix.

**JMP Version Added:** Before version 14

``` jsl
/* example that Design Last(...) takes one argument */
exLevels = [1, 2, 3, 2, 1];
Show( Design Last( exLevels ) );
/* see what is different from Design(...) */
Show( Design( exLevels ) );

/* Also see Design, DesignOrd */

/* example that Design Last(...) takes two arguments */
Show( Design Last( 3, {1, 2, 3} ) );
Show( Design( 3, {1, 2, 3} ) );
Show( Design Last( [1 2], {1, 2, 3} ) );
Show( Design( [1 2], {1, 2, 3} ) );
exLevels = [1, 2, 3, 2, 1, 2, 3];
Show( Design Last( exLevels, {1, 2, 3} ) );
Show( Design( exLevels, {1, 2, 3} ) );
Show( Design Last( {"a", "b"}, {"a", "b", "c"} ) );
Show( Design( {"a", "b"}, {"a", "b", "c"} ) );

/* example that Design Last(...) takes three arguments */
Show( Design Last( [1, 2, 3, 4, 5], {1, 2, 3, 4}, <<ElseMissing ) );
Show( Design Last( [1, 2, 3, 4, 5], {1, 2, 3, 4} ) );
```

### [Design Nom](#design-nom)[](#design-nom "Click to copy url")

**Syntax:** y = Design Nom( v, \< levelsList\|\<\<Levels, \<\<ElseMissing \> )

**Description:** Creates a design matrix that contains a column of 1s and 0s for all but the last of the unique values of the argument. The last level is coded as a row of -1s. If the levelsList argument is specified, the last level is the last level in levelsList. Otherwise, the last level is defined as the largest value in v. If the \<\<Levels argument is specified, the return value is a list that contains the design matrix and a list of the levels. If the \<\<ElseMissing argument is specified, missing values are placed in the design matrix for values in the v argument that do not appear in the levelsList. Otherwise, 0s are placed in the design matrix.

**JMP Version Added:** Before version 14

``` jsl
/* example that Design Nom(...) takes one argument */
exLevels = [1, 2, 3, 2, 1];
Show( Design Nom( exLevels ) );
/* see what is different from Design(...) */
Show( Design( exLevels ) );

/* Also see Design, DesignOrd */

/* example that Design Nom(...) takes two arguments */
Show( Design Nom( 3, {1, 2, 3} ) );
Show( Design( 3, {1, 2, 3} ) );
Show( Design Nom( [1 2], {1, 2, 3} ) );
Show( Design( [1 2], {1, 2, 3} ) );
exLevels = [1, 2, 3, 2, 1, 2, 3];
Show( Design Nom( exLevels, {1, 2, 3} ) );
Show( Design( exLevels, {1, 2, 3} ) );
Show( Design Nom( {"a", "b"}, {"a", "b", "c"} ) );
Show( Design( {"a", "b"}, {"a", "b", "c"} ) );

 /* example that Design Nom(...) takes three arguments */
Show( Design Nom( [1, 2, 3, 4, 5], {1, 2, 3, 4}, <<ElseMissing ) );
Show( Design Nom( [1, 2, 3, 4, 5], {1, 2, 3, 4} ) );
```

### [Design Ord](#design-ord)[](#design-ord "Click to copy url")

**Syntax:** y = Design Ord( v, \< levelsList\|\<\<Levels, \<\<ElseMissing \> )

**Description:** Creates a design matrix that contains a column for all but the last of the unique values of the argument. The first level is coded as a row of 0s. Each subsequent (nth) level in the levelsList argument is coded as a row of (n-1) 1s and the rest 0s. If the \<\<Levels argument is specified, the return value is a list that contains the design matrix and a list of the levels. If the \<\<ElseMissing argument is specified, missing values are placed in the design matrix for values in the v argument that do not appear in the levelsList. Otherwise, 0s are placed in the design matrix.

**JMP Version Added:** Before version 14

``` jsl
/* example that Design Ord(...) takes one argument */
exLevels = [1, 2, 3, 2, 1];
Show( Design Ord( exLevels ) );
/* see what is different from Design Nom(...) */
Show( Design Nom( exLevels ) );

/* Also see Design, Design Nom */

/* example that Design Ord(...) takes two arguments */
Show( Design Ord( 3, {1, 2, 3} ) );
Show( Design Nom( 3, {1, 2, 3} ) );
Show( Design Ord( [1 2], {1, 2, 3} ) );
Show( Design Nom( [1 2], {1, 2, 3} ) );
exLevels = [1, 2, 3, 2, 1, 2, 3];
Show( Design Ord( exLevels, {1, 2, 3} ) );
Show( Design Nom( exLevels, {1, 2, 3} ) );
Show( Design Ord( {"a", "b"}, {"a", "b", "c"} ) );
Show( Design Nom( {"a", "b"}, {"a", "b", "c"} ) );

/* example that Design Ord(...) takes three arguments */
Show( Design Ord( [1, 2, 3, 4, 5], {1, 2, 3, 4}, <<ElseMissing ) );
Show( Design Ord( [1, 2, 3, 4, 5], {1, 2, 3, 4} ) );
```

### [DesignF](#designf)[](#designf "Click to copy url")

**Syntax:** y = DesignF( v, \< levelsList\|\<\<Levels, \<\<ElseMissing \> )

**Description:** Creates a design matrix that contains a column of 1s and 0s for all but the last of the unique values of the argument. The last level is coded as a row of -1s. If the levelsList argument is specified, the last level is the last level in levelsList. Otherwise, the last level is defined as the largest value in v. If the \<\<Levels argument is specified, the return value is a list that contains the design matrix and a list of the levels. If the \<\<ElseMissing argument is specified, missing values are placed in the design matrix for values in the v argument that do not appear in the levelsList. Otherwise, 0s are placed in the design matrix.

**JMP Version Added:** Before version 14

``` jsl
/* example that DesignF(...) takes one argument */
exLevels = [1, 2, 3, 2, 1];
Show( DesignF( exLevels ) );
/* see what is different from Design(...) */
Show( Design( exLevels ) );

/* Also see Design, DesignOrd */

/* example that DesignF(...) takes two arguments */
Show( DesignF( 3, {1, 2, 3} ) );
Show( Design( 3, {1, 2, 3} ) );
Show( DesignF( [1 2], {1, 2, 3} ) );
Show( Design( [1 2], {1, 2, 3} ) );
exLevels = [1, 2, 3, 2, 1, 2, 3];
Show( DesignF( exLevels, {1, 2, 3} ) );
Show( Design( exLevels, {1, 2, 3} ) );
Show( DesignF( {"a", "b"}, {"a", "b", "c"} ) );
Show( Design( {"a", "b"}, {"a", "b", "c"} ) );

/* example that DesignF(...) takes three arguments */
Show( DesignF( [1, 2, 3, 4, 5], {1, 2, 3, 4}, <<ElseMissing ) );
Show( DesignF( [1, 2, 3, 4, 5], {1, 2, 3, 4} ) );
```

### [Det](#det)[](#det "Click to copy url")

**Syntax:** y = Det( x )

**Description:** Returns the determinant of a square matrix.

**JMP Version Added:** Before version 14

``` jsl
Det( [11 22, 33 44] );
```

### [Diag](#diag)[](#diag "Click to copy url")

**Syntax:** y = Diag( matrix ); y = Diag( vector ); y = Diag( matrix1, matrix )

**Description:** Constructs a diagonal matrix from either a matrix or a vector. If two arguments are specified, the function returns the concatenation of the matrices diagonally.

**JMP Version Added:** Before version 14

``` jsl
Diag( [11 22] );
```

### [Direct Product](#direct-product)[](#direct-product "Click to copy url")

**Syntax:** y = Direct Product( A, B )

**Description:** Returns the direct or Kronecker product. Result has A\[i,j\]\*B, expanding to all possible products.

**JMP Version Added:** Before version 14

``` jsl
exA = [1 2, 3 4];
exB = [1 1 1, 2 2 2, 3 3 3];
exProd = Direct Product( exA, exB );
Show( exProd );

/* verify results */
Show( exProd[1 :: 3, 1 :: 3] == exB );
Show( exProd[4 :: 6, 1 :: 3] == (exB * 3) );
Show( exProd[1 :: 3, 4 :: 6] == (exB * 2) );
Show( exProd[4 :: 6, 4 :: 6] == (exB * 4) );

/* Also see H Direct Product */
```

### [Distance](#distance)[](#distance "Click to copy url")

**Syntax:** y = Distance( x1, x2, \<scales\>, \<powers\> )

**Description:** Produces a matrix of distances between rows of x1 and rows of x2. To customize the scaling and powers for each column, specify the extra arguments scale and powers. For Kriging, Exp(-distance(x1,x2)) is used.

**JMP Version Added:** Before version 14

``` jsl
/*1-D example*/
exX1 = [1, 2, 3, 4];
exX2 = [2, 4, 6, 8]; 
/*Compute squared Euclidean distance*/
exD = Distance( exX1, exX2 ); 
/*Verify result*/
exDm = J( 4, 4, . );
For( exi = 1, exi <= 4, exi++,
    For( exj = 1, exj <= 4, exj++,
        exDm[exi, exj] = Sum( (exX1[exi, 0] - exX2[exj, 0]) ^ 2 )
    )
);
Show( exDm == exD ); 

/*2-D example*/
exX1 = [1 1, 2 2, 3 3, 4 4];
exX2 = [2 1, 4 2, 6 0, 8 7]; 
/*Compute squared Euclidean distance*/
exD = Distance( exX1, exX2 ); 
/*Verify result*/
exDm = J( 4, 4, . );
For( exi = 1, exi <= 4, exi++,
    For( exj = 1, exj <= 4, exj++,
        exDm[exi, exj] = Sum( (exX1[exi, 0] - exX2[exj, 0]) ^ 2 )
    )
);
Show( exDm == exD ); 

/*2-D example*/
exX1 = [1 1, 2 2, 3 3, 4 4];
exX2 = [2 1, 4 2, 6 0, 8 7]; 
/*Compute squared Euclidean distance, with a scaler [0.5 2.0]*/
exD = Distance( exX1, exX2, [0.5 2.0] ); 
/*Verify result*/
exDm = J( 4, 4, . );
For( exi = 1, exi <= 4, exi++,
    For( exj = 1, exj <= 4, exj++,
        exDm[exi, exj] = Sum( [0.5 2.0] :* (Abs( exX1[exi, 0] - exX2[exj, 0] ) ^ 2) )
    )
);
Show( exDm == exD ); 

/*2-D example*/
exX1 = [1 1, 2 2, 3 3, 4 4];
exX2 = [2 1, 4 2, 6 0, 8 7]; 
/*Compute squared Euclidean distance, with scalers [0.5 2.0] and powers [1.5 2.0]*/
exD = Distance( exX1, exX2, [0.5 2.0], [1.5 2.0] ); 
/*Verify result*/
exDm = J( 4, 4, . );
For( exi = 1, exi <= 4, exi++,
    For( exj = 1, exj <= 4, exj++,
        exDm[exi, exj] = Sum(
            [0.5 2.0] :* (Abs( exX1[exi, 0] - exX2[exj, 0] ) :^ [1.5 2.0])
        )
    )
);
Show( exDm == exD );
```

### [E Div](#e-div)[](#e-div "Click to copy url")

**Syntax:** y = A :/ B; y = E Div( A, B )

**Description:** Returns an element-wise division of matrices.

**JMP Version Added:** Before version 14

``` jsl
[11 22 33] :/ [1 2 3];
```

### [E Max](#e-max)[](#e-max "Click to copy url")

**Syntax:** y = E Max( A, B )

**Description:** Returns a matrix that is the maximum of corresponding elements of its arguments.

**JMP Version Added:** 16

``` jsl
E Max( [1 22 33], [11 2 3] );
```

### [E Min](#e-min)[](#e-min "Click to copy url")

**Syntax:** y = E Min( A, B )

**Description:** Returns a matrix that is the minimum of corresponding elements of its arguments.

**JMP Version Added:** 16

``` jsl
E Min( [1 22 33], [11 2 3] );
```

### [E Mult](#e-mult)[](#e-mult "Click to copy url")

**Syntax:** y = A :\* B; y = E Mult( A, B )

**Description:** Returns an element-wise multiplication of matrices.

**JMP Version Added:** Before version 14

``` jsl
[1 2 3] :* [11 22 33];
```

### [Eigen](#eigen)[](#eigen "Click to copy url")

**Syntax:** {M, E} = Eigen( X )

**Description:** Performs eigenvalue decomposition of symmetric matrix X. Returns list {M, E} such that E\*Diag(M)\*E\` = X.

**JMP Version Added:** Before version 14

``` jsl
X = [11 22, 22 33];
{M, E} = Eigen( X );
E * Diag( M ) * E`;
```

### [Eigen BLAS](#eigen-blas)[](#eigen-blas "Click to copy url")

**Syntax:** z = Eigen BLAS( X, \<nvec = ncol\> )

**JMP Version Added:** 17

``` jsl
X = [5 4 1 1, 4 5 1 1, 1 1 4 2, 1 1 2 4];
{M1, E1} = Eigen BLAS( X );
```

### [Estimate Bartlett Factor Score](#estimate-bartlett-factor-score)[](#estimate-bartlett-factor-score "Click to copy url")

**Syntax:** {factorScores} = Estimate Bartlett Factor Score( dataRow , mvMeanVec, lvMeanVec, modSRAM, modARAM )

**Description:** Estimates factor scores, using Bartlett's method, from a structural equation model (SEM). The input arguments are a row vector of data, the model-implied means for the manifest variables, the model-implied means for the latent variables, the S RAM matrix from an SEM, and the A RAM matrix from an SEM. It returns a row vector with estimated factor scores based on the SEM.

**JMP Version Added:** 16

``` jsl
Estimate Bartlett Factor Score(
    [2 2 0],
    [2.085 2.76 1.56],
    [0],
    [1 0 0 0 0,
    0 0.684181992749 0 0 0,
    0 0 1.19686444665695 0 0,
    0 0 0 0.875198112795068 0,
    0 0 0 0 0.953592961124492],
    [0 0 0 0 0,
    2.085 0 0 0 1,
    2.76 0 0 0 0.61913203807175,
    1.56 0 0 0 0.710365935511608,
    0 0 0 0 0]
);
```

### [Estimate Factor Score](#estimate-factor-score)[](#estimate-factor-score "Click to copy url")

**Syntax:** {factorScores} = Estimate Factor Score( dataRow , modImpVarCov, mvMeanVec, lvMeanVec )

**Description:** Estimates factor scores, using the regression method, from a structural equation model (SEM). The input arguments are a row vector of data, a model-implied variance-covariance matrix, a vector of model-implied manifest variable means, and a vector of model-implied latent variable means. It returns a row vector with estimated factor scores based on the SEM.

**JMP Version Added:** 15

``` jsl
Estimate Factor Score(
    [7 10 5 2 2 0],
    [1.66 0.45 0.58 -0.58 -0.44 -0.5 0.59 -0.58,
    0.45 1.22 0.44 -0.44 -0.33 -0.38 0.45 -0.44,
    0.58 0.44 1.88 -0.57 -0.43 -0.49 0.58 -0.57,
    -0.58 -0.44 -0.57 1.64 0.57 0.65 -0.58 0.76,
    -0.44 -0.33 -0.43 0.57 1.56 0.49 -0.44 0.57,
    -0.5 -0.38 -0.49 0.65 0.49 1.36 -0.5 0.65,
    0.59 0.45 0.58 -0.58 -0.44 -0.5 0.59 -0.58,
    -0.58 -0.44 -0.57 0.76 0.57 0.65 -0.58 0.76],
    [6.59, 8.81, 2.92, 2.09, 2.76, 1.56],
    [0, 0]
);
```

### [Fourier Basis Coef](#fourier-basis-coef)[](#fourier-basis-coef "Click to copy url")

**Syntax:** coef = Fourier Basis Coef( x, Number Pairs, \<Period = max(x)-min(x)+1\> )

**Description:** Returns the matrix of Fourier Basis coefficients. Number Pairs is the number of sin() and cos() pairs for the basis. Optional parameter Period specifies the period for the trigonometric functions and defaults to max(x) - min(x) + 1.

**JMP Version Added:** 14

``` jsl
Fourier Basis Coef( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] / 10, 2 );
Fourier Basis Coef( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] / 10, 2, 2 );
```

### [G Inverse](#g-inverse)[](#g-inverse "Click to copy url")

**Syntax:** g = G Inverse( A )

**Description:** Returns the generalized (Moore-Penrose) matrix inverse.

**JMP Version Added:** Before version 14

``` jsl
Round( G Inverse( [11 22, 33 44] ), 2 );
```

### [H Direct Product](#h-direct-product)[](#h-direct-product "Click to copy url")

**Syntax:** y = H Direct Product( A, B )

**Description:** Returns the horizontal direct product, which is the direct product of each row of matrices A and B.

**JMP Version Added:** Before version 14

``` jsl
exA = [1 2, 3 4];
exB = [1 1 1, 2 2 2];
exProd = H Direct Product( exA, exB );
Show( exProd );

/* verify result */
Show( exProd[1, 1 :: 6] == Direct Product( exA[1, 1 :: 2], exB[1, 1 :: 3] ) );
Show( exProd[2, 1 :: 6] == Direct Product( exA[2, 1 :: 2], exB[2, 1 :: 3] ) );
```

### [Hadamard](#hadamard)[](#hadamard "Click to copy url")

**Syntax:** y = Hadamard( n, \<normalize = 0\> )

**Description:** Creates a Hadamard matrix of order n.

**JMP Version Added:** 15

``` jsl
Show( Hadamard( 12 ), Hadamard( 12, 1 ) );
```

### [Hough Line Transform](#hough-line-transform)[](#hough-line-transform "Click to copy url")

**Syntax:** accum = Hough Line Transform( matrix, \<NAngle(number)\> \<NRadius(number)\> )

**Description:** Returns the Hough transform for detecting lines in image data

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
xx = .4;
yy = .4;
angleDegrees = (1 :: 180)`;
angle = Pi() * angleDegrees / (180);
New Window( "Hough Transform Demo 1",
    Border Box( Left( 20 ), Top( 20 ), Right( 15 ), Bottom( 15 ),
        V List Box(
            Text Box( "Click and drag the circle in a straight line." ),
            Graph Box(
                X Scale( -1, 1 ),
                Y Scale( -1, 1 ),
                Circle( {xx, yy}, .05 );
                Text( {xx + .1, yy + .1}, Char( xx, 4 ) || " " || Char( yy, 4 ) );
                Mousetrap(
                    xx = x;
                    yy = y;
                    gb << reshow;
                );
            ),
            Text Box( "For angle 1 to 180 , x*Cos(angle)+y*Sin(angle)" ),
            Text Box( "What position stays constant as you move?" ),
            gb = Graph Box(
                X Scale( 0, 180 ),
                XName( "Angle" ),
                Y Scale( -1.5, 1.5 ),
                YName( "Distance to Line" ),
                Line( angleDegrees, xx * Cos( angle ) + yy * Sin( angle ) )
            )
        )
    )
);
```

**Example 2**

``` jsl
nRow = 35;
nCol = 35;

// Make a wafer template missing outside a radius
waferTemplate = J( nRow, nCol, 0 );
If( 0,
    For( i = 1, i <= nRow, i++,
        For( j = 1, j <= nCol, j++,
            If( (i - nrow / 2) ^ 2 + (j - nCol / 2) ^ 2 > ((nRow + nCol) / 4) ^ 2,
                waferTemplate[i, j] = .
            )
        )
    )
);
wafer = waferTemplate;
wafer[5, 22] = 1;
lightGray = RGB Color( .9, .9, .9 );
showWafer = Expr(
    For( i = 1, i <= nRow, i++,
        For( j = 1, j <= nCol, j++,
            z = wafer[i, j];
            If( Is Missing( z ),
                Continue()
            );
            Fill Color( If( z == 0, lightGray, 3 ) );
            Rect( i - nrow / 2, j - nCol / 2, i - nrow / 2 - 1, j - nCol / 2 + 1, 1 );
        )
    )
);
showHough = Expr(
    accum = Hough Line Transform( wafer );
    maxAccum = Max( Max( accum ), 1 );
    accumHeat = Heat Color( accum / maxAccum );
    nr = N Row( accum );
    nc = N Col( accum );
    For( i = 1, i <= nr, i++,
        For( j = 1, j <= nc, j++,
            z = accumHeat[i, j];
            Fill Color( z );
            Rect( j - 1, nr - i, j, nr - i + 1, 1 );
        )
    );
    //Marginals
    radiusDensity = V Max( accum` );
    radiusScale = 3 * Max( radiusDensity ) / Mean( radiusDensity );
    radiusColor = Heat Color( radiusDensity / radiusScale );
    If( 1,
        angleDensity = V Max( accum );
        angleScale = 3 * Max( angleDensity ) / Mean( angleDensity );
        angleColor = Heat Color( angleDensity / angleScale );
    ,
        angle1 = angleDensity - Mean( angleDensity );
        angle1 = angle1 :* (angle1 > 0);
        angleColor = Heat Color( angle1 / Max( angle1 ) );
    );
    For( j = 1, j <= nc, j++,
        Fill Color( angleColor[j] );
        Rect( j - 1, -5, j, -8, 1 );
    );
    For( i = 1, i <= nr, i++,
        Fill Color( radiusColor[i] );
        Rect( 185, nr - i, 190, nr - i + 1, 1 );
    );
);
mouseAction = Expr(
    i = Floor( x + nrow / 2 + .5 );
    j = Floor( y + ncol / 2 + .5 );
    If( i > 0 & i <= nRow & j > 0 & j <= nCol,
        wafer[i, j]
        ++);
    bothBox << reshow;
);
New Window( "Hough Transform Demo 2",
    Border Box( Left( 15 ), Top( 15 ), Right( 10 ), Bottom( 10 ),
        bothBox = V List Box(
            Text Box( "Click to add points in the top frame along a slanted line." ),
            Text Box( "The Hough transform is shown below with marginal densities." ),
            Text Box( "" ),
            H List Box(
                Button Box( "Clear",
                    wafer = waferTemplate;
                    bothBox << Reshow;
                ),
                Button Box( "Add Random",
                    wafer = wafer | J( nRow, nCol, Random Uniform() < .05 );
                    bothBox << Reshow;
                )
            ),
            waferBox = Graph Box(
                X Scale( -18, 18 ),
                Y Scale( -18, 18 ),
                FrameSize( 300, 300 ),
                XName( "Angle" ),
                YName( "Radius" ),
                Mousetrap( mouseAction ),
                showWafer
            ),
            houghBox = Graph Box(
                X Scale( 0, 190 ),
                Y Scale( -10, 50 ),
                FrameSize( 500, 200 ),
                showHough
            )
        )
    )
);
```

### [Identity](#identity)[](#identity "Click to copy url")

**Syntax:** y = Identity( n )

**Description:** Creates an n-by-n identity matrix, with ones on diagonal, zeros elsewhere.

**JMP Version Added:** Before version 14

``` jsl
Identity( 2 );
```

### [Index](#index)[](#index "Click to copy url")

**Syntax:** ii = n1::n2; ii = n1::n2::n3; ii = Index( n1, n2, \<n3=1\>)

**Description:** Returns a row matrix that contains the sequence of values from n1 to n2 by increments of n3.

**JMP Version Added:** Before version 14

``` jsl
1 :: 10;
```

### [Inner Product BLAS](#inner-product-blas)[](#inner-product-blas "Click to copy url")

**Syntax:** y = Inner Product BLAS( A, B, ... )

**JMP Version Added:** 17

``` jsl
a = [1, 2, 3, -2, 0, -1, 0, 1, 1];
b = [4, 5, 6, -2, 0, -1, 0, 7, 2];
y = Inner Product BLAS( a, b );
```

### [Inv](#inv)[](#inv "Click to copy url")

**Syntax:** y = Inverse( x ); y = Inv( x )

**Description:** Returns the inverse of the x argument, which must be a square non-singular matrix.

**JMP Version Added:** Before version 14

``` jsl
Round( Inverse( [11 22, 33 44] ), 2 );
```

### [Inv Update](#inv-update)[](#inv-update "Click to copy url")

**Syntax:** y = Inv Update( S, X, \<w=1\> )

**Description:** Returns an updated inverse matrix, where the first argument S is a symmetric positive definite matrix with the same number of columns as X, the second argument X is a matrix that contains the rows to add or delete, and the third argument w determines whether to add or delete rows (use 1 to add rows and -1 to delete rows). This function evaluates as S-w\*S\*X`\*Inv(I+w\*X\*S\*X`)\*X\*S, where I is an identity matrix and Inv(A) means an inverse matrix of A.

**JMP Version Added:** Before version 14

``` jsl
/* Generate a design matrix */
exX = [1 0 4 2,
1 0 5 1,
1 0 2 4,
5 4 4 5,
0 1 4 3,
0 1 9 1,
0 1 2 4,
0 1 1 9,
0 1 5 2,
0 1 2 1,
0 1 4 5];
S = Inverse( exX` * exX );
Show( "----------Adding Rows (w=1) --------" );
X = [5 4 3 3, 4 3 2 1, 9 1 2 5];
w = 1;
y = Inv Update( S, X, w );
Show( "Result of Inv Update" );
Show( y );
Show( "Result of updating formula" );
Show( S - w * S * X` * Inv( Identity( N Row( X ) ) + w * X * S * X` ) * X * S );
Show( "Result of direct calculation" );
Show( Inverse( (exX |/ X)` * (exX |/ X) ) );
Show( "----------Deleting Rows (w=-1) --------" );
X = [0 1 5 2, 0 1 2 1, 0 1 4 5];
w = -1;
y = Inv Update( S, X, w );
Show( "Result of Inv Update" );
Show( y );
Show( "Result of updating formula" );
Show( S - w * S * X` * Inv( Identity( N Row( X ) ) + w * X * S * X` ) * X * S );
Show( "Result of direct calculation" );
p = N Row( exX ) - 3;
Show( Inverse( exX[Index( 1, p ), 0]` * exX[Index( 1, p ), 0] ) );
```

### [Inverse](#inverse)[](#inverse "Click to copy url")

**Syntax:** y = Inverse( x ); y = Inv( x )

**Description:** Returns the inverse of the x argument, which must be a square non-singular matrix.

**JMP Version Added:** Before version 14

``` jsl
Round( Inverse( [11 22, 33 44] ), 2 );
```

### [Is Matrix](#is-matrix)[](#is-matrix "Click to copy url")

**Syntax:** y = Is Matrix( x )

**Description:** Returns 1 if the argument is a matrix, 0 otherwise.

**JMP Version Added:** Before version 14

``` jsl
Is Matrix( [11 22 33] );
```

### [J](#j)[](#j "Click to copy url")

**Syntax:** y = J( nr, \<nc\>, \<v\> ); y = J( nr, nc ); y = J( n )

**Description:** Creates a matrix (nr by nc) of values that are determined by the third argument. The default value of the second argument equals the first argument. The default value of the third argument is 1. But the third argument can be a number, a variable name of a number, or JSL code. If the third argument is code, the code is evaluated and assigned the return value to every element in the matrix, element by element, row by row.

**JMP Version Added:** Before version 14

``` jsl

// Produce a 2x3 matrix, filled with 15.
m = J( 2, 3, 15 );
// Produce a default 4x4 matrix, filled with 1.
m = J( 4 );
// Produce a 2x3 matrix, filled with a number determined by a variable.
a = 3.14;
m = J( 2, 3, a );
// Produce a vector of random numbers from the Uniform distribution.
m = J( 1, 100, Random Uniform() );
// Produce a 2x3 matrix, filled with a sequence of integers.
a = 0;
m = J( 2, 3, a = a + 1 );
// This is a fun example to illustrate what is possible for the third argument.
i = 1;
J(
    10,
    1,
    Print(
        Eval Insert(
            "For the ^i^^if(i < 4, words(\!"st,nd,rd\!",\!",\!")[i], \!"th\!")^ time, I'm not a loop!"
        )
    );
    Round( 1 / Sqrt( 5 ) * ((1 + Sqrt( 5 )) / 2) ^ i++ );
);
```

### [KDTable](#kdtable)[](#kdtable "Click to copy url")

**Syntax:** tab = KDTable( \[ 1 1 1, 1 2 1, 1 2 2, 2 2 2, 3 3 3, 4 5 6 \] )

**Description:** Returns a table for efficiently looking up near neighbors. The matrix arguments are k-dimensional points. There is no built in limit on the number of dimensions or points.

**JMP Version Added:** Before version 14

``` jsl
tab = KDTable( [1 1 1, 1 2 1, 1 2 2, 2 2 2, 3 3 3, 4 5 6] );
{rows, dist} = tab << K nearest rows( 2, 1 );
"2 nearest rows to row 1 are " || Char( rows );
```

### [Least Squares Solve](#least-squares-solve)[](#least-squares-solve "Click to copy url")

**Syntax:** {Beta, VarBeta} = Least Squares Solve(y, X, \<\<noIntercept, \<\<weights(optionalWeightVector), \<\<method("Sweep"\|"GInv"))

**Description:** Returns a list that contains a vector of estimates, Beta = Inverse(X'X)X'y, and the estimated variance matrix of Beta. The optional \<\<noIntercept argument specifies a no-intercept model. The optional \<\<weights argument specifies a vector of weights to perform weighted least squares. The optional \<\<method argument enables you to choose between the default Sweep method and a generalized inverse ("GInv") method for solving the normal equations.

**JMP Version Added:** Before version 14

``` jsl
/*Simple Linear Regression*/
y = [3, 5, 7, 5];
X = [1, 2, 3, 4];
{Beta, VarBeta} = Least Squares Solve( y, X );
```

### [Linear Regression](#linear-regression)[](#linear-regression "Click to copy url")

**Syntax:** {Estimates, Std_Error, Diagnostics} = Linear Regression(y, X, \<\<noIntercept, \<\<printToLog, \<\<weight(WeightVector), \<\<freq(FrequencyVector)

**Description:** Fits a linear regression for the assumed model y = X \* beta + error. The optional \<\<noIntercept argument specifies a no-intercept model. The optional \<\<printToLog argument specifies that a summary of fit is printed to the log window. The optional weight argument specifies a vector of weights to perform weighted least squares, and the optional freq argument specifies a vector of frequencies. Returns a list containing a vector of the estimates, a vector of the standard errors, and a list of diagnostics. The list of diagnostics contains vectors of the t statistics and p-values for the estimates, as well as the R-Square and adjusted R-Square values for the regression fit.

**JMP Version Added:** 14

**Example 1**

``` jsl
/*Simple Linear Regression: y = intercept + beta * x + error*/
y = [3, 5, 7, 5];
X = [1, 2, 3, 4];
{Estimates, Std_Error, Diagnostics} = Linear Regression( y, X, <<printToLog ); 
/*
t_ratio = Diagnostics["t_ratio"]; 
p_value = Diagnostics["p_value"]; 
RSquare = Diagnostics["RSquare"]; 
RSquare Adj = Diagnostics["RSquare Adj"];
*/
```

**Example 2**

``` jsl
/*Model: y = beta_1*x + beta_2*x^2 + error*/
y = [3, 5, 7, 5];
X = [1 1, 2 4, 3 9, 4 16];
{Estimates, Std_Error, Diagnostics} = Linear Regression( y, X, <<noIntercept, <<printToLog );
```

**Example 3**

``` jsl
/*Categorical Variable Example*/
/*Model: y = beta_1*boy + beta_2*girl + beta_3*x + error*/
y = [3, 5, 7, 5];
x = [1, 2, 3, 4];
gender = {"boy", "girl", "girl", "boy"};
designMat = Design( gender ) || x;
{Estimates, Std_Error, Diagnostics} = Linear Regression(
    y,
    designMat,
    <<noIntercept,
    <<printToLog
);
```

### [Loc](#loc)[](#loc "Click to copy url")

**Syntax:** y = Loc( m ); y = Loc( v, x )

**Description:** Returns a matrix of the positions of the matrix m that are nonzero.If two arguments are specified, Loc(v, x) returns a matrix of the positions of the list or matrix v that are equal to the value x. Prefer Where instead where possible.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
/*more examples, above*/
Show( Loc( [1 0 1 0 1 0] ) );
Show( Loc( {"A", 2, 3, 2, 5, 2, 4, [1 5]}, 2 ) );
Show( Loc( {"A", 2, 3, 2, 5, 2, 4, [1 5]}, [1 5] ) );
```

**Example 2**

``` jsl
Loc( [0, -2, 3, 0, 5, ., -7, ., 9] ) /*missing is not zero or non-zero*/;
```

**Example 3**

``` jsl
Loc( [5, 7, 5, ., 5], 5 );
```

**Example 4**

``` jsl
Loc( [5, 7, 5, ., 5] == 5 ) /*[5,7,5, . ,5]==5   ==>   [1, 0, 1, ., 1]*/;
```

**Example 5**

``` jsl
Loc( {"a", "fred", "b", "fred"}, "fred" );
```

### [Loc Max](#loc-max)[](#loc-max "Click to copy url")

**Syntax:** y = Loc Max( x )

**Description:** Returns the first position in x of the maximum value.

**JMP Version Added:** Before version 14

``` jsl
Loc Max( [11 22 33 22 33 11] );
```

### [Loc Min](#loc-min)[](#loc-min "Click to copy url")

**Syntax:** y = Loc Min( x )

**Description:** Returns the first position in x of the minimum value.

**JMP Version Added:** Before version 14

``` jsl
Loc Min( [11 22 33 22 33 11] );
```

### [Loc Nonmissing](#loc-nonmissing)[](#loc-nonmissing "Click to copy url")

**Syntax:** y = Loc Nonmissing( matrixArg,...,{listArg},... )

**Description:** Returns a vector of row numbers in argument matrix rows that have no missing values, or for lists, those that are nonmissing numbers or nonempty character.

**JMP Version Added:** Before version 14

``` jsl
Loc Nonmissing( [1 2 3, 4 . 6, 7 8 ., 8 7 6] );
```

### [Loc Sorted](#loc-sorted)[](#loc-sorted "Click to copy url")

**Syntax:** idx = Loc Sorted( x, y )

**Description:** Creates a column vector of subscript positions where the values of x have values less than or equal to the values in y based on a binary search. x must be a matrix sorted in ascending order without missing values.

**JMP Version Added:** Before version 14

``` jsl
Show(
    Loc Sorted( [11 22 33 44 55], [11 33 55] ),
    Loc Sorted( [11 22 33 44 55], [1] ),
    Loc Sorted( [11 22 33 44 55], [500] )
);
```

### [Low Rank Symmetric Update BLAS](#low-rank-symmetric-update-blas)[](#low-rank-symmetric-update-blas "Click to copy url")

**Syntax:** y = Low Rank Symmetric Update BLAS( A, U, s )

**JMP Version Added:** 17

``` jsl
A = [2 0, 0 2];
U = [2 4, 3 5];
s = 2.5;
AUpdate = Low Rank Symmetric Update BLAS( A, U, s );
```

### [Matrix](#matrix_1)[](#matrix_1 "Click to copy url")

**Syntax:** y = Matrix( {{x11, ..., x1m}, {...}, {xn1, ..., xnm}} ) y = Matrix( {x1, ..., xn} ) y = Matrix( n, m )

**Description:** Constructs an n-by-m matrix. If you specify a list of n lists that each contain m row values, the matrix is formed by vertically concatenating the evaluated lists. If you specify a single list of n items, the return value is an n-by-1 column vector. If you specify two integer arguments, the return value is a matrix of zeros that contains n rows and m columns.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
Matrix( {{11, 22, 33}, {44, 55, 66}} );
```

**Example 2**

``` jsl
Matrix( {{[1 2 3], 4, 5, 6, 7, 8, 9}} );
```

**Example 3**

``` jsl
Matrix( {2, 3 + 7} );
```

**Example 4**

``` jsl
Matrix( 2, 3 );
```

### [Matrix Mult](#matrix-mult)[](#matrix-mult "Click to copy url")

**Syntax:** y = Matrix Mult( A, B, ... ); y = A \* B

**Description:** Performs matrix multiplication. The matrix arguments must be conformable: NCol(a)==NRow(b). Note that A \* B also works.

**JMP Version Added:** Before version 14

``` jsl
exMatA = [1 2 3, -2 0 -1, 0 1 1];
exMatB = [1 2, 1 2, 1 2];
exMatM1 = exMatA * exMatB;
exMatM2 = Matrix Mult( exMatA, exMatB );
exMatC = [1 2, 1 2];
exMatM3 = Matrix Mult( exMatA, exMatB, exMatC );
Show( exMatM1 );
Show( exMatM2 );
Show( exMatM3 );
```

### [Matrix Mult BLAS](#matrix-mult-blas)[](#matrix-mult-blas "Click to copy url")

**Syntax:** y = Matrix Mult BLAS( A, B, ... )

**Description:** Performs matrix multiplication. The matrix arguments must be conformable: NCol(A)==NRow(B).

**JMP Version Added:** 17

``` jsl
exMatA = [1 2 3, -2 0 -1, 0 1 1];
exMatB = [1 2, 1 2, 1 2];
exMatM2 = Matrix Mult BLAS( exMatA, exMatB );
```

### [Matrix Rank](#matrix-rank)[](#matrix-rank "Click to copy url")

**Syntax:** r = Matrix Rank( X )

**Description:** Returns the rank of the matrix X.

**JMP Version Added:** 14

``` jsl
Matrix Rank( [1 0 0, 0 1 0, 0 1 0] );
```

### [Mode](#mode)[](#mode "Click to copy url")

**Syntax:** y = Mode( list or matrix )

**Description:** Picks the 'most frequent' item from a matrix or list, the lower value for ties

**JMP Version Added:** Before version 14

``` jsl
Show( Mode( [1, 2, 3, 2, 1] ), Mode( {"a", "b", "c", "b", "a", "b"} ) );
```

### [Multivariate Normal Impute](#multivariate-normal-impute)[](#multivariate-normal-impute "Click to copy url")

**Syntax:** y = Multivariate Normal Impute( yVec, meanYvec, symCovMat, colMin, colMax )

**Description:** Returns a response vector with imputed values for the missing values in the yVec vector of responses. Imputations are based on a multivariate normal distribution with mean vector meanYvec and symmetric covariance matrix symCovMat. Optional arguments colMin and colMax are the respective vectors of column minimums and maximums. These arguments provide bounds for the imputations.

**JMP Version Added:** Before version 14

``` jsl
mat = [0.430735257211985 -0.935632420013493 . 0.424649913158299,
. -0.687720061441453 0.29665732536624 -1.94898001941576,
-0.0425472526673373 0.463229145080277 0.635619352779951 .];
cov = Covariance( mat, <<"Pairwise"/*, <<"shrink"*/ );
colMean = V Mean( mat );
colMin = V Min( mat );
colMax = V Max( mat );
For( it = 1, it <= N Row( mat ), it++,
    mat[it, 0] = Multivariate Normal Impute( mat[it, 0], colMean, cov, colMin, colMax )`
);
Print( mat );
```

### [N Col](#n-col)[](#n-col "Click to copy url")

**Syntax:** y = N Col(); y = N Col( dataTable ); y = N Col( matrix )

**Description:** Returns the number of columns in the current data table, a specified data table, or a matrix.

**JMP Version Added:** Before version 14

``` jsl
N Col( [11 22, 33 44] );
```

### [N Cols](#n-cols)[](#n-cols "Click to copy url")

**Syntax:** y = N Cols(); y = N Cols( dataTable ); y = N Col( matrix )

**Description:** Returns the number of columns in the current data table, a specified data table, or a matrix.

**JMP Version Added:** Before version 14

``` jsl
N Col( [11 22, 33 44] );
```

### [NChooseK Matrix](#nchoosek-matrix)[](#nchoosek-matrix "Click to copy url")

**Syntax:** m = NChooseK Matrix( n, k )

**Description:** Creates a matrix of nChooseK(n,k) rows and k columns forming all the combinations of k integers from 1 to n.

**JMP Version Added:** Before version 14

``` jsl
Print( NChooseK Matrix( 5, 3 ) );
```

### [Ortho](#ortho)[](#ortho "Click to copy url")

**Syntax:** L = Ortho( A, \<Centered( 1 )\>, \<Scaled( 1 )\> )

**Description:** Orthogonalizes the columns of a matrix. Center option makes them sum to zero. Scale option makes them unit length.

**JMP Version Added:** Before version 14

``` jsl
Ortho( [1 1, 1 -1] );
```

### [Ortho Poly](#ortho-poly)[](#ortho-poly "Click to copy url")

**Syntax:** L = Ortho Poly( V, order )

**Description:** Returns orthogonal polynomials of vector V up to order specified by the order argument. The V argument can be a row or column vector. Scale option makes them unit length.

**JMP Version Added:** Before version 14

``` jsl
Ortho Poly( 1 :: 10, 2 );
```

### [P Spline Coef](#p-spline-coef)[](#p-spline-coef "Click to copy url")

**Syntax:** coef = P Spline Coef( x, Internal Knot Grid, \<degree = 3\>, \<KnotEndPoints = min(x) \|\| max(x)\> )

**Description:** Returns the matrix of P-Spline coefficients. Internal Knot Grid is either the number of desired knot points based on percentiles of x or a vector specifying the internal knot points. Optional parameter degree specifies the degree of the P-splines with a default of 3.

**JMP Version Added:** 14

``` jsl
P Spline Coef( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2 );
P Spline Coef( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 7] );
```

### [Parallel Assign](#parallel-assign)[](#parallel-assign "Click to copy url")

**Syntax:** tf = ParallelAssign( { thread_local_var = global_var, ... }, m\[ a, b \] = expression using a and b )

**Description:** Use multiple threads to assign values to the matrix. If any thread throws an exception, a message will be printed to the log and the return value will be 0. If all threads complete without error, the return value will be 1. Functions that launch platforms, create or use data tables, or access the graphics subsystem are only supported on the main thread, and will throw an exception if called from a worker thread.

**JMP Version Added:** Before version 14

``` jsl
m = J( 3, 2, -1 );
If( Parallel Assign( {/*no locals */ }, m[a/* 1,2,3 */, b/* 1,2 */ ] = a * a + b ) == 0,
    Throw( "thread failed" )
);
m;/* 1*1+1  1*1+2, 2*2+1  2*2+2, 3*3+1  3*3+2 */
```

### [Print Matrix](#print-matrix)[](#print-matrix "Click to copy url")

**Syntax:** s = Print Matrix( M, \<\<ignore locale( 0 ), \<\<style( "parseable" ), \<\<separate( ", " ), \<\<line begin( "\[ " ), \<\<line end( " \]" ) )

**Description:** Prints the matrix M. The optional argument ignore locale determines whether the printing of decimal separators should respect Locale information, where zero means to respect Locale. The optional argument style determines whether to use a style and which style to use. The available styles are parseable, which is a reformatted JSL matrix expression, latex, and other. When the style argument is other, the last three optional arguments define the beginning and ending characters of printed rows and separating characters of concatenated entries.

**JMP Version Added:** Before version 14

``` jsl
A = [3.509 0.003, 874.4 0.00384, 0.03 0.093];
Print Matrix( A );
Print Matrix( A, <<ignore locale( 1 ) );
Print Matrix( A, <<style( "latex" ) );
Print Matrix(
    A,
    <<style( "other" ),
    <<line begin( "| " ),
    <<line end( " |" ),
    <<separate( " | " )
);
```

### [QR](#qr)[](#qr "Click to copy url")

**Syntax:** {Q, R} = QR( X )

**Description:** Creates an m by m orthogonal matrix Q and an m by n upper triangular matrix R, such that X = Q \* R. The argument X is an m by n matrix.

**JMP Version Added:** Before version 14

``` jsl
QR( [11 22, 33 44] );
```

### [QR LAPACK](#qr-lapack)[](#qr-lapack "Click to copy url")

**Syntax:** {Q, R} = QR LAPACK( X )

**Description:** Creates an m by k orthogonal matrix Q and a k by n upper triangular matrix R, such that X = Q \* R. The argument X is an m by n matrix, where k is min(m, n).

**JMP Version Added:** 17

``` jsl
QR LAPACK( [11 22, 33 44] );
```

### [Quadratic Form BLAS](#quadratic-form-blas)[](#quadratic-form-blas "Click to copy url")

**Syntax:** y = Quadratic Form BLAS( A, x )

**JMP Version Added:** 17

``` jsl
A = [2 0, 0 2];
x = [2, 3];
y = Quadratic Form BLAS( A, x );
```

### [Random SVD](#random-svd)[](#random-svd "Click to copy url")

**Syntax:** {U, M, V} = Random SVD( X , \<nSingularValues=min(nRow,nCol)\>, \<nOver=10\>, \<nIter=2\>)

**Description:** Computes the singular value decomposition of matrix X using the randomized singular value decomposition by returning a list {U, M, V} such that U\*diag(M)\*V\` is equal to X.

**JMP Version Added:** 17

``` jsl
Random SVD( [11 22, 33 44], 1 );
```

### [Rank](#rank)[](#rank "Click to copy url")

**Syntax:** y = Rank Index( x )

**Description:** Returns a vector of indices that, used as a subscript to the original vector v, sorts the vector by rank. Excludes missing values.

**JMP Version Added:** Before version 14

``` jsl
Rank( [33, 22, 44, 11, ., 33] );
```

### [Rank Index](#rank-index)[](#rank-index "Click to copy url")

**Syntax:** y = Rank Index( x )

**Description:** Returns a vector of indices that, used as a subscript to the original vector v, sorts the vector by rank. Excludes missing values.

**JMP Version Added:** Before version 14

``` jsl
Rank Index( [33, 22, 44, 11, ., 33] );
```

### [Ranking](#ranking)[](#ranking "Click to copy url")

**Syntax:** y = Ranking( x, \< \<\<tie("average"\|"row"\|"minimum"\|"maximum"\|"arbitrary")\> )

**Description:** Returns a vector of ranks of the values of x, low to high as 1 to n, ties arbitrary.

**JMP Version Added:** Before version 14

``` jsl
Ranking( [33, 22, 44, 11, 33] );
Ranking( [22, 11, 33, 11, 44, 55, 44, 44, 44], <<Tie( "minimum" ) );
```

### [Ranking Tie](#ranking-tie)[](#ranking-tie "Click to copy url")

**Syntax:** y = Ranking Tie( x, \< \<\<tie("average"\|"row"\|"minimum"\|"maximum"\|"arbitrary")\> )

**Description:** Returns a vector of ranks of the values of x, but ranks for ties averaged.

**JMP Version Added:** Before version 14

``` jsl
Ranking Tie( [33, 22, 44, 11, 33] );
```

### [Robust PCA](#robust-pca)[](#robust-pca "Click to copy url")

**Syntax:** {A,E} = Robust PCA( X , \<Lambda(2/sqrt(max(nrow,ncol)))\>, \<tolerance=1e-10\>,\<maxit(75)\>,\<Center(1)\>,\<Scale(1)\>

**Description:** Robustly decomposes data into a low-rank matrix and a sparse matrix of residuals. Outliers are detected in the residuals. It can also impute missing values.

**JMP Version Added:** 16

``` jsl
X = [1 -3, -1 -2, -3 -4, -4 -3, -3 1, 3 3] * [-2 5 -1 -2 1, 4 5 -4 -3 1];
X[2, 3] += 15;
Result = Robust PCA( X, Center( 0 ), Scale( 0 ), Lambda( .80 ) );
```

### [SVD](#svd)[](#svd "Click to copy url")

**Syntax:** {U, M, V} = SVD( X )

**Description:** Computes the singular value decomposition of matrix X by returning a list {U, M, V} such that U\*diag(M)\*V\` is equal to X.

**JMP Version Added:** Before version 14

``` jsl
SVD( [11 22, 33 44] );
```

### [SVD LAPACK](#svd-lapack)[](#svd-lapack "Click to copy url")

**Syntax:** {U, M, V} = SVD LAPACK( X )

**Description:** Computes the singular value decomposition of matrix X by returning a list {U, M, V} such that U\*diag(M)\*V\` is equal to X.

**JMP Version Added:** 17

``` jsl
SVD LAPACK( [11 22, 33 44] );
```

### [Scoring Impute](#scoring-impute)[](#scoring-impute "Click to copy url")

**Syntax:** {imputedRow} = Scoring Impute ( rowWithMissing , VMat, colMeanVec, colStdDevVec)

**Description:** Provides streaming functionality for the Automated Data Imputation (ADI) algorithm. The input arguments are a row vector that contains missing values, a loading matrix (also called the V matrix) that is produced by the ADI algorithm, a vector of the column means ignoring missing cells, and a vector of the column standard deviations ignoring missing cells. It returns the row vector with the missing values imputed using least squares estimation.

**JMP Version Added:** 14

``` jsl
Scoring Impute(
    [1 2 3 . 4 .],
    [.5 .6, .3 .4, .1 .2, .6 .7, .3 .3, .5 .4],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1]
);
```

### [Shape](#shape)[](#shape "Click to copy url")

**Syntax:** r = Shape( M, nr, \<nc\>, \<\<bycol)

**Description:** Reshapes the M matrix or scalar across rows to be nr rows by nc columns. A missing value is permitted for nr. Data from M is replicated as needed to fill the nr by nc matrix. The optional argument \<\<bycol fills the data by column. By default, the data is filled by row. Common uses are to reshape a vector into a matrix or to vectorize a matrix.

**JMP Version Added:** Before version 14

``` jsl
Eval List(
    {Shape( [11 22, 33 44], 1, 4 ), Shape( [11 22, 33 44], 1 ), Shape( [11 22, 33 44], ., 4 )
    }
);
```

### [Solve](#solve)[](#solve "Click to copy url")

**Syntax:** y = Solve( A, B )

**Description:** Solves the linear system A\*x=B for x. The Solve() function is equivalent to Inverse(A)\*B if A is non-singular. Note that the A argument must be a square matrix.

**JMP Version Added:** Before version 14

``` jsl
Solve( [1 1, -1 4], [11, 14] );
```

### [Sort Ascending](#sort-ascending)[](#sort-ascending "Click to copy url")

**Syntax:** y = Sort Ascending( x )

**Description:** Returns a copy of list or matrix x with the items in ascending order.

**JMP Version Added:** Before version 14

``` jsl
Sort Ascending( {111, 212, 133, 114, 55} );
```

### [Sort Descending](#sort-descending)[](#sort-descending "Click to copy url")

**Syntax:** y = Sort Descending( x )

**Description:** Returns a copy of list or matrix x with the items in descending order.

**JMP Version Added:** Before version 14

``` jsl
Sort Descending( {111, 212, 133, 114, 55} );
```

### [Sparse SVD](#sparse-svd)[](#sparse-svd "Click to copy url")

**Syntax:** {U, M, V} = Sparse SVD( X , \<nSingularValues=min(nRow,nCol)\>, \<tolerance=1e-10\>)

**Description:** Computes the singular value decomposition of matrix X using the implicitly restarted, partially reorthogonalized Lanczos method for sparse matrices by returning a list {U, M, V} such that U\*diag(M)\*V\` is equal to X.

**JMP Version Added:** Before version 14

``` jsl
Sparse SVD( [11 22, 33 44], 1, 1e-8 );
```

### [Spline Coef](#spline-coef)[](#spline-coef "Click to copy url")

**Syntax:** coef = Spline Coef( x, y, lambda, \<weights\> )

**Description:** Returns a five-column matrix of coefficients in the following order: knots\|\|a\|\|b\|\|c\|\|d for each of the unique values in x. The smoothing parameter lambda must be a positive value, where larger values of lambda result in greater stiffness of the spline. The optional weights vector specifies a weight for each value in x. A weight of zero removes the corresponding point from the spline fit.

**JMP Version Added:** Before version 14

``` jsl
Spline Eval( 0 :: 10, Spline Coef( 0 :: 10, Sqrt( 0 :: 10 ), 100 ) );
```

### [Spline Eval](#spline-eval)[](#spline-eval "Click to copy url")

**Syntax:** yhat = Spline Eval( x, coef, \<extrapolation=-1\> )

**Description:** Evaluates the spline predictions using the coef matrix in the same form as returned by the Spline Coef() function. extrapolation indicates how far beyond the spline range, as a fraction of the range, to extend evaluation before returning missing values.

**JMP Version Added:** Before version 14

``` jsl

New Window( "Spline Fit",
    window:x = 20 :: 80;
    window:y = 50 + Sin( (20 :: 80) / 10 ) * 40 + J(
        1,
        N Col( window:x ),
        Random Normal( 0, 10 )
    );
    window:loglambda = 2;
    window:g = Graph Box(
        Pen Color( "blue" );
        window:m = Spline Coef( window:x, window:y, Power( 10, window:loglambda ) );
        Marker( window:x, window:y );
        Y Function( Spline Eval( a, window:m, 0.05 ), a );
    );,
    H List Box(
        Text Box( "Lambda: " ),
        Slider Box( -2, 5, window:loglambda, window:g << reshow )
    )
)
;
```

### [Spline Smooth](#spline-smooth)[](#spline-smooth "Click to copy url")

**Syntax:** yhat = Spline Smooth( x, y, lambda, \<weights\> )

**Description:** Returns the smoothed predicted values from a spline fit. The smoothing parameter lambda must be a positive value, where larger values of lambda result in greater stiffness of the spline. The optional weights vector specifies a weight for each value in x. A weight of zero removes the corresponding point from the spline fit.

**JMP Version Added:** Before version 14

``` jsl
Spline Smooth( 0 :: 10, Sqrt( 0 :: 10 ), 100 );
```

### [Sweep](#sweep)[](#sweep "Click to copy url")

**Syntax:** y = Sweep( A, \<indices\> )

**Description:** Returns the sweep of the matrix A on diagonal pivots indicated by indices. This is a way of inverting a matrix one pivot at a time.

**JMP Version Added:** Before version 14

``` jsl
exMat = [5 4 1 1, 4 5 1 1, 1 1 4 2, 1 1 2 4];
exMatswp = Sweep( exMat, [1, 2, 3, 4] );
exMatinv = Inverse( exMat );
Show( exMatswp );
Show( exMatinv );
```

### [Sym Matrix Mult BLAS](#sym-matrix-mult-blas)[](#sym-matrix-mult-blas "Click to copy url")

**Syntax:** y = Sym Matrix Mult BLAS( A, B, ... )

**Description:** Performs matrix multiplication, where A is a symmetric matrix. The matrix arguments must be conformable: NCol(A)==NRow(B).

**JMP Version Added:** 17

``` jsl
exMatA = [1 2 3, -2 0 -1, 0 1 1];
exMatA = exMatA` * exMatA;
exMatB = [1 2, 1 2, 1 2];
exMatM2 = Sym Matrix Mult BLAS( exMatA, exMatB );
```

### [Trace](#trace)[](#trace "Click to copy url")

**Syntax:** y = Trace( x )

**Description:** Returns the sum of the diagonal elements of a square matrix.

**JMP Version Added:** Before version 14

``` jsl
Trace( [11 22, 33 44] );
```

### [Transpose](#transpose)[](#transpose "Click to copy url")

**Syntax:** y = Transpose( matrix ); y = matrix\`

**Description:** Transposes the matrix argument by interchanging the rows and columns.

**JMP Version Added:** Before version 14

``` jsl
Show( Transpose( [11 22, 33 44] ), [11 22, 33 44]` );
```

### [V Concat](#v-concat)[](#v-concat "Click to copy url")

**Syntax:** y = a \|/ b; y = V Concat( a, b, ... )

**Description:** Concatenates matrices vertically. Arguments must have same number of columns.

**JMP Version Added:** Before version 14

``` jsl
[11 22] |/ [33 44];
```

### [V Concat To](#v-concat-to)[](#v-concat-to "Click to copy url")

**Syntax:** matrix1 \|/= matrix2; V Concat To( matrix1, matrix2 )

**Description:** Concatenates in place, vertically. a \|/= b is equivalent to a = a \|/ b. This is an assignment operator.

**JMP Version Added:** Before version 14

``` jsl
exA = [1 2, 3 4];
exB = [5 6, 7 8, 9 10];
exC = [1, 1, 1, 1, 1];
exD = V Concat To( exA, exB );
exE = Concat( exD, exC );
/* exA is changed and exD is not. */
Show( exA, exB, exC, exD, exE );
/* Also see ConcatTo(), VConcat() */
```

### [V Max](#v-max)[](#v-max "Click to copy url")

**Syntax:** b = V Max( matrix )

**Description:** Returns a row vector containing the maximum of each column in the argument.

**JMP Version Added:** Before version 14

``` jsl
V Max( [11 22, 33 44, 55 66] );
```

### [V Mean](#v-mean)[](#v-mean "Click to copy url")

**Syntax:** m = V Mean( matrix )

**Description:** Returns a row vector containing the mean of each column in the argument.

**JMP Version Added:** Before version 14

``` jsl
V Mean( [11 22, 33 44, 55 66] );
```

### [V Median](#v-median)[](#v-median "Click to copy url")

**Syntax:** m = V Median( matrix )

**Description:** Returns a row vector containing the median of each column in the argument.

**JMP Version Added:** 15

``` jsl
V Median( [11 22, 33 44, 35 46, 55 66] );
```

### [V Min](#v-min)[](#v-min "Click to copy url")

**Syntax:** a = V Min( matrix )

**Description:** Returns a row vector containing the minimum of each column in the argument.

**JMP Version Added:** Before version 14

``` jsl
V Min( [11 22, 33 44, 55 66] );
```

### [V Quantile](#v-quantile)[](#v-quantile "Click to copy url")

**Syntax:** m = V Quantile( matrix, p )

**Description:** Returns a row vector containing the specified quantile p of each column in the argument.

**JMP Version Added:** 15

``` jsl
V Quantile( [11 22, 33 44, 35 46, 55 66], .25 );
```

### [V Robust Standardize](#v-robust-standardize)[](#v-robust-standardize "Click to copy url")

**Syntax:** b = V Robust Standardize( X, \<center=1\>, \<scale=1\> )

**Description:** Returns a matrix that is centered by the median and scaled by a robust estimate of the standard deviation of matrix X. The optional Boolean arguments specify if centering and scaling are performed.

**JMP Version Added:** 17

``` jsl
V Robust Standardize( J( 150, 4, Random Normal() ), 1, 1 );
```

### [V Standardize](#v-standardize)[](#v-standardize "Click to copy url")

**Syntax:** b = V Standardize( X )

**Description:** Returns a matrix that is the centered and scaled version of matrix X. Each column of b has mean 0 and standard deviation 1.

**JMP Version Added:** Before version 14

``` jsl
V Standardize( [11 22, 33 44, 55 66] );
```

### [V Std](#v-std)[](#v-std "Click to copy url")

**Syntax:** b = V Std( matrix )

**Description:** Returns a row vector containing the standard deviations of each column in the argument.

**JMP Version Added:** Before version 14

``` jsl
V Std( [11 22, 33 44, 55 66] );
```

### [V Sum](#v-sum)[](#v-sum "Click to copy url")

**Syntax:** s = V Sum( matrix )

**Description:** Returns a row vector containing the sum of each column in the argument.

**JMP Version Added:** Before version 14

``` jsl
V Sum( [11 22, 33 44, 55 66] );
```

### [VPTree](#vptree)[](#vptree "Click to copy url")

**Syntax:** tab = VPTree( \[ matrix \] )

**Description:** Returns a table for efficiently looking up near neighbors. The matrix arguments are k-dimensional points. There is no built in limit on the number of dimensions or points.

**JMP Version Added:** 16

``` jsl
tab = VPTree( [1 1 1, 1 2 1, 1 2 2, 2 2 2, 3 3 3, 4 5 6] );
{rows, dist} = tab << K nearest rows( 2, [1.1 .9 1] );
"2 nearest rows to [1.1 .9 1] are " || Char( rows );
```

### [Varimax](#varimax)[](#varimax "Click to copy url")

**Syntax:** {R,T} = Varimax( F, \<norm=1\> )

**Description:** Performs a varimax rotation of the specified matrix F. Returns a list that contains the rotated matrix and the orthogonal rotation matrix. By default, a normalized varimax rotation is performed. Specify norm = 0 to perform a non-normalized varimax rotation.

**JMP Version Added:** Before version 14

``` jsl
Varimax( [1.2 .4, .9 1.5] );
```

### [Vec Diag](#vec-diag)[](#vec-diag "Click to copy url")

**Syntax:** y = Vec Diag( x )

**Description:** Returns the diagonal elements of the square matrix as a vector.

**JMP Version Added:** Before version 14

``` jsl
Vec Diag( [11 22, 33 44] );
```

### [Vec Quadratic](#vec-quadratic)[](#vec-quadratic "Click to copy url")

**Syntax:** Vec Quadratic( S, X )

**Description:** Evaluates as Vec Diag( X \* S \* X\` ).

**JMP Version Added:** Before version 14

``` jsl
exS = [1 3 5, 3 2 6, 5 6 1];
exX = [1 3 5, 2 4 6];
Vec Quadratic( exS, exX );
```

### [Wavelet Basis Coef](#wavelet-basis-coef)[](#wavelet-basis-coef "Click to copy url")

**Syntax:** y = Wavelet Basis Coef( x, grid, coef, \<wavelet = "Haar" or "Biorthogonal" or "Coiflet" or "Daubechies" or "Symlet"\>, \<param = 0\> )

**Description:** Returns the prediction at the points x for the specified Wavelet model. The grid parameter is a vector specifying the grid of the data for the wavelet model. The coef parameter is a vector of wavelet coefficients. The wavelet parameter is the name of the wavelet model. The optional param parameter is the wavelet model parameter (if necessary, defaults to 0).

**JMP Version Added:** 17

``` jsl
Wavelet Basis Coef( 2.5, [1, 2, 3, 4], [0, 1, 2, 3], "Haar" );
```

[ Previous](MATLAB.html "MATLAB") [Next ](Numeric.html "Numeric")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
