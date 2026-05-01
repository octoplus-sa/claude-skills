# Numeric Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 216-218).

## Index (line numbers in this file)

- `Abs()` — L38
- `Ceiling()` — L48
- `Derivative()` — L58
- `Floor()` — L80
- `Integrate()` — L95
- `Invert Expr()` — L119
- `Mod()` — L123
- `Modulo()` — L125
- `Names Default To Here()` — L30
- `Normal Integrate()` — L134
- `Num Deriv()` — L147
- `StoreInfo()` — L115
---

Numeric Functions

The indices returned by Where() are optimized for high performance on large lists,
matrices, and columns.
Required Arguments
clause A comparison function or conditional statement.
Optional Arguments
<dt> Changes the current Data Table during the evaluation.
Examples
Names Default To Here( 1 );
xs = [10 20 30 . 50];
xs[Where( xs >= 20 )];
xs[Where( !Is Missing( xs ) )];
ys = {10, 20, "30", ., 50};
ys[Where( ys >= 20 )];

Numeric Functions
Abs(n)
Description

Calculates the absolute value of n.
Returns

Returns a positive number of the same magnitude as the value of n.
Argument
n Any number.

Ceiling(n)
Description

If n is not an integer, rounds n to the next highest integer.
Returns

Returns the smallest integer greater than or equal to n.
Argument
n Any number.

Derivative(expr, {name, ...}, ...)
Description

Calculates the derivative of the expr expression with respect to name.

JSL Functions, Operators, and Messages
Numeric Functions

217

Returns

Returns the derivative.
Arguments
expr Any expression. Indirect arguments (for example, Name Expr, Expr, Eval) are

supported.
name Can be a single variable or a list of variables.
Notes

Adding an additional variable (Derivative(expr, name, name2)) takes the second
derivative.
Floor(n)
Description

If n is not an integer, rounds n to the next lowest integer.
Returns

Returns the largest integer less than or equal to n.
Argument
n Any number.
Examples
Floor( 2.7 );
2
Floor( –.5 );
–1

Integrate(expr, varname, lowLimit, upLimit, <<Tolerance(1e-10),
<<StoreInfo({list}), <<StartingValue(val))
Description

Integrates an expression with respect to a scalar value, using the adaptive quadrature
method from Gander and Gautschi (2000).
Arguments
expr an expression that defines the integrand.
varname the name of the variable of integration. If this variable contains a value, that value

specifies a starting value that is used as a typical value to improve the accuracy of the
integral.
lowLimit specifies the lower limit of integration. To specify negative infinity as the lower
limit of integration, set this to missing.
upLimit specifies the upper limit of integration. To specify positive infinity as the upper
limit of integration, set this to missing.

Numeric Functions

StoreInfo saves diagnostics of the numerical integration routine to the argument of
StoreInfo().
StartingValue specifies a starting value that is used as a typical value to improve the
accuracy of the integral.

Invert Expr(expr, name)
Description

Attempts to unfold expr around name.
Mod()
See “Modulo(number, divisor)”
Modulo(number, divisor)
Mod(number, divisor)
Description

Returns the remainder when number is divided by divisor.
Examples
Modulo( 6, 5 );
1

Normal Integrate(muVector, sigmaMatrix, expr, x, nStrata, nSim)
Description

Returns the result of radial-spherical integration for smooth functions of multivariate,
normally distributed variables.
Arguments
muVector A vector.
sigmaMatrix A matrix.
expr An expression in terms of the variable x.
x The variable used in the expression expr.
nStrata Number of strata.
nSim Number of simulations.

Num Deriv(f(x,...), <parnum=1>)
Description

Returns the numerical derivative of the f( x,... ) function with respect to one of its
arguments. You can specify that argument as the second argument in the Num Deriv
function. If no second argument is specified, the derivative is taken with respect to the
