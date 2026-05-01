# Introduction to Writing JSL Scripts

Source: JMP 19 Scripting Guide (PDF pages 39-50).

## Index (line numbers in this file)

- `<< Summary` — L314
- `Add()` — L298
- `Button Box()` — L480
- `Connect Color()` — L515
- `Continuous Distribution()` — L273
- `Distribution()` — L268
- `Frame Size()` — L371
- `Graph Box()` — L370
- `Line()` — L374
- `Marker()` — L372
- `Message Name()` — L469
- `Nominal Distribution()` — L275
- `Pen Color()` — L373
- `Root()` — L363
- `Show()` — L354
- `Text Box()` — L478
---

Introduction to Writing JSL Scripts
Welcome to the JMP Scripting Language
The JMP Scripting Language, or JSL, lets you write scripts to re-create results in JMP. Power
users often develop scripts to extend JMP’s functionality and automate a regularly scheduled
analysis in production settings. If you do not want to learn JSL, JMP can write the scripts for
you.
JSL is used to perform many actions:
•

implements column formulas

•

launches platforms

•

interactively modifies platforms

•

creates graphics

40

Introduction to Writing JSL Scripts

Contents
What JSL Can Do for You. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
Help with Learning JSL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
The Scripting Guide . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
The Scripting Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
Let JMP Teach You JSL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
JSL Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
Basic JSL Syntax. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Scripting Guide Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

Introduction to Writing JSL Scripts
What JSL Can Do for You

41

What JSL Can Do for You
JMP can automatically save scripts to reproduce any data table or analysis in its current state.
You can pause anytime in your analysis to save a script to a script window (or script editor), in
a data table, or in an analysis report. You can then modify the script as needed for future
projects. When you are finished with your work, you can then save a script to reproduce your
final results.
Here are some examples where JSL scripts can be helpful:
•

Suppose you need to describe an analysis process in detail, from beginning to end. An
example is to create an audit trail for a governing agency, or for peers reviewing your
journal article.

•

Suppose you have a set of analysis steps that should be followed routinely by your lab
technicians.

•

Suppose you fit the same model to new data every day, and the steps are always the same.

You can use JMP interactively as usual, save scripts to reproduce your work, and in the future
run those scripts to reproduce your results.
There are a few things that JSL is not designed to do:
•

JMP cannot record scripts while you are working. Though script-recording is a useful
feature in some other scripting languages, it is less important for software like JMP, where
the results are what matter. You cannot use script-recording to observe how a sequence of
interactive steps is performed.

•

JSL is not an alternative command-line interface for using the program.

Help with Learning JSL
There are several places within JMP to get help with writing or understanding a JSL script.

The Scripting Guide
The Scripting Guide begins with basic information (such as terminology and syntax) for JMP
users who are not familiar with the scripting language. The Scripting Guide then progresses to
more advanced information.

42

Introduction to Writing JSL Scripts
Help with Learning JSL

Chapters 2 through 4

Includes information about learning JSL, producing
basic scripts, and introduces you to the JSL scripting
environment.

Chapters 5 through 8

Introduces the building blocks of the language;
working with basic data types, such as numbers and
strings; writings lists, matrices, and associate arrays;
namespaces; and the fundamentals of programming in
JSL.

Chapters 9 through 13

Covers using JSL with objects in JMP, such as data
tables, platforms, windows, and graphics.

Describes how to write scripts that work with external
programs, such as SAS, R, and Microsoft Excel.

Describes how to organize files that you use in an
analysis, perform analyses, and run scripts from one
workspace.

Introduces creating JMP applications in Application
Builder, a drag-and-drop environment for visually
designing windows with buttons, lists, graphs, and
other objects. The chapter also describes how to use
Add-In Builder to compile scripts into one easily shared
file.

Contains a collection of recipes, or script examples, that
you can copy and modify for your own use.

Appendices A, B, C, and D

Provides information about compatibility issues with
the previous version of JMP, provides tips for writing
more efficient scripts, gives information about
references, and defines JSL concepts and terminology.

The Scripting Index
The Scripting Index on the Help menu provides a brief description and the syntax for JSL
functions, objects, and display boxes. Each entry includes an example that you can run and
modify to test your own code. And an embedded log window lets you see messages as
examples are run.

Introduction to Writing JSL Scripts
Help with Learning JSL

43

Notes:
•

To display the Scripting Index entry for a function in a script, run the script, press Alt, and
then double-click the function. You can also run the script, right-click the function, and
select Help Scripting Index.

•

To copy the syntax or description from the Scripting Index window, right-click the area
that you want to copy and select Copy Text.

The Scripting Index window includes the following buttons:
Click the Clear button to clear the search text box to begin a new search.
Click the arrow to set search filter options and parameters.
After you edit the sample script in the Scripting Index, click this button to revert to the
original script.
Note: When you edit an example script, the changes persist when you view other entries in
the Scripting Index. To revert the script, click Reset, which appears above the script after you
edit it.

