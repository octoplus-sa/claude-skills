# Schedule Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 493-493).

## Index (line numbers in this file)

- `<< Clear Schedule` — L45
- `<< Close` — L47
- `<< Get Version` — L26
- `<< JMP Name To R Name` — L31
- `<< Restart` — L49
- `Echo()` — L24
---

JSL Messages
Schedule Messages

493

Returns

Void.
Optional Named Argument
Echo(Boolean) Echoes the R source lines to the JMP log.

rconn<<Get Version()
Gets the current version of R that is installed.
Returns

A vector of length 3 containing the R version number.
rconn<<JMP Name To R Name(name)
Maps a quoted JMP Name to its corresponding R Name using R variable name naming
rules.
Returns

A quoted string that contains the quoted R name.
Arguments

name A quoted string that specifies the name of a JMP variable to be sent to R.

Schedule Messages
This section contains JSL messages that apply to schedules.
Related Information
•
sch<<Clear Schedule()
Cancels all scheduled events.
sch<<Close()
Closes the scheduler.
sch<<Restart()
Restarts the scheduler after it was stopped from running all scheduled events.
