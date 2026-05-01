# DOE

*Source: [https://jsl.jmp.com/All%20Categories/Objects/DOE.html](https://jsl.jmp.com/All%20Categories/Objects/DOE.html)*

---

# [DOE](#doe)[](#doe "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [DOE](#doe_1)[](#doe_1 "Click to copy url")

**Syntax:** DOE

#### [Augment Design](#augment-design)[](#augment-design "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Design Experiment/Reactor 8 Runs.jmp" );
Wait( 0 );
DOE(
    Augment Design,
    X( :Feed Rate, :Catalyst, :Stir Rate, :Temperature, :Concentration ),
    Y( :Percent Reacted ),
    {Augment Method( Augment ), Set Random Seed( 282322901 ), Number of Starts( 800 ),
    Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ), Add Term( {3, 1} ),
    Add Term( {4, 1} ), Add Term( {5, 1} ), Add Term( {1, 1}, {2, 1} ),
    Add Term( {1, 1}, {3, 1} ), Add Term( {1, 1}, {4, 1} ), Add Term( {1, 1}, {5, 1} ),
    Add Term( {2, 1}, {3, 1} ), Add Term( {2, 1}, {4, 1} ), Add Term( {2, 1}, {5, 1} ),
    Add Term( {3, 1}, {4, 1} ), Add Term( {3, 1}, {5, 1} ), Add Term( {4, 1}, {5, 1} ),
    Set Sample Size( 16 ), Optimality Criterion( "Make D-Optimal Design" ), Make Design,
    Save X Matrix( 0 ), Simulate Responses( 0 )}
);
```

#### [Augment Design, Add Center Points to a Design](#augment-design-add-center-points-to-a-design)[](#augment-design-add-center-points-to-a-design "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Design Experiment/Reactor 8 Runs.jmp" );
Wait( 0 );
DOE(
    Augment Design,
    X( :Feed Rate, :Catalyst, :Stir Rate, :Temperature, :Concentration ),
    Y( :Percent Reacted ),
    {Group new runs into separate block, Augment Method( Centerpoints, 2 ),
    Save X Matrix( 0 ), Simulate Responses( 0 )}
);
```

#### [Augment Design, Replicate a Design](#augment-design-replicate-a-design)[](#augment-design-replicate-a-design "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Design Experiment/Reactor 8 Runs.jmp" );
Wait( 0 );
DOE(
    Augment Design,
    X( :Feed Rate, :Catalyst, :Stir Rate, :Temperature, :Concentration ),
    Y( :Percent Reacted ),
    {Group new runs into separate block, Augment Method( Replicate, 2 ), Save X Matrix( 0 ),
    Simulate Responses( 0 )}
);
```

#### [Choice Design](#choice-design)[](#choice-design "Click to copy url")

``` jsl

DOE(
    Choice Design,
    {Add Factor( Categorical, {"Medium", "Coarse"}, "Grind", 0 ),
    Add Factor( Categorical, {"195", "200", "205"}, "Temperature", 0 ),
    Add Factor( Categorical, {"3", "3.5", "4"}, "Time", 0 ),
    Add Factor( Categorical, {"1.6", "2", "2.4"}, "Charge", 0 ), Set Random Seed( 12345 ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Add Term( {3, 1} ), Add Term( {4, 1} ),
    Set Prior Mean Choice( [0 0 0 0 0 0 0] ),
    Set Prior Variance Matrix(
        [1 0 0 0 0 0 0,
        0 1 0 0 0 0 0,
        0 0 1 0 0 0 0,
        0 0 0 1 0 0 0,
        0 0 0 0 1 0 0,
        0 0 0 0 0 1 0,
        0 0 0 0 0 0 1]
    ), Set Number of Attributes( 4 ), Set Number of Profiles( 2 ),
    Set Number of Choice Sets( 12 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 10 ), Make Design,
    Choice Design Table Output( Separate )}
);
```

#### [Custom Design, Coffee Strength](#custom-design-coffee-strength)[](#custom-design-coffee-strength "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Match Target, "Strength", 1.2, 1.4, . ),
    Add Factor( Categorical, {"Coarse", "Medium"}, "Grind", 0 ),
    Add Factor( Continuous, 195, 205, "Temperature", 0 ),
    Add Factor( Continuous, 3, 4, "Time", 0 ), Add Factor(
        Continuous, 1.6, 2.4, "Charge", 0
    ), Add Factor( Blocking, 4, "Station " ), Set Random Seed( 569534903 ),
    Number of Starts( 100 ), Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ),
    Add Term( {3, 1} ), Add Term( {4, 1} ), Add Term( {5, 1} ),
    Add Alias Term( {1, 1}, {2, 1} ), Add Alias Term( {1, 1}, {3, 1} ),
    Add Alias Term( {1, 1}, {4, 1} ), Add Alias Term( {2, 1}, {3, 1} ),
    Add Alias Term( {2, 1}, {4, 1} ), Add Alias Term( {3, 1}, {4, 1} ), Set Sample Size( 12 ),
    Make Design}
);
```

#### [Custom Design, Design for Fixed Blocks](#custom-design-design-for-fixed-blocks)[](#custom-design-design-for-fixed-blocks "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Maximize, "Y", ., ., . ), Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ), Add Factor( Continuous, -1, 1, "X3", 0 ),
    Add Factor( Blocking, 3, "X4" ), Set Random Seed( 12345 ), Number of Starts( 5 ),
    Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ), Add Term( {3, 1} ),
    Add Term( {4, 1} ), Add Term( {1, 1}, {2, 1} ), Add Term( {1, 1}, {3, 1} ),
    Add Term( {2, 1}, {3, 1} ), Set Sample Size( 18 ), Make Design}
);
```

#### [Custom Design, Design with Fixed Covariates](#custom-design-design-with-fixed-covariates)[](#custom-design-design-with-fixed-covariates "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Design Experiment/Thermoplastic.jmp" );
Wait( 0 );
DOE(
    Custom Design,
    {Add Response( Minimize, "Shrinkage", ., ., . ),
    Add Factor( Covariate, Specific Gravity, 0 ), Add Factor(
        Covariate, Tensile Strength, 0
    ), Add Factor( Covariate, Supplier, 0 ), Add Factor(
        Continuous, -1, 1, "Temperature", 0
    ), Add Factor( Continuous, -1, 1, "Speed", 0 ), Add Factor(
        Continuous, -1, 1, "Time", 0
    ), Set Random Seed( 84951 ), Number of Starts( 40 ), Add Term( {1, 0} ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Add Term( {3, 1} ), Add Term( {4, 1} ),
    Add Term( {5, 1} ), Add Term( {6, 1} ), Add Alias Term( {1, 1}, {2, 1} ),
    Add Alias Term( {1, 1}, {3, 1} ), Add Alias Term( {1, 1}, {4, 1} ),
    Add Alias Term( {1, 1}, {5, 1} ), Add Alias Term( {1, 1}, {6, 1} ),
    Add Alias Term( {2, 1}, {3, 1} ), Add Alias Term( {2, 1}, {4, 1} ),
    Add Alias Term( {2, 1}, {5, 1} ), Add Alias Term( {2, 1}, {6, 1} ),
    Add Alias Term( {3, 1}, {4, 1} ), Add Alias Term( {3, 1}, {5, 1} ),
    Add Alias Term( {3, 1}, {6, 1} ), Add Alias Term( {4, 1}, {5, 1} ),
    Add Alias Term( {4, 1}, {6, 1} ), Add Alias Term( {5, 1}, {6, 1} ), Set Sample Size( 12 ),
    Make Design}
);
```

#### [Custom Design, Design with Hard-to-Change Covariates](#custom-design-design-with-hard-to-change-covariates)[](#custom-design-design-with-hard-to-change-covariates "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Design Experiment/Runners Covariates.jmp" );
Wait( 0 );
DOE(
    Custom Design,
    {Add Response( Minimize, "Wear", ., ., . ), Add Factor( Covariate, Miles, 1 ),
    Add Factor( Covariate, Weight, 1 ), Add Factor( Covariate, Strike Point, 1 ),
    Add Factor( Continuous, 5, 20, "Thickness", 0 ),
    Add Factor( Continuous, 1, 10, "Gel", 0 ), Add Factor(
        Categorical,
        {"L1", "L2", "L3"},
        "Outsole",
        0
    ), Add Factor( Categorical, {"L1", "L2", "L3"}, "Midsole", 0 ), Set Random Seed( 12345 ),
    Number of Starts( 1 ), Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ),
    Add Term( {3, 1} ), Add Term( {4, 1} ), Add Term( {5, 1} ), Add Term( {6, 1} ),
    Add Term( {7, 1} ), Add Term( {1, 1}, {2, 1} ), Add Term( {1, 1}, {3, 1} ),
    Add Term( {1, 1}, {4, 1} ), Add Term( {1, 1}, {5, 1} ), Add Term( {1, 1}, {6, 1} ),
    Add Term( {1, 1}, {7, 1} ), Add Term( {2, 1}, {3, 1} ), Add Term( {2, 1}, {4, 1} ),
    Add Term( {2, 1}, {5, 1} ), Add Term( {2, 1}, {6, 1} ), Add Term( {2, 1}, {7, 1} ),
    Add Term( {3, 1}, {4, 1} ), Add Term( {3, 1}, {5, 1} ), Add Term( {3, 1}, {6, 1} ),
    Add Term( {3, 1}, {7, 1} ), Add Term( {4, 1}, {5, 1} ), Add Term( {4, 1}, {6, 1} ),
    Add Term( {4, 1}, {7, 1} ), Add Term( {5, 1}, {6, 1} ), Add Term( {5, 1}, {7, 1} ),
    Add Term( {6, 1}, {7, 1} ), Set N Whole Plots( 32 ), Set Sample Size( 64 ),
    Simulate Responses( 0 ), Save X Matrix( 0 ), Make Design}
);
```

#### [Custom Design, Mixture Design with Nonmixture Factors](#custom-design-mixture-design-with-nonmixture-factors)[](#custom-design-mixture-design-with-nonmixture-factors "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( None, "Damping", ., ., . ), Add Factor( Mixture, 0.2, 0.8, "CuSO4", 0 ),
    Add Factor( Mixture, 0.2, 0.8, "Na2S2O3", 0 ), Add Factor(
        Mixture, 0, 0.6, "Glyoxal", 0
    ), Add Factor( Categorical, {"L1", "L2", "L3"}, "Wavelength", 0 ),
    Set Random Seed( 12345 ), Number of Starts( 5 ), Add Term( {1, 1} ), Add Term( {2, 1} ),
    Add Term( {3, 1} ), Add Term( {1, 1}, {2, 1} ), Add Term( {1, 1}, {3, 1} ),
    Add Term( {1, 1}, {4, 1} ), Add Term( {2, 1}, {3, 1} ), Add Term( {2, 1}, {4, 1} ),
    Add Term( {3, 1}, {4, 1} ), Set Sample Size( 18 ), Make Design}
);
```

