# File Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 128-149).

## Index (line numbers in this file)

- `Allow Undo()` — L299
- `BLOB()` — L646
- `Base()` — L172
- `Charset()` — L635
- `Close All()` — L126
- `Close Database Connection()` — L142
- `Close Log()` — L152
- `Close()` — L112
- `Column Names Start()` — L721
- `Columns()` — L725
- `Compress Allow List Check()` — L743
- `Compress Character Columns()` — L746
- `Compress Numeric Columns()` — L748
- `Concatenate Worksheets()` — L750
- `Convert File Path()` — L156
- `Copy Directory()` — L191
- `Copy File()` — L216
- `Create Concatenation Column()` — L752
- `Create Database Connection()` — L231
- `Create Directory()` — L269
- `Creation Date()` — L279
- `Data Starts()` — L754
- `Debug JSL()` — L756
- `Delete Directory()` — L289
- `Delete File()` — L304
- `Directory Exists()` — L317
- `Driver Prompt()` — L254
- `EOF Other()` — L770
- `EOL Other()` — L772
- `Empty()` — L605
- `End Of Field()` — L758
- `End Of Line()` — L765
- `File Exists()` — L327
- `File Size()` — L337
- `Files In Directory()` — L353
- `Find All()` — L371
- `First()` — L787
- `Force()` — L617
- `Get Default Directory()` — L398
- `Get Excel Worksheets()` — L415
- `Get File Search Path()` — L186
- `Get Path Variable()` — L432
- `Google Sheet Export()` — L449
- `Google Sheet Import()` — L474
- `Guess()` — L531
- `HTML Table()` — L792
- `Ignore Columns()` — L802
- `Imported Column Names()` — L1137
- `Invisible()` — L529
- `Is Directory Writable()` — L501
- `Is Directory()` — L497
- `Is File Writable()` — L509
- `Is File()` — L505
- `JSON Literal()` — L600
- `JSON To Data Table()` — L513
- `JSON To List()` — L584
- `Labels()` — L815
- `Last Modification Date()` — L606
- `Last()` — L817
- `Line Separator()` — L641
- `Load Text File()` — L616
- `Method()` — L689
- `Move Directory()` — L657
- `Move File()` — L672
- `Name Expr()` — L106
- `New IP21 Client()` — L688
- `Open Database()` — L922
- `Open()` — L698
- `Parse JSON()` — L955
- `Password()` — L690
- `Path()` — L428
- `Pick Directory()` — L978
- `Pick File()` — L999
- `Private()` — L526
- `Project()` — L136
- `Quarantine Action()` — L843
- `Random()` — L822
- `Recursive()` — L210
- `Rename Directory()` — L1049
- `Rename File()` — L1064
- `Run JSL()` — L826
- `Save Flag()` — L1019
- `Save Text File()` — L1078
- `Scan Whole File()` — L847
- `Select Columns()` — L851
- `Set Default Directory()` — L1082
- `Set File Search Path()` — L180
- `Set Path Variable()` — L1107
- `Show Files()` — L991
- `Show()` — L184
- `Table Contains Column Headers()` — L859
- `TripleS Import()` — L1117
- `Worksheet Settings()` — L877
- `Worksheets()` — L907
- `Write()` — L391
---

File Functions

Name Expr(x)
Description

Returns the unevaluated expression of x rather than the evaluation of x.

File Functions
Close(<dt|query>, <noSave|Save(path)>)
Description

Closes a data table, query, or JSON file. If no arguments are specified, the current file is
closed. If the file has been changed, it is automatically saved. All dependent windows are
also closed (for example, report windows that are based on the data table).
Returns

Void.
Arguments

dt An optional reference to a data table, query, or JSON file.
nosave|Save(path) An optional switch to either save the file to the specified quoted
path before closing or to close the file without saving it.
Close All(<Project(title|index|display box|window)>, type,
<"Invisible"|"Private">, <NoSave|Save>)
Description

Closes all open resources of type.
Required Argument

type A named argument that defines the type of resources that you want to close. The
allowable types are: Data Tables, Reports, and Journals.
Optional Argument
Project(title|index|display box|window) Closes the specified project window.
"Invisible" Closes all invisible data tables.
"Private" Closes all private data tables.
NoSave or Save Saves the specified types of windows before closing or to close without

saving.
Close Database Connection(db connection handle)
Description

Closes a database connection returned from Create Database Connection.

JSL Functions, Operators, and Messages
File Functions

129

Close Log(Boolean)
Description

Closes the log window.
Convert File Path(path, <"Absolute"|"Relative">, <"POSIX"|"Windows">,
<Base(path)>, <Search>)
Description

Converts a file path according to the arguments.
Returns

The converted path.
Required Argument

