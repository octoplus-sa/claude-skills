# Graphics Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 155-173).

## Index (line numbers in this file)

- `Add Color Theme()` — L92
- `Arc()` — L145
- `Arrow()` — L158
- `Back Color()` — L175
- `Char To Path()` — L191
- `Circle()` — L201
- `Color Theme()` — L97
- `Color To HLS()` — L232
- `Color To RGB()` — L255
- `Contour Function()` — L302
- `Contour()` — L277
- `Drag Line()` — L335
- `Drag Marker()` — L351
- `Drag Polygon()` — L364
- `Drag Rect()` — L386
- `Drag Text()` — L409
- `Fill Color()` — L424
- `Fill Pattern()` — L437
- `Fill()` — L717
- `Floor()` — L660
- `Get Color Theme Detail()` — L445
- `Get Color Theme Names()` — L455
- `Gradient Function()` — L471
- `Graph Box()` — L225
- `H Line()` — L503
- `H Size()` — L510
- `HLS Color()` — L537
- `Handle()` — L514
- `Heat Color()` — L519
- `In Path()` — L549
- `In Polygon()` — L560
- `J()` — L658
- `Level Color()` — L576
- `Line Style()` — L611
- `Line()` — L599
- `Marker Size()` — L632
- `Marker()` — L626
- `Mousetrap()` — L636
- `New Heat Image()` — L641
- `New Window()` — L677
- `Normal Contour()` — L679
- `Oval()` — L696
- `Path To Char()` — L724
- `Path()` — L703
- `Pen Color()` — L739
- `Pen Size()` — L743
- `Pick Color()` — L747
- `Pie()` — L769
- `Pixel Line To()` — L774
- `Pixel Move To()` — L780
- `Pixel Origin()` — L784
- `Pixel Path()` — L815
- `Pixel Text()` — L845
- `PixelRadius()` — L213
- `Polygon Area()` — L797
- `Polygon Centroid()` — L806
- `Polygon()` — L789
- `RGB Color()` — L894
- `Rect()` — L864
- `Remove Color Theme()` — L871
- `Reverse Gradient()` — L674
- `Scale Type()` — L672
- `Show Missing Color()` — L673
- `Show()` — L249
- `Text Color()` — L915
- `Text Font()` — L919
- `Text Size()` — L927
- `Text()` — L906
- `To()` — L779
- `Transparency()` — L937
- `True()` — L555
- `V Line()` — L945
- `V Size()` — L951
- `X Function()` — L955
- `X Origin()` — L960
- `X Range()` — L964
- `X Scale()` — L969
---

JSL Functions, Operators, and Messages
Graphics Functions

155

