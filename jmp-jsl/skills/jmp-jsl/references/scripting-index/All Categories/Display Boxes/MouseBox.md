# MouseBox

*Source: [https://jsl.jmp.com/All%20Categories/Display%20Boxes/MouseBox.html](https://jsl.jmp.com/All%20Categories/Display%20Boxes/MouseBox.html)*

---

# [MouseBox](#mousebox)[](#mousebox "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Mouse Box](#mouse-box)[](#mouse-box "Click to copy url")

**Syntax:** box = MouseBox( displayBoxArgs )

**Description:** Returns a box that can make JSL callbacks for mouse actions

``` jsl
New Window( "Example",
    MouseBox(/*first sibling*/Text Box( "drag from here" ),
        <<setDragText( "hello" ),
        <<setTooltip( "source" ),
        <<setDragEnable( 1 ),
        <<setDragBegin(/* decide if a drag is allowed */
            Function( {this, clickpt},
                "magic text";/* 0.0 to prevent the drag.  1.0 is the same as 'this<<getDragText' */
            )
        ),
        <<setDragEnd(/* clean up after a drag finishes or cancels */
            Function( {this, clickpt, how}, /* how=move,copy,ignore */
                If(
                    how != "ignore" & !Is Empty( this << getDestBox ) & this << getDestBox
                     == this << sib, /* the getDestBox check makes sure the destination of the drag-and-drop was my sibling and not some other program beyond our control */
                    (this << child) << setText(
                        "done!" /* 'move' suggests clearing the source */
                    )
                )
            )
        )
    ),
    MouseBox(/*second sibling*/Text Box( "drag to here" ),
        <<setTooltip( "destination" ),
        <<setDropEnable( 1 ),
        <<setDropTrack(/* decide if dropping is allowed, before the drop.  The getSourceBox check makes sure the source of the drag-and-drop is my sibling, and not some other program */
            Function( {this, clickpt},
                If( !Is Empty( this << getSourceBox ) & this == (this << getSourceBox) << sib,
                    1, /*else*/0
                )
            )
        ),
        <<setDropCommit(/* accept the drop */Function( {this, clickpt, text},
                (this << child) << setText( text )
            )
        )
    )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [GetChildBox](#getchildbox)[](#getchildbox "Click to copy url")

**Syntax:** GetChildBox( { x, y } \| \[ x y \] \| x, y )

**Description:** returns a list of zero or more nested display boxes: { child, grand-child, great-grand-child, ... } at the specified coordinates within this mouse box. In many cases it might be simpler to use a separate mouse box around each child.

``` jsl
New Window( "MouseBox",
    Text Box( "Move the mouse around" ),
    MouseBox(
        Lineup Box( N Col( 2 ), 
            /*pre-load the spacer boxes with a color, but make them transparent as well so the color won't show*/
            s1 = Spacer Box( size( 50, 50 ), <<Color( "red" ), <<SetFill( 0 ) ),
            s2 = Spacer Box( size( 50, 50 ), <<Color( "green" ), <<SetFill( 0 ) ),
            s3 = Spacer Box( size( 50, 50 ), <<Color( "blue" ), <<SetFill( 0 ) ),
            Lineup Box( N Col( 2 ), 
                /*demonstrate nested boxes*/
                s4 = Spacer Box( size( 24, 24 ), <<Color( "red" ), <<SetFill( 0 ) ),
                s5 = Spacer Box( size( 24, 24 ), <<Color( "green" ), <<SetFill( 0 ) ),
                s6 = Spacer Box( size( 24, 24 ), <<Color( "blue" ), <<SetFill( 0 ) ),
                s7 = Spacer Box( size( 24, 24 ), <<Color( "yellow" ), <<SetFill( 0 ) )
            )
        ), 
        /*set up a callback function to track the mouse movements*/
        <<SetTrackEnable( 1 ),
        <<SetTrack(
            Function( {this, clickpt}, /*clickpt is really the move point*/
/*on each mouse move, make children transparent*/
                s1 << setfill( 0 );
                s2 << setfill( 0 );
                s3 << setfill( 0 );
                s4 << setfill( 0 );
                s5 << setfill( 0 );
                s6 << setfill( 0 );
                s7 << setfill( 0 );
                /*retrieve a list of boxes under the clickpt (which is a mouse coordinate within the mouse box like {10,20})*/
                childBoxList = this << GetChildBox( clickpt );
                /* child 1 is the LineupBox.  child 2, if present, is one of the Spacer Boxes */
                If(
                    N Items( childBoxList ) > 0 & (childBoxList[N Items( childBoxList )]) <<
                    className == "SpacerBox", 
                    /*if a SpacerBox is under the mouse, make it opaque*/
                    childBoxList[N Items( childBoxList )] << SetFill( 1 )
                );
            )
        )
    )
);
```

### [GetClick](#getclick)[](#getclick "Click to copy url")

**Syntax:** obj \<\< GetClick

**Description:** returns the function from \<\<SetClick

``` jsl
mb = MouseBox();
mb << setClick( Function( {this, clickPt, event}, Print( 42 ) ) );
mb << getClick();
```

### [GetClickEnable](#getclickenable)[](#getclickenable "Click to copy url")

**Syntax:** obj \<\< GetClickEnable

**Description:** report the value set by SetClickEnable

``` jsl
mb = MouseBox();
mb << setClickEnable( 1 );
mb << getClickEnable();
```

### [GetDefaultCursor](#getdefaultcursor)[](#getdefaultcursor "Click to copy url")

**Syntax:** obj \<\< GetDefaultCursor

**Description:** retrieves the value specified by SetDefaultCursor

### [GetDefaultCursorEnable](#getdefaultcursorenable)[](#getdefaultcursorenable "Click to copy url")

**Syntax:** obj \<\< GetDefaultCursorEnable

**Description:** retrieves the value specified by SetDefaultCursorEnable

### [GetDestBox](#getdestbox)[](#getdestbox "Click to copy url")

**Syntax:** obj \<\< GetDestBox

### [GetDragBegin](#getdragbegin)[](#getdragbegin "Click to copy url")

**Syntax:** obj \<\< GetDragBegin

**Description:** returns the function specified by \<\<SetDragBegin

### [GetDragEnable](#getdragenable)[](#getdragenable "Click to copy url")

**Syntax:** obj \<\< GetDragEnable

**Description:** ask if the MouseBox is currently allowed to source drag-and-drop operations

``` jsl
mb = MouseBox();
mb << GetDragEnable;
```

### [GetDragEnd](#getdragend)[](#getdragend "Click to copy url")

**Syntax:** obj \<\< GetDragEnd

**Description:** returns the function specified by \<\<SetDragEnd

### [GetDragText](#getdragtext)[](#getdragtext "Click to copy url")

**Syntax:** obj \<\< GetDragText

**Description:** Not normally needed. Returns the text supplied by SetDragText, which might not be the text sent to the drop point.

``` jsl
mb = MouseBox();
mb << setDragText( "1000 words" );
mb << getDragText;
```

### [GetDropCommit](#getdropcommit)[](#getdropcommit "Click to copy url")

**Syntax:** obj \<\< GetDropCommit

**Description:** returns the function set by \<\<setDropCommit

``` jsl
mb = MouseBox();
mb << setDropCommit( Function( {this, clickPt, text}, Print( 42 ) ) );
mb << getDropCommit();
```

### [GetDropEnable](#getdropenable)[](#getdropenable "Click to copy url")

**Syntax:** obj \<\< GetDropEnable

**Description:** reports the value stored by \<\<SetDropEnable

``` jsl
mb = MouseBox();
mb << setDropEnable( 1 );
mb << getDropEnable();
```

### [GetDropTrack](#getdroptrack)[](#getdroptrack "Click to copy url")

**Syntax:** obj \<\< GetDropTrack

**Description:** returns the function set by \<\<setDropTrack

``` jsl
mb = MouseBox();
mb << setDropTrack( Function( {this, clickPt}, Print( 42 ) ) );
mb << getDropTrack();
```

### [GetEdit](#getedit)[](#getedit "Click to copy url")

**Syntax:** obj \<\< GetEdit

### [GetEditClear](#geteditclear)[](#geteditclear "Click to copy url")

**Syntax:** obj \<\< GetEditClear( state=0\|1 )

### [GetEditCopy](#geteditcopy)[](#geteditcopy "Click to copy url")

**Syntax:** obj \<\< GetEditCopy( state=0\|1 )

### [GetEditCopyLabel](#geteditcopylabel)[](#geteditcopylabel "Click to copy url")

**Syntax:** obj \<\< GetEditCopyLabel( state=0\|1 )

### [GetEditCopyText](#geteditcopytext)[](#geteditcopytext "Click to copy url")

**Syntax:** obj \<\< GetEditCopyText( state=0\|1 )

### [GetEditCut](#geteditcut)[](#geteditcut "Click to copy url")

**Syntax:** obj \<\< GetEditCut( state=0\|1 )

### [GetEditEnable](#geteditenable)[](#geteditenable "Click to copy url")

**Syntax:** obj \<\< GetEditEnable

### [GetEditJournal](#geteditjournal)[](#geteditjournal "Click to copy url")

**Syntax:** obj \<\< GetEditJournal( state=0\|1 )

### [GetEditPaste](#geteditpaste)[](#geteditpaste "Click to copy url")

**Syntax:** obj \<\< GetEditPaste( state=0\|1 )

### [GetEditPasteJSL](#geteditpastejsl)[](#geteditpastejsl "Click to copy url")

**Syntax:** obj \<\< GetEditPasteJSL( state=0\|1 )

### [GetEditPasteLabel](#geteditpastelabel)[](#geteditpastelabel "Click to copy url")

**Syntax:** obj \<\< GetEditPasteLabel( state=0\|1 )

### [GetEditSaveSelectionAs](#geteditsaveselectionas)[](#geteditsaveselectionas "Click to copy url")

**Syntax:** obj \<\< GetEditSaveSelectionAs( state=0\|1 )

### [GetEditSubmit](#geteditsubmit)[](#geteditsubmit "Click to copy url")

**Syntax:** obj \<\< GetEditSubmit( state=0\|1 )

### [GetEditSubmitDebug](#geteditsubmitdebug)[](#geteditsubmitdebug "Click to copy url")

**Syntax:** obj \<\< GetEditSubmitDebug( state=0\|1 )

### [GetFocus](#getfocus)[](#getfocus "Click to copy url")

**Syntax:** obj \<\< GetFocus

### [GetKey](#getkey)[](#getkey "Click to copy url")

**Syntax:** obj \<\< GetKey

**Description:** Returns the function set by Set Key.

``` jsl
New Window( "SetKey Example", mb = MouseBox( tb = Text Box( "Press a key." ) ) );
mb << setkey(
    Function( {this, key},
        tb << settext( key );
        1;
    )
);
mb << setkeyenable( 1 );
mb << setfocus;
Show( mb << GetKey );
```

### [GetKeyEnable](#getkeyenable)[](#getkeyenable "Click to copy url")

**Syntax:** obj \<\< GetKeyEnable

### [GetMark](#getmark)[](#getmark "Click to copy url")

**Syntax:** obj \<\< GetMark

**Description:** retrieves the value specified by \<\<SetMark

``` jsl
New Window( "Mouse Box", mb = MouseBox( Text Box( "Text" ) ) );
mb << setMarkEnable( 1 );
mb << setMark( Function( {this}, this << Set Marked( !(this << Get Marked) ) ) );
mb << GetMark;
```

### [GetMarkEnable](#getmarkenable)[](#getmarkenable "Click to copy url")

**Syntax:** obj \<\< GetMarkEnable

**Description:** retrieves value set by \<\<SetMarkEnable

``` jsl
New Window( "Mouse Box", mb = MouseBox( Text Box( "Text" ) ) );
mb << setMarkEnable( 1 );
mb << getMarkEnable();
```

### [GetMarked](#getmarked)[](#getmarked "Click to copy url")

**Syntax:** obj \<\< GetMarked

**Description:** Returns the current marked flag.

``` jsl
New Window( "Mouse Box", mb = MouseBox( Text Box( "Text" ) ) );
mb << setMarkEnable( 1 );
mb << setMarked();
mb << getMarked();
```

### [GetSourceBox](#getsourcebox)[](#getsourcebox "Click to copy url")

**Syntax:** obj \<\< GetSourceBox

### [GetToolTip](#gettooltip)[](#gettooltip "Click to copy url")

**Syntax:** obj \<\< GetToolTip

**Description:** Not normally needed. Returns the text supplied by SetTooltip. Tooltips are automatic and don't need this message.

``` jsl
mb = MouseBox();
mb << setTooltip( "this is your best choice" );
mb << getTooltip;
```

### [GetTrack](#gettrack)[](#gettrack "Click to copy url")

**Syntax:** obj \<\< GetTrack

**Description:** retrieves the value specified by \<\<SetTrack

``` jsl
mb = MouseBox();
mb << setTrack(/*track the button-up mouse movement*/Function( {this, clickPt},
        Print( 42 )
    )
);
mb << getTrack();
```

### [GetTrackEnable](#gettrackenable)[](#gettrackenable "Click to copy url")

**Syntax:** obj \<\< GetTrackEnable

**Description:** retrieves value set by \<\<SetTrackEnable

``` jsl
mb = MouseBox();
mb << setTrackEnable( 1 );
mb << getTrackEnable();
```

### [GetUserData](#getuserdata)[](#getuserdata "Click to copy url")

**Syntax:** obj \<\< GetUserData

**Description:** retrieves the value stored by \<\<SetUserData

``` jsl
mb = MouseBox();
mb << setUserData( [1 2, 3 4] );
(mb << getUserData())[2, 1];
```

### [RemoveFocus](#removefocus)[](#removefocus "Click to copy url")

**Syntax:** obj \<\< RemoveFocus

### [SetClick](#setclick)[](#setclick "Click to copy url")

**Syntax:** obj \<\< SetClick( Function( {this, clickpt, event}, \<script\> ) )

**Description:** Supplies a function to handle mouse events when the button is down (or first pressed or released). For button-up, see \<\<SetTrack(). clickpt is an {x,y} position within this MouseBox that was clicked. event is the click event. Values are (in the order in which they happen): "Pressed", "Ticked", or "Released".

``` jsl
xsize = 300; /* size of the bitmap */
ysize = 200;
backred = .8; /* background color is light gray-green */
backgrn = .9;
backblu = .8;
RED = J( ysize, xsize, backred ); /* matrix where the bitmap is composed */
GRN = J( ysize, xsize, backgrn );
BLU = J( ysize, xsize, backblu );
BITMAP = New Image( xsize, ysize ); /* displaybox that holds the bitmap */
BITMAP << setpixels( "rgb", {RED, GRN, BLU} ); /* initialize bitmap */
drawline = Function( {x0, y0, x1, y1}, /* utility function to draw a line in an array using matrix operations */
    {dx = x1 - x0, dy = y1 - y0, adx = Abs( dx ), ady = Abs( dy ), m, b},
    If( adx > ady,
        xx = Round( x0 ) :: Round( x1 );
        m = dy / dx;
        b = y0 - m * x0;
        yy = Round( xx * m + b );
    ,
        yy = Round( y0 ) :: Round( y1 );
        m = dx / dy;
        b = x0 - m * y0;
        xx = Round( yy * m + b );
    );
    singleindex = (yy - 1) * N Col( GRN ) + xx;
    Try( GRN[singleindex] = .6, 0 ); /* catch indexing errors and ignore the problems */
    Try( RED[singleindex] = .1, 0 ); /* the line is dark green; you could add other */
    Try( BLU[singleindex] = .1, 0 ); /* controls to change the color. */
);
w = New Window( "paint",
    MouseBox( /* <<<<<<<< handler for mouse events */
        BITMAP, /* <<<<<< child box does not receive the mouse events */
        <<setTrackEnable( 1 ),
        <<setTrack(
            Function( {this, clickpt},
                this << setCursor( "Hand" ) /* button-up tracking - use the hand */
            )
        ),
        <<setClickEnable( 1 ),
        <<setClick( /* button-down, move, button-release handler */
            Function( {this, clickpt, event}, /*Is Alt Key(),Is Control Key(),Is Shift Key() should be captured on "Pressed" */
                If( event == "Released" | event == "Canceled",
                    this << setCursor( "Hand" ) /* switch back to hand immediately */
                ,
                    this << setCursor( "Finger" ) /* change cursor during drawing */
                );
                If(
                    event == "Pressed",
                        origin = clickpt; /* capture starting point */
                        Show( event, origin );,
                    event == "Moved", /* else */
                        {x0, y0} = origin;
                        {x1, y1} = clickpt; /* draw to new point */
                        drawline( x0, y0, x1, y1 );
                        drawline( x0 + 1, y0, x1 + 1, y1 ); /* make a thick line */
                        drawline( x0 - 1, y0, x1 - 1, y1 );
                        drawline( x0, y0 + 1, x1, y1 + 1 );
                        drawline( x0, y0 - 1, x1, y1 - 1 );
                        origin = clickpt;
                        BITMAP << setpixels( "rgb", {RED, GRN, BLU} ); /* apply changes to bitmap */
                        w << reshow; /* force screen update */
                ,
                    event == "Ticked", /* else ... while the button is pressed but not moving, the tick event will let you do something...here we fade the drawing... */
                        GRN = (49 * GRN + backgrn) / 50;
                        RED = (49 * RED + backred) / 50;
                        BLU = (49 * BLU + backblu) / 50;
                        BITMAP << setpixels( "rgb", {RED, GRN, BLU} );
                        w << reshow;
                );
            )
        )
    )
);
```

### [SetClickEnable](#setclickenable)[](#setclickenable "Click to copy url")

**Syntax:** obj \<\< SetClickEnable( state=0\|1 )

**Description:** Enable the MouseBox to handle button-pressed, mouse-move, button-released operations via the \<\<SetClick function

### [SetCursor](#setcursor)[](#setcursor "Click to copy url")

**Syntax:** obj \<\< SetCursor( "Arrow"\|"NS"\|"EW"\|"NWSE"\|"NESW"\|"Finger"\|"Hand" )

**Description:** \<\<SetCursor("Hand") (or Finger or Arrow or NS EW NWSE NESW) will set the cursor. Use it from a \<\<SetTrack or \<\<SetClick function

``` jsl
New Window( "roll over demo",
    MouseBox(
        Text Box( "hello" ),
        <<setTrackEnable( 1 ),
        <<settrack(
            Function( {this, pos},
                (this << child) << FontColor( If( pos[1] >= 0, "red", "black" ) )
            )
        ),
        <<setDefaultCursor( "Finger" )
    ),
    MouseBox(
        Text Box( "there" ),
        <<setToolTip( "Special!" ),
        <<setTrackEnable( 1 ),
        <<settrack( Function( {this, pos}, this << setCursor( "Hand" ) ) )
    )
);
```

### [SetDefaultCursor](#setdefaultcursor)[](#setdefaultcursor "Click to copy url")

**Syntax:** obj \<\< SetDefaultCursor( "Arrow"\|"NS"\|"EW"\|"NWSE"\|"NESW"\|"Finger"\|"Hand" )

**Description:** specifies the default cursor to display if SetDefaultCursorEnable(1) is also specified; use one of "Arrow", "NS", "EW", "NWSE", "NESW", "Finger", or "Hand". Unlike SetCursor, which is used from a SetTrack script, SetDefaultCursor works without a script.

``` jsl
clickFunction = Function( {this, pos, action},
    If(
        action == "Pressed", oldPos = pos,
        action == "Moved",
            dx = pos[1] - oldPos[1];
            dy = pos[2] - oldPos[2];
            oldPos = pos;
            {tops, lefts, rights, bottoms} = this << getUserData();
            If(
                N Items( tops ) > 0 & 0 < ((border << getTop()) + dy) & (((boxes[tops[1]] <<
                child) << getTop) - dy) > 0,
                border << top( (border << getTop()) + dy );
                For( i = 1, i <= N Items( tops ), i++,
                    (boxes[tops[i]] << child) << top(
                        ((boxes[tops[i]] << child) << getTop) - dy
                    )
                );
            );
            If(
                N Items( bottoms ) > 0 & 0 < ((border << getBottom()) - dy) & (((boxes[
                bottoms[1]] << child) << getBottom) + dy) > 0,
                border << bottom( (border << getBottom()) - dy );
                For( i = 1, i <= N Items( bottoms ), i++,
                    (boxes[bottoms[i]] << child) << bottom(
                        ((boxes[bottoms[i]] << child) << getBottom) + dy
                    )
                );
            );
            If(
                N Items( lefts ) > 0 & 0 < ((border << getLeft()) + dx) & (((boxes[lefts[1]]
                 << child) << getLeft) - dx) > 0,
                border << Left( (border << getLeft()) + dx );
                For( i = 1, i <= N Items( lefts ), i++,
                    (boxes[lefts[i]] << child) << Left(
                        ((boxes[lefts[i]] << child) << getLeft) - dx
                    )
                );
            );
            If(
                N Items( rights ) > 0 & 0 < ((border << getRight()) - dx) & (((boxes[rights[1
                ]] << child) << getRight) + dx) > 0,
                border << Right( (border << getRight()) - dx );
                For( i = 1, i <= N Items( rights ), i++,
                    (boxes[rights[i]] << child) << Right(
                        ((boxes[rights[i]] << child) << getRight) + dx
                    )
                );
            );,
        action == "Released", 0,
        action == "Ticked",
            ((this << child) << child) << settext(
                Char( Num( ((this << child) << child) << gettext() ) + 1 )
            )
    )
);
mb = Function( {boxNumber, cursor, TopLeftRightBottom},
    MouseBox(
        Border Box( sides( 15 ), Left( 5 ), Right( 5 ), top( 5 ), bottom( 5 ),
            Text Box( boxNumber )
        ),
        <<setDefaultCursor( Eval( cursor ) ),
        <<setClickEnable( 1 ),
        <<SetClick( clickFunction ),
        <<SetUserData( TopLeftRightBottom )
    )
);
boxes = {};
bigBorder = 50;
New Window( "corner demo",
    border = Border Box( sides( 15 ), Left( bigBorder ), Right( bigBorder ), top( bigBorder ),
        bottom( bigBorder ),
        Lineup Box( N Col( 3 ), spacing( 10, 10 ),
            boxes[1] = mb( "1000", "NWSE", {{1, 2, 3}, {1, 4, 7}, {}, {}} ),
            boxes[2] = mb( "2000", "NS", {{1, 2, 3}, {}, {}, {}} ),
            boxes[3] = mb( "3000", "NESW", {{1, 2, 3}, {}, {3, 6, 9}, {}} ),
            boxes[4] = mb( "4000", "EW", {{}, {1, 4, 7}, {}, {}} ),
            boxes[5] = mb( "5000", "HAND", {{}, {}, {}, {}} ),
            boxes[6] = mb( "6000", "EW", {{}, {}, {3, 6, 9}, {}} ),
            boxes[7] = mb( "7000", "NESW", {{}, {1, 4, 7}, {}, {7, 8, 9}} ),
            boxes[8] = mb( "8000", "NS", {{}, {}, {}, {7, 8, 9}} ),
            boxes[9] = mb( "9000", "NWSE", {{}, {}, {3, 6, 9}, {7, 8, 9}} )
        )
    )
);
```

### [SetDefaultCursorEnable](#setdefaultcursorenable)[](#setdefaultcursorenable "Click to copy url")

**Syntax:** obj \<\< SetDefaultCursorEnable( state=0\|1 )

**Description:** Enables MouseBox to show the cursor specified by SetDefaultCursor

### [SetDragBegin](#setdragbegin)[](#setdragbegin "Click to copy url")

**Syntax:** obj \<\< SetDragBegin( Function( {this, clickpt}, \<script\> ) )

**Description:** Supplies a function to call at the beginning of a drag-and-drop operation. The function can prevent the drag by returning 0.0 or allow the drag by either returning a string (instead of using \<\<SetDragText) or by returning 1.0 (to use \<\<SetDragText). clickpt is an {x,y} position within the MouseBox where the drag began.

``` jsl
/* See full example for MouseBox() */
mb = MouseBox();
mb << SetDragBegin( Function( {this, clickpt}, 1.0 /*always allow*/ ) );
```

### [SetDragEnable](#setdragenable)[](#setdragenable "Click to copy url")

**Syntax:** obj \<\< SetDragEnable( state=0\|1 )

**Description:** The MouseBox can source a drag-and-drop operation

``` jsl
New Window( "example",
    MouseBox(
        Text Box( "drag me to a text editor" ),
        <<SetDragEnable( 1 ),
        <<SetDragText( "hello" )
    )
);
```

### [SetDragEnd](#setdragend)[](#setdragend "Click to copy url")

**Syntax:** obj \<\< SetDragEnd( Function( {this, clickpt, how}, \<script\> ) )

**Description:** Supplies a function to call at the end of a drag-and-drop operation. how reports how the operation ended, either "move" or "ignore". If the operation ended as a "move" you might use this function to clear the drag source location. clickpt is an {x,y} position within the MouseBox where the drag began.

``` jsl
/* See full example for MouseBox() */
mb = MouseBox();
mb << SetDragEnd(
    Function( {this, clickpt, how},
        If( how == "move",
            (this << child) << delete/* example; probably not what you want */
        )
    )
);
```

### [SetDragText](#setdragtext)[](#setdragtext "Click to copy url")

**Syntax:** obj \<\< SetDragText

**Description:** specify the text the MouseBox will send to the drop point

``` jsl
mb = MouseBox();
mb << setDragText( "1000 words" );
```

### [SetDropCommit](#setdropcommit)[](#setdropcommit "Click to copy url")

**Syntax:** obj \<\< SetDropCommit( Function( {this, clickpt, text}, \<script\> ) )

**Description:** Supplies a function that is called near the end of a drag-and-drop sequence when the button-release event happens. The commit function receives the text supplied by the drag source and can use it as needed, for example, setting the content of a TextBox. clickpt is an {x,y} position within this MouseBox where the drag ended.

``` jsl
/* See full example for <<SetDropTrack() */
mb = MouseBox();
mb << setDropCommit(
    Function( {this, clickPt, text},
        ((this << child) << child) << setText( text );
        1;/* return code is ignored */
    )
);
```

### [SetDropEnable](#setdropenable)[](#setdropenable "Click to copy url")

**Syntax:** obj \<\< SetDropEnable( state=0\|1 )

**Description:** enables the MouseBox to accept drops

``` jsl
mb = MouseBox();
mb << setDropEnable( 1 );
```

### [SetDropTrack](#setdroptrack)[](#setdroptrack "Click to copy url")

**Syntax:** obj \<\< SetDropTrack( Function( {this, clickpt}, \<script\> ) )

**Description:** Supplies a function to call when a drag-and-drop operation drags across the MouseBox. The supplied function returns 0.0 to prevent the drop or 1.0 to allow the drop. The actual drop won't happen until the button-release, at which point the SetDropCommit function is called to do something with the dropped text, but only if setDropTrack returned 1.0. clickpt is an {x,y} position within the MouseBox where another MouseBox is being dragged. It is {-1, -1} when the drag is not on this MouseBox.

``` jsl
nextToBlank = Function( {x, y}, /* helper function */
    If( /* child is border, grandchild is text */
        (x > 1 & (((puzzle[x - 1][y] << child) << child) << gettext) == " ") | (x < 4 & (((
        puzzle[x + 1][y] << child) << child) << gettext) == " ") | (y > 1 & (((puzzle[x][y
        -1] << child) << child) << gettext) == " ") | (y < 4 & (((puzzle[x][y + 1] << child)
         << child) << gettext) == " ")
    ,
        1,
        0
    )
);/* only allow drag begin if next door to empty cell */
dragBegin = Function( {this, clickPt},
    {x, y} = this << getUserData;
    If( nextToBlank( x, y ),
        ((this << child) << child) << getText/* the message is the textbox content */
    , /* else */
        0 /* suppress the drag */
    );
);/* function to remove the character from the source cell, but only if the drop was successful */
dragEnd = Function( {this, clickPt, how}, /* how is copy/move/ignore */
    destbox = this << getDestBox;
    If( Is Empty( destBox ),
        Show( "unknown destination" );
        0 /* don't know where the dest was, force ignore */
        ;
    ,
        Try(
            {x, y} = destbox << GetUserData,
            x = -1;
            y = -1;
        ); /* the destbox might not have a list in userdata */
        If(
            Try(
                puzzle[x][y] != destbox,
                1 /*throw is same as !=*/
            )
        , /* x,y might not be valid index */
            Show( "not dropped in this puzzle" );
            0 /* not this puzzle instance, force ignore */
            ;
        , /* else */
            If( how == "ignore",
                Show( "drop not completed" );
                0 /* the drop was not completed */
                ;
            , /* else */
                ((this << child) << child) << setText( " " )
            )
        );
    );
    0 /* the return code is ignored */
    ;
);/* function to decide if a drop is allowed.  return codes (0,1) are critical. */
dropTrack = Function( {this, clickPt},
    sourcebox = this << getSourceBox;
    If( Is Empty( sourcebox ),
        Show( "unknown source" );
        0 /* no drop from unknown source box */
        ;
    , /* else */
        Try(
            {x, y} = sourcebox << getUserData,
            x = -1;
            y = -1;
        ); /* the sourcebox mightnot have a list in userdata */
        If(
            Try(
                puzzle[x][y] != sourcebox,
                1 /*throw is same as !=*/
            )
        , /* x,y might not be valid index */
            Show( "not from this puzzle" );
            0 /* not sourced from this puzzle instance, ignore */
            ;
        , /* else */
            If( ((this << child) << child) << getText != " ",
                0 /* no drop on occupied cell */
            , /* else */
                1 /* allow drop on the blank cell */
            )
        );
    );
);/* function to implement the drop */
dropCommit = Function( {this, clickPt, text},
    ((this << child) << child) << setText( text );
    1; /* ignored */
);/* cursor changer for cells that can source a drag */
track = Function( {this, clickPt},
    {x, y} = this << getUserData;
    If( nextToBlank( x, y ),
        this << setCursor( "Hand" ),
        this << setCursor( "Arrow" )
    );
    1; /* ignored */
);/* helper function to construct the displaybox tree */
mb = Function( {letter, x, y},
    MouseBox(
        Border Box( Left( 9 ), Right( 9 ), top( 3 ), bottom( 3 ), sides( 15 ),
            Text Box(
                letter,
                <<setFont( "Courier New" ),
                <<set font size( 15 ),
                <<set font style( "bold" )
            )
        ),
        <<setUserData( Eval List( {x, y} ) ), /* remember my location.  I don't move, but my content changes. */
        <<setDragEnable( 1 ),
        <<setDragBegin( dragBegin ), /* dragFunctions defined below */
        <<setDragEnd( dragEnd ),
        <<setDropEnable( 1 ),
        <<setDropTrack( dropTrack ),
        <<setDropCommit( dropCommit ),
        <<setTrackEnable( 1 ),
        <<setTrack( track )
    )
);
puzzle = Eval List(
    {Eval List( {mb( "b", 1, 1 ), mb( "u", 1, 2 ), mb( "y", 1, 3 ), mb( " ", 1, 4 )} ),
    Eval List( {mb( "t", 2, 1 ), mb( "h", 2, 2 ), mb( "i", 2, 3 ), mb( "s", 2, 4 )} ),
    Eval List( {mb( "w", 3, 1 ), mb( "o", 3, 2 ), mb( "r", 3, 3 ), mb( "d", 3, 4 )} ),
    Eval List( {mb( "g", 4, 1 ), mb( "a", 4, 2 ), mb( "m", 4, 3 ), mb( "e", 4, 4 )} )}
);
New Window( "puzzle",
    Border Box( Left( 5 ), Right( 5 ), top( 5 ), bottom( 5 ), sides( 15 ),
        Lineup Box( N Col( 4 ), spacing( 3, 3 ),
            puzzle[1][1],
            puzzle[1][2],
            puzzle[1][3],
            puzzle[1][4],
            puzzle[2][1],
            puzzle[2][2],
            puzzle[2][3],
            puzzle[2][4],
            puzzle[3][1],
            puzzle[3][2],
            puzzle[3][3],
            puzzle[3][4],
            puzzle[4][1],
            puzzle[4][2],
            puzzle[4][3],
            puzzle[4][4]
        )
    )
);
```

### [SetEdit](#setedit)[](#setedit "Click to copy url")

**Syntax:** obj \<\< SetEdit

### [SetEditClear](#seteditclear)[](#seteditclear "Click to copy url")

**Syntax:** obj \<\< SetEditClear( state=0\|1 )

### [SetEditCopy](#seteditcopy)[](#seteditcopy "Click to copy url")

**Syntax:** obj \<\< SetEditCopy( state=0\|1 )

### [SetEditCopyLabel](#seteditcopylabel)[](#seteditcopylabel "Click to copy url")

**Syntax:** obj \<\< SetEditCopyLabel( state=0\|1 )

### [SetEditCopyText](#seteditcopytext)[](#seteditcopytext "Click to copy url")

**Syntax:** obj \<\< SetEditCopyText( state=0\|1 )

### [SetEditCut](#seteditcut)[](#seteditcut "Click to copy url")

**Syntax:** obj \<\< SetEditCut( state=0\|1 )

### [SetEditEnable](#seteditenable)[](#seteditenable "Click to copy url")

**Syntax:** obj \<\< SetEditEnable

### [SetEditJournal](#seteditjournal)[](#seteditjournal "Click to copy url")

**Syntax:** obj \<\< SetEditJournal( state=0\|1 )

### [SetEditPaste](#seteditpaste)[](#seteditpaste "Click to copy url")

**Syntax:** obj \<\< SetEditPaste( state=0\|1 )

### [SetEditPasteJSL](#seteditpastejsl)[](#seteditpastejsl "Click to copy url")

**Syntax:** obj \<\< SetEditPasteJSL( state=0\|1 )

### [SetEditPasteLabel](#seteditpastelabel)[](#seteditpastelabel "Click to copy url")

**Syntax:** obj \<\< SetEditPasteLabel( state=0\|1 )

### [SetEditSaveSelectionAs](#seteditsaveselectionas)[](#seteditsaveselectionas "Click to copy url")

**Syntax:** obj \<\< SetEditSaveSelectionAs( state=0\|1 )

### [SetEditSubmit](#seteditsubmit)[](#seteditsubmit "Click to copy url")

**Syntax:** obj \<\< SetEditSubmit( state=0\|1 )

### [SetEditSubmitDebug](#seteditsubmitdebug)[](#seteditsubmitdebug "Click to copy url")

**Syntax:** obj \<\< SetEditSubmitDebug( state=0\|1 )

### [SetFocus](#setfocus)[](#setfocus "Click to copy url")

**Syntax:** obj \<\< SetFocus

### [SetKey](#setkey)[](#setkey "Click to copy url")

**Syntax:** obj \<\< SetKey( Function( {this, key}, \<script\> ) )

**Description:** Sets the function to be called when a key is pressed while the mouse box has focus. The function should return 1 if the key was handled, or 0 if it was not.

``` jsl
New Window( "SetKey Example", mb = MouseBox( tb = Text Box( "Press a key." ) ) );
mb << setkey(
    Function( {this, key},
        tb << settext( key );
        1;
    )
);
mb << setkeyenable( 1 );
mb << setfocus;
```

### [SetKeyEnable](#setkeyenable)[](#setkeyenable "Click to copy url")

**Syntax:** obj \<\< SetKeyEnable

### [SetMark](#setmark)[](#setmark "Click to copy url")

**Syntax:** obj \<\< SetMark( Function( {this}, \<script\> ) )

**Description:** SetMark specifies a function that will be called when the mouse is clicked or the return key is pressed when the box has focus. Marking can be used to implement a selection state associated with a Mouse Box. To implement clicking actions, use \<\<SetClick.

``` jsl
New Window( "Mouse Box", mb = MouseBox( Text Box( "Text" ) ) );
mb << setMarkEnable( 1 );
mb << getMarkEnable();
mb << setMark( Function( {this}, this << Set Marked( !(this << Get Marked) ) ) );
```

### [SetMarkEnable](#setmarkenable)[](#setmarkenable "Click to copy url")

**Syntax:** obj \<\< SetMarkEnable( state=0\|1 )

**Description:** enables MouseBox to call \<\<SetMark function when the mouse is clicked or the return key is pressed when the box has focus.

``` jsl
New Window( "Mouse Box", mb = MouseBox( Text Box( "Text" ) ) );
mb << setMarkEnable( 1 );
```

### [SetMarked](#setmarked)[](#setmarked "Click to copy url")

**Syntax:** obj \<\< SetMarked( state=0\|1 )

**Description:** Set the marked flag for the Mouse Box. A marked box is shown with a highlighted background.

``` jsl
New Window( "Mouse Box", mb = MouseBox( Text Box( "Text" ) ) );
mb << setMarkEnable( 1 );
mb << setMarked();
```

### [SetToolTip](#settooltip)[](#settooltip "Click to copy url")

**Syntax:** obj \<\< SetToolTip

**Description:** specify the text the MouseBox will use for a tooltip

``` jsl
mb = MouseBox();
mb << setTooltip( "this is your best choice" );
```

### [SetTrack](#settrack)[](#settrack "Click to copy url")

**Syntax:** obj \<\< SetTrack( Function( {this, clickpt}, \<script\> ) )

**Description:** Specifies a function that will be called when the mouse moves over the MouseBox with the button up. For button-down, see \<\<SetClick. clickpt is an {x,y} position within this MouseBox that is the cursor's current position.

``` jsl
/* See full example for <<SetClick() */
mb = MouseBox();
mb << setTrack(
    Function( {this, clickpt},
        this << setCursor( "Hand" ) /* button-up tracking - use the hand */
    )
);
```

### [SetTrackEnable](#settrackenable)[](#settrackenable "Click to copy url")

**Syntax:** obj \<\< SetTrackEnable( state=0\|1 )

**Description:** enables MouseBox to call \<\<SetTrack function when mouse moves with button-up

### [SetUserData](#setuserdata)[](#setuserdata "Click to copy url")

**Syntax:** obj \<\< SetUserData

**Description:** stores a JSL value in the MouseBox; the value could be a number, string, list, associative array, or other JSL type

## [Shared Item Messages](#shared-item-messages)[](#shared-item-messages "Click to copy url")

### [Add Line Annotation](#add-line-annotation)[](#add-line-annotation "Click to copy url")

**Syntax:** obj \<\< Add Line Annotation

**Description:** Adds a line on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Line Annotation( Line( 160, 235, 240, 235 ) );
```

### [Add Pin Annotation](#add-pin-annotation)[](#add-pin-annotation "Click to copy url")

**Syntax:** obj \<\< Add Pin Annotation

**Description:** Adds a pinned annotation on top of a display box. Most attributes (such as Index Row, UniqueID and FoundPt) are designed for internal use only.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Bivariate(
    Y( :weight ),
    X( :height ),
    SendToReport(
        Dispatch( {}, "Bivar Plot", FrameBox,
            Add Pin Annotation(
                Seg( Marker Seg( 1 ) ),
                Index( 17 ),
                Index Row( 17 ),
                UniqueID( -960001792 ),
                FoundPt( {238, 219} ),
                Origin( {64.9765625, 142} ),
                Offset( {-174, -40} ),
                Tag Line( 1 ),
                Font( "Helvetica", 11, "Plain" )
            )
        )
    )
);
```

### [Add Polygon Annotation](#add-polygon-annotation)[](#add-polygon-annotation "Click to copy url")

**Syntax:** obj \<\< Add Polygon Annotation

**Description:** Adds a polygon on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Polygon Annotation(
    Points( {210, 80}, {230, 70}, {280, 115}, {240, 120} ),
    Color( "Red" ),
    Closed( 1 )
);
```

### [Add Simple Shape Annotation](#add-simple-shape-annotation)[](#add-simple-shape-annotation "Click to copy url")

**Syntax:** obj \<\< Add Simple Shape Annotation

**Description:** Adds a simple shape on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Simple Shape Annotation( Oval( 210, 100, 250, 75 ) );
rbiv << Add Simple Shape Annotation( Rectangle( 70, 180, 95, 215 ) );
```

### [Add Text Annotation](#add-text-annotation)[](#add-text-annotation "Click to copy url")

**Syntax:** obj \<\< Add Text Annotation

**Description:** Adds text on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Text Annotation(
    Text( "We need to discuss this at the next meeting." ),
    Text Box( {65, 35, 200, 77} )
);
```

### [Append](#append)[](#append "Click to copy url")

**Syntax:** obj \<\< Append( db2 )

**Description:** Add db2 to the display tree after db.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << append( Text Box( "=== below ===" ) );
```

### [Background Color](#background-color)[](#background-color "Click to copy url")

**Syntax:** obj \<\< Background Color( color ); color = obj \<\< Get Background Color

**Description:** If the background color is set, the box is filled with the background color prior to drawing its content. If the background color is not set, the background and content of the containing boxes show through.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Background Color );
Wait( 2 );
tb << Background Color( "Yellow" );
```

### [Border](#border)[](#border "Click to copy url")

**Syntax:** obj \<\< Border( sides ); sides = obj \<\< Get Border

**Description:** Borders are solid lines drawn around the outside of a display box. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical borders.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Border );
Wait( 1 );
tb << Border( 1 );
```

### [Border Color](#border-color)[](#border-color "Click to copy url")

**Syntax:** obj \<\< Border Color( color ); color = obj \<\< Get Border Color

**Description:** Optional color to override the default color for box borders.

**JMP Version Added:** 19

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Wait( 2 );
tb << Border( 1 );
tb << Border Color( "Light Red" );
```

