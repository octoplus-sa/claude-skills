# Assignment Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 29-31).

## Index (line numbers in this file)

- `Add To()` — L32
- `Assign()` — L61
- `Divide To()` — L77
- `For Add To()` — L48
- `For Multiply To()` — L111
- `Multiply To()` — L89
- `Post Increment()` — L137
- `PostDecrement()` — L122
- `To()` — L49
---

JSL Functions, Operators, and Messages
Assignment Functions

29

Assignment Functions
JSL also provides operators for in-place arithmetic, or assignment operators. These operations
are all done in place, meaning that the result of the operation is assigned to the first argument.
The most basic assignment operator is the = operator (or the equivalent function Assign). For
example, if a is 3 and you do a+=4, then a becomes 7.
The first argument to an assignment function must be something capable of being assigned
(an L-value). You cannot do something like 3+=4, because 3 is just a value and cannot be
reassigned. However, you can do something like a+=4, because a is a variable whose value
you can set.
Add To(a, b)
a+=b
Description

Adds a and b and places the sum into a.
Returns

The sum.
Arguments

a Must be a variable.
b Can be a variable, a list, a number, or a matrix.
Notes

The first argument must be a variable, because its value must be able to accept a value
change. A number as the first argument produces an error.
For Add To(): Only two arguments are permitted. If one or no argument is specified, Add
To() returns a missing value. Any arguments after the first two are ignored.
For a+=b: More than two arguments can be strung together. JMP evaluates pairs from right
to left, and each sum is placed in the left-hand variable. All arguments except the last must
be a variable.
Example
a+=b+=c

JMP adds b and c and places the sum into b. Then JMP adds a and b and places the sum
into a.

Assignment Functions

Assign(a, b)
a=b
Description

Places the value of b into a.
Returns

The new value of a.
Arguments
a Must be a variable.
b Can be a variable, number, or matrix.
Notes

a must be a variable, because it must be able to accept a value change. A number as the
first argument produces an error. If b is some sort of expression, it’s evaluated first and the
result is placed into a.
Divide To(a, b)
a/=b
Description

Divides a by b and places the result into a.
Returns

The quotient.
Arguments

a Must be a variable.
b Can be a variable, number, or matrix.
Multiply To(a, b)
a*=b
Description

Multiplies a and b and places the product into a.
Returns

The product.
Arguments

a Must be a variable.
b Can be a variable, number, or matrix.
Notes

The first argument must be a variable, because its value must be able to accept a value
change. A number as the first argument produces an error.

JSL Functions, Operators, and Messages
Assignment Functions

31

For Multiply To(): Only two arguments are permitted. If one or no argument is
specified, Multiply To() returns a missing value. Any arguments after the first two are
ignored.
For a*=b: More than two arguments can be strung together. JMP evaluates pairs from
right to left, and each product is placed in the left-hand variable. All arguments except the
last must be a variable.
Example
a*=b*=c

JMP multiplies b and c and places the product into b. Then JMP multiplies a and b and
places the product into a.
PostDecrement(a)
a-Description

Post-decrement. Subtracts 1 from a and places the difference into a.
Returns

a-1
Argument

a Must be a variable.
Notes

If a-- or Post Decrement(a) is inside another expression, the expression is evaluated
first, and then the decrement operation is performed. This expression is mostly used for
loop control.
Post Increment(a)
a++
Description

Post-increment. Adds 1 to a and places the sum into a.
Returns

a+1
Argument

a Must be a variable.
Notes

If a++ or Post Increment(a) is inside another expression, the expression is evaluated
first, and then the increment operation is performed. Mostly used for loop control.
