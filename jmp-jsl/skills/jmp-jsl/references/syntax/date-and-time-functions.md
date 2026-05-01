# Date and Time Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 76-84).

## Index (line numbers in this file)

- `Abbrev Date()` — L50
- `As Date()` — L65
- `Date DMY()` — L101
- `Date Difference()` — L77
- `Date Increment()` — L114
- `Date MDY()` — L139
- `Day Of Week()` — L171
- `Day Of Year()` — L187
- `Day()` — L152
- `Days In Month()` — L198
- `Format Date()` — L255
- `Format()` — L207
- `HP Time()` — L283
- `Hour()` — L270
- `ISO Year()` — L349
- `In Days()` — L292
- `In Hours()` — L300
- `In Minutes()` — L305
- `In Weeks()` — L310
- `In Years()` — L315
- `Informat()` — L320
- `Is Leap Year()` — L345
- `Long Date()` — L354
- `MDYHMS()` — L359
- `Minute()` — L364
- `Month()` — L371
- `Parse Date()` — L321
- `Quarter()` — L389
- `Second()` — L393
- `Short Date()` — L404
- `Tick Seconds()` — L409
- `Time Of Day()` — L416
- `Today()` — L420
---

Date and Time Functions

Date and Time Functions
Datetime values are handled internally as numbers of seconds since midnight, January 1,
1904.
The expression x=01Jan1904 sets x to zero, since the indicated date is the base date or “zero
date” in JMP. If you examine the values of dates, they should be appropriately large numbers
(for example, 5oct1998 is 2990390400).
Abbrev Date(date)
Description

Converts the provided date to a quoted string.
Returns

A quoted string representation of the date.
Argument

date Can be the number of seconds since the base date (midnight, January 1, 1904), or
any date-time operator.
Example
Abbrev Date( 29Feb2004 );
02/29/2004

As Date(x)
Description

Formats the number or expression x so that it shows as a date or duration when displayed
in a text window. Values that represent one year or more are returned as dates. Values that
represent less than a year are returned as durations.
Returns

A date that is calculated from the number or expression provided.
Argument
x Number or expression.

Date Difference(datetime1, datetime2, interval name, <alignment>)
Description

Returns the difference in intervals of two date-time values.
Returns

A number.
Required Arguments
datetime1, datetime2 Date-time values.

JSL Functions, Operators, and Messages
Date and Time Functions

77

interval name A quoted string that contains a date-time interval, such as "month",
"day", or "hour".
Optional Arguments

alignment A quoted string:
– "Start" includes full or partial intervals.
– "Actual" counts only whole intervals.
– "Fractional" returns fractional differences using averages for "year", "quarter",
and "month" intervals.
Date DMY(day, month, year)
Description

Constructs a date value from the arguments.
Returns

The specified date, expressed as the number of seconds since midnight, 1 January 1904.
Arguments

day The numeric day of month, 1-31. Note that there is no error-checking, so you can
enter February 31.
month The numeric month, 1-12.
year The year.
Date Increment(datetime, interval name, <increment>, <alignment>)
Description

Adds 1 or more intervals to a starting datetime value.
Returns

Returns the new datetime value.
Required Arguments

datetime The starting datetime value.
interval name A quoted string that contains the name of a datetime interval. "year",
"quarter", "month", "week", "day", "hour", "minute", and "second" are
supported.
Optional Arguments

increment A number that specifies the number of intervals. The default value is 1.
alignment A quoted string that contains a keyword:
– "Start" truncates the date to the nearest interval prior to adding the increment. For
example, it removes the time and outputs the date. "start" is the default value.
– "Actual" retains the full input datetime value.

Date and Time Functions

– "Fractional" allows fractional incremental values using averages for the duration of
"Year", "Quarter", and "Month" intervals.
Date MDY(month, day, year)
Description

Constructs a date value from the arguments.
Returns

The specified date, expressed as the number of seconds since midnight, 1 January 1904.
Arguments

month The numeric month, 1-12.
day The numeric day of month, 1-31. Note that there is no error-checking, so you can
enter February 31.
year The year.
Day(datetime)
Description

Determines the day of the month supplied by the datetime argument.
Returns

Returns an integer representation for the day of the month of the date supplied.
Arguments

datetime The number of seconds since midnight, 1 January 1904. This can also be an
expression.
Example
d1 = Date DMY( 12, 2, 2003 );
3127852800
Day( 3127852800 );
12
Day( d1 );
12

Day Of Week(datetime)
Description

Determines the day of the week supplied by the datetime argument.
Returns

Returns an integer representation for the day of the week of the date supplied. Weeks are
Sunday–Saturday.

JSL Functions, Operators, and Messages
Date and Time Functions

Arguments

datetime The number of seconds since midnight, 1 January 1904. This can also be an
expression.
Day Of Year(datetime)
Description

Determines the day of the year supplied by the datetime argument.
Returns

Returns an integer representation for the day of the year of the date supplied.
Arguments

datetime The number of seconds since midnight, 1 January 1904. This can also be an
expression.
Days In Month(year, month)
Description

Returns the number of days in the month for the specified month and year.

79

Date and Time Functions

