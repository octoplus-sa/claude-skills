# List Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 175-181).

## Index (line numbers in this file)

- `As List()` — L38
- `Concat Items()` — L48
- `Delimiter()` — L137
- `Eval List()` — L73
- `Include Boundary Delimiters()` — L141
- `Insert Into()` — L105
- `Insert()` — L86
- `Is List()` — L120
- `Items()` — L130
- `List()` — L154
- `N Items()` — L159
- `Names Default To Here()` — L339
- `Remove From()` — L192
- `Remove()` — L175
- `Reverse Into()` — L221
- `Reverse()` — L209
- `Shift Into()` — L238
- `Shift()` — L228
- `Sort List Into()` — L252
- `Sort List()` — L248
- `Substitute Into()` — L281
- `Substitute()` — L259
- `Words()` — L313
---

JSL Functions, Operators, and Messages
List Functions

175

List Functions
As List(matrix)
Description

Converts a matrix into a list. Multi-column matrices are converted to a list of row lists.
Returns

A list.
Argument

matrix Any matrix.
Concat Items({string1, string2, ...}, <delimiter>})
Description

Converts a list of quoted string expressions into one string, with each item separated by a
delimiter. The delimiter is a blank if unspecified.
Returns

The concatenated quoted string.
Arguments

string Any quoted string.
delimiter An optional quoted string that is placed between each item. The delimiter can
be more than one character long.
Example
str1 = "one";
str2 = "two";
str3 = "three";
comb = Concat Items({str1, str2, str3});
"one two three"
comb = Concat Items({str1, str2, str3}, " : ");
"one : two : three"
del = ",";
comb = Concat Items({str1, str2, str3}, del);
"one,two,three"

Eval List({list})
Description

Evaluates expressions inside list.
Returns

A list of the evaluated expressions.

List Functions

Arguments

list A list of valid JSL expressions.
Insert(source, item, <position>)
Insert(source, key, value)
Description

Inserts a new item into the source at the given position. If position is not given, item
is added to the end.
For an associative array: Adds the key into the source associative array and assigns
value to it. If the key exists in source already, its value is overwritten with the new
value.
Required Arguments

source A quoted string, list, vector, expression, or associative array.
item|key Any value to be placed within source. For an associative array, key might or
might not be present in source.
value A value to assign to the key.
Optional Arguments

position Optional numeric value that specifies the position in source to place the item
into.
Insert Into(source, item, <position>)
Insert Into(source, key, value)
Description

Inserts a new item into the source at the given position in place. The source must be an
L-value.
Arguments

source A variable that contains a quoted string, list, vector, display box, expression, or
associative array.
item|key Any value to be placed within source. For an associative array, key might be
present in source.
position Optional numeric value that specifies the position in source to place the item
into.
value A value to assign to the key.
Is List(x)
Description

Returns 1 if the evaluated argument is a list, or 0 otherwise.

JSL Functions, Operators, and Messages
List Functions

177

Items(string, <delimiter>, <Include Boundary Delimiters(Boolean)>)
Description

Returns a list of (possibly empty) quoted sub-strings separated by exactly one of any of the
characters specified in the delimiter argument.
Arguments
string The quoted string that is evaluated.
Delimiter (Optional) The character used as a boundary. If delimiter is absent, an

ASCII space is used. If delimiter is the empty quoted string, each character is treated
as a separate word.
Include Boundary Delimiters(Boolean) (Optional) Returns the empty strings
between the boundary and the delimiter.
Example
Items( "http://www.jmp.com", ":/." );
{"http", "", "", "www", "jmp", "com"}
Items(",toy,", ",");
{"toy"}
Items(",toy,", ",", Include Boundary Delimiters( 1 ));
{"", "toy", ""}
/* There is no text between the boundary (the beginning of the quoted string)
and the comma delimiter, so you get an empty string. The same priniciple
applies to the delimiter at the end of the string. */

List(a, b, c, ...)
{a, b, c, ...}
Description

Constructs a list from a set of items.
N Items(source)
Description

Determines the number of elements in the source specified.
Returns

For a list or display box, the number of items in the list or display box is returned. For an
associative array, the number of keys is returned. For a matrix, the number of elements in
the matrix is returned. For a namespace, the number of functions and variables in the
namespace is returned. For a class object, the number of methods, functions, and variables
is returned.
Arguments
source A list, associative array, matrix, display box, or namespace.

List Functions

Remove(source, position, <n>)
Remove(source, {items})
Remove(source, key)
Description

Deletes the n item(s), starting from the indicated position. If n is omitted, the item at
position is deleted. If position and n are omitted, the item at the end is removed. For
an associative array: Deletes the key and its value.
Returns

