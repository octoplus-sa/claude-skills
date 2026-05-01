# Programming Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 254-271).

## Index (line numbers in this file)

- `As Boolean()` — L97
- `As C Expr()` — L108
- `As Column()` — L115
- `As Constant()` — L137
- `As Global()` — L152
- `As JSON Expr()` — L168
- `As JavaScript Expr()` — L161
- `As List()` — L178
- `As Name()` — L180
- `As Namespace()` — L187
- `As Python Expr()` — L197
- `As SAS Expr()` — L204
- `As Scoped()` — L220
- `Associative Array()` — L232
- `Class Exists()` — L245
- `Clear Globals()` — L257
- `Clear Log()` — L273
- `Clear Symbols()` — L277
- `Close Log()` — L290
- `Define Class()` — L294
- `Delete Classes()` — L311
- `Delete Globals()` — L321
- `Delete Namespaces()` — L332
- `Delete Symbols()` — L354
- `Delete()` — L334
- `Eval Insert Into()` — L390
- `Eval Insert()` — L377
- `Eval()` — L367
- `Exit()` — L410
- `First()` — L422
- `Force()` — L316
- `Function()` — L432
- `Get Class Names()` — L460
- `Get Classes()` — L471
- `Get Environment Variable()` — L482
- `Get Locale Setting()` — L496
- `Get Log()` — L504
- `Get Namespace Names()` — L517
- `Get Namespaces()` — L539
- `Globals()` — L886
- `Include File List()` — L580
- `Include()` — L561
- `Is Class()` — L584
- `Is Log Open()` — L600
- `Local Here()` — L612
- `Local()` — L608
- `Lock Globals()` — L633
- `Lock Namespaces()` — L619
- `Lock Symbols()` — L640
- `Log Capture()` — L646
- `Method()` — L660
- `NameExpr()` — L209
- `Names Default To Here()` — L672
- `Namespace Exists()` — L690
- `Namespace()` — L683
- `New Namespace()` — L694
- `New Object()` — L711
- `Open Log()` — L706
- `Parameter()` — L752
- `Parse()` — L756
- `Print()` — L760
- `Quit()` — L411
- `Recurse()` — L772
- `Return()` — L456
- `Save Log()` — L776
- `Send()` — L780
- `Set Environment Variable()` — L785
- `Show Classes()` — L795
- `Show Globals()` — L822
- `Show Namespaces()` — L830
- `Show Symbols()` — L835
- `Show()` — L105
- `Throw()` — L846
- `Try()` — L629
- `Type()` — L875
- `Unlock Globals()` — L882
- `Unlock Symbols()` — L881
- `Use Locale()` — L388
- `Wait()` — L887
---

Programming Functions

Arguments
p The probability of the quantile desired. p must be between 0 and 1.
shape Shape parameter , which must be greater than 0.
scale Optional scale parameter , which must be greater than 0. The default is 1.
threshold Optional threshold parameter . The default is 0.

Programming Functions
As Boolean(x)
Description

Evaluates a JSL expression and returns a JSL Boolean value for use with JSON data.
Example

x = 45;
b = As Boolean( x > 2 );
Show( b );
b = true;

As C Expr(x)
Description

Returns a C programming language representation of the expression.
Returns

A quoted string.
As Column(name)
As Column(dt, name)
:name
dt:name
Description

This scoping operator forces name to be evaluated as a data table column in the current
data table (or the table given by the optional data table reference argument, dt) rather than
as a global variable.
Arguments
name Variable name.
dt The data table reference

JSL Functions, Operators, and Messages
Programming Functions

255

Notes
:name refers to a column name in the current data table. You can also specify which data
table to refer to by use dt:name.

As Constant(expr)
Description

Evaluates an expression once to create a value that does not change after it is computed.
Returns

The result of the evaluation.
Argument
expr Any JSL expression.
Notes

A few platforms that can save prediction columns to a data table use As Constant(). The
function is wrapped around the part of the formula that is constant across all rows. The
argument is evaluated for the first row and then the result is used without re-evaluation
for subsequent rows.
As Global(name)
::name
Description

This scoping operator forces name to be evaluated as a global variable rather than as a data
table column.
Arguments
name Variable name.

As JavaScript Expr(x)
Description

Returns a JavaScript representation of the expression.
Returns

A quoted string.
As JSON Expr(x)
Description

