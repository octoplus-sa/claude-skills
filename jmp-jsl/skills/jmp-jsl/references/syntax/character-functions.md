# Character Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 32-46).

## Index (line numbers in this file)

- `BLOB To Char()` — L83
- `BLOB To Matrix()` — L109
- `Base()` — L203
- `Char To BLOB()` — L157
- `Char To Hex()` — L184
- `Char()` — L128
- `Collapse Whitespace()` — L208
- `Concat To()` — L258
- `Concat()` — L220
- `Contains Item()` — L323
- `Contains()` — L297
- `Ends With()` — L351
- `For SubtractTo()` — L68
- `Hex To BLOB()` — L367
- `Hex To Char()` — L376
- `Hex To Number()` — L394
- `Hex()` — L185
- `Include Boundary Delimiters()` — L440
- `Item()` — L419
- `Left()` — L465
- `Length()` — L472
- `Lowercase()` — L484
- `Munger()` — L503
- `Num()` — L521
- `Pad To()` — L207
- `Regex()` — L528
- `Repeat()` — L552
- `Right()` — L363
- `Starts With()` — L579
- `Substr()` — L597
- `Subtract To()` — L52
- `Text Score()` — L615
- `Titlecase()` — L636
- `Trim Whitespace()` — L659
- `Trim()` — L658
- `Unmatched()` — L439
- `Uppercase()` — L682
- `Use Locale()` — L144
- `Word()` — L458
- `Write()` — L347
- `XPath Query()` — L719
---

Character Functions

Subtract To(a, b)
a-=b
Description

Subtracts b from a and places the difference into a.
Returns

The difference.
Arguments

a Must be a variable.
b Can be a variable, number, or matrix.
Notes

The first argument must be a variable, because its value must be able to accept a value
change. A number as the first argument produces an error.
For SubtractTo(): Only two arguments are permitted. If fewer than two or more than
two arguments is specified, SubtractTo() returns a missing value.
For a-=b: More than two arguments can be strung together. JMP evaluates pairs from
right to left, and each difference is placed in the left-hand variable. All arguments except
the last must be a variable.
Example
a-=b-=c

JMP subtracts c from b and places the difference into b. Then JMP subtracts b from a and
places the difference into a.

Character Functions
Most character functions take character arguments and quoted return character strings,
although some take numeric arguments or return numeric data. Arguments that are literal
character strings must be enclosed in quotation marks.
BLOB To Char(blob, <Encoding="enc">)
Description

Reinterpret binary data as a quoted Unicode string.
Returns

A quoted string.
Required Argument

blob A binary large object.

JSL Functions, Operators, and Messages
Character Functions

33

Optional Argument

Encoding A quoted string that specifies an encoding. The default encoding for the
character string is "utf-8". "utf-16le", "utf-16be", "us-ascii", "iso-8859-1",
"ascii~hex", "shift-jis", and "euc-jp" are also supported.
Notes

The optional argument "ascii~hex" is intended to make conversions of blobs containing
normal ASCII data simpler when the data might contain CR, LF, or TAB characters (for
example) and those characters do not need any special attention.
BLOB To Matrix(blob, type, bytes, endian, <nCols>)
Description

Creates a matrix by converting each byte in the blob to numbers.
Returns

A matrix that represents the blob.
Required Arguments

blob A blob or reference to a blob.
type A quoted string that contains the named type of number. The options are "int",
"uint", or ʺfloat".
bytes Byte size of the data in the blob. Options are 1, 2, 4, or 8.
endian The quoted endian-ness of your system: "Big" (the first byte is most significant),
"Little" (the first byte is the least significant), or "Native" (the machine’s native
format).
Optional Argument

<nCols> The number of columns in the matrix. The default value is 1.
Char(x, <width>, <decimal>, < <<Use Locale(Boolean)>)
Description

Converts an expression or numeric value into a quoted character string.
Returns

A quoted string.
Required Argument
x an expression or a numeric value. An expression must be quoted with Expr().

Otherwise, its evaluated value is converted to a quoted string.
Optional Arguments
width A number that sets the maximum number of characters in the quoted string.
decimal A number that sets the maximum number of places after the decimal that is

included in the quoted string.
Use Locale(Boolean) Preserves locale-specific numeric formatting.

Character Functions

Example
Char( Pi(), 10, 4)
"3.1416"
Char( Pi(), 3, 4)
"3.1"

Notes

The width argument overrides the decimal argument.
Char To BLOB(string, <encoding="enc">)
Description

