# Common Tasks

Source: JMP 19 Scripting Guide (PDF pages 917-930).

## Index (line numbers in this file)

- `<< Data Type` — L129
- `<< Modeling Type` — L130
- `<< New Column` — L210
- `<< Select Where` — L173
- `Add Rows()` — L108
- `Button Box()` — L378
- `Close()` — L339
- `Density Ellipse()` — L255
- `Fit Line()` — L256
- `Format()` — L150
- `Formula()` — L212
- `Group()` — L184
- `H List Box()` — L377
- `Insert Into()` — L420
- `Lineup Box()` — L300
- `Mean()` — L185
- `New Column()` — L109
- `Number Col Box()` — L315
- `Outline Box()` — L297
- `Output Table Name()` — L179
- `Set Values()` — L112
- `Spacer Box()` — L311
- `String Col Box()` — L306
- `Table Box()` — L320
- `Text Box()` — L301
- `V List Box()` — L363
- `While()` — L416
- `X()` — L254
- `Y()` — L253
---

Common Tasks
Getting Started with Sample Scripts
Examining working scripts line-by-line is one of the best ways to learn JSL. This chapter
describes common tasks in JMP, such as converting date/time values and extracting specific
values from reports. Sample scripts that address these issues are installed with JMP in the
Samples/Scripts folder so you can run them yourself.

918

Common Tasks

Contents
Run a Script at Start Up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 919
Convert Character Dates to Numeric Dates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 920
Format Date-Time Values and Subset Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 921
Create a Formula Column . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 922
Extract Values from an Analysis into a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 924
Create an Interactive Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 927

Common Tasks
Run a Script at Start Up

919

Run a Script at Start Up
You can run the same script every time you start JMP. For example, you might include the
definitions of some utility functions or a namespace that you want available throughout your
JMP session. You might also set some preferences in a startup script to keep preferences
consistent. Preferences persist across JMP sessions, but you could explicitly reset some
preferences in case they were changed at some point in the previous session.
Name the script jmpStart.jsl and place it in one of the following folders, as appropriate for your
operating system. When JMP starts, JMP looks for the jmpStart.jsl script in these folders in the
order in which they are listed here. The first one that is found is run, and the search
immediately stops.
Note: Some path names in this section refer to the “JMP” folder. On Windows, in JMP Pro, the
“JMP” folder is named “JMPPro”.
On Windows:
1. C:\Users\<username>\AppData\Roaming\JMP\JMP\19
2. C:\Users\<username>\AppData\Roaming\JMP\JMP

On Apple macOS:
1. /Users/<username>/Library/Application Support/JMP/19
2. /Users/<username>/Library/Application Support/JMP

The jmpStart.jsl script runs only for a particular user on a computer. You can add a script
named jmpStartAdmin.jsl in one of the following places, as appropriate for your operating
system. This script is run for every user on a computer. JMP runs jmpStartAdmin.jsl first if
found. Then JMP runs jmpStart.jsl if found.
On Windows:
1. C:\ProgramData\JMP\JMP\19
2. C:\ProgramData\JMP\JMP

On Apple macOS:
1. /Library/Application Support/JMP/19
2. /Library/Application Support/JMP

920

Common Tasks
Convert Character Dates to Numeric Dates

Convert Character Dates to Numeric Dates
In JMP, data might appear to be numeric in the data table. However, the column properties
can specify a character data type. To manipulate the data as date/time values, convert the
column to a numeric column and specify how you want the values to appear.
Convert Dates.jsl creates a data table, specifies the data input format, changes the column to a

numeric continuous column, and applies the m/d/y format (Figure 18.1).
// Create a data table with character dates.
dt = New Table( "Example",
Add Rows( 3 ),
New Column( "Dates",
Character,
Nominal,
Set Values( {"25/01/2010", "30/09/2009", "15/12/2013"} )
)
);
// Display a modal dialog for the user to confirm the format conversion.
nw = New Window( "Date Conversion",
<<Modal,
tb = Text Box(
"Notice the d/m/y format of the character dates.
Click OK to convert the column to a numeric column and apply the m/d/y
format."
)
);
/* Apply the Numeric data type.
Specify the Informat (input format) value "d/m/y".
Specify the Format (display format) value "m/d/y".
Apply the Continuous modeling type */
col = Column( dt, "Dates" );
col << Data Type( "Numeric", Informat( "d/m/y" ), Format( "m/d/y" ) );
col << Modeling Type( "Continuous" );

Common Tasks
Format Date-Time Values and Subset Data

921

Figure 18.1 Converting Character Dates (Before and After)

When you change the column’s data type from character to numeric, defining the format in
which the data were entered is important. In this example, Informat( "d/m/y" ) defines the
input format. Format( "m/d/y" ) defines the new display format. If Informat() is omitted,
the Format() value is applied as both the input and display format. This results in missing
values for some data.
Modify Convert Dates.jsl to see for yourself.
1. Open Convert Dates.jsl from the sample scripts folder.
2. Right-click the script window and select Show Line Numbers.
3. On line 9, change ʺ25/01/2010ʺ to ʺ01/25/2010ʺ.
4. On line 27, delete Informat( "d/m/y" ), (including the comma).
5. Run the script.
Format( "m/d/y" ) is applied to the column. Only ʺ01/25/2010ʺ appears in the column.