### [Bring Window To Front](#bring-window-to-front)[](#bring-window-to-front "Click to copy url")

**Syntax:** obj \<\< Bring Window To Front

**Description:** Brings the window to the front.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Run Script( "Bivariate" );
w << Bring Window To Front;
```

### [Child](#child)[](#child "Click to copy url")

**Syntax:** obj \<\< Child

**Description:** Returns the child of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisParent = axisbox << parent();
axisChild = axisParent << child();
Print( axisChild << Class Name() );
```

### [Class Name](#class-name)[](#class-name "Click to copy url")

**Syntax:** obj \<\< Class Name

**Description:** Returns the name of the display class for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisbox << Class Name();
```

### [Clone Box](#clone-box)[](#clone-box "Click to copy url")

**Syntax:** obj \<\< Clone Box

**Description:** Makes a new copy of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << append( Text Box( "=== below ===" ) );
clonedBox = rbiv << Clone Box();
rbiv << append( clonedBox );
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

### [Copy Data](#copy-data)[](#copy-data "Click to copy url")

**Syntax:** obj \<\< Copy Data

**Description:** copies the tab-delimited data from a matrix or table to the clip board.

``` jsl
New Window( "x", mat = Matrix Box( [1 2 3, 4 5 6, 7 8 9] ) );
mat << CopyData;
```

### [Copy Graph](#copy-graph)[](#copy-graph "Click to copy url")

**Syntax:** obj \<\< Copy Graph

**Description:** Puts a picture of the graph and axes on the clipboard.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
(rbiv[FrameBox( 1 )]) << Copy Graph();
"paste into a paint program";
```

