# Conditional and Logical Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 63-74).

## Index (line numbers in this file)

- `Across()` — L164
- `And()` — L57
- `AndMZ()` — L74
- `Break()` — L94
- `Choose()` — L101
- `Continue()` — L115
- `Count()` — L170
- `Empty()` — L393
- `Filter Each()` — L122
- `For Each Row()` — L282
- `For Each()` — L217
- `IfMZ()` — L343
- `IfMax()` — L313
- `IfMin()` — L331
- `Interpolate()` — L359
- `Is Associative Array()` — L383
- `Is Empty()` — L387
- `Is Expr()` — L394
- `Is Name()` — L400
- `Is Namespace()` — L404
- `Is Number()` — L414
- `Is Scriptable()` — L418
- `Is String()` — L422
- `Match()` — L426
- `MatchMZ()` — L439
- `Or()` — L467
- `OrMZ()` — L482
- `Output()` — L586
- `Return()` — L505
- `Show()` — L191
- `Step()` — L528
- `Stop()` — L534
- `The Match()` — L433
- `The MatchMZ()` — L446
- `The Return()` — L512
- `Transform Each()` — L538
---

JSL Functions, Operators, and Messages
Conditional and Logical Functions

63

Argument
a, b Any variable or number.
Notes

Mostly used for conditional statements and loop control.

Conditional and Logical Functions
And(a, b)
a&b
Description

The logical And.
Returns

1 (true) if both a and b are true.
0 (false) if either a or b is false or if both a and b are false.
Missing if either a or b is a missing value or if both a and b are missing values.
Arguments

Two or more variables or expressions.
Notes

More than two arguments can be strung together. a&b returns 1 (true) only if all arguments
evaluate to true.
AndMZ(a, b)
a:&b
Description

Returns the logical AND of all arguments. Missing values are treated as zeroes.
Returns

1 (true) if both a and b are true.
0 (false) if either a or b is false or if both a and b are false.
0 (false) if either a or b is a missing value or if both a and b are missing values.
Arguments

Two or more variables or expressions.
Notes

More than two arguments can be strung together. a:&b returns 1 (true) only if all
arguments evaluate to true.

Conditional and Logical Functions

Break()
Description

Stops execution of a loop completely and continues to the statement following the loop.
Notes
Break() works with For and While loops and also with For Each Row.

Choose(expr, r1, r2, r3, ..., resultElse)
Description

Evaluates expr. If the value of expr is 1, r1 is returned; if 2, the value of r2 is returned,
and so on. If no matches are found, the last argument (resultElse) is returned.
Returns

The value whose index in the list of arguments matches expr, or the value of the last
argument.
Arguments

expr An expression or a value.
r1, r2, r3, ... An expression or a value.
resultElse The argument that is returned when no matches are found.
Continue()
Description

Ends the current iteration of a loop and begins the loop at the next iteration.
Notes
Continue() works with For and While loops, and also with For Each Row.

Filter Each(names, container, locals, body)
Description

Iterates over a container, which can be a list, an associative array, or a matrix, and returns
a subset of the values in the container based on the evaluation of a Boolean expression at
each iteration. The value, key, or element, as well as the index number, are all available at
each iteration.
– For associative array containers, the key and value can be accessed using a two-item
list.
– For matrix containers, a linear index is provided by default, but a two-item list can be
used to access the row and column indices.

JSL Functions, Operators, and Messages
Conditional and Logical Functions

65

These symbols are provided within the body of the loop only. A list of local variables can
also be provided. If local variables are defined, they are initialized after the first iteration
symbols are set.
Returns

A subset from the original container. The return object has the same type as the original
container.
Arguments

names Specification of loop control variable names, specified as a list. The form of the list
is determined by the type of container. All of the names are optional, so you need to
specify them only if you need to refer to them in the locals or body arguments. If you
do not specify any names, the first argument should be an empty list, which can be
specified as {} or List().
For a list container, the names list contains a name for each value in the list and a name
for the index of each value in the list.
For an associative array container, the names list contains a two-item list of names and a
name for the index of each item in the associative array.
For a matrix container, the names list contains a name for each element in the matrix
and a second argument for the index of each element in the matrix. The second
argument can be specified as a single name or as a two-item list of names that represent
symbols for the row and column indices.
When specifying multiple containers using the Across() keyword, the names list
contains a list of names that refer to values in each container. The number of names in
the first item in the names list must match the number of containers specified in the
Across() keyword.
container A list, associative array, or a matrix. The container can be defined in the
argument or it can be a reference to a previously defined object.
This argument can also use the Across() keyword, which enables you to use the
function across multiple containers. The multiple containers can be specified as
separate arguments or as items in a list. The Across() keyword has an optional
Count() argument that enables you to specify how containers of different sizes are
handled. The available Count() options are: "Shortest", "Longest", "Enforce
Equal", and N, where N is a number. If you specify a number, the function iterates
through all containers exactly N times; note that the function loops back to the start of
containers that have fewer than N items.
locals A list of variables that are local to the function. This is equivalent to other Local
variable initializations in JSL. The initialization of the local variables occurs after the
first loop control variables have been set, but the local variables do not get initialized
again after that.
body Any number of valid JSL expressions, glued together if there are more than one. The
result of the JSL expressions should be a Boolean value. If the result of the expression is
true, the container value at the current iteration is included in the result; otherwise, the