Returns a JSON (JavaScript Object Notation) representation of the expression.
Returns

A quoted string.

Programming Functions

As List(matrix)
See “As List(matrix)”.
As Name(string)
Description

Evaluates argument as a quoted string and changes it into a name.
Returns

A name.
As Namespace(name)
Description

Accesses the specified namespace. An error is thrown if no such namespace exists.
Returns

The namespace.
Arguments
name Unquoted name of a defined namespace.

As Python Expr(x)
Description

Returns a Python representation of the expression.
Returns

A quoted string.
As SAS Expr(x)
Description

Converts an expression to a version that is more suitable for SAS DATA step. The code
must be wrapped in a PROC DS2 call. Use Expr(...) for literal expressions. Use
NameExpr(name) for expressions stored in a variable. Otherwise, the expression returns
the expression to convert.
Returns

A quoted string.

JSL Functions, Operators, and Messages
Programming Functions

257

As Scoped(namespace, variable)
namespace:variable
Description

Accesses the specified variable within the specified namespace.
Returns

The value of the variable, or an error the scoped variable is not found.
Arguments
namespace The name of a defined namespace.
variable A variable defined within namespace.

Associative Array({key, value}, ...)
Associative Array(keys, values)
Description

Creates an associative array (also known as a dictionary or hash map).
Returns

An associative array object.
Arguments

Either list of key-value pairs; or a list, matrix, or data table column that contains keys
followed by a list, matrix, or data table column, respectively, that contains the
corresponding values.
Class Exists(class)
Description

Returns a value indicating whether a class definition represented by the class reference is a
defined class.
Returns

0 or 1.
Argument
class A quoted string representation of the name of a defined class or reference to an

instantiated class object.
Clear Globals(<name>, <name>, ...)
Description

Clears the values for all global symbols. Symbols in any scope other than global are not
affected. If one or more names are specified, only those global symbols are cleared.

Programming Functions

Returns

Null.
Optional Arguments
name Any global variable name(s).
See Also

“Clear Symbols(<name>, <name>, ...)”
Clear Log()
Description

Empties the log.
Clear Symbols(<name>, <name>, ...)
Description

Clear the values for all symbols in any and all scopes. If one or more names are specified,
only those symbols are cleared.
Returns

Null.
Optional Arguments
name Any global variable name(s).
See Also

“Clear Globals(<name>, <name>, ...)”
Close Log()
Description

Closes the log.
Define Class("class name", <Base Class( "base class name", <"base class
name", ...> ),> <Show( All(Boolean) ) | Show( <Members(Boolean),>
<Methods(Boolean),> <Functions(Boolean)> ),> <Assignment Statements>)
Description

Defines a new class object.
Example
Define Class(
"aa",
_init_ = Method( {} ); x = 1; m1 = Method( {a, b}, a * b )
);

JSL Functions, Operators, and Messages
Programming Functions

259

Delete Classes(<Force(Boolean)>, < <class>, ...>)
Description

Deletes all currently defined classes.
Optional Arguments
Force(Boolean) Deletes the class or classes even if they are in use.
class Specifies the classes to delete. You can specify more than one class. This argument

can be a quoted string representation of the name of a defined class or a reference to an
instantiated class object.
Delete Globals(<name>, <name>, ...)
Description

Deletes all global symbols, except global symbols that are locked. Symbols in any scope
other than global are not affected. If one or more names are specified, only those global
symbols are cleared.
Optional Arguments
name Any global variable name(s).
See Also

“Delete Symbols(<name>, <name>, ...)”
Delete Namespaces(<Force(Boolean expression)>, < <namespace reference>,
...>)
Delete(<Force(Boolean expression)>, < <namespace reference>, ...>)
Description

Deletes all currently defined namespaces or one or more specific namespaces.
Optional Arguments
Force(Boolean expression) Deletes the namespace even if it’s in use.
namespace reference Specifies the namespaces to delete. You can specify more than

one namespace reference.
Notes

•

When you delete a namespace that contains locked namespaces, an error appears in the
log. Use the Force() argument to delete the locked namespaces.

•

With no arguments, Delete Namespaces() ignores locked namespaces.

Delete Symbols(<name>, <name>, ...)
Description

Deletes all symbols in any and all scopes. If one or more names are specified, only those
symbols are deleted.

Programming Functions

Optional Arguments
name Any global variable name(s).
See Also