Format(x, formatString, width|<width, decimal places>, <"Use Thousands
Separator">)
Format(x, "Best", <width>, <"Use Thousands Separator">)
Format(x, ("Fixed Dec"|"Percent"), width|<width, decimal places>, <"Use
Thousands Separator">)
Format(x, "Pvalue", <width>)
Format(x, ("Scientific"|"Engineering"|"Engineering SI"), <width>|<width,
decimal places>)
Format(x,"Precision", width|<width, decimal places>, <"Use Thousands
Separator">, <"Keep Trailing Zeroes">, <"Keep All Whole Digits">)
Format(x, "Currency", <currency code>, <width>|<width, decimal places>, <"Use
Thousands Separator">, < <<Use Locale(Boolean) >)
Format(x, datetime, <width>)
Format(x, ("Latitude DDD"|"Latitude DDM"|"Latitude DMS"|"Longitude
DDD"|"Longitude DDM"|"Longitude DDM"), width|<width, decimal places>,
("PUN"|"DIR"|"PUNDIR"))
Format(x, "Custom", Formula(), <width>)
Description

Converts the value x into the quoted format that you specify in the subsequent
arguments.
Returns

Returns the text that corresponds to the number in the specified format.
Arguments

See Using JMP for more information about the arguments. The arguments are also shown
in a data table column’s Column Info window.
Examples
Format( x, "Fixed Dec", 10, 2, "Use Thousands Separator");
Format( x, "Currency", "EUR", 20, <<Use Locale(0)); // ignores computer locale
Format( x, "m/d/y", 10 );
Format( x, "Precision", 10, 2, "Keep trailing zeroes", "Keep All Whole Digits"
);
Format( x, "Latitude DDD", "PUNDIR"); // "PUN" for punctuation, "DIR" for
direction, PUNDIR for both
Format( x, "Custom", Formula( Abs( value ) ), 15 );

Notes

– You must always precede the number of decimal places with the width.
– If the date format is unknown, an error is written to the log.

JSL Functions, Operators, and Messages
Date and Time Functions

81

Format Date(x, datetime, <width>)
Description

Converts the value of x into the quoted datetime that you specify in the second
argument. Format choices are those shown in the data table Column Info window.
Returns

Returns the number in the specified format.
Arguments

See Using JMP for more information about the arguments.
Example
Format Date( 22Feb2021, "yyyyQq" );
"2021Q1"

Hour(datetime, <"12"|"24">)
Description

Determines the hour supplied by the datetime argument.
Returns

Returns an integer representation for the hour part of the date-time value supplied.
Arguments
datetime The number of seconds since midnight, 1 January 1904. This can also be an

expression.
"12"|"24" Changes the mode to 12 hours (with am and pm). The default is 24-hour
mode.
HP Time()
Description

Returns a high precision time value (in microseconds). This function is only useful relative
to another HP Time() value. The time value represents the number of microseconds since
the start of the JMP session.
Notes

For less precise time values use Tick Seconds().
In Days(n)
Description

Returns the number of seconds per n days. Divide by this function to express seconds as
days.

Date and Time Functions

In Hours(n)
Description

Returns the number of seconds per n hours. Divide by this function to express seconds as
hours.
In Minutes(n)
Description

Returns the number of seconds per n minutes. Divide by this function to express seconds
as minutes.
In Weeks(n)
Description

Returns the number of seconds per n weeks. Divide by this function to express seconds as
weeks.
In Years(n)
Description

Returns the number of seconds per n years. Divide by this function to express seconds as
years.
Informat(string, format)
Parse Date(string, format)
Description

Parses a quoted string of a given quoted format and returns a date/time value. The
value is expressed as if surrounded by the As Date() function, returning the date in
ʺddMonyyyyʺ format.
Example
Informat( "07152000", "MMDDYYYY" );
15Jul2000

Notes

– To see the format options, open the Column Info window on a data table column, select
a date/time value for the format, and view the Input Format list.
– If the date format is unknown, an error is written to the log.
See Also

“As Date(x)”

JSL Functions, Operators, and Messages
Date and Time Functions

83

Is Leap Year(year)
Description

Returns 1 if the specified year is a leap year and 0 otherwise.
ISO Year(datetime)
Description

Returns the ISO year of the datetime supplied. ISO years correspond to ISO weeks; they
begin on the Monday of the first week that contains at least four days.
Long Date(date)
Description

Returns a locale-specific quoted string representation for the date supplied, formatted
like "Sunday, February 29, 2004" or "Wednesday, November 9, 2011".
MDYHMS(date)
Description

Returns a quoted string representation for the date supplied, formatted like "2/29/04
00:02:20".
Minute(datetime)
Description

Determines the minute supplied by the datetime argument, 0-59.
Returns

Returns an integer representation for the minute part of the date-time value supplied.
Month(date)
Description

Returns an integer representation for the month of the date that is supplied.
Nth Day of Week in the Month(datetime)
Description

Determines the day of the week of the datetime argument and how many instances of
that day of the week have occurred in the month of the datetime argument.
Returns

Returns an integer that represents the number of instances of the day of the week of the
datetime argument that have occurred in the month.

Date and Time Functions

Parse Date()
See “Informat(string, format)”.
Quarter(datetime)
Description

Returns the annual quarter of a datetime value as an integer 1-4.
Second(datetime)
Description

Determines the second supplied by the datetime argument.
Returns

Returns an integer representation for the second part of the date-time value supplied.
Argument

datetime Number of seconds since midnight, 1 January 1904. This can also be an
expression.
Short Date(date)
Description

Returns a quoted string representation for the date supplied in the format
MM/DD/YYYY.
Tick Seconds()
Description

Measures the time taken for a script to run, measured down to the 60th of a second.
Notes

For higher time value resolution (for example, microseconds) use the HP Time() function.
Time Of Day(datetime)
Description

Returns an integer representation for the time of day of the datetime supplied.
Today()
Description

Returns the current date and time expressed as the number of seconds since midnight, 1
January 1904. No arguments are available, but the parentheses are still necessary.
