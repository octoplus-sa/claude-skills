# Expression Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 126-127).

## Index (line numbers in this file)

- `Arg Expr()` — L25
- `Arg()` — L24
- `Empty()` — L32
- `Eval Expr()` — L40
- `Expr()` — L50
- `Extract Expr()` — L66
- `Head Expr()` — L78
- `Head Name Expr()` — L86
- `Head Name()` — L85
- `Head()` — L77
- `N Arg Expr()` — L97
- `N Arg()` — L93
---

Expression Functions

Expression Functions
Arg(expr, i)
Arg Expr(expr, i)
Description

Finds the argument numbered by i within the given expression.
Returns

The ith argument within the expression expr.
Empty() if that argument does not exist or is not specified.
Arguments

expr An expression.
i An integer that indicates which argument to return.
Notes
Arg Expr() is deprecated. Use Arg() instead.

Eval Expr(expr)
Description

Evaluates any expressions within expr, but leaves the outer expression unevaluated.
Returns

An expression with all the expressions inside expr evaluated.
Argument

expr A valid expression.
Expr(expr, i)
Description

Returns the argument unevaluated (expression-quoting).
Returns

The argument, unevaluated.
Empty() if that argument does not exist or is not specified.
Argument

expr An expression.
i An integer that indicates which argument to return.

JSL Functions, Operators, and Messages
Expression Functions

Extract Expr(expr, pattern)
Description

Find expr matching pattern.
Returns

A pattern that matches the specified pattern.
Arguments

expr An expression.
pattern Any pattern.
Head(exprArg)
Head Expr(exprArg)
Description

Returns the head of the evaluated expression, without its arguments.
Notes
Head Expr() is deprecated. Use Head() instead.

Head Name(expr)
Head Name Expr(expr)
Description

Returns the head of the evaluated expression as a quoted string.
Notes
Head Name Expr() is deprecated. Use Head Name() instead.

N Arg(exprArg)
Description

Returns the number of arguments of the evaluated expression head.
N Arg Expr(exprArg)
Description

Returns the number of arguments of the expression head.
Notes
N Arg Expr() is deprecated. Use N Arg() instead.

127