“Delete Globals(<name>, <name>, ...)”
Eval(expr)
Description

Evaluates expr, and then evaluates the result of expr (unquoting).
Returns

The result of the evaluation.
Argument
expr Any JSL expression.

Eval Insert(string, <startDel>, <endDel>, < <<Use Locale(1) >)
Description

Allows for multiple substitutions.
Returns

The result.
Arguments
string A quoted string with embedded expressions.
startDel Optional starting delimiter. The default value is ^.
endDel optional ending delimited. The default value is the starting delimiter.
Use Locale(1) Optional argument that preserves locale-specific numeric formatting.

Eval Insert Into(string, <startDel>, <endDel>)
Description

Allows for multiple substitutions in place. The same operation as in Eval Insert is
performed, and the result is placed into the quoted string.
Returns

The result.
Arguments
string A quoted string variable that contains a string with embedded expressions.
startDel Optional starting delimiter. The default value is ^.
endDel optional ending delimited. The default value is the starting delimiter.

JSL Functions, Operators, and Messages
Programming Functions

261

Eval List
See “Eval List({list})”.
Exit(<NoSave>)
Quit(<NoSave>)
Description

Exits JMP.
Returns

Void.
Arguments
NoSave Optional, named command; exits JMP without prompting to save any open files.

This command is not case-sensitive, and spaces are optional.
First(expr, <expr>, ...)
Description

Evaluates all expressions provided as arguments.
Returns

Only the result of the first evaluated expression.
Arguments
expr Any valid JSL expression.

Function({arguments}, <{local variables}>, <Return(<expr>)>, script)
Description

Stores the body script with arguments as local variables.
Returns

The function as defined. If the Return() argument is specified, the expression is returned.
When called later, it returns the result of the script given the specified arguments.
Arguments
{arguments} A list of arguments to pass into the function. You can specify some

arguments as optional or required.
{local variables} A list of variables that are local to the function. You can declare local

variables in three ways:
{var1, var2}
{var1=0, var1="a string"}
{Default Local}

The last option declares that all unscoped variables used in the function are local to the
function.

Programming Functions

Return(expr) This optional argument returns an expression from an user defined

function. If a null expression is used, a period, “.”, is returned.
script Any valid JSL script.
Get Class Names(< <class>, ...>)
Description

Gets a set of names to all classes or the set of specific class references.
Arguments
class A quoted string representation of the name of a defined class or a reference to an

instantiated class object.
Returns

A list of class names as determined by the arguments to the function.
Get Classes(< <class>, ...>)
Description

Gets a set of references to all classes or the set of specific class references.
Arguments
class A quoted string representation of the name of a defined class or a reference to an

instantiated class object.
Returns

A list of class references as determined by the arguments to the function.
Get Environment Variable("variable")
Description

Retrieves the value of an operating system environment variable.
Returns

A quoted string that contains the value of the specified environment variable. If the
specified variable is not found, an empty string is returned.
Arguments
"variable" A quoted string that contains the name of an environment variable.
Notes

On Apple macOS, environment variable names are case-sensitive. On Windows, the
names are case-insensitive.
Get Locale Setting()
Gets a local setting such as a decimal setting.

JSL Functions, Operators, and Messages
Programming Functions

263

Get Log(<n>)
Description

Returns a list of lines from the log.
Returns

A list of quoted strings. Each string contains one line from the log.
Argument
n Optional, integer. If no argument is specified, all the lines are returned. If a positive

number is specified, the first n lines are returned. If a negative number is specified, the
last n lines are returned. If n=0, no lines are returned (an empty list). If the log is empty,
an empty list is returned.
Get Namespace Names(< <namespace reference>,...>)
Description

Returns a list of the names of all currently defined namespaces.
Example
nsaa = New Namespace(
"aa",
{
x = 1
}
);
nsbb = New Namespace(
"bb",
{
y = 1
}
);
lns = Get Namespace Names();
Show( lns );
nsaa << Delete;
nsbb << Delete;

Get Namespaces(< <namespace reference>,...>)
Description

Returns a list of currently defined namespaces.
Example
nsaa = New Namespace(
"aa",
{
x = 1
}

Programming Functions

);
nsbb = New Namespace(
"bb",
{
y = 1
}
);
lns = Get Namespaces();

Include("pathname", <named arguments>)
Description