Graphics Functions
Add Color Theme({name, <flags>, {color}, <{position}>)
Description

Creates a custom color theme that you can apply to components such as markers, data
table rows, and treemaps. Add the color theme to the JMP Preferences by including Add
Color Theme(...) inside Preferences().
Returns

Null.
Required Arguments
name The quoted name of the color theme.
color Lists of RGB values. These values define the blocks in categorical color themes and

the gradients in continuous color themes. Each list of RGB values corresponds to a
slider in the preferences Color Themes window.
position An optional list of numbers between 0 and 1 with one position per color. Each
position corresponds to a slider in the preferences Color Themes window. If you omit
the position, the sliders are evenly spaced.
Optional Argument
flags A flag for the Continuous or Categorical color theme list and category of color.
Continuous, <Continuous>, Sequential
Continuous, <Continuous>, Diverging
Continuous, <Continuous>, Chromatic
Categorical, <Continuous>, Sequential
Categorical, <Continuous>, Diverging
Categorical, Qualitative
Categorical, <Continuous>, Chromatic

With the default JMP color themes, Sequential colors transition from left to right or right to
left. Diverging colors are lighter in the middle. Chromatic colors consist of blocks or
gradients of bright color. All categories except for Qualitative can be both continuous and
categorical.
If you omit the flag, the color is shown in the Continuous, Sequential and Categorical,
Sequential categories.
Examples

The following example creates a continuous color theme named Blue to Purple. The color
is in the Diverging category. RGB values are defined in the four lists.
Add Color Theme(
{"Blue to Purple", {"Continuous", "Diverging"}, {{0, 0, 255},
{57, 108, 244}, "white", {128, 0, 100}}} );

Graphics Functions

Notes

Any style except for Qualitative can be Continuous and Categorical at the same time. For
example, the Cool to Warm Diverging theme is in the Continuous and Categorical theme
lists. In JMP, select Preferences > Graphs to see examples.
To delete a color theme, use Remove Color Theme().
See Also

“Remove Color Theme(name|{name, <flags>, {color, ...}, <{position, ...}>}>)”
Arc(x1, y1, x2, y2, startangle, endangle)
Description

Inscribes an arc in the rectangle described by the arguments.
Returns

Null.
Arguments
x1, y1 The point at the top left of the rectangle

x2, y2 The point at the bottom right of the rectangle
startangle, endangle The starting and ending angle in degrees, where 0 degrees is 12
oʹclock and the arc or slice is drawn clockwise from startangle to endangle.
Arrow(<pixellength>, {x1, y1}, {x2, y2})
Description

Draws an arrow from the first point to the second point. The optional first argument
specifies the length of the arrow’s head lines (in pixels).
Returns

Null.
Required Arguments
{x1, y1}, {x2, y2} Two lists of two numbers that each specify a point in the graph.
Optional Argument

pixellength The length of the arrowhead in pixels.
Notes

The two points can also be enclosed in square brackets: Arrow(<pixellength>, [x1,
x2], [y1, y2]).
Back Color(name)
Description

Sets the color used for filling the graph’s background.

JSL Functions, Operators, and Messages
Graphics Functions

157

Returns

Null.
Argument
name A quoted color name or a color index (such as "red" or "3" for the color red).

Char To Path(path)
Description

Converts a path specification from a quoted string to a matrix.
Returns

A matrix.
Arguments

path A quoted string that contains the path specification.
Circle({x, y}, radius|PixelRadius(n), <...>, <"Fill">)
Description

Draws a circle centered at {x, y} with the specified radius.
Returns

Null.
Required Arguments
{x, y} A number that describes a point in the graph

radius The length of the circle’s radius in relation to the vertical axis. If the vertical axis is
resized, the circle is also resized.
PixelRadius(n) The length of the circle’s radius in pixels. If the vertical axis is resized,
the circle is not resized.
Optional Argument
"Fill" A positional argument indicating that all circles defined in the function are filled
with the current fill color. If "Fill" is omitted, the circle is empty.
Notes

The center point and the radius can be placed in any order. You can also add additional
center point and radius arguments and draw more than one circle in one statement. One
point and several radii results in a bull’s-eye. Adding another point still draws all previous
circles, and then adds an additional circle with the last radius specified. This means that
this code:
Graph Box(circle({20, 30}, 5, {50, 50}, 15))

results in three circles, not two. First, a circle with radius 5 is drawn at 20, 30. Second, a
circle with radius 5 is drawn at 50, 50. Third, a circle with radius 15 is drawn at 50, 50.

Graphics Functions

Color To HLS(color)
Description

Converts the color argument (including any JMP color) to a list of HLS values.
Returns

A list of the hue, lightness, and saturation components of color. The values range
between 0 and 1.
Argument

color A number from the JMP color index.
Example

The output from ColorToHLS() can either be assigned to a single list variable or to a list of
three scalar variables:
hls = Color To HLS( 8 );
{h, l, s} = Color To HLS( 8 );
Show( hls, h, l, s );
hls = {0.778005464480874, 0.509803921568627, 0.976};
h = 0.778005464480874;
l = 0.509803921568627;
s = 0.976;

Color To RGB(color)
Description

Converts the color argument (including any JMP color) to a list of RGB values.
Returns

A list of the red, green, and blue components of color. The values range between 0 and 1.
Argument

color A number from the JMP color index.
Example

The output from ColorToRGB() can either be assigned to a single list variable or to a list of
three scalar variables:
rgb = Color To RGB( 8 );
{r, g, b} = Color To RGB( 8 );
Show( rgb, r, g, b );
rgb = {0.670588235294118, 0.0313725490196078, 0.988235294117647};
r = 0.670588235294118;
g = 0.0313725490196078;
b = 0.988235294117647;

Contour(xVector, yVector, zGridMatrix, zContour, <messages>)
Description

Draws contours given a grid of values.

JSL Functions, Operators, and Messages
Graphics Functions

159

Returns

None.
Required Arguments

xVector The n values that describe zGridMatrix.
yVector The m values that describe zGridMatrix.
zGridMatrix An nxm matrix of values on some surface.
zContour The values for the contour lines.
Optional Messages

<<zColor(color, option) The colors to use for the contour lines.
<<"Fill"|"Fill Between"|"Fill Below"|"Fill Above" Specifies where the contour
fill appears.
<<Transparency(vector) Specifies the transparency level of the fill in a vector.
Contour Function(zExpr, xName, yName, (z|zMatrix), < <<xGrid(min, max,
incr)>, < <<yGrid(min, max, incr)>, < <<zColor(color, option)>, <
<<zLabeled>, < <<"Filled">, < <<"FillBetween">, < <<"Ternary">, <
<<Transparency(number|matrix))
Description

Draws sets of contour lines of the expression, a function of the two symbols. The z
argument can be a single value or an index or matrix of values.
Returns

None.
Arguments

zExpr Any expression (for example, Sine(y)+Cosine(x)).
xName, yName The values to use in the expression.
z|zMatrix A z-value or a matrix of z-values.
Optional Messages
<<xGrid, <<yGrid Defines a box, beyond which the contour lines are not drawn.
<<zColor Defines the color in which to draw the contour lines. The argument can be

either a scalar or a matrix but must evaluate to numeric.
<<zLabeled Labels the contours.
<<"Filled" Fills the contour levels using the current fill color.
<<"FillBetween" Fills only between adjacent contours using the current fill color. For nz
contours specified, this option fills nz-1 regions for the intervals between the nz values.
Using this option is recommended over using the <<Filled option.
<<"Ternary" Clips lines to be within the ternary coordinate system inside ternary plots.
<<Transparency(number|matrix) Sets the transparency level of the fill. A vector of
numbers between 0 and 1 are sequenced through and cycled for the z contours. This
option should be used only in conjunction with the <<FillBetween option.

Graphics Functions

Drag Line(xMatrix, yMatrix, <dragScript>, <mouseUpScript>)
Description

Draws line segments between draggable vertices at the coordinates given by the matrix
arguments.
Returns

None.
Required Arguments

xMatrix A matrix of x-coordinates.
yMatrix A matrix of y-coordinates.
Optional Arguments

dragScript Any valid JSL script. The script is run at drag.
mouseUpScript Any valid JSL script. The script is run at mouseup.
Drag Marker(xMatrix, yMatrix, <dragScript>, <mouseUpScript>)
Description

Draws draggable markers at the coordinates given by the matrix arguments.
Returns

None.
Arguments

xMatrix A matrix of x-coordinates.
yMatrix A matrix of y-coordinates.
dragScript Any valid JSL script. The script is run at drag.
mouseUpScript Any valid JSL script. The script is run at mouseup.
Drag Polygon(xMatrix, yMatrix, <dragScript>, <mouseupScript>)
Description

Draws a filled polygon with draggable vertices at the coordinates given by the matrix
arguments.
Returns

None.
Required Arguments

xMatrix A matrix of x-coordinates.
yMatrix A matrix of y-coordinates.
Optional Arguments

dragScript Any valid JSL script. The script is run at drag.
mouseUpScript Any valid JSL script. The script is run at mouseup.

JSL Functions, Operators, and Messages
Graphics Functions

161

Drag Rect(xMatrix, yMatrix, <dragScript>, <mouseupScript>)
Description

Draws a filled rectangle with draggable vertices at the first two coordinates given by the
matrix arguments.
Returns

None.
Required Arguments

xMatrix A matrix of two x-coordinates.
yMatrix A matrix of two y-coordinates.
Optional Arguments

dragScript Any valid JSL script. The script is run at drag.
mouseUpScript Any valid JSL script. The script is run at mouseup.
Notes

xMatrix and yMatrix should each contain exactly two values. The resulting coordinate
pairs should follow the rules for drawing a Rect(). The first point (given by the first value
in xMatrix and the first value in yMatrix) must describe the top, left point in the
rectangle. The second point (given by the second value in xMatrix and the second value
in yMatrix) must describe the bottom, right point in the rectangle.
Drag Text(xMatrix, yMatrix, string, <dragScript>, <mouseUpScript>)
Description

Draws the string (or all the items if a list is specified) at the coordinates given by the
matrix arguments.
Returns

None.
Arguments

xMatrix A matrix of x-coordinates.
yMatrix A matrix of y-coordinates.
string A quoted string to be drawn in the graph.
dragScript Any valid JSL script. The script is run at drag.
mouseUpScript Any valid JSL script. The script is run at mouseup.
Fill Color(name|color|rgbList)
Description

Sets the color used for filling solid areas.
Returns

None.

Graphics Functions

Arguments

name|color|rgbList The quoted color name, index, or list of RGB values.
Fill Pattern(name|mask|image)
Description

Sets the pattern for filled areas.
Arguments
name|mask|image The quoted color name, matrix of values between 0 and 1, or image

path.
Get Color Theme Detail(name)
Description

Returns a script for the specified color theme.
Example

The following example returns the script for the JMP default color theme:
Get Color Theme Detail( "JMP Default" );
{"JMP Default", 9221, {{212, 73, 88}, {61, 174, 70}, {66, 112, 221}...}}

Get Color Theme Names(<kind>)
Description

Returns a list of all color theme names or color themes of the specified kind. The kinds
include "Continuous", "Categorical", "Sequential", "Diverging", "Qualitative",
or "Chromatic".
Example

The following example returns all color themes:
Get Color Theme Names();
{"Green to Black to Red", "Green to White to Red", "White to Black"...}

The following example returns the diverging color themes:
Get Color Theme Names( "diverging" );
{"Green to Black to Red", "Green to White to Red", "Blue to Gray to Red"...}

Gradient Function(zExpr, xName, yName, [zLow, zHigh], zColor([colorLow,
colorHigh]), < <<xGrid(min, max, incr)>, < <<yGrid(min, max, incr)> <
<<Transparency(alpha|vector))
Description

Fills a set of rectangles on a grid according to a color determined by the expression value
as it crosses a range corresponding to a range of colors.

JSL Functions, Operators, and Messages
Graphics Functions

163

Required Arguments

zExpr Any expression (for example, Sine(y)+Cosine(x)).
xName, yName The values to use in the expression.
zLow, zHigh A matrix of low and high values (2 to 10).
zColor([colorLow, colorHigh]) The two colors that are blended together (4 is
green, 6 is orange).
Optional Messages
<<xGrid, <<yGrid Specifies a box, beyond which the gradients are not drawn.
<<zColor The color in which to draw the contour lines. The argument can be either a

scalar or a matrix but must evaluate to numeric.
<<Transparency(number|matrix) The transparency level of the fill. A vector of
numbers between 0 and 1 are sequenced through and cycled for the z contours.
Example
Gradient Function(Log(a * a + b * b),
a, b, [2 10],
zColor([4, 6]));

H Line(x1, x2, y)
H Line(y)
Description

Draws a horizontal line at y across the graph. If you specify start and end points on the
x-axis (x1 and x2), the line is drawn horizontally at y from x1 to x2. You can also draw
multiple lines by using a matrix of values in the y argument.
H Size()
Description

Returns the horizontal size of the graphics frame in pixels.
Handle(xPos, yPos, dragScript, mouseUpScript)
Description

Places draggable marker at coordinates given by xPos, yPos. The first script is executed at
drag and the second at mouseup.
Heat Color(x, < <<theme>)
Heat Color(x)
Description

Returns the JMP color that corresponds to n in the color ʺtheme".

Graphics Functions

Returns

An integer that is a JMP color.
Required Argument

x A value between 0 and 1.
Optional Message

theme A quoted color theme that is supported by Cell Plot. The default value is "Blue to
Gray to Red".
HLS Color(h, l, s)
HLS Color({h, l, s})
Description

Converts hue, lightness, and saturation values into a JMP color number.
Returns

An integer that is a JMP color number.
Arguments

Hue, lightness, and saturation, or a list containing the three HLS values. All values should
be between 0 and 1.
In Path(x, y, (pathMatrix|pathText))
Description

Determines it the point described by x and y falls in path.
Returns

True (1) if the point (x, y) is in the given path, False(0) otherwise.
Arguments
x and y The coordinates of a point.

pathMatrix|pathText Either a matrix or a quoted string describing a path.
In Polygon(x, y, xMatrix, yMatrix)
In Polygon(x, y, xyPolygon)
Description

Returns 1 or 0, indicating whether the point (x, y) is inside the polygon that is defined by
the xMatrix and yMatrix vector arguments.
xMatrix, yMatrix can also be combined into a two-column matrix (xyPolygon),
allowing you to use three arguments instead of four. Also, x and y can be conformable
vectors, and then a vector of 0s and 1s are returned based on whether each (x, y) pair is
inside the polygon.

JSL Functions, Operators, and Messages
Graphics Functions

165

Level Color(i)
Level Color(i, n)
Level Color(i, n, <theme>)
Level Color(i, <theme>)
Description

Assigns a JMP color to categorical data in a graphic.
Returns

An integer that is a JMP color.
Required Arguments

i An integer that is greater than or equal to 1 and less than or equal to the number of
categories specified by n.
n The number of categories.
Optional Argument

theme A quoted color theme from the Value Color list of the Column Properties window.
If not specified, the JMP Default color theme is applied.
Notes

When the second argument is a quoted character string and not n, then the second
argument determines the color theme.
Line({x1, y1}, {x2, y2}, ..., <<ValueSpace(Boolean))
Line([x1, x2, ...], [y1, y2, ...], <<ValueSpace(Boolean))
Description

Draws a line between points.
Arguments
{x1, y1}, {x2, y2}|[x1, x2, ...], [y1, y2, ...] Can be any number of lists of

two points, separated by commas or a matrix of x values and a matrix of y values.
<<ValueSpace(Boolean) Draws lines that follow the projection when the line represents
a movement of the underlying data, such as a bubble trail in a bubble plot. The Boolean
value can be a constant or an expression.
Line Style(name|number)
Description

Sets the line style used to draw the graph.
Argument

n Can be either a quoted style name or the style’s number:
– 0 or "Solid"

Graphics Functions

– 1 or "Dotted"
– 2 or "Dashed"
– 3 or "DashDot"
– 4 or "DashDotDot"
Marker(<rowState>, {x1, y1}, {x2, y2}, ...)
Marker(<rowState>, [x1, x2, ...], [y1, y2, ...})
Description

Draws one or more markers at the points described either by lists or matrices. The optional
rowState argument sets the type of marker.
Marker Size(n)
Description

Sets the size used for markers.
Mousetrap(dragScript, mouseUpscript)
Description

Captures click coordinates to update graph properties. The first script is executed at drag
and the second script at mouseup.
New Heat Image(matrix, <colorTheme>)
Description

Creates a heat map image based on a matrix and color theme or gradient.
Arguments

matrix A matrix of values. The function creates a heat map that has the same dimensions
as the input matrix.
colorTheme A color theme or set of gradient properties that define the mapping of
values to colors. The example below shows the use of a custom gradient.
Example
width = 256;
height = 256;
wstride = 16;
hstride = 16;
b = J( hstride, wstride, Random Normal() );
a = Transform Each( {z, {row, col}},
J( height, width, 0 ),
b[Floor( (row - 1) / hstride ) + 1,
Floor( (col - 1) / wstride ) + 1]

JSL Functions, Operators, and Messages
Graphics Functions

167

);
E1 = New Heat Image(
a,
gradient(
{Color Theme( "Blue To Gray To Orange" ),
Scale Type( "Standard Deviation" ),
Show Missing Color( "On" ),
Reverse Gradient( 1 )}
)
);
New Window( "test", Lineup Box( E1 ) );

Normal Contour(prob, meanMatrix, stdMatrix, corrMatrix, <colorsMatrix>,
<fill=x>)
Description

Draws normal probability contours for k populations and two variables.
Required Arguments

prob A scalar or matrix of probabilities.
meanMatrix A matrix of means of size k by 2.
stdMatrix A matrix of standard deviations of size k by 2.
corrMatrix A matrix of correlations of size k by 1.
Optional Arguments

colorsMatrix Specifies the color(s) for the k contour(s). The colors must be specified as
JSL colors (either JSL color integer values or return values of JSL Color functions such
as RGB Color or HLS Color).
fill=x Specifies the amount of transparency for the contour fill color.
Oval(x1, y1, x2, y2, <Fill(Boolean)>)
Oval({x1, y1}, {x2, y2}, <Fill(Boolean)>)
Description

Draws an oval inside the rectangle whose diagonal has the coordinates (x1, y1) and (x2,
y2). Fill is Boolean. If Fill is 0, the oval is empty. If Fill is nonzero, the oval is filled
with the current fill color. The default value for Fill is 0.
Path((pathMatrix|pathText), <Fill(Boolean)>)
Description

Draws a stroke along the given path. If a fill is specified, the interior of the path is filled
with the current fill color.

Graphics Functions

Required Arguments

pathMatrix An Nx3 matrix. If you don’t specify the path matrix, specify the path text.
pathText A quoted string that contains SVG code.
Optional Arguments

Fill(Boolean) Specifies whether a line is drawn (0) or the path is filled (1). The default
value is 0.
Notes

A path matrix has three columns, for x and y, and a flag. The flag value for each point can
be 0 for control, 1 for move, 2 for line segment, 3 for cubic Bézier segment, and any
negative value to close the path.
Path To Char(path)
Description

Converts a path specification from a matrix to a quoted string.
Returns

A quoted string.
Argument

path An Nx3 path matrix.
Notes

A path matrix has three columns, for x and y, and a flag. The flag value for each point can
be 0 for control, 1 for move, 2 for line segment, 3 for cubic Bézier segment, and any
negative value to close the path.
Pen Color(n)
Description

Sets the color used for the pen.
Pen Size(n)
Description

Sets the thickness of the pen in pixels.
Pick Color(<window title>, <name|index|RGBlist>)
Description

Creates a color picker, which enables the user to select a color to apply to graphs. The
operating system color picker lets users select a predefined color or create their own color.
You can also specify a default color in your script. If you omit the default color, Black is
selected.

JSL Functions, Operators, and Messages
Graphics Functions

169

Returns

The color that the user selected in the operating system’s color picker.
Arguments

window title The quoted title of the color picker window.
name The name of the default JMP color.
index The number of the default JMP color.
RGBlist The RGB values of the default color.
Pie(left, top, right, bottom, startAngle, endAngle)
Description

Draws a filled pie slice. The two points describe a rectangle, within which is a virtual oval.
Only the slice described by the start and end angles is drawn.
Pixel Line To(h, v)
Description

Draws a one-pixel-wide line from the current pixel location to the location given in pixel
coordinates. Set the current pixel location using the Pixel Origin() and Pixel Move
To() functions.
Pixel Move To(h, v)
Description

Moves the current pixel location to a new location given in pixel coordinates.
Pixel Origin(x, y)
Description

Sets the origin, in graph coordinates, for subsequent Pixel Line To() or Pixel Move
To() functions.
Polygon({x1, y1}, {x2, y2}, ...)
Polygon(xMatrix, yMatrix)
Description

Draws a filled polygon defined by the listed points.

Graphics Functions

Polygon Area({x1, y1}, {x2, y2}, ...)
Polygon Area(xMatrix, yMatrix)
Description

Calculates the area of the specified polygon.
Examples
area = Polygon Area( {0, 0}, {0, 10}, {10, 10}, {10, 0} );
area = Polygon Area( [10 20 30], [10 30 20] );

Polygon Centroid({x1, y1}, {x2, y2}, ...)
Polygon Centroid(xMatrix, yMatrix)
Description

Calculates the centroid of the specified polygon.
Examples
{cx, cy} = Polygon Centroid( {0, 0}, {0, 10}, {10, 10}, {10, 0} );
centroid = Polygon Centroid( [10 20 30], [10 30 20] );

Pixel Path(h, v, (path matrix|path text), <fill=Boolean)>, <scale=n>,
<orient={n, n})
Description