path A quoted pathname that can be either Windows or POSIX.
Optional Arguments
"Absolute"|"Relative" Specifies whether the returned pathname is in absolute or
relative terms. The default value is Absolute.
"POSIX"|"Windows" Specifies whether the returned pathname is in Windows or POSIX
style. The default is POSIX.
Base(path) Specifies the quoted base pathname, useful if Relative is specified. The

default is the default directory. See “Set Default Directory(path)”.
Search Searches through the specified directories for the specified string. In the example
below, JMP searches $SAMPLE_DATA/ and $SAMPLE_DATA/Time Series/ for Air.jmp. If
Air.jmp is in both directories, the first instance is returned. Without the search option,
Convert File Path() uses the default directory instead.
Example
Set File Search Path(
{Convert File Path( "$SAMPLE_DATA/" ),
Convert File Path( "$SAMPLE_DATA/Time Series/" )}
);
Show( Get File Search Path() );
Show( Convert File Path( "Air.jmp", Search ) );
Get File Search Path() = {"/C:/Program Files/JMP/JMPPRO/19/Samples/Data/",
"/C:/Program Files/JMP/JMPPRO/19/Samples/Data/Time Series/"};
Convert File Path("Air.jmp", search) = "/C:/Program
Files/JMP/JMPPRO/19/Samples/Data/Time Series/Air.jmp";

Copy Directory(from path, to path, <Recursive(Boolean)>)
Description

Copies files from one directory to another, optionally copying subdirectories. The
directory name is created in the to path and should not be part of the to path
argument.

File Functions

Returns

Returns 1 if the directory is copied; otherwise, returns 0.
Required Arguments

from path Specifies the directory containing the files to copy to the new directory. from
path is a quoted string.
to path Specifies the path where the new directory should be created and to which the
files are copied. to path is a quoted string.
Optional Argument
Recursive(Boolean)> Specifies whether to copy the from path subdirectory structure

to the to path.
Notes
Copy Directory(from path, to path, Boolean) is deprecated.

Copy File(from path, to path)
Description

Copies one file to a new file using the same or a different name.
Returns

Returns 1 if the file is copied; otherwise, returns 0.
Arguments

from path Specifies the path and file name to copy to the new file. from path is a
quoted string.
to path Specifies the path and file name for the new file. from path is a quoted string.
Note
Copy File() does not replace a file if it already exists.

