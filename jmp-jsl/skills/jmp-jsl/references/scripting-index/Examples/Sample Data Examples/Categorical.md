# Categorical

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Categorical.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Categorical.html)*

---

# [Categorical](#categorical)[](#categorical "Click to copy url")

More examples for this topic using the sample data files provided with JMP

## [Indicator Group](#indicator-group)[](#indicator-group "Click to copy url")

### [Perform categorical analysis with indicator group](#perform-categorical-analysis-with-indicator-group)[](#perform-categorical-analysis-with-indicator-group "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Consumer Preferences.jmp");
// Flossing Indicator by Age
Categorical(
    X( :Age Group ),
    Indicator Group(
        :Floss After Waking Up,
        :Floss After Meal,
        :Floss Before Sleep,
        :Floss Another Time
    ),
    Share Of Responses( 0 ),
    Share Chart( 0 ),
    Frequency Chart( 1 ),
    Crosstab Transposed( 1 ),
    Legend( 0 ),
    Test Each Response( 1 )
);
```

[ Previous](Bivariate%20Analysis.html "Bivariate Analysis") [Next ](Clustering.html "Clustering")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
