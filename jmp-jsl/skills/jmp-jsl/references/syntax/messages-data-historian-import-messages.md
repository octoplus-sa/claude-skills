# Data Historian Import Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 480-484).

## Index (line numbers in this file)

- `<< AF Path` — L204
- `<< Authentication Method` — L125
- `<< Boundary Type` — L210
- `<< End Time` — L214
- `<< Filter` — L218
- `<< Importer` — L75
- `<< Interval` — L222
- `<< Intervals` — L231
- `<< Max Count` — L235
- `<< Modify` — L177
- `<< New Namespace` — L60
- `<< Next` — L63
- `<< Password` — L182
- `<< Remove` — L65
- `<< Retrieve Attribute Status` — L239
- `<< Run` — L104
- `<< Series` — L246
- `<< Show Contents` — L67
- `<< Stack` — L250
- `<< Start Time` — L255
- `<< Sync Time` — L260
- `<< URL` — L194
- `<< Unlock Namespace` — L69
- `<< Username` — L198
- `AF Path()` — L151
- `Aggregate()` — L78
- `Anchor()` — L80
- `Authentication Method()` — L146
- `Boundary Type()` — L166
- `Data Source()` — L87
- `End Time()` — L90
- `Filter()` — L169
- `Include Outsiders()` — L77
- `Max Count()` — L168
- `Names Default To Here()` — L139
- `Password()` — L148
- `Period()` — L98
- `Retrieval Type()` — L91
- `Retrieve Attribute Status()` — L170
- `Series()` — L160
- `Start Time()` — L89
- `Tag Set()` — L88
- `Time()` — L81
- `Timeout()` — L173
- `URL()` — L145
- `UTC()` — L164
- `Username()` — L147
- `Wait()` — L119
- `While()` — L117
---

Data Historian Import Messages

ns<<New Namespace(name, <{list of expressions}>)
Creates a namespace where all functions and variables created are defined only within the
optional quoted name argument.
ns<<Next(variable name)
Returns the name of the variable that follows the specified quoted variable.
ns<<Remove(variable name, ...)
Removes the specified quoted variable or list of variables.
ns<<Show Contents
Shows the contents of a namespace in the log.
ns<<Unlock Namespace(variable name, ...);
Unlocks the specified quoted variables in the namespace. If no variables are specified, all
variables are unlocked.