Create Database Connection(dataSourceName|"Connect
Dialog",<DriverPrompt(Boolean)>);
Description

Creates a connection to the specified database or prompts the user to provide database log
in information.
Returns

A handle to the database connection.
Required Argument

dataSourceName The quoted server connection string that contains information such as
the data source name and user name.
Optional Arguments
"Connect Dialog" Opens the Select Data Source window, from which the user selects

the database.

JSL Functions, Operators, and Messages
File Functions

131

Driver Prompt(Boolean) Enables the ODBC driver to prompt for the connection

information if necessary.
Examples

Specify the data source name, user name, and password:
Create Database Connection( "dsn=Books;UID=johnsmith;password=Christmas" );

Request that the ODBC driver prompt the user to enter connection information, because
the quoted connection string does not specify the password:
Create Database Connection( "dsn=Books;UID=johnsmith", Driver Prompt( 1 ) );

Enable the user to select the data source, specify "Connect Dialog":
Create Database Connection( "Connect Dialog" );

Create Directory(path)
Description

Creates a new directory at the specified path location.
Returns

Returns 1 if the directory is created; otherwise, returns 0.
Arguments

path Specifies the quoted path where the new directory should be located.
Creation Date(path)
Description

Returns the creation date for the specified file or directory.
Returns

Creation date.
Arguments

path Specifies the quoted directory or path and file name for the query.
Delete Directory(path, <Allow Undo(Boolean)>)
Description

Deletes the specified directory and its contents and any subdirectories.
Returns

Returns 1 if the directory is deleted; otherwise, returns 0.
Arguments

path Specifies the path and directory for deletion.
Allow Undo(Boolean) Allows undo operations, for example, moving to the Recycle Bin
or Trash Can.

File Functions

Delete File(path, <Allow Undo(Boolean)>)
Description

Deletes the specified file.
Returns

Returns 1 if the file is deleted; otherwise, returns 0.
Required Argument
path Specifies the quoted path and file name for deletion.
Optional Argument
Allow Undo(Boolean) Allows undo operations, for example, moving to the Recycle Bin

or Trash Can.
Directory Exists(path)
Description

Verifies the specified directory exists.
Returns

Returns 1 if the directory exists; otherwise returns 0.
Arguments

path Specifies the quoted path and directory for verification.
File Exists(path)
Description

Verifies the specified file name exists at the specified path.
Returns

Returns 1 if the file exists; otherwise returns 0.
Arguments

path Specifies the quoted path and file name for verification.
File Size(path)
Description

Determines the size of the file within the specified path.
Arguments

path Specifies the quoted path and file name.
Example
File Size( "$SAMPLE_DATA/Big Class.jmp" );
14890

JSL Functions, Operators, and Messages
File Functions

133

Files In Directory(path, <Recursive(Boolean)>)
Description

Returns a list of file names in the path given.
Returns

List of file names. If Recursive(Boolean) is not specified, directory names are included
in the list.
Required Argument

path A valid quoted pathname.
Optional Argument
Recursive(Boolean) A keyword that causes all folders in the path (and all folders that

they contain, and so on) to be searched for files.
Notes
Files In Directory(path, "Recursive"|Boolean) is deprecated.

Find All(<Project(title|index|display box|window)>, type,
<"Invisible"|"Private">)
Description

Finds all open files of the specified type.
Required Argument

type A named argument that defines the type of resources that you want to close. The
allowable types are: Data Tables, Reports, and Journals.
Optional Argument
Project(title|index|display box|window) Closes the specified project window.
"Invisible" Closes all invisible data tables.
"Private" Closes all private data tables.
Example

The following example finds all open data tables:
exdt1 = Open( "$SAMPLE_DATA/Big Class.jmp" );
exdt2 = Open( "$SAMPLE_DATA/Animals.jmp" );
windows = Find All( Data Tables );
For( i = 1, i <= N Items( windows ), i++,
Write( Char( windows[i] << Get Window Title ) || "\!N" )
);
Big Class
Animals

File Functions

Get Default Directory()
Description

Retrieves the user’s default directory. This path is used for subsequent relative paths.
If the default directory was set using Set Default Directory(), JMP returns the
specified path as long as Get Default Directory() and Set Default Directory() are
in the same script.
See “Set Default Directory(path)”.
Returns

The absolute pathname as a quoted string.
Arguments

none
Notes
Get Default Directory() also gets the path of an active saved scripting window.

Get Excel Worksheets(absolute path)
Description

Retrieves a list of worksheets that are in the specified Microsoft Excel workbook. If no
worksheets are found, an empty list is returned. The path is a quoted string.
Notes

The function supports .xlsx and Excel 1997 or later workbooks.
Get File Search Path()
Description

Retrieves the current list of directories to search for opening files.
This list is configured using the Set File Search Path() function. See “Set File Search
Path(path|{list of paths})”.
Returns

A list of pathnames as quoted strings.
Get Path Variable(name)
Description

Retrieves the value of name, a path variable.
Returns

The absolute pathname as a quoted string.

JSL Functions, Operators, and Messages
File Functions

135

Argument
name A quoted string that contains a path variable. (Examples: SAMPLE_DATA and
SAMPLE_SCRIPTS)

Google Sheet Export(dt, email, spreadsheet URL|spreadsheet ID|new spreadsheet
name, sheet name)
Description

Exports a data table to a Google sheet.
Returns

“1” if the export is successful.
Arguments
dt The data table.

email The quoted Google email address. @gmail.com is unnecessary.
spreadsheet URL|ID The quoted spreadsheet’s URL or ID (the string that precedes
“spreadsheets/d/”).
new spreadsheet name The quoted name of the new spreadsheet that you are creating.
sheet name The quoted name of the sheet (or tab) within the spreadsheet.
Notes

– JMP features such as formulas and List Check column properties are not supported in
Google Sheets.
– If the spreadsheet is empty, look in the JMP log for error messages. On Windows, select
View > Log. On Apple macOS, select Window > Log.
See Also

See Using JMP for details about security, country restrictions, and more.
Google Sheet Import(email, spreadsheet URL|spreadsheet ID, <sheet name|{sheet
name, sheet name}, Google Sheet Settings>)
Description

Imports sheets from a Google Sheet.
Returns

A data table (or the first data table imported if several sheets are imported at once).
Required Arguments

email The quoted Google email address. @gmail.com is unnecessary.
spreadsheet URL|ID The quoted spreadsheet’s URL or ID (which precedes
“spreadsheets/d/”).
Optional Arguments

sheet name The quoted name of the sheet or sheets that you want to import.

File Functions

Google Sheet Settings The settings that describe how the data is imported.
See Also

See Using JMP for details about security, country restrictions, and more.
Is Directory(path)
Description

Returns 1 if the quoted path argument is a directory and 0 otherwise.
Is Directory Writable(path)
Description

Returns 1 if the directory specified in the quoted path is writable and 0 otherwise.
Is File(path)
Description

Returns 1 if the quoted path is a file and 0 otherwise.
Is File Writable(path)
Description

Returns 1 if the file specified in the quoted path is writable and 0 otherwise.
JSON To Data Table(JSON string, (<Private(Boolean)>|<Invisible(Boolean)>),
<Guess(Stack(Boolean)|"Tall"|"Wide"|"Huge"|"Pandas")>)
Description

Converts a quoted JSON string to a data table.
Returns

A data table reference. The parsing of an empty value, ʺʺ string, missing value, or any
other invalid value returns an empty data table.
Required Argument

JSON string The quoted JSON string.
Optional Arguments
Private(Boolean) Hides the data table completely. Specify this argument if the user

doesn’t need to interact with the data table.
Invisible(Boolean) Hides the data table from view but shows it in the JMP Home
Window.
Guess(Stack(Boolean)|"Tall"|"Wide"|"Huge"|"Pandas") Stack applies to nodes
that repeat within a parent node that is creating rows. By default, extra values are

JSL Functions, Operators, and Messages
File Functions

137

stored in a single table cell separated by commas. If the value is 1, repeating values are
stacked in extra rows. Be careful stacking data. It can cause non-obvious data errors.
"Tall" imports the data in a tall data table. Select this option when the JSON file

contains many rows. This option is the default setting.
"Wide" imports the data in a wide data table. Select this option when the JSON file

contains many columns.
"Huge" imports the data in a tall and wide data table.
"Pandas" imports data in the pandas format.
Example
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt = JSON to Data Table(
"[ { \!"name\!": \!"KATIE\!", \!"age\!": 12, \!"sex\!": \!"F\!",
\!"height\!": 59, \!"weight\!": 95 }, { \!"name\!": \!"LOUISE\!",
\!"age\!": 12, \!"sex\!": \!"F\!", \!"height\!": 61, \!"weight\!": 123 }, {
\!"name\!": \!"JANE\!", \!"age\!": 12, \!"sex\!": \!"F\!", \!"height\!":
55, \!"weight\!": 74 } ]"
);

