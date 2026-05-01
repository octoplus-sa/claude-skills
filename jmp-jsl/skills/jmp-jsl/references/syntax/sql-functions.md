# SQL Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 309-310).

## Index (line numbers in this file)

- `As SQL Expr()` — L29
- `Compatible()` — L45
- `Complete()` — L86
- `Connection()` — L71
- `Expr()` — L33
- `From()` — L77
- `New SQL Query()` — L39
- `Open()` — L42
- `Query()` — L93
- `QueryName()` — L74
- `Select()` — L40
- `Show()` — L79
- `Table()` — L116
---

JSL Functions, Operators, and Messages
SQL Functions

309

SQL Functions
Note: Database table names that contain the characters $# -+/%()&|;? are not supported.
As SQL Expr(x, <style>)
Description

Converts an expression to code that you can use in an SQL Select statement. Use
Expr(...) for literal expressions. Use NameExpr(name) for expressions stored in a
variable. Otherwise, the expression returns the expression to convert.
Returns

A quoted string that contains the expression converted to valid SQL syntax for use in an
SQL Select statement.
New SQL Query(Connection ("ODBC:connection_string"),
Select(Column("column", "t1")), From(Table("table", <Schema("schema")>,
<Alias("t1")>)), <Options(JMP 12 Compatible(1)|JMP 13 Compatible(1)|Run on
Open(1)))>
New SQL Query(Connection("ODBC:connection_string;"), Custom SQL("SELECT
col1, col2, col3 FROM table;")), <Options(JMP 12 Compatible(1)|JMP 13
Compatible(1)|Run on Open(1))>
Creates an SQL Query object for the specified connection, columns, data table, or for the
custom SQL query.
Returns

A data table that contains the queried data. The data table includes the quoted SQL query
string and table scripts for modifying and updating the query.
Arguments
Connection The quoted string for an ODBC connection.
Select The column that you want to select and its alias.
From The table that is queried and the optional schema and column alias.
Custom SQL An SQL statement that selects columns from the specified table.
Version The minimum JMP version required to open the query. If this condition is not

met, a message regarding compatibility is written to the log, and the query does not
open.
Options Boolean. JMP 12 Compatible is included in generated scripts when you select
the Query Builder preference to create a JMP 12 compatible option or select the
corresponding Query Builder red triangle menu option. The option enables JMP 12
users to run a JMP 13 query that might contain compatibility issues. Include Run on
Open(1) to run the query when opened rather than opening the query in edit mode.

SQL Functions

Example
New SQL Query(
Connection(
"ODBC Connection String..."
),
QueryName( "g6_Movies" ),
Select( Column( "ItemNo", "t1" ), Column( "LengthMins", "t1" ), Column(
"Genre", "t1" ) ),
From( Table( "g6_Movies", Schema( "SQBTest" ), Alias( "t1" ) ) )
) << Run Background( On Run Complete( dt = queryResult ) );
Show( dt );

Notes

•

Query Builder creates a symbol called queryResult in the context of an On Run
Complete() script. This is a reference to the data table imported by the query.
queryResult enables you to assign a global variable to the table for later use.

•

New SQL Query() always closes the ODBC connection after performing the query. There
is not a command to close an ODBC connection that was established with New SQL
Query().

•

New SQL Query() does not include the password from the connection string in the
resulting table even if the Hide ODBC Connection String preference is not checked.

•

After you run New SQL Query(), the database connection appears in the Database > Open
Table window as an available connection. JMP is keeping track of how to connect to that
database; the ODBC connection was not left open.

Query(<<dt1|Table(dt1, alias1)>, ..., <dtN, aliasN)>>, <private |
invisible>, <scalar>, sqlStatement )
Description

Performs a SQL query on selected data tables.
Returns

The result of the query, either a data table or a single value.
Arguments
dt1, dtN (Optional) A variable that has been assigned to the data table.
Table (Optional) Passes a reference to the data table.
alias1, aliasN Specifies the alias of the database table.
private (Optional) Avoids showing the resulting data table. Using a private data table

speeds the process of getting to the data; it does not save the computer from allocating
the memory necessary to hold the data table data.
invisible (Optional) Hides the resulting data table from view. The data table appears
only in the JMP Home Window and the Window menu. Hidden data tables remain in