The other values are missing; ʺ30/09/2009ʺ and ʺ15/12/2013ʺ are not valid m/d/y values.

Format Date-Time Values and Subset Data
JMP provides a number of date formats that you can use to make comparisons and then
subset data based on the date.
Select Where Using Dates.jsl applies the Date MDY format to a column of departure dates and

subsets the data. A summary table of mean net costs by departure date then appears
(Figure 18.2).
/* How can you work with dates in JSL? JMP provides a number of formats
that you can use to make comparisons and then subset data based on the date.
*/
hdt = Open( "$SAMPLE_DATA/Travel Costs.jmp" );

922

Common Tasks
Create a Formula Column

/* Apply the Date MDY format to Departure Date values and then select only
February dates. */
hdt << Select Where(
(Date MDY( 02, 01, 2007 ) <= :Departure Date < Date MDY( 03, 1, 2007 ))
);
/* Subset the selected rows into two tables: one table contains February
departure dates, the other contains all data for those departure dates. */
nt1 = hdt << Subset( Columns( :Departure Date ),
Output Table Name( "February Departure Date" ) );
nt2 = hdt << Subset( Output Table Name( "February Data" ) );
/* Create a summary table, grouping mean cost by day of week that departure
took place. */
sumDt = nt2 << Summary(
Group( :Departure Day of Week ),
Mean( :Net Cost ),
Output Table Name( "Mean Net Cost by Departure Date" )
);

Figure 18.2 The Original Table and the Final Summary Table

Create a Formula Column
In JMP, you can create a formula column that combines conditional expressions with value
comparisons. Create a Formula Column.jsl shows how to create a new formula column that
evaluates ages in Big Class.jmp and returns the result in the new column (Figure 18.3).

Common Tasks
Create a Formula Column

/* Scenario:
How do you create a formula column that combines conditional expressions
with value comparisons? This script shows how to create a new formula
column that evaluates ages in Big Class.jmp and returns the conditional
result in the new column. */
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
/* Create a new character column for the formula.
Insert "early" in the new column if the age is less than or
equal to 12. Insert "mid" if the age is less than or equal to
15 but greater than 12. For ages greater than 15, insert "late".
*/
dt << New Column( "Adolescent Phase",
Character,
Formula(
If( :age <= 12, "early",
12 < :age <= 15, "mid",
"late"
)
)
);

923

924

Common Tasks
Extract Values from an Analysis into a Report

Figure 18.3 Conditional Expression in Formula

Extract Values from an Analysis into a Report
Using JSL, you can capture specific results of an analysis into a custom report. The JMP
platforms in the Analyze and Graph menus contain two objects known as the analysis and
report layers. Messages are sent to the analysis layer that generate the desired results.
Extract Values from Reports.jsl performs a Bivariate analysis and shows results such as the
sample size, RSquare, and Correlation in a new report window. Figure 18.4 shows the
customized report.

Common Tasks
Extract Values from an Analysis into a Report

925

/* Scenario: How do you capture specific results of an analysis
in a report using JSL?
The JMP platforms in the Analyze and Graph menus contain two objects
known as the analysis and report layers.
Messages are sent to the analysis layer that generate the desired results.
This script performs a Bivariate analysis and shows results
such as the sample size, RSquare, and Correlation in a new report window.
*/
sd = Open( "$SAMPLE_DATA/Lipid Data.jmp" );
biv = Bivariate(
// biv is the analysis layer.
Y( :Triglycerides ),
X( :LDL ),
Density Ellipse( 0.95, {Line Color( {213, 72, 87} )} ),
Fit Line( {Line Color( {57, 177, 67} )} ),
);
/* Make sure the second Outline Box (called "Correlation")
in the Bivariate report is open. You can then see which content
is extracted into the Custom report. */
report(biv) [Outline Box( 2 )] << Close( 0 );
reportbiv = biv << Report;

// reportbiv is the report layer.

/* The density ellipse is generated first.
Extract the correlation coefficient. */
corrvalue = reportbiv[Outline Box( 2 )][Number Col Box( 3 )] << Get( 1 );
/* ...followed by Fit Line
Extract the numeric values from the Summary of Fit report
and place them in a matrix. */
sumfit = reportbiv[Outline Box( 4 )][Number Col Box( 1 )] << Get as Matrix;
// Extract the values of RSquare and AdjRSquare as one by one matrices.
rsquare = sumfit[1];
adjrsq = sumfit[2];
avg = sumfit[4];
samplesize = sumfit[5];
/* Extract the first column of the Parameter.
Estimates report as two objects. */
term = reportbiv[Outline Box( 7 )][String Col Box( 1 )] << Get();

926

Common Tasks
Extract Values from an Analysis into a Report