Conditional and Logical Functions

container value at the current iteration is not included in the result. You can use the
Continue() function as an equivalent way to return false and skip to the next iteration.
You can also use Break() function to stop iteration through the loop and proceed to the
next expression that follows the loop. See “Break and Continue Functions”.
Example
values = Filter Each( {x}, {10, 20, 30}, x > 15 );
Show( values );
values = {20, 30};

For(init, while, increment, body)
Description

Repeats the statement(s) in the body as long as the while condition is true. init and
increment control iterations.
Returns

Null.
Arguments

init Initialization of loop control counter.
while Condition for loop to continue or end. As long as the conditional statement while
is true, the loop is iterated one more time. As soon as while is false, the loop is exited.
increment Increments (or decrements) the loop counter after while is evaluated every
time the loop is executed.
body Any number of valid JSL expressions, glued together if there are more than one.
Example
mysum = 0; myprod = 1;
For( i = 1, i <= 10, i++, mysum += i; myprod *= i; );
Show( mysum, myprod );
mysum = 55;
myprod = 3628800;

For Each(names, container, locals, body)
Description

Iterates over a container, which can be a list, an associative array, or a matrix, and provides
the value, key, or element at each iteration. The index number is also available at each
iteration. For associative array containers, the key and value can be accessed using a
two-item list. For matrix containers, a linear index is provided by default, but a two-item
list can be used to access the row and column indices. These symbols are provided within
the body of the loop only. A list of local variables can also be provided. If local variables
are defined, they are initialized after the first iteration symbols are set.

JSL Functions, Operators, and Messages
Conditional and Logical Functions

67

Arguments

names Specification of loop control variable names, specified as a list. The form of the list
is determined by the type of container. All of the names are optional, so you need to
specify them only if you need to refer to them in the locals or body arguments. If you
do not specify any names, the first argument should be an empty list, which can be
specified as {} or List().
For a list container, the names list contains a name for each value in the list and a name
for the index of each value in the list.
For an associative array container, the names list contains a two-item list of names and a
name for the index of each item in the associative array.
For a matrix container, the names list contains a name for each element in the matrix
and a second argument for the index of each element in the matrix. The second
argument can be specified as a single name or as a two-item list of names that represent
symbols for the row and column indices.
When specifying multiple containers using the Across() keyword, the names list
contains a list of names that refer to values in each container. The number of names in
the first item in the names list must match the number of containers specified in the
Across() keyword.
container A list, associative array, or a matrix. The container can be defined in the
argument or it can be a reference to a previously defined object.
This argument can also use the Across() keyword, which enables you to use the
function across multiple containers. The multiple containers can be specified as
separate arguments or as items in a list. The Across() keyword has an optional
Count() argument that enables you to specify how containers of different sizes are
handled. The available Count() options are: "Shortest", "Longest", "Enforce
Equal", and N, where N is a number. If you specify a number, the function iterates
through all containers exactly N times; note that the function loops back to the start of
containers that have fewer than N items.
locals A list of variables that are local to the function. This is equivalent to other Local
variable initializations in JSL. The initialization of the local variables occurs after the
first loop control variables have been set, but the local variables do not get initialized
again after that.
body Any number of valid JSL expressions, glued together if there are more than one.
You can use the Continue() function to skip to the next iteration. You can also use
Break() function to stop iteration through the loop and proceed to the next expression
that follows the loop. See “Break and Continue Functions”.
Example
For Each( {value, index}, {10, 20, 30}, Show( value, index ) );
value = 10;
index = 1;
value = 20;
index = 2;

Conditional and Logical Functions

value = 30;
index = 3;

For Each Row(<dt>, script)
Description

Repeats the script on each row of the data table.
Returns

Null.
Required Argument

script Any valid JSL expressions.
Optional Argument

dt Positional argument that is a reference to a data table. If this argument is not in the
form of an assignment, then it is considered a data table expression.
Example

The following example creates data table references and then iterates over each row in Big
Class.jmp. If the value of age in a row is greater than 15, the age is printed to the log.
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
For Each Row( dt, If( :age > 15, Show( :age ) ) );

If(condition1, result1, <condition2, result2>, ..., <elseResult>)
Description

