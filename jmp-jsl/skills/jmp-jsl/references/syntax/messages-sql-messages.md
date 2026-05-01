# SQL Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 497-500).

## Index (line numbers in this file)

- `<< Custom SQL` — L68
- `<< Generate SQL` — L77
- `<< Modify` — L79
- `<< PostQueryScript` — L81
- `<< Query Name` — L84
- `<< Run` — L88
- `<< Run Background` — L128
- `<< Send` — L44
- `<< SendTo` — L45
- `Connection()` — L158
- `From()` — L164
- `Gets()` — L85
- `N Rows()` — L124
- `Names Default To Here()` — L111
- `Null()` — L96
- `OnRunComplete()` — L180
- `QueryName()` — L162
- `Run Background()` — L171
- `Select()` — L163
- `Write()` — L120
---

JSL Messages
SQL Messages

497

was received. If a callback function is used, a fourth element is the socket that was used in
the original recv or recvfrom message.
Required Argument

n Specifies the number of bytes to receive from the other socket.
Optional Arguments

callback Specifies the name of a function to receive the data.
timeout If you use a callback, timeout specifies how long the function should wait
for an answer.
skt<<Send(stream)
skt<<SendTo(dgram)
Description

Sends the data in the argument to the other socket. Send sends a stream and sendto sends
a datagram.
Returns

A list of three quoted strings. The first string is the command name (“send” or “sendto”).
The second is “ok” if successful or an error message if not. The third string is any portion
of the stream that could not be sent, or empty if all the data was sent correctly.
Arguments

stream Specifies the command to send to the other socket.
dgram Specifies the command to send to the other socket.
Notes

Either argument might need to contain binary data. JMP represents non-printable ASCII
characters with a tilde (~) followed by the hexadecimal number. For example,
skt<<send(("GET / HTTP/1.0~0d~0a~0d~0a");

sends a “get request” to an HTTP server.

SQL Messages
obj<<Custom SQL(sql)
Description

Changes the query to a custom SQL query and sets the SQL.
Required Argument
sql The quoted SQL query.

SQL Messages

obj<<Generate SQL
Returns the SQL that the query generates when you run it.
obj<<Modify
Opens the query in Query Builder.
obj<<PostQueryScript(script as text)
Sets a JSL script that runs after the query finishes executing. script as text is quoted
JSL code.
obj<<Query Name(<new name>)
Gets (without the new name argument) or sets (with the new name argument) the name of
the query. The name of the query is used as the name of the data table that results from
running the query.
obj<<Run(<"Private"|"Invisible">, <Update Table(table)>,
<OnRunComplete(script)>, <OnRunCanceled(script)>, <OnError(script)>)
Description

Runs the SQL query in the background or foreground depending on the Query Builder
preference “Run queries in the background when possible”.
Returns

Null (if the query runs in the background) or a data table (if the query runs in the
foreground).
Optional Named Arguments
"Private" A quoted keyword that opens the data table that the query produces without
displaying it in a data table window. "Private" is available only if OnRunComplete is

included in the script.
"Invisible" A quoted keyword that hides the data table that the query produces. Use
this argument to keep the query result hidden but use it in a subsequent query. The
data table is displayed in the Home Window’s Window List and the Window > Unhide
list.
Update Table Updates the specified data table. Runs the query in the foreground.
OnRunComplete Specifies a script to run after the query is complete. To get the resulting
data table, include OnRunComplete. The OnRunComplete script needs to be defined in
the global namespace, as indicated by the double colons in this example:
Names Default To Here( 1 );
::onComplete = Function( {dt},
{default local},

JSL Messages
SQL Messages

499

Write(
"\!NQuery is complete! Result name: \!"",
dt << Get Name,
"\!", Number of rows: ",
N Rows( dt )
)
);
query = Include( "rentals_fam_romcom.jmpquery" );
query << Run Background( On Run Complete( ::onComplete ) );

OnRunCanceled Specifies a script to run after the user cancels the query.
OnError Specifies a script to run if an error occurs.
Notes

If you want the data table that results from the background query, use the OnRunComplete
optional argument. You can include a script that runs when the query completes and then
assigns a data table reference to the resulting data table. Or you might pass the name of a
function that accepts a data table as its first argument. That function is called when the
query completes.
Examples

The following example opens a query that you previously saved from Query Builder. The
query opens privately, that is, without opening Query Builder. The query runs, and the
resulting data table opens.
query = Open( "C:\My Data\Movies.jmpquery", "Private");
dt = query << Run();

You can include a .jmpquery file in a script and run the query in the background using the
<<Run Background message.
query = Include( "C:\Queries\movies.jmpquery");
query <<Run Background();

The following example queries the database, opens the resulting data table, and prints the
number of data table rows to the log.
confirmation = Function( {dtResult},
Write( "\!NNumber of rows in query result: ", N Rows( dtResult ) )
);
query = New SQL Query(
Connection(
"ODBC:DSN=SQL
Databases;APP=MYAPP;TrustedConnection=yes;WSID=D79255;DATABASE=SQB;"
),
QueryName( "movies_to_update" ),
Select( Column( "YearMade", "t1" ), Column( "Rating", "t1" ) ),
From( Table( "g6_Movies", Schema( "SQB" ), Alias( "t1" ) ) ),

SQL Messages

);
query << Run( OnRunComplete( confirmation ) );

Run Background(<OnRunComplete(script), <"Private"|"Invisible">>,
<OnRunCanceled(script)>, <OnError(script)>)
Description

Runs the SQL query in the background. The running query is not displayed.
Returns

Null (or the data table object, if OnRunComplete is included).
Optional Named Arguments
OnRunComplete(script) Specifies a script to run after the query is complete. To get the
resulting data table, include OnRunComplete. The OnRunComplete script needs to be

defined in the global namespace, as indicated by the double colons in this example:
Names Default To Here( 1 );
::onComplete = Function( {dt},
{default local},
Write(
"\!NQuery is complete! Result name: \!"",
dt << Get Name,
"\!", Number of rows: ",
N Rows( dt )
)
);
query = Include( "rentals_fam_romcom.jmpquery" );
query << Run Background( On Run Complete( ::onComplete ) );

"Private" Does not open the resulting data table. Specify only with OnRunComplete. If
you include private in a background query, JMP opens the data table as invisible

instead.
"Invisible" Hides the data table. Use this argument to keep the query result hidden but
use it in a subsequent query. The data table is displayed in the Home Window’s
Window List and the Window > Unhide list.
OnRunCanceled Specifies a script to run after the user cancels the query.
OnError Specifies a script to run if an error occurs.
Notes

All queries run in the background based on the Query Builder preference “Run the queries
in the background when possible”, which is selected by default.
You can include a .jmpquery file in a script and run the query in the background using the
Run Background message.
query = Include( "C:\Queries\movies.jmpquery");
query <<Run Background();
