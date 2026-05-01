# R Integration Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 490-492).

## Index (line numbers in this file)

- `<< Control` — L42
- `<< Disconnect` — L45
- `<< Execute` — L143
- `<< Get` — L104
- `<< Get Graphics` — L113
- `<< Is Connected` — L47
- `<< Send` — L101
- `<< Send File` — L49
- `<< Submit` — L126
- `<< Submit File` — L32
- `Colored()` — L65
- `Colors()` — L94
- `Echo()` — L137
- `Excluded()` — L61
- `Expand()` — L134
- `Hidden()` — L64
- `Labeled()` — L63
- `Markered()` — L72
- `Markers()` — L97
- `Row States()` — L75
- `Selected()` — L58
---

R Integration Messages

pythconn<<Submit File(path)
Description

Submits statements to Python using the quoted path name.
Argument
path The quoted path to the file that contains the Python source lines to be executed.

R Integration Messages
The R interfaces are also scriptable using an R connection object. A scriptable R connection
object can be obtained using the R Connect() function.
rconn<<Control(Interrupt|Async(Boolean)|Echo(Boolean))
Changes the control options for R. If Async is set to true (1) for R Submit(), this message
immediately stops the execution of the R code that was submitted.
rconn<<Disconnect()
Disconnects this R connection.
rconn<<Is Connected()
Returns 1if the R connection is active, 0 otherwise.
rconn<<Send File(name, <named arguments>)
Send the specified JMP variable to R.
Returns

0 if successful, nonzero otherwise.
Required Argument

name A quoted string contains the name of a JMP variable to send to R.
Optional Named Arguments for Data Tables
Selected(Boolean) If true, sends only the selected rows from the referenced data table

to R.
Excluded(Boolean) If true, sends only the excluded rows from the referenced data table
to R.
Labeled(Boolean) If true, sends only labeled rows from the referenced data table to R.
Hidden(Boolean) If true, sends only hidden rows from the referenced data table to R.
Colored(Boolean) If true, sends only colored rows from the referenced data table to R.

JSL Messages
R Integration Messages

491

Markered(Boolean) If true, sends only markered rows from the referenced data table to

R.
Row States(Boolean, <named arguments>) Includes a Boolean argument and
optional named arguments. Sends row state information from the referenced data table
to R by adding an additional data column named “RowState”. The row state value
consists of individual settings with the values shown in Table 3.2.
Table 3.2 Row States
Multiple row states are
created by adding
together individual
settings.

Selected = 1
Excluded = 2
Labeled = 4
Hidden = 8
Colored = 16
Markered = 32

Arguments

Colors(Boolean) (Optional) If true, sends row colors and

adds an additional data column named “RowStateColor”.
Markers(Boolean) (Optional) If true, sends row markers

and adds an additional data column named
“RowStateMarker”.
rconn<<Send(name, <R Name(name)>)
Sends the quoted JMP data file to R. The name argument can represent any of the
following data types: numeric, quoted string, matrix, list, or data table.
rconn<<Get(name)
Returns data from R. The name argument can represent any of the following data types:
numeric, quoted string, matrix, list, or data table.
Returns

The value of the specified variable.
Arguments

name Specifies the quoted name of a JMP variable to be retrieved from R.
rconn<<Get Graphics(type)
Gets the last graphics object written to the R graph display window. The graphics object
can be returned in different graphic formats.

R Integration Messages

Returns

A JMP picture object.
Required Argument
type The format the R graph display window contents are converted to. Valid formats are
"png", "bmp", "jpeg", "jpg", "tiff", and "tif".

rconn<<Submit(R code, Expand(Boolean), Echo(Boolean))
Submits the quoted R code.
Returns

0 if successful, nonzero otherwise.
Required Argument
code Specifies the quoted R code to submit.
Optional Named Arguments
Expand(Boolean) Performs an Eval Insert() on the R code before submitting the

code.
Echo(Boolean) Echoes the R source lines to the JMP log. The default value is true.
Rconn<<Submit File(path)
Submits statements to R using the file in the quoted path.
Arguments
path Specifies the quoted path to the file that contains R code to be executed.

rconn<<Execute({list of inputs}, {list of outputs}, R code, <named
arguments>)
Submits the quoted R code to the R connection using the list of inputs. Upon completion, a
list of outputs is returned.
Returns

0 if successful, nonzero otherwise.
Required Arguments

R code Specifies the quoted R code to submit.
{list of inputs} List of JMP variable names to be sent to R as inputs.
{list of outputs} List of JMP variable names to be retrieved from R as outputs.
Optional Named Arguments

See “rconn<<Submit(R code, Expand(Boolean), Echo(Boolean))”.
rconn<<Control(<Echo(Boolean)>)
Controls the execution of R.
