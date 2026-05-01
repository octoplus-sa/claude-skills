# Neural

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Neural.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Neural.html)*

---

# [Neural](#neural)[](#neural "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Train a neural network model with ABRASION, MODULUS, ELONG, and HARDNESS as the response variables and SILICA, SILANE, and SULFUR as the predictors. Use Holdback validation with a holdback percentage of 33.33.](#train-a-neural-network-model-with-abrasion-modulus-elong-and-hardness-as-the-response-variables-and-silica-silane-and-sulfur-as-the-predictors-use-holdback-validation-with-a-holdback-percentage-of-3333)[](#train-a-neural-network-model-with-abrasion-modulus-elong-and-hardness-as-the-response-variables-and-silica-silane-and-sulfur-as-the-predictors-use-holdback-validation-with-a-holdback-percentage-of-3333 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Tiretread.jmp");
// Neural
Neural(
    Y(
        :ABRASION, :MODULUS, :ELONG,
        :HARDNESS
    ),
    X( :SILICA, :SILANE, :SULFUR ),
    Informative Missing( 0 ),
    Validation Method(
        "Holdback", 0.3333
    ),
    Go,
    Profiler( 1 )
);
```

[ Previous](Multivariate%20Analysis.html "Multivariate Analysis") [Next ](Other%20Analysis.html "Other Analysis")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