// Clone the report layer as a String Col Box.
cloneterm = reportbiv[Outline Box( 7 )][String Col Box( 1 )] << Clone Box;
// Extract the Parameter Estimates values as a matrix.
est = reportbiv[Outline Box( 7 )][Number Col Box( 1 )] << Get as Matrix;
// Extract the Standard Error values as a matrix.
stde = reportbiv[Outline Box( 7 )][Number Col Box( 2 )] << Get as Matrix;
dvalues = [];
dvalues = samplesize |/ adjrsq |/ rsquare |/ corrvalue;
sfactor = term[2];
dlg = New Window( "Custom Report",
Outline Box( "Selected Values",
/* The Lineup box defines a two-column layout, each of which contains
a Text Box. */
Lineup Box( N Col( 2 ),
Text Box( "Factor of Interest: " ),
Text Box( sfactor ), ),
tb = Table Box(
/* Display an empty string in the first column
and the text in the second column. */
String Col Box( " ",
{"Sample Size: ", "Adjusted RSquare: ", "RSquare: ",
"Correlation:"}
),
// Insert a 30 pixel x 30 pixel spacer between the columns.
Spacer Box( Size( 30, 30 ) ),
,
/* Display an empty string in the first column
and the dvalues in the second column. */
Number Col Box( " ", dvalues )
),
// Insert a 1 x 30 spacer.
Spacer Box( Size( 0, 30 ) ),
,
Table Box(
/* Display the cloned String Col Box followed by a spacer.
Then insert the Parameter Estimates and Standard Error values. */
CloneTerm,
Spacer Box( Size( 10, 0 ) ),
,
Number Col Box( "Estimate", est ),
Spacer Box( Size( 10, 0 ) ),

Common Tasks
Create an Interactive Program

927

,
Number Col Box( "Standard Error", stde )
)
)
);
Close( sd ); // Close the data table.

Figure 18.4 Customized Report from the Bivariate Analysis

Create an Interactive Program
Using JSL, you can gather numeric input from users, perform a calculation on the input, and
show the results in a new window.
Prime Numbers.jsl asks the user to enter a number and then factors the number or confirms it

as a prime number (Figure 18.5). This script is a good example of aligning several types of
display boxes, concatenating text, and working with conditional functions.

928

Common Tasks
Create an Interactive Program

/* How do you gather numeric input from the users, perform a
calculation on that input, and show the results in a new window?
This script demonstrates how to create an interactive program that
asks the user to enter a number and then factors the number or confirms
it as a prime number. */
// Ask the user to enter a name and number.
nw = New Window( "Factoring Fun",
V List Box(
Text Box( "Choose a number between 2 and 100, inclusive. " ),
Spacer Box( Size( 25, 25 ) )
),
V List Box(
Lineup Box(
2,
Text Box( "Your name
" ),
uname = Text Edit Box( "< name > ", << Justify Text( Center ) ),
Text Box( "Your choice " ),
uprime = Number Edit Box( 2 )
),
Spacer Box( Size( 25, 25 ) ),
H List Box(
Button Box( "OK",
// Unload responses.
username = uname << Get Text;
fromUser0 = uprime << Get;
// Test input for out of range condition.
If( fromUser0 <= 1 | fromUser0 > 100,
// Send message to user that input value is out of range.
nw2 = New Window( " Factoring Fun: Message for "
|| username,
<<Modal,
Text Box(
"The number you chose, " || Char( fromUser0 ) ||
" is not between 2 and 100, inclusive.
Please try
again. "
),
Button Box( "OK" )
),

Common Tasks
Create an Interactive Program

929

/* Else the number is within range.
Test for a prime number. If not prime, factor it.
Create a vector which holds the prime numbers
within specified range. */
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
// Count the number of primes in the vector.
p# = N Row( primes );
isprime = 0; // Set flag.
// Make a copy of the value for processing.
fromuser1 = fromuser0;
factors = {}; // Initialize list.
/* Process the value by checking for prime then
factoring if needed. */
While( isPrime == 0,
// Compare value to vector of prime numbers.
If( Any( fromuser0 == primes ),
// If found, place value in factor list.
Insert Into( factors, fromUser0 );
isPrime = 1 // Set condition to exit While loop.
;
); // End For loop.
If( isprime == 0,
For( q = 1, q <= p#, q++,
If( Mod( fromuser0, primes[q] ) == 0,
fromUser0 = fromUser0 / primes[q];
Insert Into( factors, primes[q] );
q = p# + 1 // End if-then loop.
;
); // End If loop.
); // End For loop.
); // End If/Then loop.
); // End while loop.
cfUser0 = Char( fromUser1 );
nf = N Items( factors );
If( nf >= 2,
fmsg = "The number you have chosen has the following
factors: ",
fmsg = "The number you have chosen is a prime number: "
);

930

Common Tasks
Create an Interactive Program

// Show message to user about results.
nw3 = New Window( " Factoring Fun - Your Results",
<<Modal,
Text Box( username || ", you chose: " || cfUser0 ),
Spacer Box( Size( 25, 25 ) ),
Text Box( fmsg || " " || Char( factors ) ),
Spacer Box( Size( 25, 25 ) ),
Button Box( "OK" )
);
);
), // End the main OK button script.
// Close the window and the program.
Button Box( "Cancel", nw << Close Window )
)
)
);

Figure 18.5 Factor Numbers Interactively
