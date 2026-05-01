# Constant Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 75-75).

## Index (line numbers in this file)

- `Pi()` — L48
- `Show()` — L28
- `While()` — L31
- `Zero Or Missing()` — L36
---

JSL Functions, Operators, and Messages
Constant Functions

75

first loop control variables have been set, but the local variables do not get initialized
again after that.
body Any number of valid JSL expressions, glued together if there are more than one. The
result of the JSL expressions at each iteration is used in the output container. You can
use the Continue() function to return no value for an iteration and skip to the next
iteration. You can also use Break() function to stop iteration through the loop and
proceed to the next expression that follows the loop. See “Break and Continue
Functions”.
Example
values = Transform Each( {x}, {10, 20}, x + 10 );
Show( values );
values = {20, 30};

While(expr, body)
Description

Repeatedly tests the expr condition and executes the body until the expr condition is no
longer true.
Zero Or Missing(expr)
Description

Returns 1 if expr yields a missing value or zero, 0 otherwise.

Constant Functions
JMP provides functions for two useful constant functions.
Note: These functions do not take an argument, but the parentheses are required.
e()
Description

Returns the constant e, which is 2.7182818284590451...
Pi()
Description

Returns the constant , which is 3.1415926535897931...
