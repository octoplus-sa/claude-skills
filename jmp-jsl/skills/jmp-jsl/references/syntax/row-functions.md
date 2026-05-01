# Row Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 299-304).

## Index (line numbers in this file)

- `As Table()` — L43
- `Col Stored Value()` — L62
- `Column Name()` — L95
- `Column()` — L84
- `Count()` — L105
- `Current Data Table()` — L144
- `Data Table List()` — L291
- `Data Table()` — L157
- `Dif()` — L173
- `Dim()` — L185
- `For Each Row()` — L136
- `Format()` — L224
- `Get Data Table List()` — L197
- `Get Data Table()` — L159
- `Lag()` — L204
- `Mean()` — L80
- `N Row()` — L208
- `N Rows()` — L209
- `N Table()` — L219
- `New Column()` — L223
- `New Table()` — L242
- `Row()` — L259
- `Sequence()` — L264
- `Stored Value()` — L79
- `Subscript()` — L275
- `Suppress Formula Eval()` — L282
- `The Like()` — L236
- `Use Project()` — L203
---

JSL Functions, Operators, and Messages
Row Functions

299

Row Functions
As Table(matrix, <matrix 2, ...>, < <<invisible >, < <<private >, <
<<Column Names({list}) >)
Description

Creates a new data tables from the matrix.
Returns

The new data table.
Argument
matrix Any matrix.
<<invisible Creates an invisible data table that hides the table from view but lists it in

the JMP Home Window and Window menu.
<<private Hides the table completely. Creating a private data table speeds the process of

getting to the data; it does not save the computer from allocating the memory necessary
to hold the data table data.
<<Column Names(list) The list specified column names for the data. The argument is a
list of quoted column names.
Col Stored Value(<dt>, col, <row>)
Description

Returns the data values stored in the column and disregards values assigned through
column properties (such as Missing Value Codes).
Arguments
dt Optional reference to a data table. If this value is not supplied, the current data table is

used.
col Name of the column.
row (Optional) Row name or number. If this value is not specified, the current row is
used.
Example

Suppose that the Missing Value Codes column property is assigned to the x1 column to
treat “999” as a missing value. Another column includes a formula that calculates the
mean. To use the value “999” instead of a missing value to calculate the mean, use Col
Stored Value() in the formula:
Mean( Col Stored Value( :x1 ), :x2, :x3 )

Row Functions

Column(<dt>, "name", "formatted")
Column(<dt>, n)
Description

Gets a reference to the data table column.
Arguments
dt Optional reference to a data table. If this is not supplied, the current data table is used.
name A quoted string that is the name of the column.
formatted A quoted string that returns the formatted string of the cell value.
n The column number.

Column Name(n)
Description

Determines the name of the column specified by number.
Returns

The name of the nth column as an expression (not a quoted string).
Argument
n The number of a column.

Count(from, to, step, times)
Description

Used for column formulas. Creates row by row the values beginning with the from value
and ending with the to value. The number of steps specifies the number of values in the
list between and including the from and to values. Each value determined by the first
three arguments of the count function occurs consecutively the number of times that you
specify. When the to value is reached, count starts over at the from value. If the from and
to arguments are data table column names, count takes the values from the first row only.
Values in subsequent rows are ignored.
Returns

The last value.
Arguments
from Number, column reference, or expression. Count starts counting with this value.
to Number, column reference, or expression. Count stops counting with this value.
step Number or expression. Specifies the number of steps to use to count between from

and to, inclusive.
times Number or expression. Specifies the number of times each value is repeated before
the next step.

JSL Functions, Operators, and Messages
Row Functions

301

Examples

/* the rows in the column named colname are filled with the series 0, 3, 6, 0,
... until all rows are filled */
For Each Row(:colname[row()]=count(0, 6, 3, 1))
/* the rows in the column named colname are filled with the series 0, 0, 3,
3, 6, 6, 0, ... until all rows are filled */
For Each Row(:colname[row()]=count(0, 6, 3, 2))

