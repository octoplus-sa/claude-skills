# MATLAB Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 475-477).

## Index (line numbers in this file)

- `<< Control` — L47
- `<< Disconnect` — L56
- `<< Execute` — L60
- `<< Get` — L97
- `<< Get Graphics` — L82
- `<< Get User Data` — L37
- `<< Get Version` — L92
- `<< Is Connected` — L107
- `<< JMP Name To MATLAB Name` — L114
- `<< Send` — L131
- `<< Set User Data` — L38
- `Colored()` — L148
- `Colors()` — L164
- `Connect()` — L46
- `Echo()` — L53
- `Excluded()` — L144
- `Expand()` — L79
- `Hidden()` — L147
- `Labeled()` — L146
- `Markered()` — L149
- `Row States()` — L151
- `Selected()` — L143
- `Visible()` — L54
---

JSL Messages
MATLAB Messages

475

inst<<Get User Data
inst<<Set User Data
Stores and retrieves a JSL value in the JMP application module instance. The value could
be a number, quoted string, list, associative array, or other JSL type that is returned with
the Type() function.

MATLAB Messages
MATLAB support has been removed from JMP 19.0.
The MATLAB interfaces are scriptable using a MATLAB connection object. Use the MATLAB
Connect() JSL function to obtain a scriptable MATLAB connection object.
mlconn<<Control(<Echo(Boolean)>, <Visible(Boolean)>)
Controls the execution of MATLAB.
Returns

None.
Optional Global Arguments
Echo(Boolean) Echo MATLAB source lines to the JMP Log window.
Visible(Boolean) Determine whether to show or hide the active MATLAB workspace.

mlconn<<Disconnect()
Description

Disconnects this MATLAB integration interface connection.
mlconn<<Execute({list of inputs}, {list of outputs}, mCode,
<Expand(Boolean)>, <Echo(Boolean)>)
Submits MATLAB code to the active global MATLAB integration interface connection
given a list of inputs and upon completion a list of outputs are retrieved.
Returns

0 if successful, otherwise nonzero.
Required Arguments
{list of inputs} Positional, name list. List of JMP variable names to be sent to

MATLAB as inputs.
{list of outputs} Positional, name list. List of JMP variable names to be retrieved

from MATLAB as outputs.
mCode Positional, quoted string. The MATLAB code to submit.

MATLAB Messages

Optional Named Arguments
Expand(Boolean) Performs an Eval Insert on the MATLAB code prior to submission.
Echo(Boolean) Echos MATLAB source lines to the JMP Log window. Default is true.

mlconn<<Get Graphics(format)
Gets the last graphic object written to the MATLAB graph display window. The graphic
object can be returned in several graphic formats.
Returns

JMP Picture object.
Optional Argument
format Positional. The quoted format the MATLAB graph display window contents are
to be converted to. Valid formats are "png", "bmp", "jpeg", "jpg", "tiff", and "tif".

mlconn<<Get Version()
Gets the current version of the installed MATLAB.
Returns

Matrix, returns a vector of length 3 containing the MATLAB version number.
mlconn<<Get(name)
Description

Gets a named variable from MATLAB to JMP.
Returns

Value of named variable.
Required Argument

name The name of a JMP variable to be retrieved from MATLAB.
mlconn<<Is Connected()
Description

Determines whether connection is active.
Returns

1 if connected, otherwise 0.
mlconn<<JMP Name To MATLAB Name(jmp name)
Description

Maps a JMP variable name to its corresponding MATLAB variable name using MATLAB
variable name naming rules.

JSL Messages
MATLAB Messages

477

Returns

A quoted string, a mapped MATLAB name.
Required Argument
jmp name Positional. The name of a JMP variable to be sent to MATLAB.

mlconn<<Send(name, <named arguments>)
Description

Sends the named variable from JMP to MATLAB.
Returns

0 if successful, otherwise nonzero.
Required Argument
name Positional. The name of a JMP variable to be sent to MATLAB.
Named Arguments

The following arguments are for data tables only:
Selected(Boolean) Send selected rows from the referenced data table to MATLAB.
Excluded(Boolean) Send only excluded rows from the referenced data table to
MATLAB.
Labeled(Boolean) Send only labeled rows from the referenced data table to MATLAB.
Hidden(Boolean) Send only hidden rows from the referenced data table to MATLAB.
Colored(Boolean) Send only colored rows from the referenced data table to MATLAB.
Markered(Boolean) Send only markered rows from the referenced data table to
MATLAB.
Row States (Boolean, <named arguments>) Send row states from referenced data
table to MATLAB by adding an additional data column named “RowState”. Create
multiple selections by adding together individual settings. The row state consists of
individual settings with the following values:
– Selected = 1
– Excluded = 2
– Labeled = 4
– Hidden = 8
– Colored = 16
– Markered = 32
Row State Optional Named Arguments

The following optional, named Row States arguments are supported:
Colors(Boolean) Send row colors. Adds additional data column named
“RowStateColor”.
