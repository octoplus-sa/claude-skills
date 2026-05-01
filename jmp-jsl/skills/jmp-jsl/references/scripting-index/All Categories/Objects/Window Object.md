# Window Object

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Window%20Object.html](https://jsl.jmp.com/All%20Categories/Objects/Window%20Object.html)*

---

# [Window Object](#window-object)[](#window-object "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Set Window Title](#set-window-title)[](#set-window-title "Click to copy url")

**Syntax:** obj \<\< Set Window Title

**Description:** Sets the window title.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Set Window Title( "New Title" );
```

## [Shared Item Messages](#shared-item-messages)[](#shared-item-messages "Click to copy url")

### [Bring Window To Front](#bring-window-to-front)[](#bring-window-to-front "Click to copy url")

**Syntax:** obj \<\< Bring Window To Front

**Description:** Brings the window to the front.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Run Script( "Bivariate" );
w << Bring Window To Front;
```

### [Close Window](#close-window)[](#close-window "Click to copy url")

**Syntax:** obj \<\< Close Window( \<"NoSave"\> )

**Description:** Closes the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
w << Close Window;
```

### [Get Content Size](#get-content-size)[](#get-content-size "Click to copy url")

**Syntax:** obj \<\< Get Content Size

**Description:** Returns the content size within the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
c = w << Get Content Size();
Show( c );
```

### [Get On Close](#get-on-close)[](#get-on-close "Click to copy url")

**Syntax:** obj \<\< Get On Close

**Description:** Returns the script or function that will run when the window closes.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << On Close(
    // Modal dialogs return Button(1) if OK is pressed, Button(-1) if canceled
    New Window( "Are you sure?",
        <<modal,
        V List Box(
            Text Box( "Press OK to allow the window to close" ),
            H List Box( Button Box( "OK" ), Button Box( "Cancel" ) )
        )
    )["button"] == 1
);
Show( w << Get On Close );
```

### [Get Page Setup](#get-page-setup)[](#get-page-setup "Click to copy url")

**Syntax:** obj \<\< Get Page Setup

**Description:** Get page setup information for PDF

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Page Setup Test" ) );
w << get page setup();
```

### [Get Project](#get-project)[](#get-project "Click to copy url")

**Syntax:** project = obj \<\< Get Project()

**Description:** Returns the parent project of the window, or Empty() if it is not in a project.

**JMP Version Added:** 14

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
c = w << Get Project();
Show( c );
```

### [Get Show Window](#get-show-window)[](#get-show-window "Click to copy url")

**Syntax:** obj \<\< Get Show Window

**Description:** Returns the visibility of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Show Window( 0 );
Wait( 2 );
Print( w << Get Show Window() );
```

### [Get Web Support](#get-web-support)[](#get-web-support "Click to copy url")

**Syntax:** obj \<\< Get Web Support

**Description:** Return a number indicating the level of Interactive HTML support for the display object. 1 means some or all elements are supported. 0 means no support.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Bivariate( Y( :Weight ), X( :Height ) );
s = obj << Get Web Support();
Show( s );
```

### [Get Window Icon](#get-window-icon)[](#get-window-icon "Click to copy url")

**Syntax:** obj \<\< Get Window Icon

**Description:** Returns the window icon.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
t = w << Get Window Icon;
Show( t );
```

### [Get Window Position](#get-window-position)[](#get-window-position "Click to copy url")

**Syntax:** obj \<\< Get Window Position

**Description:** Returns the position of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
p = w << Get Window Position();
Show( p );
```

### [Get Window Size](#get-window-size)[](#get-window-size "Click to copy url")

**Syntax:** obj \<\< Get Window Size

**Description:** Returns the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = w << Get Window Size();
Show( s );
```

### [Get Window Title](#get-window-title)[](#get-window-title "Click to copy url")

**Syntax:** obj \<\< Get Window Title

**Description:** Returns the window title.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
t = w << Get Window Title;
Show( t );
```

### [Get Window View](#get-window-view)[](#get-window-view "Click to copy url")

**Syntax:** obj \<\< Get Window View

**Description:** Returns the current window view. Windows can be "Visible", "Invisible", or "Private".

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Print( w << Get Window View() );
```

### [Is Modal Dialog](#is-modal-dialog)[](#is-modal-dialog "Click to copy url")

**Syntax:** obj \<\< Is Modal Dialog

**Description:** Returns true if the window is a modal dialog. Only useful when called from a window handler callback.

``` jsl
With Window Handler(
    New Window( "Modal Window", <<Modal ),
    Function( {win},
        Print( win << Is Modal Dialog() );
        win << close window();
    )
);
```

### [Maximize Window](#maximize-window)[](#maximize-window "Click to copy url")

**Syntax:** obj \<\< Maximize Window( \<state=0\|1\> )

**Description:** Maximizes the window. Default argument is 1.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Maximize Window( 1 );
Wait( 1 );
w << Maximize Window( 0 );
```

### [Minimize Window](#minimize-window)[](#minimize-window "Click to copy url")

**Syntax:** obj \<\< Minimize Window( \<state=0\|1\> )

**Description:** Minimizes the window. Default argument is 1.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Minimize Window( 1 );
Wait( 1 );
w << Minimize Window( 0 );
```

### [Move Window](#move-window)[](#move-window "Click to copy url")

**Syntax:** obj \<\< Move Window( x,y )

**Description:** Moves the window to the specified position.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
w << Move Window( 500, 500 );
```

### [On Close](#on-close)[](#on-close "Click to copy url")

**Syntax:** obj \<\< On Close( script )

**Description:** Sets a script or function to run upon closing the window. This script should return 1 to allow the close, or 0 to prevent the window from closing.

#### [Close Function](#close-function)[](#close-function "Click to copy url")

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << On Close(
    Function( {this}, 
        // Modal dialogs return Button(1) if OK is pressed, Button(-1) if cancelled
        New Window( "Are you sure?",
            <<modal,
            V List Box(
                Text Box( "Press OK to allow " || (this << Get Window Title) || " to close" ),
                H List Box( Button Box( "OK" ), Button Box( "Cancel" ) )
            )
        )["button"] == 1
    )
);
```

#### [Close Script](#close-script)[](#close-script "Click to copy url")

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << On Close(
    // Modal dialogs return Button(1) if OK is pressed, Button(-1) if canceled
    New Window( "Are you sure?",
        <<modal,
        V List Box(
            Text Box( "Press OK to allow the window to close" ),
            H List Box( Button Box( "OK" ), Button Box( "Cancel" ) )
        )
    )["button"] == 1
);
```

### [Optimize Display](#optimize-display)[](#optimize-display "Click to copy url")

**Syntax:** obj \<\< Optimize Display

**Description:** Sets a data table's column widths and window to an optimum size.

**JMP Version Added:** 14

``` jsl
//This message applies to Data Table objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Optimize Display;
```

### [Pad Window](#pad-window)[](#pad-window "Click to copy url")

**Syntax:** obj \<\< Pad Window( bool )

**Description:** Turns window padding on or off.

``` jsl
//This message applies to all display box objects
Open( "$SAMPLE_DATA/Big Class.jmp" );
d = distribution( Column( :height ) );
r = d << report;
r << Pad Window( 0 );
```

### [Print Window](#print-window)[](#print-window "Click to copy url")

**Syntax:** obj \<\< Print Window

**Description:** Prints the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Print Window;
```

### [Save Window Report](#save-window-report)[](#save-window-report "Click to copy url")

**Syntax:** obj \<\< Save Window Report( pathname, \<embed data(0\|1)\> )

**Description:** Saves the current report window to a JMP report file (.jrp).

**JMP Version Added:** 16

``` jsl
//This message can be sent to any display box object but will be applied to the report window
Open( "$SAMPLE_DATA/Big Class.jmp" );
d = distribution( Column( :height ) );
d << Save Window Report( "$DOCUMENTS/test.jrp", embed data( 1 ) );
```

### [Set Content Size](#set-content-size)[](#set-content-size "Click to copy url")

**Syntax:** obj \<\< Set Content Size( x,y )

**Description:** Sets the content size within the window.

``` jsl
//This message applies to all display box objects
w = New Window( "Test",
    lb = List Box( {"a", "b", "c", "d"} ),
    Button Box( "Enable 2nd item",
        lb << enable item( 2, 1 );
        Show( lb << item enabled( 2 ) );
    ),
    Button Box( "Disable 2nd item",
        lb << enable item( 2, 0 );
        Show( lb << item enabled( 2 ) );
    )
);
Wait( 2 );
w << Set Content Size( 400, 300 );
```

### [Set Main Window](#set-main-window)[](#set-main-window "Click to copy url")

**Syntax:** obj \<\< Set Main Window

**Description:** Set the window to be the main window in JMP and sets the prior main window to be a normal window

``` jsl
//This message applies to all display box objects
w = New Window( "Main Window", Text Box( "Main JMP Window" ) );
w << Set Main Window;
```

### [Set Page Setup](#set-page-setup)[](#set-page-setup "Click to copy url")

**Syntax:** obj \<\< Set Page Setup( \<margins(left, top, right, bottom)\>, \<scale(s)\>, \<portrait(0\|1)\>, \<paper size(p)\>, \<Table of Contents(always, never, default)\> )

**Description:** Sets the page setup information that is used during printing or saving as pdf. A Table of Contents can optionally be generated from Outline Boxes.

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Outline Box( "TOC", Text Box( "Page Setup Test" ) ) );
w << Set page setup(
    margins( 1, 1, 1, 1 ),
    scale( 1 ),
    portrait( 1 ),
    paper size( "Letter" ),
    Table of Contents( "always" )
);
w << Save pdf( "$DOCUMENTS\test.pdf" );
```

### [Set Print Footers](#set-print-footers)[](#set-print-footers "Click to copy url")

**Syntax:** obj \<\< Set Print Footers( left footer, center footer, right header )

**Description:** Sets the left, center, and right footers for printed output

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Footer Test" ) );
w << Set Print Footers(
    "Today is: &d;"/*left*/, "&wt;"/*center*/,
    "Page &pn; of &pc;"/*right*/
);
w << Print Window;
```

