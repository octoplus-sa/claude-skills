# Model Fitting

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Model%20Fitting.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Model%20Fitting.html)*

---

# [Model Fitting](#model-fitting)[](#model-fitting "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Develop a standard least squares regression model with mixture effects.](#develop-a-standard-least-squares-regression-model-with-mixture-effects)[](#develop-a-standard-least-squares-regression-model-with-mixture-effects "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Plasticizer.jmp");
// Model
Fit Model(
    Effects(
        :p1 & RS & Mixture,
        :p2 & RS & Mixture,
        :p3 & RS & Mixture, :p1 * :p2,
        :p1 * :p3, :p2 * :p3
    ),
    Y( :Y ),
    No Intercept,
    PERSONALITY(
        "Standard Least Squares"
    )
);
```

[ Previous](Mixed%20Model.html "Mixed Model") [Next ](Multivariate%20Analysis.html "Multivariate Analysis")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