Converts a quoted string of characters into a binary (blob).
Returns

A binary object.
Required Argument

string A quoted string or a reference to a string.
Optional Argument

encoding A quoted string that specifies an encoding. The default encoding for the blob is
"utf-8". "utf-16le", "utf-16be", "us-ascii", "iso-8859-1", "ascii~hex",
"shift-jis", and "euc-jp" are also supported.
Notes

Converting BLOBs into printable format escapes \ (in addition to ~ " ! and characters
outside of the printable ASCII range) into hex notation (~5C for the backslash character).
x = Char To BLOB( "abc\def\!n" );
y = BLOB To Char( x, encoding = "ASCII~HEX" );
If(
y == "abc~5Cdef~0A", "JMP 12.2 and later behavior",
y == "abc\def~0A", "Pre-JMP 12.2 behavior"
);
"JMP 12.2 and later behavior" // output

Char To Hex(value, <integer|encoding="enc">)
Hex(value, <integer|encoding="enc"|Base(number)|Pad To(number)>)
Description

Returns the hexadecimal (or other base number system) text corresponding to the given
value and encoding, which can be a number a quoted string or a blob. If the value is a
number, IEEE 754 64-bit encoding is used unless one of the optional arguments, integer,
or Base, is provided.
Required Argument
value Any number, quoted string, or blob.

JSL Functions, Operators, and Messages
Character Functions

Optional Arguments
integer A quoted switch that causes the value to be interpreted as an integer.
encoding A quoted string that specifies an encoding. The default encoding is "utf-8".
"utf-16le", "utf-16be", "us-ascii", "iso-8859-1", "ascii~hex", "shift-jis",
and "euc-jp" are also supported.
Base(number) An integer value between 2 and 36 inclusive. If base is specified, the

function returns the text corresponding to the specified number in that base number
system instead of hexadecimal.
Pad To(number) A value to specify the padded width of the hex output.
Collapse Whitespace(text)
Description

Trims leading and trailing whitespace and replaces interior whitespace with a single
space. That is, if more than one white space character is present, the Collapse
Whitespace function replaces the two spaces with one space.
Returns

A quoted string.
Required Argument

text A quoted string.
Concat(a, b)
Concat(A, B)
a||b
A||B
Description

For quoted strings: Appends the string b to the string a. Neither argument is changed.
For lists: Appends the list b to the list a. Neither argument is changed.
For matrices: Horizontal concatenation of two matrices, A and B.
Returns

For quoted strings: A quoted string composed of the string a directly followed by the
string b.
For lists: A list composed of the list a directly followed by the list b.
For matrices: A matrix.
Arguments

Two or more quoted strings, quoted string variables, lists, or matrices.
Example
a = "Hello"; b = " "; c = "World"; a || b || c;

35

Character Functions

"Hello World"
d = {"apples", "bananas"}; e = {"peaches", "pears"}; Concat( d, e );
{"apples", "bananas", "peaches", "pears"}
A = [1 2 3]; B = [4 5 6]; Concat( A, B );
[1 2 3 4 5 6]

Notes

More than two arguments can be strung together. Each additional quoted string is
appended to the end, in left to right order. Each additional matrix is appended in left to
right order.
Concat Items
See “Concat Items({string1, string2, ...}, <delimiter>})”.
Concat To(a, b)
Concat To(a, b)
a||=b
A||=B
Description

For quoted strings: Appends the string b to the string a and places the new concatenated
string into a.
For matrices: Appends the matrix b to the matrix a and places the new concatenated
matrix into a.
For lists: Appends the list b to the list and places the new concatenated list into a.
Returns

For quoted strings: A string composed of the string a directly followed by the string b.
For matrices: A matrix.
For lists: A list composed of the list a directly followed by the list b.
Arguments

Two or more quoted strings, quoted string variables, matrices, or lists. The first variable
must be a variable whose value can be changed.
Notes

More than two arguments can be strung together. Each additional quoted string, matrix, or
list is appended to the end, in left to right order.
Example
a = "Hello"; b = " "; c = "World"; Concat To( a, b, c ); Show( a );
a = "Hello World"
A = [1 2 3]; B = [4 5 6]; Concat To( A, B ); Show( A );
A = [1 2 3 4 5 6];

JSL Functions, Operators, and Messages
Character Functions

37

d = {"apples", "bananas"}; e = {"peaches", "pears"}; Concat to(d,e); Show( d
);
d = {"apples", "bananas", "peaches", "pears"};

