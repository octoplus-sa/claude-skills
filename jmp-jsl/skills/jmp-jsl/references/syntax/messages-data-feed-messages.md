# Data Feed Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 422-424).

## Index (line numbers in this file)

- `<< Close` — L51
- `<< Connect` — L53
- `<< Disconnect` — L55
- `<< EOL` — L57
- `<< Get Line` — L69
- `<< Get Lines` — L71
- `<< Print Queue` — L73
- `<< Queue Line` — L75
- `<< Restart` — L80
- `<< Set Script` — L82
- `<< Stop` — L84
- `<< To Journal` — L34
- `<< To Row State Column` — L38
- `<< To Script Window` — L40
- `<< Use Floating Window` — L44
- `<< Where` — L47
- `<< Write` — L86
- `<< Write Line` — L107
- `<< Write Lines` — L127
- `Connect()` — L95
- `Data Feed Messages()` — L32
- `Set Script()` — L100
- `Show()` — L102
---

Data Feed Messages (Windows Only)

dtf<<To Journal
Creates a Where clause from the current state of the data filter and appends it to the
current journal. If there is no current journal, a new journal is opened and the Where
clause is added to it.
dtf<<To Row State Column
Creates a row state column whose formula is the Where clause.
dtf<<To Script Window
Creates a Where clause from the current state of the data filter and appends it to the
current script window. If there is no current script window, a new script window is
opened and the Where clause is added to it.
dtf<<Use Floating Window(Boolean)
Sets whether the data filter window floats on top of its associated data table or behaves as
a normal window.
dtf<<Where(clause)
Sets a condition for selecting rows.

Data Feed Messages (Windows Only)
feed<<Close
Closes the data feed object and its window.
feed<<Connect(port settings)
Sets up port settings for the connection to the device.
feed<<Disconnect
Disconnects the device from the data feed queue but leaves the data feed object active.
feed<<EOL("CR", "LF", "CRLF")
Sets the line ending value used as a separator when parsing incoming lines of data. The
value is also used as the terminator in outgoing lines of data.
– "CR": ASCII character 13 (carriage return)

JSL Messages
Data Feed Messages (Windows Only)

423

– "LF": ASCII character 10 (line feed)
– "CRLF": Uses both CR and LF in sequence.
feed<<Get Line
Returns and removes one line from the data feed queue.
feed<<Get Lines
Returns as a list and removes all lines from the data feed queue.
feed<<Print Queue
Prints the internal queue of messages to the log window.
feed<<Queue Line(quoted string)
Sends one quoted string (or line) to the end of the data feed queue. Queue Line is
primarily useful for testing your script without requiring it to be attached to a device. You
can essentially simulate the data coming from the device to make sure the rest of your
code handles the values properly when itʹs really attached to a working device.
feed<<Restart
Restarts processing queued lines.
feed<<Set Script(script)
Assigns the script that is run each time a line of data is received.
feed<<Stop
Stops processing queued lines.
feed<<Write(quoted string)
Description

Sends a quoted string to the data feed device.
Example
/* Example - send a message to external device over the serial port to trigger
data messages. This can be used to send control messages to a sensor or
other attached device.*/
exfeed = Open Datafeed(
Connect( Port( "com1" ), Baud rate( 4800 ), Parity( "even" ), DataBits( 8 )
),

Data Feed Messages (Windows Only)

Set Script(
ex = exfeed << Get Line;
Show( ex );
)
);
exfeed << Write( "Ready" );

feed<<Write Line(quoted string)
Description

Sends a quoted string to the data feed device. If EOL has been set for the data feed, the
quoted strings are terminated by the specified EOL value. If EOL has not been set, the line
is terminated with CRLF.
Example
/* Send a message to external device over the serial port to trigger data
messages. This can be used to send control messages to a sensor or other
attached device.*/
exfeed = Open Datafeed(
Connect( Port( "com1" ), Baud rate( 4800 ), Parity( "even" ), DataBits( 8 )
),
Set Script(
ex = exfeed << Get Line;
Show( ex );
)
);
exfeed << Write Line( "Ready" );

feed<<Write Lines({quoted string1, quoted string2, quoted string3})
Description

Sends a list of quoted strings to the data feed device. If EOL has been set for the data
feed, the quoted strings are terminated by the specified EOL value. If EOL has not been
set, the line is terminated with CRLF.
Example
/* Send a message to external device over the serial port to trigger data
messages. This can be used to send control messages to a sensor or other
attached device.*/
exfeed = Open Datafeed(
Connect( Port( "com1" ), Baud rate( 4800 ), Parity( "even" ), DataBits( 8 )
),
Set Script(
ex = exfeed << Get Line;
Show( ex );
)
);