### [Copy Picture](#copy-picture)[](#copy-picture "Click to copy url")

**Syntax:** obj \<\< Copy Picture

**Description:** Puts a picture of the display box on the clipboard.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Copy Picture();
```

### [Delete Box](#delete-box)[](#delete-box "Click to copy url")

**Syntax:** obj \<\< Delete Box

**Description:** Delete the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisbox << Delete Box();
```

### [Deselect](#deselect)[](#deselect "Click to copy url")

**Syntax:** obj \<\< Deselect

**Description:** Deselects this object for use by Edit menu commands.

``` jsl
//This message applies to all display box objects
selected = 0;
New Window( "Example",
    ex = Button Box( "Press Me",
        selected = !selected;
        refresh;
    )
);
refresh = Function( {},
    If( selected,
        ex << Select,
        ex << Deselect
    )
);
```

### [Dispatch](#dispatch)[](#dispatch "Click to copy url")

**Syntax:** obj \<\< Dispatch( {outline node, ...}, display element, display element type, command )

**Description:** Send command to a specific part of a display tree.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Dispatch( {}, "Bivar Plot", FrameBox, {Marker Size( 3 )} );
```

### [Enabled](#enabled)[](#enabled "Click to copy url")

**Syntax:** obj \<\< Enabled( state=0\|1 ); state = obj \<\< Get Enabled

**Description:** An object that is not enabled will not respond to keyboard or mouse input. This property is inherited by child objects, so a container object that is disabled will cause all descendent objects to be disabled.

``` jsl
//This message applies to all display objects
New Window( "enabled",
    V List Box(
        check = Check Box(
            {"Use Password"},
            ptext << Enabled( check << Get( 1 ) );
            pvalue << Enabled( check << Get( 1 ) );
        ),
        Lineup Box( N Col( 2 ),
            Text Box( "Username:" ),
            Text Edit Box( "", <<Set Width( 100 ) ),
            ptext = Text Box( "Password:", <<Enabled( 0 ) ),
            pvalue = Text Edit Box( "",
                <<Password Style( 1 ),
                <<Set Width( 20 ),
                <<Enabled( 0 )
            )
        )
    )
);
```

### [Find](#find)[](#find "Click to copy url")

**Syntax:** obj \<\< Find

**Description:** Returns a display box with the given argument.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv << Find( axis box( 1 ) );
axisbox << Delete();
```