Opens the script file identified by the quoted string pathname, parses the script in it, and
executes it.
Returns

Whatever the included script returns. If you use the <<Parse Only option, Include
returns the contents of the script.
Named Arguments
<<Parse Only Parses the script but does not execute the script.
<<New Context Causes the included script to be run its own unique namespace. When
the parent and included scripts use the global namespace, include <<Names Default
to Here along with <<New Context.
<<Allow Include File Recursion Lets the included script include itself.
Notes

If a trailing space is included in the path name, the space is ignored on Windows. On
Apple macOS, the script fails.
Include File List()
Description

Returns a list of files that are included at the point of execution.
Is Class(class)
Description

Returns a value that indicates whether the class reference is a class object.
Argument

A class reference to an instantiated class object.
Returns

Returns a zero or a 1.

JSL Functions, Operators, and Messages
Programming Functions

265

Is Log Open()
Description

Returns result if log window is open.
Length
See “Length(string)”.
List
See “List(a, b, c, ...)”.
Local({name=value, ...}, script)
Description

Resolves names to local expressions.
Local Here(expression)
Description

Creates a local Here namespace block. Use this function to prevent name collisions when
multiple scripts are executed from the same root namespace (for example, when a script
executes two button scripts that have the same variables). The argument can be any valid
JSL expression.
Lock Namespaces(<string>,|< {string}, ...>)
Description

Locks all variables or specified named variables in this namespace and prevents variables
from being added, changed, or removed.
Example
ns = New Namespace(
"aaa"
);
ns << Lock Namespaces;
Try( ns << Delete Namespaces, Show( exception_msg ) );
Delete Namespaces();
Try( Delete Namespaces( "aaa" ), Show( exception_msg ) );

Lock Globals(name1, name2, ...)
Description

Locks one or more global variables to prevent it or them from being changed.

Programming Functions

Lock Symbols(<name>, <name>, ...)
Description

Locks the specified symbols, which prevents them from being modified or cleared. If no
symbols are provided, all global symbols are locked. If no symbols are provided and the
script has the Names Default To Here mode turned on, then all local symbols are locked.
Log Capture(expr)
Description

Evaluates the expr, captures the output that would normally be sent to the log, and instead
returns it.
Returns

A quoted string that contains the log output.
Argument

Any valid JSL expression.
Notes

No output appears in the log.
Method({arg1 = val1, ...}, script)
Description

Creates a method within a class. Note that methods use local scoping for all variables that
are not explicitly scoped, with the exception of class member variables.
Arguments
{ arg1 = val1, … } The set of expected arguments and optional initialization
expressions to be passed to the method when called.
script Any valid JSL script.

N Items
See “N Items(source)”.
Names Default To Here(Boolean)
Description

Determines where unresolved names are stored, either as a global or local (if Boolean is 0)
or in the Here scope (if Boolean is 1).

JSL Functions, Operators, and Messages
Programming Functions

267

Namespace(name)
Description

Returns a reference to the named namespace (name).
Argument
Name A namespace name quoted string or a reference to a namespace.

Namespace Exists(name)
Description

Returns 1 if a namespace with the specified name exists; otherwise, returns 0.
New Namespace(<"name">, <{expr, ...}>)
Description

Creates a new namespace with the specified name. If a name is not provided, an
anonymous name is provided.
Returns

A reference to the namespace.
Arguments
name An optional, quoted string that contains the name of the new namespace.
{list of expressions} An optional list of expressions within the namespace.

Open Log(<Boolean>)
Description

Opens the log. Include the Boolean argument to make the window active, even if it is
already open.
New Object("class name"(constructor arguments))
New Object(class name(constructor arguments))
New Object(class reference(constructor arguments))
Description

Creates an instance object of a class.
Arguments
"class name" Name of the class to be instantiated.
class name Unquoted name of the class to be instantiated.
class reference Reference to an existing class object that will be used to instantiate a

new object of the same class.
constructor arguments Set of arguments to be passed to the _init_ constructor.

Programming Functions