Search Filter Options
Click the down arrow button next to the filter box to refine your search.
Contains Terms

Returns items that contain a part of the search criteria. A search for “ease
oom” returns messages such as “Release Zoom”.

Contains Phrase

Returns items that contain the exact search criteria. A search for “text box”
returns entries that contain “text” followed directly by “box” (for example, “Context Box”
and “Text Box”).

Starts With Phrase

Returns items that start with the search criteria.

Ends With Phrase

Returns items that end with the search criteria.

Whole Phrase

Returns items that consist of the entire string. A search for “text box” returns
entries that contain only “text box”.

Regular Expression Enables you to use the wildcard (*) and period (.) in the search box.

Searching for “get.*name” looks for items that contain “get” followed by one or more
words. It returns “Get Color Theme Names”, “Get Name Info”, and “Get Effect Names”,
and so on.
Invert Result

Returns items that do not match the search criteria.

44

Introduction to Writing JSL Scripts
Help with Learning JSL

Match All Terms Returns items that contain both strings. A search for “t test” returns

elements that contain either or both of the search strings: “Pat Test”, “Shortest Edit Script”
and “Paired t test”.
Ignore Case

Ignores the case in the search criteria.

Match Whole Words Returns items that contain each word in the string based on the Match

All Terms setting. If you search for “data filter”, and Match All Terms is selected, entries
that contain both “data” and “filter” are returned.
Search Category and Item Names

Returns category names (in the left column) and item
names (in the middle column) that match the search criteria.

Search Prototypes and Descriptions

Returns prototypes (the JSL syntax) and descriptions

that match the search criteria.
Search Examples

Returns examples that match the search criteria.

Let JMP Teach You JSL
The best JSL writer is JMP. You can work in JMP interactively and then save the results as a
script to reuse later. With simple modifications, your script can serve as a template for
speeding up routine tasks.
Because JSL is a very flexible language, you can reach your goals in many different ways. Here
is an example. Typically, the script that JMP saves for you specifies every detail of your
analysis, even if most of the details happen automatically by default. Does that mean that the
scripts that you write have to be just as complete and detailed? Not at all. You usually need to
specify only those details that you would select in the graphical user interface (GUI). For
example, if you open Big Class.jmp from the sample data folder and want to launch
Distribution for height, weight, and sex, the following script is all that is necessary:
Distribution( Y( :height, :weight, :sex ) );

Suppose you run the Distribution platform in the GUI and then select Save Script > To Script
Window from the red triangle menu for the report. The following script appears:
Distribution(
Continuous Distribution( Column( :height ) ),
Continuous Distribution( Column( :weight ) ),
Nominal Distribution( Column( :sex ) ),
);

Both scripts give the same result.
Feel free to experiment with JSL. If you think something ought to be possible, it probably is.
Give it a try, and see what happens.

Introduction to Writing JSL Scripts
JSL Terminology

45

JSL Terminology
Before you begin creating scripts, you should become familiar with basic JSL terms used
throughout the Scripting Guide.

Operators and Functions
An operator is one- or two-character symbol (such as + or =) for features such as common
arithmetic actions, scoping names, regular expressions, concatenating, and subscripting.
A function is a command that might contain additional information for the function to use.
Certain JSL functions work the same as operators but provide access to more complex actions.
For example, the following two lines are equivalent:
2 + 3; // returns 5
Add( 2, 3 ); // returns 5

The first line uses the + operator. The second line uses the Add() function equivalent.
Although all JSL operators have function equivalents, not all functions have operator
equivalents. For example, Sqrt(a) can be represented only by the Sqrt() function.
Note: In previous versions of JMP and its documentation, the terms operators and functions
were used interchangeably. Now each term has a specific meaning.

Objects and Messages
An object is a dynamic entity in JMP, such as a data table, a data column, a platform results
window, a graph, and so on. Most objects can receive messages that instruct the object to
perform some action on itself.
A message is a JSL expression that is directed to an object. That object knows how to evaluate
the message. In the following example, dt is the data table object. << indicates that a message
follows. In the following example, the message tells JMP to create a summary table with the
specified variables.
dt << Summary( Group( :age ), Mean( :height ) )

In this expression, dt is the name of a variable that contains a reference to a data table. You
could use any name for this variable. The Scripting Guide commonly uses dt to represent data
table references. Here are some of the more common names used to represent references to
certain objects:

46

Introduction to Writing JSL Scripts
JSL Terminology

Abbreviation

Object

dt

data table

col

column in a data table

colname

the name of a column in a data table

obj

an object

db

display box

These variables are not pre-assigned references. Each one must be assigned prior to its use. In
the following example, the global variable named A is assigned the value “Hello, World”.
When the Show( A ) command is processed, the result is the value of A.
A = "Hello, World";
Show( A );
A = "Hello, World";