Data Historian Import Messages
AspenTech InfoPlus.21 Messages
obj<<Importer(Data Source(string), Tag Set(string), Start Time(time
string), End Time(time string), Retrieval Type(<type>), Max Count(n),
Include Outsiders(Boolean), Stepped(Boolean), Period(<unit>(n),
Aggregate(Method("Integral"|"Value"|"Integral Incomplete"|"Value
Incomplete"), Start("Start of Day"|"Start of Time"),
Anchor("Begin"|"Middle"|"End"), Adjust For Daylight Savings
Time(Boolean)))
Description

Creates a raw importer instance.
Example
importer = client << Importer(
Data Source("MYDATASOURCE"),
Tag Set("TAG1", "TAG2", "TAG3"),
Start Time(Today() - In Days(1)),
End Time(Today()),
Retrieval Type("Interpolated"),

JSL Messages
Data Historian Import Messages

481

Period(Minute(90))
);

See Also

Using JMP.
obj<<Run( Async )
Description

Imports data from an existing AspenTech IP.21 server connection.
Optional Arguments
Async Performs the import in the background. This allows you to work on other tasks

simultaneously. When using the Async argument, the Run message returns a Promise
object to the imported data table. Use the Promise object to check if the import is
complete.
Example
dt promise = importer << Run( Async );
// Perform other actions while waiting for the import to complete
While( !(dt promise << Has Result),
// Perform other actions here, or just wait
Wait( dt promise );
);
// Imported data table is now available
dt = dt promise << Result;

PI Server Messages
obj<<Authentication Method("none"|"kerberos"|"basic")
Description

Specifies the authentication method.
obj<<Importer(AF Path(Asset Framework path), <Series(string)>, <Start
Time(PI time string)>, <End Time(PI time string)>, <UTC(boolean)>,
<Boundary Type(string)>, <Max Count(integer)>, <Filter(string)>,
<Retrieve Attribute Status(boolean)>, <Intervals(integer)>, <Sync
Time(PI time string)>, <Sync Time Boundary Type(string)>,
<Interval(duration in PI AFTimeSpan format)>, <Timeout(integer)>)
Description

Creates a new raw importer instance.
Example
Names Default To Here( 1 );
/* Import raw data with attribute status */

Data Historian Import Messages

client = New PI Client(
URL( "https://myserver.com/piwebapi" ),
Authentication Method( "basic" ),
Username( "myuserid" ),
Password( "mypassword" )
);
importer = client << Importer(
AF Path(
/* Asset Framework paths */
"\\myserver\PIData\Atlanta Data Center\Server Rack1\ION 6200 Power
Meter1|I A",
"\\myserver\PIData\Atlanta Data Center\Server Rack1\ION 6200 Power
Meter1|I B",
"\\myserver\PIData\Atlanta Data Center\Server Rack1\ION 6200 Power
Meter1|I C"
),
Series( "raw" ),
Start Time( "*-1d" ), /* PI time string */
End Time( "*" ),
/* PI time string */
UTC( 0 ), /* Whether specified start/end times are based on UTC - default is
zero */
Boundary Type( "inside" ), /* Choices are "inside", "outside",
"interpolated" */
Max Count( 5000 ), /* Max. number of values to fetch - default is 5000 */
Filter( "" ), /* Optional filter */
Retrieve Attribute Status( 1 ), /* retrieve attribute status for each
imported column, into corresponding columns "I A status", "I B status", and
"I C status" */
Timeout( 120 ) /* add extra time for the server to respond */
);
importer << Run;

obj<<Modify
Description

Invokes the import window, using the provided parameters as a starting point, to create
an interactive session where new tables can be imported.
obj<<Password(text)
Description

Only used when authentication method is ʺbasicʺ.

JSL Messages
Data Historian Import Messages

obj<<Run
Description

Runs the importer to create the table.
obj<<URL(text)
Description

URL of the PI server REST API endpoint.
obj<<Username(text)
Description

Required when authentication method is ʺbasicʺ.

Importer Messages
obj<<AF Path(path1, path2, ...)
Description

Asset Framework path of the attribute to import. This can be a single path or multiple
paths. The list of paths can be a JSL List, allowing the set of paths to be placed in a list
variable.
obj<<Boundary Type("inside"|"outside"|"interpolated")
Description

Determines how values that occur near the start and end time boundaries are treated.
obj<<End Time(text)
Description

Optional end time of the series to import. Default value is ʺ*ʺ (now).
obj<<Filter(text)
Description

An optional filter expression using PI Server’s filter expression syntax.
obj<<Interval(text)
Description

Sampling interval in AFTimeSpan format. The default is ʺ1hʺ.

483

Data Historian Import Messages

obj<<Intervals(n)
Description

Number of intervals to fetch. Default is 24.
obj<<Max Count(n)
Description

Sets the maximum number of values to retrieve. The default is 5000.
obj<<Retrieve Attribute Status(state=0|1)
Description

Specifies whether to retrieve attribute status, which is stored in an additional column. This
column, named ʺ<attribute-name> statusʺ, uses a Multiple Response property with Value
Labels to display the status as a set of the values: ʺGood,ʺ ʺQuestionable,ʺ ʺSubstituted,ʺ
and ʺAnnotated.ʺ This option is disabled by default.
obj<<Series("raw"|"plot"|"interpolated")
Description

Specifies the time series type. The default value is ʺrawʺ.
obj<<Stack(state=0|1)
Description

Stacks attributes with the same name into a single column, and creates stacking columns
for the common elements in their paths.
obj<<Start Time(text)
Description

(Optional) Specifies the start time of the series to import. The default value is ʺ*-1dʺ (24
hours ago).
obj<<Sync Time(text)
Description

(Optional) Specifies the synchronization time that sets the starting point from which
interval boundaries are calculated.