### [Get Annotation](#get-annotation)[](#get-annotation "Click to copy url")

**Syntax:** obj \<\< Get Annotation

**Description:** Returns the first annotation that is anchored to this display box. Other annotations can be accessed by using Sib() on the result.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Text Annotation(
    Text( "We need to discuss this at the next meeting." ),
    Text Box( {65, 35, 200, 77} )
);
annotation = rbiv << Get Annotation;
annotation << delete;
```

### [Get Background Color](#get-background-color)[](#get-background-color "Click to copy url")

**Syntax:** obj \<\< Background Color( color ); color = obj \<\< Get Background Color

**Description:** If the background color is set, the box is filled with the background color prior to drawing its content. If the background color is not set, the background and content of the containing boxes show through.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Background Color );
Wait( 2 );
tb << Background Color( "Yellow" );
```

### [Get Border](#get-border)[](#get-border "Click to copy url")

**Syntax:** obj \<\< Border( sides ); sides = obj \<\< Get Border

**Description:** Borders are solid lines drawn around the outside of a display box. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical borders.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Border );
Wait( 1 );
tb << Border( 1 );
```

### [Get Border Color](#get-border-color)[](#get-border-color "Click to copy url")

**Syntax:** obj \<\< Border Color( color ); color = obj \<\< Get Border Color

**Description:** Optional color to override the default color for box borders.

**JMP Version Added:** 19

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Wait( 2 );
tb << Border( 1 );
tb << Border Color( "Light Red" );
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

### [Get Display Path](#get-display-path)[](#get-display-path "Click to copy url")

**Syntax:** obj \<\< Get Display Path( parent box, \<receiver expr\>, \<Mode("XPath"\|"Subscript")\> )

**Description:** Gets a relatively robust expression to navigate between parent box and obj. This path is not guaranteed to be stable across JMP releases. The receiver expr is incorporated into the output expression if provided. If not, the expression provided for parent box is used instead. As shown in the example, this message is mainly useful for increasing the robustness of a path you already have available. The XPath mode is default.

#### [Basic](#basic)[](#basic "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
rpt = Report( biv );
xpath expr = rpt[Number Col Box( 9 )] << Get Display Path( rpt, Expr( Report( biv ) ) ); // Make Number Col Box(9) more robust
Show( xpath expr );
xpath expr << Select;
```

