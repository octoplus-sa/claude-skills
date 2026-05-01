# Namespace Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 478-479).

## Index (line numbers in this file)

- `<< Contains` — L57
- `<< Delete Namespace` — L60
- `<< First` — L63
- `<< Get Contents` — L71
- `<< Get Keys` — L75
- `<< Get Name` — L77
- `<< Get Value` — L79
- `<< Get Values` — L82
- `<< Insert` — L88
- `<< Lock Namespace` — L91
- `<< N Items` — L94
- `<< Submit` — L30
- `<< Submit File` — L44
- `Echo()` — L42
- `Expand()` — L41
- `Markers()` — L27
---

Namespace Messages

Markers(Boolean) Send row markers. Adds additional data column named

“RowStateMarker”.
mlconn<<Submit(mCode, <named arguments>)
Description

Submits MATLAB code to the active global MATLAB integration interface connection.
Returns

0 if successful, otherwise nonzero.
Required Argument

mCode Positional quoted string. The MATLAB code to submit.
Named Arguments
Expand(Boolean) Perform an Eval Insert on the MATLAB code prior to submission.
Echo(Boolean) Echo MATLAB source lines to the JMP log. The default is true.

mlconn<<Submit File(path)
Description

Submits statements to MATLAB using a quoted path.
Returns

0 if successful, otherwise nonzero.
Arguments

path Positional quoted string. The path to a file containing the MATLAB source lines to
be executed.

Namespace Messages
ns<<Contains(string)
Returns 1 or 0, depending on whether the specified quoted string exists within the
namespace.
ns<<Delete Namespace
Removes this namespace from the internal global list.
To delete variables in the namespace, use the Remove(variable name) message.
ns<<First
Returns a quoted string that contains the first variable name used within the namespace.

JSL Messages
Namespace Messages

479

ns<<Get Contents
Returns a list of key-value pairs, which are each enclosed in a list. Each key is a quoted
string that contains a variable name, and each value is the unevaluated expression that the
variable contains.
ns<<Get Keys
Returns a list of variable names.
ns<<Get Name
Returns the name of this namespace.
ns<<Get Value(variable name);
Returns the unevaluated expression that the quoted variable name contains in this
namespace.
ns<<Get Values
Returns a list of unevaluated expressions that each variable in the namespace contains.
ns<<Get Values({variable name1, variable name2, ... });
Returns a list of unevaluated expressions that each quoted variable in the namespace
specified in the list argument contains. If a requested variable name is not found, an error
is returned.
ns<<Insert(variable name, expr);
Inserts into this namespace a quoted variable named variable name that holds the
expression expr.
ns<<Lock Namespace(<variable name, ...>)
Locks all specified variables in the namespace and prevents quotes variables from being
added or removed. If no variables are specified, all variables in the namespace are locked.
ns<<N Items
Returns the number of variables contained in the namespace.
