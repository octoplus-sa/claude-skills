# Creating Projects

Source: JMP 19 Scripting Guide (PDF pages 855-866).

## Index (line numbers in this file)

- `<< Add Bookmarks` — L100
- `<< Close Window` — L313
- `<< Reset Layout` — L396
- `<< Run Script` — L77
- `<< Save` — L194
- `<< Set Layout` — L127
- `Bivariate()` — L372
- `Continuous Distribution()` — L112
- `Distribution()` — L110
- `Elements()` — L121
- `Expanded()` — L281
- `File()` — L101
- `Get Project()` — L346
- `Get Window List()` — L323
- `Get Window()` — L225
- `Graph Builder()` — L115
- `Group()` — L279
- `H Splitter Box()` — L139
- `New Window()` — L333
- `Nominal Distribution()` — L113
- `Open()` — L106
- `Print()` — L353
- `Set Window ID()` — L108
- `Show Control Panel()` — L118
- `Size()` — L117
- `Tab Box()` — L165
- `Tab Page Box()` — L147
- `Title()` — L148
- `V Splitter Box()` — L128
- `Variables()` — L120
- `Wait()` — L224
- `Window ID()` — L149
---

Creating Projects
Organizing Project Files in JMP
A JMP project provides a way to organize files that you use in an analysis. You can add JMP
files (reports, data tables, scripts, journals, and so on) and non JMP files, such as Microsoft
Word or Adobe PDF files. After you perform an analysis, the data table, report, and graph
appear in the project on tabs. You can display multiple reports or graphs, display the project
or script editor log, and run scripts from the project. Reports and graphs remain linked to the
data table.
Projects help you avoid the clutter of several open JMP windows. You can maximize the
project window to have a bigger view of the project. And when you save the project, the state
of the project is saved (for example, the open reports and the layout of the window).

856

Creating Projects

Contents
Create a Simple Project. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 857
Create a Project with a Bookmarks Pane and Log . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 858
Run Scripts in a Project. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 860
Create a Bookmark Group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 862
Close Tabs in Projects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 863
Get a Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 863
Reset the Window Layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 864
Run Startup Scripts to Control Workspaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 865

Creating Projects
Create a Simple Project

857

Create a Simple Project
A JMP project provides a way to organize files that you use in an analysis and display the
output. A simple project might display the data table, graphs, and reports on separate tabs in
the project window.
project = New Project();
project << Run Script(
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Run Script( "Bivariate" );
dt << Run Script( "Distribution" );
);

Figure 16.1 shows the project with selected bars, showing that the graph is still linked to the
data table.
Figure 16.1 Example of a Simple Project

858

Creating Projects
Create a Project with a Bookmarks Pane and Log

Note: The best way to learn how to write a script for a project is to change the project
extension to .zip, open the zip file, and then look for a file called project.jsl in the root directory.

Create a Project with a Bookmarks Pane and Log
A more complicated JMP project might include a Bookmarks pane (to show file, folders, and
groups that use frequently), and a project log. The data table and output are in separate tabs.
Begin by creating a new project and creating a bookmark.
project = New Project();
project << Add Bookmarks({
File( "$SAMPLE_DATA/Big Class.jmp" )
});

Run Script opens the data table and creates output inside the project.
project << Run Script(
Open(
"$SAMPLE_DATA/Big Class.jmp",
Set Window ID( "data" ) // unique window ID
);
Distribution(
Set Window ID( "distrib" ),
Continuous Distribution( Column( :weight ) ),
Nominal Distribution( Column( :age ) )
);
Graph Builder(
Set Window ID( "graphbuilder" ),
Size( 443, 409 ),
Show Control Panel( 0 ),
Fit to Window( "Maintain Aspect Ratio" ),
Variables( X( :age ), Y( :height ), Y( :weight ) ),
Elements( Position( 1, 1 ), Line( X, Y, Legend( 1 ) ) ),
Elements( Position( 1, 2 ), Bar( X, Y, Legend( 2 ) ) )
);
);

