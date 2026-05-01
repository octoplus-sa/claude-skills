# Date Time

*Source: [https://jsl.jmp.com/All%20Categories/Functions/Date%20Time.html](https://jsl.jmp.com/All%20Categories/Functions/Date%20Time.html)*

---

# [Date Time](#date-time)[](#date-time "Click to copy url")

### [Abbrev Date](#abbrev-date)[](#abbrev-date "Click to copy url")

**Syntax:** s = Abbrev Date( datetime, \<format\> )

**Description:** Returns an abbreviated locale-specific representation of a date-time value.

**JMP Version Added:** Before version 14

``` jsl
Abbrev Date( Today() );
```

### [As Date](#as-date)[](#as-date "Click to copy url")

**Syntax:** dt = As Date( datetime )

**Description:** Returns a date-time value marked internally as a date for output purposes.

**JMP Version Added:** Before version 14

``` jsl
As Date( Today() );
```

### [Date DMY](#date-dmy)[](#date-dmy "Click to copy url")

**Syntax:** z = Date DMY( d, m, y )

**Description:** Converts day, month, and year into a JMP date-time value, which is the number of seconds since 01Jan1904.

**JMP Version Added:** Before version 14

``` jsl
As Date( Date DMY( 15, 7, 2000 ) );
```

### [Date Difference](#date-difference)[](#date-difference "Click to copy url")

**Syntax:** delta = Date Difference( dt1, dt2, intervalName, \<alignment="start"\> )

**Description:** Returns the difference in intervals of two date/time values. Supported values of intervalName are "Year", "Quarter", "Month", "Week", "Day", "Hour", "Minute", "Second", and "Numeric". An alignment of "Start" includes full or partial intervals, while "Actual" only includes full intervals. An alignment of "Fractional" returns fractional differences, using averages for the duration of "Year", "Quarter", and "Month" intervals.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
Date Difference( Date DMY( 31, 1, 2015 ), Date DMY( 1, 3, 2015 ), "Month", "start" );
```

**Example 2**

``` jsl
Date Difference( Date DMY( 31, 1, 2015 ), Date DMY( 1, 3, 2015 ), "Month", "actual" );
```

**Example 3**

``` jsl
Date Difference( Date DMY( 31, 1, 2015 ), Date DMY( 1, 3, 2015 ), "Month", "fractional" );
```

### [Date Increment](#date-increment)[](#date-increment "Click to copy url")

**Syntax:** d = Date Increment( datetime, intervalName, \<incr=1\>, \<alignment="start"\> )

**Description:** Returns a new date-time value by adding incr number of intervals. Supported values of intervalName are "Year", "Quarter", "Month", "Week", "Day", "Hour", "Minute", "Second", and "Numeric". An alignment of "Start" truncates to the nearest interval prior to adding the increment, while "Actual" retains the full input date/time. An alignment of "Fractional" allows fractional incr values, using averages for the duration of "Year", "Quarter", and "Month" intervals.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
Date Increment( Today(), "Month", 100, "start" );
```

**Example 2**

``` jsl
Date Increment( Today(), "Month", 100, "actual" );
```

**Example 3**

``` jsl
Date Increment( Today(), "Month", 100, "fractional" );
```

### [Date MDY](#date-mdy)[](#date-mdy "Click to copy url")

**Syntax:** z = Date MDY( m, d, y )

**Description:** Converts month, day, and year into a JMP date value, which is the number of seconds since 01Jan1904.

**JMP Version Added:** Before version 14

``` jsl
As Date( Date MDY( 7, 15, 2000 ) );
```

### [Day](#day)[](#day "Click to copy url")

**Syntax:** d = Day( datetime )

**Description:** Returns the day of month part of a date-time value, 1 - 31.

**JMP Version Added:** Before version 14

``` jsl
Day( Today() );
```

### [Day Of Week](#day-of-week)[](#day-of-week "Click to copy url")

**Syntax:** d = Day Of Week( datetime )

**Description:** Returns the day of the week of a date-time value. Sunday = 1, ..., Saturday = 7.

**JMP Version Added:** Before version 14

``` jsl
Day Of Week( Today() );
```

### [Day Of Year](#day-of-year)[](#day-of-year "Click to copy url")

**Syntax:** d = Day Of Year( datetime )

**Description:** Returns the day of the year of a date-time value. January 1 is 1.

**JMP Version Added:** Before version 14

``` jsl
Day Of Year( Today() );
```

### [Days In Month](#days-in-month)[](#days-in-month "Click to copy url")

**Syntax:** v = Days In Month(year, month)

**Description:** Return the number of days in a given month.

**JMP Version Added:** 15

``` jsl
v = Days In Month( 2016, 2 );
```

### [Format](#format)[](#format "Click to copy url")

**Syntax:** s = Format( x, formatString, \<options\> ) s = Format( x, "Format Pattern", pattern, \<options\> )

**Description:** Returns the number in the specified format. Formats include items in the Column Info dialog, such as "Best" and "h:m:s". See Topic Help for other options, including p-value, currency, date and time, and geographic formats.

**JMP Version Added:** Before version 14

#### [Date Time](#date-time_1)[](#date-time_1 "Click to copy url")

``` jsl
Print( Format( Today(), "yyyyQq" ), Format( Today(), "m/d/y h:m" ) );
```

#### [Format Pattern](#format-pattern)[](#format-pattern "Click to copy url")

``` jsl
Print( Format( Today(), "Format Pattern", "<YYYY></><MM></><DD> <hh24><:><mm><:><ss>" ) );
```

#### [Full Precision](#full-precision)[](#full-precision "Click to copy url")

``` jsl
Show( Format( 88.54, "Best" ), Format( 88.54, "Best", "Full Precision" ) );
```

#### [Percent, Currency](#percent-currency)[](#percent-currency "Click to copy url")

``` jsl
pct = Format( 0.123, "Percent", 2 );
amt = Format( 123.4567, "Currency", "EUR", 2 );
result = "Revenue increase: " || amt || " or " || pct || ".";
```

### [Format Date](#format-date)[](#format-date "Click to copy url")

**Syntax:** s = Format( x, formatString, \<options\> ) s = Format( x, "Format Pattern", pattern, \<options\> )

**Description:** Returns the number in the specified format. Formats include items in the Column Info dialog, such as "Best" and "h:m:s". See Topic Help for other options, including p-value, currency, date and time, and geographic formats.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
Print( Format( Today(), "yyyyQq" ), Format( Today(), "m/d/y h:m" ) );
```

**Example 2**

``` jsl
Print( Format( Today(), "Format Pattern", "<YYYY></><MM></><DD> <hh24><:><mm><:><ss>" ) );
```

**Example 3**

``` jsl
pct = Format( 0.123, "Percent", 2 );
amt = Format( 123.4567, "Currency", "EUR", 2 );
result = "Revenue increase: " || amt || " or " || pct || ".";
```

### [HP Time](#hp-time)[](#hp-time "Click to copy url")

**Syntax:** t = HP Time()

**Description:** Returns a High Precision time value in microseconds. Only useful relative to another HP Time() value. The time value represents the number of microseconds since the start of the JMP session.

**JMP Version Added:** Before version 14

``` jsl
bt = HP Time();
Open( "$SAMPLE_DATA/Big Class.jmp" );
et = HP Time();
it = et - bt;
Show( it );
```

### [Hour](#hour)[](#hour "Click to copy url")

**Syntax:** hr = Hour( datetime, \<12\> )

**Description:** Returns the hours part of a date-time value, in 12-hour mode (12, 1 - 11) or 24-hour mode (0 - 23).

**JMP Version Added:** Before version 14

``` jsl
Hour( Today() );
```

### [ISO Year](#iso-year)[](#iso-year "Click to copy url")

**Syntax:** yr = ISO Year( datetime )

**Description:** Returns the ISO Year of a date-time value. ISO Years correspond to ISO Weeks; they begin on the Monday of the first week containing at least four days.

**JMP Version Added:** 16

``` jsl
ISO Year( Today() );
```

### [In Days](#in-days)[](#in-days "Click to copy url")

**Syntax:** y = In Days( \<x=1\> )

**Description:** Converts x from a number of days to the equivalent number of seconds.

**JMP Version Added:** Before version 14

``` jsl
In Days( 1.5 );
```

### [In Hours](#in-hours)[](#in-hours "Click to copy url")

**Syntax:** y = In Hours( \<x=1\> )

**Description:** Converts x from a number of hours to the equivalent number of seconds.

**JMP Version Added:** Before version 14

``` jsl
In Hours( 0.5 );
```

### [In Minutes](#in-minutes)[](#in-minutes "Click to copy url")

**Syntax:** y = In Minutes( \<x=1\> )

**Description:** Converts x from a number of minutes to the equivalent number of seconds.

**JMP Version Added:** Before version 14

``` jsl
In Minutes( 1 );
```

### [In Weeks](#in-weeks)[](#in-weeks "Click to copy url")

**Syntax:** y = In Weeks( \<x=1\> )

**Description:** Converts x from a number of weeks to the equivalent number of seconds.

**JMP Version Added:** Before version 14

``` jsl
In Weeks( 1 );
```

### [In Years](#in-years)[](#in-years "Click to copy url")

**Syntax:** y = In Years( \<x=1\> )

**Description:** Converts x from a number of years to the equivalent number of seconds.

**JMP Version Added:** Before version 14

``` jsl
In Years( 1 );
```

### [Informat](#informat)[](#informat "Click to copy url")

**Syntax:** dt = In Format( s, formatString, \< \<\<Use Locale(b=1)\>, \< \<\<Restrict \> ) dt = In Format( s, "Format Pattern", pattern, \< \<\<Use Locale(b=1)\> )

**Description:** Parses a string of a given format. If the format is a date-time format, the value is expressed as if surrounded by As Date(), returning the date in ddMonyyyy format. The optional \<\<Restrict used with the "Best" formatString only allows conversion using integer, decimal, and scientific formats.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
Informat( "07152000", "MMDDYYYY" );
```

**Example 2**

``` jsl
Informat( "07.15.2000", "Format Pattern", "<MM>.<DD>.<YYYY>" );
```

**Example 3**

``` jsl
Informat( "86.8287° W", "Longitude DDD" );
```

**Example 4**

``` jsl
Informat( "123.45%", "Percent" );
```

**Example 5**

``` jsl
Show(
    Informat( "1.23e4", "Best" ),
    Informat( "1.23e4", "Best", <<Restrict ),
    Informat( "1989-10-04", "Best" ),
    Informat( "1989-10-04", "Best", <<Restrict )
);
```

### [Is Leap Year](#is-leap-year)[](#is-leap-year "Click to copy url")

**Syntax:** v = Is Leap Year(year)

**Description:** Return whether a given year is a leap year.

**JMP Version Added:** 15

``` jsl
v = Is Leap Year( 2016 );
```

### [Long Date](#long-date)[](#long-date "Click to copy url")

**Syntax:** s = Long Date( datetime, \<format\> )

**Description:** Returns a long locale-specific representation of a date-time value.

**JMP Version Added:** Before version 14

``` jsl
Long Date( Today() );
```

### [MDYHMS](#mdyhms)[](#mdyhms "Click to copy url")

**Syntax:** s = MDYHMS( datetime, \<format\> )

**Description:** Returns a representation of a date-time value with the ordering: month, day, year, hour, minute, second.

**JMP Version Added:** Before version 14

``` jsl
MDYHMS( Today() );
```

### [Minute](#minute)[](#minute "Click to copy url")

**Syntax:** min = Minute( datetime )

**Description:** Returns the minutes part of a date-time value, 0 - 59.

**JMP Version Added:** Before version 14

``` jsl
Minute( Today() );
```

### [Month](#month)[](#month "Click to copy url")

**Syntax:** mon = Month( datetime )

**Description:** Returns the month part of a date-time value, 1 - 12.

**JMP Version Added:** Before version 14

``` jsl
Month( Today() );
```

### [Nth Day Of Week in the Month](#nth-day-of-week-in-the-month)[](#nth-day-of-week-in-the-month "Click to copy url")

**Syntax:** n = Nth Day Of Week in the Month( datetime )

**Description:** Returns an integer that represents the number of instances of the day of the week of the datetime argument that have occurred in the month. For example, November 28, 2019 is the 4th Thursday of the month, so the function returns 4.

**JMP Version Added:** 16

``` jsl
Nth Day Of Week in the Month( Date MDY( 11, 28, 2019 ) );
```

### [Parse Date](#parse-date)[](#parse-date "Click to copy url")

**Syntax:** dt = In Format( s, formatString, \< \<\<Use Locale(b=1)\>, \< \<\<Restrict \> ) dt = In Format( s, "Format Pattern", pattern, \< \<\<Use Locale(b=1)\> )

**Description:** Parses a string of a given format. If the format is a date-time format, the value is expressed as if surrounded by As Date(), returning the date in ddMonyyyy format. The optional \<\<Restrict used with the "Best" formatString only allows conversion using integer, decimal, and scientific formats.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
Informat( "07152000", "MMDDYYYY" );
```

**Example 2**

``` jsl
Informat( "07.15.2000", "Format Pattern", "<MM>.<DD>.<YYYY>" );
```

**Example 3**

``` jsl
Informat( "86.8287° W", "Longitude DDD" );
```

**Example 4**

``` jsl
Informat( "123.45%", "Percent" );
```

**Example 5**

``` jsl
Show(
    Informat( "1.23e4", "Best" ),
    Informat( "1.23e4", "Best", <<Restrict ),
    Informat( "1989-10-04", "Best" ),
    Informat( "1989-10-04", "Best", <<Restrict )
);
```

### [Quarter](#quarter)[](#quarter "Click to copy url")

**Syntax:** q = Quarter( datetime )

**Description:** Returns the quarter part of a date-time value, 1 - 4.

**JMP Version Added:** Before version 14

``` jsl
Quarter( Today() );
```

### [Second](#second)[](#second "Click to copy url")

**Syntax:** sec = Second( datetime )

**Description:** Returns the seconds part of a date-time value, including any fractional part, 0 - 60 exclusive.

**JMP Version Added:** Before version 14

``` jsl
Second( Today() );
```

### [Short Date](#short-date)[](#short-date "Click to copy url")

**Syntax:** s = Short Date( datetime, \<format\> )

**Description:** Returns a numeric (MM/DD/YYYY) locale-specific representation of a date-time value.

**JMP Version Added:** Before version 14

``` jsl
Short Date( Today() );
```

### [Tick Seconds](#tick-seconds)[](#tick-seconds "Click to copy url")

**Syntax:** t = Tick Seconds()

**Description:** Returns a time value in seconds, usually accurate to at least 1/60 of a second (a "tick"), depending on the computer. Only useful relative to another Tick Seconds() value.

**JMP Version Added:** Before version 14

``` jsl
t1 = Tick Seconds();
Open( "$SAMPLE_DATA/Big Class.jmp" );
t2 = Tick Seconds();
Round( t2 - t1, 3 );
```

### [Time Of Day](#time-of-day)[](#time-of-day "Click to copy url")

**Syntax:** sec = Time Of Day( datetime )

**Description:** Returns the time part of a date-time value, including any fractional seconds.

**JMP Version Added:** Before version 14

``` jsl
Format( Time Of Day( Today() ), "h:m:s" );
```

### [Today](#today)[](#today "Click to copy url")

**Syntax:** dt = Today()

**Description:** Returns the date-time value of the current moment.

**JMP Version Added:** Before version 14

``` jsl
As Date( Today() );
```

### [Week Of Year](#week-of-year)[](#week-of-year "Click to copy url")

**Syntax:** d = Week Of Year( datetime, \<rule=1\> )

**Description:** Returns the week of the year containing a date-time value using one of three rules. By default (rule 1), weeks start on Sunday with the first Sunday of the year being week 2. Week 1 will be a partial week or empty (as in 2006). For rule 2, the first Sunday is week 1, with previous days being week 0. For rule 3, the ISO week number is returned, where weeks start on Monday and week 1 is the first week of the year with four days in that year. With ISO weeks, it's possible for the first or last three days of the year to belong to the neighboring year's week number.

**JMP Version Added:** Before version 14

**Example 1**

``` jsl
Week Of Year( Today() );
```

**Example 2**

``` jsl
Show(
    Week Of Year( 01jan2012, 1 ),
    Week Of Year( 01jan2012, 2 ),
    Week Of Year( 01jan2012, 3 )
);
```

### [Year](#year)[](#year "Click to copy url")

**Syntax:** yr = Year( datetime )

**Description:** Returns the year part of a date-time value.

**JMP Version Added:** Before version 14

``` jsl
Year( Today() );
```

[ Previous](Constant.html "Constant") [Next ](Discrete%20Probability.html "Discrete Probability")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