Notes

Stacking the data can cause non-obvious data errors. Values that are supposed to be in the
same row might not be. Here’s an example of stacking data:
d =
"\[
{
"toys": [{
"Wheels": 2,
"Color": "Red"
},
{
"Wheels": 4,
"Size": "Large"
}]
}
]\";
JSON to Data Table( d, Guess( Stack( 1 ) ) );

Figure 2.1 Example of Stacking Data that Shows Errors

File Functions

The first toy should be red and have 2 wheels. The second toy should be large and have 4
wheels.
JSON To List(JSON string)
Description

Converts quoted JSON string to a JSL list that represents the structure specified by the
JSON data. The parsing of an empty value, ʺʺ string, missing value, or any other invalid
value returns {}.
Example
l = JSON To List(
"[ { \!"name\!": \!"KATIE\!", \!"age\!": 12, \!"sex\!": \!"F\!",
\!"height\!": 59, \!"weight\!": 95 }, { \!"name\!": \!"LOUISE\!",
\!"age\!": 12, \!"sex\!": \!"F\!", \!"height\!": 61, \!"weight\!": 123 }, {
\!"name\!": \!"JANE\!", \!"age\!": 12, \!"sex\!": \!"F\!", \!"height\!":
55, \!"weight\!": 74 } ]"
);
Show( l );

JSON Literal(JSON string)
Description

Returns a valid JSON Boolean or null constant based on the specification of the parameter.
The parsing of an empty value, ʺʺ string, missing value, or any other invalid value returns
Empty().
Last Modification Date(path)
Description

Returns the last modification date of the path.
Returns

Last modification date.
Arguments

path The quoted directory or file name.
Load Text File(path, <Charset(character set),
Force("Throw"|"Alert"|"Silent")>)>, <Line Separator(character)>,
<"XMLParse">|<"SASODSXML">|<"JSON">|<BLOB(<arguments>)>)>)
Description

Reads the text file at path into a JSL variable.
Returns

A quoted string.

JSL Functions, Operators, and Messages
File Functions

139

Required Argument

path A quoted pathname that points to a text file. The path can be a URL.
Optional Arguments
Charset("charater set") Specifies the character set. Valid character sets are "Best
Guess", "utf-8", "utf-16", "us-ascii"," windows-1252", "x-max-roman",
"x-mac-japanese", "shift-jis", "euc-jp", "utf-16be", and "gb2312".
Force("Throw"|"Alert"|"Silent") Specifies what happens if the character set cannot

be detected.
Line Separator(character) Specifies the quoted end-of-line character. For example,
"\!n" specifies a line feed character. "\!t" specifies a tab.
"XMLParse" Converts an XML file into JSL.
"SASODSXML" Parses the text file as SAS ODS default XML.
"JSON" Converts JSON into an expression tree.
BLOB(<arguments>) Returns data from the file as a blob rather than a quoted string. The
following optional arguments are for reading parts of the file:
– ReadOffsetFromBegin(n) specifies the zero-based offset to begin reading from the
beginning of the file.
– ReadOffsetFromEnd(n) specifies the zero-based offset to begin reading from the end of
the file.
– ReadLength(n) specifies the number of bytes to read from the file, either from the
beginning of the file or from one of the offset values.
– Base64Compressed(Boolean) specifies how the blob is converted to a printable
representation. 0, the default and recommended setting, uses JMP’s ASCII~HEX
representation. 1 means the blob is compressed and converted to base 64 when printed.
Move Directory(from path, to path)
Description