Example
Define Class(
"complex",
real = 0; imag = 0;
_init_ = Method( {a, b}, real = a; imag = b; );
Add = Method( {y}, complex( real + y:real, imag + y:imag ) );
Sub = Method( {y}, complex( real - y:real, imag - y:imag ) );
Mul = Method( {y},
complex( real * y:real - imag * y:imag, imag * y:real + real * y:imag )
);
Div = Method( {y},
t = complex( 0, 0 );
mag2 = y:Magsq();
t:real = real * y:real + imag * y:imag;
t:imag = imag * y:real + real * y:imag;
t:real = t:real / mag2;
t:imag = t:imag / mag2;
t;
);
Magsq = Method( {}, real * real + imag * imag );
Mag = Method( {}, Sqrt( real * real + imag * imag ) );
To String = Method( {}, Char( real ) || " + " || Char( imag ) || "i" )
);
cl = New Object( complex( 1, 2 ) );

Parameter({name=value, ...}, model expression)
Description

Defines formula parameters for models for the Nonlinear platform.
Parse(string)
Description

Converts a quoted character string into a JSL expression.
Print(expr, expr, ...)
Description

Prints the values of the specified expressions to the log.
Quit()
See “Exit(<NoSave>)”.

JSL Functions, Operators, and Messages
Programming Functions

269

Recurse(function)
Description

Makes a recursive call of the defining function.
Save Log(pathname)
Description

Writes the contents of the log to the specified file location.
Send(obj, message)
obj << message
Description

Sends a message to a platform object.
Set Environment Variable( "variable", <"value">)
Description

Sets the environment variable to the value specified. If the “value” argument is missing or
is an empty quoted string, then the environment variable is deleted from the JMP process
environment variable table.
Show(expr, expr, ...)
Description

Prints the name and value of each expression to the log.
Show Classes(< <class>,...>)
Description

Shows the contents of user-defined classes in the log. You can specify more than one class.
If you do not specify an argument, all user-defined classes are shown in the log.
Example
Define Class(
"aa",
_init_ = Method( {} ); x = 1; m1 = Method( {a, b}, a * b )
);
Define Class(
"bb",
_init_ = Method( {} ); y = 1; m2 = Method( {a, b}, a / b )
);
Show Classes();
// Class aa

Programming Functions

_init_ = Method( {} );
m1 = Method( {a, b}, a * b );
x = 1;
// Class bb
_init_ = Method( {} );
m2 = Method( {a, b}, a / b );
y = 1;

Show Globals()
Description

Shows the values for all global symbols. Symbols in any scope other than global are not
shown.
See Also

“Show Symbols()”
Show Namespaces(< <namespace reference>,...>)
Description

Shows the contents of all user-defined namespaces, both named and anonymous. You can
specify zero or more namespaces.
Show Symbols()
Description

Shows the values for all symbols in any and all scopes.
See Also

“Show Globals()”
Sort List
See “Sort List({list}|expr)”.
Sort List Into
See “Sort List Into({list}|expr)”.
Throw("text")
Description

Returns a Throw. If you include text, throwing stores text in a global exception_msg. If
text begins with “!” and is inside a Try() expression, throwing creates an error message

JSL Functions, Operators, and Messages
Programming Functions

271

about where the exception was caught. “!” stops the script even if the Throw() is caught by
the second argument of Try().
Try(expr1, expr2)
Description

Evaluates expr1. If the evaluation returns a Throw, execution stops, and nothing is
returned. expr2 is evaluated next to return the result.
Examples
Try( Sqrt( "s" ), "invalid" );
"invalid"
Try( Sqrt( "s" ), exception_msg );
{"Cannot convert argument to a number [or matrix]"(1, 2, "Sqrt",
Sqrt/*###*/("s"))}

Notes
Expr2 can be a quoted character string or the global exception message (exception_msg)
that contains more information about the error returned.

Type(x)
Description

Returns a quoted string that names the type of object x is. The list of possible types is:
Unknown, List, DisplayBox, Picture, Column, TableVar, Table, Empty, Pattern, Date,
Integer, Number, String, Name, Matrix, RowState, Expression, Associative Array, BLOB.
Unlock Symbols(name1, name2, ...)
Unlock Globals(name1, name2, ...)
Description

Unlocks the specified symbols that were locked with a Lock Symbols() or Lock
Globals() command.
Wait(n)
Description

Pauses n seconds before continuing the script. The default setting is 3 seconds. Specifying
Wait(0) enables one cycle of message processing. For example, you can use this function
to allow a button press in the UI. The shortest duration that actually allows JMP to pause is
n = 0.01. The longest duration you can specify without prompting a JMP dialog is
n = 60*60*4.