Evaluates the first of each pair of arguments and returns the evaluation of the result
expression associated with the first condition argument that evaluates to a nonzero
result. The condition arguments are evaluated in order. If all of the condition
arguments evaluate to zero, the optional elseResult is evaluated and the result is
returned. If no elseResult is specified, and none of the conditions are true, a missing
value is returned. If all of the condition arguments evaluate to missing, a missing value
is returned.
IfMax(expr1, result1, expr2, result2, ... <all missing results>)
Description

Evaluates the first of each pair of arguments and returns the evaluation of the result
expression (the second of each pair) associated with the maximum of the expressions. If
more than one expression is the maximum, the first maximum is returned. If all
expressions are missing and a final result is not specified, missing is returned. If all
expressions are missing and a final result is specified, that final result is returned. The test
expressions must evaluate to numeric values, but the result expressions can be anything.
Returns

The result expression associated with the maximum of the expressions

JSL Functions, Operators, and Messages
Conditional and Logical Functions

69

IfMin(expr1, result1, expr2, result2, ... <all missing results>)
Description

Evaluates the first of each pair of arguments and returns the evaluation of the result
expression (the second of each pair) associated with the minimum of the expressions. If
more than one expression is the minimum, the first minimum is returned. If all
expressions are missing and a final result is not specified, missing is returned. If all
expressions are missing and a final result is specified, that final result is returned. The test
expressions must evaluate to numeric values, but the result expressions can be anything.
Returns

The result expression associated with the minimum of the expressions
IfMZ(condition1, result1, <condition2, result2>, ..., <elseResult>)
Description

Evaluates the first of each pair of arguments and returns the evaluation of the result
expression associated with the condition1 argument that evaluates to a nonzero result.
The condition arguments are evaluated in order. If all of the condition arguments
evaluate to zero or missing, the optional elseResult is evaluated and the result is
returned. If no elseResult is specified, and none of the conditions are true, a missing
value is returned.
Notes

The test arguments are evaluated in order until the first nonzero result. If all test results
return zero or missing, the elseExpr argument is evaluated.
IfMZ() is equivalent to If() where missing values for evaluated condition arguments
are treated as zero.

Interpolate(x|xmatrix|xlist, x1, y1, x2, y2, ...)
Interpolate(x|xmatrix|xlist, xmatrix, ymatrix)
Interpolate({x, y}, xvector, yvector, zmatrix)
Description

Performs linear interpolation for continuous data. There are many ways to specify the
function.
In the simplest cases where the first argument is a single numeric value, the y value
corresponding to a given x value between two sets of points or by matrices xmatrix and
ymatrix. The x values, (x1, x2, ...) or xmatrix, must be in ascending order.
If the first argument is a matrix or list of numeric values, the resulting matrix or list is a set
of interpolated values.

Conditional and Logical Functions

You can perform bilinear interpolation using the four-argument case. Here, the first
argument is a list of two points, the second and third arguments are vectors that define the
grid of x and y values, and the fourth argument is a matrix of data points. The function
then finds the interpolated z value within the appropriate quadrant of the zmatrix.
Returns

The interpolated value or values. In the three-argument cases, the return object type
matches the type of the first argument. In the four-argument case, the return object is a
number.
Is Associative Array(name)
Description

Returns 1 if the evaluated argument is an associative array, or 0 otherwise.
Is Empty(global)
Is Empty(dt)
Is Empty(col)
Description

Returns 1 if the global variable, data table, or data column is undefined or holds the
Empty() value, or 0 otherwise.
Is Expr(x)
Description

Returns 1 if the evaluated argument is an expression, or 0 otherwise.
Is List
See “Is List(x)”.
Is Name(x)
Description

Returns 1 if the evaluated argument is a name, or 0 otherwise.
Is Namespace(namespace)
Description

Returns 1 if the namespace argument is a namespace; returns 0 otherwise.

JSL Functions, Operators, and Messages
Conditional and Logical Functions

71

Is Number(x)
Description

Returns 1 if the evaluated argument is a number or missing numeric value, or 0 otherwise.
Is Scriptable(x)
Description

Returns 1 if the evaluated argument is a scriptable object, or 0 otherwise.
Is String(x)
Description

Returns 1 if the evaluated argument is a quoted string, or 0 otherwise.
Match(x, value1, result1, value2, result2, ..., resultElse)
Description

If a is equal to value1, then result1 is returned. If a is equal to value2, result2 is
returned, and so on.
Notes

The Match() function explicitly checks to see if the compare expression x is missing and if
the value of value1 is missing, then it returns the value of result1; otherwise it continues
to compare the expression x to each valueN value in each valueN/resultN pair,
ignoring any missing values. If the expression x is equal to any of the valueN value, then
the corresponding resultN value is returned. If no matching valueN value is found, then
the resultElse value is returned.
MatchMZ(x, value1, expr1, value2, expr2, ..., exprElse)
Description

