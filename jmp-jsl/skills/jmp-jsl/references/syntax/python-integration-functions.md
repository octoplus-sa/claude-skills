# Python Integration Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 272-277).

## Index (line numbers in this file)

- `Names Default To Here()` — L78
- `Python Connect()` — L59
- `Python Create JPIP CMD()` — L70
- `Python Disconnect()` — L81
- `Python Execute()` — L83
- `Python Get Graphics()` — L179
- `Python Get Version()` — L210
- `Python Get()` — L153
- `Python Init()` — L217
- `Python Install Packages()` — L219
- `Python Send File()` — L281
- `Python Send()` — L173
- `Python Submit()` — L207
- `Show()` — L126
- `Watch()` — L34
- `Wild List()` — L48
- `Wild()` — L43
- `Write()` — L53
---

Python Integration Functions

Notes

You can use Wait(n) if you want something to stay on the screen long enough to see it, if
you need a platform to finish launching before scripting it, or if you need to press buttons
in the UI while the script runs.
Watch(all | name1, ...)
Description

Shows variables from global, here, and local namespaces and their values in a window. If
“all” is provided as the argument, all globals are placed into the window.
Notes

– New globals are not added to the window list.
– Watching associative arrays that have been modified using messages is not supported.
Wild()
Description

Only used with Extract Expr() for expression matching to denote a wildcard position
that matches any expression.
Wild List()
Description

Only used with Extract Expr() for expression matching to denote a series of wildcard
arguments that match any expression.
Write("text")
Description

Prints text to the log without surrounding quotation marks.

Python Integration Functions
Python Connect()
Description

Returns an active Python integration interface connection as a scriptable object.
Parameters that were available for Python Connect() in JMP 14-17 are deprecated.

JSL Functions, Operators, and Messages
Python Integration Functions

273

Python Create JPIP CMD()
Description

Triggers the creation of a jpip command line wrapper script for Python’s pip command.
A directory picker dialog will ask for the directory location to save the generated script.
This script then provides the full capabilities of pip, while correctly establishing the
necessary environment variables for JMP’s isolated Python environment.
Example
Names Default To Here( 1 );
Python Create JPIP CMD();

Python Disconnect()
This function is deprecated.
Python Execute({list of inputs}, {list of outputs}, Python_Code)
Description

Submits Python code to the Python environment given a list of inputs. On completion, the
outputs are returned in the output list.
Returns

Returns 0 if successful and 1 otherwise.
Arguments
{list of inputs} A list of JMP variable names to be sent to Python as inputs.
{list of outputs} A list of JMP variable names to be retrieved from Python as outputs.
Python_Code The Python code to submit.
Examples

This example sends a character variable, a numeric variable, and a set of matrices to
Python. Python is then instructed to perform a set of matrix operations on the sent
matrices. The Python Execute() function then gets the set of matrices created by the
matrix operations and gets the values of the character and numeric variables that was
originally sent.
Names Default To Here( 1 );
a = "abcdef";
d = 3.141;
x = 0;
z = 0;
v = [1 0 0, 0 1 0, 0 0 1];
// pi, e, phi, c, Plank's, Faraday, 345 triangle
m = [3.141 2.718 1.618,
2.997 6.626 9.648,
3 4 5];

Python Integration Functions

ml = Python Execute(
{v, m, a, d},
{x, z, a, d},
"\[
import numpy as np
a = np.multiply(v, m) # matrix product
d = np.divide(v, m) # matrix division
z = np.multiply(m, np.linalg.inv(v)) # m * inv(v) called Left division
x = np.multiply(np.linalg.inv(m), v) # inv(m) * v called right division
]\"
);
Show( v, m, ml, x, z, a, d );
v =
[ 1 0 0,
0 1 0,
0 0 1];
m =
[ 3.141 2.718 1.618,
2.997 6.626 9.648,
3 4 5];
ml = 0;
x =
[ -0.681183278459541 0 0,
0 1.3532624962586 0,
0 0 1.57966926070039];
z =
[ 3.141 0 0,
0 6.626 0,
0 0 5];
a =
[ 3.141 0 0,
0 6.626 0,
0 0 5];
d =
[ 0.318369945877109 0 0,
0 0.150920615756112 0,
0 0 0.2];