#### [Subscript Mode](#subscript-mode)[](#subscript-mode "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
rpt = Report( biv );
subscript expr = rpt[Number Col Box( 9 )] << Get Display Path( rpt, Mode( "Subscript" ) ); // Make Number Col Box(9) more robust
Show( subscript expr );
subscript expr << Select;
```

### [Get Enabled](#get-enabled)[](#get-enabled "Click to copy url")

**Syntax:** obj \<\< Enabled( state=0\|1 ); state = obj \<\< Get Enabled

**Description:** An object that is not enabled will not respond to keyboard or mouse input. This property is inherited by child objects, so a container object that is disabled will cause all descendent objects to be disabled.

``` jsl
//This message applies to all display objects
New Window( "enabled",
    V List Box(
        check = Check Box(
            {"Use Password"},
            ptext << Enabled( check << Get( 1 ) );
            pvalue << Enabled( check << Get( 1 ) );
        ),
        Lineup Box( N Col( 2 ),
            Text Box( "Username:" ),
            Text Edit Box( "", <<Set Width( 100 ) ),
            ptext = Text Box( "Password:", <<Enabled( 0 ) ),
            pvalue = Text Edit Box( "",
                <<Password Style( 1 ),
                <<Set Width( 20 ),
                <<Enabled( 0 )
            )
        )
    )
);
```

### [Get HTML](#get-html)[](#get-html "Click to copy url")

**Syntax:** obj \<\< Get HTML( \<format\> )

**Description:** Returns a string containing HTML source for the display box.

**Example 1**

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << Set Text( win << Get HTML );
```

**Example 2**

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), Means( 1 ), Mean Diamonds( 1 ) );
Save Text File( "$TEMP/Oneway.html", obj << Get HTML( "svg" ) ); // Prefer <<Save HTML
Web( "$TEMP/Oneway.html", JMPWindow );
```

### [Get Height](#get-height)[](#get-height "Click to copy url")

**Syntax:** width = obj \<\< Get Height

**Description:** Returns the height of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Height;
```

### [Get Horizontal Alignment](#get-horizontal-alignment)[](#get-horizontal-alignment "Click to copy url")

**Syntax:** obj \<\< Horizontal Alignment( "Default"\|"Left"\|"Center"\|"Right" ); "Default"\|"Left"\|"Center"\|"Right" = obj \<\< Get Horizontal Alignment

**Description:** Horizontal alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Border( 1 );
Wait( 2 );
lb << Horizontal Alignment( "Right" );
```

### [Get Journal](#get-journal)[](#get-journal "Click to copy url")

**Syntax:** obj \<\< Get Journal

**Description:** Returns a string containing journal source for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
Print( rbiv << Get Journal );
```

### [Get Margin](#get-margin)[](#get-margin "Click to copy url")

**Syntax:** obj \<\< Margin( sides ); sides = obj \<\< Get Margin

**Description:** Margin adds space between the border of the box and adjacent boxes. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical margins.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Margin );
tb << Border( 1 );
Wait( 2 );
tb << Margin( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Get Max Size](#get-max-size)[](#get-max-size "Click to copy url")

**Syntax:** width,height = obj \<\< Get Max Size

**Description:** Returns the maximum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Max Size;
```

### [Get Min Size](#get-min-size)[](#get-min-size "Click to copy url")

**Syntax:** width,height = obj \<\< Get Min Size

**Description:** Returns the minimum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Min Size;
```

### [Get Namespace](#get-namespace)[](#get-namespace "Click to copy url")

**Syntax:** obj \<\< Get Namespace

**Description:** Returns the namespace associated with this display object.

``` jsl
//This message applies to all display objects
x = 1;
w = New Window( "Test", b = Button Box( "Press me" ) );
b:x = 2;
ns = b << GetNamespace();
Show( ns:x, x );
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

### [Get Padding](#get-padding)[](#get-padding "Click to copy url")

**Syntax:** obj \<\< Padding( sides ); sides = obj \<\< Get Padding

**Description:** Padding adds space between the content and the border of the box. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical padding.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Padding );
tb << Border( 1 );
Wait( 1 );
tb << Padding( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Get Page Setup](#get-page-setup)[](#get-page-setup "Click to copy url")

**Syntax:** obj \<\< Get Page Setup

**Description:** Get page setup information for PDF

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Page Setup Test" ) );
w << get page setup();
```

### [Get Picture](#get-picture)[](#get-picture "Click to copy url")

**Syntax:** obj \<\< Get Picture( \<Scale(factor)\>, \<Type("Bitmap" \| "Scalable")\>, \<View("Picture" \| "Screen" \| "Print"), \<Appearance("Default" \| "Current")\>, \<SubRect(Left(number), Top(number), Right(number), Bottom(number))\> )

**Description:** Captures db as an Image Object. The optional Scale argument will render the image at a scaled resolution. Scaling requires that the display box be stretchable. The Type argument determines whether the result will be a scalable vector image or a bitmap. By default a scalable image is returned, which is suitable for saving to vector formats like PDF. The View option changes the behavior of some boxes. The default option of "Picture" draws the report as it would when exporting to an image format, with scrolled areas fully shown. View mode of "Screen" draws the report as seen on-screen, and "Print" draws the report as it does when printing, without any of the page setup features. The SubRect option will capture a portion of the resulting image rather than a full image. The Appearance option can change from the "Default" output colors to the "Current" colors as seen on-screen. The View, SubRect, and Appearance options are only supported for Type "Bitmap".

#### [Default](#default)[](#default "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
New Window( "Example", rbiv << Get Picture );
```

#### [Scale](#scale)[](#scale "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv[FrameBox( 1 )] << Set Stretch( "Window", "Window" );
New Window( "Example", rbiv << Get Picture( Scale( 1.5 ) ) );
```

#### [View and Appearance](#view-and-appearance)[](#view-and-appearance "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate(
    Y( :weight ),
    X( :height ),
    Fit Line( {Line Color( {212, 73, 88} )} ),
    Fit Polynomial( 3, {Line Color( {61, 174, 70} )} ),
    Kernel Smoother( 1, 1, 0.5, 0 )
);
rbiv = biv << report;
rbiv[FrameBox( 1 )] << Set Stretch( "Window", "Window" );
New Window( "Example",
    H List Box(
        rbiv << Get Picture( View( "Screen" ), Appearance( "Current" ) ),
        rbiv << Get Picture( View( "Print" ), Appearance( "Default" ) )
    )
);
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

### [Get Properties](#get-properties)[](#get-properties "Click to copy url")

**Syntax:** obj \<\< Get Properties

**Description:** Returns an associative array that contains the display box's properties and their values.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Get Properties;
```

### [Get Property](#get-property)[](#get-property "Click to copy url")

**Syntax:** obj \<\< Get Property( "property" )

**Description:** Returns the current setting for the named property.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Get Property( "Enabled" );
```

### [Get Property List](#get-property-list)[](#get-property-list "Click to copy url")

**Syntax:** obj \<\< Get Property List

**Description:** Returns a list of properties the display box has.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Get Property List;
```

### [Get RTF](#get-rtf)[](#get-rtf "Click to copy url")

**Syntax:** obj \<\< Get RTF( \<format\> )

**Description:** Returns a string containing RTF source for the display box.

**Example 1**

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << Set Text( win << Get RTF );
```