Set Layout specifies the layout of the tabs that show the data table and output.
project << Set Layout(
V Splitter Box(
Size( 1215, 700 ),
<<Set Sizes( {0.77, 0.23} ),
<<Dockable(),
V Splitter Box(

Creating Projects
Create a Project with a Bookmarks Pane and Log
Size( 1215, 540 ),
<<Set Sizes( {1} ),
<<Dockable(),
H Splitter Box(
Size( 1215, 540 ),
<<Set Sizes( {0.11, 0.42, 0.47} ),
<<Dockable(),
V Splitter Box(
Size( 128, 540 ),
<<Set Sizes( {0.33, 0.33, 0.33} ),
<<Dockable(),
Tab Page Box(
Title( "Window List" ), // show the Window List
Window ID( "Window List" )
),
Tab Page Box(
Title( "Bookmarks" ), // show the Bookmarks pane
Window ID( "Bookmarks" )
),
Tab Page Box(
// show the Recent Files pane
Title( "Recent Files" ),
Window ID( "Recent Files" )
)
),
Tab Page Box( // show the data table
Title( "Big Class" ),
Window ID( "data" )
),
Tab Box(
<<Dockable(),
Tab Page Box( // show the Distribution graph and reports
Title( "Big Class - Distribution" ),
Window ID( "distrib" )
),
Tab Page Box( // show the Graph Builder graph
Title( "Big Class - Graph Builder" ),
Window ID( "graphbuilder" )
)
)
)
),
Tab Page Box( Title( "Log" ), Window ID( "Log" ) )
)

);

Save saves the project.

859

860

Creating Projects
Run Scripts in a Project

// if the project has already been saved, the Save message
// with no argument saves the file to the existing location
project << Save( "$DOCUMENTS/Big Class.jmpprj" );

Note: If youʹre saving a project with unsaved documents in JSL, the project doesnʹt close and
you get a log message that the project has unsaved documents. All files in a project must be
saved or closed before the project can be saved. However, if you interactively save a project
with unsaved documents, you are prompted to save the documents.
Figure 16.2 Example of a Complex Project

Open the project from another script:
project = Open( "Big Class.jmpprj" );

In this example, the script that you are running to open the project is in the same folder as the
project.

Run Scripts in a Project
When you run a script outside of a JMP project, the reports generated by the script appear in
different windows. When you run a script inside a project, the reports appear in different tabs
inside the project.

Creating Projects
Run Scripts in a Project

861

Running a JSL script outside of a project
Open a Script Editor window by selecting File > New > Script. Paste and run the following
script:
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Run Script( "Bivariate" );
dt << Run Script( "Distribution" );
Wait( 2 );
Get Window( "Big Class - Distribution" ) << Close Window();

Note that this script opens three JMP windows: one for the data table and one for each report.
Close the reports and then the data table.

Running a JSL script inside of a project
Create a new project by selecting File > New > Project. From the project window, create a new
script editor window by selecting File > New > Script. Note that the script editor window
opens as a tab in the project. Paste the same JSL script you previously ran into the script editor
and run it:
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Run Script( "Bivariate" );
dt << Run Script( "Distribution" );
Wait( 2 );
Get Window( "Big Class - Distribution" ) << Close Window();

Note that this time, the data table and the reports all opened as tabs in the project, and that
Get Window() correctly found the distribution tab. In general, all JSL functions that open,
find, manipulate, and close JMP windows, tables, and reports work from within a project the
same as they would outside projects.

Running a JSL script using a project’s Run Script message
You can use the Run Script message to run JSL in the project’s context. Open a Script Editor
window, then paste and run the following code:
project = New Project();
project << Run Script(
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Run Script( "Bivariate" );
dt << Run Script( "Distribution" );
Wait( 2 );
Get Window( "Big Class - Distribution" ) << Close Window();
);

Note that the script inside the Run Script message runs the same as if it had been in a script
editor window inside the project.

862

Creating Projects
Create a Bookmark Group

Scoping Variables
JMP can have several projects open at the same time, as well as items not open in any project.
Each project has its own global scope, which prevents conflicts caused by identically named
variables in different projects. In the rare case that you do want to share specific variables
among all opened projects, use the ::: root operator.

Create a Bookmark Group
You can create bookmark groups to organize the bookmarks in a JMP project. A bookmark
group can contain bookmarked files, folder, and additional bookmark groups. The bookmark
group exists only in the project, not on your computer. Use Group() to create the bookmark
group.
project = New Project();
project << Add Bookmarks(
Group(
"Sample Data",
Expanded( 1 ), // open the group
{File( "$SAMPLE_DATA/Air Traffic.jmp" ),
File( "$SAMPLE_DATA/Big Class.jmp" )}
)
);
project << Set Layout(
H Splitter Box(
<<Set Sizes( {0.15, 0.85} ),
Tab Page Box( Window ID( "Bookmarks" ), )
)
);
project << Save( "$DOCUMENTS/My Project.jmpprj" );

Figure 16.3 “Sample Data” Group in a Project

Creating Projects
Close Tabs in Projects

863