Python Get(python_var)
Description

Gets a named variable from Python.
Returns

The value of the named variable.
Argument
name The name of the Python variable to be sent to JMP. The argument can represent any

of the following Python data types: numeric, quoted string, matrix, list, or data frame.
Example
Names Default To Here( 1 );

JSL Functions, Operators, and Messages
Python Integration Functions

275

x1 = {1, 2, 3};
Python Send( x1 );
x2 = Python Get( x1 );
Show( x1, x2 );
x1 = {1, 2, 3};
x2 = {1, 2, 3};

Python Get Graphics(format)
Description

This function is deprecated and will generate a syntax error when used. Previously, the
function returned the last graphics object written by matplotlib’s pyplot in a graphics
format specified by the format argument.
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
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.draw()
# Save image to location of your choosing
plt.savefig('/tmp/get_graphics_img.png')
]\"
);
// plot = Python Get Graphics( png );
// DEPRECATED
plot = Open( "/tmp/get_graphics_img.png", png );
pngJMP = New Window( "Plot", Picture Box( plot ) );
Python Submit( "plt.close()" );
rc = Delete File( "/tmp/get_graphics_img.png" );

Python Get Version()
Description

Returns the version number of Python being used with the JMP Python interfaces.

Python Integration Functions

Python Init()
This function is deprecated as of JMP 18. Instead, use “Python Connect()”.
Python Install Packages(packages)
Description

This wrappers the install of Python packages into the JMP site-packages directory. For
operations beyond simple package installation, use Python Create JPIP CMD() to create
a command line wrapper script in a directory chosen with Directory Pick().
Alternatively, to run the install from a JMP Python script window, see the JMP Scripting
Guide.
Example
Names Default To Here( 1 );
// Install numpy and pandas packages
Python Install Packages( "numpy pandas" );

Python Is Connected
This function is deprecated and always returns 1.
Python JMP Name to Python Name(jmp_var)
Description

Maps a JMP variable name to its corresponding Python variable name using Python
variable name naming rules.
Returns

A quoted string, the mapped Python name.
Argument
jmp_var The name of the JMP variable to be sent to Python.

Python Send(jmp_var, <Python Name( name ) | "as_name" >)
Description

Sends a named variable from JMP to Python. Data table columns can be passed as the
variable.
Returns

0 if successful.
Arguments
jmp_var The name of the JMP variable to be sent to Python.

<Python Name( name )> Specifies the name assigned to the variable in the Python
environment.

JSL Functions, Operators, and Messages
Python Integration Functions

277

as_name The name assigned to the variable in the Python environment. The name is
automatically passed through Python Name() to ensure a valid Python variable name.
Examples

Assuming ‘Big Class.jmp’ as variable dt, the following code creates a vector named
‘weight’ that has the values from the data table’s weight column:
Python Send( dt:weight );

This example sends data to Python:
Names Default To Here( 1 );
x = {1, 2, 3};
Python Send( x );
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Python Send( dt );
Python Submit( "print(x)" );
Python Submit( "print(dt)" );

Python Send File(filename, <Python Name( name )>)
Description

Sends a data file to Python. The file name argument is a quoted string that specifies a
pathname to the file to be sent to Python.
Argument
filename The name of the file to be sent to Python.

<Python Name( name )> Specifies the name assigned to the file in the Python
environment.
Python Submit(python_code)
Description

Submits Python code to the Python environment.
Returns

Returns 0 if successful and non-zero otherwise.
Arguments
python_code The Python code to submit. Statements can be a quoted string value or a list

of string values.
Example
Names Default To Here( 1 );
Python Submit( "\[
str = 'The quick brown fox jumps over the lazy dog'
a = 200]\" );
getStr = Python Get( str );
getNum = Python Get( a );
