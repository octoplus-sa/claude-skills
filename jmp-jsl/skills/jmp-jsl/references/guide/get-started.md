# Get Started

Source: JMP 19 Scripting Guide (PDF pages 51-60).

## Index (line numbers in this file)

- `Continuous Distribution()` — L199
- `Distribution()` — L198
- `Estimation Method()` — L218
- `Frame3D()` — L214
- `Multivariate()` — L216
- `Scatterplot 3D()` — L212
- `Scatterplot Matrix()` — L219
- `Y()` — L213
---

Get Started
Let JMP Write Your Scripts
You often have to produce the same reports for the same data on a regular basis. This chapter
shows you how to let JMP write scripts for common tasks like importing text data, opening
Microsoft Excel files, and producing reports. A final tutorial shows you how to put it all
together into a single script to open an Microsoft Excel file and produce three reports
automatically.
The Scripting Guide is written for users who are familiar with JMP but might not be familiar
with JSL. For more information about performing common tasks, see Using JMP. Discovering
JMP is also a good resource for learning basic concepts and understanding the JMP workflow.

52

Get Started

Contents
Capture a Script for an Analysis Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
Capture a Script for a Data Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
Capture a Script to Import a File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
Glue Scripts Together . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56

Get Started
Capture a Script for an Analysis Report

53

Capture a Script for an Analysis Report
Here are the basic steps for capturing a script to reproduce an JMP analysis:
1. Launch a platform, such as Distribution.
2. Make any changes or additions that you need. For example, add tests and other graphs.
3. Capture the script to recreate your results.
You can save the script in the data table, so that if you send the data table to others, they can
run your script and duplicate your reports.

Example
Follow these steps to produce a distribution report, capture the script to reproduce it, and save
it to the data table.
Note: The data tables that you use in examples are located in JMP’s Samples/Data folder.
1. Select Help > Sample Data Folder and open Companies.jmp.
2. Select Analyze > Distribution to open the Distribution launch window.
3. Select Profits ($M) in the Select Columns box and click the Y, Columns button.
4. Click OK.
The Distribution report window appears.
5. Click the Distributions red triangle and select Stack to make your report horizontal.
6. Click the red triangle next to Profits ($M) and deselect Outlier Box Plot to turn the option
off.
7. Click the red triangle next to Profits ($M) and select Test Mean.
The Test Mean window appears.
8. Type 500 in the Specify Hypothesized Mean box.
9. Click OK.
The test for the mean is added to the report window.
Now you have your customized report.

54

Get Started
Capture a Script for a Data Table

Figure 3.1 Customized Distribution Report

10. Click the Distributions red triangle and select Save Script > To Data Table.
Your data table now has a script named Distribution saved to it. Right-click the
Distribution script and select Edit to see the script.
Figure 3.2 Distribution Script Saved to the Data Table

11. To run the script and reproduce your final report exactly, click the green triangle next to
the script.

Capture a Script for a Data Table
Here are the basic steps for capturing a script to reproduce a JMP data table:
1. Open the data table.

Get Started
Capture a Script to Import a File

2. Make any changes that you need. For example, add a script, correct values, add new
columns.
3. Capture the script to recreate your data table.

Example
Use the data table from the previous example, where you saved a script to it.
1. In the data table, select the red triangle next to the data table’s name.
2. Select Copy Table Script.
Figure 3.3 Copy the Table Script

3. Open a script window by selecting File > New > Script.
4. Select Edit > Paste.
You now have a script that duplicates your data table. You can save this script and run it at
any time to recreate your data table, with all its scripts attached.

Capture a Script to Import a File
When you open a non-JMP file in JMP, a script is automatically created and attached to the
data table. This script contains the code to open the file.

Import a Text File
1. Select File > Open.

55

56

Get Started
Glue Scripts Together

The Open Data File window appears.
2. Select Text Files from the list next to File name.
3. In the Open as section, select Data (Best Guess).
JMP formats the data based on tabs, commas, white space, and other characters in the text
file.
4. Browse to select the file, and then select Open.
The file is opened as a data table. The data table includes a script named Source. This JSL
script imports your text file with the text import rules that you used.
5. Right-click the Source script and select Edit.
You can copy this script, paste it into a new script window, and save it. Then you can run
this script later to reimport the text file.
Tip: The import script is an Open() expression that specifies the text file and the import
options to correctly import the file into JMP. The first part of this expression is the pathname to
the specific file that you imported. If you save this script and want to run it a different place,
you might need to edit the pathname so that it points to the text file. Pathnames are discussed
in greater detail in “Path Variables”.