Close Tabs in Projects
Close a tab in a JMP project by identifying the window with Get Window() and then closing it
with Close Window.
project = New Project();
project << Run Script(
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Run Script( "Bivariate" );
dt << Run Script( "Distribution" );
);
Wait( 2 ); // for demonstration purposes
// returns a reference to the open "Big Class - Distribution" window
dist = Get Window( Project( project ), "Big Class - Distribution" ) ;
dist << Close Window();

To close all tabs in a project, use Get Window List << Close Window().
project = New Project();
project << Run Script(
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Run Script( "Bivariate" );
dt << Run Script( "Distribution" );
);
Wait( 2 ); // for demonstration purposes
Get Window List( Project( project ) ) << Close Window();

Get a Project
When running a JSL script from within a project, you can use the This Project() function to
obtain that project. The following example displays the name of the current project in a new
window.
project = This Project();
If( Is Empty( project ),
/* if the script is not run from a project, display this
sentence in the new window */
New Window( "My Project", Text Box( "Script isn’t running in a project." )
),

864

Creating Projects
Reset the Window Layout

/* if the script is run from a project, display the window title
in the new window */
New Window( "My Project", Text Box( project << Get Window Title() ) )
);

Get Project() takes the same arguments as the Window() function. Omit the arguments to

get a list of the currently open projects, include a string to find a specific project by title, or
include a number to get the ith open project.
Open( "$SAMPLE_PROJECTS/Big Class.jmpprj" );
Open( "$SAMPLE_PROJECTS/Sports.jmpprj" );
// print the title of Sports.jmpprj
Print( Get Project( 2 ) << Get Window Title() );

Get Project() is also helpful when you want to save a project or set the layout from within

the project.
Get Project() << Save(...);
Get Project() << Set Layout(...);

Reset the Window Layout
Suppose that you create a JMP project and customize the layout of the windows. For example,
you might hide the Window List. Use the Reset Layout message to return the windows to
their original layout.
project = New Project();
project << Run Script( // open data table and create a graph
Open(
"$SAMPLE_DATA/Big Class.jmp", Set Window ID( "data" )
);
New Window( "Big Class - Bivariate of weight by height",
Set Window ID( "bivariate" ),
Bivariate(Y( :weight ), X( :height ),
)
) << Set Window Icon( "Bivariate" );
);
Wait(3); // for demonstration purposes
project << Set Layout( // set a custom layout
H Splitter Box(
<<Set Sizes( {0.2, 0.8} ),
Tab Page Box( Window ID( "Bookmarks" ) ), V Splitter Box(
<<Set Sizes( {0.53, 0.47} ),

Creating Projects
Run Startup Scripts to Control Workspaces

865

Tab Page Box(
Window ID( "bivariate" ) ),
Tab Page Box(
Window ID( "data" ) )
)
)
);
Wait( 3 ); // for demonstration purposes
project << Reset Layout(); // return to the original layout

Run Startup Scripts to Control Workspaces
A workspace is either a project window or the windows that are not in a project (for example,
the home window). A default workspace loads when JMP starts, and then each time you
create or open a project, JMP creates another workspace.
Consider writing a workspace startup script to customize variables for a specific project. You
might also construct a new customized window in a workspace startup script to put a copy of
that window in each project. This is an alternative to having a single copy of the script that
runs outside of projects.
The workspace startup script runs each time a new workspace loads. This means that the
workspace startup script runs once when JMP starts (when the “default workspace” loads)
and then runs again each time a new project is loaded. The workspace startups script runs in
the context of the project, so any windows it opens or variables it sets are for that project only.
Name the script workspaceStart.jsl and place it in one of the following folders, as appropriate
for your operating system. When JMP starts, JMP looks for the workspaceStart.jsl script in
these folders in the order in which they are listed here. The first one that is found is run, and
the search immediately stops.
Note: Some path names in this section refer to the “JMP” folder. On Windows, in JMP Pro, the
“JMP” folder is named “JMPPro”.
On Windows:
1. C:\Users\<username>\AppData\Roaming\JMP\JMP\19
2. C:\Users\<username>\AppData\Roaming\JMP\JMP

On Apple macOS:
1. /Users/<username>/Library/Application Support/JMP/19
2. /Users/<username>/Library/Application Support/JMP

866

Creating Projects
Run Startup Scripts to Control Workspaces

The workspaceStart.jsl script runs only for a particular user on a computer. You can add a
script named workspaceStartAdmin.jsl in one of the following places, as appropriate for your
operating system. This script is run for every user on a computer. JMP runs
workspaceStartAdmin.jsl first if found. Then JMP runs workspaceStart.jsl if found.
On Windows:
1. C:\ProgramData\JMP\JMP\19
2. C:\ProgramData\JMP\JMP

On Apple macOS:
1. /Library/Application Support/JMP/19
2. /Library/Application Support/JMP
