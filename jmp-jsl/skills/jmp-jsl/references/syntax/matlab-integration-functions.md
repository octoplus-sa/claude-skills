# MATLAB Integration Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 182-188).

## Index (line numbers in this file)

- `Colored()` — L253
- `Colors()` — L267
- `Echo()` — L59
- `Excluded()` — L249
- `Expand()` — L100
- `Get()` — L47
- `Hidden()` — L252
- `Labeled()` — L251
- `MATLAB Connect()` — L50
- `MATLAB Control()` — L61
- `MATLAB Execute()` — L83
- `MATLAB Get Graphics()` — L183
- `MATLAB Get()` — L113
- `MATLAB Init()` — L107
- `MATLAB Is Connected()` — L215
- `MATLAB JMP Name To MATLAB Name()` — L222
- `MATLAB Send File()` — L327
- `MATLAB Send()` — L233
- `MATLAB Submit File()` — L337
- `MATLAB Submit()` — L320
- `MATLAB Term()` — L325
- `Markered()` — L254
- `Markers()` — L270
- `Numeric()` — L149
- `Row States()` — L256
- `Selected()` — L248
- `Send()` — L283
- `Show()` — L111
- `Visible()` — L74
---

MATLAB Integration Functions

MATLAB Integration Functions
MATLAB support has been removed from JMP 19.0.
JMP provides the following interfaces to access MATLAB. The basic execution model is to first
initialize the MATLAB connection, perform the required MATLAB operations, and then
terminate the MATLAB connection. In most cases, these functions return 0 if the MATLAB
operation was successful or an error code if it was not. If the MATLAB operation is not
successful, a message is written to the Log window. The single exception to this is MATLAB
Get( ), which returns a value.

MATLAB JSL Function Interfaces
MATLAB Connect( <named arguments> )
Description

Initializes the MATLAB integration interfaces and returns an active MATLAB integration
interface connection as a scriptable object.
Returns

MATLAB scriptable object.
Named Arguments
Echo(Boolean) Sends the MATLAB source lines to the JMP log. The default value is true.

MATLAB Control( <named arguments> )
Description

Sends control operations to signal MATLAB with external events such as source line
echoing.
Returns

None.
Arguments

None.
Named Arguments
Echo(Boolean) Global. Echo MATLAB source lines to the JMP log.
Visible(Boolean) Global. Determine whether to show or hide the active MATLAB

workspace.

JSL Functions, Operators, and Messages
MATLAB Integration Functions

183

MATLAB Execute( { list of inputs }, { list of outputs }, mCode, <named
arguments> )
Description

Submits the MATLAB code to the active global MATLAB connection given a list of inputs.
Upon completion, retrieves a list of outputs.
Returns

0 if successful, otherwise nonzero.
Arguments
{ list of inputs } Positional, name list. List of JMP variable names to send to

MATLAB as inputs.
{ list of outputs } Positional, name list. List of JMP variable names to retrieve from
MATLAB as outputs.
mCode Positional, quoted string. The MATLAB code to submit.
Named Arguments
Expand(Boolean) Perform an Eval Insert on the MATLAB code prior to submission.
Echo(Boolean) Echo MATLAB source lines to the JMP log. Default is true.
Example

The following example sends the JMP variables x and y to MATLAB, executes the
MATLAB statement z = x * y, and then gets the MATLAB variable z and returns it to
JMP.
MATLAB Init();
x = [1 2 3];
y = [4 5 6];
MATLAB Execute( {x, y}, {z}, "z = x * y;" );
Show( z );

MATLAB Get( name )
Description

Gets named variable from MATLAB to JMP.
Returns

Value of named variable.
Arguments
name Positional. The name of a JMP variable to be sent to MATLAB.
Example

Suppose that a matrix named qbx and a structure named df are present in your MATLAB
connection.
// get the MATLAB variable qbx and placed it into a JMP variable qbx
qbx = MATLAB Get( qbx );

MATLAB Integration Functions

/* get the MATLAB variable df and placed it into a JMP data table
referenced by df */
df = MATLAB Get( df );

Table 2.1 shows what JMP data types can be exchanged with MATLAB using the MATLAB Get(
) function. Getting lists from MATLAB recursively examines each element of the list and
sends each base MATLAB data type. Nested lists are supported.
Table 2.1 JMP and MATLAB Equivalent Data Types for MATLAB Get( )
MATLAB Data Type

JMP Data Type

Double

Numeric

Logical

Numeric ( 0 | 1 )

String

String

Integer

Numeric

Date/Time

Numeric

Structure

Data Table

Matrix

Numeric Matrix

Numeric Vector

Numeric Matrix

String Vector

List of Strings

Graph

Picture object

MATLAB Get Graphics( format )
Description

Get the last graphic object written to the MATLAB graph display window in a specific
graphic format. The graphic object can be returned in several graphic formats.
Returns

JMP Picture object.
Argument
format Positional. The format the MATLAB graph display window contents are to be
converted to. Valid formats are png, bmp, jpeg, jpg, tiff, tif, and gif.

