# Comparison Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 58-62).

## Index (line numbers in this file)

- `Equal()` — L83
- `Greater()` — L100
- `Is Missing()` — L148
- `Less Equal Less()` — L221
- `Less Less Equal()` — L179
- `Less()` — L158
- `Not Equal()` — L237
- `Show()` — L53
---

Comparison Functions

//!
Description

If placed on the first line of a script, this comment line causes the script to be run when
opened in JMP without opening into the script editor window.
Notes

You can over-ride this comment when opening the file. Select File > Open. Hold the Ctrl
key while you select the JSL file and click Open. Or right-click the file in the Home
Window Recent Files list and select Edit Script. The script opens into a script window
instead of being executed.
/*debug step*/
/*debug run*/
Description

If placed on the first line of a script, the script is opened in the debugger when it is run.
Notes

All letters must be lowercase. There must be one space between debug and step or run,
and there must be no other spaces present. Only one of these lines can be used, and it must
be the first line of the script; a first line that is blank followed by this comment negates the
debug command.

Comparison Functions
The comparison operators (<, <=, >, >=) work for numbers, quoted strings, and matrices. For
matrices, they produce a matrix of results. If you compare mixed arguments, such as strings
with numbers or matrices, the result is a missing value. Comparisons involving lists are not
allowed and also return missing values.
The equality operators (== and !=) work for numbers, quoted strings, matrices, and lists. For
matrices, they produce a matrix of results; for lists, they produce a single result. If you test
equality of mixed results (for example. strings with numbers or matrices) the result is 0 or
unequal.
Range check operators let you check whether something falls between two specified values:
a = 1;
Show( 1 <= a < 3 );
b = 2;
Show( 2 < b <= 3 );
1 <= a < 3 = 1;
2 < b <= 3 = 0;

JSL Functions, Operators, and Messages
Comparison Functions

59

Expressions with comparison operators are evaluated all at once, not in sequence
All the comparison operators are eliding operators. That means JMP treats arguments joined by
comparison operators as one big clause, as opposed to the way most expressions are
evaluated one operator at a time. Evaluating as a single clause produces different results than
the more usual method of evaluating in pieces. For example, the following two statements are
different:
12 < a < 13;
(12 < a) < 13;

The first statement checks whether a is between 12 and 13, because all three arguments and
both operators are read and evaluated together. The second statement uses parentheses to
regroup the operations explicitly to evaluate from left to right, which would be the normal
way to evaluate most expressions. Thus it first checks whether 12 is less than a, returning 1 if
true or 0 if false. Then it checks whether the result is less than 13, which is always true because
0 and 1 are both less than 13.
All the comparison operators are elided when they are used in matched pairs or in the
unmatched pairs <... <= and <=... <. What this means is that if you want a comparison
statement to be evaluated one comparison operator at a time, you should use parentheses ( )
to control the order of operations explicitly.
Equal(a, b, ...)
a==b==...
Description

Compares all the listed values and tests if they are all equal to each other.
Returns

1 (true) if all arguments evaluate to the same value.
0 (false) otherwise.
Arguments

Two or more variables, references, matrices, or numbers.
Notes

– If more than two arguments are specified, a 1 is returned only if all arguments are
exactly the same. This is typically used in conditional statements and to control loops.
– The comparison is case-sensitive for quoted string comparisons.
Greater(a, b, ...)
a>b>...
Description

Compares all the list values and tests if, in each pair, the left value is greater than the right.

Comparison Functions

Returns

1 (true) if a evaluates strictly greater than b (and b evaluates strictly greater than c, and so
on).
0 (false) otherwise.
Arguments

Two or more variables, references, matrices, or numbers.
Notes

If more than two arguments are specified, a 1 is returned only if each argument is greater
than the one that follows it. This is typically used in conditional statements and to control
loops.
Greater, Less, Greater Or Equal, and Less Or Equal can also be strung together (as in
0 < x <= 5). If you do not group with parentheses, JMP evaluates each pair left to right.

You can also use parentheses to explicitly tell JMP how to evaluate the expression.
Greater or Equal(a, b, ...)
a>=b>=...
Description

Compares all the list values and tests if, in each pair, the left value is greater than or equal
to the right.
Returns

1 (true) if a evaluates strictly greater than or equal to b (and b evaluates strictly greater
than or equal to c, and so on).
0 (false) otherwise.
Arguments

Two or more variables, references, matrices, or numbers.
Notes

If more than two arguments are specified, a 1 is returned only if each argument is greater
than or equal to the one that follows it. This is typically used in conditional statements and
to control loops.
Greater, Less, Greater Or Equal, and Less Or Equal can also be strung together (as in
0 < x <= 5). If you do not group with parentheses, JMP evaluates each pair left to right.

You can also use parentheses to explicitly tell JMP how to evaluate the expression.
Is Missing(expr)
Description

Returns 1 if the expression yields a missing value and 0 otherwise.

JSL Functions, Operators, and Messages
Comparison Functions

61

Less(a, b, ...)
a<b<...
Description

Compares all the list values and tests if, in each pair, the left value is less than the right.
Returns

1 (true) if a evaluates strictly less than b (and b evaluates strictly less than c, and so on).
0 (false) otherwise.
Arguments

Two or more variables, references, matrices, or numbers.
Notes

If more than two arguments are specified, a 1 is returned only if each argument is less than
the one that follows it. This is typically used in conditional statements and to control
loops.
Greater, Less, Greater Or Equal, and Less Or Equal can also be strung together (as in
0 < x <= 5). If you do not group with parentheses, JMP evaluates each pair left to right.

You can also use parentheses to explicitly tell JMP how to evaluate the expression.
Less Less Equal(a, b, c, ...)
a<b<=c<=...
Description

Range check, exclusive below and inclusive above.
Returns

1 (true) if b is greater than a and less than or equal to c.
0 (false) otherwise.
Arguments
a, b, c Variables, references, matrices, or numbers.
Notes

Returns 1 when two conditions are met: the first argument is less than the second
argument, and each remaining argument is less than or equal to its argument on the right.
This is typically used in conditional statements and to control loops.
Less or Equal(a, b, ...)
a<=b<=...
Description

Compares all the list values and tests if, in each pair, the left value is less than or equal to
the right.

Comparison Functions

Returns

1 (true) if a evaluates strictly less than or equal to b (and b evaluates strictly less than or
equal to c, and so on).
0 (false) otherwise.
Arguments

Two or more variables, references, matrices, or numbers.
Notes

If more than two arguments are specified, a 1 is returned only if each argument is less than
or equal to the one that follows it. This is typically used in conditional statements and to
control loops.
Greater, Less, Greater Or Equal, and Less Or Equal can also be strung together (as in
0 < x <= 5). If you do not group with parentheses, JMP evaluates each pair left to right.

You can also use parentheses to explicitly tell JMP how to evaluate the expression.
Less Equal Less(a, b, c, ...)
a<=b<c<...
Description

A range check, inclusive below and exclusive above.
Returns

1 (true) if b is greater than or equal to a and less than c.
0 (false) otherwise.
Arguments
a, b, c Variables, references, matrices, or numbers.
Notes

Returns 1 when two conditions are met: the first argument is less than or equal to the
second argument, and each remaining argument is less than its argument on the right.
This is typically used in conditional statements and to control loops.
Not Equal(a, b)
a!=b
Description

Compares a and b and tests if they are equal.
Returns

0 (false) if a and b evaluate to the same value.
1 (true) otherwise.
