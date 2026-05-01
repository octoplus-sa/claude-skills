# Row State Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 305-308).

## Index (line numbers in this file)

- `<< Select Rows` — L198
- `As Row State()` — L56
- `Color Of()` — L66
- `Color State()` — L83
- `Combine States()` — L93
- `Excluded State()` — L113
- `Excluded()` — L103
- `Hidden State()` — L127
- `Hidden()` — L123
- `Hue State()` — L131
- `Labeled State()` — L139
- `Labeled()` — L135
- `Marker Of()` — L143
- `Marker State()` — L147
- `Names Default To Here()` — L46
- `Row State()` — L151
- `Selected State()` — L175
- `Selected()` — L171
- `Shade State()` — L179
---

JSL Functions, Operators, and Messages
Row State Functions

305

Where(<dt>, clause)
Description

Filters and returns indices depending on the given clause. The clause can be a comparison
function or a conditional statement. Columns, matrices, and lists can be mixed and
matched within the same clause.
The indices returned by Where() are optimized for high performance on large lists,
matrices, and columns.
Required Arguments
clause A comparison function or conditional statement.
Optional Arguments
<dt> Changes the current Data Table during the evaluation.
Examples
Names Default To Here( 1 );
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Clear Select << Select Rows(
Where( Col Max( :height, :age ) >= 68 )
);
dt << Clear Select << Select Rows(
Where( :height == Col Max( :height, :age ) )
);

Row State Functions
As Row State(i)
Description

Converts i into a row state value.
Returns

A row state from the i given.
Argument
i an integer

Color Of(rowstate)
Description

Returns or sets the color index.
Returns

The color index of rowstate.

Row State Functions

Argument
rowstate a row state argument
Example

Set the color of the fifth row to red.
Color Of( Rowstate( 5) ) = 3

Color State(i)
Description

Returns a row state with the color index of i.
Returns

A row state.
Argument
i index for a JMP color

Combine States(rowstate, rowstate, ...)
Description

Generates a row state combination from two or more row state arguments.
Returns

A single numeric representation of the combined row states.
Arguments
rowstate Two or more row states.

Excluded(rowstate)
Description

Returns or sets an excluded index.
Returns

The excluded attribute, 0 or 1.
Argument
rowstate One or more row states.

Excluded State(num)
Description

Returns a row state for exclusion from the num given.

JSL Functions, Operators, and Messages
Row State Functions

307

Hidden(rowstate)
Description

Returns or sets the hidden index.
Hidden State(num)
Description

Returns a row state for hiding from the num given.
Hue State(num)
Description

Returns a hue state from the num given.
Labeled(rowstate)
Description

Returns or sets the labeled index.
Labeled State(num)
Description

Returns a labeled state from the num given.
Marker Of(rowstate)
Description

Returns or sets the marker index of a row state.
Marker State(num)
Description

Returns a marker state from the num given.
Row State(<dt,> <n>)
Description

Returns the row state changed from the initial condition of the active row or the nth row.
Arguments
dt Optional positional argument: a reference to a data table. If this argument is not in the

form of an assignment, then it is considered a data table expression.
n The row number.

Row State Functions

Example

The following example creates the data table references and then returns the row state of
row 1 in Big Class.jmp:
dt1 = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt2 = Open( "$SAMPLE_DATA/NYC 311 Records.jmp" );
Row State( dt1, 1 );

Selected(rowstate)
Description

Returns or sets the selected index.
Selected State(num)
Description

Returns a selected state from the num given.
Shade State(num)
Description

The Shade State function assigns 5 shade levels to a color or hue.
Where(<dt>, clause)
Description

Filters and returns indices depending on the given clause. The clause can be a comparison
function or a conditional statement. Columns, matrices, and lists can be mixed and
matched within the same clause.
The indices returned by Where() are optimized for high performance on large lists,
matrices, and columns.
Required Arguments
clause A comparison function or conditional statement.
Optional Arguments
<dt> Changes the current Data Table during the evaluation.
Examples
Names Default To Here( 1 );
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Select Rows( [2 4 6] ) << Exclude( 1 );
Where( Excluded() );
Where( !Excluded() );