Moves a directory and its contents (including subdirectories) from the quoted path to
another quoted path.
Returns

Returns 1 if the directory is moved; otherwise returns 0.
Arguments

from path Specifies the path and directory for relocation.
to path Specifies the destination path and directory.

File Functions

Move File(from path, to path)
Description

Moves a file from the quoted path to another quoted path with the same or different file
name.
Returns

Returns 1 if the file is moved. Otherwise, it returns 0.
Arguments

from path Specifies the quoted path and file name for relocation.
to path Specifies the quoted destination path and file name.
Notes

On Windows, when you move a file to a folder that does not exist, Windows creates the
folder and returns 1. On Apple macOS, the folder is not created, and an error is returned.
New IP21 Client(URL(<baseURL>), Authentication
Method("None"|"Basic"|"NTLM"|"Kerberos"), Username(<userID>),
Password(<password>))
Description

Creates an AspenTech InfoPlus.21 Client object that establishes a connection to an IP.21
server.
To import data using the established connection, an importer object must be created from
this client object. For information on creating an importer object, see “AspenTech
InfoPlus.21 Messages”.
Open(path, <arguments>)
Description

Opens the data table or other JMP file or object created from a file named by the path. If
no path is specified, the Open window appears. Also opens JSON and HDF5 files. See the
examples in the JMP Scripting Index in the Help menu for more information about which
arguments apply to specific file types.
Required Argument

path The quoted path to the file that you want to open.
Optional Arguments
Add to Recent Files(Boolean) Determines whether the file is added to the Recent

Files list in the Home Window.
Charset(character set) The available character set options for importing text files are
"Best Guess", "utf-8", "utf-16", "us-ascii"," windows-1252", "x-max-roman",
"x-mac-japanese", "shift-jis", "euc-jp", "utf-16be", and "gb2312".

JSL Functions, Operators, and Messages
File Functions

141

Column Names Start(n)|Column Names are on Line(n) Specifies the line number

that column names start in the imported text file. If the text file uses returns between
cells, column names could be on multiple lines.
Columns(colName=colType(colWidth),...) Specifies the columns by name in the
text file to import into a data table where:
– colName: Specifies the column name used in the imported text file.
– colType("Character"|"Numeric"): Specifies whether the specified column contains
character or numeric data.
– colWidth(n): Specifies the integer width of the specified column.
Columns(<arguments>) For ESRI shapefiles (.shp), this argument and its settings

indicate the following:
– Shape=numeric(n): Specifies the column number in the imported ESRI shapefile that
contains the shape number.
– Part=numeric(n): Specifies the column number in the imported ESRI shapefile that
contains the part number.
– X=numeric(n): Specifies the column number in the imported ESRI shapefile that
contains the decimal degree for the longitude (range of ±180°).
– Y=numeric(n): Specifies the column number in the imported ESRI shapefile that
contains the decimal degree for the latitude (range of ±90°).
"Column Names Only" Returns a list of column names.
Compress Allow List Check(Boolean) Specifies that JMP can compress data table

created from the imported text file.
Compress Character Columns(Boolean) Specifies that JMP should compress data
table columns that contain character data from the imported text file.
Compress Numeric Columns(Boolean) Specifies that JMP should compress data table
columns that contain numeric data from the imported text file.
Concatenate Worksheets(Boolean) Specifies that JMP should combine the imported
Excel worksheets into one data table.
Create Concatenation Column(Boolean) Specifies that JMP should combine columns
from an imported Excel file into one column.
Data Starts(n)|Data Starts on Line(n) Specifies the line number where data starts
in the imported text file.
Debug JSL(Boolean) Opens the specified JSL script in the Debugger instead of opening
it.
End Of Field("Tab"|"Space"|"Comma"|"Semicolon"|"Other"|"None") Specifies the
quoted character used to delimit the end of a field in the imported text file. To specify
multiple characters, separate each character designation by a comma. If you use
"Other", designate the delimiter with EOF Other() argument.

File Functions

End Of Line("CRLF"|"CR"|"LF"|"Semicolon"|"Other") Specifies the quoted

