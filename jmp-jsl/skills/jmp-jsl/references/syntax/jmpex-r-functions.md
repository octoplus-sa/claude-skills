# JMPEX R Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 283-286).

## Index (line numbers in this file)

- `Async()` — L28
- `Echo()` — L26
- `Expand()` — L23
- `R Submit File()` — L40
---

JSL Functions, Operators, and Messages
JMPEX R Functions

283

Returns

0 if successful; nonzero otherwise.
Arguments
rCode A required, quoted string that contains the R code to submit.
Expand(Boolean) An optional named argument. Performs an Eval Insert() on the R

code before submitting to R.
Echo(Boolean) An optional named argument. Sends all source lines to the JMP log. This
option is global. The default value is true.
Async(Boolean) An optional named argument. If set to true (1), the submit can be
canceled either by pressing the ESCAPE key, or by using this message to an R
connection: rconn<<Control( Interrupt( 1 ) ). False (0) is the default value.
Example
rc = R Submit("\[
x <- rnorm(5)
print(x)
y <- rnorm(5)
print(y)
z = plot(x, y)
]\" );

R Submit File( "pathname" )
Description

Submits statements to R using a file.
Returns

0 if successful; nonzero otherwise.
Argument
pathname A quoted string that contains the pathname of the file that contains the R code

to execute.

JMPEX R Functions
jmpex.R.R( <'BACKEND'> )
Description

Creates the R class object. The optional BACKEND parameter specifies the backend R
support. Currently only rpy2 is supported, and is the default if not specified.

JMPEX R Functions

jmpex.R.R.get( 'R_variable' )
Description

Gets a variable from the R environment.
Returns

The value of the variable to Python using r2obj(). Returns an R DataFrame as a
pandas.DataFrame.
Example
import jmp
from jmpex.R import R
dt = jmp.open(jmp.SAMPLE_DATA + 'Big Class.jmp')
jr = R()
a = jr.set( dt['age'], 'r_age' ) # as_name required from Python
print(a.__class__)
print(a)
ra = jr.get('r_age')
print( ra.__class__ )
print( ra )

Note that on the Python side, jmpex.R.R.set() requires setting the ‘as_name’ parameter to
name the variable in R.
jmpex.R.R.is_connected()
Description

Returns whether the R subsystem has been initialized. This is a static function that is
available regardless of whether an R() instance object exists.
Returns

A Python True or False.
Example
import jmp
from jmpex.R import R
print(f'\nR initialized 1: {R.is_connected()}\n')
jr = R()
print(f'\nR initialized 2: {R.is_connected()}')

JSL Functions, Operators, and Messages
JMPEX R Functions

285

jmpex.R.R.obj2r( PyObj )
Description

Creates an R object from a Python object, where an appropriate conversion exists.
Returns

The created object or None.
Example
import jmp
from jmpex.R import R
jr = R()
d = { "canine": ["poodle", "dalmation", "wolf"],
"ages": [ 1, 3, 5],
"vet bill": [200.0, 300.57, 2000.99] }
r_obj = jr.obj2r( d )
p_obj = jr.r2obj( r_obj )
print(r_obj.__class__)
print(r_obj)
print(p_obj.__class__)
print(p_obj)

jmpex.R.R.r_version()
Description

Returns the version of R. Also prints to the log the rpy2 version, and the rpy2 package
path.
Example
import jmp
from jmpex.R import R
jr = R()
print(f'R Version: {jr.r_version()}')

jmpex.R.R.r2obj( rpy2_object )
Description

Creates a Python object from an R or rpy2 object where an appropriate conversion exists.
Returns

The created object or None.

JMPEX R Functions

Example
import jmp
from jmpex.R import R
jr = R()
d = { "canine": ["poodle", "dalmation", "wolf"],
"ages": [ 1, 3, 5],
"vet bill": [200.0, 300.57, 2000.99] }
r_obj = jr.obj2r( d )
p_obj = jr.r2obj( r_obj )
print(r_obj.__class__)
print(r_obj)
print(p_obj.__class__)
print(p_obj)

jmpex.R.R.set( Python_variable, 'as_R_name' )
Description

Sets a Python variable in the R environment named by the required ‘as_R_name’
parameter. The R object is created using obj2r().
Example
import jmp
from jmpex.R import R
dt = jmp.open(jmp.SAMPLE_DATA + 'Big Class.jmp')
jr = R()
a = jr.set( dt['age'], 'rage' ) # as_name required from Python
print(a.__class__)
print(a)
ra = jr.get('rage')
print( ra.__class__ )
print( ra )

jmpex.R.R.submit( 'R_script' )
Description

Submits R program code for evaluation.
Returns

A Python object, if possible.