#### [Custom Design, Mixture of Mixtures Design](#custom-design-mixture-of-mixtures-design)[](#custom-design-mixture-of-mixtures-design "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Maximize, "Taste", 0, 10, . ), Add Factor( Mixture, 0.1, 0.2, "Cocoa", 0 ),
    Add Factor( Mixture, 0, 0.15, "Sugar", 0 ), Add Factor( Mixture, 0.2, 0.3, "Flour", 0 ),
    Add Factor( Mixture, 0.1, 0.2, "Butter", 0 ), Add Factor(
        Mixture, 0.25, 0.35, "Milk", 0
    ), Add Factor( Mixture, 0.05, 0.2, "Eggs", 0 ), Set Random Seed( 12345 ),
    Number of Starts( 40 ), Add Constraint( [1 1 1 0 0 0 0.45, -1 -1 -1 0 0 0 -0.45] ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Add Term( {3, 1} ), Add Term( {4, 1} ),
    Add Term( {5, 1} ), Add Alias Term( {1, 1}, {2, 1} ), Add Alias Term( {1, 1}, {3, 1} ),
    Add Alias Term( {1, 1}, {4, 1} ), Add Alias Term( {1, 1}, {5, 1} ),
    Add Alias Term( {1, 1}, {6, 1} ), Add Alias Term( {2, 1}, {3, 1} ),
    Add Alias Term( {2, 1}, {4, 1} ), Add Alias Term( {2, 1}, {5, 1} ),
    Add Alias Term( {2, 1}, {6, 1} ), Add Alias Term( {3, 1}, {4, 1} ),
    Add Alias Term( {3, 1}, {5, 1} ), Add Alias Term( {3, 1}, {6, 1} ),
    Add Alias Term( {4, 1}, {5, 1} ), Add Alias Term( {4, 1}, {6, 1} ),
    Add Alias Term( {5, 1}, {6, 1} ), Set Sample Size( 10 ), Make Design}
);
```

#### [Custom Design, Resolution V Screening Experiment that Resolves all Two-Factor Interactions](#custom-design-resolution-v-screening-experiment-that-resolves-all-two-factor-interactions)[](#custom-design-resolution-v-screening-experiment-that-resolves-all-two-factor-interactions "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Maximize, "Y", ., ., . ), Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ), Add Factor( Continuous, -1, 1, "X3", 0 ),
    Add Factor( Continuous, -1, 1, "X4", 0 ), Add Factor( Continuous, -1, 1, "X5", 0 ),
    Set Random Seed( 12345 ), Number of Starts( 10 ), Add Term( {1, 0} ), Add Term( {1, 1} ),
    Add Term( {2, 1} ), Add Term( {3, 1} ), Add Term( {4, 1} ), Add Term( {5, 1} ),
    Add Term( {1, 1}, {2, 1} ), Add Term( {1, 1}, {3, 1} ), Add Term( {1, 1}, {4, 1} ),
    Add Term( {1, 1}, {5, 1} ), Add Term( {2, 1}, {3, 1} ), Add Term( {2, 1}, {4, 1} ),
    Add Term( {2, 1}, {5, 1} ), Add Term( {3, 1}, {4, 1} ), Add Term( {3, 1}, {5, 1} ),
    Add Term( {4, 1}, {5, 1} ), Set Sample Size( 16 ),
    Optimality Criterion( "Make D-Optimal Design" ), Make Design}
);
```

#### [Custom Design, Response Surface Design](#custom-design-response-surface-design)[](#custom-design-response-surface-design "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Match Target, "Y", 54, 56, . ), Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ), Add Factor( Continuous, -1, 1, "X3", 0 ),
    Set Random Seed( 929281409 ), Number of Starts( 40 ), Add Term( {1, 0} ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Add Term( {3, 1} ), Add Term( {1, 2} ),
    Add Term( {1, 1}, {2, 1} ), Add Term( {2, 2} ), Add Term( {1, 1}, {3, 1} ),
    Add Term( {2, 1}, {3, 1} ), Add Term( {3, 2} ), Set Sample Size( 16 ),
    Optimality Criterion( 2 ), Make Design}
);
```

#### [Custom Design, Response Surface Design with Flexible Blocking](#custom-design-response-surface-design-with-flexible-blocking)[](#custom-design-response-surface-design-with-flexible-blocking "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Maximize, "Y", ., ., . ), Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ), Add Factor( Blocking, 4, "X3" ),
    Set Random Seed( 12345 ), Number of Starts( 5 ), Add Term( {1, 0} ), Add Term( {1, 1} ),
    Add Term( {2, 1} ), Add Term( {3, 1} ), Add Term( {1, 2} ), Add Term( {1, 1}, {2, 1} ),
    Add Term( {2, 2} ), Set Sample Size( 12 ), Optimality Criterion( 2 ), Make Design}
);
```

#### [Custom Design, Screening Experiment that Estimates Main Effects Only](#custom-design-screening-experiment-that-estimates-main-effects-only)[](#custom-design-screening-experiment-that-estimates-main-effects-only "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Maximize, "Y", ., ., . ), Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ), Add Factor( Continuous, -1, 1, "X3", 0 ),
    Add Factor( Continuous, -1, 1, "X4", 0 ), Add Factor( Continuous, -1, 1, "X5", 0 ),
    Add Factor( Continuous, -1, 1, "X6", 0 ), Set Random Seed( 12345 ), Number of Starts( 1 ),
    Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ), Add Term( {3, 1} ),
    Add Term( {4, 1} ), Add Term( {5, 1} ), Add Term( {6, 1} ),
    Add Alias Term( {1, 1}, {2, 1} ), Add Alias Term( {1, 1}, {3, 1} ),
    Add Alias Term( {1, 1}, {4, 1} ), Add Alias Term( {1, 1}, {5, 1} ),
    Add Alias Term( {1, 1}, {6, 1} ), Add Alias Term( {2, 1}, {3, 1} ),
    Add Alias Term( {2, 1}, {4, 1} ), Add Alias Term( {2, 1}, {5, 1} ),
    Add Alias Term( {2, 1}, {6, 1} ), Add Alias Term( {3, 1}, {4, 1} ),
    Add Alias Term( {3, 1}, {5, 1} ), Add Alias Term( {3, 1}, {6, 1} ),
    Add Alias Term( {4, 1}, {5, 1} ), Add Alias Term( {4, 1}, {6, 1} ),
    Add Alias Term( {5, 1}, {6, 1} ), Set Sample Size( 12 ), Make Design}
);
```

#### [Custom Design, Split-Plot Experiment](#custom-design-split-plot-experiment)[](#custom-design-split-plot-experiment "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Maximize, "thickness", 10, ., . ),
    Add Factor( Continuous, -1, 1, "extrusion rate", 1 ),
    Add Factor( Continuous, -1, 1, "temperature", 1 ), Add Factor( Mixture, 0, 1, "m1", 0 ),
    Add Factor( Mixture, 0, 1, "m2", 0 ), Add Factor( Mixture, 0, 1, "m3", 0 ),
    Set Random Seed( 12345 ), Number of Starts( 5 ), Add Term( {3, 1} ), Add Term( {4, 1} ),
    Add Term( {5, 1} ), Add Term( {1, 1}, {2, 1} ), Add Term( {1, 1}, {3, 1} ),
    Add Term( {1, 1}, {4, 1} ), Add Term( {1, 1}, {5, 1} ), Add Term( {2, 1}, {3, 1} ),
    Add Term( {2, 1}, {4, 1} ), Add Term( {2, 1}, {5, 1} ), Add Term( {3, 1}, {4, 1} ),
    Add Term( {3, 1}, {5, 1} ), Add Term( {4, 1}, {5, 1} ), Set N Whole Plots( 7 ),
    Set Sample Size( 28 ), Optimality Criterion( "Make D-Optimal Design" ), Make Design}
);
```

#### [Custom Design, Supersaturated Screening Design](#custom-design-supersaturated-screening-design)[](#custom-design-supersaturated-screening-design "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Maximize, "Y", ., ., . ), Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ), Add Factor( Continuous, -1, 1, "X3", 0 ),
    Add Factor( Continuous, -1, 1, "X4", 0 ), Add Factor( Continuous, -1, 1, "X5", 0 ),
    Add Factor( Continuous, -1, 1, "X6", 0 ), Add Factor( Continuous, -1, 1, "X7", 0 ),
    Add Factor( Continuous, -1, 1, "X8", 0 ), Add Factor( Continuous, -1, 1, "X9", 0 ),
    Add Factor( Continuous, -1, 1, "X10", 0 ), Add Factor( Continuous, -1, 1, "X11", 0 ),
    Add Factor( Continuous, -1, 1, "X12", 0 ), Set Random Seed( 12345 ),
    Number of Starts( 5 ), Add Term( {1, 0} ), Add Potential Term( {1, 1} ),
    Add Potential Term( {2, 1} ), Add Potential Term( {3, 1} ), Add Potential Term( {4, 1} ),
    Add Potential Term( {5, 1} ), Add Potential Term( {6, 1} ), Add Potential Term( {7, 1} ),
    Add Potential Term( {8, 1} ), Add Potential Term( {9, 1} ), Add Potential Term( {10, 1} ),
    Add Potential Term( {11, 1} ), Add Potential Term( {12, 1} ), Set Sample Size( 8 ),
    Simulate Responses( 1 ), Save X Matrix( 0 ), Set Run Order( Randomize ), Make Design}
);
```

#### [Custom Design, Two-Way Split-Plot Experiment](#custom-design-two-way-split-plot-experiment)[](#custom-design-two-way-split-plot-experiment "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Minimize, "OCV", ., ., . ), Add Factor( Continuous, -1, 1, "A1", 2 ),
    Add Factor( Continuous, -1, 1, "A2", 2 ), Add Factor( Continuous, -1, 1, "A3", 2 ),
    Add Factor( Continuous, -1, 1, "A4", 2 ), Add Factor( Continuous, -1, 1, "C1", 1 ),
    Add Factor( Continuous, -1, 1, "C2", 1 ), Set Random Seed( 1866762673 ),
    Number of Starts( 21 ), Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ),
    Add Term( {3, 1} ), Add Term( {4, 1} ), Add Term( {5, 1} ), Add Term( {6, 1} ),
    Add Term( {1, 1}, {2, 1} ), Add Term( {1, 1}, {3, 1} ), Add Term( {1, 1}, {4, 1} ),
    Add Term( {1, 1}, {5, 1} ), Add Term( {1, 1}, {6, 1} ), Add Term( {2, 1}, {3, 1} ),
    Add Term( {2, 1}, {4, 1} ), Add Term( {2, 1}, {5, 1} ), Add Term( {2, 1}, {6, 1} ),
    Add Term( {3, 1}, {4, 1} ), Add Term( {3, 1}, {5, 1} ), Add Term( {3, 1}, {6, 1} ),
    Add Term( {4, 1}, {5, 1} ), Add Term( {4, 1}, {6, 1} ), Add Term( {5, 1}, {6, 1} ),
    Make Strip Plot Design, Set N Whole Plots( 16 ), Set N Subplots( 6 ),
    Set Sample Size( 48 ), Optimality Criterion( "Make D-Optimal Design" ), Make Design}
);
```

#### [Custom Design, Wine Tasting](#custom-design-wine-tasting)[](#custom-design-wine-tasting "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Maximize, "Rating", 0, 20, . ), Add Factor( Blocking, 8, "Rater" ),
    Add Factor( Categorical, {"Bernard", "Dijon"}, "Variety", 0 ),
    Add Factor( Categorical, {"1", "2", "3", "4"}, "Field", 0 ),
    Add Factor( Categorical, {"No", "Yes"}, "De-Stem", 0 ),
    Add Factor( Categorical, {"Cultured", "Wild"}, "Yeast", 0 ),
    Add Factor( Categorical, {"High", "Low"}, "Temperature", 0 ),
    Add Factor( Categorical, {"Hard", "Soft"}, "Press", 0 ),
    Add Factor( Categorical, {"New", "2 Years"}, "Barrel Age", 0 ),
    Add Factor( Categorical, {"Air", "Kiln"}, "Barrel Seasoning", 0 ),
    Add Factor( Categorical, {"No", "Yes"}, "Filtering", 0 ), Set Random Seed( 1234 ),
    Number of Starts( 2 ), Add Term( {1, 0} ), Add Term( {2, 1} ), Add Term( {3, 1} ),
    Add Term( {4, 1} ), Add Term( {5, 1} ), Add Term( {6, 1} ), Add Term( {7, 1} ),
    Add Term( {8, 1} ), Add Term( {9, 1} ), Add Term( {10, 1} ), Add Term( {1, 1} ),
    Add Alias Term( {2, 1}, {3, 1} ), Add Alias Term( {2, 1}, {4, 1} ),
    Add Alias Term( {2, 1}, {5, 1} ), Add Alias Term( {2, 1}, {6, 1} ),
    Add Alias Term( {2, 1}, {7, 1} ), Add Alias Term( {2, 1}, {8, 1} ),
    Add Alias Term( {2, 1}, {9, 1} ), Add Alias Term( {2, 1}, {10, 1} ),
    Add Alias Term( {3, 1}, {4, 1} ), Add Alias Term( {3, 1}, {5, 1} ),
    Add Alias Term( {3, 1}, {6, 1} ), Add Alias Term( {3, 1}, {7, 1} ),
    Add Alias Term( {3, 1}, {8, 1} ), Add Alias Term( {3, 1}, {9, 1} ),
    Add Alias Term( {3, 1}, {10, 1} ), Add Alias Term( {4, 1}, {5, 1} ),
    Add Alias Term( {4, 1}, {6, 1} ), Add Alias Term( {4, 1}, {7, 1} ),
    Add Alias Term( {4, 1}, {8, 1} ), Add Alias Term( {4, 1}, {9, 1} ),
    Add Alias Term( {4, 1}, {10, 1} ), Add Alias Term( {5, 1}, {6, 1} ),
    Add Alias Term( {5, 1}, {7, 1} ), Add Alias Term( {5, 1}, {8, 1} ),
    Add Alias Term( {5, 1}, {9, 1} ), Add Alias Term( {5, 1}, {10, 1} ),
    Add Alias Term( {6, 1}, {7, 1} ), Add Alias Term( {6, 1}, {8, 1} ),
    Add Alias Term( {6, 1}, {9, 1} ), Add Alias Term( {6, 1}, {10, 1} ),
    Add Alias Term( {7, 1}, {8, 1} ), Add Alias Term( {7, 1}, {9, 1} ),
    Add Alias Term( {7, 1}, {10, 1} ), Add Alias Term( {8, 1}, {9, 1} ),
    Add Alias Term( {8, 1}, {10, 1} ), Add Alias Term( {9, 1}, {10, 1} ),
    Set Sample Size( 40 ), Simulate Responses( 0 ), Save X Matrix( 0 ), Make Design}
);
```

#### [Definitive Screening Design](#definitive-screening-design)[](#definitive-screening-design "Click to copy url")

``` jsl