character used to delimit the end of a line in the imported text file. To specify multiple
characters, separate each character designation by a comma. If you use "Other",
designate the delimiter with EOL Other() argument.
EOF Other(char) If the imported text file uses an end-of-field character other than the
one specified by End of Field(), this argument specifies the character used.
EOL Other(char) If the imported text file uses an end of line character other than the
one specified by End of Line(), this argument specifies the character used.
"Excel Wizard" Opens Microsoft Excel worksheets in the Excel Import Wizard. If you
omit this argument, the worksheets open directly as a data table.
"text"|"journal"|"sas"|"script"|"png"|"jmp" An optional quoted string that
specifies the type of file that you are opening. This can be useful if your file does not
have a file extension, the file extension of the file does not match the contents of the file,
or you want to import a JSL BLOB. If you do not specify this string, the file opens in the
default program for the file extension.
Note: The path argument should be used for a zip archive. The extension (.zip) is not
required. See “Zip Archives” for the messages that you can send to a zip archive. The basic
functionality is to get a list of files in the zip archive, to read a file in the zip archive into
either a quoted string or a blob, and to write files into the zip archive. Note that reading a
zip archive temporarily puts the contents into memory. Reading very large zip archives
can cause errors.
First(n) imports the first n number of rows from the data table.
"Force Refresh" Closes the specified JMP (.jrn, .jsl, .jrp, or .jmpappsource) file without

saving and tries to reopen the file from disk. This argument deletes any changes made
since the last time the file was opened.
HTML Table(n, <ColumnNames(n)>, <DataStarts(n)>) To import a table from an
HTML web page, use the URL as the filepath. The optional n argument specifies which
table number, n, on the web page to open. If you omit the value, only the first table on
the page is imported. The optional ColumnNames(n) specifies the row that contains
column names. The optional DataStarts(n) specifies the row on which the data
begins.
Tip: If the table you are importing contains images, they are first imported as text. To load
the images in your JMP data table, run the automatically generated table script named
Load Pictures. A new expression column containing the images is created. See Using JMP
for more information about expression columns.
Ignore Columns(col1, ...) Specifies the quoted column names in the JMP data table

or other JMP file that should not be included in the data table.

JSL Functions, Operators, and Messages
File Functions

143

"Invisible" Opens the file as invisible. This quoted keyword applies to these files: data

table, JMP file, external, text, Excel, SAS, ESRI shapefile, and HTML. The data table
appears only in the JMP Home Window and the Window menu.
Labels(Boolean) Specifies the imported text file contains labels or column headers as
the first line in the file. The default value is True.
Last(n) imports the last n number of rows from the data table.
Lines to Read(n) Specifies the number of lines in the text file to import. JMP starts
counting lines after column names are read.
Number of Columns(n) Specifies the number of columns contained in the imported text
file.
Random(n) imports n number of random rows from the data table. If the argument is
between 0 and 1, the number is used as a proportion. For example, Random(.1) imports
a random 10 percent of the data.
Note: Entering a number n less than or equal to 0 will instead import the entire table.
Run JSL(Boolean) Runs the specified JSL file instead of opening it. Include a Boolean
argument or an expression that contains a Boolean value. If the script begins with //!,
which automatically runs the script, include the Boolean value (0) to open the script

instead.
Password(password) Specifies the quoted password for a password-protected SAS file

