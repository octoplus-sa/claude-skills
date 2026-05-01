# Regression

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Regression.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Regression.html)*

---

# [Regression](#regression)[](#regression "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Perform a Partial Least Squares (PLS) analysis on the Wine Tasting data using the NIPALS method with 1 factor extracted through KFold validation.](#perform-a-partial-least-squares-pls-analysis-on-the-wine-tasting-data-using-the-nipals-method-with-1-factor-extracted-through-kfold-validation)[](#perform-a-partial-least-squares-pls-analysis-on-the-wine-tasting-data-using-the-nipals-method-with-1-factor-extracted-through-kfold-validation "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Wine Tasting.jmp");
// Partial Least Squares
Partial Least Squares(
    Y(
        :Hedonic, :Goes with meat,
        :Goes with dessert
    ),
    X(
        :Price, :Sugar, :Alcohol,
        :Acidity
    ),
    Validation Method(
        KFold( 5 ),
        Initial Number of Factors( 4 )
    ),
    Fit(
        Method( NIPALS ),
        Number of Factors( 1 )
    )
);
```

[ Previous](Other%20Analysis.html "Other Analysis") [Next ](Statistical%20Analysis.html "Statistical Analysis")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