Notes
Count() is dependent on Row(), and is therefore mainly useful in column formulas.

Current Data Table(<dt>)
Description

Without an argument, gets the current (topmost) data table. With an argument, sets the
current data table.
Returns

Reference to the current data table.
Argument
dt Optional name of or reference to a data table.
Notes

Private tables cannot be made current with Current Data Table().
Data Table(n)
Data Table("name")
Get Data Table(<project(title|index|box|window),> name|index)
Description

Gets reference to the nth open data table or the table with the given name in a global
variable.
Returns

Reference to the specified data table.
Argument
n Number of a data table.
name Quoted string, name of a data table.

Row Functions

Dif(col, n)
Description

Calculates the difference of the value of the column col in the current row and the value n
rows previous to the current row.
Returns

The difference.
Arguments
col A column name (for example, :age).
n A number.

Dim(<dt|matrix>)
Description

Returns a row vector with the dimensions of the current data table, a specified data table,
or a matrix. The dimensions are the number of rows and the number of columns and are
listed in that order.
Arguments
dt A data table.
matrix A matrix.
Notes

If no argument is specified, the dimensions of the current data table are returned.
Get Data Table List(<Project(title|index|box|window>)
Description

Returns a list of all open data tables.
Notes

Use Project(0) to specify no project when running the expression in a project.
Lag(col, n)
Description

Returns for each row the value of the column n rows previous.
N Row(dt); NRow(matrix)
N Rows(dt); NRows(matrix)
Description

Returns the number of rows in the data table given by dt or in the matrix.

JSL Functions, Operators, and Messages
Row Functions

303

N Table()
Description

Returns the number of open data tables. Private tables are not included.
New Column("name", <"data type">, <"modeling type">, <Width(n)>,
Format("format", width, precision), <Formula()>, <Set Values>, <Like(column
reference)>, <actions>)
Description

Adds a new column named "name" after the last column in dt. Unless otherwise
specified, columns are numeric, continuous, and 12 characters wide.
Returns

A column reference.
Notes

Can also be used as a message: dt<<New Column.
The Like() argument copies the data type, modeling type, format, formula, and other
properties from the reference column into the new column.
See Also

“dt<<New Column(name, <data type>, <modeling type>, <Format(format, width)>,
<Formula()>, <Set Values({..., ..., })>, <Set Property(properties)>)”
New Table("name", <visibility("invisible" | "private" | "visible")>,
<actions>)
Description

Creates a new data table with the specified name.
Arguments
name A quoted string that contains the name of the new table.
visibility Optional quoted keyword. invisible hides the data table from view but
lists it in the JMP Home Window and Window menu. private hides the table
completely. visible shows the data table. "visible" is the default value.

Note: Creating a private data table speeds the process of getting to the data; it does not
save the computer from allocating the memory necessary to hold the data table data.
actions Optional argument that can define the new table.

Row Functions

Row()
Row() = y
Description

Returns or sets the current row number. No argument is expected.
Sequence(from, to, <step size>, <repeat times>)
Description

Produces an arithmetic sequence of numbers across the rows in a data table. The step
size and repeat times arguments are optional, and the default value for both is 1.
Subscribe to Data Table List(<subscriber name|"">,
<OnOpen(function)|OnClose(function)|OnRename(function)>)
Description

Subscribes to the data table list. You will be notified when a new data table has been
added, closed, or renamed.
Subscript(a, b, c)
list[i]
matrix[b, c]
Description

Subscripts for lists extract the ith item from the list, or the bth row and the cth column
from a matrix.
Suppress Formula Eval(Boolean)
Description

Turns off automatic calculation of formulas for all data tables.
Unsubscribe to Data Table List(<subscriber name>,
<"OnOpen"|"OnClose"|"All">)
Description

Removes a subscription to the data table list that has been added through Subscribe to
Data Table List().
