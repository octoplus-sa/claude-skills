# Scheduler

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Scheduler.html](https://jsl.jmp.com/All%20Categories/Objects/Scheduler.html)*

---

# [Scheduler](#scheduler)[](#scheduler "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Schedule](#schedule)[](#schedule "Click to copy url")

**Syntax:** Schedule( sec, scpt )

**Description:** Schedules an event that runs the scpt script argument after sec seconds have elapsed. Note: the scheduler only runs during idle times.

``` jsl
s = Schedule(
    10,
    Beep();
    Print( "Hello World!" );
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Clear Schedule](#clear-schedule)[](#clear-schedule "Click to copy url")

**Syntax:** obj \<\< Clear Schedule

**Description:** Clears the scheduler of all events currently scheduled.

``` jsl
s = Schedule(
    10,
    Beep();
    Print( "Hello World!" );
);
s << Clear Schedule;
```

### [Close](#close)[](#close "Click to copy url")

**Syntax:** obj \<\< Close

**Description:** Closes the scheduler.

``` jsl
s = Schedule(
    10,
    Beep();
    Print( "Hello World!" );
);
Wait( 2 );
s << Close;
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

``` jsl
s = Schedule(
    10,
    Beep();
    Print( "Hello World!" );
);
t = s << Get Container;
Show( (t << XPath( "//OutlineBox" )) << Get Title );
```

### [Restart](#restart)[](#restart "Click to copy url")

**Syntax:** obj \<\< Restart

**Description:** Restarts the scheduler after it was stopped from running all events currently scheduled.

``` jsl
s = Schedule(
    10,
    Beep();
    Print( "Hello World!" );
);
s << Stop;
Wait( 2 );
s << Restart;
```

### [Show Schedule](#show-schedule)[](#show-schedule "Click to copy url")

**Syntax:** obj \<\< Show Schedule

**Description:** Shows the next event currently scheduled.

``` jsl
s = Schedule(
    10,
    Beep();
    Print( "Hello World!" );
);
s << Show Schedule;
```

### [Stop](#stop)[](#stop "Click to copy url")

**Syntax:** obj \<\< Stop

**Description:** Stops the scheduler from running all events currently scheduled.

``` jsl
s = Schedule(
    10,
    Beep();
    Print( "Hello World!" );
);
s << Stop;
```

[ Previous](Scatterplot%20Matrix.html "Scatterplot Matrix") [Next ](Score%20Ellipse%20Coverage.html "Score Ellipse Coverage")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
