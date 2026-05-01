# Visualization

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Visualization.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Visualization.html)*

---

# [Visualization](#visualization)[](#visualization "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Fit a linear model using REML with a random effects structure involving both machine and person variables.](#fit-a-linear-model-using-reml-with-a-random-effects-structure-involving-both-machine-and-person-variables)[](#fit-a-linear-model-using-reml-with-a-random-effects-structure-involving-both-machine-and-person-variables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Machine.jmp");
// Fit Model REML
Fit Model(
    Y( :rating ),
    Effects(
        :machine, :person & Random,
        :machine * :person & Random
    ),
    Personality(
        "Standard Least Squares"
    ),
    Run
);
```

[ Previous](Time%20Series.html "Time Series")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