Evaluates and returns the exprN argument that equals x or evaluates and returns the
exprElse argument if no value equals x.
Notes

The MatchMZ() function works the same as the Match() function except that missing
values are treated as 0.
Not(a)
!a
Description

The logical Not.

Conditional and Logical Functions

Returns

0 (false) if a!=0.
1 (true) if a=0.
Missing value if a is missing.
Argument

a Any variable or number. The variable must have a numeric or matrix value.
Notes

Mostly used for conditional statements and loop control.
Or(a, b)
a|b
Description

The logical Or.
Returns

1 (true) if either of or both a and b are true.
0 (false) otherwise.
Missing if either are a or b are missing and the other is missing or 0.
Arguments
a, b Any variable or number.
Notes

Mostly used for conditional statements and loop control.
OrMZ(a, b)
a:|b
Description

Returns the logical OR of all arguments with missing values treated as zeroes: 1 if any
arguments are nonzero and 0 otherwise.
Returns

1 (true) if either of or both a and b are true.
0 (false) otherwise.
Arguments
a, b Any variable or number.
Notes

– Mostly used for conditional statements and loop control.

JSL Functions, Operators, and Messages
Conditional and Logical Functions

73

– Or() returns missing if any evaluated argument is missing. OrMZ() returns 0 if any
evaluated argument is missing.
Return(<expr1>, <expr2>, ..., <exprN>)
Description

Returns an expression value from a user-defined function.
Example

This example returns the evaluation of both expressions in the Return() function as a list.
The Return() function can have more than one argument. If only one is present, then the
value of the expression is returned. If more than one is present, then the values of all the
expressions is returned in a list.
f = Function( {a, b},
Return( a - b, a + b )
);
{lo, hi} = f( 10, 1 );
Show( lo, hi );
Show( f( 7, 15 ) );
lo = 9;
hi = 11;
f(7, 15) = {-8, 22};

Notes
Return() not enclosed by a function, method, or recursive function call causes an error.

Step(x0, x1, y1, x2, y2, ...)
Step(x0, [x1, x2, ...], [y1, y2, ...])
Description

Returns the y argument corresponding to the largest x argument that is less than or equal
to x0. The x points must be specified in ascending order.
Stop()
Description

Immediately stops a script that is running.
Transform Each(names, container, <Output(type)>, <locals>, body)
Description

Iterates over a container, which can be a list, an associative array, or a matrix, and updates
each of the values in the container based on the evaluation of a JSL expression at each
iteration. The value, key, or element, as well as the index number, are all available at each
iteration. For associative array containers, the key and value can be accessed using a

Conditional and Logical Functions

two-item list. For matrix containers, a linear index is provided by default, but a two-item
list can be used to access the row and column indices. These symbols are provided within
the body of the loop only. A list of local variables can also be provided. If local variables
are defined, they are initialized after the first iteration symbols are set.
Returns

An updated version of the original container. The return object has the same type as the
original container, unless the Output() keyword is used to designate a different type for
the returned container.
Arguments

names Specification of loop control variable names, specified as a list. The form of the list
is determined by the type of container. All of the names are optional, so you need to
specify them only if you need to refer to them in the locals or body arguments. If you
do not specify any names, the first argument should be an empty list, which can be
specified as {} or List().
For a list container, the names list contains a name for each value in the list and a name
for the index of each value in the list.
For an associative array container, the names list contains a two-item list of names and a
name for the index of each item in the associative array.
For a matrix container, the names list contains a name for each element in the matrix
and a second argument for the index of each element in the matrix. The second
argument can be specified as a single name or as a two-item list of names that represent
symbols for the row and column indices.
When specifying multiple containers using the Across() keyword, the names list
contains a list of names that refer to values in each container. The number of names in
the first item in the names list must match the number of containers specified in the
Across() keyword.
container A list, associative array, or a matrix. The container can be defined in the
argument or it can be a reference to a previously defined object.
This argument can also use the Across() keyword, which enables you to use the
function across multiple containers. The multiple containers can be specified as
separate arguments or as items in a list. The Across() keyword has an optional
Count() argument that enables you to specify how containers of different sizes are
handled. The available Count() options are: "Shortest", "Longest", "Enforce
Equal", and N, where N is a number. If you specify a number, the function iterates
through all containers exactly N times; note that the function loops back to the start of
containers that have fewer than N items.
Output(type) Specifies a type for the output. This can be "List", "Matrix", or
"Associative Array". By default, the output type matches the type of the input
container.
locals A list of variables that are local to the function. This is equivalent to other Local
variable initializations in JSL. The initialization of the local variables occurs after the
