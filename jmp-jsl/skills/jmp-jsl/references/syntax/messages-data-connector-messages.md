# Data Connector Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 379-380).

## Index (line numbers in this file)

- `<< Get` — L73
- `<< Get Available` — L75
- `<< Get Description` — L54
- `<< Get Driver` — L56
- `<< Get Metadata` — L77
- `<< Get Name` — L58
- `<< Get Path` — L63
- `<< Get Type` — L65
- `<< N Items` — L33
- `<< Next` — L35
- `<< Register` — L79
- `<< Remove` — L39
- `<< Set Description` — L67
- `<< Set Name` — L69
- `<< Show Contents` — L42
- `<< Unlock Class` — L44
- `Data Connector Registry()` — L90
- `Names Default To Here()` — L89
- `Path()` — L91
---

JSL Messages
Data Connector Messages

379

obj<<N Items
Returns the number of members (items) in the obj class object.
obj<<Next(quoted string)
Returns the quoted string representation of the name of the member (item) in the obj
class object that follows the member (item) specified by the quoted string. The members
(items) in the class object are sorted in alphabetical order.
obj<<Remove(<string|{stringList}>)
Removes the member (item) specified by the quoted string or quoted stringlist from
the obj class. You can remove multiple members (items) using a list of quoted strings.
obj<<Show Contents
Shows the contents of the obj class object in the log window.
obj<<Unlock Class(<quoted string|{stringList}>)
Unlocks the obj class object, or unlocks specific members (items) within the obj class
object. When a class object is unlocked, members (items) can be added, changed, or
removed. The quoted string or quoted stringlist specify a member (item) to unlock.
You can also specify a list of quoted strings to unlock multiple members (items).

Data Connector Messages
This section contains JSL messages for configurable data connectors.

Data Connector Metadata Messages
metadata<<Get Description()
Gets the data connector description.
metadata<<Get Driver()
Gets the data connector driver, if there is one.
metadata<<Get Name()
Gets the data connector name.

Data Connector Messages

metadata<<Get Path()
Gets the data connector path.
metadata<<Get Type()
Gets the data connector type.
metadata<<Set Description(description)
Sets the data connector description.
metadata<<Set Name(name)
Sets the data connector name.

Data Connector Registry Messages
dc<<Get(name)
Retrieves a data connector from the registry.
dc<<Get Available()
Retrieves a list of available data connectors in the registry.
dc<<Get Metadata(name)
Gets a data connector’s metadata from the registry.
dc<<Register(Path(path), <Name(name)>, <Description(description)>)
Description

Adds a data connector to the registry.
Required Arguments
path The path to register the data connector to.
name The name of the data connector.
Optional Arguments
description The description of the data connector.
Example
Names Default To Here( 1 );
Data Connector Registry() << Register(
Path( "$DOCUMENTS/my connector.jmpdc" ),