DOE(
    Definitive Screening Design,
    {Add Response( Maximize, "Yield", ., ., . ), Add Factor(
        Continuous, 0, 10, "Methanol", 0
    ), Add Factor( Continuous, 0, 10, "Ethanol", 0 ),
    Add Factor( Continuous, 0, 10, "Propanol", 0 ), Add Factor(
        Continuous, 0, 10, "Butanol", 0
    ), Add Factor( Continuous, 6, 9, "pH", 0 ), Add Factor( Continuous, 1, 2, "Time", 0 ),
    Show Blocking Options( 0, 0 ), Number of Extra Runs( 4 ), Set Random Seed( 880596769 ),
    Make Design, Simulate Responses( 0 ), Save X Matrix( 0 )}
);
```

#### [Definitive Screening Design with Blocks](#definitive-screening-design-with-blocks)[](#definitive-screening-design-with-blocks "Click to copy url")

``` jsl

DOE(
    Definitive Screening Design,
    {Add Response( Maximize, "Yield", ., ., . ), Add Factor( Blocking, 0, "Lot" ),
    Add Factor( Continuous, 0, 10, "Methanol", 0 ), Add Factor(
        Continuous, 0, 10, "Ethanol", 0
    ), Add Factor( Continuous, 0, 10, "Propanol", 0 ),
    Add Factor( Continuous, 0, 10, "Butanol", 0 ), Add Factor( Continuous, 6, 9, "pH", 0 ),
    Add Factor( Continuous, 1, 2, "Time", 0 ), Show Blocking Options( 1, 2 ),
    Number of Extra Runs( 0 ), Set Random Seed( 1146016221 ), Make Design,
    Simulate Responses( 0 ), Save X Matrix( 0 )}
);
```

#### [Full Factorial Design](#full-factorial-design)[](#full-factorial-design "Click to copy url")

``` jsl

DOE(
    Full Factorial Design,
    {Add Response( Maximize, "Percent Reacted", 90, 100, 1 ),
    Add Factor( Continuous, {10, 15}, "Feed Rate", 0 ),
    Add Factor( Continuous, {1, 2}, "Catalyst", 0 ),
    Add Factor( Continuous, {100, 120}, "Stir Rate", 0 ),
    Add Factor( Continuous, {140, 180}, "Temperature", 0 ),
    Add Factor( Continuous, {3, 6}, "Concentration", 0 ), Set Random Seed( 12345 ),
    Make Design}
);
```

#### [Group Orthogonal Supersaturated Design](#group-orthogonal-supersaturated-design)[](#group-orthogonal-supersaturated-design "Click to copy url")

``` jsl

DOE(
    Group Orthogonal Supersaturated Design,
    {GOSSDStructure( 12, 16, 4, 4 ), ChangeFactorSettings( 1, Continuous, -1, 1, "Fake 1" ),
    ChangeFactorSettings( 2, Continuous, -1, 1, "Fake 2" ),
    ChangeFactorSettings( 3, Continuous, -1, 1, "Fake 3" ),
    ChangeFactorSettings( 4, Continuous, -1, 1, "X4" ),
    ChangeFactorSettings( 5, Continuous, -1, 1, "X5" ),
    ChangeFactorSettings( 6, Continuous, -1, 1, "X6" ),
    ChangeFactorSettings( 7, Continuous, -1, 1, "X7" ),
    ChangeFactorSettings( 8, Continuous, -1, 1, "X8" ),
    ChangeFactorSettings( 9, Continuous, -1, 1, "X9" ),
    ChangeFactorSettings( 10, Continuous, -1, 1, "X10" ),
    ChangeFactorSettings( 11, Continuous, -1, 1, "X11" ),
    ChangeFactorSettings( 12, Continuous, -1, 1, "X12" ),
    ChangeFactorSettings( 13, Continuous, -1, 1, "X13" ),
    ChangeFactorSettings( 14, Continuous, -1, 1, "X14" ),
    ChangeFactorSettings( 15, Continuous, -1, 1, "X15" ), Make Design,
    Simulate Responses( 0 )}
);
```

#### [MaxDiff Design](#maxdiff-design)[](#maxdiff-design "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Design Experiment/Candy Profiles.jmp" );
DOE(
    MaxDiff Design,
    X( :Candy ),
    {Set Number of Profiles( 4 ), Set Number of Choice Sets( 7 ), Make Design,
    Simulate Responses( 0 )}
);
```

#### [Mixture Design, Extreme Vertices Design](#mixture-design-extreme-vertices-design)[](#mixture-design-extreme-vertices-design "Click to copy url")

``` jsl

DOE(
    Mixture Design,
    {Add Response( Maximize, "Y", ., ., . ), Change Factor Settings( 1, 0.05, 0.25, "X1" ),
    Change Factor Settings( 2, 0.1, 0.3, "X2" ), Change Factor Settings( 3, 0.1, 0.3, "X3" ),
    Add Factor( Mixture, 0.1, 0.4, "X4", 0 ), Add Factor( Mixture, 0.05, 0.25, "X5", 0 ),
    Set Random Seed( 1409 ), Mixture Design Type( Extreme Vertices, 4 ), Find Subset( 10 ),
    Simulate Responses( 0 )}
);
```

#### [Mixture Design, Optimal Mixture Design](#mixture-design-optimal-mixture-design)[](#mixture-design-optimal-mixture-design "Click to copy url")

``` jsl

DOE(
    Custom Design,
    {Add Response( Maximize, "Y", ., ., . ), Add Factor( Mixture, 0, 1, "X1", 0 ),
    Add Factor( Mixture, 0, 1, "X2", 0 ), Add Factor( Mixture, 0, 1, "X3", 0 ),
    Set Random Seed( 1409 ), Number of Starts( 2 ), Add Constraint( [1 1 0 0.8] ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Add Term( {3, 1} ), Add Term( {1, 1}, {2, 1} ),
    Add Term( {1, 1}, {3, 1} ), Add Term( {2, 1}, {3, 1} ), Center Points( 2 ),
    Set Sample Size( 12 ), Simulate Responses( 0 ), Save X Matrix( 0 ),
    Optimality Criterion( "Make D-Optimal Design" ), Make Design}
);
```

#### [MSA Design](#msa-design)[](#msa-design "Click to copy url")

``` jsl

DOE(
    MSA Design,
    {Add Response( None, "Y", ., ., . ), Add Factor(
        Categorical,
        {"1", "2", "3", "4", "5"},
        "Part",
        MSA( 2, 1 )
    ), Add Factor( Categorical, {"1", "2", "3"}, "Operator", MSA( 1, 1 ) ),
    Add Factor( Categorical, {"Lab A", "Lab B", "Lab C"}, "Lab", MSA( 3, 1 ) ),
    Set Random Seed( 123 ), Replicates( 5, 0 ),
    Nesting Structure( {"Lab", {"Operator" || "Part"}} ), Make Design,
    Simulate Responses( 0 )}
);
```

#### [Response Surface Design, Box-Behnken Design](#response-surface-design-box-behnken-design)[](#response-surface-design-box-behnken-design "Click to copy url")

``` jsl

DOE(
    Response Surface Design,
    {Add Response( Match Target, "Stretch", 350, 550, 1 ),
    Change Factor Settings( 1, 0.7, 1.7, "Silica" ),
    Change Factor Settings( 2, 1.8, 2.8, "Sulfur" ),
    Add Factor( Continuous, 40, 60, "Silane", 0 ), Set Random Seed( 12345 ), Make Design( 1 ),
    Center Points( 3 ), Simulate Responses( 0 ), Save X Matrix( 0 )}
);
```

#### [Screening Design, Fractional Factorial Design](#screening-design-fractional-factorial-design)[](#screening-design-fractional-factorial-design "Click to copy url")

``` jsl

DOE(
    Screening Design,
    {Add Response( Match Target, "Depth", 0.12, 0.22, . ),
    Add Factor( Continuous, 3, 5, "Speed", 0 ), Add Factor(
        Continuous, 150, 165, "Current", 0
    ), Add Factor( Continuous, 20, 30, "Wall Size", 0 ),
    Add Factor( Categorical, {"John", "Mary"}, "Operator", 0 ),
    Add Factor( Categorical, {"Conductance", "Keyhole"}, "Mode", 0 ),
    Add Factor( Categorical, {"Double", "Single"}, "Geometry", 0 ),
    Add Factor( Categorical, {"Aluminum", "Magnesium"}, "Material", 0 ),
    Set Random Seed( 12345 ), Make Design( 1 ), Simulate Responses( 0 ), Save X Matrix( 0 )}
);
```

#### [Screening Design, Main Effects Screening Design](#screening-design-main-effects-screening-design)[](#screening-design-main-effects-screening-design "Click to copy url")

``` jsl

DOE(
    Screening Design,
    {Add Response( Match Target, "Depth", 0.12, 0.22, . ),
    Add Factor( Continuous, 3, 5, "Speed", 0 ), Add Factor(
        Continuous, 150, 165, "Current", 0
    ), Add Factor( Continuous, 20, 30, "Wall Size", 0 ),
    Add Factor( Categorical, {"John", "Mary"}, "Operator", 0 ),
    Add Factor( Categorical, {"Conductance", "Keyhole"}, "Mode", 0 ),
    Add Factor( Categorical, {"Double", "Single"}, "Geometry", 0 ),
    Add Factor( Categorical, {"Aluminum", "Magnesium"}, "Material", 0 ),
    Set Random Seed( 12345 ), Screening Type( 1 ), Number of Starts( 1 ),
    Number of Column Starts( 50 ), Set Sample Size( 12 ), Make Design,
    Simulate Responses( 0 ), Save X Matrix( 0 )}
);
```

#### [Screening Design, Mixed-Level Screening Design](#screening-design-mixed-level-screening-design)[](#screening-design-mixed-level-screening-design "Click to copy url")

``` jsl

DOE(
    Screening Design,
    {Add Response( Maximize, "Y", ., ., . ), Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ), Add Factor( Continuous, -1, 1, "X3", 0 ),
    Add Factor( Continuous, -1, 1, "X4", 0 ), Add Factor( Continuous, -1, 1, "X5", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X6", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X7", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X8", 0 ), Set Random Seed( 12345 ),
    Screening Type( 2, 2, 16 ), Make Design, Simulate Responses( 0 ), Save X Matrix( 0 )}
);
```

#### [Space Filling Design, Constrained Fast Flexible Filling](#space-filling-design-constrained-fast-flexible-filling)[](#space-filling-design-constrained-fast-flexible-filling "Click to copy url")

``` jsl

DOE(
    Space Filling Design,
    {Add Response( Maximize, "Y", ., ., . ), Add Factor( Continuous, 0, 1, "X1", 0 ),
    Add Factor( Continuous, 0, 1, "X2", 0 ), Set Random Seed( 765 ),
    Add Constraint( [1 1 0.8] ), FFF Optimality Criterion( MaxPro ),
    Space Filling Design Type( Fast Flexible Filling, 200 ), Simulate Responses( 0 )}
);
```

#### [Space Filling Design, Sphere Packing](#space-filling-design-sphere-packing)[](#space-filling-design-sphere-packing "Click to copy url")

