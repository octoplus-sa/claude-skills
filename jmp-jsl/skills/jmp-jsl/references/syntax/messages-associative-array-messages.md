# Associative Array Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 376-376).

## Index (line numbers in this file)

- `<< First` — L30
- `<< Get Alpha` — L21
- `<< Get Contents` — L33
- `<< Get Default Value` — L37
- `<< Get Keys` — L35
- `<< Get Tri Alpha` — L25
- `<< Get Value` — L39
- `<< Set Alpha` — L23
---

Alpha Shape Messages

Alpha Shape Messages
For the following JSL messages, ashape stands for an alpha shape or a reference to one.
ashape <<Get Alpha
Returns the current alpha value.
ashape <<Set Alpha(alpha)
Sets the current alpha value and recomputes the triangulation.
ashape <<Get Tri Alpha
Returns the alpha values for each triangle.

Associative Array Messages
For the following JSL messages, map stands for an associative array or a reference to one.
map<<First
Returns the first key within map, or Empty() if map has no keys. Note that keys are
returned in lexicographical order.
map<<Get Contents
Returns a list of all key-value pairs within map.
map<<Get Keys
Returns a list of all the keys within map.
map<<Get Default Value()
Returns the implicit value of all absent keys, or Empty() if none has been set.
map<<Get Value(key)
Returns the value for the key within map.
