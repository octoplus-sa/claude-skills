# Scripting Guide Glossary

Source: JMP 19 Scripting Guide (PDF pages 941-945).

## Index (line numbers in this file)

- `Current Data Table()` — L63
---

Appendix D
Scripting Guide Glossary
Terms, Concepts, and Placeholders
|

In syntax summaries, | means “or” and separates possible choices. Usually choices
separated by | are mutually exclusive. In other words, you have to pick one and cannot list
several.

argument

An argument is something specified inside the parentheses of a JSL function,
message, and so forth. Big Class.jmp is the argument in Open("Big Class.jmp").
You can often infer the meaning by the argument’s position. For example, the values 200
and 100 in size(200, 100) are implicit arguments. The first value is always interpreted
as the width; the second value is always interpreted as the height. See also named argument.

Boolean

A Boolean value is a yes/no value, something that is on or off, shown or hidden,
true or false, 1 or 0, yes or no. A value listed as being a Boolean value is one that evaluates to
true or false (or missing).

col

In syntax summaries, a placeholder for any reference to a data table column. For
example, Column("age").

command

A generic description for a JSL statement that performs an action. The Scripting
Guide prefers the more specific terms function and message when they are applicable.
The current data table is the data table that Current Data Table() either
returns or is assigned.

current data table

current row The current row for scripting is defined to be zero (no row) by default. You can
set a current row with Row() or For Each Row, and so forth.
database

Although the term is much more general, for JMP’s purposes, the word “database”
describes any external data source (such as SQL) accessed through ODBC with JSL’s Open
Database command.

Datafeed

A Datafeed is a method to read real-time data continuously, such as from a
laboratory measurement device connected to a serial port.

db In syntax summaries, a placeholder for any reference to a display box. For example,
report(Bivariate[1]).
dt In syntax summaries, a placeholder for any reference to a data table. For example,
Current Data Table() or Data Table("Big Class.jmp").

942

Scripting Guide Glossary

Appendix D

eliding operator An eliding operator is one that causes arguments on either side to combine

and evaluate differently than if the statement were evaluated strictly left to right. For
example, 12<a<13 is a range check to test whether a is between 12 and 13: JMP reads the
whole expression before evaluating. If < did not elide, the expression would be evaluated
left to right as (12<a)<13. In other words, it would check whether the result of the
comparison (1 or 0, for false or true) is below 13, which of course would always yield 1 for
true. The << operator (for object<<message, which is equivalent to Send(object,
message) is another example of an eliding operator.
function

A function takes an argument or series of arguments inside parentheses after the
function name. For example, the infix operator + has a function equivalent Add(). The
statements 3 + 4 and Add(3, 4) are equivalent. All JSL’s operators have function
equivalents, but not all functions have operator equivalents. For example, Sqrt(a) can be
represented only by the function. Also see the Function operator for storing a function
under a name.

global variable

A global variable is a name to hold values that exists for the remainder of a
session. Globals can contain many types of values, including numbers, strings, lists, or
references to objects. They are called globals because they can be referred to almost
anywhere, not just in some specific context.

head

The head of a JSL expression is the expression without any of its arguments. For
example, the head of the expression Assign( x, 100.1 ) is Assign().

infix operator An infix operator takes one argument on each side, such as + in arithmetic,
3 + 4 , or the = in an assignment, a=7.
L-value Something that can be the destination of an assignment. In this manual, L-value

describes an expression that normally returns its current value but that can alternatively
receive an assignment to set its value. For example, you would ordinarily use a function
such as Row() to get the current row number and assign it to something else. For example,
x=Row(). However, since Row is an L-value, you can also place it on the left side of an
assignment to set its value. For example, Row()=10.
list

A list is a multiple-item data type entered in special brace { } notation or with the List
function. Lists enable scripts to work with many things at once, often in the place of a
single thing.

matrix

A matrix is a JMP data type for a rectangular array of rows and columns of number.
In JSL, matrices are entered in bracket [ ] notation or with the Matrix function.

message

A message is a JSL statement that is directed to an object, which knows how to
execute the message.

metadata

In JMP data tables, metadata are data about the data, such as the source of the
data, comments about each variable, scripts for working with the data, and so on.

Appendix D

Scripting Guide Glossary

943

mousedown

An event generated by pressing down the mouse button. See “Handle()” and
“Mousetrap()”.

mouseup

An event generated by releasing the mouse button. See “Handle()” and
“Mousetrap()”.

name

A name is a reference to a JSL object. For example, when you assign the numeric value
3 to a global variable in the statement a=3, “a” is a name.

namespace

A namespace is a collection of unique names and corresponding values.
Namespaces are useful for avoiding name collisions between different scripts.

named argument

A named argument is an optional argument that you select from a
predetermined set and explicitly define. For example, HexToNumber(hextext,
<Base(number)>) has a single named argument, Base. This is the fixed name that must
directly be in the HexToNumber argument.

ODBC database

The Microsoft standard for Open DataBase Connectivity. JSL supports
access to any ODBC-enabled data source through the Open Database command.

obj In syntax summaries, a placeholder for any reference to an analysis platform. For
example, Bivariate[1].
object

An object is a dynamic entity in JMP, such as a data table, a data column, a platform
results window, a graph, and so forth. Most objects can receive messages telling them to
act on themselves in some way.

operator Usually operator refers to a one- or two-character symbol such as + for addition or
<= for less than or equal to.
POSIX

POSIX is an acronym for Portable Operating System Interface and is a registered
trademark of the IEEE. POSIX pathnames enable you to use one syntax for paths for any
operating system, instead of having to use a different syntax for each.

postfix operator A postfix operator takes on argument on its left side (before the operator),
such as a++ for postincrement or a–– for postdecrement.
pre-evaluated statistics

Statistics that are calculated once and used as constants thereafter.

prefix operator A prefix operator takes one argument on its right side (after the operator),
such as !a for negation.
reference A way to address a scriptable object in order to send it messages. For example,.
column("age") or Current Data Table() or Bivariate[1]. Typically a reference is

stored in a global variable for convenience.
row state

A data element type to store any combination of the following attributes for data
rows: excluded, hidden, labeled, selected, color, marker, hue, shade.

944

Scripting Guide Glossary

Appendix D

scalar A simple non-matrix numeric value.
scoping operator

A scoping operator forces a name to be interpreted as a particular type of
data element, for example the : operator in :name forces name to be resolved as a column;
the :: operator in ::name forces name to be resolved as a global variable. In the rare case
that you do want to share specific variables among all opened projects, use the ::: root
operator.

toggle

Omitting the Boolean argument for a row state command toggles the setting. If the
option is off, the message turns it on. If the option is on, the message turns it off. Sending
such a command repeatedly flips back and forth between on and off. If you include the
Boolean argument, the command sets an absolute on or off state, and sending the
command repeatedly has no further effect. For all other messages, omitting the Boolean
argument enables the option.

vector

A matrix with only one column or row.