A copy of the source with the items deleted.
Arguments
source A quoted string, list, vector, expression, or associative array.
position or key An integer (or list of integers) that points to a specific item (or items) in

the list or expression.
n (Optional) An integer that specifies how many items to remove.
Remove From(source, position, <n>)
Remove From(source, key)
Description

Deletes the n item(s) in place, starting from the indicated position. If n is omitted, the
item at position is deleted. If position and n are omitted, the item at the end is
removed. For an associative array: Deletes the key and its value. The source must be an
L-value.
Returns

The original source with the items deleted.
Arguments
source A quoted string, list, vector, expression, display box, or associative array.
position or key An integer (or list of integers) that points to a specific item (or items) in

the list or expression.
n (Optional) An integer that specifies how many items to remove.
Reverse(source)
Description

Reverse order of elements or terms in the source.
Argument
source A quoted string, list, matrix, or expression.

JSL Functions, Operators, and Messages
List Functions

179

Reverse Into(source)
Description

Reverses the order of elements or terms in source in place.
Argument
source A quoted string, list, matrix, display box, or expression.

Shift(source, <n>)
Description

Shifts an item or n items from the front to the back of the source.
Arguments
source A quoted string, list, matrix, or expression.
n (Optional) An integer that specifies the number of items to shift. Positive values shift

items from the beginning of the source to the end. Negative values shift items from the
end of the source to the beginning. The default value is 1.
Shift Into(source, <n>)
Description

Shifts items in place.
Arguments
source A quoted string, list, matrix, display box, or expression.
n (Optional) An integer that specifies the number of items to shift. Positive values shift

items from the beginning of the source to the end. Negative values shift items from the
end of the source to the beginning. The default value is 1.
Sort List({list}|expr)
Description

Sort the elements or terms of list or expr.
Sort List Into({list}|expr)
Description

Sort the elements or terms of list or expr in place.

List Functions

Substitute(string, "substring", "replacementString", ...)
Substitute({list}, listItem, replacementItem, ...)
Substitute(Expr(sourceExpr), Expr(findExpr), Expr(replacementExpr), ...)
Description

This is a search and replace function. It searches for a specific portion (second argument)
of the source (first argument), and replaces it (third argument).
If a quoted string, finds all matches to substring in the source string, and replaces
them with the replacementString.
If a list, finds all matches to listItem in the source list, and replaces them with the
replacementItem.
If an expression, finds all matches to the findExpr in the sourceExpr, and replaces them
with the replacementExpr. Note that all expressions must be enclosed within an Expr()
function.
Arguments
string, list, sourceExpr A quoted string, list, matrix, or expression in which to

perform the substitution.
substring, listItem, findExpr A quoted string, list item, or expression to be found
in the source string, list, or expression.
replacementString, replacementItem, replacementExpr A quoted string, list item,
or expression to replace the found string, list item, or expression.
Substitute Into(string, substring, replacementString, ...)
Substitute Into(list, listItem, replacementItem, ...)
Substitute Into(Expr(sourceExpr), Expr(findExpr), Expr(replacementExpr),
...)
Description

This is a search and replace function, identical to Substitute() except in place. It
searches for a specific portion (second argument) of the source (first argument), and
replaces it (third argument). The first argument must be an L-value.
If a quoted string, finds all matches to substring in the source string, and replaces
them with the replacementString.
If a list, finds all matches to listItem in the source list, and replaces them with the
replacementItem.
If an expression, finds all matches to the findExpr in the sourceExpr, and replaces them
with the replacementExpr. Note that all expressions must be enclosed within an Expr()
function.

JSL Functions, Operators, and Messages
List Functions

181

Arguments
string, list, sourceExpr A quoted string, list, matrix, or expression in which to

perform the substitution.
substring, listItem, findExpr A quoted string, list item, or expression to be found

in the source string, list, or expression.
replacementString, replacementItem, replacementExpr A quoted string, list item,

or expression to replace the found string, list item, or expression.
Words(string, <delimiter>)
Description

Extracts the words from the quoted string according to the delimiters given. The default
delimiter is ASCII whitespace. If you include a second argument, any and all characters in
that argument are considered delimiters. If delim is an empty string, each character is
treated as a separate word.
Examples
Words( "the quick brown fox" );
{"the","quick","brown","fox"}
Words( "Doe, Jane P.",", ." );
{"Doe","Jane","P"}

Where(<dt>, clause)
Description

Filters and returns indices depending on the given clause. The clause can be a comparison
function or a conditional statement. Columns, matrices, and lists can be mixed and
matched within the same clause.
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
