# Display Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 91-125).

## Index (line numbers in this file)

- `<< Arcball` — L1310
- `<< Background Color` — L1305
- `<< Color` — L1302
- `<< Date` — L346
- `<< Max Date` — L353
- `<< Min Date` — L350
- `<< Perspective` — L1308
- `<< Run Script` — L1080
- `<< Save` — L1636
- `<< Set Function` — L357
- `<< Set Increment` — L1490
- `<< Set Max Size` — L1781
- `<< Set Script` — L317
- `<< Set Scroll Position` — L1396
- `<< Set Scrollers` — L1394
- `<< Set Sizes` — L835
- `<< Set Stretch` — L1779
- `<< Set Width` — L1459
- `<< Set Window Size` — L1393
- `<< SetWidth` — L1527
- `<< Show Arcball` — L1306
- `<< Show Time` — L347
- `<< Text` — L1303
- `<< Translate` — L1309
- `Align()` — L791
- `Alpha Shape()` — L207
- `Border Box()` — L211
- `Bottom()` — L234
- `Box Plot Seg()` — L242
- `Box()` — L804
- `Bubble Plot()` — L1208
- `Busy Light()` — L274
- `Button Box()` — L289
- `Calendar Box()` — L324
- `Cell Plot()` — L360
- `Check Box()` — L370
- `Col Box()` — L400
- `Col List Box()` — L427
- `Col Span Box()` — L483
- `Color()` — L1471
- `Combo Box()` — L507
- `Context Box()` — L522
- `Contour Seg()` — L533
- `Current Journal()` — L582
- `Current Report()` — L589
- `Current Window()` — L596
- `Data Filter Context Box()` — L600
- `Data Filter Source Box()` — L609
- `Data Table Box()` — L615
- `Data Table Col Box()` — L623
- `Data Table()` — L440
- `Destination()` — L1002
- `Dialog()` — L633
- `Excerpt Box()` — L637
- `Expr As Picture()` — L643
- `Expr()` — L657
- `File()` — L1070
- `Filter Col Selector()` — L662
- `Folder()` — L1058
- `Frame Size()` — L258
- `Get Project List()` — L681
- `Get Project()` — L667
- `Get Window List()` — L719
- `Get Window()` — L689
- `Global Box()` — L746
- `Graph 3D Box()` — L752
- `Graph Box()` — L257
- `Graph()` — L750
- `H Center Box()` — L779
- `H List Box()` — L786
- `H Scroll Box()` — L795
- `H Sheet Box()` — L805
- `H Splitter Box()` — L811
- `Hier Box()` — L853
- `Hist Seg()` — L859
- `Icon Box()` — L877
- `If Box()` — L916
- `If Seg()` — L924
- `Journal Box()` — L943
- `Left()` — L231
- `Line Seg()` — L948
- `Lines Seg()` — L954
- `Lineup Box()` — L958
- `List Box()` — L962
- `Location()` — L290
- `Marker Seg()` — L970
- `Matrix Box()` — L979
- `MaxItems()` — L452
- `MaxSelected()` — L449
- `MinItems()` — L453
- `Mouse Box()` — L986
- `MultiSelect()` — L1652
- `Names Default To Here()` — L1518
- `New Image()` — L1020
- `New Project()` — L1048
- `New Window()` — L344
- `Number Col Box()` — L1133
- `Number Col Edit Box()` — L502
- `Number Edit Box()` — L1143
- `On Change()` — L456
- `Open()` — L1039
- `Outline Box()` — L1158
- `Page Box()` — L1537
- `Page Break Box()` — L1162
- `Panel Box()` — L1166
- `Path()` — L1421
- `Picture Box()` — L1171
- `Platform()` — L1189
- `Plot Col Box()` — L1227
- `Poisson Quantile()` — L194
- `Poisson()` — L198
- `Poly Seg()` — L1232
- `Popup Box()` — L1245
- `Radio Box()` — L1259
- `Range Slider Box()` — L1264
- `Report()` — L1280
- `Rescale Slider()` — L1451
- `Right()` — L232
- `Row States()` — L1422
- `Scene Box()` — L1286
- `Script Box()` — L1313
- `Scroll Box()` — L1335
- `Set Width()` — L1450
- `Shape Seg()` — L1403
- `Sheet Box()` — L1427
- `Sides()` — L235
- `Size()` — L283
- `Sizes()` — L1211
- `Slider Box()` — L420
- `Slider()` — L1433
- `Source()` — L1001
- `Spacer Box()` — L1461
- `Spin Box()` — L1473
- `Splitter Box()` — L1497
- `State()` — L929
- `String Col Box()` — L414
- `String Col Edit Box()` — L1510
- `Tab Box()` — L1536
- `Tab List Box()` — L1569
- `Tab Page Box()` — L1572
- `Table Box()` — L413
- `Text Box()` — L1608
- `Text Edit Box()` — L1616
- `This Project()` — L1628
- `Tips()` — L473
- `Title Position()` — L1212
- `Top()` — L233
- `Transparency()` — L552
- `Tree Box()` — L1643
- `Tree Node()` — L1653
- `Triangulation()` — L1671
- `Type()` — L430
- `Use H Splitter Box()` — L1504
- `Using Set Tip()` — L475
- `V Center Box()` — L1685
- `V List Box()` — L1689
- `V Scroll Box()` — L1698
- `V Sheet Box()` — L1732
- `V Splitter Box()` — L1738
- `Vertical()` — L254
- `Web Browser Box()` — L1751
- `Width()` — L660
- `Window()` — L1787
- `Windows()` — L1003
- `Wrap List Box()` — L1801
- `X Scale()` — L559
- `X()` — L1209
- `Y Scale()` — L259
- `Y()` — L1210
- `YScale()` — L777
- `Yname()` — L762
---

JSL Functions, Operators, and Messages
Display Functions

91

– k

e 
P  X = k ;  = -------------k!
Arguments

k The number of events in a given time interval. k must be an integer.
lambda The shape parameter , which must be greater than 0 This is the mean of the
distribution.
Poisson Quantile(lambda, cumprob)
Description

Returns the smallest integer quantile for which the cumulative probability of the
Poisson(lambda) distribution is larger than or equal to cumprob.
Arguments

lambda The shape parameter , which must be greater than 0 This is the mean of the
distribution.
cumprob The cumulative probability of the quantile desired. cumprob must be between 0
and 1.

Display Functions
Alpha Shape(Triangulation())
Description

Returns the alpha shape for the given triangulation.
Border Box(<Left(pix)>, <Right(pix)>, <Top(pix)>, <Bottom(pix)>,
<Sides(Boolean)>, db)
Description

Constructs a bordered display box that contains another display box. Optional arguments
(Left, Right, Top, Bottom) add space between the border box and what it contains. The
other optional argument (Sides) draws borders around the border box on any single side
or combination of sides; draws the border in black or the highlight color; makes the
background transparent or white or erases the background of a display box that contains
it.
Returns