Draws a stroke along the given pixel-based path if the fill is 0, or paints the interior of the
path if the fill is not 0.
Required Arguments
h, v Specifies the horizontal and vertical position.

path matrix Contains three columns for h, v, and flags for each point in the path. The
flag values are 0 for control, 1 for move, 2 for line segment, 3 for cubic Bézier segment,
and are negative if the point also closes the path. Each flag (one for each point) can be 0,
1, 2 or 3, (or negative, if it closes the shape).
If you don’t specify the path matrix, specify the path text.
path text Supports SVG syntax. The path is scaled (scale) and translated about its
origin according to the optional parameters (fill and orient), with the orientation
specified in the axis space.
Optional Arguments
fill(Boolean) 0 fills the shape. 1 draws an empty shape.
orient Rotates the object. For example, an orientation of {Sqrt( 2 ), Sqrt( 2 )}

draws the shape on a 45-degree angle.
scale Sizes the object. For example, a scale of 1.0 draws the shape as it is defined; a scale
of 2.0 draws it twice as big; and a scale of 0.5 draws it half as big.

JSL Functions, Operators, and Messages
Graphics Functions

171

Pixel Text(<properties>, {h, v}, text, ...)
Description

Moves to the {h, v} pixel position and draws text that the quoted text argument specifies.
Required Arguments