**Example 2**

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), Means( 1 ), Mean Diamonds( 1 ) );
Save Text File( "$TEMP/Oneway.rtf", obj << Get RTF( "png" ) ); // Prefer <<Save RTF
Open( "$TEMP/Oneway.rtf" );
```

### [Get Row States](#get-row-states)[](#get-row-states "Click to copy url")

**Syntax:** rs = obj \<\< Get Row States( \<dt\> )

**Description:** Returns a vector containing the row state for every row in the given data table or the current data table. The row states can come from the table, or from the filter context of the box.

#### [Single table](#single-table)[](#single-table "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    Data Filter Context Box(
        H List Box(
            dt << Data Filter(
                Local,
                Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
                Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
            ),
            V List Box(
                t = Text Box( "0 Rows Excluded" ),
                Distribution(
                    Continuous Distribution( Column( :weight ) ),
                    Nominal Distribution( Column( :age ) )
                )
            )
        )
    )
);
updatetext = Function( {},
    rs = t << Get Row States( dt );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = t << Make Row State Handler( dt, rsupdate );
updatetext();
```

#### [Where subset](#where-subset)[](#where-subset "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    t = Text Box( "0 Rows Excluded" ),
    dist = Distribution(
        Continuous Distribution( Column( :weight ) ),
        Nominal Distribution( Column( :age ) ),
        Local Data Filter(
            Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
            Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
        ),
        Where( :sex == "F" )
    )
);
subset = dist << Get Data Table();
updatetext = Function( {},
    rs = Report( dist ) << Get Row States( subset );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = Report( dist ) << Make Row State Handler( subset, rsupdate );
updatetext();
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

### [Get Size](#get-size)[](#get-size "Click to copy url")

**Syntax:** width,height = obj \<\< Get Size

**Description:** Returns the size of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
Print( fb << Get Size );
```

### [Get Stretch](#get-stretch)[](#get-stretch "Click to copy url")

**Syntax:** x,y = obj \<\< Get Stretch

**Description:** Returns the stretching flags for this display box in the horizontal and vertical directions.

**JMP Version Added:** 16

``` jsl
//This message applies to all display box objects
New Window( "Stretch",
    V List Box(
        H List Box( Text Edit Box( "String1" ), Text Edit Box( "String2" ) ),
        spacer = Spacer Box(
            Size( 20, 20 ),
            Color( "Light Red" ),
            <<Set Stretch( "Fill", "Off" )
        )
    )
);
spacer << Get Stretch();
```

### [Get Text](#get-text)[](#get-text "Click to copy url")

**Syntax:** obj \<\< Get Text

**Description:** Returns a string containing the text of the display box.

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << Set Text( win << Get Text );
```

### [Get Text Color](#get-text-color)[](#get-text-color "Click to copy url")

**Syntax:** obj \<\< Text Color( color ); color = obj \<\< Get Text Color

**Description:** Text will be drawn using the text color if it has been set. If the property has not been set, the box will inherit the text color of the containing box.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Text Color );
Wait( 2 );
tb << Text Color( "Red" );
```

### [Get UI Only](#get-ui-only)[](#get-ui-only "Click to copy url")

**Syntax:** obj \<\< UI Only( state=0\|1 ); state = obj \<\< Get UI Only

### [Get Vertical Alignment](#get-vertical-alignment)[](#get-vertical-alignment "Click to copy url")

**Syntax:** obj \<\< Vertical Alignment( "Default"\|"Top"\|"Center"\|"Bottom" ); "Default"\|"Top"\|"Center"\|"Bottom" = obj \<\< Get Vertical Alignment

**Description:** Vertical alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Set Horizontal( 1 );
lb = r[List Box( 7 )];
lb << Border( 1 );
Wait( 2 );
lb << Vertical Alignment( "Bottom" );
```

### [Get Visibility](#get-visibility)[](#get-visibility "Click to copy url")

**Syntax:** obj \<\< Visibility( "Visible"\|"Hidden"\|"Collapse" ); "Visible"\|"Hidden"\|"Collapse" = obj \<\< Get Visibility

**Description:** Visibility determines whether a box is shown and whether it takes up space. The default value of "Visible" means that the object will be shown. A "Hidden" box is not shown but still takes up space, while a "Collapsed" box takes up no space in the layout.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Visibility );
Wait( 1 );
tb << Visibility( "Collapse" );
Show( tb << Get Visibility );
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

### [Get Width](#get-width)[](#get-width "Click to copy url")

**Syntax:** width = obj \<\< Get Width

**Description:** Returns the width of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Width;
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

### [Get XML](#get-xml)[](#get-xml "Click to copy url")

**Syntax:** obj \<\< Get XML( \<English(0\|1)\>, \<NoData(0\|1)\> )

**Description:** Retrieves the display tree formatted as XML. By default, strings are returned in the local language, and the XML includes data values within some boxes. Use the English option to return English strings where available. Use the NoData option to omit the data values within boxes, which can be very large for some display trees.

``` jsl
//This message applies to all display box objects
win = New Window( "test", a = Text Box( "my test" ) );
a << set text( win << get xml );
```

### [GetOffset](#getoffset)[](#getoffset "Click to copy url")

**Syntax:** x,y = obj \<\< GetOffset

**Description:** Returns the offset of this display box relative to the parent box. You might need to use the \<\<parent message in a loop to accumulate several offsets.

``` jsl
New Window( "example",
    MouseBox(
        Graph Box(
            title( "title" ),
            Pen Size( 3 );
            Y Function( -3 + 100 / 2 * (1 + Sin( (2 * Pi() * (x + .3)) / 100 )), x );
        ),
        <<settrackenable( 1 ) // put the mouse box to work, watching "tracking"
    ,
        <<settrack( // events from the mouse (movement, with button up or down)
            Function( {this, pt}, // parameters: this is the mousebox, pt is mouse x,y
                {fb, offset, t, off, size}, // local variables
                // recalulate offset and size each time, the values can change
                fb = this[framebox( 1 )]; // the framebox in the graph 
                offset = [0, 0]; // accumulator to sum up the offset between framebox and mousebox
                t = fb; // a temporary box that starts at the frame 
                While( t != this, // and walks up to the mousebox
                    off = t << getOffset; // ask each box for its offset to the immediate parent
                    offset += Matrix( off ); // convert list answer to matrix so + will work
                    t = t << parent; // crawl up to the mousebox, one box at a time
                );
                size = Matrix( fb << getSize ); // the frame knows its size
                If( // over the frame box
                    offset[1] < pt[1] < offset[1] + size[1] & offset[2] < pt[2] < offset[2]
                     + size[2]
                ,
                    fb << setbackgroundcolor( "red" ),
                    fb << setbackgroundcolor( "blue" )
                );
            )
        )
    )
);
```

### [Horizontal Alignment](#horizontal-alignment)[](#horizontal-alignment "Click to copy url")

**Syntax:** obj \<\< Horizontal Alignment( "Default"\|"Left"\|"Center"\|"Right" ); "Default"\|"Left"\|"Center"\|"Right" = obj \<\< Get Horizontal Alignment

**Description:** Horizontal alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Border( 1 );
Wait( 2 );
lb << Horizontal Alignment( "Right" );
```

### [Inval](#inval)[](#inval "Click to copy url")

**Syntax:** obj \<\< Inval

**Description:** Invalidate the displaybox. The window will update when either the \<\<UpdateWindow message is sent or the operating system has time for the update.

``` jsl
//This message applies to all display box objects
color = "green"; /* initial color in a variable */
New Window( "Inval example",
    Button Box( "red",
        color = "red";
        g1 << inval; /* tell the oval to redraw */
        g2 << inval; /* tell the rectangle to redraw */
        g1 << updateWindow; /* tell the window to update immediately */
        // this is a busy-wait to help demonstrate the various behaviors...
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 /* delay without wait(.5) */ );
    ),
    Button Box( "blue",
        color = "blue";
        g1 << inval; /* same comments */
        g2 << inval;
        g1 << updateWindow;
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 );
    ),
    g1 = Graph Box(/* the graph does NOT watch for the color variable to change 
                      but will use the current value of color when it reshows */
        Fill Color( color );
        Oval( 10, 80, 70, 50, 1 );
    ),
    g2 = Graph Box(
        Fill Color( color );
        Rect( 10, 80, 70, 50, 1 );
    )
);
```

### [Is Dirty](#is-dirty)[](#is-dirty "Click to copy url")

**Syntax:** obj \<\< Is Dirty

**Description:** Gets the document's modified status. 1 means the document has been modified and will prompt for saving; 0 means the document is not modified.

**JMP Version Added:** 14

``` jsl

ww = New Window( "Test", <<Script, "Open(\!"$SAMPLE_DATA\Big Class.jmp\!");" );
Show( ww << Is Dirty );
ww << Set Dirty( 0 );
Show( ww << Is Dirty );
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

### [Journal](#journal)[](#journal "Click to copy url")

**Syntax:** obj \<\< Journal

**Description:** Makes a journal from the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << journal;
```

### [Journal Window](#journal-window)[](#journal-window "Click to copy url")

**Syntax:** obj \<\< Journal Window

**Description:** Opens a journal window of the window.

``` jsl
//This message applies to all display box objects
w = New Window( "Main Window", Text Box( "Main JMP Window" ) );
w << Journal Window;
```

### [Launch](#launch)[](#launch "Click to copy url")

**Syntax:** obj \<\< Launch

**Description:** Evaluates the given argument in the context of the display box.

``` jsl
//This message applies to all display box objects
Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "example",
    ob1 = Outline Box( "treemap launcher" ),
    ob2 = Outline Box( "bivariate partial" ),
    ob3 = Outline Box( "bivariate launched" )
);
ob1 << launch( Treemap() );
ob2 << launch( Bivariate( Y( :height ) ) );
ob3 << launch( Bivariate( Y( :height ), X( :weight ) ) );
```

### [Make RowState Handler](#make-rowstate-handler)[](#make-rowstate-handler "Click to copy url")

**Syntax:** rs = obj \<\< Make RowState Handler( \<dt\>, function(a) )

**Description:** Creates a row state handler for the given data table or the current data table. The function is called when the row states change in the filter context of the box. The argument of the function holds the rows numbers that have changed, or -1 if the row state filter has changed.

#### [Single table](#single-table_1)[](#single-table_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    Data Filter Context Box(
        H List Box(
            dt << Data Filter(
                Local,
                Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
                Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
            ),
            V List Box(
                t = Text Box( "0 Rows Excluded" ),
                Distribution(
                    Continuous Distribution( Column( :weight ) ),
                    Nominal Distribution( Column( :age ) )
                )
            )
        )
    )
);
updatetext = Function( {},
    rs = t << Get Row States( dt );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = t << Make Row State Handler( dt, rsupdate );
updatetext();
```