Glue Scripts Together
Suppose new data is saved out to an Microsoft Excel file once a week, and you need to
produce the same reports every week. Instead of performing these steps manually, you can
create a script that imports the new Microsoft Excel file into JMP and automatically runs all
analyses. The following example shows you how to set up your script and run it each week.

Import the Microsoft Excel File
1. Open a new script window (File > New > Script).
2. In your script window, enter the Open() expression to open the Solubil.xlsx sample import
data file. The file is located in JMP’s Samples/Import Data folder.
dt = Open( "$SAMPLE_IMPORT_DATA/Solubil.xlsx" );

Be sure to put the semicolon at the end of this expression, because you will add more
expressions. The semicolon glues expressions together.
3. Run your script to import the Microsoft Excel file by selecting Edit > Run Script.
The Microsoft Excel file opens as a data table.

Get Started
Glue Scripts Together

57

Notes:
•

You can also include the Excel Wizard argument in the Open() expression to preview the
worksheet before importing it. See “Import Data from a Microsoft Excel File”.

•

You can specify an absolute or relative path to the file rather than using a path variable.
For relative links, the script and file being opened must be in the same relative location
each time you run the script. With absolute links, make sure that other users running the
script have access to the file’s location. See “Path Variables” for more information about
using pathnames.

Run Your Reports and Capture Their Scripts
You have three reports to produce: a distribution report, a 3D scatterplot, and a multivariate
report. Perform each one using the GUI, and add its script to the script window.
1. With your new data table open, select Analyze > Distribution.
2. Select all the columns except Labels and click Y, Columns.
3. Click OK.
4. Press Ctrl, click the eth red triangle, and then select Histogram Options > Show Counts.
Bar counts are added to all six histograms.
5. In the Distribution window, click the Distributions red triangle and select Save Script > To
Clipboard.
6. Click a line or two after your Open() expression and select Edit > Paste.
7. Type a semicolon after the last close parenthesis.
8. Select Graph > Scatterplot 3D.
9. Select all the columns except Labels and click Y, Columns.
10. Click OK.
11. Copy and paste the script for Scatterplot 3D into the script window just like you did for
your Distribution report. Be sure to add the semicolon at the end.
12. Select Analyze > Multivariate Methods > Multivariate.
13. Select all the columns except Labels and click Y, Columns.
14. Click OK.
15. Copy and paste the script for Multivariate into the script window just like you did for
Distributions and Scatterplot 3D.
You should see the following script:
dt = Open( "$SAMPLE_IMPORT_DATA/Solubil.xlsx" );
Distribution(
Continuous Distribution( Column( :eth ), Show Counts( 1 ) ),
Continuous Distribution( Column( :oct ), Show Counts( 1 ) ),

58

Get Started
Glue Scripts Together

Continuous Distribution( Column( :cc14 ), Show Counts( 1 ) ),
Continuous Distribution( Column( :c6c6 ), Show Counts( 1 ) ),
Continuous Distribution( Column( :hex ), Show Counts( 1 ) ),
Continuous Distribution( Column( :chc13 ), Show Counts( 1 ) ),
);
Scatterplot 3D(
Y( :eth, :oct, :cc14, :c6c6, :hex, :chc13 ),
Frame3D( Set Grab Handles( 0 ), Set Rotation( -54, 0, 38) )
);
Multivariate(
Y( :eth, :oct, :cc14, :c6c6, :hex, :chc13 ),
Estimation Method( "Row-wise" ),
Scatterplot Matrix( Density Ellipses( 0 ), Shaded Ellipses( 0 ) )
);

Save the Script
You now have a script that reproduces all of the steps that you performed manually. Save the
script, and close your data table and all its report windows.
1. In the script window that contains your script, select File > Save or File > Save As.
2. Specify a file name (for example, Weekly Report).
3. Click Save.

Run the Script
As long as your weekly updated Microsoft Excel file is saved in the same place and contains
the same columns, you can run your script and automatically produce all your reports.
1. Open the script that you saved.
2. Select Edit > Run Script.
Your Microsoft Excel file is opened in JMP, and all three of your reports appear.
You can send this script to others. As long as they have access to the same Microsoft Excel file
in the same location, they can also run the script in JMP and see your reports.

Advanced Note: Auto-Submit
If you want a particular script to always be executed instead of opened into the script window,
put the following command on the first line of the script:
//!

If this is not the very first line, with nothing else on the same line, this command does nothing.
You can override this command when opening the file.
1. Select File > Open.

Get Started
Glue Scripts Together

2. Press Ctrl, select the JSL file, and then click Open.
The script opens into a script window instead of being executed.
The command is also ignored when you right-click the file in the Home Window and select
Edit Script.

59

60

Get Started
Glue Scripts Together
