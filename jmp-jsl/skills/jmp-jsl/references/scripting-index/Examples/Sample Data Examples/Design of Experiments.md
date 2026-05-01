# Design of Experiments

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Design%20of%20Experiments.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Design%20of%20Experiments.html)*

---

# [Design of Experiments](#design-of-experiments)[](#design-of-experiments "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Evaluate the design of a study using the DOE platform with variables X1, X2, and X3.](#evaluate-the-design-of-a-study-using-the-doe-platform-with-variables-x1-x2-and-x3)[](#evaluate-the-design-of-a-study-using-the-doe-platform-with-variables-x1-x2-and-x3 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Functional Data/Simple Linear Functional Data.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X( :X1, :X2, :X3 )
);
```

### [Create a custom experimental design using the DOE platform with a specified set of factors and terms to maximize the response variable Y.](#create-a-custom-experimental-design-using-the-doe-platform-with-a-specified-set-of-factors-and-terms-to-maximize-the-response-variable-y)[](#create-a-custom-experimental-design-using-the-doe-platform-with-a-specified-set-of-factors-and-terms-to-maximize-the-response-variable-y "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Functional Data/Simple Linear Functional Data.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        Maximize, "Y", ., ., .
    ),
    Add Factor(
        Continuous, -1, 1, "X1", 0
    ),
    Add Factor(
        Continuous, -1, 1, "X2", 0
    ),
    Add Factor(
        Continuous, -1, 1, "X3", 0
    ), Set Random Seed( 78379455 ),
    Number of Starts( 1 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Add Term( {1, 1}, {2, 1} ),
    Add Term( {1, 1}, {3, 1} ),
    Add Term( {2, 1}, {3, 1} ),
    Set Sample Size( 24 ),
    Simulate Responses( 0 ),
    Save X Matrix( 0 ), Make Design}
);
```

### [Generate a custom DOE using the Custom Design function to minimize the Odor response with continuous factors temp, gl ratio, and ht, and include specific polynomial terms and interaction terms.](#generate-a-custom-doe-using-the-custom-design-function-to-minimize-the-odor-response-with-continuous-factors-temp-gl-ratio-and-ht-and-include-specific-polynomial-terms-and-interaction-terms)[](#generate-a-custom-doe-using-the-custom-design-function-to-minimize-the-odor-response-with-continuous-factors-temp-gl-ratio-and-ht-and-include-specific-polynomial-terms-and-interaction-terms "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Odor JSS.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        Minimize, "Odor", ., ., .
    ),
    Add Factor(
        Continuous, -1, 1, "temp", 0
    ),
    Add Factor(
        Continuous, -1, 1, "gl ratio", 0
    ),
    Add Factor(
        Continuous, -1, 1, "ht", 0
    ), Set Random Seed( 904322795 ),
    Number of Starts( 21 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Add Term( {1, 2} ),
    Add Term( {1, 1}, {2, 1} ),
    Add Term( {2, 2} ),
    Add Term( {1, 1}, {3, 1} ),
    Add Term( {2, 1}, {3, 1} ),
    Add Term( {3, 2} ),
    Set Sample Size( 16 ),
    Optimality Criterion( 2 ),
    Make Design, Make Table}
);
```

### [Construct a custom experimental design using the DOE platform with specified factors, responses, and aliasing terms.](#construct-a-custom-experimental-design-using-the-doe-platform-with-specified-factors-responses-and-aliasing-terms)[](#construct-a-custom-experimental-design-using-the-doe-platform-with-specified-factors-responses-and-aliasing-terms "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Potato Chip Combined.jmp");
// Basis for Design
DOE(
    Custom Design,
    {
    Add Response(
        Maximize, "Y", ., ., .
    ),
    Add Factor(
        Continuous, -1, 1, "X1", 2
    ),
    Add Factor(
        Continuous, -1, 1, "X2", 1
    ),
    Add Factor(
        Categorical,
        {"L1", "L2", "L3", "L4", "L5",
        "L6", "L7", "L8", "L9", "L10"},
        "X3",
        0
    ), Set Random Seed( 117724710 ),
    Number of Starts( 253 ),
    Add Term( {1, 0} ),
    Add Term( {3, 1} ),
    Add Alias Term( {1, 1}, {2, 1} ),
    Add Alias Term( {1, 1}, {3, 1} ),
    Add Alias Term( {2, 1}, {3, 1} ),
    Set N Whole Plots( 4 ),
    Set N Subplots( 16 ),
    Set Sample Size( 48 ), Make Design,
    Make Table}
);
```

[ Previous](Dataset%20Analysis.html "Dataset Analysis") [Next ](Dimensionality%20Reduction.html "Dimensionality Reduction")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