to avoid entering it manually. The password is not encrypted. (Password-protected
Microsoft Excel files cannot be imported.)
"PDF Wizard" Opens a PDF file in the PDF Import Wizard, where you can control how
data is imported.
"Private" Opens the table as invisible and without showing it in the JMP Home
Window or Window menu. For example, you might create a private data table to hold
temporary data that the user does not need to see. This quoted keyword applies to the
following files: data table, JMP file, external, text, Excel, SAS, ESRI shapefile, or HTML.
Creating a private data table speeds the process of getting to the data; it does not save
the computer from allocating the memory necessary to hold the data table data.
Quarantine Action("Allow Scripts"|"Block Scripts"|"Do Not Open"|"Show
Dialog") Specifies whether scripts run when you open downloaded data tables. Also
provides an option to display a window that prompts users to examine or open the data
table. If they click Examine, the scripts are disabled.
Scan Whole File(Boolean) Specifies how long JMP scans the text file to determine
data types for the columns. This is a Boolean value. The default value is true; the entire
file is scanned until the data type is determined. To import large files, consider setting
the value to false, which scans the file for five seconds.
Select Columns(col1, ...) Specifies the quoted column names in the JMP data table
or other JMP file that should be included in the data table.

File Functions

"Strip Quotes"|Strip Enclosing Quotes(Boolean) If the fields in the text file are
quoted, setting this to True removes the quotes, and setting it to False does not remove
the quotes. The default value is True.
Table Contains Column Headers(Boolean) Indicates the imported text file contains
labels or column headers as the first line in the file. The default value is True.
"Text Wizard" Opens the text file in the text import window, where you can select

import options. Otherwise, the Text Data Files options in the JMP preferences apply,
and the text file is automatically imported as a data table.
Treat Empty Columns as Numeric(Boolean) Specifies that JMP should import text
file columns of missing data as numeric rather than character. Possible missing value
indicators are a period, a Unicode dot, NaN, or a blank quoted string. The default value
is False.
Use Apostrophe as Quotation Mark(Boolean) Declares apostrophes as quotation
marks in importing text files. This option is not recommended unless your data comes
from a nonstandard source that places apostrophes around data fields rather than
quotation marks. The default value is False.
Use Labels for Var Names(Boolean) For SAS data sets, this option specifies to use
SAS labels as JMP columns names. The default value is False.
Use for All Sheets(Boolean) Indicates that JMP should use the Worksheets settings
for all worksheets in the Excel file to be opened as a data table.
Worksheet Settings(Boolean, <options>) specifies options for importing an Excel
file into a JMP data table. Available options are:
– Has Column Headers(Boolean) specifies that the Excel file has column headers in the
first row.
– Number of Rows in Headers(n) specifies the number of rows in the Excel file used as
column headers.
– Headers Start on Row(n) specifies the row number in the Excel file where the
column headers begin. Default is row 1.
– Data Starts on Row(n) specifies the row number in the Excel file where the data
begins.
– Data Starts on Column(n) specifies the column number in the Excel file where the
data begins.
– Data Ends on Row(n) specifies the row number in the Excel file where data ends.
– Data Ends on Column(n) specifies the column number in the Excel file where the
data ends.
– Replicated Spanned Rows(Boolean) specifies that the Excel file contains spanned
columns should be imported into JMP as spanned columns.
– Suppress Hidden Rows(Boolean) indicates that JMP should not import rows hidden
in the Excel file.

JSL Functions, Operators, and Messages
File Functions

145

– Suppress Hidden Columns(Boolean) indicates that JMP should not import columns
hidden in the Excel file.
– Treat as Hierarchy(Boolean) indicates that JMP should treat multiple column
headers (merged cells) as hierarchies when importing an Excel file. If True, the Excel
file opens with the merged columns stacked (Tables > Stacked).
Worksheets("Sheet Name"|{"Sheet Name", "Sheet Name",...}|n) Opens the

specified Excel file worksheet by name, all worksheets in a list of names, or the indexed
number of the worksheet. If the worksheets are not specified, all worksheets in the
spreadsheet open as separate data tables.
Note: You can import .xls worksheets from a web site by specifying worksheets
arguments. .xlsx worksheets cannot be imported from a web site using Open().
"XML Wizard" Opens XML files in the XML Import Wizard. If you omit this argument,

the XML file opens as a data table.
Year Rule | Two Digit Year Rule
("1900-1999"|"1910-2009"|"1920-2019"|"1930-2029"|"1940-2039"|
"1950-2049"|"1960-2059"|"1970-2069"|"1980-2079"|"1990-2089"|"2000-2099
") Indicates the year format used in the imported text file. For example, if the earliest
date is 1979, use “1970-2069”.
Open Database(dataSourceName|"Connect Dialog", "SELECT
..."|"SQLFILE..."|tableName, <"Invisible"|"Private">, <outputTableName>)
Description

Opens the database indicated by dataSourceName (or opened by the user) with the
SELECT , SQLFILE, or tableName arguments.
Returns

A data table named outputTableName.
Required Argument

dataSourceName|"Connect Dialog" dataSourceName specifies the name of the data
source. "Connect Dialog" shows a window from which the user selects the data
source.
Optional Arguments
"Invisible" Creates an invisible data table that hides the table from view but lists it in

the JMP Home Window and Window menu.
"Private" Hides the data table completely. Creating a private data table speeds the
process of getting to the data; it does not save the computer from allocating the memory
necessary to hold the data table data.
outputTableName The name of the data table in JMP.
Example
Open Database(

File Functions

"DSN=dBASE Files;DBQ=C:\Program Files\JMP\JMPPRO\19\Samples\Import Data\;",
// SQL statement
"SELECT HEIGHT, WEIGHT FROM Bigclass", // selected columns
"hw" // name of the output data table
);

Parse JSON(JSON string)
Description

Converts JSON string into an associative array or list based on the structure of the JSON
data. Convert the result to a list if the parsed JSON object contains more than one member.
The parsing of an empty value, ʺʺ quoted string, missing value, or any other invalid value
returns Empty().
Example

The following example converts JSON into a list:
j = Parse JSON(
"[ { \!"name\!": \!"KATIE\!", \!"age\!": 12, \!"sex\!": \!"F\!",
\!"height\!": 59, \!"weight\!": 95 }, { \!"name\!": \!"LOUISE\!",
\!"age\!": 12, \!"sex\!": \!"F\!", \!"height\!": 61, \!"weight\!": 123 }, {
\!"name\!": \!"JANE\!", \!"age\!": 12, \!"sex\!": \!"F\!", \!"height\!":
55, \!"weight\!": 74 } ]"
);
Show( j );
j = {["age" => 12, "height" => 59, "name" => "KATIE", "sex" => "F", "weight"
=> 95], ["age" => 12, "height" => 61, "name" => "LOUISE", "sex" => "F",
"weight" => 123], ["age" => 12, "height" => 55, "name" => "JANE", "sex"
=> "F", "weight" => 74]};

Pick Directory(<"Prompt">, <path>, <Show Files(Boolean)>)
Description

Prompts the user for a directory, returning the directory path as a quoted string.
Returns

The path for the directory that the user selects.
Optional Arguments
"Prompt" The quoted string appears at the top of the Browse window (Windows) or the

Finder window (Apple macOS).
path The quoted string specifies the initial directory that appears in the Pick Directory
window.
Show Files(Boolean) 1 shows files in the Pick Directory window. 0 hide the files. The
default is 0.

JSL Functions, Operators, and Messages
File Functions

147

Pick File(<"Prompt">, <initial directory>, <{filter list}>, <first filter>,
<Save Flag(Boolean)>, <default file>), <"Multiple">)
Description