#### [Where subset](#where-subset_1)[](#where-subset_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    t = Text Box( "0 Rows Excluded" ),
    dist = Distribution(
        Continuous Distribution( Column( :weight ) ),
        Nominal Distribution( Column( :age ) ),
        Local Data Filter(
            Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
            Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
        ),
        Where( :sex == "F" )
    )
);
subset = dist << Get Data Table();
updatetext = Function( {},
    rs = Report( dist ) << Get Row States( subset );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = Report( dist ) << Make Row State Handler( subset, rsupdate );
updatetext();
```

### [Margin](#margin)[](#margin "Click to copy url")

**Syntax:** obj \<\< Margin( sides ); sides = obj \<\< Get Margin

**Description:** Margin adds space between the border of the box and adjacent boxes. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical margins.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Margin );
tb << Border( 1 );
Wait( 2 );
tb << Margin( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
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

### [Next](#next)[](#next "Click to copy url")

**Syntax:** obj \<\< Next

**Description:** Returns the display box after this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
next = rbiv << Next();
Print( next << Class Name() );
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

### [Padding](#padding)[](#padding "Click to copy url")

**Syntax:** obj \<\< Padding( sides ); sides = obj \<\< Get Padding

**Description:** Padding adds space between the content and the border of the box. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical padding.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Padding );
tb << Border( 1 );
Wait( 1 );
tb << Padding( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Page Break](#page-break)[](#page-break "Click to copy url")

**Syntax:** obj \<\< Page Break

**Description:** Inserts a page break before the display box.

``` jsl
//This message applies to all display box objects
New Window( "Example",
    ob = Outline Box( "Outline Box",
        V List Box(
            ob2 = Outline Box( "Outline Box 2",
                H List Box( Text Edit Box( "Top Left" ), Text Edit Box( "Top Right" ) )
            ),
            ob3 = Outline Box( "Outline Box",
                H List Box( Text Edit Box( "Bottom Left" ), Text Edit Box( "Bottom Right" ) )
            )
        )
    )
);
ob3 << Page Break;
```

### [Parent](#parent)[](#parent "Click to copy url")

**Syntax:** obj \<\< Parent

**Description:** Returns the parent of this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisParent = axisbox << parent();
Print( axisParent << Class Name() );
```

### [Prepend](#prepend)[](#prepend "Click to copy url")

**Syntax:** obj \<\< Prepend( db2 )

**Description:** Add db2 to the display tree before db.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << prepend( Text Box( "=== above ===" ) );
```

### [Prev Sib](#prev-sib)[](#prev-sib "Click to copy url")

**Syntax:** obj \<\< Prev Sib

**Description:** Returns the previous sibling of the display box.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 2 )];
axisSibling = axisbox << Prev Sib();
Print( axisSibling << Class Name() );
```

### [Print Window](#print-window)[](#print-window "Click to copy url")

**Syntax:** obj \<\< Print Window

**Description:** Prints the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Print Window;
```

### [Reshow](#reshow)[](#reshow "Click to copy url")

**Syntax:** obj \<\< Reshow

**Description:** Invalidate the displaybox and update the window with the new content. See \<\<Inval and \<\<UpdateWindow messages if more control over timing of the update is required.

``` jsl
//This message applies to all display box objects
color = "green"; /* initial color in a variable */
New Window( "Reshow example",
    Button Box( "red",
        color = "red";
        g << reshow/* tell the graph that something changed */;
    ),
    Button Box( "blue",
        color = "blue";
        g << reshow/* tell the graph that something changed */;
    ),
    g = Graph Box(/* the graph does NOT watch for the color variable to change
                     but will use the current value of color when it reshows */
        Fill Color( color );
        Oval( 10, 80, 70, 50, 1 );
    )
);
```

### [Save Capture](#save-capture)[](#save-capture "Click to copy url")

**Syntax:** obj \<\< Save Capture( \<"path"\>, \<format\>, \<Add Sibling(n)\> )

**Description:** Saves a screen capture of the display box at the specified path. If a path is not given, the Save As window appears.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Capture( "$TEMP/jmp_example.png", "png" );
```

### [Save HTML](#save-html)[](#save-html "Click to copy url")

**Syntax:** obj \<\< Save HTML( \<pathname\>, \<format\> )

**Description:** Saves HTML source and folder of graphics in format specified.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save HTML( "$TEMP/jmp_example.html" );
```

### [Save Interactive HTML](#save-interactive-html)[](#save-interactive-html "Click to copy url")

**Syntax:** obj \<\< Save Interactive HTML( \<pathname\>, \<Boolean\> )

**Description:** Saves Interactive HTML with Data to a file. The Boolean argument represents the report being static.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Interactive HTML( "$TEMP/jmp_example.html" );
```

### [Save Journal](#save-journal)[](#save-journal "Click to copy url")

**Syntax:** obj \<\< Save Journal( \<pathname\> )

**Description:** Saves journal source for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Journal( "$TEMP/jmp_example.jrn" );
```

### [Save MSWord](#save-msword)[](#save-msword "Click to copy url")

**Syntax:** obj \<\< Save MSWord( \<pathname\>, \<format\> )

**Description:** Saves the display box as a Microsoft Word document. (Windows Only)

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save MSWord( "$TEMP/jmp_example.doc" );
```

### [Save PDF](#save-pdf)[](#save-pdf "Click to copy url")

**Syntax:** obj \<\< Save PDF( \<pathname\>, \<Show Page Setup(0\|1)\>, \<Portrait(0\|1)\> )

**Description:** Saves a PDF of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save PDF( "$TEMP/jmp_example.pdf" );
```

### [Save Picture](#save-picture)[](#save-picture "Click to copy url")

**Syntax:** obj \<\< Save Picture( \<pathname\>, \<format\>, \<Scale(factor)\>, \<Type("Bitmap" \| "Scalable")\>, \<View("Picture" \| "Screen" \| "Print"), \<Appearance("Default" \| "Current")\>, \<SubRect(Left(number), Top(number), Right(number), Bottom(number))\> )

**Description:** Saves a picture of the display box. Supported formats are EMF(Windows), PICT(Macintosh), JPEG or JPG, GIF, or PNG. The optional Scale argument will render the image at a scaled resolution. Scaling requires that the display box be stretchable. The Type argument determines whether the result will be a scalable vector image or a bitmap. By default a scalable image is returned, which is suitable for saving to vector formats like PDF. The View option changes the behavior of some boxes. The default option of "Picture" draws the report as it would when exporting to an image format, with scrolled areas fully shown. View mode of "Screen" draws the report as seen on-screen, and "Print" draws the report as it does when printing, without any of the page setup features. The SubRect option will capture a portion of the resulting image rather than a full image. The Appearance option can change from the "Default" output colors to the "Current" colors as seen on-screen. The View, SubRect, and Appearance options are only supported for Type "Bitmap".

#### [Default](#default_1)[](#default_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Picture( "$TEMP/jmp_example.png", "png" );
```

#### [Scale](#scale_1)[](#scale_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv[FrameBox( 1 )] << Set Stretch( "Window", "Window" );
rbiv << Save Picture( "$TEMP/jmp_example_scale.png", "png", Scale( 1.5 ) );
New Window( "scaled image", New Image( "$TEMP/jmp_example_scale.png" ) );
```

#### [View and Appearance](#view-and-appearance_1)[](#view-and-appearance_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate(
    Y( :weight ),
    X( :height ),
    Fit Line( {Line Color( {212, 73, 88} )} ),
    Fit Polynomial( 3, {Line Color( {61, 174, 70} )} ),
    Kernel Smoother( 1, 1, 0.5, 0 )
);
rbiv = biv << report;
rbiv << Save Picture(
    "$TEMP/jmp_example_screen.png",
    "png",
    View( "Screen" ),
    Appearance( "Current" )
);
rbiv << Save Picture(
    "$TEMP/jmp_example_print.png",
    "png",
    View( "Print" ),
    Appearance( "Default" )
);
New Window( "Example",
    H List Box(
        New Image( "$TEMP/jmp_example_screen.png" ),
        New Image( "$TEMP/jmp_example_print.png" )
    )
);
```

### [Save Presentation](#save-presentation)[](#save-presentation "Click to copy url")

**Syntax:** obj \<\< Save Presentation( "filename.pptx", \<Template("path\to\my_template.pptx")\>, \<Insert(Begin\|End\|#) \| Replace(Begin\|End\|#) \| Append\>, \<Outline Titles(None\|Hide\|TopLeft\|TopRight\|BottomLeft\|BottomRight)\>, \<"EMF"\|"PNG"\|"JPG"\|"Native"\> )

**Description:** Saves the display box tables and graphs slides in a presentation. The presentation can be opened with Microsoft PowerPoint or other presentation software.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Presentation( "$TEMP/jmp_example.pptx" );
Open( "$TEMP/jmp_example.pptx" );
```

### [Save RTF](#save-rtf)[](#save-rtf "Click to copy url")

**Syntax:** obj \<\< Save RTF( \<pathname\>, \<format\> )

**Description:** Saves RTF source with graphics in format specified.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save RTF( "$TEMP/jmp_example.rtf", "png" );
```

### [Save Text](#save-text)[](#save-text "Click to copy url")

**Syntax:** obj \<\< Save Text( \<pathname\>, \<format\> )

**Description:** Saves a file containing the text of the display box.

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << save text( "$TEMP/jmp_example.txt" );
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

### [Scroll Window](#scroll-window)[](#scroll-window "Click to copy url")

**Syntax:** obj \<\< Scroll Window( DisplayBox \| \<Relative(\<v\> \| \<h\>,\<v\>)\> \| \<Absolute(\<v\> \| \<h\>,\<v\>) )

**Description:** Adjust the window scrollbar to bring the given DisplayBox into view, or scroll a relative number of pixels, or scroll to an absolute pixel location. In place of a number of pixels the keywords "Start" or "End" can be used.

#### [Absolute](#absolute)[](#absolute "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
fm = Fit Model(
    Y( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    Effects( :Subject, :Dose ),
    Personality( "Manova" ),
    Run
);
fm << setwindowsize( 600, 600 ); // shrink the window
fm << scroll window( Absolute( "End", "End" ) );
Wait( 1 );
fm << scroll window( Absolute( 0, 300 ) );
Wait( 1 );
```

#### [Box](#box)[](#box "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
fm = Fit Model(
    Y( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    Effects( :Subject, :Dose ),
    Personality( "Manova" ),
    Run
);
fm << setwindowsize( 600, 600 ); // shrink the window
For( i = 1, i <= 5, i++, // repeatedly, bring each frame box into view for 1/2 second
    fm << scroll window( Report( fm )[framebox( 2 )] );
    Wait( .5 );
    fm << scroll window( Report( fm )[framebox( 3 )] );
    Wait( .5 );
    fm << scroll window( Report( fm )[framebox( 1 )] );
    Wait( .5 );
);
```

#### [Relative](#relative)[](#relative "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
fm = Fit Model(
    Y( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    Effects( :Subject, :Dose ),
    Personality( "Manova" ),
    Run
);
fm << setwindowsize( 600, 600 ); // shrink the window
fm << scroll window( Relative( 300 ) );
Wait( 1 );
fm << scroll window( Relative( -50 ) );
Wait( 1 );
fm << scroll window( Relative( "Start" ) );
Wait( 1 );
```

### [Select](#select)[](#select "Click to copy url")

**Syntax:** obj \<\< Select

**Description:** Selects this object for use by Edit menu commands.

``` jsl
//This message applies to all display box objects
New Window( "Example", ex = Button Box( "Press Me" ) );
ex << Select;
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

### [Set Dirty](#set-dirty)[](#set-dirty "Click to copy url")

**Syntax:** obj \<\< Set Dirty

**Description:** Sets the document's modified status. 0 will not prompt for saving; 1 will prompt.

**JMP Version Added:** 14

``` jsl

ww = New Window( "Test", <<Script, "Open(\!"$SAMPLE_DATA\Big Class.jmp\!");" );
Show( ww << Is Dirty );
ww << Set Dirty( 0 );
Show( ww << Is Dirty );
```

### [Set Height](#set-height)[](#set-height "Click to copy url")

**Syntax:** obj \<\< Set Height( width )

**Description:** Sets the height of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Height( 150 );
```

### [Set Main Window](#set-main-window)[](#set-main-window "Click to copy url")

**Syntax:** obj \<\< Set Main Window

**Description:** Set the window to be the main window in JMP and sets the prior main window to be a normal window

``` jsl
//This message applies to all display box objects
w = New Window( "Main Window", Text Box( "Main JMP Window" ) );
w << Set Main Window;
```

### [Set Max Size](#set-max-size)[](#set-max-size "Click to copy url")

**Syntax:** obj \<\< Set Max Size( width,height )

**Description:** Sets the maximum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Max Size( 500, 500 );
fb << Get Max Size;
```

### [Set Min Size](#set-min-size)[](#set-min-size "Click to copy url")

**Syntax:** obj \<\< Set Min Size( width,height )

**Description:** Sets the minimum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Min Size( 30, 30 );
fb << Get Min Size;
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

### [Set Property](#set-property)[](#set-property "Click to copy url")

**Syntax:** obj \<\< Set Property( "property", value )

**Description:** Sets the value for the named property for the display box.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Set Property( "Enabled", 0 );
```

### [Set Report Title](#set-report-title)[](#set-report-title "Click to copy url")

**Syntax:** obj \<\< Set Report Title( "string" )

**Description:** Changes the report title.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Set Report Title( "New Title" );
```

### [Set Stretch](#set-stretch)[](#set-stretch "Click to copy url")

**Syntax:** obj \<\< Set Stretch( x,y )

**Description:** Sets the horizontal and vertical stretching behavior of the box. Boxes that stretch with Window will resize as the window or splitter size changes. Boxes that stretch to Fill will stretch to fill available space in their container. Boxes with stretching turned Off generally will not stretch. Most boxes default to Neutral, which means that they will determine their behavior based on their child boxes.

**JMP Version Added:** 16

#### [Stretch to Fill](#stretch-to-fill)[](#stretch-to-fill "Click to copy url")

``` jsl
//This message applies to all display box objects
New Window( "Stretch",
    V List Box(
        H List Box( Text Edit Box( "String1" ), Text Edit Box( "String2" ) ),
        Spacer Box( Size( 20, 20 ), Color( "Light Red" ), <<Set Stretch( "Fill", "Off" ) )
    )
);
```

#### [Stretch with Window](#stretch-with-window)[](#stretch-with-window "Click to copy url")

``` jsl
//This message applies to all display box objects
New Window( "Example",
    H List Box(
        tv = Text Box( "V+V", <<rotate text( left ) ),
        V List Box(
            Text Box( "resize the containing window" ),
            th = Text Box( "H+H" ),
            ts = Spacer Box( <<Size( 10, 30 ), <<Color( "blue" ) )
        )
    )
);
tv << Vertical Alignment( "Center" );
th << Horizontal Alignment( "Center" );
th << Set Stretch( "Window", "Off" );
ts << Set Min Size( 5, 20 );
ts << Set Max Size( 100000, 100 );
ts << Set Stretch( "Window", "Window" );
```

### [Set Summary Behavior](#set-summary-behavior)[](#set-summary-behavior "Click to copy url")

**Syntax:** obj \<\< Set Summary Behavior( "Default"\|"Visible"\|"Collapse" )

**Description:** Sets the behavior of the box when a report is viewed in Summary mode.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
d << Report View( "Summary" );
r = d << Report;
tb = r[Table Box( 1 )];
tb << Set Summary Behavior( "Visible" );
```

### [Set Width](#set-width)[](#set-width "Click to copy url")

**Syntax:** obj \<\< Set Width( width )

**Description:** Sets the width of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Width( 400 );
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

### [Set Window Title](#set-window-title)[](#set-window-title "Click to copy url")

**Syntax:** obj \<\< Set Window Title( "string" )

**Description:** Changes the window title.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Set Window Title( "New Title" );
```

### [Show Properties](#show-properties)[](#show-properties "Click to copy url")

**Syntax:** obj \<\< Show Properties

**Description:** Displays a property editor for display boxes

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Show Properties();
```

### [Show Tree Structure](#show-tree-structure)[](#show-tree-structure "Click to copy url")

**Syntax:** obj \<\< Show Tree Structure

**Description:** Displays a hierarchical tree structure of the display box and its related nodes.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Show Tree Structure();
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

### [Sib](#sib)[](#sib "Click to copy url")

**Syntax:** obj \<\< Sib

**Description:** Returns the sibling of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisSibling = axisbox << sib();
Print( axisSibling << Class Name() );
```

### [Sib Append](#sib-append)[](#sib-append "Click to copy url")

**Syntax:** obj \<\< Sib Append( Display box, Horizontal\|Vertical )

**Description:** Adds a display box immediately after this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r()[framebox( 1 )];
fb << sib append(
    Text Box( "============ after ==============", Rotate Text( "Right" ) ),
    "Horizontal"
);
fb << sib append( Text Box( "=== below ===" ), "Vertical" );
```

### [Sib Prepend](#sib-prepend)[](#sib-prepend "Click to copy url")

**Syntax:** obj \<\< Sib Prepend( Display box, Horizontal\|Vertical )

**Description:** Adds a display box immediately before this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << sib prepend(
    Text Box( "    ============ before ==============", Rotate Text( "Right" ) ),
    "Horizontal"
);
fb << sib prepend( Text Box( "=== above ===" ), "Vertical" );
```

### [Size Window](#size-window)[](#size-window "Click to copy url")

**Syntax:** obj \<\< Size Window( x,y )

**Description:** Sets the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Size Window( 500, 500 );
```

### [Text Color](#text-color)[](#text-color "Click to copy url")

**Syntax:** obj \<\< Text Color( color ); color = obj \<\< Get Text Color

**Description:** Text will be drawn using the text color if it has been set. If the property has not been set, the box will inherit the text color of the containing box.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Text Color );
Wait( 2 );
tb << Text Color( "Red" );
```

### [Top Parent](#top-parent)[](#top-parent "Click to copy url")

**Syntax:** obj \<\< Top Parent

**Description:** Returns the root parent of this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rootParent = rbiv << Top Parent();
Print( rootParent << Class Name() );
```

### [UI Only](#ui-only)[](#ui-only "Click to copy url")

**Syntax:** obj \<\< UI Only( state=0\|1 ); state = obj \<\< Get UI Only

### [Update Window](#update-window)[](#update-window "Click to copy url")

**Syntax:** obj \<\< Update Window

**Description:** Update the window holding the displaybox if there are invalidated regions. The \<\<Inval message creates invalidated regions.

``` jsl
//This message applies to all display box objects
color = "green"; /* initial color in a variable */
New Window( "UpdateWindow example",
    Button Box( "red",
        color = "red";
        // try commenting out each of the 4 lines that follow, run the script,
        // click the buttons, and resize the windows (for example) to force a
        // redraw.  All 4 lines are important, though the last two may be
        // slightly different on Windows and Mac OSs.
        g1 << inval; /* tell the oval to redraw */
        g2 << inval; /* tell the rectangle to redraw */
        g1 << updateWindow; /* tell the oval window to update immediately */
        g2 << updateWindow; /* tell the rect window to update immediately */
        // this is a busy-wait to help demonstrate the various behaviors...
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 /* delay without wait(.5) */ );
    ),
    Button Box( "blue",
        color = "blue";
        g1 << inval; /* same comments */
        g2 << inval;
        g1 << updateWindow;
        g2 << updateWindow;
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 );
    )
);
New Window( "oval",
    g1 = Graph Box(/* the graph does NOT watch for the color variable to change
                      but will use the current value of color when it reshows */
        Fill Color( color );
        Oval( 10, 80, 70, 50, 1 );
    )
);
New Window( "rect",
    g2 = Graph Box(
        Fill Color( color );
        Rect( 10, 80, 70, 50, 1 );
    )
);
```

### [Vertical Alignment](#vertical-alignment)[](#vertical-alignment "Click to copy url")

**Syntax:** obj \<\< Vertical Alignment( "Default"\|"Top"\|"Center"\|"Bottom" ); "Default"\|"Top"\|"Center"\|"Bottom" = obj \<\< Get Vertical Alignment

**Description:** Vertical alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Set Horizontal( 1 );
lb = r[List Box( 7 )];
lb << Border( 1 );
Wait( 2 );
lb << Vertical Alignment( "Bottom" );
```

### [Visibility](#visibility)[](#visibility "Click to copy url")

**Syntax:** obj \<\< Visibility( "Visible"\|"Hidden"\|"Collapse" ); "Visible"\|"Hidden"\|"Collapse" = obj \<\< Get Visibility

**Description:** Visibility determines whether a box is shown and whether it takes up space. The default value of "Visible" means that the object will be shown. A "Hidden" box is not shown but still takes up space, while a "Collapsed" box takes up no space in the layout.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Visibility );
Wait( 1 );
tb << Visibility( "Collapse" );
Show( tb << Get Visibility );
```

### [Window Class Name](#window-class-name)[](#window-class-name "Click to copy url")

**Syntax:** obj \<\< Window Class Name

**Description:** Returns the name of the window class for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
Show( biv << Window Class Name() );
Show( rbiv << Window Class Name() );
```

### [XPath](#xpath)[](#xpath "Click to copy url")

**Syntax:** obj \<\< XPath( XPath expression, \<English(0\|1)\>, \<NoData(0\|1)\> )

**Description:** Applies an XPath expression to the XML representation of the display tree and returns the results. By default, strings are returned in the local language, and the XML includes data values within some boxes. Use the English option to return English strings where available. Use the NoData option to omit the data values within boxes, which is useful for performance when your query is based only on box attributes.

#### [Attributes](#attributes)[](#attributes "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//OutlineBox[@isOpen='false']" )) << Close( 0 );
```

#### [Box type](#box-type)[](#box-type "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//TextEditBox" )) << Text Color( "Green" );
```

#### [Child box](#child-box)[](#child-box "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//OutlineBox[text()='Summary of Fit']/TableBox" )) <<
Make Into Data Table;
```

#### [Data](#data)[](#data "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//NumberColBoxItem[text()='40']/parent::*" )) <<
Text Color( "Green" );
```

#### [Display Seg](#display-seg)[](#display-seg "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//MarkerSeg" )) << Set Marker( "Square" );
```

#### [Text](#text)[](#text "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//OutlineBox[text()='Parameter Estimates']" )) << Close;
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

[ Previous](MosaicSeg.html "MosaicSeg") [Next ](MultiTblNumColBox.html "MultiTblNumColBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