h The horizontal pixel position.
v The vertical pixel position.
text The quoted string to display at the start and end of the pixels.
Optional Arguments
center justified Center justifies the text.
right justified Right justifies the text.
erased Omits pixels from the edges of the rectangle of text. The text is drawn over the

graph content in the background color, erasing the graph within the rectangle to make
the text more readable.
boxed Displays a box around the text.
counterclockwise Rotates the text counterclockwise.
clockwise Rotates the text clockwise.
Rect(left, top, right, bottom, <Fill(Boolean)>)
Rect({left, top}, {right, bottom}, <Fill(Boolean)>)
Description

Draws a rectangle whose diagonal has the coordinates (left, top) and (right, bottom).
Fill is Boolean. If Fill is 0, the rectangle is empty. If Fill is nonzero, the rectangle is
filled with the current fill color. The default value for Fill is 0.
Remove Color Theme(name|{name, <flags>, {color, ...}, <{position, ...}>}>)
Description

Removes a custom color theme from the global list, either by name or by the full color
theme object.
Required Arguments

name The quoted name of the color theme.
color The RGB values for the color.
Optional Arguments

flags A number that represents metadata such as whether the theme is continuous or
categorical. Run Get Color Theme Details("name") on the color theme and use the
flag that is returned.
position A number between 0 and 1. There is one number per color that indicates where
on the gradient that color is, where 0 is the beginning and 1 is the end.