Prompts the user to select one or more files in the Open window.
Returns

The path of the file that the user selects.
Optional Arguments
"Prompt" A quoted string. If provided, that string appears at the top of the Open

window.
initial directory A quoted string that is a valid filepath to a folder. If provided, it
specifies where the Open window begins. If not provided, or if it’s an empty string, the
JMP Default Directory is used.
filter list A list of quoted strings that define the filetypes to show in the Open
window. See the following example for syntax.
first filter An integer that specifies which of the filters in the filter list to use
initially. If you use an integer that is too large or small for the list (for example, 4 for a
list of 3), the first filter in the list is used.
Save Flag(Boolean) A Boolean that specifies whether the Open window or Save
window is used. 0 lets the user select a file to open in JMP. 1 lets the user save a new,
empty file of the selected type in the selected folder. The default value is 0.
default file The quoted name of the file that appears in the window by default.
"Multiple" The quoted name that lets the user select multiple files if the Save Flag
value is 0.
Notes

Although all arguments are optional, they are also positional. For example, you cannot
specify a filter list without also specifying the caption and the initial directory.
The buffer size in the computer’s physical memory affects the number of files the user can
open.
Example

The following script assigns Select JMP File as the window title; shows the JMP
Samples/Data directory; shows JMP Files and All Files in the File name list and selects JMP
Files; displays the Open window; and shows the sample data file name Hollywood
Movies.jmp.
Pick File(
"Select JMP File",
"$SAMPLE_DATA",
{"JMP Files|jmp;jsl;jrn", "All Files|*"},
1,
0,
"Hollywood Movies.jmp"

File Functions

);

Rename Directory(old path name, new directory name)
Description

Renames a directory without moving or copying it.
Returns

Returns 1 if the directory is renamed; otherwise, returns 0.
Arguments

old path name A quoted string that specifies the path and old directory name.
new directory name A quoted string that specifies the new directory name.
Notes

When you specify the new directory Name, include only the directory name, not the
entire path.
Rename File(old path name, new file name)
Description

Renames a file without moving or copying it.
Returns

Returns 1 if the file is renamed; otherwise, returns 0.
Arguments

old path name Specifies the path and old file name.
new file name Specifies the new file name.
Notes

When you specify the new name, include only the file name, not the entire path.
Save Text File(path, text|BLOB, <Mode("Replace"|"Append")>)
Description

Returns the path name of the created file. text is quoted string.
Set Default Directory(path)
Description

Sets the default directory, which is used for resolving relative paths.
See Also

“Get Default Directory()”

JSL Functions, Operators, and Messages
File Functions

149

Set File Search Path(path|{list of paths})
Description

Sets the current list of directories to search for opening files. Using {ʺ.ʺ} as the path
configures JMP to use the current directory.
Example
Set File Search Path( {"C:\JMP\13\source", "C:\Program
Files\JMP\JMPPRO\19\Samples"} );

See Also

“Get File Search Path()”.
Set Path Variable(name, <path>)
Description

Sets the path stored in the variable.
Required Argument

name The quoted name of the variable.
Optional Argument

path The path.
TripleS Import(path, <arguments>)
Description

Imports the specified Triple-S Survey (SSS) file. The SSS format consists of a pair of files:
.xml or .sss, and a .csv, .dat, or .asc file. Both sets of files must have the same root name and
be in the same folder.
Required Argument

path A quoted string that contains the full path to the .xml or .sss file.
Optional Arguments
"Invisible" A quoted keyword that hides the table from view. The data table appears

only in the JMP Home Window and the Window menu. Hidden data tables remain in
memory until they are explicitly closed, reducing the amount of memory that is
available to JMP. To explicitly close the hidden data table, call Close(dt), where dt is
the data table reference returned by TripleS Import.
Use Labels for Imported Column Names(Boolean) Converts the label names to
column headings. The default value is 1.
Example
dt = TripleS Import( "C:\Data\airlines.sss", "Invisible", Use Labels for
Imported Column Names( 0 ) );
