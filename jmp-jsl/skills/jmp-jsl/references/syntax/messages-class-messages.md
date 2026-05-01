# Class Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 377-378).

## Index (line numbers in this file)

- `<< Clone` — L49
- `<< Contains` — L51
- `<< Delete Class` — L54
- `<< Equal` — L59
- `<< First` — L61
- `<< Get Contents` — L64
- `<< Get Keys` — L67
- `<< Get Name` — L70
- `<< Get Value` — L72
- `<< Get Values` — L29
- `<< Insert` — L33
- `<< Lock Class` — L82
- `<< Next` — L37
- `<< Remove` — L40
- `<< Set Default Value` — L44
---

JSL Messages
Class Messages

377

map<<Get Values(<{keyList}>)
If no argument is provided, a list of all values within map is returned.
If a list of keys is provided, a list of the values corresponding to only those keys is
returned.
map<<Insert(key, value)
Inserts the key into map and assigns value to it. If key already exists in map, its value is
replaced by the new value given. This message is equivalent to the function Insert
Into.
map<<Next(key)
Returns the key following the given key within the map, or Empty() if map has no keys.
Note that keys are returned in lexicographical order.
map<<Remove(key)
Removes the key and value from map. This message is equivalent to the function Remove
From.

map<<Set Default Value(v)
Sets the implicit value of all absent keys. Any key added without a value is assigned this
value by default.

Class Messages
obj<<Clone
Returns a reference to a new class object that is a copy of the obj class object.
obj<<Contains(quoted string)
Returns 1 if the obj class object contains the specified quoted string expression, and 0
otherwise.
obj<<Delete Class
Deletes the obj class object.

Class Messages

obj<<Equal(classref)
Returns 1 if the classref class object is equal to the obj class object, and 0 otherwise.
obj<<First
Returns the quoted string representation of the name of the first member (item) in the obj
class object. The members (items) in the class object are sorted in alphabetical order.
obj<<Get Contents
Returns a list of members (items) in the obj class object. Each element in the list is a
two-item list that contains a key and an associated value.
obj<<Get Keys
Returns a list of keys within the obj class. Each key is a quoted string representation of the
name of a member (item) in the obj class object.
obj<<Get Name
Returns a quoted string representation of the name of the obj class object.
obj<<Get Value(key quoted string)
Returns the value of the specified member (item) within the obj class object. The quoted
key quoted string argument specifies the key to the member (item).
obj<<Get Values
Returns a list of values of the members (items) in the obj class object. Each element in the
list is the expression that represents the value of each member (item) in the class.
obj<<Insert(quoted string, value)
Inserts a member (item) into the obj class object. The quoted string argument is the
name of the member (item), and the value argument is the expression value of the
member (item).
obj<<Lock Class(<quoted string|{quoted stringList}>)
Locks the obj class object, or locks specific members (items) within the obj class object.
When a class object is locked, members (items) cannot be added, changed, or removed.
The quoted string or quoted stringlist arguments specify a member (item) to lock.
You can also specify a list of quoted strings to lock multiple members (items).