The display box.

Display Functions

Required Argument

db A display box object (for example, a text box or another border box).
Optional Arguments
Left(pix) An integer that measures pixels.
Right(pix) An integer that measures pixels.
Top(pix) An integer that measures pixels.
Bottom(pix) An integer that measures pixels.
Sides(pix) An integer that maps to settings for the display box.
Notes

The formula for deriving the integer for Sides is: 1*top + 2*left + 4*bottom + 8*right +
16*highlightcolor + 32*whitebackground + 64*erase. Thus, if you want to just draw a black
border on the top and bottom, 1+4 = 5. If you want that same box with a white background,
5+32 = 37.
Box Plot Seg(<data>, <frequency>, <weight>, <Vertical(Boolean)>)
Description

Returns a display seg that represents a box plot based on the passed x and y values.
Returns

The display box (a box plot).
Optional Arguments

data The data values within the box plot.
frequency The frequency values within the box plot.
weight The weights for observations on continuous Ys.
Vertical(Boolean) A vertical (1) or horizontal (0) box plot.
Example
win = New Window( "Box Plot Seg Example",
Graph Box(
Frame Size( 40, 180 ),
Y Scale( 0, 100 ),
Box Plot Seg(
[20, 30, 40], // data
[1, 1, 3], // frequencies
[1, 1, 1], // weights
1 // vertical
)
)
);

JSL Functions, Operators, and Messages
Display Functions

93

Busy Light(< <<Automatic(Boolean)>, <Size(x, y)>, < <<Disable>)
Description

Creates a rotating image to indicate a busy process.
Returns

A rotating image.
Optional Argument and Messages
<<Automatic(Boolean) Rotates the image.
Size(x, y) Specifies the size of the image in pixels.
<<Disable Hides the image.
Example
win = New Window( "Example",
blb = Busy Light( <<Automatic( 1 ), Size( 50, 50 ) ) );