Arguments and Parameters
An argument is additional information that you can provide to a function or message. For
example, in Root(25), 25 is an argument to the Root() function. Root() acts on the argument
that you provide and returns the result: 5.
Programming and scripting books commonly talk about parameters as well. A parameter is a
description of the argument that a function accepts. For example, the general specification for
Root() might be Root( number ), where number is the parameter.
Parameter and argument express two perspectives of the same concept: information that a
function needs.
For simplicity in the Scripting Guide, we use the word argument in both cases.
A named argument is an optional argument that you select from a predetermined set and
explicitly define. For example, title("My Line Graph") in the Graph Box() function is a
named argument because the title is explicitly defined as such.
Graph Box( title( "My Line Graph" ),
Frame Size( 300, 500 ),
Marker( Marker State( 3 ), [11 44 77], [75 25 50] );
Pen Color( "Blue" );
Line( [10 30 70], [88 22 44] ));

Note that the Frame Size() arguments 300 and 500 are not named. The position of these
arguments implies meaning; the first argument is always the width, the second argument is
always the height.

Introduction to Writing JSL Scripts
JSL Terminology

47

Optional Arguments
Functions and messages require certain arguments, and other arguments are optional. You
can include them, but you do not have to. In specifications, optional arguments are enclosed in
angle brackets. For example:
Root( x, <n> )

The x argument is required. The n argument is optional.
Optional arguments often have a default value. For example, for Root(), the default value of n
is 2:

Code

Output

Explanation

Root( 25 )

5

Returns the square root of 25.

Root( 25, 2 )

5

Returns the square root of 25.

Root( 25, 3 )

2.92401773821287

Returns the cube root of 25.

Or and the Vertical Bar Symbol
A single vertical bar (|) represents a logical OR. For brevity, | represents the word or when
referring to alternative values.
For example, a pathname can be either absolute or relative. When you see an argument such
as absolute|relative, this means that you enter either one of the following two options:
•

absolute indicates an absolute pathname.

•

relative indicates a relative pathname.

More than two options can also be strung together with a vertical bar in this way.

Script Formatting
Whitespace characters (such as spaces, tabs, and newlines) and capitalization are ignored in
JSL. This means that the following two expressions are equivalent:
Expression 1:
sum = 0;
For( i = 1, i <= 10, i++,
sum += i;
Show( i, sum );
);

Expression 2:

48

Introduction to Writing JSL Scripts
Basic JSL Syntax

Sum = 0;
For( i = 1, i <= 10, i++,
Sum += i;
Show( i, Sum );
);

You can format your script in any way that you like. However, the script editor can also format
your script for you. The Scripting Guide uses the script editor’s default formatting for
capitalization, spaces, returns, tabs, and so on. See “Work with the Script Editor” for more
information about using the script editor.
Note: The only white space exception is two-character operators (such as <= or ++). The
operators cannot be separated by a space.

Basic JSL Syntax
A JSL script is a series of expressions. Each expression is a section of JSL code that
accomplishes a task. JSL expressions hold data, manipulate data, and send commands to
objects.
Many expressions are nested message names. Message contents are enclosed in parentheses:
Message Name ( argument 1, argument 2, ... );

The meaning of JSL names depends on the context. The same name might mean one thing in a
data table context and something entirely different in a function context. See “Rules for Name
Resolution”.
Almost anything that follows certain punctuation rules, such as matching parentheses, is a
valid JSL expression. For example:
win = New Window( "Window Example",
<<Modal,
Text Box( "Hello, World" ),
Text Box( "-----" ),
Button Box( "OK" )
);

Notes:
•

Names can have embedded spaces. See “JSL Rules for Names”.

•

Message contents are enclosed in parentheses, which must be balanced. See
“Parentheses”.

•

Items are separated by commas. See “Commas”.

•

JSL is not case sensitive; you can type “text box();” or “Text Box()”.

•

Introduction to Writing JSL Scripts
Scripting Guide Conventions

49

Messages are commonly nested inside other messages.

Scripting Guide Conventions
In the Scripting Guide, the function names that are case sensitive are capitalized as you must
use them. Arguments that are placeholders for actual choices are in lowercase. For example,
Connect Color is a function that you need to type as is, and color stands for some color
choice that you make yourself.
Connect Color(color);

In this case, the argument in parentheses must be some color value (for example, a JMP color
number, or a supported color name like "red", "blue", and so on, or an RGB value given as a
list, such as {.75, .50, .50}). Sometimes alternatives like these are shown with the vertical
bar (|) character for “or,” like this:
Connect Color( number | "color name" | {r,g,b} );

Syntax coloring is applied to scripts that you can paste into a script editor and then run.

50

Introduction to Writing JSL Scripts
Scripting Guide Conventions