``` jsl

DOE(
    Space Filling Design,
    {Add Response( Maximize, "Y", ., ., . ), Add Factor( Continuous, 0, 1, "X1", 0 ),
    Add Factor( Continuous, 0, 1, "X2", 0 ), Set Random Seed( 765 ),
    Space Filling Design Type( Sphere Packing, 8 ), Simulate Responses( 0 )}
);
```

## [Columns](#columns)[](#columns "Click to copy url")

### [Factor](#factor)[](#factor "Click to copy url")

**Syntax:** obj \<\< Factor( column(s) )

``` jsl

DOE(
    Custom Design,
    {Add Response( Match Target, "Strength", 1.2, 1.4, . ),
    Add Factor( Categorical, {"Coarse", "Medium"}, "Grind", 0 ),
    Add Factor( Continuous, 195, 205, "Temperature", 0 ),
    Add Factor( Continuous, 3, 4, "Time", 0 ), Add Factor( Continuous, 1.6, 2.4, "Charge", 0 ),
    Add Factor( Blocking, 4, "Station " ), Set Random Seed( 569534903 ), Number of Starts( 100 ),
    Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ), Add Term( {3, 1} ),
    Add Term( {4, 1} ), Add Term( {5, 1} ), Add Alias Term( {1, 1}, {2, 1} ),
    Add Alias Term( {1, 1}, {3, 1} ), Add Alias Term( {1, 1}, {4, 1} ),
    Add Alias Term( {2, 1}, {3, 1} ), Add Alias Term( {2, 1}, {4, 1} ),
    Add Alias Term( {3, 1}, {4, 1} ), Set Sample Size( 12 ), Make Design}
);
```

### [Response](#response)[](#response "Click to copy url")

**Syntax:** obj \<\< Response( column(s) )

``` jsl

DOE(
    Custom Design,
    {Add Response( Match Target, "Strength", 1.2, 1.4, . ),
    Add Factor( Categorical, {"Coarse", "Medium"}, "Grind", 0 ),
    Add Factor( Continuous, 195, 205, "Temperature", 0 ),
    Add Factor( Continuous, 3, 4, "Time", 0 ), Add Factor(
        Continuous, 1.6, 2.4, "Charge", 0
    ), Add Factor( Blocking, 4, "Station " ), Set Random Seed( 569534903 ),
    Number of Starts( 100 ), Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ),
    Add Term( {3, 1} ), Add Term( {4, 1} ), Add Term( {5, 1} ),
    Add Alias Term( {1, 1}, {2, 1} ), Add Alias Term( {1, 1}, {3, 1} ),
    Add Alias Term( {1, 1}, {4, 1} ), Add Alias Term( {2, 1}, {3, 1} ),
    Add Alias Term( {2, 1}, {4, 1} ), Add Alias Term( {3, 1}, {4, 1} ), Set Sample Size( 12 ),
    Make Design}
);
```

### [X](#x)[](#x "Click to copy url")

**Syntax:** obj \<\< X( column(s) )

``` jsl

DOE(
    Custom Design,
    {Add Response( Match Target, "Strength", 1.2, 1.4, . ),
    Add Factor( Categorical, {"Coarse", "Medium"}, "Grind", 0 ),
    Add Factor( Continuous, 195, 205, "Temperature", 0 ),
    Add Factor( Continuous, 3, 4, "Time", 0 ), Add Factor(
        Continuous, 1.6, 2.4, "Charge", 0
    ), Add Factor( Blocking, 4, "Station " ), Set Random Seed( 569534903 ),
    Number of Starts( 100 ), Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ),
    Add Term( {3, 1} ), Add Term( {4, 1} ), Add Term( {5, 1} ),
    Add Alias Term( {1, 1}, {2, 1} ), Add Alias Term( {1, 1}, {3, 1} ),
    Add Alias Term( {1, 1}, {4, 1} ), Add Alias Term( {2, 1}, {3, 1} ),
    Add Alias Term( {2, 1}, {4, 1} ), Add Alias Term( {3, 1}, {4, 1} ), Set Sample Size( 12 ),
    Make Design}
);
```

### [Y](#y)[](#y "Click to copy url")

**Syntax:** obj \<\< Y( column(s) )

``` jsl

DOE(
    Custom Design,
    {Add Response( Match Target, "Strength", 1.2, 1.4, . ),
    Add Factor( Categorical, {"Coarse", "Medium"}, "Grind", 0 ),
    Add Factor( Continuous, 195, 205, "Temperature", 0 ),
    Add Factor( Continuous, 3, 4, "Time", 0 ), Add Factor(
        Continuous, 1.6, 2.4, "Charge", 0
    ), Add Factor( Blocking, 4, "Station " ), Set Random Seed( 569534903 ),
    Number of Starts( 100 ), Add Term( {1, 0} ), Add Term( {1, 1} ), Add Term( {2, 1} ),
    Add Term( {3, 1} ), Add Term( {4, 1} ), Add Term( {5, 1} ),
    Add Alias Term( {1, 1}, {2, 1} ), Add Alias Term( {1, 1}, {3, 1} ),
    Add Alias Term( {1, 1}, {4, 1} ), Add Alias Term( {2, 1}, {3, 1} ),
    Add Alias Term( {2, 1}, {4, 1} ), Add Alias Term( {3, 1}, {4, 1} ), Set Sample Size( 12 ),
    Make Design}
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [A-Optimality Parameter Weights](#a-optimality-parameter-weights)[](#a-optimality-parameter-weights "Click to copy url")

**Syntax:** obj \<\< A-Optimality Parameter Weights

**Description:** Sets the weights to be used for creating an A-optimal design.

**JMP Version Added:** 14

``` jsl
DOE(
    Custom Design,
    {Add Factor( Continuous, -1, 1, "X1", 0 ), Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ), Add Term( {1, 0} ), Add Term( {1, 1} ),
    Add Term( {2, 1} ), Add Term( {3, 1} ), Add Term( {1, 1}, {2, 1} ),
    Add Term( {1, 1}, {3, 1} ), Add Term( {2, 1}, {3, 1} ), Set Sample Size( 14 ),
    Optimality Criterion( "Make A-Optimal Design"n ),
    "A-Optimality Parameter Weights"n( [1 1 1 1 0.1 0.1 0.1] )}
);
```

### [ALT Factor Settings](#alt-factor-settings)[](#alt-factor-settings "Click to copy url")

**Syntax:** obj \<\< ALT Factor Settings

**Description:** For the given factor number in an accelerated life test plan, allows specification of factor name, number of levels, factor transformation, usage conditions and test conditions.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [ALT Plan Setup](#alt-plan-setup)[](#alt-plan-setup "Click to copy url")

**Syntax:** obj \<\< ALT Plan Setup( 1\|2\|3 )

**Description:** Specifies the initial choice of model for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Add Alias Term](#add-alias-term)[](#add-alias-term "Click to copy url")

**Syntax:** obj \<\< Add Alias Term

**Description:** Adds an alias term to the list of alias terms. Specify the factor number and power for each effect in a list. Create interactions by separating effects with commas.

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 )
);
d << Add Alias Term( {1, 1}, {2, 1} );
d << Add Alias Term( {1, 2} );
```

### [Add Constraint](#add-constraint)[](#add-constraint "Click to copy url")

**Syntax:** obj \<\< Add Constraint

**Description:** Adds linear constraints through a matrix. Each row represents a constraint. The last column is for values on the right side of the inequality constraints. In JSL, the inequality constraints must be less than or equal to the values on the right.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Add Constraint( [1 1 0 1, 1 0 1 1] ),
    Add Term( {1, 0} )
);
```

### [Add Factor](#add-factor)[](#add-factor "Click to copy url")

**Syntax:** obj \<\< Add Factor( Continuous\|Discrete Numeric\|Blocking\|Constant\|Categorical\|Mixture )

**Description:** Adds a factor of the specified type and optional arguments. If nothing is specified, this command adds a continuous factor.

``` jsl
d = DOE( Custom Design );
d << Add Factor( Continuous, -1, 1, "X1", 0 );
d << Add Factor( Discrete Numeric, {1, 2, 3}, "X2", 0 );
d << Add Factor( Categorical, {"L1", "L2"}, "X3", 0 );
d << Add Factor( Blocking, 8, "X4" );
d << Add Factor( Constant, 3, "X5" );
```

### [Add Functional Response](#add-functional-response)[](#add-functional-response "Click to copy url")

**Syntax:** obj \<\< Add Functional Response

**Description:** Adds a functional response with the specified name, number of measurements per run, and values.

**JMP Version Added:** 15

``` jsl
DOE(
    Custom Design,
    Add Response( Maximize, "Y", ., ., . ),
    Add Functional Response( "Y", 5, {1, 2, 3, 4, 5} ),
    Set Random Seed( 46055034 ),
    Simulate Responses( 0 ),
    Save X Matrix( 0 )
);
```

### [Add Potential Term](#add-potential-term)[](#add-potential-term "Click to copy url")

**Syntax:** obj \<\< Add Potential Term

**Description:** Adds an If Possible term to the list of model terms. Specify the factor number and power for each effect in a list. Create interactions by separating effects with commas.

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 )
);
d << Add Potential Term( {1, 1}, {2, 1} );
d << Add Potential Term( {1, 2} );
```

### [Add Response](#add-response)[](#add-response "Click to copy url")

**Syntax:** obj \<\< Add Response( goal, name, lower limit, upper limit, importance, lower detection limit, upper detection limit )

**Description:** Adds a response with the specified goal, name, lower limit, upper limit, and importance.

**Example 1**

``` jsl
DOE( Custom Design, Add Response( Match Target, "Y", 10, 30, 1 ) );
```

**Example 2**

``` jsl
DOE( Custom Design, Add Response( Match Target, "Y", ., ., 1, 10, 30 ) );
```

### [Add Term](#add-term)[](#add-term "Click to copy url")

**Syntax:** obj \<\< Add Term

**Description:** Adds a "Necessary" term to list of the model terms. Effects are specified by {factor number, power}. Interactions can be created by separating effects by commas.

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 )
);
d << Add Term( {1, 1}, {2, 1} );
d << Add Term( {1, 2} );
```

### [Additional Designs](#additional-designs)[](#additional-designs "Click to copy url")

**Syntax:** obj \<\< Additional Designs

**Description:** Specify up to nine additional designs to be compared to the reference design.

**JMP Version Added:** 14

``` jsl
DOE(
    Custom Design,
    Add Factor,
    Add Factor,
    Add Factor,
    Set Sample Size( 12 ),
    Make Design,
    Make Table
);
DOE( Custom Design, Add Factor, Add Factor, Add Factor, Make Design, Make Table );
DOE(
    Custom Design,
    Add Factor,
    Add Factor,
    Add Factor,
    Set Sample Size( 4 ),
    Make Design,
    Make Table
);
DOE(
    Compare Designs,
    Reference Design( "Custom Design", X( :X1, :X2, :X3 ) ),
    Additional Designs(
        "Custom Design 2",
        X( :X1, :X2, :X3 ),
        "Custom Design 3",
        X( :X1, :X2, :X3 )
    )
);
```

### [Allow covariate rows to be repeated](#allow-covariate-rows-to-be-repeated)[](#allow-covariate-rows-to-be-repeated "Click to copy url")

**Syntax:** obj \<\< Allow covariate rows to be repeated( state=0\|1 )

**Description:** Specifies if covariate rows are allowed to be repeated in the design.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
DOE(
    Custom Design,
    Add Response( Maximize, "Y", ., ., . ),
    Add Factor( Covariate, :sex, 0 ),
    Add Factor( Covariate, :height, 0 ),
    Add Factor( Covariate, :weight, 0 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Enforce Use of Selected Covariate Rows( 1 ),
    Allow covariate rows to be repeated( 1 ),
    Select Covariate Rows( [1 2 3 4] ),
    Set Sample Size( 24 )
);
```

### [Augment Method](#augment-method)[](#augment-method "Click to copy url")

**Syntax:** obj \<\< Augment Method( Replicate\|Centerpoints\|Fold Over\|Add Axial\|Augment )

**Description:** Specifies the type of augment method and its parameters.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Augment Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Augment Method( Augment );
d << Set Sample Size( 24 );
d << Make Design;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/2x3x4 Factorial.jmp" );
d = DOE( Augment Design, X( :X1, :X2, :X3 ), Y( :Y ) );
d << Augment Method( Replicate, 2 );
```

**Example 3**

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Augment Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Augment Method( Centerpoints, 3 );
```

**Example 4**

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Augment Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Augment Method( Fold Over, [1 2] );
```

**Example 5**

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Augment Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Augment Method( Add Axial, 1, 2 );
```

