# R Integration Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 278-282).

## Index (line numbers in this file)

- `Colored()` — L209
- `Colors()` — L228
- `Echo()` — L62
- `Excluded()` — L203
- `Hidden()` — L207
- `Labeled()` — L205
- `Markered()` — L211
- `Markers()` — L230
- `Names Default To Here()` — L135
- `Python Submit File()` — L41
- `Python Term()` — L48
- `R Connect()` — L52
- `R Control()` — L65
- `R Execute()` — L78
- `R Get Graphics()` — L127
- `R Get Version()` — L146
- `R Get()` — L105
- `R Init()` — L136
- `R Is Connected()` — L161
- `R Name()` — L195
- `R Send File()` — L247
- `R Send()` — L185
- `R Submit()` — L258
- `Row States()` — L213
- `Selected()` — L201
- `Show()` — L37
---

R Integration Functions

Show( getStr, getNum );
getStr = "The quick brown fox jumps over the lazy dog";
getNum = 200;

Python Submit File(path)
Description

Submits statements to Python using the file specified in the path name.
Argument
path The path to the file that contains the Python source lines to be executed.

Python Term()
This function is deprecated.

R Integration Functions
R Connect( <named_arguments> )
Description

Returns the current R connection object. If there is no connection to R, it intializes the R
integration interface and returns an active R integration interface connection as a
scriptable object.
Returns

R scriptable object.
Arguments
Echo(Boolean) (Optional) Sends all source lines to the JMP log. This option is global. The
default value is true.

R Control( Echo(Boolean) )
Description

Changes the control options for R. As of JMP 19, the Interrupt and Async options have no
effect, and are no longer listed as possible arguments.
Argument
Echo(Boolean) Whether to send source lines to the JMP log. Optional.

JSL Functions, Operators, and Messages
R Integration Functions

279

R Execute( { list of inputs }, { list of outputs }, "rCode" )
Description

Submits the specified R code to the active global R connection given a list of inputs. On
completion, the output list is populated.
Returns

0 if successful; nonzero otherwise.
Arguments
{ list of inputs } A list of JMP variables or named columns to be sent to R as inputs.
{ list of outputs } A list of JMP variable names to contain the outputs returned from

R.
rCode A quoted string that contains the R code to submit.
Examples

Send the JMP variables x and y to R, execute the R statement z <- x + y, and then get the R
variable z and return it to JMP.
x = [1 2 3];
y = [4 5 6];
rc = R Execute( {x, y}, {z}, "z <- x + y" );
jz = R Get( z );
jz;

Send multiple named columns
R Execute( { dt:age, dt:height, dt:weight }, {}, “R code here” );

R Get( variable_name )
Description

Gets the named variable from R. The variable can represent any of the following data
types: numeric, string, matrix, list, data frame.
Returns

The value of the named variable.
Argument
variable_name Required. The name of an R variable whose value to return to JMP.
Example

Assume that a matrix named qbx and a data frame named df are present in your R
connection.
// get the R variable qbx and placed it into a JMP variable qbx.
qbx = R Get( qbx );
// get the R variable df and placed it into a JMP data table
// referenced by df.
df = R Get( df );

R Integration Functions

R Get Graphics( "format" )
Description

Deprecated in JMP 19 and has no effect.
Details

As an alternative, set the graphics device to a filename such as png("r_plot.png"), plot
to a file, and then open the file to get the image.
Names Default To Here( 1 );
R Init();
img_path = Get Path Variable( "TEMP" ) || "r_plot.png";
R Execute( {img_path}, {}, "\[
png(img_path)
plot(1:10)
dev.off()
]\" );
plot = Open( img_path );
rc = Delete File( img_path );

R Get Version()
Description

Returns the version number of R being used with the JMP R interfaces.
R Init( named_arguments )
Description

Initializes the R session.
Returns

0 if the initialization is successful; any nonzero value otherwise.
Argument
Echo(Boolean) (Optional) Sends all source lines to the JMP log. This option is global. The
default value is true.

R Is Connected()
Description

Determines whether a connection to R exists.
Returns

1 if connected; 0 otherwise.

JSL Functions, Operators, and Messages
R Integration Functions

281

R JMP Name to R Name( JMP_variable_name )
Description

Maps the specified JMP variable name to the corresponding R variable name using R
naming rules. Requires an active connection to R.
Returns

A quoted string that contains the R name.
Argument

JMP_variable_name The name of a JMP variable to be sent to R.
R Send( name, <R Name( as_name ) | "as_name">)
Description

Sends named variables from JMP to R. The variable can represent any of the following
data types: numeric, string, matrix, list, data table, data table column, data frame.
Returns

0 if the send is successful; any nonzero value otherwise.
Arguments
name Required. The name of a JMP variable to be sent to R.
R Name(as_name) (Optional) A different name for the variable in R.
as_name (Optional) The name assigned to the variable in the R environment. The name is
automatically passed through R Name() to ensure a valid R variable name.
Details

For data tables only:
Selected(Boolean) optional, named, Boolean. Send only selected rows from the
referenced data table to R.
Excluded(Boolean) optional, named, Boolean. Send only excluded rows from the
referenced data table to R.
Labeled(Boolean) optional, named, Boolean. Send only labeled rows from the
referenced data table to R.
Hidden(Boolean) optional, named, Boolean. Send only hidden rows from the referenced
data table to R.
Colored(Boolean) optional, named, Boolean. Send only colored rows from the
referenced data table to R.
Markered(Boolean) optional, named, Boolean. Send only markered rows from the
referenced data table to R.
Row States(Boolean, <named arguments>) optional, named. Includes a Boolean
argument and optional named arguments. Send row state information from the
referenced data table to R by adding an additional data column named “RowState”.

R Integration Functions

Multiple row states are created by adding together individual settings. Here are the
individual values:
– Selected = 1
– Excluded = 2
– Hidden = 4
– Labeled = 8
– Colored = 16
– Markered = 32
Here are the named arguments for the Row States() argument:
Colors(Boolean) optional, named, Boolean. Sends row colors. Adds additional data
column named “RowStateColor”.
Markers(Boolean) optional, named, Boolean. Sends row markers. Adds additional data
column named “RowStateMarker”.
Examples

Assuming variable dt is ‘Big Class.jmp’, create an R Vector named ‘weight’ with the
values from the weight column:
R Send( dt:weight );

Create a matrix, assign it to X, and send the matrix to R:
X = [1 2 3];
rc = R Send( X );

Open a data table, assign a reference to it (dt), and send the data table, along with its
current row states, to R:
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
rc = R Send( dt, Row States(1) );

R Send File( "filename", <R Name("name")>)
Description

Sends the specified file from JMP to R.
Returns

0 if the send is successful; any nonzero value otherwise.
Arguments
filename Required. A quoted string that contains a path for a file.
R Name(name) (Optional) The name assigned to the file in the R environment.

R Submit( "rCode", <named_arguments> )
Description

Submits the specified R code to the active global R connection.