### [Set Print Headers](#set-print-headers)[](#set-print-headers "Click to copy url")

**Syntax:** obj \<\< Set Print Headers( left header, center header, right header )

**Description:** Sets the left, center, and right headers for printed output

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Header Test" ) );
w << Set Print Headers(
    "Today is: &d;"/*left*/, "&wt;"/*center*/,
    "Page &pn; of &pc;"/*right*/
);
w << Print Window;
```

### [Set Window Icon](#set-window-icon)[](#set-window-icon "Click to copy url")

**Syntax:** obj \<\< Set Window Icon( icon name )

**Description:** Sets the window icon.

``` jsl
//This message applies to all display box objects
w = New Window( "Example", ex = Button Box( "New Analysis" ) );
w << Set Window Icon( "Scatter3D" );
```

### [Set Window Size](#set-window-size)[](#set-window-size "Click to copy url")

**Syntax:** obj \<\< Set Window Size( x,y )

**Description:** Sets the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Set Window Size( 800, 1200 );
```

### [Show Window](#show-window)[](#show-window "Click to copy url")

**Syntax:** obj \<\< Show Window( state=0\|1 )

**Description:** Shows or hides the window. This is useful for hiding windows temporarily. On by default.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Show Window( 0 );
Wait( 2 );
w << Show Window( 1 );
```

### [Size Window](#size-window)[](#size-window "Click to copy url")

**Syntax:** obj \<\< Size Window( x,y )

**Description:** Sets the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Size Window( 500, 500 );
```

### [Zoom Window](#zoom-window)[](#zoom-window "Click to copy url")

**Syntax:** obj \<\< Zoom Window

**Description:** Resizes the window to be large enough to show all of its contents.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Set Window Size( 80, 120 );
Wait( 2 );
w << Zoom Window;
```

[ Previous](WebReport.html "WebReport") [Next ](Workflow.html "Workflow")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