### [Blocks](#blocks)[](#blocks "Click to copy url")

**Syntax:** obj \<\< Blocks

**Description:** Specifies the block size for a balanced incomplete block design (BIBD).

**JMP Version Added:** 14

``` jsl
d = DOE( Balanced Incomplete Block Design, Treatments( 3, {"L1", "L2", "L3"} ) );
d << Blocks( 2 );
d << Make Design;
```

### [Center Points](#center-points)[](#center-points "Click to copy url")

**Syntax:** obj \<\< Center Points

**Description:** Specifies the number of center points.

**Example 1**

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 )
);
d << Make Model( Linear );
d << Center Points( 2 );
```

**Example 2**

``` jsl
DOE(
    Definitive Screening Design,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Show Blocking Options( 1, 2 ),
    Number of Extra Runs( 4 ),
    Center Points( 1 )
);
```

### [Change Anticipated Coefficients](#change-anticipated-coefficients)[](#change-anticipated-coefficients "Click to copy url")

**Syntax:** obj \<\< Change Anticipated Coefficients

**Description:** Change the Anticipated Coefficients in Power Analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Change Anticipated Coefficients( [1 2 3 4 2 2 2 3 3 3] );
```

### [Change Factor Settings](#change-factor-settings)[](#change-factor-settings "Click to copy url")

**Syntax:** obj \<\< Change Factor Settings

**Description:** Specifies the minimum, maximum, and name of the continuous or mixture factor that you included in the first argument. Most useful for platforms that initially have predefined factors.

**Example 1**

``` jsl
d = DOE( Response Surface Design );
d << Change Factor Settings( 1, 2, 3, "A" );
d << Change Factor Settings( 2, 0, 4 );
```

**Example 2**

``` jsl
d = DOE( Mixture Design );
d << Change Factor Settings( 1, 0.1, 0.4, "A" );
d << Change Factor Settings( 3, 0, 0.8, "C" );
```

### [Check Inscribe](#check-inscribe)[](#check-inscribe "Click to copy url")

**Syntax:** obj \<\< Check Inscribe

**Description:** Rescales the design so that axial points are at the low and high ends of the range.

``` jsl
d = DOE( Response Surface Design, Make Design( 2 ) );
d << Set Axial Choice( 2 );
d << Check Inscribe;
```

### [Choice Design Table Output](#choice-design-table-output)[](#choice-design-table-output "Click to copy url")

**Syntax:** obj \<\< Choice Design Table Output( "Separate"\|"Combined" )

**Description:** Specifies how to create a data table for a choice design.

``` jsl
DOE(
    Choice Design,
    {Add Factor( Categorical, {"L1", "L2"}, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ), Add Term( {1, 1} ), Add Term( {2, 1} ),
    Set Prior Mean Choice( [0 0] ), Set Prior Variance Matrix( [1 0, 0 1] ),
    Set Number of Attributes( 2 ), Set Number of Profiles( 2 ),
    Set Number of Choice Sets( 8 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 1 ), Make Design,
    Choice Design Table Output( Combined )}
);
```

### [D Efficiency Weight](#d-efficiency-weight)[](#d-efficiency-weight "Click to copy url")

**Syntax:** obj \<\< D Efficiency Weight

**Description:** Use this option to control the relative importance of D-efficiency and reduction of aliasing. Supply a number between zero and one.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    D Efficiency Weight( 0.5 ),
    Make Design
);
```

### [Design Search Time](#design-search-time)[](#design-search-time "Click to copy url")

**Syntax:** obj \<\< Design Search Time( number )

**Description:** Specifies the number of seconds to search for a design.

``` jsl
DOE(
    Custom Design,
    {Add Factor( Continuous, -1, 1, "X1", 0 ), Add Factor( Continuous, -1, 1, "X2", 0 ),
    Set Sample Size( 7 ), Design Search Time( 8 ), Make Design}
);
```

### [Disallowed Combinations](#disallowed-combinations)[](#disallowed-combinations "Click to copy url")

**Syntax:** obj \<\< Disallowed Combinations

**Description:** Enables you to supply a script that returns true for any factor combinations that should be excluded from your design.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ),
    Number of Starts( 100 ),
    Disallowed Combinations( X1 > 0.5 & X2 == 2 ),
    Make Design
);
```

### [Discrete Numeric Powers Set to Necessary](#discrete-numeric-powers-set-to-necessary)[](#discrete-numeric-powers-set-to-necessary "Click to copy url")

**Syntax:** obj \<\< Discrete Numeric Powers Set to Necessary( state=0\|1 )

**Description:** Specifies if powers in discrete numeric factors should be necessary model terms.

``` jsl
DOE(
    Custom Design,
    Add Factor( Discrete Numeric, {1, 2, 3}, "X1", 0 ),
    Add Factor( Discrete Numeric, {1, 2, 3}, "X2", 0 ),
    Discrete Numeric Powers Set to Necessary( 1 ),
    Make Model( Linear )
);
```

### [Distribution Choice](#distribution-choice)[](#distribution-choice "Click to copy url")

**Syntax:** obj \<\< Distribution Choice

**Description:** Specifies the distribution for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Enforce Use of Selected Covariate Rows](#enforce-use-of-selected-covariate-rows)[](#enforce-use-of-selected-covariate-rows "Click to copy url")

**Syntax:** obj \<\< Enforce Use of Selected Covariate Rows( state=0\|1 )

**Description:** Specifies if all selected covariate rows should be included in the design.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
DOE(
    Custom Design,
    Add Response( Maximize, "Y", ., ., . ),
    Add Factor( Covariate, :sex, 0 ),
    Add Factor( Covariate, :height, 0 ),
    Add Factor( Covariate, :weight, 0 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Enforce Use of Selected Covariate Rows( 1 ),
    Allow covariate rows to be repeated( 1 ),
    Select Covariate Rows( [1 2 3 4] ),
    Set Sample Size( 24 )
);
```

### [FFF Optimality Criterion](#fff-optimality-criterion)[](#fff-optimality-criterion "Click to copy url")

**Syntax:** obj \<\< FFF Optimality Criterion( "MaxPro"\|"Centroid" )

**Description:** Specifies the criterion used in the design. Recommended is the default value.

**Example 1**

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Optimality Criterion( "Make I-optimal Design" ),
    Make Design
);
```

**Example 2**

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Optimality Criterion( 2 ),
    Make Design
);
```

### [Find Subset](#find-subset)[](#find-subset "Click to copy url")

**Syntax:** obj \<\< Find Subset

**Description:** Finds the D-optimal subset of an Extreme Vertices design.

``` jsl
d = DOE( Mixture Design, Add Factor( Mixture, 0.1, 1, "X4", 0 ) );
d << Mixture Design Type( Extreme Vertices, 3 );
d << Find Subset( 10 );
```

### [GOSSDDetails](#gossddetails)[](#gossddetails "Click to copy url")

**Syntax:** obj \<\< GOSSDDetails

**Description:** Returns the current factor settings as a list.

**JMP Version Added:** 15

``` jsl
d = DOE( Group Orthogonal Supersaturated Design );
Show( d << GOSSDDetails );
```

### [GOSSDStructure](#gossdstructure)[](#gossdstructure "Click to copy url")

**Syntax:** obj \<\< GOSSDStructure

**Description:** Specifies the structure of a GOSSD

**JMP Version Added:** 15

``` jsl
d = DOE( Group Orthogonal Supersaturated Design );
d << GOSSDStructure( 6, 8 );
```

### [Get Alias Matrix](#get-alias-matrix)[](#get-alias-matrix "Click to copy url")

**Syntax:** obj \<\< Get Alias Matrix

**Description:** Returns the alias matrix from design evaluation.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Get Alias Matrix;
```

### [Get Design Diagnostics](#get-design-diagnostics)[](#get-design-diagnostics "Click to copy url")

**Syntax:** obj \<\< Get Design Diagnostics

**Description:** Return D-Efficiency, G-Efficiency, A-Efficiency and Average Variance of Prediction.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Get Design Diagnostics;
```

### [Get Effect Power](#get-effect-power)[](#get-effect-power "Click to copy url")

**Syntax:** obj \<\< Get Effect Power

**Description:** Return vector of powers for effect estimates.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/2x3x4 Factorial.jmp" );
d = DOE( Evaluate Design, X( :X1, :X2, :X3 ), Y( :Y ) );
d << Get Effect Power;
```

### [Get Estimation Efficiencies](#get-estimation-efficiencies)[](#get-estimation-efficiencies "Click to copy url")

**Syntax:** obj \<\< Get Estimation Efficiencies

**Description:** Returns a vector for the increased width of each parameter estimate compared to an ideal design.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Get Estimation Efficiencies;
```

### [Get MaxPro Values](#get-maxpro-values)[](#get-maxpro-values "Click to copy url")

**Syntax:** obj \<\< Get MaxPro Values

**Description:** Returns the MaxPro values for a fast-flexible design, including any subdesigns based on levels of a categorical factor.

**JMP Version Added:** 14

``` jsl
d = DOE(
    Space Filling Design,
    {Add Factor( Continuous, -1, 1, "X1", 0 ), Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Categorical, {"L1", "L2", "L3", "L4"}, "X3", 0 ),
    FFF Optimality Criterion( MaxPro ), MaxPro Categorical Weight( 4 ),
    Space Filling Design Type( Fast Flexible Filling, 100 )}
);
d << Get MaxPro Values;
```

### [Get Number of Random Starts](#get-number-of-random-starts)[](#get-number-of-random-starts "Click to copy url")

**Syntax:** obj \<\< Get Number of Random Starts

**Description:** Returns the number of random starts used in design generation.

**JMP Version Added:** 15

### [Get Power](#get-power)[](#get-power "Click to copy url")

**Syntax:** obj \<\< Get Power

**Description:** Return vector of powers for parameter estimates.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Get Power;
```

### [Get Prediction Variances](#get-prediction-variances)[](#get-prediction-variances "Click to copy url")

**Syntax:** obj \<\< Get Prediction Variances

**Description:** Returns the vector of prediction variances from the Fraction of Design Space Plot.

**JMP Version Added:** 14

``` jsl
d = DOE(
    Custom Design,
    {Add Factor( Continuous, -1, 1, "X1", 0 ), Add Factor( Continuous, -1, 1, "X2", 0 ),
    Set Sample Size( 7 ), Design Search Time( 8 ), Set Number of FDS points( 20000 ),
    Make Design}
);
d << Get Prediction Variances;
```

### [Get X Matrix](#get-x-matrix)[](#get-x-matrix "Click to copy url")

**Syntax:** obj \<\< Get X Matrix

**Description:** Returns the design matrix (also called the X matrix).

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Get X Matrix;
```

### [Group New Runs Into Separate Block](#group-new-runs-into-separate-block)[](#group-new-runs-into-separate-block "Click to copy url")

**Syntax:** obj \<\< Group New Runs Into Separate Block

**Description:** Adds a blocking factor, which groups new runs into separate blocks when augmenting a design.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Augment Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Group New Runs Into Separate Block;
```

### [Load Constraints](#load-constraints)[](#load-constraints "Click to copy url")

**Syntax:** obj \<\< Load Constraints

**Description:** Load a previously saved factor constraints table for use in this experiment.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Diamond Constraints.jmp" );
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Term( {1, 0} ),
    Load Constraints
);
```

### [Load Design](#load-design)[](#load-design "Click to copy url")

**Syntax:** obj \<\< Load Design

**Description:** Load Design

``` jsl
d = DOE( Custom Design );
d << Load Design();
```

### [Load Factors](#load-factors)[](#load-factors "Click to copy url")

**Syntax:** obj \<\< Load Factors

**Description:** Load a previously saved factors table for use in this experiment.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Factors.jmp" );
DOE( Custom Design, Load Factors );
```

### [Load Responses](#load-responses)[](#load-responses "Click to copy url")

**Syntax:** obj \<\< Load Responses

**Description:** Loads a previously saved data table of responses.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Response.jmp" );
DOE( Custom Design, Load Responses );
```

### [Local Design](#local-design)[](#local-design "Click to copy url")

**Syntax:** obj \<\< Local Design( state=0\|1 )

**Description:** Specifies if local design for the prior mean should be created.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( 2, {5, 200, 200} ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Local Design( 0 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Inspection Times( [200 400 600 800 1000] ),
    Set Number of Units( 150 ), Set Candidate Runs( [90 0 150, 100 0 150, 110 0 150] )}
);
```

