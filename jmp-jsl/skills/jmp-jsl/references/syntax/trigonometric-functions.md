# Trigonometric Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 334-336).

## Index (line numbers in this file)

- `ATan()` — L108
- `ArCos()` — L75
- `ArSin()` — L86
- `ArcCosH()` — L59
- `ArcCosine()` — L74
- `ArcSinH()` — L96
- `ArcSine()` — L85
- `ArcTan()` — L107
- `ArcTanH()` — L122
- `ArcTangent()` — L106
- `Cos()` — L143
- `CosH()` — L132
- `Cosine()` — L142
- `Sin()` — L154
- `SinH()` — L158
- `Sine()` — L153
- `Squash()` — L32
- `Squish()` — L36
- `SuInv()` — L41
- `SuTrans()` — L46
- `Trigamma()` — L51
---

Trigonometric Functions

Squash(expr)
Description

An efficient computation of the function 1/ [1 + exp(expr)].
Squish(expr)
Description
–

Equivalent to Squash(-expr), or 1   1 + e expr  .
SuInv(z, gamma, delta, theta, sigma)
Description

Returns a transformation of a standard normal variable to an unbounded Johnson
variable.
SuTrans(x, gamma, delta, theta, sigma)
Description

Returns a transformation of an unbounded Johnson variable to a standard normal
variable.
Trigamma()
Description

Returns the trigamma function evaluated at n. The trigamma function is the derivative of
the digamma function.

Trigonometric Functions
JMP’s trigonometric functions expect all angle arguments in radians.
ArcCosH(x)
Description

Inverse hyperbolic cosine.
Returns

The inverse hyperbolic cosine of x.
Argument
x Any number, numeric variable, or numeric expression.

JSL Functions, Operators, and Messages
Trigonometric Functions

335

ArcCosine(x)
ArCos(x)
Description

Inverse cosine.
Returns

The inverse cosine of x, an angle in radians.
Argument
x Any number, numeric variable, or numeric expression.

ArcSine(x)
ArSin(x)
Description

Inverse sine.
Returns

The inverse sine of x, an angle in radians.
Argument
x Any number, numeric variable, or numeric expression.

ArcSinH(x)
Description

Inverse hyperbolic sine.
Returns

The inverse hyperbolic sine of x.
Argument
x Any number, numeric variable, or numeric expression.

ArcTangent(x1, <x2=1>)
ArcTan(x1 <x2=1>)
ATan(x1 <x2=1>)
Description

Inverse tangent.
Returns

The inverse trigonometric tangent of x1/x2, where the result is in the range -Pi()/2, Pi()/2.
Argument
x1 Any number, numeric variable, or numeric expression.

Trigonometric Functions

x2=1 Specifies atan2.

ArcTanH(x)
Description

Inverse hyperbolic tangent.
Returns

The inverse hyperbolic tangent of x.
Argument
x Any number, numeric variable, or numeric expression.

CosH(x)
Description

Hyperbolic cosine.
Returns

The hyperbolic cosine of x.
Argument
x Any number, numeric variable, or numeric expression.

Cosine(x)
Cos(x)
Description

Cosine.
Returns

The cosine of x.
Argument
x Any number, numeric variable, or numeric expression. The angle in radians.

Sine(expr)
Sin(expr)
Description

Returns the sine.
SinH(expr)
Description

Returns the hyperbolic sine.