JSL Functions, Operators, and Messages
MATLAB Integration Functions

185

MATLAB Get Version
Description

Returns the version number of MATLAB being used with the JMP MATLAB interfaces.
MATLAB Init( <named arguments> )
Description

Initializes the MATLAB integration interfaces.
Returns

Return code.
Named Arguments
Echo(Boolean) Sends MATLAB source lines to the JMP log. This option is global. The
default value is true.

MATLAB Is Connected()
Description

Determines whether a MATLAB connection is active.
Returns

1 if connected, otherwise 0.
MATLAB JMP Name To MATLAB Name( name )
Description

Maps a JMP variable name to its corresponding MATLAB variable name using MATLAB
variable name naming rules.
Returns

A quoted string, mapped MATLAB variable name.
Argument
name Positional. The name of a JMP variable to be sent to MATLAB.

MATLAB Send( name, <named arguments> )
Description

Sends the named variable from JMP to MATLAB.
Returns

0 if successful, otherwise nonzero.
Arguments
name Positional. The name of a JMP variable to be sent to MATLAB.

MATLAB Integration Functions

Named Arguments

The following optional arguments apply to data tables only:
Selected(Boolean) Send selected rows from the referenced data table to MATLAB.
Excluded(Boolean) Send only excluded rows from the referenced data table to
MATLAB.
Labeled(Boolean) Send only labeled rows from the referenced data table to MATLAB.
Hidden(Boolean) Send only hidden rows from the referenced data table to MATLAB.
Colored(Boolean) Send only colored rows from the referenced data table to MATLAB.
Markered(Boolean) Send only markered rows from the referenced data table to
MATLAB.
Row States(Boolean, <named arguments>) Send row states from referenced data
table to MATLAB by adding an additional data column named “RowState”. Create
multiple selections by adding together individual settings. The row state consists of
individual settings with the following values:
– Selected = 1
– Excluded = 2
– Labeled = 4
– Hidden = 8
– Colored = 16
– Markered = 32
The following optional, named Row States arguments are supported:
Colors(Boolean) Send row colors. Adds additional data column named

“RowStateColor”.
Markers(Boolean) Send row markers. Adds additional data column named

“RowStateMarker”.
Example
// create a matrix, assign it to X, and send the matrix to MATLAB
X = [1 2 3];
ml = MATLAB Send( X );
/* open a data table, assign a reference to it to dt, and send the
data table along with its current row states to MATLAB */
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
ml = MATLAB Send( dt, Row States( 1 ) );

Table 2.2 shows what JMP data types can be exchanged with MATLAB using the MATLAB
Send( ) function. Sending lists to MATLAB recursively examines each element of the list and
sends each base JMP data type. Nested lists are supported.

JSL Functions, Operators, and Messages
MATLAB Integration Functions

187

Table 2.2 JMP and MATLAB Equivalent Data Types for MATLAB Send( )
MATLAB Data Type

JMP Data Type

Double

Numeric

String

String

Double Matrix

Matrix

Structure

Data Table

Example
MATLAB Init( );
X = 1;
MATLAB Send( X );
S = "Report Title";
MATLAB Send( S );
M = [1 2 3, 4 5 6, 7 8 9];
MATLAB Send( M );
MATLAB Submit( "
X
S
M
" );
MATLAB Term( );

MATLAB Send File(filename, <MATLAB Name(name)>)
Description

Sends a data file to MATLAB.
Arguments
filename Specifies a quoted string that identifies the pathname to the file to be sent to

MATLAB.
MATLAB Name Enables you to change the name of the file sent to MATLAB.

MATLAB Submit File( pathname, <named arguments> )
Description

Submits statements to MATLAB using a file pointed to by pathname.
Returns

0 if successful, otherwise nonzero.

MATLAB Integration Functions

Arguments
Pathname Positional, quoted string. Pathname to file containing MATLAB source lines to

be executed.
Named Arguments
Expand(Boolean) Perform an Eval Insert on the MATLAB code prior to submission.
Echo(Boolean) Echo MATLAB source lines to the JMP log. Default is true.

MATLAB Submit( mCode, <named arguments> )
Description

Submits the MATLAB code to the active global MATLAB connection.
Returns

0 if successful, otherwise nonzero.
Arguments
mCode Positional, quoted string. The MATLAB code to submit.
Named Arguments
Expand(Boolean) Perform an Eval Insert on the MATLAB code prior to submission.
Echo(Boolean) Echo MATLAB source lines to the JMP log. Default is true.
Example

The following example creates two vectors of random points and plots them as x and y
variables.
MATLAB Init();
mc = MATLAB Submit("/[
x = rand(5);
fprintf('%f/n', x);
y = rand(5);
fprintf('%f/n', x);
z = plot(x, y);
]/" );

MATLAB Term();
Description

Terminates the currently active MATLAB integration interface.
Returns

1 if an active MATLAB connection exists, otherwise returns 0.
Arguments

None.
