# Score Ellipse Coverage

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Score%20Ellipse%20Coverage.html](https://jsl.jmp.com/All%20Categories/Objects/Score%20Ellipse%20Coverage.html)*

---

# [Score Ellipse Coverage](#score-ellipse-coverage)[](#score-ellipse-coverage "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Remove Fit](#remove-fit)[](#remove-fit "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**JMP Version Added:** 15

### [Shaded Contour](#shaded-contour)[](#shaded-contour "Click to copy url")

**Syntax:** obj \<\< Shaded Contour( state=0\|1 )

**Description:** Shows or hides the shaded contour.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Flight Delays.jmp" );
obj = dt << Model Driven Multivariate Control Chart(
    Process( :AA, :CO, :DL, :F9, :FL, :NW, :UA, :US, :WN )
);
obj << Score Plot( Score Ellipse Coverage( 0.95, {Shaded Contour( 1 )} ) );
```

[ Previous](Scheduler.html "Scheduler") [Next ](Sequencing%20Variants%20Toolset.html "Sequencing Variants Toolset")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
