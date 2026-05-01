# Optimization Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 219-222).

## Index (line numbers in this file)

- `Constrained Maximize()` — L58
- `Constrained Minimize()` — L88
- `Desirability()` — L121
- `LPSolve()` — L137
- `Maximize()` — L159
- `Minimize()` — L190
- `Num Deriv2()` — L41
- `Round()` — L47
- `Simplify Expr()` — L51
- `The Num Deriv()` — L28
---

JSL Functions, Operators, and Messages
Optimization Functions

219

functionʹs first argument. The derivative is evaluated using numeric values specified in
the f( x,... ) function expression.
Notes

The Num Deriv() function might appear not to produce the correct results as seen here:
x = 3;
n = Num Deriv( 3 * x ^ 2 );
// 9.00000000001455

The preceding usage is not correct. The function was designed to be used in the Nonlinear
platform to differentiate functions for which it does not know the analytic derivatives. The
proper usage takes the following form:
x = 3;
f = Function( {x}, 3 * x ^ 2 );
n = Num Deriv( f( x ), 1 );
// 18.000029999854

Num Deriv2(f(x,...))
Description

Returns the numerical second derivative of the f( x,... ) function with respect to x.
The derivative is evaluated using numeric values specified in the f( x,... ) function
expression.
Round(n, places)
Description

Rounds n to number of decimal places given.
Simplify Expr(expr(expression))
Simplify Expr(nameExpr(global))
Description

Algebraically simplifies an expression

Optimization Functions
Constrained Maximize(expr, {x1(low1, up1), x2(low2, up2), ...}, messages)
Description

Finds the values for the x arguments, specified as a list, that maximize the expr expression
with optional linear constraints. You must either specify lower and upper bounds in

Optimization Functions

parentheses for each argument or with the optional Set Variable Limit() message. The
x arguments can be scalar values or vectors.
In the following messages, A is a matrix of coefficients. x = [x1, x2, ...] is the vector of
arguments. b is a vector that forms the right side of the expression.
Messages
<<Less than EQ({A, b}) Sets the constraint to less than or equal to the specified values
(A*x <= b).
<<Greater Than EQ({A, b}) Sets the constraint to greater than or equal to the specified
values (A*x >= b).
<<Equal To({A, b}) Sets the constraint as equal to the specified values (A*x = b).
<<Starting Values([x1Start, x2Start, ...]) Specifies a starting point.
<<Max Iter(int) An integer that specifies the maximum number of iterations to be

performed.
<<Tolerance(p) p sets the tolerance for the convergence criterion. The default tolerance

is 10-5.
<<Show Details("true") Returns a list with the final values for (objective value,
number of iterations, gradient, and Hessian). Shows the step-by-step results of the
optimizer in the log.
<<SetVariableLimit({low,high}) Specifies vectors for the lower and upper limits for
the optimization variables.
Constrained Minimize(expr, {x1(low1, up1), x2(low2, up2), ...}, messages)
Description

Finds the values for the x arguments, specified as a list, that minimize the expr expression
with optional linear constraints. You must either specify lower and upper bounds in
parentheses for each argument or with the optional Set Variable Limit() message. The
x arguments can be scalar values or vectors.
In the following messages, A is a matrix of coefficients. x = [x1, x2, ...] is the vector of
arguments. b is a vector that forms the right side of the expression.
Messages
<<Less than EQ({A, b}) Sets the constraint to less than or equal to the specified values
(A*x <= b).
<<Greater Than EQ({A, b}) Sets the constraint to greater than or equal to the specified
values (A*x >= b).
<<Equal To({A, b}) Sets the constraint as equal to the specified values (A*x = b).
<<Starting Values([x1Start, x2Start, ...]) Specifies a starting point.
<<Max Iter(int) An integer that specifies the maximum number of iterations to be

performed.

JSL Functions, Operators, and Messages
Optimization Functions

221

<<Tolerance(p) p sets the tolerance for the convergence criterion. The default tolerance

is 10-5.
<<Show Details("true") Returns a list with the final values for (objective value,
number of iterations, gradient, and Hessian). Shows the step-by-step results of the
optimizer in the log.
<<SetVariableLimit({low,high}) Specifies vectors for the lower and upper limits for
the optimization variables.
Desirability(yVector, desireVector, y)
Description

Fits a function to go through the three points, suitable for defining the desirability of a set
of response variables (y’s). yVector and desireVector are matrices with three values,
corresponding to the three points defining the desirability function. The actual function
depends on whether the desire values are in the shape of a larger-is-better,
smaller-is-better, target, or antitarget.
Returns

The desirability function.
Arguments
yVector Three input values.
desireVector the corresponding three desirability values.
y the value of which to calculate the desirability.

LPSolve(A, b, c, L, U, neq, nle, nge, <slackVars(Boolean)>)
Description

Returns a list containing the decision variables (and slack variables if applicable) in the
first list item and the optimal objective function value (if one exists) in the second list item.
Arguments
A A matrix of constraint coefficients.
b A matrix that is a column of right hand side values of the constraints.
c A vector of cost coefficients of the objective function.
L, U Matrices of lower and upper bounds for the variables.
neq The number of equality constraints.
nle The number of less than or equal inequalities.
nge The number of greater than or equal inequalities.
slackVars(Boolean) (Optional) Determines whether the slack variables are returned in
addition to the decision variables. The default value is 0.

Optimization Functions

Notes

The constraints must be listed as equalities first, less than or equal inequalities next, and
greater than or equal inequalities last.
Maximize(expr, {x1(low1, up1), x2(low2, up2), ...}, messages)
Description

Finds the values for the x arguments, specified as a list, that maximize the expression
expr. You can specify lower and upper bounds in parentheses for each argument.
Additional arguments for the function enable you to set the maximum number of
iterations, tolerance for convergence, and view more details about the optimization. The
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
Minimize(expr, {x1(low1, up1), x2(low2, up2), ...}, messages)
Description

Finds the values for the x arguments, specified as a list, that minimize the expression
expr. You can specify lower and upper bounds in parentheses for each argument.
Additional arguments for the function enable you to set the maximum number of
iterations, tolerance for convergence, and view more details about the optimization. The