### [Make Design](#make-design)[](#make-design "Click to copy url")

**Syntax:** obj \<\< Make Design

**Description:** Creates the design that you specified in the script.

``` jsl
d = DOE( Custom Design, Add factor, Add factor, Add factor );
d << Make Model( RSM );
d << Make Design;
```

### [Make Model](#make-model)[](#make-model "Click to copy url")

**Syntax:** obj \<\< Make Model( Linear\|Interactions\|RSM )

**Description:** Adds terms to the list of model terms for the specified model.

**Example 1**

``` jsl
d = DOE( Custom Design, Add Factor, Add Factor, Add Factor );
d << Make Model( RSM );
```

**Example 2**

``` jsl
d = DOE( Custom Design, Add Factor, Add Factor, Add Factor );
d << Make Model( Interactions );
```

### [Make Strip Plot Design](#make-strip-plot-design)[](#make-strip-plot-design "Click to copy url")

**Syntax:** obj \<\< Make Strip Plot Design

**Description:** Specifies a strip plot design when hard-to-change factors vary independently from very hard-to-change factors.

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 2 ),
    Add Factor( Continuous, -1, 1, "X2", 1 ),
    Add Factor( Continuous, -1, 1, "X3", 0 )
);
d << Set N Whole Plots( 4 );
d << Make Strip Plot Design;
```

### [Make Table](#make-table)[](#make-table "Click to copy url")

**Syntax:** obj \<\< Make Table

**Description:** Creates a data table from the current design.

``` jsl
d = DOE( Custom Design, Add factor, Add factor, Add factor );
d << Make Design;
d << Make Table;
```

### [Make Test Plan](#make-test-plan)[](#make-test-plan "Click to copy url")

**Syntax:** obj \<\< Make Test Plan

**Description:** Creates the test plan for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Monitoring at Intervals", {5, 200, 200} ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Inspection Times( [200 400 600 800 1000] ),
    Set Number of Units( 150 ), Set Candidate Runs( [90 0 150, 100 0 150, 110 0 150] ),
    Make Design, Make Test Plan}
);
```

### [MaxPro Categorical Weight](#maxpro-categorical-weight)[](#maxpro-categorical-weight "Click to copy url")

**Syntax:** obj \<\< MaxPro Categorical Weight

**Description:** Specifies MaxPro weight. Values larger than 1 increase the separation of points that have the same categorical level.

**JMP Version Added:** 14

``` jsl
DOE(
    Space Filling Design,
    {Add Factor( Continuous, -1, 1, "X1", 0 ), Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Categorical, {"L1", "L2", "L3", "L4"}, "X3", 0 ),
    FFF Optimality Criterion( MaxPro ), MaxPro Categorical Weight( 4 ),
    Space Filling Design Type( Fast Flexible Filling, 100 )}
);
```

### [Mixture Design Type](#mixture-design-type)[](#mixture-design-type "Click to copy url")

**Syntax:** obj \<\< Mixture Design Type( Simplex Centroid\|Simplex Lattice\|ABCD\|Extreme Vertices\|Space Filling )

**Description:** Specifies the type of mixture design. The default parameters are used unless you specify the parameter as the second argument.

**Example 1**

``` jsl
d = doe( Mixture Design );
d << Mixture Design Type( Simplex Centroid, 2 );
```

**Example 2**

``` jsl
d = doe( Mixture Design );
d << Mixture Design Type( Simplex Lattice, 4 );
```

**Example 3**

``` jsl
d = doe( Mixture Design );
d << Mixture Design Type( ABCD );
```

**Example 4**

``` jsl
d = doe( Mixture Design );
d << Change Factor Settings( 1, .05, .25 );
d << Mixture Design Type( Extreme Vertices, 3 );
```

**Example 5**

``` jsl
d = doe( Mixture Design );
d << Mixture Design Type( Space Filling, 25 );
```

### [Mixture Sum](#mixture-sum)[](#mixture-sum "Click to copy url")

**Syntax:** obj \<\< Mixture Sum

**Description:** Use this option when you want to express the sum of all the ingredients to be other than 1. The mixture total is the sum of all the ingredient amounts.

``` jsl
DOE(
    Custom Design,
    Mixture Sum( 50 ),
    Add Factor( Mixture, 10, 25, "X1", 0 ),
    Add Factor( Mixture, 0, 15, "X2", 0 ),
    Add Factor( Mixture, 25, 40, "X3", 0 ),
    Make Design
);
```

### [Nesting Structure](#nesting-structure)[](#nesting-structure "Click to copy url")

**Syntax:** obj \<\< Nesting Structure

**Description:** Specifies the nesting structure of the design. Use a bracketed list to indicate nesting (first element is nesting factor, second element is bracketed list of nested factors or structures). Use horizontal concatenation ('\|\|') to indicate crossed factors or structures.

``` jsl
DOE(
    MSA Design,
    Add Factor( Categorical, {"L1", "L2"}, "X1", MSA( 4, 1, 1 ) ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", MSA( 4, 1, 1 ) ),
    Add Factor( Categorical, {"L1", "L2"}, "X3", MSA( 4, 1, 1 ) ),
    Nesting Structure( {"X1", {"X2"}} || "X3" )
);
```

### [Number of Column Starts](#number-of-column-starts)[](#number-of-column-starts "Click to copy url")

**Syntax:** obj \<\< Number of Column Starts

**Description:** Specifies the number of times that random columns are optimized for each factor of a main effects screening design.

``` jsl
DOE(
    Screening Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Screening Type( 1 ),
    Number of Column Starts( 100 ),
    Set Sample Size( 12 ),
    Make Design
);
```

### [Number of Extra Runs](#number-of-extra-runs)[](#number-of-extra-runs "Click to copy url")

**Syntax:** obj \<\< Number of Extra Runs

**Description:** Specifies the number of extra runs to include in a definitive screening design.

``` jsl
DOE(
    Definitive Screening Design,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Show Blocking Options( 1, 2 ),
    Number of Extra Runs( 4 )
);
```

### [Number of Starts](#number-of-starts)[](#number-of-starts "Click to copy url")

**Syntax:** obj \<\< Number of Starts

**Description:** Specifies the number of times the design is regenerated to optimize the overall design.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Number of Starts( 1000 ),
    Make Design
);
```

### [Optimality Criterion](#optimality-criterion)[](#optimality-criterion "Click to copy url")

**Syntax:** obj \<\< Optimality Criterion( "Recommended"\|"Make D-Optimal Design"\|"Make I-Optimal Design"\|"Make A-Optimal Design"\|"Make Alias Optimal Design" )

**Description:** Specifies the criterion used in the design. Recommended is the default value.

**Example 1**

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Optimality Criterion( "Make I-optimal Design" ),
    Make Design
);
```

**Example 2**

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Optimality Criterion( 2 ),
    Make Design
);
```

### [Order Column](#order-column)[](#order-column "Click to copy url")

**Syntax:** obj \<\< Order Column

**Description:** Requests an order column when the data table is created.

**JMP Version Added:** 14

``` jsl
d = DOE( Balanced Incomplete Block Design );
d << Treatments( 3, {"L1", "L2", "L3"} );
d << Make Design;
d << OrderColumn( 1 );
```

### [Prior Parameter Variance](#prior-parameter-variance)[](#prior-parameter-variance "Click to copy url")

**Syntax:** obj \<\< Prior Parameter Variance

**Description:** Use this option to control the weight used for If Possible terms in a model. Higher values mean more prior information and smaller variance. The variances are the reciprocals of the entered values.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Potential Term( {1, 1} ),
    Add Potential Term( {2, 1} ),
    Add Potential Term( {1, 1}, {2, 1} ),
    Prior Parameter Variance( [0, 1, 2, 6] ),
    Make Design
);
```

### [Prior Specification Choice](#prior-specification-choice)[](#prior-specification-choice "Click to copy url")

**Syntax:** obj \<\< Prior Specification Choice

**Description:** Sets the option for specifying prior parameters, where 1 indicates Specify Intercept and 2 indicates Specify Quantile.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Prior Specification Choice( 1 ), Set Prior Mean ALT( [-40 1.5 2] ),
    Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Reference Design](#reference-design)[](#reference-design "Click to copy url")

**Syntax:** obj \<\< Reference Design

**Description:** Specify the reference design for design comparison.

**JMP Version Added:** 14

``` jsl
DOE(
    Custom Design,
    Add Factor,
    Add Factor,
    Add Factor,
    Set Sample Size( 12 ),
    Make Design,
    Make Table
);
DOE( Custom Design, Add Factor, Add Factor, Add Factor, Make Design, Make Table );
DOE(
    Custom Design,
    Add Factor,
    Add Factor,
    Add Factor,
    Set Sample Size( 4 ),
    Make Design,
    Make Table
);
DOE(
    Compare Designs,
    Reference Design( "Custom Design", X( :X1, :X2, :X3 ) ),
    Additional Designs(
        "Custom Design 2",
        X( :X1, :X2, :X3 ),
        "Custom Design 3",
        X( :X1, :X2, :X3 )
    )
);
```

### [Remove Alias Term](#remove-alias-term)[](#remove-alias-term "Click to copy url")

**Syntax:** obj \<\< Remove Alias Term

**Description:** Removes a term from the list of alias terms. Specify the factor number and power for each effect in a list. Create interactions by separating effects with commas.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Remove Alias Term( {1, 1}, {3, 1} );
```

### [Remove All Alias Terms](#remove-all-alias-terms)[](#remove-all-alias-terms "Click to copy url")

**Syntax:** obj \<\< Remove All Alias Terms

**Description:** Removes all Alias Terms from the list of alias terms

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 )
);
d << Make Model( Linear );
d << Remove All Alias Terms;
```

### [Remove Term](#remove-term)[](#remove-term "Click to copy url")

**Syntax:** obj \<\< Remove Term

**Description:** Removes a term from the list of model terms. Specify the factor number and power for each effect in a list. Create interactions by separating effects with commas.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Remove Term( {1, 1}, {3, 1} );
d << Remove Term( {3, 2} );
```

### [Replicates](#replicates)[](#replicates "Click to copy url")

**Syntax:** obj \<\< Replicates

**Description:** Specifies the number of replicate runs. For MSA Designs, a second argument specifies the replicate structure: 0=Completely Randomized, 1=Batch Repeat, 2=Fast Repeat.

**Example 1**

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 )
);
d << Make Model( Linear );
d << Replicates( 2 );
```

**Example 2**

``` jsl
d = DOE(
    MSA Design,
    {Add Response( None, "Y", ., ., . ), Add Factor(
        Categorical,
        {"L1", "L2"},
        "X1",
        MSA( 4, 1 )
    ), Add Factor( Categorical, {"L1", "L2"}, "X2", MSA( 4, 1 ) ),
    Add Factor( Categorical, {"L1", "L2"}, "X3", MSA( 4, 1 ) ), Set Random Seed( 3983347 ),
    Replicates( 2, 0 ), Simulate Responses( 0 )}
);
```

### [Report](#report)[](#report "Click to copy url")

**Syntax:** obj \<\< Report

**Description:** Returns a reference to the report object.

``` jsl
d = DOE( Custom Design );
r = d << report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Save Constraints](#save-constraints)[](#save-constraints "Click to copy url")

**Syntax:** obj \<\< Save Constraints

**Description:** Save the factor constraints of the current experiment to a JMP table for use in another experiment

``` jsl
DOE(
    Custom Design,
    Add Response( Maximize, "Y", ., ., . ),
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Add Constraint( [1 1 0 1, 1 0 1 1] ),
    Add Term( {1, 0} ),
    Save Constraints
);
```

### [Save Factors](#save-factors)[](#save-factors "Click to copy url")

**Syntax:** obj \<\< Save Factors

**Description:** Save the factors you just created to a JMP table so you can use these factors for another experiment.

``` jsl
DOE(
    Custom Design,
    Add Response( Match Target, "Stretch", 350, 550, 1 ),
    Add Factor( Continuous, 0.7, 1.7, "Silica", 0 ),
    Add Factor( Continuous, 1.8, 2.8, "Sulfur", 0 ),
    Add Factor( Continuous, 40, 60, "Silane", 0 ),
    Save Factors
);
```

### [Save Responses](#save-responses)[](#save-responses "Click to copy url")

**Syntax:** obj \<\< Save Responses

**Description:** Saves the responses that you created as a JMP data table. You can load these responses in other experiments.

``` jsl
DOE(
    Custom Design,
    Add Response( Match Target, "Stretch", 350, 550, 1 ),
    Add Factor( Continuous, 0.7, 1.7, "Silica", 0 ),
    Add Factor( Continuous, 1.8, 2.8, "Sulfur", 0 ),
    Add Factor( Continuous, 40, 60, "Silane", 0 ),
    Save Responses
);
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script to Data Table

**Description:** Create a Script that will reproduce this design.

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a Script that will reproduce this design.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Make Design,
    Save Script to Script Window
);
```

### [Save X Matrix](#save-x-matrix)[](#save-x-matrix "Click to copy url")

**Syntax:** obj \<\< Save X Matrix( state=0\|1 )

**Description:** Saves the design matrix (also called the X matrix) as a table property in the JMP data table that contains the design.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Save X Matrix,
    Make Design,
    Make Table
);
```

