# Constant Stress ALT Design

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Constant%20Stress%20ALT%20Design.html](https://jsl.jmp.com/All%20Categories/Objects/Constant%20Stress%20ALT%20Design.html)*

---

# [Constant Stress ALT Design](#constant-stress-alt-design)[](#constant-stress-alt-design "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [ALT Plan](#alt-plan)[](#alt-plan "Click to copy url")

**Syntax:** ALT Plan

### [Factors](#factors)[](#factors "Click to copy url")

**Syntax:** Factors

**Description:** Creates the Factor Table in the CSALT platform.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Factor](#factor)[](#factor "Click to copy url")

**Syntax:** obj \<\< Factor

**Description:** Adds a factor with the specified properties.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    )
);
```

### [Factor Name](#factor-name)[](#factor-name "Click to copy url")

**Syntax:** obj \<\< Factor Name

**Description:** Sets the name of the factor.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    )
);
```

### [Factor Transformation](#factor-transformation)[](#factor-transformation "Click to copy url")

**Syntax:** obj \<\< Factor Transformation( Arrhenius Celsius\|Arrhenius Fahrenheit\|Arrhenius Kelvin\|Reciprocal\|Log\|Root\|None )

**Description:** Sets the transformation function for the levels of the factor.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    )
);
```

### [High Test Condition](#high-test-condition)[](#high-test-condition "Click to copy url")

**Syntax:** obj \<\< High Test Condition

**Description:** Sets the highest testing level for the factor.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    )
);
```

### [High Usage Condition](#high-usage-condition)[](#high-usage-condition "Click to copy url")

**Syntax:** obj \<\< High Usage Condition

**Description:** Sets the highest level for the usage condition for the factor. This value can be the same as the lowest usage condition.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    )
);
```

### [Low Test Condition](#low-test-condition)[](#low-test-condition "Click to copy url")

**Syntax:** obj \<\< Low Test Condition

**Description:** Sets the lowest testing level for the factor.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    )
);
```

### [Low Usage Condition](#low-usage-condition)[](#low-usage-condition "Click to copy url")

**Syntax:** obj \<\< Low Usage Condition

**Description:** Sets the lowest level for the usage condition for the factor. This value can be the same as the highest usage condition.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    )
);
```

### [Number of Levels](#number-of-levels)[](#number-of-levels "Click to copy url")

**Syntax:** obj \<\< Number of Levels

**Description:** Sets the number of levels for the factor. Primarily used for balanced designs.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    )
);
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a Script that will reproduce this design.

``` jsl
d = Constant Stress ALT Design(
    Factors(
        Factor(
            Factor Name( "X1" ),
            Number of Levels( 3 ),
            Factor Transformation( "Arrhenius Celsius" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        ),
        Factor(
            Factor Name( "X2" ),
            Number of Levels( 3 ),
            Factor Transformation( "Log" ),
            Low Usage Condition( 20 ),
            High Usage Condition( 30 ),
            Low Test Condition( 90 ),
            High Test Condition( 110 ),

        )
    ),
    ALT Plan(),
    Save Script to Script Window
);
```

[ Previous](Compare%20Data%20Tables.html "Compare Data Tables") [Next ](Contour%20Plot.html "Contour Plot")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