Graphics Functions

Example
Remove Color Theme( {"Yellow Blue", 0, {{255, 255, 0}, {0, 0, 255}}, {0.0,
1.0}} );

RGB Color(r, g, b)
RGB Color({r, g, b})
Description

Converts red, green, and blue values into a JMP color number.
Returns

An integer that is a JMP color number.
Arguments

Red, green, and blue, or a list containing the three RGB values. All values should be
between 0 and 1.
Text(<properties>, ({x, y}|{left, bottom, right, top}), text)
Description

Draws the quoted string text at the given point, either the x and y axes or the left, bottom,
right, and top axes.
Properties can be any of several named arguments: Center Justified, Right
Justified, Erased, Boxed, Counterclockwise, Position, and named arguments. The
position, named arguments, and quoted strings can be added in any order. The position
and named arguments apply to all the strings.
Text Color(n)
Description

Sets the color for text strings.
Text Font(fontName, <size>, <bold italic underline strikeout>, <angle>)
Description

Sets the font for text strings. Use without arguments to get the current font properties.
Angle is in degrees clockwise.
Quote the font properties. To apply multiple properties, specify them together, as in "bold
italic".

Text Size(n)
Description

Sets the font size in points for text strings.

JSL Functions, Operators, and Messages
Graphics Functions

173

Transparency(alpha)
Description

Sets the transparency of the current drawing, with alpha between 0 and 1 where 0 is clear
(no drawing) and 1 is completely opaque (the default).
Notes

Not all operating systems support transparency.
V Line(x, <y1, y2>)
Description

Draws a vertical line at x across the graph. If you specify start and end points on the y-axis
(y1 and y2), the line is drawn vertically at x from y1 to y2. You can also draw multiple
lines by using a matrix of values in the x argument.
V Size()
Description

Returns the vertical size of the graphics frame in pixels
X Function(zExpr, yName, <Min(min), Max(max), Fill(Boolean), Inc(upper
bound))
Description

Draws a plot of the function as the yName is varied over the y-axis of the graph.
X Origin()
Description

Returns the x-value for the left edge of the graphics frame.
X Range()
Description

Returns the distance from the left to right edge of the display box. For example,
X Origin() + X Range() is the right edge.
X Scale(xMin, xMax)
Description

Sets the range for the horizontal scale. The default value for xMin is 0. The default value
for xMax is 100.
