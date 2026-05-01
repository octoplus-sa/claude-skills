# Efficient Scripts

Source: JMP 19 Scripting Guide (PDF pages 933-938).

## Index (line numbers in this file)

- `<< Add Rows` — L172
- `<< Distribution` — L167
- `<< Fit Line` — L227
- `<< Show Window` — L218
- `Add Factor()` — L127
- `Avoid Break()` — L257
- `Close()` — L137
- `Column()` — L168
- `DOE()` — L125
- `Data Update()` — L165
- `Delete Symbols()` — L91
- `Dispatch()` — L197
- `New Window()` — L210
- `Preferences()` — L191
- `SendToReport()` — L196
- `Show()` — L73
- `Wait()` — L170
---

Appendix B
Efficient Scripts
Tips for Writing Scripts That Run Faster
This appendix provides ideas for writing JSL scripts that run faster and more efficiently. For
example, it is possible to control how much time is allocated to finding an optimal design. You
can collapse outlines in a report that are not necessary. Or you can write static matrices, which
is faster than developing them dynamically.

934

Efficient Scripts

Appendix B

Contents
Use Matrices. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 935
Design of Experiments Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 936
Script Data Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 936
Script Graphs and Display Boxes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 937
Script Numbers, Strings, Arrays, and Lists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 938
Programming Tips . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 938
Troubleshoot Scripts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 938

Appendix B

Efficient Scripts
Use Matrices

935

Use Matrices
•

The matrix concatenation operators, || and |/, add columns or rows to a matrix
dynamically. However, the script runs faster if you define a matrix in a static fashion
instead.
// faster example
t1 = Tick Seconds();
A = J( 10, 10000, . );
For( i = 1, i <= 10000, i++,
a2 = J( 10, 1, Random Gamma( 1, 1 ) );
// define a2 to be a 10 by 1 vector of random gamma values.
A[0, i] = a2;
/* populate the ith column of the matrix A to have the
values in a2. The first argument, 0, means "all rows". */
);
t2 = Tick Seconds();
Show( t2 - t1 );
t2 - t1 = 0.0166666666627862;
// slower example
t3 = Tick Seconds();
B = J( 10, 0, . );
For( i = 1, i <= 10000, i++,
a2 = J( 10, 1, Random Gamma( 1, 1 ) );
B = B || a2;
);
t4 = Tick Seconds();
Show( t4 - t3 );
t4 - t3 = 3.1333333333605;

•

If you know the size of a matrix that youʹre going to need, it’s typically better to allocate
the matrix in its entirety first and then populate it. In the example below, the J() function
is doing the allocation of the 100000x1 matrix all at the same time.
Delete Symbols( a1, a2 );
// faster example
t1 = Tick Seconds();
a1 = J( 100000, 1, Random Uniform() );
t2 = Tick Seconds();
Show( t2 - t1 );
Delete Symbols( a1 );
t2 - t1 = 0;
// slower example
t3 = Tick Seconds();
a2 = J( 0, 0 );

936

Efficient Scripts
Design of Experiments Options

Appendix B

For( i = 1, i <= 100000, i++,
a2 |/= Random Uniform()
);
t4 = Tick Seconds();
Show( t4 - t3 );
t4 - t3 = 5.05000000004657;

•

Use matrices rather than a data table to store numbers.

Design of Experiments Options
In DOE, there are options such as Number of Starts and Design Search Time that enable
you to control how much time is allocated to finding an optimal design.
// Number of Starts example
DOE(
Custom Design,
Add Factor( Continuous, -1, 1, "X1", 0 ),
Add Factor( Continuous, -1, 1, "X2", 0 ),
Add Factor( Continuous, -1, 1, "X3", 0 ),
Number of Starts( 1000 ),
Make Design
);
// Design Search Time example
d = DOE( Screening Design );
dt2 = Open( "$SAMPLE_DATA/Design Experiment/Weld Factors.jmp" );
d << Load Factors;
Close( dt2 );
d << {Set Random Seed( 12345 ), Screening Type( 1 ),
Suppress Cotter Designs, Design Search Time( 8 ),
Number of Column Starts( 50 ), Set Sample Size( 12 ), Make Design};

Script Data Tables
•

Displaying a large data table can cause scripts to run slower. To speed things up, you can
make a data table invisible, especially if you need to reference numbers in a report that
will be used for future calculations or used in another platform. In this case, there isnʹt a
need to see the current data table.
dt = Open( "$SAMPLE_DATA/Big Class.jmp", invisible);

•

Drawing objects is slow. Suppose that you have a graph with a lot of data. The platform
does complicated calculations or the data table contains a formula. Adding a row can
require a lot of processing. Use Begin Data Update() so you only redraw the graph once

Appendix B

Efficient Scripts
Script Graphs and Display Boxes

937

instead of for each change. Begin Data Update() saves all update messages until End
Data Update() is reached.
dt = Open( "MyData.jmp" );
dt << Distribution(
Column( :"N=1"n, :"N=5"n), :"N=10"n )
);
Wait(1);
dt << Begin Data Update;
dt << Add Rows( 2000 );
dt << End Data Update;

•

The use of functions might help speed things up, for example, using the Summarize()
function rather than creating a Summary table. Maintaining a data table can be too much
overhead. See “Store Summary Statistics in Global Variables”.

•

Data tables are great for keeping tabular data.
– Keep data table strings under 23 characters. Longer strings have additional overhead.
– Numeric values use less memory than character values.

Script Graphs and Display Boxes
•

When displaying large numbers in graphs, you can set a preference to use Fast Markers.
Preferences( Fast Marker Threshold( 25000 ) ); // 50000 is the default.

•

Collapse some of the outline nodes in a report to speed up the script.
SendToReport(
Dispatch(
{"Fit Life by X - Hours BY Arrhenius Celsius (Temp) Regression "},
"Scatterplot",
OutlineBox,
{Close( 1 )}
),

•

Construct your display boxes outside New Window() and then include them by reference
in New Window(). This method saves the drawing until the end.
tb = Text Box( "Select:" );
lb = List Box( {"One", "Two", "Three"} );
New Window( "test", tb, lb );

•

The user might not need to see a report if the numbers will be used in another platform or
for a future calculation. You can hide the report.
dt= Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Bivariate( Y( :Weight ), X( :Height ) );
obj << Show Window( 0 ); // hide the window

938

Efficient Scripts
Script Numbers, Strings, Arrays, and Lists

Appendix B

obj << Fit Line( {Confid Curves Fit( 1 )} );

Submit the following script to see the report window. Notice that the confidence curves
were fit even though the window was not shown.
obj << Show Window( 1 );

Script Numbers, Strings, Arrays, and Lists
•

Use a faster algorithm. Replacing an O(n^2) algorithm with an O(n) algorithm is faster
than anything else. See https://en.wikipedia.org/wiki/Big_O_notation.

•

Avoid concatenating long strings. 100s of characters is OK; 1,000,000s of characters will be
slow if you build the string in 1,000,000s of operations.

•

Use numeric arrays (matrices, not lists).
– Use numeric arrays with operators that operate on the entire array.
– Avoid writing loops to manipulate numeric arrays.

•

Use associative arrays for lookups.

Programming Tips
•

Avoid Break(), Continue(), and Return() functions for speed. Using them might make
it easier for you to read the script.

•

Functions versus expressions:
– User-defined functions have overhead for calling them but might make it easier for you
to read the script.
– Expressions have no overhead for calling but might make it more difficult for you to
read the script.

Troubleshoot Scripts
Use the JSL Debugger to discover where the script is expending the most time. See “Debug or
Profile Scripts”.