### [Screening Type](#screening-type)[](#screening-type "Click to copy url")

**Syntax:** obj \<\< Screening Type

**Description:** Specifies a main effects screening design, which is orthogonal or near orthogonal.

``` jsl
d = DOE(
    Screening Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 )
);
d << Screening Type( 1 );
d << Set Sample Size( 12 );
d << Make Design;
```

### [Select Covariate Rows](#select-covariate-rows)[](#select-covariate-rows "Click to copy url")

**Syntax:** obj \<\< Select Covariate Rows

**Description:** Specifies the rows from the covariate table to be selected in DOE.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
DOE(
    Custom Design,
    Add Response( Maximize, "Y", ., ., . ),
    Add Factor( Covariate, :sex, 0 ),
    Add Factor( Covariate, :height, 0 ),
    Add Factor( Covariate, :weight, 0 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Enforce Use of Selected Covariate Rows( 1 ),
    Allow covariate rows to be repeated( 1 ),
    Select Covariate Rows( [1 2 3 4] ),
    Set Sample Size( 24 )
);
```

### [Set ALT Probability of Interest](#set-alt-probability-of-interest)[](#set-alt-probability-of-interest "Click to copy url")

**Syntax:** obj \<\< Set ALT Probability of Interest

**Description:** Sets the probability of interest for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Set ALT Time Range](#set-alt-time-range)[](#set-alt-time-range "Click to copy url")

**Syntax:** obj \<\< Set ALT Time Range

**Description:** Sets the time range of interest for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Failure Probability Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Set Average Cluster Size](#set-average-cluster-size)[](#set-average-cluster-size "Click to copy url")

**Syntax:** obj \<\< Set Average Cluster Size

**Description:** Controls number of random points for clustering a Fast Flexible Filling Design.

``` jsl
DOE(
    Space Filling Design,
    Change Factor Settings( 1, -1, 1, "X1" ),
    Change Factor Settings( 2, -1, 1, "X2" ),
    Set Average Cluster Size( 100 ),
    Space Filling Design Type( Fast Flexible Filling, 50 )
);
```

### [Set Axial Choice](#set-axial-choice)[](#set-axial-choice "Click to copy url")

**Syntax:** obj \<\< Set Axial Choice( 1\|2\|3\|4 )

**Description:** Specifies the axial value settings. Use 1 for Rotatable, 2 for Orthogonal, 3 for On Face, and 4 User Specified.

``` jsl
d = DOE( Response Surface Design, Make Design( 2 ) );
d << Set Axial Choice( 2 );
```

### [Set Axial Value](#set-axial-value)[](#set-axial-value "Click to copy url")

**Syntax:** obj \<\< Set Axial Value

**Description:** Specifies the User Specified axial value.

``` jsl
d = DOE( Response Surface Design, Make Design( 2 ) );
d << Set Axial Value( 2 );
```

### [Set Candidate Runs](#set-candidate-runs)[](#set-candidate-runs "Click to copy url")

**Syntax:** obj \<\< Set Candidate Runs

**Description:** Sets the candidate runs for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Monitoring at Intervals", {5, 200, 200} ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Inspection Times( [200 400 600 800 1000] ),
    Set Number of Units( 150 ), Set Candidate Runs( [90 0 150, 100 0 150, 110 0 150] )}
);
```

### [Set Delta For Power](#set-delta-for-power)[](#set-delta-for-power "Click to copy url")

**Syntax:** obj \<\< Set Delta For Power

**Description:** Specifies the values of the anticipated coefficients in Power Analysis. Anticipated coefficients will be one half of the specified value.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Set Delta For Power( 3 ),
    Make Design
);
```

### [Set Expected Number of Respondents](#set-expected-number-of-respondents)[](#set-expected-number-of-respondents "Click to copy url")

**Syntax:** obj \<\< Set Expected Number of Respondents

**Description:** Sets the expected number of respondents per survey.

``` jsl
DOE(
    Choice Design,
    {Add Factor( Categorical, {"L1", "L2"}, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ), Set Random Seed( 1245253625 ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Set Prior Mean Choice( [0 0] ),
    Set Prior Variance Matrix( [1 0, 0 1] ), Set Number of Attributes( 2 ),
    Set Number of Profiles( 2 ), Set Number of Choice Sets( 8 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 1 )}
);
```

### [Set Generators](#set-generators)[](#set-generators "Click to copy url")

**Syntax:** obj \<\< Set Generators

**Description:** Specifies the generators to be used in a screening design.

``` jsl
DOE(
    Screening Design,
    {Add Factor, Add Factor, Add Factor, Make Design( 1 ), Set Generators( [1, 1, 0] )}
);
```

### [Set Inspection Times](#set-inspection-times)[](#set-inspection-times "Click to copy url")

**Syntax:** obj \<\< Set Inspection Times

**Description:** Sets the inspection times for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Monitoring at Intervals", {5, 200, 200} ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Inspection Times( [200 400 600 800 1000] ),
    Set Number of Units( 150 ), Set Candidate Runs( [90 0 150, 100 0 150, 110 0 150] )}
);
```

### [Set Length of Test](#set-length-of-test)[](#set-length-of-test "Click to copy url")

**Syntax:** obj \<\< Set Length of Test

**Description:** Sets the length of test for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Set Level Values](#set-level-values)[](#set-level-values "Click to copy url")

**Syntax:** obj \<\< Set Level Values

**Description:** Sets the level values for the accelerating factor(s) in an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Monitoring at Intervals", {5, 200, 200} ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Inspection Times( [200 400 600 800 1000] ),
    Set Number of Units( 150 ), Set Candidate Runs( [90 0 150, 100 0 150, 110 0 150] )}
);
```

### [Set Monitoring Choice](#set-monitoring-choice)[](#set-monitoring-choice "Click to copy url")

**Syntax:** obj \<\< Set Monitoring Choice

**Description:** Specifies the type of monitoring for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Set N Subplots](#set-n-subplots)[](#set-n-subplots "Click to copy url")

**Syntax:** obj \<\< Set N Subplots

**Description:** Specifies the number of subplots when there are both hard-to-change and very hard-to-change factors.

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 2 ),
    Add Factor( Continuous, -1, 1, "X2", 1 ),
    Add Factor( Continuous, -1, 1, "X3", 0 )
);
d << Set N Whole Plots( 4 );
d << Set N Subplots( 8 );
```

### [Set N Whole Plots](#set-n-whole-plots)[](#set-n-whole-plots "Click to copy url")

**Syntax:** obj \<\< Set N Whole Plots