Button Box(title, script, < <<Set Icon(path)>, < <<Set Icon
Location(left|right)>
Description

Constructs a button with the text title that executes script when clicked.
Returns

The display box (button box).
Required Arguments

title A quoted string or a string variable.
script A quoted string or a reference to a string that specifies a valid JSL script.
Optional Messages
<<Set Icon("path") Displays the image in the quoted pathname on the button. Most

common graphic formats are supported, such as GIF, JPG, PNG, BMP, TIF. Since the
title argument is optional, you can create a button with only a text title, with only an
icon, or with both a text title and an icon. In the last case, the icon is placed next to the
text title.
<<Set Icon Location("left"|"right") Allows the position of the icon on a button to
be either left or right of the text.
Example

The following example shows a simple button box. When the user clicks the button box,
"Pressed" is printed to the log.
win = New Window( "Simple Example",
ex = Button Box( "Press me" )
);
ex << Set Script( Print( "Pressed" ) );

Display Functions

Notes

Line-break characters are ignored in button boxes.
Calendar Box(title, < <<Date>, < <<Min Date>, < <<Max Date>, < <<Show Time>)
Description

Constructs a pop-up calendar with selectable days and time.
Returns

The display box (calendar box).
Required Argument

title A quoted string or a string variable.
Optional Messages
<<Date The currently selected date.
<<Min Date The earliest date that can be selected.
<<Max Date The latest date that can be selected.
<<Show Time The time that can be specified.
Example

The following example creates a calendar with October 5, 1989 initially selected. The
minimum date and maximum date are specified, so the user can select only dates in that
range.
New Window( "Calendar Box Example", cal = Calendar Box() );
date = Date MDY (10, 5, 1989);
cal << Date( date );
cal << Show Time( 0 ); // omit the time
/* earliest date that can be selected is 60 days before 10/5/1989
"start" truncates the value so the time is not included */
cal << Min Date( Date Increment(date, "Day", -60, "start" ) );

// latest date that can be selected is 60 days after 10/5/1989
cal << Max Date( Date Increment(date, "Day",

60, "start" ) );

cal << Set Function( Function( {this}, Print( Abbrev Date(this << Get Date())
) ) ); // print the abbreviated date to the log

Cell Plot(Y(column(s)), <X(column)>)
Description

Displays each value in a cell graph.

JSL Functions, Operators, and Messages
Display Functions

95

Check Box({list}, <script>, < <<Get(n)>, < <<Set(n, Boolean)>, < <<Get
Selected>, < <<Enable Item(n, Boolean)>, < <<Item Enabled(check box item)>)
Description

Constructs a display box to show one or more check boxes.
Returns

The display box (Check Box).
Required Argument

list A list of quoted strings or a reference to a list of strings.
Optional Argument

script An optional JSL script.
Optional Messages
<<Get(n) Returns 1 if the check box item specified by n is selected, or 0 otherwise.
<<Set(n, Boolean) Sets the check box item specified by n as either selected (1) or

cleared (0).
<<Get Selected Returns a list of quoted strings that contain the names of the check box
items that are selected.
<<Enable Item(n, Boolean) Sets the check box item specified by n as either enabled
(1) or disabled (0). The state of a disabled check box cannot be changed.
<<Item Enabled(check box item) Returns 0 or 1 depending on whether the specific
check box item is enabled.
Example

Create three check boxes labeled “one”, “two”, and “three”. The first check box is selected.
New Window( "Example", Check Box( {"one", "two", "three"}, <<Set( 1, 1 ) ) );

Col Box(title, display boxes)
Description

Returns a column box made up of the specified display boxes.
Arguments

title The quoted title of the column.
display boxes Display boxes that hold content within the column box.
Example
win = New Window( "Example",
exx = 1;
exy = 4;
exz = 8;
Table Box(
String Col Box( "strings", {"x", "y", "z"} ),
Col Box(
"boxes",

Display Functions

Slider Box( 0, 10, exx, Show( exx ) ),
Slider Box( 0, 10, exy, Show( exy ) ),
Slider Box( 0, 10, exz, Show( exz ) )
)
);
);

Col List Box(<Data Table(name)>, <"All"|"Character"|"Numeric">,
<width(pixels)>, <"Grouped">, <MaxSelected(n)>, <nLines(n)>, <MaxItems(n)>,
<MinItems(n)>, <On Change(expr)>, < <<Modeling
Type("Any"|"Continuous"|"Ordinal"|"Nominal"|Multiple
Response"|"Unstructured Text"|"Vector"|"None"|"Row State") >, < <<Set Data
Type(Any|Numeric|Character)>, <script>)
Description

Constructs a display box to show a list box that allows selection of data table columns.
Returns

The display box (Col List Box).
Optional Arguments
Data Table(name) The quoted name of the data table.
"All" | "Character" | "Numeric" Adds all columns of the current data table into the
list. Omitting "All" results in an empty col list box with the “optional” label. To display
“optional character”, specify "Character". To display “optional numeric”, specify
"Numeric".
width(pixels) Sets the width of the list box to pixels. pixels is a number that

measures pixels.
"Grouped" Displays grouped columns in the box.
MaxSelected(n) Sets whether only one item can be selected. For n<1, n is ignored.
nLines(n) Sets the length of the list box to n number of lines. n is an integer.
script A script.
MaxItems(n) A number that allows only n columns to be added to the list.
MinItems(n) A number that only requires at least n columns for the list. If n=2, the top
two slots in the col list box an initial display of “required numeric” (or whatever you set
the data type to be).
On Change(expr) Evaluates the expression when the selection in the list changes.
Dragging between two column list boxes that have this argument results in both
expressions being evaluated. The expression for the target being dragged is evaluated
first, then the expression for the source is evaluated.
Optional Messages
<<Set Tips({Tip text 1, Tip text 2, ...}) Quoted strings that set tool tips for

items in the list box. A quoted null string or an empty list results in no tips. A list

JSL Functions, Operators, and Messages
Display Functions

97

shorter that the list of items in the list box will use the last tip text for the remaining
items in the list and the list box.
<<Set Tip(Tip text) A quoted string that overrides any tool tips set using Set
Tips() function. If there is a tip set for the box, you cannot set tips for each individual
item.
Using Set Tip() with no arguments clears the list box tip and allows the individual
item tool tips to be displayed.
Notes

– The MaxSelected(n) argument only affects whether one or more than one item can be
selected. It does not enforce a limit greater than 1.
– Specialty modeling types can be used only in a role (determined by the platform) that
explicitly accepts columns of the same type.
Col Span Box(title, display box args)
Description

Creates spanned columns headers inside a table box. The top column header spans two
child column headers.
Returns

The display box (a Col Span Box).
Arguments

title The title that appears in the box.
display box args Display boxes.
Example
win = New Window( "Col Span Box",
<<Modal,
Table Box(
Col Span Box(
"Confidence Limits",
neb = Number Col Edit Box( "Upper limits", [0, 0] ),
Number Col Edit Box( "Lower limits", [0, 0] )
)
)
);

Combo Box({items <(tip string)>, ...}, <script>)
Description

Constructs a display box to show a drop-down list.
Returns

The display box (Combo Box).

Display Functions

Arguments

items The items that the user can select.
tip string A quoted string that specifies tooltip text.
script An optional JSL script.
Context Box(display box, ...)
Description

Defines a scoped evaluation context. Each Context Box is executed independently of each
other.
Returns

A display box.
Arguments

Any number of display boxes.
Contour Seg(Triangulation, [levels], <zColor([colors]|{colors}, <"Cycle
Colors"|"Interpolate Colors">)>, <"Fill"|"Fill Between"|"Fill Below"|"Fill
Above">, <Transparency([]|t)>)
Description

Returns a display seg that represents contours of a Triangulation.
Required Arguments
Triangulation The columns to include in the Triangulation.
[levels] A matrix of values that control the contour levels that are drawn.
Optional Arguments
zColor([colors]|{colors} Colors for each level, specified as a list or matrix.
"Cycle Colors"|"Interpolate Colors Cycle Colors" alternates the colors (for
example, red, green, red, green). With Interpolate Colors, the first contour is red,

and the last is green. The contours between smoothly blend the colors.
"Fill Below"|"Fill Between"|"Fill Above"|"Fill" "Fill Below" fills the region
below the lines. "Fill Between" fills only the middle region. "Fill Above" fills the
region above the lines.. "Fill" works like "Fill Above", but the default is to display
lines if no Fill options are specified.
Transparency([]|t) The transparency specified as a number or matrix.
Example
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
tri = Triangulation( X( :X, :Y ), Y( :POP ) );
{xx, yy} = tri << Get Points();
win = New Window( "Contour Seg Example",
g = Graph Box(
X Scale( Min( xx ) - .1, Max( xx ) + .1 ),

JSL Functions, Operators, and Messages
Display Functions

99

Y Scale( Min( yy ) - .1, Max( yy ) + .1 ),
Contour Seg(
tri,
[0, 400, 1000, 2000, 9000],
zColor( 5 + [64 32 0 16 48] ),
Transparency( [1, 1, 1, 1, 1] )
)
)
);

Notes

The triangulation is computed using the Xs, and the Y is a continuous variable defined at
each position. The [levels] in this case defines values of POP that are drawn as lines, one
line per level. If any Fill argument is specified, then the filled regions are [level1, level2],
[level2, level3], ..., [level-n].
Current Journal()
Description

Gets the display box at the top of the current (topmost) journal.
Returns

Returns a reference to the display box at the top of the current journal.
Current Report()
Description

Gets the display box at the top of the current (topmost) report window.
Returns

Returns a reference to the display box at the top of the current report window.
Current Window()
Description

Returns a reference to the current window.
Data Filter Context Box(display box)
Description

Returns a display box that defines the extent of the local data filters that a display tree
contains. Data filters and Data Filter Context Boxes can be arranged in a hierarchy and
shared among platforms or boxes that the Data Filter Context Boxes contain.

Display Functions

Data Filter Source Box(display box)
Description

Defines which graph is the “source” of the selection filter. Selected rows in reports that are
within the Data Filter Source box are included for analysis in the other reports that are
within a common Data Filter Context Box.
Data Table Box(data table)
Description

Returns a table box the represents the specified data table.
Example
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
win = New Window( "Example", Data Table Box( dt ) );

Data Table Col Box(column)
Description

Returns a column box that corresponds to the specified data table column.
Example
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
win = New Window( "Example",
Table Box( Data Table Col Box( :name ), Data Table Col Box( :height ) )
);

Dialog(contents)
Description
Dialog is deprecated. Use New Window() with the Modal argument instead.

Excerpt Box(report, subscripts)
Description

Returns a display box containing the excerpt designated by the report held at number
report and the list of display subscripts subscripts. The subscripts reflect the current
state of the report, after previous excerpts have been removed.
Expr As Picture(Expr(...), <Width(pixels)>)
Description

Converts expr() to a picture as it would appear in the Formula Editor.
Returns

Reference to the picture.

JSL Functions, Operators, and Messages
Display Functions

101

Required Argument
Expr(...) Place any valid JSL expression that can be displayed as a picture inside
expr().
Optional Argument
Width(pixels) Sets the width of the box to pix. pix is a number that measures pixels.

Filter Col Selector(<Data Table(name)>, <Width(pixels)>, <nLines(n)>,
<script>, <OnChange(expr)>)
Description

Returns a display box that contains a list of items. Control allows column filtering.
Get Project(title|index|display box|window)
Description

Returns a single project.
Examples

The following examples show how to get the window title of various projects.
Get Project( 1 ) << Get Window Title;
// first open project
Get Project( "My Project" ) << Get Window Title;
// first project named “My Project”
Get Project( display box ) << Get Window Title;
// parent project of the specified display box

Get Project List()
Description

Returns a list of all open projects.
Example
Get Project List() << Get Window Title;
// list of the titles of all open projects

Get Window(<Project(title|index|display box|window)>, <Type(string)>,
title|index|display box)
Description

Returns a reference to a specific open window by title, index, or display box. When run in
a project, Get Window() returns windows from the current project.
Optional Arguments
Project Specifies the title (a quoted string), index, display box, or window from another

project.

Display Functions

Type(string) To limit the search to particular types of windows, use the Type()
argument and one of these quoted strings: "Data Tables", "Journals", "Reports", or
"Dialogs".
Examples

The following examples show how to get the window title of various windows.
Get Window( 1 ) << Get Window Title;
// first window in the current project
Get Window( "Big Class" ) << Get Window Title;
// Big Class window in the current project
Get Window( ob ) << Get Window Title;
// parent window of specified display box in the current project
Get Window( Project(), 1 ) << Get Window Title;
// first window, no project (global scope)
Get Window( Project( myProject ), "Big Class" << Get Window Title;
// Big Class window in the specified project

Get Window List(<Project(title|index|display box|window),><Type(string)>)
Description

Returns a list of currently open windows. By default, Get Window List() returns
references to open windows in the current project. You can return an open window list
from something other than the current project by using the Project() argument. To limit
the search to particular types of windows, use the Type () argument and one of these
quoted strings: "Data Tables", "Journals", "Reports", or "Dialogs".
Optional Arguments
Project Specifies the title, index, display box, or window from another project.
Type To limit the search to particular types of windows, use the Type () argument and
one of these quoted strings: "Data Tables", "Journals", "Reports", or "Dialogs".
Examples
Get Window List() << Get Window Title;
// list of open windows in the current project
Get Window List( Type( "Reports" ) ) << Get Window Title;
// list of the titles of open reports in the current project
Get Window List( Project( 0 ), Type( "Reports" ) ); // positional arguments
// list of the titles of open reports outside of a project
Get Window List( 2 );
// second window list

JSL Functions, Operators, and Messages
Display Functions

103

Global Box(global)
Description

Constructs a box for editing global value directly.
Graph()
See “Graph Box(properties, script)”.
Graph 3D Box(properties)
Description

Constructs a display box with 3-D content.
Returns

The display box.
Arguments

properties Properties can include: Frame Size(x, y), Xname("title"),
Yname("title"), Zname("title").
Notes

This display box constructor is experimental.
Graph Box(properties, script)
Graph(properties, script)
Description

Constructs a graph with axes.
Returns

The display box (Graph Box).
Arguments

properties Named property arguments: Title("title"), XScale(low, high),
YScale(low, high), FrameSize(h, v), XName("x"), YName("y"), SuppressAxes.
script Any script to be run on the graph box.
H Center Box(<child box>)
Returns a display box that contains the optional child display box argument. The box is
centered in the horizontal space defined by the maximum size of that child display box and all
of the other siblings of the center box.

Display Functions

H List Box(<Align("center"|"bottom")>, display box, ...)
Description

Creates a display box that contains other display boxes and displays them horizontally.
Arguments
Align("center"|"bottom") Specify center or bottom alignment of the contents in the

list box. The contents are bottom aligned by default.
display box Any number of display box arguments can be contained in the list box.
H Scroll Box(<Size(h)>, display box)
Description

Returns a display box that positions a larger child box using a horizontal scroll bar.
Arguments
Size(h) The horizontal length of the scroll bar.
Notes

The flexible argument is deprecated. Use Set Stretch instead. See “V Scroll
Box(<Size(v)>, display box)” for an example.
H Sheet Box(<<Hold(report), display boxes)
Description

Returns a display box that arranges the display boxes provided by the arguments in a
horizontal layout. The <<Hold() message tells the sheet to own the report(s) that is
excerpted.
H Splitter Box(<Size(h, v)>, display box, ...)
Description

Returns a display box that arranges the display boxes provided by the arguments in a
horizontal layout (or panel). The splitter enables the user to interactively resize the panel.
Required Argument

display box Any number of display box arguments can be contained in the splitter box.
Optional Argument
Size(h, v) Specifies the size of the splitter box in pixels. This size is for the outer splitter

box. Inner display boxes are proportionately sized according to the width and height of
the outer splitter box.
Optional Messages
<<Size(n) Specifies the proportions of the last panel. <<Size(.25) resizes the last panel

to 25% the splitter box height (or width, for vertical splitter boxes).

JSL Functions, Operators, and Messages
Display Functions

105

<<Set Sizes({n, n}) Specifies the proportions of each panel.
db<<Set Sizes({.75, .25}) sizes the first panel to 75% and the second panel to 25%

of the splitter box height (or width, for vertical splitter boxes).
<<Close Panel(n, <Boolean>) Closes the panel that you specify. <<Close Panel(2)

closes the second panel. With three or more panels, you must include the second
Boolean value. That value indicates which panel expands to fill the space left by the
closed panel.
– <<Close Panel(2,0) closes the second panel; the following sibling takes the extra
space.
– <<Close Panel(2,1) closes the second panel; the preceding sibling takes the extra
space.
<<Open Panel(n, <Boolean>) Opens the panel that you specify. With three or more
panels, you must include the second Boolean value. Works similar to <<Close Panel
described above. The panels are initially opened. You use <<Open Panel only after
using <<Close Panel.
<<Get Sizes() Returns the proportions of each panel as a list.

Hier Box(text, Hier Box(...), ...)
Description

Constructs a node of a tree (similar to Diagram output) containing text. Hier Box can
contain additional Hier Boxes, allowing you to create a tree. The text can be a quoted
string or a Text Edit Box.
Hist Seg([data], <[freq column]>, <[weight column]>, <Vertical(Boolean)>,
<Row States()>
Description

Returns a histogram seg.
Required Argument

data The data in matrix format.
Optional Arguments

freq column The frequency column in matrix format.
weight column The weight column in matrix format.
Vertical(Boolean) Displays the histogram vertically by default (or if set to 1). Display
the histogram horizontally by setting the value to 0.
Row States Specifies a data table reference or row states.

Display Functions

Icon Box(name)
Description

Constructs a display box containing an icon, where the argument is a name such as
Popup
Nominal

, Locked

, Labeled

, or Ordinal

, Sub

, Excluded

, Hidden

, Continuous

,

. The argument can also be a path to an image.

Argument

name A quoted string that is the name of a JMP icon or the path to an icon.
Example
Icon Box( "Nominal" ) constructs a display box that contains the Nominal icon.
Icon Box( "$SAMPLE_IMAGES/pi.gif" ) inserts the pi.gif sample image.

Notes

– Some icons are used on both Windows and Apple macOS. Other icons are platform
specific.
– Consider installing the Built-In JMP Icons add-in. The add-in lets you view icons
interactively and see what they look like in different contexts. Download the add-in
from https://community.jmp.com/t5/JMP-Add-Ins/Built-In-JMP-Icons/ta-p/42251.
If Box(Boolean, display boxes)
Description

Constructs a display box whose contents are conditionally displayed.
Arguments

Boolean 1 displays the display boxes inside the If Box. 0 does not display them.
display boxes Any display box tree.
If Seg(<State(Boolean)>)
Description

Returns a display seg that shows or hides display seg children.
Arguments
State(Boolean) Determines whether the display seg children are shown (1) or hidden

(0).
Example
lines = [30 20 80 70, 10 90 90 10, 40 20 60 30];
win = New Window( "Lines Seg Example",
g = Graph Box( If Seg( true, <<Append( Lines Seg( lines ) ) ) )
);

JSL Functions, Operators, and Messages
Display Functions

107

Journal Box(string)
Description

Constructs a display box that displays the quoted string. We recommend that you do not
generate the journal text by hand.
Line Seg(x, y, <Row States(dt|dt, [rows]|dt, {{rows}, ...}|{row states})>,
<Sizes(s)>)
Description

Creates a display seg of connected line segments for the given x and y values. The optional
third argument enables row state assignments from either a data table or independently.
Lines Seg([x1 y1 x2 y2, ...])
Description

Returns a display seg with a sequence of line segments for the given x and y values.
Lineup Box(<nCol(n)>, <Spacing(pixels, <vspace>), display boxes, ...)
Description

Constructs a display box to show an alignment of boxes in n columns.
List Box({item, ...}, <Width(pixels)>, <maxSelected(n)>, <nLines(n)>,
<script>)
Description

Creates a display box to show a list box of selection items (quoted strings). The argument
can be a list of two-item lists containing the item name and a quoted string that specifies
the modeling type or sorting order. Item names are case sensitive by default. The icon
appears next to the corresponding item in the list box.
Marker Seg(x, y, <Row States(dt|dt, [rows]|dt, {{rows}, ...}|{row states})>,
<Sizes(s)>)
Description

Creates a display seg with markers for all of the x and y values. The optional third
argument enables row state assignments from either a data table or independently.

Display Functions

Matrix Box(x)
Matrix Box(matrix, < <<Column Names(col1, col2, ...)>, < <<Row Names(row1,
row2, ...)>)
Description

Displays the matrix given in the usual array form. Column and row names are quoted
strings.
Mouse Box(display box arguments)
Description

Returns a box that can make JSL callbacks for dragging and dropping, marking, or clicking
and tracking mouse actions.
Arguments

display box arguments Specifies the object that the user interacts with, such as a Text
Box or Button Box. See the Scripting Index in the Help menu.
Move to Project(<Source(project)|Destination(project)>, <Windows({list of
windows to move})>)
Description

Moves one or more windows into a project or out of a project, or between projects.
Arguments
Source(project) The project containing the windows that you want to move.
Destination(project) The project to which you want to move the windows.
Windows({list of windows to move}) A list of windows to move to the project. If

omitted, all windows will be moved. Note that the data table and all of its dependent
reports will be moved. However, you need to specify only the data table name or report
name in the windows argument to move it.
Example
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
report = dt << Run Script( "Bivariate" );
project = New Project();
// move the report and data table to a new project
Move to Project( Destination( project ), Windows( {report} ) );

JSL Functions, Operators, and Messages
Display Functions

109

New Image()
New Image(width, height)
New Image(filepath)
New Image(Open(url) )
New Image(picture)
New Image(matrix)
New Image(rgb|r|rgba, {matrix, ...})
Description

Creates a new image which can then be edited using JSL. Valid formats are png, bmp, jpeg,
jpg, tiff, tif, and gif.
Returns

An image.
Arguments

All argument sets are optional, but all arguments within each set are required.
width, height Sets the width and height of the image in pixels.
filepath The quoted filepath to an image.
Open(url) Opens the image at the specified URL path.
picture A JSL picture object.
matrix The image as a matrix of JSL color pixels.
rgb|r|rgba, {matrix, ...} Specifies the channels ("rgb", "r", or "rgba") and
provides a matrix of values (0.0-1.0) for each channel. Examples:
New Image( "r", [r matrix] );
New Image( "rgb", {[r matrix], [g matrix], [b matrix]} );
New Image( "rgba", {[r matrix], [g matrix], [b matrix], [a matrix]} );

New Project(arguments)
Description

Creates a project using the specified script.
Arguments
<<Add Bookmarks({<File(path)>, <Folder(path, Expanded(Boolean)>)>,
<Group(name, <Expanded(Boolean)>, {contents}>) Creates bookmarks for

frequently used files in the project. The argument is a list of bookmark items, each of
which is specified using File(), Folder(), or Group(). Group() accepts File(),
Folder(), and Group() as children.
<<Reset Layout Sets the project to use the default layout.
<<Run Script Specifies the data tables and reports that appear in the project.

Display Functions

<<Save(<path>) Saves the project. Include a quoted path and file name to save the
project to a specific location. Save As is an alias.
<<Set Bookmarks({<File(path)>, <Folder(path, Expanded(Boolean)>)>,
<Group(name, <Expanded(Boolean)>, {contents}>) Sets the bookmarks for the

project. The argument is a list of bookmark items, each of which is specified using
File(), Folder(), or Group(). Group() accepts File(), Folder(), and Group() as
children.
<<Set Layout Sets the window layout of the project.
<<Show Bookmarks Shows or hides the bookmarks.
<<Show Log Shows or hides the log.
<<Show Window List Shows or hides the Window List.
Example

The following example creates a project from BigClass.jmp and two reports.
project = New Project();
project << Run Script(
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Run Script( "Bivariate" );
dt << Run Script( "Distribution" );
);

New Window(title, <optional arguments>, displayBox | script)
Description

Creates a new window with the required, quoted title.
Required Arguments
title The title of the window to display.
displayBox Any display box.
script The script to display. Valid only with Type("Script").
Optional Arguments
<<Type ("Report" | "Dialog" | "Modal Dialog" | "Journal" | "Launcher" |
"Script")

Creates a window of the specified type. If not specified, a ʺReportʺ is created. A
window of Type("Modal Dialog") halts execution until dismissed.
<<Return Result Changes the window’s return value when it closes to match that of the
deprecated Dialog() function. Valid only with Type("Modal Dialog").
<<On Open(expr) Runs expr when the window is created. Valid only with Type("Modal
Dialog").
<<On Close(expr) Runs expr when the window is closed. If the expression returns
false, the window does not close. Returns 0 if the window fails to close.

JSL Functions, Operators, and Messages
Display Functions

111

<<On Validate(expr) Runs expr when the OK button is clicked. If the expression

returns True, the window is closed. Otherwise, the window remains open. Valid only
with Type("Modal Dialog").
<<Show Menu(Boolean) Shows or hides the menu bar. The default value is 1. Valid only
with Type("Report"). Windows only.
<<Show Toolbars(Boolean) Shows or hides the toolbar. The default value is 1. Valid
only with Type("Report"). Windows only. Right-click in the menu area to customize
which toolbars are shown. Your selections are remembered across JMP sessions.
<<Suppress AutoHide(Boolean) Suppresses or uses the auto-hide feature for menus
and toolbars. The default value is 1. Windows only. Valid only with Type("Report").
<<Window View("Visible" | "Invisible") Using the value ʺInvisibleʺ is valid for all
window types except ʺModal Dialogʺ.
<<Size Window(width, height) Creates a new window of the specified width and
height, in pixels.
Notes

In data tables, On Open (or OnOpen) scripts that execute other programs are never run. Set
the Evaluate OnOpen Scripts preference to control when the script is run.
Dialog() is deprecated. Instead, use New Window() with Type("Modal Dialog").

Number Col Box(title, numbers)
Description

Creates a column named title (a quoted string) with numeric entries given in list or
matrix form.
Number Col Edit Box(title, {numbers}|[numbers])
Description

Creates a column named title (a quoted string) with numeric entries given in list or
matrix form. The numbers can be edited.
Number Edit Box(initial value, <width>)
Description

Creates an editable number box that initially contains the initial value argument.
Returns

The display box object.
Argument

initial value Any number to use as the initial value. If you use a date or time format,
a date and time selector window is created.
<width> Sets the width of the box in characters.

Display Functions

Outline Box(title, display box, ...)
Description

Creates a new outline named title (a quoted string) containing the listed display boxes.
Page Break Box()
Description

Creates a display box that forces a page break when the window is printed.
Panel Box(title, display box)
Description

Creates a display box labeled with the quoted string title that contains the listed display
boxes.
Picture Box(Open(picture), format)
Description

Creates a display box that contains a graphics picture object.
Returns

A reference to the display box.
Argument
Open(picture) Opens the directory that contains the picture.

format Specifies the graphic file format. Specifying the format opens the picture in JMP.
If you omit this argument, the picture opens in the default graphics program. Valid
formats are the quoted strings "png", "bmp", "jpeg", "jpg", "tiff", "tif", and
"gif".
Example
New Window( "Example",
Picture Box( Open( "$SAMPLE_IMAGES/pi.gif", gif ) ) );

Platform(data table, script)
Description

Evaluates the specified script in the context of the specified data table.
Returns

The resulting display box for embedding in a display tree.
Example
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
win = New Window( "Platform example",
H List Box(

JSL Functions, Operators, and Messages
Display Functions

113

Platform(
dt,
Bubble Plot(
X( :weight ),
Y( :height ),
Sizes( :age ),
Title Position( 0, 0 )
)
),
Platform(
dt,
Bubble Plot(
X( :weight ),
Y( :age ),
Sizes( :height ),
Title Position( 0, 0 )
)
)
)
);

Plot Col Box(title, numbers)
Description

Returns a display box labeled with the quoted string title to graph the numbers. The
numbers can be either a list or a matrix.
Poly Seg(x values, y values)
Description

Returns a display seg that represents a polygon with vertices based on the x values and
y values.
Example
x = [10, 50, 90];
y = [10, 90, 10];
win = New Window( "Poly Seg Example",
g = Graph Box( Poly Seg( x, y ) ) );
frame = g[FrameBox( 1 )];
seg = (frame << Find Seg( "Poly Seg" ));

Popup Box({command1, script1, command2, script2, ...})
Description

Creates a red triangle menu. The single argument is an expression yielding a list of an
even number of items alternating between the quoted command string and the expression

Display Functions

that you want evaluated when the command is selected. If the command is an empty
string, a separator line is inserted.
Notes

Pressing ALT and right-clicking the red triangle menu opens a window with check boxes
for the commands.
Radio Box({item, ...}, <script>)
Description

Constructs a display box to show a set of radio buttons. The items are quoted strings. The
optional script is run every time a radio button is selected.
Range Slider Box(minValue, maxValue, lowVariable, highVariable, script)
Description
Range Slider Box() returns a display box that shows a range slider control that ranges

from minValue to maxValue. As the two sliders’ positions change, their values are placed
into lowVariable and highVariable, and the script is run.
Returns

The display box (Range Slider Box).
Arguments

minValue, maxValue Numbers that set the minimum and maximum value the slider
represents.
lowVariable The variable whose value is set and changed by the lower slider.
highVariable The variable whose value is set and changed by the upper slider.
script Any valid JSL commands that are run as the slider is moved.
Report(obj)
Description

Returns the display tree of a platform obj. This can also be sent as a message to a platform:
obj<<Report.

Scene Box(x size, y size)
Description

Creates an x-sized by y-sized scene box for 3-D graphics.
Scene Display List
Description

Returns a display list for 3-D graphics.

JSL Functions, Operators, and Messages
Display Functions

115

Example
ex = Scene Display List();
ex << Color( .9, .9, .9 );
ex << Text( center, middle, .3, "Hello World" );
exScene = Scene Box( 600, 600 );
exScene << Background Color( 0 );
exScene << Show Arcball( always );
New Window( "See HelloWorld.jsl in sample scripts", exScene );
exScene << Perspective( 45, .2, 20 );
exScene << Translate( 0.0, 0.0, -4.5 );
exScene << Arcball( ex, 1.5 );
exScene << Update;

Script Box(<script>, <language>, <width>, <height>)
Description

Constructs an editable box that contains the quoted string script. The editable box is a
script window and can both be edited and run as JSL.
Optional Arguments

script A quoted string that appears in the script box.
language A quoted string that provides syntax highlighting for the specified language.
Valid languages are "JSL", "Text", "SAS", "SAS Output", "SASLog", "R", "MATLAB",
"JavaScript", "C", "SQL", "Python", "JSON", and "XML".
width An integer that sets the width of the script box.
height An integer that sets the height of the script box.
Example
// JSON
New Window( "JSON",
Script Box(
"{\!"a\!":1,\!"b\!":\!"test\!"}",
"JSON"
)
);

Scroll Box(<Size(h,v)>, display box, ...)
Description

Creates a display box that positions a larger child box using scroll bars.
Returns

A reference to the scroll box object.
Required Argument

display box Any number of display box arguments can be contained in the scroll box.

Display Functions

Optional Argument
Size(h,v) The h and v arguments specify the size of the box in pixels.
Notes

You can send a scroll box object a message to set the background color:
<<Set Background Color( {R, G, B} | <color> )

The Flexible argument is deprecated. Use the Set Stretch message instead. See “V
Scroll Box(<Size(v)>, display box)” for an example.
You can set the Boolean flags for horizontal (h) and vertical (v) scrolling to enable (1) or
disable (0) the scroll bars. If scrolling is disabled in a given direction, the Scroll Box will
behave as a regular container in that direction.
<<Set Scrollers (h, v)

To return the flags for scrolling, use the following message:
<<Get Scrollers

To set the horizontal (h) and vertical (v) positions (in pixels) for the scrollers on the scroll
bar:
<<Set Scroll Position (h,v)

To return the flags for scroll position, use the following message:
<<Get Scroll Position

To return the maximum positions for horizontal and vertical scrolling, use the following
message:
<<Get Scroll Extents

Example

The following example shows a window containing a scroll box with the specified
settings.
win = New Window( "Example",
sb = Scroll Box(
Size( 150, 75 ),
List Box(
{"First Item", "Second Item",
"Third Item", "Fourth Item",
"Fifth Item"},
width( 200 ),
max selected( 2 ),
nLines( 6 )
)
)
);
win << Set Window Size( 300, 200 );
sb << Set Scrollers( 1, 1 ); // enable both scroll bars
// position the scrollers on the scroll bar
sb << Set Scroll Position( 0, 20 );

JSL Functions, Operators, and Messages
Display Functions

117

Shape Seg( {Path(path), ...}, <Row States(dt|dt,[rows]|dt,{{rows}, ...}|{row
states})>)
Description

Returns a display seg with a collection of shapes.
Required Argument
Path Specifies the path with an Nx3 matrix or with a text representation. A path matrix

has three columns for x, y, and flags for each point in the path. The flag values are 0 for
control, 1 for move, 2 for a line segment, 3 for a cubic Bézier segment, and are negative
if the point also closes the path. Path text supports SVG syntax.
Optional Arguments
Row States Specifies a data table reference and optionally rows or the actual row state.
Example
win = New Window( "Shape Seg Example",
Graph Box(
Shape Seg(
{Path( [10 10 1, 10 70 0, 70 70 0, 70 10 -3] ),
Path( "M20,20 C20,60 60,60 60,20 Z" )},
Row States( {Selected State( 1 ), Color State( "red" )} )
)
)
);

Sheet Box(<<Hold(rpt), display box, ...)
Description

Returns a display box that can organize other display boxes vertically or horizontally.

Slider Box(minValue, maxValue, variable, script, <Set Width(n)>, <Rescale
Slider(min, max)>)
Description

Creates an interactive slider control.
Returns

The display box (Slider Box).
Required Arguments
minValue, maxValue Numbers that set the minimum and maximum value the slider

represents.
variable The variable whose value is set and changed by the slider box.
script Valid JSL commands that are run as the slider box is moved.

Display Functions

Optional Arguments
Set Width(n) Specifies the width of the slider box in pixels.
Rescale Slider(minValue, maxValue) Resets the maximum and minimum values

for the slider box.
Notes

You can send Set Width and Rescale Slider as messages to a slider object. For example:
ex = .6;
New Window( "Example", mybox = Slider Box( 0, 1, ex, Show( ex ) ) );
mybox << Set Width( 200 ) << Rescale Slider( 0, 5 );

Spacer Box(<Size(h, v)>, <Color(color)>)
Description

Creates a display box that can be used to maintain space between other display boxes, or
to fill a cell in a LineUp Box.
Returns

A reference to the display box.
Optional Arguments
Size(h, v) The h and v arguments specify the size of the box in pixels.
Color(color) Sets the color of the box to the JSL color argument.

Spin Box(script)
Description

Returns a display box that shows a button with up and down controls.
Argument

script Invoked with an argument that indicates the direction of the arrow clicked.
Negative is down, and positive is up. A value of 1 indicates a single click, while larger
values indicate a repeating action.
Example
win = New Window( "Example",
Lineup Box(
2,
nb = Number Edit Box( 3 ),
sb = Spin Box( Function( {value}, nb << Increment( value ) ) )
)
);
nb << Set Increment( 1 );

JSL Functions, Operators, and Messages
Display Functions

119

Splitter Box(<Size(x, y)>, display box, ...)
Description

Returns a display box that can organize other display boxes horizontally or vertically with
interactive control of sizes. Child sizes are specified as a proportion of the width or height
of the splitter box. The optional Size argument is used only for the top-most splitter box.
Lower level display boxes are sized like any other child box.
Use H Splitter Box() or V Splitter Box().
String Col Box(title, {string, ...})
Description

Creates a column in the data table containing the quoted string items. The column is
named after the quoted title.
String Col Edit Box(title, {string, ...}, <Set Width(n)>)
Description

Creates a column in the data table containing the quoted string items. The string boxes
are editable. The column is named after the quoted title.
Optional Arguments
Set Width(n) Specifies the width of the column in pixels.
Example
Names Default To Here( 1 );
New Window( "Example",
scb =
String Col Edit Box(
"Strings",
{"The", "quick", "brown", "fox", "jumps",
"over", "the", "lazy", "dog"},
)
);
scb << SetWidth( 300 );

Notes

To retrieve the data, use the following message:
data = obj << Get;

Display Functions

Tab Box(Tab Page Box(Title(page title 1), <options>, contents of page 1), Tab
Page Box(Title(page title 2), <options>, contents of page 2), ...);
Description

(Previously called Tab List Box.) Creates a tabbed window pane. The arguments are an
even number of items alternating between the name of a tab page and the contents of the
tab page. The page titles must be quoted.
Arguments
Tab Page Box Returns a display box that can be used in a tab box or as a stand-alone

container with a title.
– Title(page title #) specifies the title of page 1.
– Options include <<Closeable(Boolean) (specifies whether the box can be closed),
<<Tip(string) (a quoted string that specifies a tooltip), and <<Icon(string) (a quoted
string that specifies the icon).
– contents of page # is a quoted string that specifies the text on the tab.
Example
New Window( "Example",
Tab Box(
t1 = Tab Page Box( Title( "alpha" ), Panel Box( "panel", Text Box( "text"
) ) ),
t2 = Tab Page Box( Title( "beta" ), Popup Box( {"x", ex = 1, "y", ex = 2}
) ),
)
);

Notes

Certain messages that you can send to Tab Page Box have been renamed:
– Set Title is called Title.
– Set Tip is called Tip.
– Set Icon is called Icon.
– Set Closeable is called Closeable.
Tab List Box(title, tabExpr1, ...)
See “Tab Box(Tab Page Box(Title(page title 1), <options>, contents of page 1), Tab
Page Box(Title(page title 2), <options>, contents of page 2), ...);”.
Tab Page Box(Title(string), <options>, contents)
Description

Returns a display box that can be used in a tab box or as a stand-alone container with a
title.

JSL Functions, Operators, and Messages
Display Functions

121

Required Argument
Title A quoted string that specifies the title on the tab.
Optional Messages
<<Tip(string) A quoted string that specifies a tooltip.
<<Closeable(Boolean) Specifies whether the page can be closed.
<<Icon(string) A quoted string that specifies the icon.
<<Set Font(font name, <size>, <"bold"|"italic"|"underline"|strikeout">,
<angle> Specifies the font properties.
<<Set Font Name("font name") Specifies the name of the font.
<<Set Font Scale(f) Specifies the scale factor for the font. The scale factor is applied to

the size that is determined by the base font and point size.
<<Set Font Size(n) Specifies the font size in pixels.
<<Set Font Style("plain"|"bold") Specifies the font style.
Notes

Certain messages that you can send to Tab Page Box have been renamed:
– Set Title is called Title.
– Set Tip is called Tip.
– Set Icon is called Icon.
– Set Closeable is called Closeable.
Table Box(display box, ...)
Description

Creates a report table with the display boxes listed as columns.
Text Box(text, <arguments>)
Description

Constructs a box that contains the quoted string text.
Arguments
<<Justify Text(position) Justifies the text left, center, or right as specified in quotes.
<<Set Wrap(pixels) Sets the point at which text wraps.

Text Edit Box(text, <arguments>)
Description

Constructs an editable box that contains the quoted string text.
Arguments
<<Password Style(Boolean) Displays asterisks in the box rather than the password.
<<Set Script Runs the specified script after the text is edited.

Display Functions

<<Set Width(pixels) Sets the point at which text wraps.

This Project()
Description

Gets the current project when a JSL script is run from that project.
Example

The following example gets the window title of the current project.
project = New Project();
project << Save( "$DOCUMENTS/Test Project.jmpprj" );
project << Run Script(
New Window( "Project Title",
Text Box(This Project() << Get Window Title())
);
);

Tree Box(<{rootnodes}>, <Size(width, height)>, <MultiSelect(Boolean)>)
Description

Constructs a box to show a hierarchical tree composed of tree nodes.
Arguments
{rootnodes} Specifies the names for the root nodes created by Tree Node() which the

box contains.
Size(width, height) Specifies the width and height (in pixels) of the box.
MultiSelect(Boolean) Indicates that more than one item in the tree can be selected.
Tree Node(<data>)
Description

Creates a node for display in a Tree Box display. Tree Node is used for both parent and
child nodes.
Notes

If you send a root node that contains one or more nodes with the Set Node Select
Script defining a collapse message, then Apple macOS runs the script twice. Windows
doesn’t run the script. This behavior on Apple macOS doesn’t just affect increments. Any
script runs twice. It will print to the log twice, create a column twice, try to delete
something twice, and so on.

JSL Functions, Operators, and Messages
Display Functions

123

Triangulation(<dt>, X(col1, col1), <Y(col)>)
Description

Returns an object containing the Delaunay triangulation of the given point set. The
optional Y will be averaged for duplicate points, and all points in the output will be
unique.
Examples
tri = Triangulation(
X( [0 0 1 1], [0 1 0 1] ),
Y( [0 1 2 3] )
);
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
tri = Triangulation( X( :X, :Y ), Y( :POP ) );

V Center Box(display box...)
Returns a display box that contains the child display box argument. The box is centered in the
vertical space defined by the maximum size of that child display box and all of the other
siblings of the center box.
V List Box(<Align("Center"|"Right")>, display box, ...)
Description

Creates a display box that contains other display boxes and displays them vertically.
Arguments
Align Specify right or center alignment of the contents in the list box. The contents are

center aligned by default.
display box Any number of display box arguments can be contained in the list box.
V Scroll Box(<Size(v)>, display box)
Description

Returns a display box that places a scroll bar on the bottom and right if the contents are
bigger than the size of the scroll box.
Arguments
Size(v) The vertical length of the scroll bar.

display box Any number of display box arguments can be contained in the scroll box.
Example
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "stretchable",
H Splitter Box(
Size( 400, 200 ),
Scroll Box(

Display Functions

Size( 200, 200 ),
dt <<Run Script( "Distribution" ),
<<Set Stretch( "Window", "Window" )
),
Scroll Box(
Size( 200, 200 ),
dt <<Run Script( "Bivariate" ),
<<Set Stretch( "Window", "Window" )
),
<<Set Stretch( "Window", "Window" )
)
);

Notes

The flexible argument is deprecated. Use Set Stretch instead.
V Sheet Box(<<Hold(report), display box, ...)
Description

Returns a display box that arranges the display boxes provided by the arguments in a
vertical layout. The <<Hold() message tells the sheet to own the report(s) that is
excerpted.
V Splitter Box(<Size(h,v)>, display box..., <arguments>)
Description

Returns a display box that arranges the display boxes provided by the arguments in a
vertical layout (or panel). The splitter enables the user to interactively resize the panel.
Arguments
Size(v) The vertical length of the scroll bar.

display box Any number of display box arguments can be contained in the splitter box.
Optional Arguments

For more information about the optional arguments, see “H Splitter Box(<Size(h, v)>,
display box, ...)”.
Web Browser Box(url)
Description

Creates a display box that contains a web page.
Returns

A reference to the web browser box object.
Argument

url A quoted string containing the URL to the web page to display.

JSL Functions, Operators, and Messages
Display Functions

125

Example

The following example creates a splitter box with the web browser box on the left and the
bubble plot on the right.
dt = Open( "$SAMPLE_DATA/PopAgeGroup.jmp" );
New Window( "Example",
H Splitter Box(
Size( 800, 300 ),
wb = Web Browser Box( "http://www.jmp.com" ),
dt << Run Script( "Bubble Plot Region" )
)
);
wb << Set Stretch( "Window", "Window" ); // auto stretch horizontally and
vertically
wb << Set Max Size( 10000, 10000 ); // maximum size in pixels

Notes

The <a href> target “_blank” opens the web page in a new Internet Explorer window.
The <a href> target “_new” opens the web page in the active Internet Explorer tab.
Window(<string|int>)
Returns

Either a list of references to all open windows, or a reference to an explicitly named
window.
Arguments

string A quoted string containing the name of a specific open window.
int The number of a specific open window.
Notes

If no argument is provided, a list of all open windows is returned.
If the argument (either a window name or number) does not exist, an empty list is
returned.
Wrap List Box(display box, ...)
Description

Creates a list box that contains other display boxes and displays them horizontally, but
wraps them when printing.
Arguments

display box Any number of display box arguments can be contained in the list box.