Contains(whole, part, <start>)
Description

Determines whether part is contained within whole.
Returns

If part is found: For lists, quoted strings, and namespaces, the numeric position where the
first occurrence of part is located. For associative arrays, 1.
If part is not found, 0 is returned in all cases.
Required Arguments

whole A quoted string, list, namespace, or associative array.
part For a quoted string or namespace, a string that can be part of the string whole. For a
list, an item that can be an item in the list whole. For an associative array, a key that can
be one of the keys in the map whole.
Optional Argument

start A numeric argument that specifies a starting point within whole. If start is
negative, contains searches whole for part backward, beginning with the position
specified by the length of whole – start. Note that start is meaningless for
associative arrays and is ignored.
Example
nameList={"Katie", "Louise", "Jane", "Jaclyn"};
r = Contains(nameList, "Katie");

The example returns a 1 because “Katie” is the first item in the list.
Contains Item(x, <item | {list} | pattern>, <delimiter>)
Description

Identifies multiple responses by searching for the specified item, list, pattern, or delimiter.
The function can be used on columns with the Multiple Response modeling type or
column property.
Returns

Returns a Boolean that indicates whether the word (item), one of a list of words (list), or
pattern (pattern) matches one of the words in the text represented by x. Words are
delimited by the characters in the optional quoted delimiter (delimiter) string. A comma
is the default delimiter. Blanks are trimmed from the ends of each extracted word from the
input text string (x).

Character Functions

Example

The following example searches for “pots” followed by a comma and then outputs the
result.
x = "Franklin Garden Supply is a leading online store featuring garden decor,
statues, pots, shovels, benches, and much more.";
b = Contains Item( x, "pots", "," );
If( b,
Write( "The specified items were found." ), Write( "No match." )
);
The specified items were found.

Ends With(string, substring)
Description

Determines whether the quoted substring appears at the end of string.
Returns

1 if quoted string ends with a quoted substring, otherwise 0.
Required Arguments

string A quoted string or a quoted string variable. Can also be a list.
substring A quoted string or a quoted string variable. Can also be a list.
Equivalent Expression
Right(string, Length(substring)) == substring

Hex(value, <integer|encoding="enc"|Base(number)|Pad To(number)>)
See “Char To Hex(value, <integer|encoding=ʺencʺ>)”.
Hex To BLOB(string)
Description

Converts the quoted hexadecimal string (including whitespace characters) to a blob
(binary large object).
Example
Hex To BLOB( "4A4D50" );
Char To BLOB("JMP", "ascii~hex")

Hex To Char(string, <encoding>)
Description

Converts the quoted hexadecimal string to its character equivalent.
Example

Hex To Char( ʺ30ʺ ) results in “0”.

JSL Functions, Operators, and Messages
Character Functions

39

Notes

The default quoted encoding for character string is "utf-8". "utf-16le", "utf-16be",
"us-ascii", "iso-8859-1", "ascii~hex", "shift-jis", and "euc-jp" are also
supported.
Hex To Number(string, <Base(number)>)
Description

Returns the number corresponding to the hexadecimal (or other base number system) text.
Required Argument

string A quoted hexadecimal string.
Optional Argument
Base(number) An integer between 2 and 36 inclusive. If base is specified, the text is

treated as a quoted string representing the number in that base.
Example
Hex To Number( "80" );
128

Notes

– 16-digit hexadecimal numbers are converted as IEEE 754 64-bit floating point numbers.
Otherwise, the input is treated as a hexadecimal integer.
– Whitespace between bytes (or pairs of digits) and in the middle of bytes is permitted
(for example, FF 1919 and F F1919).
Insert
See “Insert(source, item, <position>)”.
Insert Into
See “Insert Into(source, item, <position>)”.
Item(n|[first last], string, <delimiter>, <Unmatched(result string)>,
<Include Boundary Delimiters(Boolean)>)
Description

Returns the nth item or the span from the first to last item of the quoted string according
to the quoted string delimiters given. If you include a third argument, any and all
characters in that argument are taken to be delimiters.
Required Arguments

n The position of the word being extracted.
[first last] A matrix that defines the beginning and end word range to return.
string The quoted string that is evaluated.

Character Functions

Optional Arguments