**Description:** Specifies the number of whole plots when there are hard-to-change or very hard-to-change factors.

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 1 ),
    Add Factor( Continuous, -1, 1, "X2", 0 )
);
d << Set N Whole Plots( 6 );
```

### [Set Number of Attributes](#set-number-of-attributes)[](#set-number-of-attributes "Click to copy url")

**Syntax:** obj \<\< Set Number of Attributes

**Description:** Sets the number of attributes that can change within a choice set.

``` jsl
DOE(
    Choice Design,
    {Add Factor( Categorical, {"L1", "L2"}, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ), Set Random Seed( 1245253625 ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Set Prior Mean Choice( [0 0] ),
    Set Prior Variance Matrix( [1 0, 0 1] ), Set Number of Attributes( 2 ),
    Set Number of Profiles( 2 ), Set Number of Choice Sets( 8 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 1 )}
);
```

### [Set Number of Choice Sets](#set-number-of-choice-sets)[](#set-number-of-choice-sets "Click to copy url")

**Syntax:** obj \<\< Set Number of Choice Sets

**Description:** Sets the number of choice sets per survey.

``` jsl
DOE(
    Choice Design,
    {Add Factor( Categorical, {"L1", "L2"}, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ), Set Random Seed( 1245253625 ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Set Prior Mean Choice( [0 0] ),
    Set Prior Variance Matrix( [1 0, 0 1] ), Set Number of Attributes( 2 ),
    Set Number of Profiles( 2 ), Set Number of Choice Sets( 8 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 1 )}
);
```

### [Set Number of FDS points](#set-number-of-fds-points)[](#set-number-of-fds-points "Click to copy url")

**Syntax:** obj \<\< Set Number of FDS points

**Description:** Sets the number of points used to generate the Fraction of Design Space Plot.

**JMP Version Added:** 14

``` jsl
DOE(
    Custom Design,
    {Add Factor( Continuous, -1, 1, "X1", 0 ), Add Factor( Continuous, -1, 1, "X2", 0 ),
    Set Sample Size( 7 ), Design Search Time( 8 ), Set Number of FDS points( 20000 ),
    Make Design}
);
```

### [Set Number of Profiles](#set-number-of-profiles)[](#set-number-of-profiles "Click to copy url")

**Syntax:** obj \<\< Set Number of Profiles

**Description:** Sets the number of profiles per choice set.

``` jsl
DOE(
    Choice Design,
    {Add Factor( Categorical, {"L1", "L2"}, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ), Set Random Seed( 1245253625 ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Set Prior Mean Choice( [0 0] ),
    Set Prior Variance Matrix( [1 0, 0 1] ), Set Number of Attributes( 2 ),
    Set Number of Profiles( 2 ), Set Number of Choice Sets( 8 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 1 )}
);
```

### [Set Number of Surveys](#set-number-of-surveys)[](#set-number-of-surveys "Click to copy url")

**Syntax:** obj \<\< Set Number of Surveys

**Description:** Sets the number of surveys for a choice design.

``` jsl
DOE(
    Choice Design,
    {Add Factor( Categorical, {"L1", "L2"}, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ), Set Random Seed( 1245253625 ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Set Prior Mean Choice( [0 0] ),
    Set Prior Variance Matrix( [1 0, 0 1] ), Set Number of Attributes( 2 ),
    Set Number of Profiles( 2 ), Set Number of Choice Sets( 8 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 1 )}
);
```

### [Set Number of Units](#set-number-of-units)[](#set-number-of-units "Click to copy url")

**Syntax:** obj \<\< Set Number of Units

**Description:** Sets the number of units under test for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Set Prior Correlation ALT](#set-prior-correlation-alt)[](#set-prior-correlation-alt "Click to copy url")

**Syntax:** obj \<\< Set Prior Correlation ALT

**Description:** Sets the prior correlations for an accelerated life test plan.

**JMP Version Added:** 16

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Set Prior Mean ALT](#set-prior-mean-alt)[](#set-prior-mean-alt "Click to copy url")

**Syntax:** obj \<\< Set Prior Mean ALT

**Description:** Sets the prior mean for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Set Prior Mean Choice](#set-prior-mean-choice)[](#set-prior-mean-choice "Click to copy url")

**Syntax:** obj \<\< Set Prior Mean Choice

**Description:** Sets the Prior Mean for a choice design.

``` jsl
DOE(
    Choice Design,
    {Add Factor( Categorical, {"L1", "L2"}, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ), Set Random Seed( 1245253625 ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Set Prior Mean Choice( [0 0] ),
    Set Prior Variance Matrix( [1 0, 0 1] ), Set Number of Attributes( 2 ),
    Set Number of Profiles( 2 ), Set Number of Choice Sets( 8 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 1 )}
);
```

### [Set Prior Quantile ALT](#set-prior-quantile-alt)[](#set-prior-quantile-alt "Click to copy url")

**Syntax:** obj \<\< Set Prior Quantile ALT

**Description:** Sets the information for specifying the prior intercept based on a quantile.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Prior Specification Choice( 2 ), Set Prior Quantile ALT( {[1.5 2], 0.065, 2642, 45} ),
    Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Set Prior Std Error ALT](#set-prior-std-error-alt)[](#set-prior-std-error-alt "Click to copy url")

**Syntax:** obj \<\< Set Prior Std Error ALT

**Description:** Sets the prior standard error for an accelerated life test plan.

**JMP Version Added:** 16

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Number of Units( 150 )}
);
```

### [Set Prior Variance ALT](#set-prior-variance-alt)[](#set-prior-variance-alt "Click to copy url")

**Syntax:** obj \<\< Set Prior Variance ALT

**Description:** Sets the prior variance for an accelerated life test plan.

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( "Continuous Monitoring" ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Variance ALT( [0.1 0 0, 0 0.1 0, 0 0 0.1] ),
    Use Prior Uncertainty( 1 ), Set ALT Time Range( 10000, 20000 ),
    Set ALT Probability of Interest( 0.1 ), Set Length of Test( 1000 ),
    Set Number of Units( 150 )}
);
```

### [Set Prior Variance Matrix](#set-prior-variance-matrix)[](#set-prior-variance-matrix "Click to copy url")

**Syntax:** obj \<\< Set Prior Variance Matrix

**Description:** Sets the Prior Variance Matrix for a choice design.

``` jsl
DOE(
    Choice Design,
    {Add Factor( Categorical, {"L1", "L2"}, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ), Set Random Seed( 1245253625 ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Set Prior Mean Choice( [0 0] ),
    Set Prior Variance Matrix( [1 0, 0 1] ), Set Number of Attributes( 2 ),
    Set Number of Profiles( 2 ), Set Number of Choice Sets( 8 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 1 )}
);
```

### [Set RMSE](#set-rmse)[](#set-rmse "Click to copy url")

**Syntax:** obj \<\< Set RMSE

**Description:** Specifies the anticipated root mean square error (RMSE) in Power Analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Set RMSE( 1.5 );
```

### [Set Random Seed](#set-random-seed)[](#set-random-seed "Click to copy url")

**Syntax:** obj \<\< Set Random Seed

**Description:** Useful for teaching. Setting the random seed to a specific value assures that all class members get the same design.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Set Random Seed( 34067086 ),
    Make Design
);
```

### [Set Run Order](#set-run-order)[](#set-run-order "Click to copy url")

**Syntax:** obj \<\< Set Run Order

**Description:** Specifies how the run order should be set when making a data table from a design.

``` jsl
d = DOE( Custom Design, Add factor, Add factor, Add factor );
d << Make Design;
d << Set Run Order( Sort Left to Right );
d << Make Table;
```

### [Set Runs Per Random Block](#set-runs-per-random-block)[](#set-runs-per-random-block "Click to copy url")

**Syntax:** obj \<\< Set Runs Per Random Block

**Description:** Specifies the size of random blocks in the design.

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Make Model( Linear )
);
d << Set Runs Per Random Block( 4 );
```

### [Set Sample Size](#set-sample-size)[](#set-sample-size "Click to copy url")

**Syntax:** obj \<\< Set Sample Size

**Description:** Specifies the sample size before the design is created. If the specified number is less than the minimum value shown in the designer, the sample size is set to the minimum value.

``` jsl
d = DOE( Custom Design, Add factor, Add factor, Add factor );
d << Make Model( Linear );
d << Set Sample Size( 12 );
```

### [Set Significance Level](#set-significance-level)[](#set-significance-level "Click to copy url")

**Syntax:** obj \<\< Set Significance Level

**Description:** Change the significance level in Power Analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Design Experiment/Bounce Data.jmp" );
d = DOE( Evaluate Design, X( :Silica, :Sulfur, :Silane ), Y( :Stretch ) );
d << Set Significance Level( 0.10 );
```

### [Set Strength](#set-strength)[](#set-strength "Click to copy url")

**Syntax:** obj \<\< Set Strength

**Description:** Sets the strength for Covering Arrays

``` jsl
d = DOE(
    Covering Array,
    Add factor( Categorical ),
    Add factor( Categorical ),
    Add factor( Categorical )
);
d << Set Strength( 3 );
d << Make Table;
```

### [Show Blocking Options](#show-blocking-options)[](#show-blocking-options "Click to copy url")

**Syntax:** obj \<\< Show Blocking Options

**Description:** Specifies the blocking choice and number of blocks for a definitive screening design. Specifying a value of 0 indicates no blocks.

**Example 1**

``` jsl
DOE(
    Definitive Screening Design,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Show Blocking Options( 0, 0 ),
    Number of Extra Runs( 4 )
);
```

**Example 2**

``` jsl
DOE(
    Definitive Screening Design,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Add Factor,
    Show Blocking Options( 1, 2 ),
    Number of Extra Runs( 4 )
);
```

### [Simulate Responses](#simulate-responses)[](#simulate-responses "Click to copy url")

**Syntax:** obj \<\< Simulate Responses( state=0\|1 )

**Description:** Add data for the responses to the JMP design table. For use in teaching DOE.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Make Design,
    Simulate Responses,
    Make Table
);
```

### [Solve for Power](#solve-for-power)[](#solve-for-power "Click to copy url")

**Syntax:** obj \<\< Solve for Power

**Description:** Sets the anticipated coefficients in Power Analysis so that the power is near the specified value.

**JMP Version Added:** 16

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Make Design,
    Solve for Power( 0.8 )
);
```

### [Space Filling Design Type](#space-filling-design-type)[](#space-filling-design-type "Click to copy url")

**Syntax:** obj \<\< Space Filling Design Type( Sphere Packing\|Latin Hypercube\|Uniform\|Minimum Potential\|Maximum Entropy\|IMSE Optimal\|Fast Flexible Filling )

**Description:** Specifies the type of space filling design and the number of runs.

**Example 1**

``` jsl
d = DOE( Space Filling Design );
d << Space Filling Design Type( Sphere Packing, 30 );
```

**Example 2**

``` jsl
d = DOE( Space Filling Design );
d << Space Filling Design Type( Latin Hypercube, 100 );
```

**Example 3**

``` jsl
d = DOE( Space Filling Design );
d << Space Filling Design Type( Uniform, 20 );
```

**Example 4**

``` jsl
d = DOE( Space Filling Design );
d << Space Filling Design Type( Fast Flexible Filling, 100 );
```

**Example 5**

``` jsl
d = DOE( Space Filling Design, Space Filling Design Type( IMSE Optimal, 20 ) );
d << Theta( [2, 3] );
d << Make Design;
```

### [Sphere Radius](#sphere-radius)[](#sphere-radius "Click to copy url")

**Syntax:** obj \<\< Sphere Radius

**Description:** Specifies a spherical design region and enables you to set the radius of the region.

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Sphere Radius( 1 ),
    Make Design
);
```

### [Split Plot Variance Ratio](#split-plot-variance-ratio)[](#split-plot-variance-ratio "Click to copy url")

**Syntax:** obj \<\< Split Plot Variance Ratio( Whole Plot Ratio \| \[Whole Plot Ratio, Subplot Ratio\] )

**Description:** For hard-to-change factors, specify the ratio of the whole-plot error variance to the run-to-run error. For hard-to-change and very hard-to-change factors, specify the ratio of the whole plot and subplot error to the run-to-run error.

**Example 1**

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 1 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Set N Whole Plots( 4 ),
    Split Plot Variance Ratio( 2 ),
    Make Design
);
```

**Example 2**

``` jsl
d = DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 2 ),
    Add Factor( Continuous, -1, 1, "X2", 1 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Set N Whole Plots( 4 )
);
d << Split Plot Variance Ratio( [3, 2] );
d << Make Design;
```

### [Suppress Cotter Designs](#suppress-cotter-designs)[](#suppress-cotter-designs "Click to copy url")

**Syntax:** obj \<\< Suppress Cotter Designs( state=0\|1 )

**Description:** Shows or hides Cotter designs in the list of screening designs. This option is selected by default, which means that Cotters designs are initially not in the screening design list. On by default.

``` jsl
DOE(
    Screening Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Factor( Continuous, -1, 1, "X3", 0 ),
    Suppress Cotter Designs,
    Make Design( 5 )
);
```

### [Table of Correlations](#table-of-correlations)[](#table-of-correlations "Click to copy url")

**Syntax:** obj \<\< Table of Correlations

**Description:** Create a data table with the Table of Correlations from Design Diagnostics.

**JMP Version Added:** 15

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Make Design,
    Table of Correlations
);
```

### [Theta](#theta)[](#theta "Click to copy url")

**Syntax:** obj \<\< Theta

**Description:** Specifies the Covariance Parameter Vector for Space Filling designs.

``` jsl
d = DOE( Space Filling Design, Space Filling Design Type( IMSE Optimal, 20 ) );
d << Theta( [2, 3] );
```

### [Treatments](#treatments)[](#treatments "Click to copy url")

**Syntax:** obj \<\< Treatments

**Description:** Specifies the number of treatments for a balanced incomplete block design (BIBD).

**JMP Version Added:** 14

``` jsl
d = DOE( Balanced Incomplete Block Design );
d << Treatments( 3, {"L1", "L2", "L3"} );
d << Make Design;
```

### [Use Bayesian information](#use-bayesian-information)[](#use-bayesian-information "Click to copy url")

**Syntax:** obj \<\< Use Bayesian information( state=0\|1 )

**Description:** Uses prior information in the Bayesian setting for the design diagnostics.

**JMP Version Added:** 15

``` jsl
DOE(
    Custom Design,
    Add Factor( Continuous, -1, 1, "X1", 0 ),
    Add Factor( Continuous, -1, 1, "X2", 0 ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Potential Term( {1, 1}, {2, 1} ),
    Number of Starts( 10 ),
    Make Design,
    Use Bayesian Information( 1 )
);
```

### [Use Blue to Red color theme for color map](#use-blue-to-red-color-theme-for-color-map)[](#use-blue-to-red-color-theme-for-color-map "Click to copy url")

**Syntax:** obj \<\< Use Blue to Red color theme for color map( state=0\|1 )

**Description:** Uses blue to red color theme for color map on correlations.

**JMP Version Added:** 15

### [Use Prior Uncertainty](#use-prior-uncertainty)[](#use-prior-uncertainty "Click to copy url")

**Syntax:** obj \<\< Use Prior Uncertainty( state=0\|1 )

**Description:** Specifies if the prior uncertainty should be used to construct the optimal design.

**JMP Version Added:** 16

``` jsl
DOE(
    Accelerated Life Test Plan,
    {ALT Plan Setup( 1 ), Set Monitoring Choice( 2, {5, 200, 200} ),
    ALT Optimality Criterion( "Make Quantile Estimate Optimal" ),
    ALT Factor Settings( 1, {"X1", 3, 1, 20, 30, 90, 110} ),
    Set Level Values( 1, [90 100 110] ), Distribution Choice( LogNormal ),
    Set Prior Mean ALT( [-40 1.5 2] ), Set Prior Std Error ALT( [10, 0.2, 0.5] ),
    Set Prior Correlation ALT( [1 -0.99 0, -0.99 1 0, 0 0 1] ), Use Prior Uncertainty( 1 ),
    Set ALT Time Range( 10000, 20000 ), Set ALT Probability of Interest( 0.1 ),
    Set Length of Test( 1000 ), Set Inspection Times( [200 400 600 800 1000] ),
    Set Number of Units( 150 ), Set Candidate Runs( [90 0 150, 100 0 150, 110 0 150] )}
);
```

### [Utility Neutral Design](#utility-neutral-design)[](#utility-neutral-design "Click to copy url")

**Syntax:** obj \<\< Utility Neutral Design( state=0\|1 )

**Description:** Specifies if Utility Neutral Choice Design should be created.

``` jsl
DOE(
    Choice Design,
    {Add Factor( Categorical, {"L1", "L2"}, "X1", 0 ),
    Add Factor( Categorical, {"L1", "L2"}, "X2", 0 ), Set Random Seed( 1245253625 ),
    Add Term( {1, 1} ), Add Term( {2, 1} ), Set Prior Mean Choice( [0 0] ),
    Set Prior Variance Matrix( [1 0, 0 1] ), Set Number of Attributes( 2 ),
    Set Number of Profiles( 2 ), Set Number of Choice Sets( 8 ), Set Number of Surveys( 1 ),
    Set Expected Number of Respondents( 1 ), Utility Neutral Design( 1 )}
);
```

[ Previous](DLLScriptable.html "DLLScriptable") [Next ](Data%20Connector%20Metadata.html "Data Connector Metadata")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
