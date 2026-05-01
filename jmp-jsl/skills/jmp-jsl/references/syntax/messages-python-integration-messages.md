# Python Integration Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 485-489).

## Index (line numbers in this file)

- `<< Control` — L58
- `<< Create JPIP CMD` — L60
- `<< Disconnect` — L71
- `<< Execute` — L76
- `<< Get` — L92
- `<< Get Graphics` — L104
- `<< Get Version` — L139
- `<< Install Packages` — L147
- `<< Is Connected` — L161
- `<< JMP Name to Python Name` — L171
- `<< Send` — L182
- `<< Send File` — L194
- `<< Set` — L226
- `<< Submit` — L254
- `<< Sync Time Boundary Type` — L38
- `<< Timeout` — L43
- `<< UTC` — L48
- `Baseball()` — L223
- `Big Class()` — L219
- `Connect()` — L57
- `Names Default To Here()` — L68
- `Python Create JPIP CMD()` — L69
- `Python Submit()` — L136
- `Python()` — L180
---

JSL Messages
Python Integration Messages

485

obj<<Sync Time Boundary Type("inside"|"outside")
Description

Determines how values that occur near the start and end time boundaries are treated. The
default value is ʺinsideʺ.
obj<<Timeout(n)
Description

Cancels the import operation after no data has been received for the given number of
seconds. A negative value directs the operation to wait for the default amount.
obj<<UTC(state=0|1)
Description

(Optional) This flag indicates whether the start time and end time parameters are based on
UTC. The default value is 0 (false).

Python Integration Messages
The Python interfaces are also scriptable using a Python connection object. A scriptable
Python connection object can be obtained using the Python Connect() function. See “Python
Connect()”.
pythconn<<Control
This message is deprecated.
pythconn<<Create JPIP CMD
Description

Triggers the creation of a jpip command line wrapper script for Python’s pip command. A
directory picker dialog will ask for the directory location to save the generated script. This
script then provides the full capabilities of pip, while correctly establishing the necessary
environment variables for JMP’s Python environment.
Example
Names Default To Here( 1 );
Python Create JPIP CMD();

pythconn<<Disconnect
This message is deprecated.

Python Integration Messages

pythconn<<Execute({list of inputs}, {list of outputs}, Python_code)
Description

Submits Python code to the Python environment given a list of inputs. On completion,
returns a list of outputs.
Returns

Returns 0 if successful and 1 otherwise. The results are returned using the list of outputs.
Given each element of the JMP output list, the corresponding Python variable value is
returned.
Positional Arguments

{list of inputs} A list of JMP variable names to be sent to Python as inputs.
{list of outputs} A list of JMP variable names to be retrieved from Python as
outputs.
Python code The quoted Python code to submit.
pythconn<<Get(name)
Description

Gets a named variable from Python.
Returns

Returns the value of the named variable.
Argument
name The name of the JMP variable to be received from Python. The argument can

represent any of the following Python data types: numeric, quoted string, matrix, list,
or data frame.
pythconn<<Get Graphics(format)
Description

This message is deprecated. Previously, the message returned the last graphics object
written by matplotlib’s pyplot in a graphics format specified by the format argument.
Example

The following example shows the previous method commented out and the new
alternative.
Names Default To Here( 1 );
ml = Python Submit(
"\[
# This sample requires the matplotlib package to be installed.
import matplotlib.pyplot as plt
plt.clf()
# make sure we are starting with a clean plot

JSL Messages
Python Integration Messages

487

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.draw()
# Save image to location of your choosing
plt.savefig('/tmp/get_graphics_img.png')
]\"
);
// pyconn << Get Graphics(); // DEPRECATED
plot = Open( "/tmp/get_graphics_img.png", png );
pngJMP = New Window( "Plot", Picture Box( plot ) );
Python Submit( "plt.close()" );
rc = Delete File( "/tmp/get_graphics_img.png" );

pythconn<<Get Version
Description

Gets the current version of the Python installation.
Returns

Returns a list of length 5 that contains the five components of the version number: major,
minor, micro, releaselevel, and serial. The releaselevel value is a quoted string.
pythconn<<Install Packages
Description

This wrappers the install of Python packages into the JMP site-packages directory. For
operations beyond simple package installation, use Python Create JPIP CMD() to create
a command line wrapper script in a directory chosen with Directory Pick().
Alternatively, to run the install from a JMP Python script window, see the JMP Scripting
Guide.
Example
Names Default To Here( 1 );
// Install numpy and pandas packages
conn = Python Connect();
conn << Install Packages( "numpy pandas" );

pythconn<<Is Connected
Description

This message is deprecated.
Returns

Always returns 1.

Python Integration Messages

pythconn<<JMP Name to Python Name(name)
Description

Maps a JMP variable name to its corresponding Python variable name using Python
variable name naming rules.
Argument
name The name of the JMP variable to be sent to Python. Some variable names allowed by

JMP are not allowed by Python. When you send using these variables from JMP to
Python (the Send message), their names get changed. Use JMP Name to Python Name
to determine what the variable name was changed to.
pythconn<<Send(name, <Python Name( name )>)
Description

Sends a named variable from JMP to Python.
Returns

Returns 0 if successful and non-zero otherwise.
Argument
name The name of the JMP variable to be sent to Python.

<Python Name( name )> Specifies the name assigned to the variable in the Python
environment.
pythconn<<Send File(name, <Python Name( name )>)
Description

Sends a JMP data table to Python. pythconn<<Send File() will be deprecated in a future
release. Instead, use pythconn<<Send().
Argument
name The name of the data table to be sent to Python.

<Python Name( name )> Specifies the name assigned to the data table in the Python
environment.
Example
Names Default To Here( 1 );
PythonConnection = Python Connect();
PythonConnection << Send File( "$SAMPLE_DATA/Big Class.jmp" );
dtname = "$SAMPLE_DATA/Baseball.jmp";
PythonConnection << Send File( dtname );
PythonConnection << Submit( "print(Big_Class)" );
PythonConnection << Submit( "print(Baseball)" );
//:*/
print(Big_Class)
/*:

JSL Messages
Python Integration Messages

Big Class (5 columns x 40 rows)
//:*/
print(Baseball)
/*:
Baseball (2 columns x 43 rows)
0

pythconn<<Set(name)
Description

Assigns a variable in the Python environment.
Argument

name A string specifying the name of the object set as a Python variable.
Example
Names Default To Here( 1 );
PythonConnection = Python Connect();
x = [1, 2, 3];
PythonConnection << Set( x );
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
PythonConnection << Set( dt );
PythonConnection << Submit( "print(x)" );
PythonConnection << Submit( "print(dt)" );
//:*/
print(x)
/*:
[[1.]
[2.]
[3.]]
//:*/
print(dt)
/*:
Big Class (5 columns x 40 rows)
0

pythconn<<Submit(Python_code)
Description

Submits Python code to the Python environment.
Returns

Returns 0 if successful and 1 otherwise.
Required Arguments

Python_code The quoted Python code to submit.

489
