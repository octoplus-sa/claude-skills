# HTTP Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 174-174).

## Index (line numbers in this file)

- `Decode 64 Blob()` — L44
- `Encode 64 Blob()` — L48
- `XY Function()` — L18
- `Y Function()` — L25
- `Y Origin()` — L29
- `Y Range()` — L33
- `Y Scale()` — L38
---

HTTP Functions

XY Function(x(t), y(t), t, Min(min), Max(max), (Inc(bound)|Steps(min))
Description

Combines an expression of x(t) and y(t) to draw an x-y curve for the specified range of
parameter t. Each time t it is varied between Min and Max, the x and y expressions are
evaluated using the current value of t.
Note: Either Inc() or Steps() is needed if the default granularity misses details.
Y Function(yExpr, xName, <Min(min), Max(max), Fill(Boolean), Inc(bound)>)
Description

Draws a plot of the function as the xName is varied over the x-axis of the graph.
Y Origin()
Description

Returns the y-value for the bottom edge of the graphics frame.
Y Range()
Description

Returns the distance from the bottom to top edges of a display box. For example,
Y Origin() + Y Range() is the top edge.
Y Scale(yMin, yMax)
Description

Sets the range for the vertical scale. If you do not specify a scale, it defaults to 0, 100.

HTTP Functions
Decode 64 Blob(string)
Description

Decodes the quoted string using Base-64 encoding.
Encode 64 Blob(string)
Description

Encodes the quoted string using Base-64 encoding.