delimiter The character used as a boundary. If delimiter is absent, an ASCII space is
used. If delimiter is the quoted empty string, each character is treated as a separate
word.
Unmatched(result string) The quoted string to print if no match is found.
Include Boundary Delimiters(Boolean) Determines how delimiters on the front and
back of string are treated. The default value is false, which means that the delimiters on
these boundaries are ignored. If the value is true, delimiters on these boundaries
produce an empty element (similar to consecutive delimiters within a string).
Example

Consecutive delimiters are treated as though they have a word between them. In this
example, the delimiters are a comma and a space.
Item( 4,"the

quick, brown fox", ", " ); // quick is preceded by two spaces

The expression is processed as follows:
the<delim[space]><word2><delim[space]>quick<delim[comma]><word
4><delim[space]>brown<delim[space]>fox
Because word4 is empty, this expression returns a quoted empty string.
Item() is the same as Word() except that Item() treats each delimiter character as a
separate delimiter, and Word() treats several adjacent delimiters as a single delimiter.
Word( 4,"the

quick, brown fox", ", " ); // quick is preceded by two spaces

This expression is processed as follows:
the<delim[2 spaces]>quick<delim[comma + space]>brown<delim[space]>fox
It returns ʺfoxʺ.
Left(string, n, <filler>)
Left({list}, n, <filler>)
Description

Returns a truncated or padded version of the original quoted string or list. The result
contains the left n characters or list items, padded with any filler on the right if the
length of string is less than n.
Length(string)
Description

Returns the length of the given quoted string (in characters), list (in items), associative
array (in number of keys), BLOB (in bytes), matrix (in elements), namespace (in number of
functions and variables), or class (in number of methods, functions, and variables).

JSL Functions, Operators, and Messages
Character Functions

41

Lowercase(string)
Description

Converts any uppercase character found in quoted string to the equivalent lowercase
character.
Matrix to BLOB(matrix, type, bytesEach, endian(value))
Description

Makes a BLOB from a matrix by converting the matrix elements to 1-byte, 2-byte, or 4-byte
signed or unsigned integers or 4-byte or 8-byte floating point numbers.
Required Arguments

matrix The matrix.
type The quoted type of BLOB: int, uint, or float.
bytesEach The number of bytes in each int, uint, or float. Integers can be 1, 2, or 4 bytes
each, and floats can be 4 or 8 bytes each.
endian(value) The quoted endian-ness of your system: "Big" (the first byte is most
significant), "Little" (the first byte is the least significant), or "Native" (the machine’s
native format).
Munger(string, start position, find|length, <replacement string>)
Description

Computes new quoted character strings from the quoted string by inserting or deleting
characters. It can also produce substrings, calculate indexes, and perform other tasks
depending on how you specify its arguments.
Required Arguments

start position A numeric expression that specifies the starting position to search in
the quoted string. If the start position is greater than the position of the first
instance of the find argument, the first instance is disregarded. If the start position
is greater than the search string’s length, Munger() uses the string’s length as the start
position.
find|length Specifies the string or number of characters to find.
Optional Argument

replacement string The quoted replacement string. If replacement string is
omitted, a substring between start position, and position and length, is returned.
Num(string)
Description

Converts a quoted character string into a number.

Character Functions

Regex(source, pattern, (<replacement string>, <format, "GLOBALREPLACE",
"IGNORECASE">>)
Description

Searches for the quoted pattern within the quoted source string.
Returns

The matched text as a quoted string or numeric missing if there was no match.
Required Arguments

source A quoted string.
pattern A quoted regular expression.
replacement string The replacement string.
Optional Arguments

format A backreference to the capturing group. The default is \0, which is the entire
matched quoted string. \n returns the nth match.
"IGNORECASE" The search is case sensitive, unless you specify ʺIGNORECASE".
"GLOBALREPLACE" Applies the regular expression to the quoted source string repeatedly
until all matches are found.
Remove
See “Remove(source, position, <n>)”.
Remove From
See “Remove From(source, position, <n>)”.
Repeat(source, a)
Repeat(matrix, a, b)
Description

Returns a copy of source concatenated with itself a times. Or returns a matrix composed
of a row repeats and b column repeats. The source can be text, a matrix, or a list.
Reverse
See “Reverse(source)”.
Reverse Into
See “Reverse Into(source)”.

JSL Functions, Operators, and Messages
Character Functions

43

Right(string, n, <filler>)
Right({list}, n, <filler>)
Description

Returns a truncated or padded version of the original quoted string or list. The result
contains the right n characters or list items, padded with any optional filler on the left if
the length of string is less than n.
Shift
See “Shift(source, <n>)”.
Shift Into
See “Shift Into(source, <n>)”.
Starts With(string, substring)
Description

Determines whether the quoted substring appears at the start of the quoted string.
Returns

1 if string starts with substring, otherwise 0.
Arguments

string A quoted string or a reference to one. Can also be a list.
substring A quoted string or a reference to one. Can also be a list.
Equivalent Expression
Left(string, Length("substring")) = = "substring"

Substitute
See “Substitute(string, ʺsubstringʺ, ʺreplacementStringʺ, ...)”.
Substitute Into
See “Substitute Into(string, substring, replacementString, ...)”.
Substr(string, start, length)
Description

Extracts the characters that are the portion of the first argument beginning at the position
given by the second argument and ending based on the number of characters specified in
the third argument. The first argument can be a character column or value, or an

Character Functions

expression evaluating to same. The starting argument and the length argument can be
numbers or expressions that evaluate to numbers.
Example

This example extracts the first name:
Substr( "Katie Layman", 1, 5 );

The function starts at position 1, reads through position 5, and ignores the remaining
characters, which yields “Katie.”
Text Score(text column, text-to-number, <weighting>, <{support vectors}>,
<text explorer setup>)
Description

Used to create scoring formulas in Text Explorer. Not supported for use with the Stem for
Combining option.
Returns

Returns a vector of scores.
Required Arguments

text column The data table column.
text-to-number An associative array that maps lowercase words to numbers.
Optional Arguments

weighting The quoted "Count", "Binary", "Ternary", "LogCount", "LCA", or an array
of inverse document frequency weights for TFLogIDF. The default value is "Count".
support vectors A list of vectors that are used in the text scoring. The number and
length of the vectors depends on the weighting argument.
text explorer setup An expression that contains a block of Text Explorer setup
information.
Titlecase(string)
Description

Converts the quoted string to title case; each word in the string has an initial uppercase
character and subsequent lowercase characters.
Returns

A quoted string.
Argument

string A quoted string.
Example

The following function capitalizes the name:
Titlecase( "veronica layman ")
"Veronica Layman"

JSL Functions, Operators, and Messages
Character Functions

45

Trim(string,<"Left"|"Right"|"Both">)
Trim Whitespace(string,<"Left"|"Right"|"Both">)
Description

Removes leading and trailing whitespace from the specified string.
Returns

A quoted string.
Required Argument

string A quoted string.
Optional Argument
"Left"|"Right"|"Both" A quoted string that specifies whether whitespace is removed

from the left, the right, or both ends of the string. If omitted, whitespace is removed
from both ends.
Example

For example, the following command returns "John":
Trim( " John
"John"

", Both )

Uppercase(string)
Description

Converts any lowercase character found in the quoted string to the equivalent uppercase
character.
Word(n|[first last], string, <delimiter>, <Unmatched(result string)>)
Description

Returns the nth item of the string, where words are substrings separated by any number of
any characters in the delimiter argument.
Required Arguments

n The position of the word being extracted.
[first last] A matrix that defines the beginning and end word range to return.
string The quoted string that is evaluated.
Optional Arguments

delimiter The character used as a boundary. If delimiter is absent, an ASCII space is
used. If delimiter is the empty quoted string, each character is treated as a separate
word.
Unmatched(result string) The quoted string to print if no match is found.
Examples

This example returns the last name:

Character Functions

Word( 2, "Katie Layman" );
"Layman"

See Also

See “Item(n|[first last], string, <delimiter>, <Unmatched(result string)>,
<Include Boundary Delimiters(Boolean)>)” for examples of how Word() differs from
Item().
Words
See “Words(string, <delimiter>)”.
XPath Query(xml, xpath_expression)
Description

Runs an XPath expression on an XML document.
Returns

A list.
Required Arguments

xml A valid XML document.
xpath_expression A quoted XPath 1.0 expression.
Example

Suppose that you created a report of test results in JMP and exported important details to
an XML document. The test results are enclosed in <result> tags.
The following example stores the XML document in a variable. The XPath Query
expression parses the XML to find the text nodes inside the <result> tags. The results are
returned in a list.
rpt =
"\[<?xml version="1.0" encoding="utf-8"?>
<JMP><report><title>Production Report</title>
<result>November 21st: Pass</result>
<result>November 22nd: Fail</result>
<note>Tests ran at 3:00 a.m.</note></report>
</JMP> ]\";
results = XPath Query( rpt, "//result/text()" );
{"November 21st: Pass", "November 22nd: Fail"}
