# DOE

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/DOE.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/DOE.html)*

---

# [DOE](#doe)[](#doe "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Make a full factorial design with a continuous factor, a 3-level categorical factor and a 4 level categorical factor](#make-a-full-factorial-design-with-a-continuous-factor-a-3-level-categorical-factor-and-a-4-level-categorical-factor)[](#make-a-full-factorial-design-with-a-continuous-factor-a-3-level-categorical-factor-and-a-4-level-categorical-factor "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/2x3x4 Factorial.jmp");
// DOE Dialog
DOE(
    Full Factorial Design,
    {
    Add Response(
        Maximize, "Y", ., ., .
    ),
    Add Factor(
        Continuous,
        {-1, 1},
        "X1",
        0
    ),
    Add Factor(
        Categorical,
        {"x", "y", "z"},
        "X2",
        0
    ),
    Add Factor(
        Categorical,
        {"A", "B", "C", "D"},
        "X3",
        0
    ), Set Random Seed( 151647685 ),
    Make Design, Simulate Responses( 0 ),
    Set Run Order( Sort Left to Right ),
    Make Table}
);
```

### [Generate a 50 trial space filling design with 3 continuous factors and 2 categorical factors](#generate-a-50-trial-space-filling-design-with-3-continuous-factors-and-2-categorical-factors)[](#generate-a-50-trial-space-filling-design-with-3-continuous-factors-and-2-categorical-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Algorithm Data.jmp");
// DOE Dialog
DOE(
    Space Filling Design,
    {
    Add Response(
        Maximize, "CPU Time", ., ., .
    ),
    Change Factor Settings(
        1, -1, 1, "Alpha"
    ),
    Change Factor Settings(
        2, -1, 1, "Beta"
    ),
    Add Factor(
        Continuous, -1, 1, "Gamma", 0
    ),
    Add Factor(
        Categorical,
        {"Dynamic", "Greedy", "Transform"
        },
        "Algorithm",
        0
    ),
    Add Factor(
        Categorical,
        {"A", "B"},
        "Compiler",
        0
    ), Set Random Seed( 12345 ),
    FFF Optimality Criterion( "MaxPro" ),
    Space Filling Design Type(
        Fast Flexible Filling, 50
    ), Make Table}
);
```

### [Generate a response surface design with three response targets and four factors, including center points, in the DOE platform.](#generate-a-response-surface-design-with-three-response-targets-and-four-factors-including-center-points-in-the-doe-platform)[](#generate-a-response-surface-design-with-three-response-targets-and-four-factors-including-center-points-in-the-doe-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Bounce Data.jmp");
// DOE Dialog
DOE(
    Response Surface Design,
    {
    Add Response(
        Match Target, "Stretch", 350, 550,
        1
    ),
    Change Factor Settings(
        1, 0.7, 1.7, "Silica"
    ),
    Change Factor Settings(
        2, 1.8, 2.8, "Sulfur"
    ),
    Add Factor(
        Continuous, 40, 60, "Silane", 0
    ), Set Random Seed( 12345 ),
    Make Design( 1 ), Center Points( 3 ),
    Make Table}
);
```

### [Generate a custom design experiment using the DOE platform with categorical factors for furnace temperature and coating, and maximize the response for corrosion resistance.](#generate-a-custom-design-experiment-using-the-doe-platform-with-categorical-factors-for-furnace-temperature-and-coating-and-maximize-the-response-for-corrosion-resistance)[](#generate-a-custom-design-experiment-using-the-doe-platform-with-categorical-factors-for-furnace-temperature-and-coating-and-maximize-the-response-for-corrosion-resistance "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Box Corrosion Split-Plot.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        Maximize, "Corrosion Resistance",
        ., ., .
    ),
    Add Factor(
        Categorical,
        {"360", "370", "380"},
        "Furnace Temp",
        1
    ),
    Add Factor(
        Categorical,
        {"C1", "C2", "C3", "C4"},
        "Coating",
        0
    ), Set Random Seed( 15973514 ),
    Number of Starts( 3 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {1, 1}, {2, 1} ),
    Set Sample Size( 24 ),
    Set N Whole Plots( 6 ), Make Design}
);
```

### [Design a custom experimental design with response maximization and multiple continuous factors.](#design-a-custom-experimental-design-with-response-maximization-and-multiple-continuous-factors)[](#design-a-custom-experimental-design-with-response-maximization-and-multiple-continuous-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Catalyst Design.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        Maximize, "Y", ., ., .
    ),
    Add Factor(
        Continuous, -1, 1, "Temperature",
        2
    ),
    Add Factor(
        Continuous, -1, 1, "Time", 1
    ),
    Add Factor(
        Continuous, -1, 1, "Catalyst", 0
    ), Set Random Seed( 12345 ),
    Number of Starts( 1000 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Add Term( {1, 1}, {2, 1} ),
    Add Term( {1, 1}, {3, 1} ),
    Add Term( {2, 1}, {3, 1} ),
    Set N Whole Plots( 4 ),
    Set N Subplots( 8 ),
    Set Sample Size( 24 ),
    Simulate Responses, Make Design}
);
```

### [Create a custom design of experiments dialog for optimizing coffee brewing conditions, including categorical and continuous factors, responses, and alias terms.](#create-a-custom-design-of-experiments-dialog-for-optimizing-coffee-brewing-conditions-including-categorical-and-continuous-factors-responses-and-alias-terms)[](#create-a-custom-design-of-experiments-dialog-for-optimizing-coffee-brewing-conditions-including-categorical-and-continuous-factors-responses-and-alias-terms "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Coffee Data.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        Match Target, "Strength", 1.2,
        1.4, .
    ),
    Add Factor(
        Categorical,
        {"Coarse", "Medium"},
        "Grind",
        0
    ),
    Add Factor(
        Continuous, 195, 205,
        "Temperature", 0
    ),
    Add Factor(
        Continuous, 3, 4, "Time", 0
    ),
    Add Factor(
        Continuous, 1.6, 2.4, "Charge", 0
    ),
    Add Factor( Blocking, 4, "Station" ),
    Set Random Seed( 569534903 ),
    Number of Starts( 100 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Add Term( {4, 1} ),
    Add Term( {5, 1} ),
    Add Alias Term( {1, 1}, {2, 1} ),
    Add Alias Term( {1, 1}, {3, 1} ),
    Add Alias Term( {1, 1}, {4, 1} ),
    Add Alias Term( {2, 1}, {3, 1} ),
    Add Alias Term( {2, 1}, {4, 1} ),
    Add Alias Term( {3, 1}, {4, 1} ),
    Set Sample Size( 12 ), Make Design}
);
```

### [Generate a custom response surface method (RSM) design using the DOE platform with specified factors, responses, and optimality criteria. The code opens a sample data table, configures the DOE dialog to include three continuous factors, sets the random seed and number of starts for optimization, specifies the model terms, and finalizes the design with a specified sample size and optimality criterion.](#generate-a-custom-response-surface-method-rsm-design-using-the-doe-platform-with-specified-factors-responses-and-optimality-criteria-the-code-opens-a-sample-data-table-configures-the-doe-dialog-to-include-three-continuous-factors-sets-the-random-seed-and-number-of-starts-for-optimization-specifies-the-model-terms-and-finalizes-the-design-with-a-specified-sample-size-and-optimality-criterion)[](#generate-a-custom-response-surface-method-rsm-design-using-the-doe-platform-with-specified-factors-responses-and-optimality-criteria-the-code-opens-a-sample-data-table-configures-the-doe-dialog-to-include-three-continuous-factors-sets-the-random-seed-and-number-of-starts-for-optimization-specifies-the-model-terms-and-finalizes-the-design-with-a-specified-sample-size-and-optimality-criterion "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Custom RSM.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        Match Target, "Y", 54, 56, .
    ),
    Add Factor(
        Continuous, -1, 1, "X1", 0
    ),
    Add Factor(
        Continuous, -1, 1, "X2", 0
    ),
    Add Factor(
        Continuous, -1, 1, "X3", 0
    ), Set Random Seed( 929281409 ),
    Number of Starts( 40 ),
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
    Make Design}
);
```

### [Construct a full factorial design with categorical and continuous factors using the DOE platform](#construct-a-full-factorial-design-with-categorical-and-continuous-factors-using-the-doe-platform)[](#construct-a-full-factorial-design-with-categorical-and-continuous-factors-using-the-doe-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/DOE Example 1.jmp");
// DOE Dialog
DOE(
    Full Factorial Design,
    {
    Add Response(
        Match Target, "Depth", 0.12, 0.22,
        .
    ),
    Add Factor(
        Categorical,
        {"John", "Mary"},
        "Operator",
        0
    ),
    Add Factor(
        Continuous,
        {3, 5},
        "Speed",
        0
    ),
    Add Factor(
        Continuous,
        {150, 165},
        "Current",
        0
    ), Set Random Seed( 1344277810 ),
    Make Design}
);
```

### [Generate a Definitive Screening Design for optimizing yield based on continuous factors.](#generate-a-definitive-screening-design-for-optimizing-yield-based-on-continuous-factors)[](#generate-a-definitive-screening-design-for-optimizing-yield-based-on-continuous-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Extraction Data.jmp");
// DOE Dialog
DOE(
    Definitive Screening Design,
    {
    Add Response(
        Maximize, "Yield", ., ., .
    ),
    Add Factor(
        Continuous, 0, 10, "Methanol", 0
    ),
    Add Factor(
        Continuous, 0, 10, "Ethanol", 0
    ),
    Add Factor(
        Continuous, 0, 10, "Propanol", 0
    ),
    Add Factor(
        Continuous, 0, 10, "Butanol", 0
    ),
    Add Factor(
        Continuous, 6, 9, "pH", 0
    ),
    Add Factor(
        Continuous, 1, 2, "Time", 0
    ), Number of Extra Runs( 0 ),
    Set Random Seed( 123 ), Make Design}
);
```

### [Create a definitive screening design with multiple continuous factors and response optimization using the DOE (Design of Experiments) platform.](#create-a-definitive-screening-design-with-multiple-continuous-factors-and-response-optimization-using-the-doe-design-of-experiments-platform)[](#create-a-definitive-screening-design-with-multiple-continuous-factors-and-response-optimization-using-the-doe-design-of-experiments-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Extraction2 Data.jmp");
// DOE Dialog
DOE(
    Definitive Screening Design,
    {
    Add Response(
        Maximize, "Y", ., ., .
    ),
    Add Factor(
        Continuous, 0, 10, "Methanol", 0
    ),
    Add Factor(
        Continuous, 0, 10, "Ethanol", 0
    ),
    Add Factor(
        Continuous, 0, 10, "Propanol", 0
    ),
    Add Factor(
        Continuous, 0, 10, "Butanol", 0
    ),
    Add Factor(
        Continuous, 6, 9, "pH", 0
    ),
    Add Factor(
        Continuous, 1, 2, "Time", 0
    ), Number of Extra Runs( 0 ),
    Show Blocking Options( 1, 2 ),
    Make Design}
);
```

### [Create a definitive screening design with multiple continuous factors and an extra set of runs for the DOE platform.](#create-a-definitive-screening-design-with-multiple-continuous-factors-and-an-extra-set-of-runs-for-the-doe-platform)[](#create-a-definitive-screening-design-with-multiple-continuous-factors-and-an-extra-set-of-runs-for-the-doe-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Extraction3 Data.jmp");
// DOE Dialog
DOE(
    Definitive Screening Design,
    {
    Add Response(
        Maximize, "Yield", ., ., .
    ),
    Add Factor(
        Continuous, 0, 10, "Methanol", 0
    ),
    Add Factor(
        Continuous, 0, 10, "Ethanol", 0
    ),
    Add Factor(
        Continuous, 0, 10, "Propanol", 0
    ),
    Add Factor(
        Continuous, 0, 10, "Butanol", 0
    ),
    Add Factor(
        Continuous, 6, 9, "pH", 0
    ),
    Add Factor(
        Continuous, 1, 2, "Time", 0
    ), Show Blocking Options( 1, 2 ),
    Number of Extra Runs( 4 ),
    Set Random Seed( 123 ), Make Design}
);
```

### [Create a custom design of experiments (DOE) with a generalized linear model response function.](#create-a-custom-design-of-experiments-doe-with-a-generalized-linear-model-response-function)[](#create-a-custom-design-of-experiments-doe-with-a-generalized-linear-model-response-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Metacrate Limit Of Detection DOE.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        Maximize, "Metacrate", ., ., ., 1,
        99
    ),
    Add Factor(
        Continuous, 110, 150,
        "Dichloromethane", 0
    ),
    Add Factor(
        Continuous, 400, 600, "Methanol",
        0
    ),
    Add Factor(
        Continuous, 3, 7, "Sample Volume",
        0
    ), Set Random Seed( 981216 ),
    Number of Starts( 6776 ),
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
    Set Sample Size( 32 ),
    Optimality Criterion(
        "Make I-Optimal Design"
    ), Simulate Responses( 0 ),
    Save X Matrix( 0 ), Make Design}
);
```

### [Generate a Definitive Screening Design for optimizing the Solids response in a peanut processing experiment using continuous and categorical factors.](#generate-a-definitive-screening-design-for-optimizing-the-solids-response-in-a-peanut-processing-experiment-using-continuous-and-categorical-factors)[](#generate-a-definitive-screening-design-for-optimizing-the-solids-response-in-a-peanut-processing-experiment-using-continuous-and-categorical-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Peanut Data.jmp");
// DOE Dialog
DOE(
    Definitive Screening Design,
    {
    Add Response(
        Maximize, "Solids", ., ., .
    ),
    Add Factor(
        Continuous, -1, 1, "pH", 0
    ),
    Add Factor(
        Continuous, -1, 1, "Water Temp",
        0
    ),
    Add Factor(
        Continuous, -1, 1,
        "Extraction TIme", 0
    ),
    Add Factor(
        Continuous, -1, 1, "Ratio", 0
    ),
    Add Factor(
        Continuous, -1, 1,
        "Agitation Speed", 0
    ),
    Add Factor(
        Categorical,
        {"L1", "L2"},
        "Hydrolyze",
        0
    ),
    Add Factor(
        Categorical,
        {"L1", "L2"},
        "Pre-Soak",
        0
    ), Show Blocking Options( 0, 0 ),
    Number of Extra Runs( 4 ),
    Set Random Seed( 12345 ), Make Design,
    Simulate Responses( 0 ),
    Save X Matrix( 0 )}
);
```

### [Construct a covering array using the DOE platform with specified categorical factors and constraints.](#construct-a-covering-array-using-the-doe-platform-with-specified-categorical-factors-and-constraints)[](#construct-a-covering-array-using-the-doe-platform-with-specified-categorical-factors-and-constraints "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Phone Data.jmp");
// DOE Dialog
DOE(
    Covering Array,
    {
    Add Factor(
        Categorical,
        {"USA", "UK", "Canada", "France",
        "Mexico"},
        "Market",
        0
    ),
    Add Factor(
        Categorical,
        {"ISDN", "Bus", "Coin", "Res"},
        "Near Phone",
        0
    ),
    Add Factor(
        Categorical,
        {"A", "B"},
        "Near Interface",
        0
    ),
    Add Factor(
        Categorical,
        {"ISDN", "Bus", "Coin", "Res"},
        "Far Phone",
        0
    ),
    Add Factor(
        Categorical,
        {"A", "B"},
        "Far Interface",
        0
    ), Set Strength( 2 ),
    Disallowed Combinations(
        Near Phone == "ISDN" &
        Near Interface == "A" | Far Phone
         == "ISDN" & Far Interface == "A"
         | Near Phone == "Bus" &
        Near Interface == "B" |
        Near Phone == "Res" &
        Near Interface == "B"
    ), Set Random Seed( 632 )}
);
```

### [Generate a Mixture Design using the DOE Dialog with specified constraints and settings.](#generate-a-mixture-design-using-the-doe-dialog-with-specified-constraints-and-settings)[](#generate-a-mixture-design-using-the-doe-dialog-with-specified-constraints-and-settings "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Piepel.jmp");
// DOE Dialog
DOE(
    Mixture Design,
    {
    Add Response(
        Maximize, "Y", ., ., .
    ),
    Change Factor Settings(
        1, 0.1, 0.5, "X1"
    ),
    Change Factor Settings(
        2, 0.1, 0.7, "X2"
    ),
    Change Factor Settings(
        3, 0, 0.7, "X3"
    ), Set Random Seed( 205900700 ),
    Add Constraint(
        [-85 -90 -100 -90,
        85 90 100 95,
        -0.7 0 -1 -0.4]
    ),
    Mixture Design Type(
        Extreme Vertices, 2
    )}
);
```

### [Perform custom design of experiments with categorical and continuous factors, and add various terms and constraints to optimize the response Number Popped.](#perform-custom-design-of-experiments-with-categorical-and-continuous-factors-and-add-various-terms-and-constraints-to-optimize-the-response-number-popped)[](#perform-custom-design-of-experiments-with-categorical-and-continuous-factors-and-add-various-terms-and-constraints-to-optimize-the-response-number-popped "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Popcorn DOE Results.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        "Maximize", "Number Popped", ., .,
        .
    ),
    Add Response(
        "None", "Total Kernals", ., ., .
    ),
    Add Factor(
        Categorical,
        {"Top Secret", "Wilbur"},
        "Brand",
        0
    ),
    Add Factor(
        Continuous, 3, 5, "Time", 0
    ),
    Add Factor(
        Continuous, 5, 10, "Power", 0
    ), Set Random Seed( 151747005 ),
    Number of Starts( 40 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Add Term( {1, 1}, {2, 1} ),
    Add Term( {1, 1}, {3, 1} ),
    Add Term( {2, 1}, {3, 1} ),
    Add Term( {2, 2} ),
    Add Term( {3, 2} ),
    Set Sample Size( 16 ),
    Add Constraint( [1 1 13, -1 -1 -10] ),
    Make Design}
);
```

### [Create a screening design with Plackett-Burman DOE platform and incorporate multiple continuous factors and response settings.](#create-a-screening-design-with-plackett-burman-doe-platform-and-incorporate-multiple-continuous-factors-and-response-settings)[](#create-a-screening-design-with-plackett-burman-doe-platform-and-incorporate-multiple-continuous-factors-and-response-settings "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Plackett-Burman.jmp");
// DOE Dialog
DOE(
    Screening Design,
    {
    Add Response(
        Maximize, "Percent Reacted", 90,
        100, 1
    ),
    Add Factor(
        Continuous, 10, 15, "Feed Rate",
        0
    ),
    Add Factor(
        Continuous, 1, 2, "Catalyst", 0
    ),
    Add Factor(
        Continuous, 100, 120, "Stir Rate",
        0
    ),
    Add Factor(
        Continuous, 140, 180,
        "Temperature", 0
    ),
    Add Factor(
        Continuous, 3, 6, "Concentration",
        0
    ), Set Random Seed( 34567 ),
    Make Design( 3 )}
);
```

### [Create a custom design experiment using the DOE platform with multiple continuous factors and optimization of a response variable.](#create-a-custom-design-experiment-using-the-doe-platform-with-multiple-continuous-factors-and-optimization-of-a-response-variable)[](#create-a-custom-design-experiment-using-the-doe-platform-with-multiple-continuous-factors-and-optimization-of-a-response-variable "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor 20 Custom.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        Maximize, "Percent Reacted", 90,
        99, 1
    ),
    Add Factor(
        Continuous, 10, 15, "Feed Rate",
        0
    ),
    Add Factor(
        Continuous, 1, 2, "Catalyst", 0
    ),
    Add Factor(
        Continuous, 100, 120, "Stir Rate",
        0
    ),
    Add Factor(
        Continuous, 140, 180,
        "Temperature", 0
    ),
    Add Factor(
        Continuous, 3, 6, "Concentration",
        0
    ), Set Random Seed( 2024677686 ),
    Number of Starts( 200 ),
    Add Term( {1, 0} ),
    Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Add Term( {4, 1} ),
    Add Term( {5, 1} ),
    Add Term( {1, 1}, {2, 1} ),
    Add Term( {1, 1}, {3, 1} ),
    Add Term( {1, 1}, {4, 1} ),
    Add Term( {1, 1}, {5, 1} ),
    Add Term( {2, 1}, {3, 1} ),
    Add Term( {2, 1}, {4, 1} ),
    Add Term( {2, 1}, {5, 1} ),
    Add Term( {3, 1}, {4, 1} ),
    Add Term( {3, 1}, {5, 1} ),
    Add Term( {4, 1}, {5, 1} ),
    Set Sample Size( 20 ), Make Design}
);
```

### [Create a full factorial design of experiments for optimizing reactor conditions.](#create-a-full-factorial-design-of-experiments-for-optimizing-reactor-conditions)[](#create-a-full-factorial-design-of-experiments-for-optimizing-reactor-conditions "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor 32 Runs.jmp");
// DOE Dialog
DOE(
    Full Factorial Design,
    {
    Add Response(
        Maximize, "Percent Reacted", 90,
        100, 1
    ),
    Add Factor(
        Continuous,
        {10, 15},
        "Feed Rate",
        0
    ),
    Add Factor(
        Continuous,
        {1, 2},
        "Catalyst",
        0
    ),
    Add Factor(
        Continuous,
        {100, 120},
        "Stir Rate",
        0
    ),
    Add Factor(
        Continuous,
        {140, 180},
        "Temperature",
        0
    ),
    Add Factor(
        Continuous,
        {3, 6},
        "Concentration",
        0
    ), Set Random Seed( 12345 ),
    Make Design, Make Table}
);
```

### [Title: Create a Covering Array Design of Experiments (DOE) with Four Categorical Factors: Web Browser, Operating System, RAM, and Connection Speed.](#title-create-a-covering-array-design-of-experiments-doe-with-four-categorical-factors-web-browser-operating-system-ram-and-connection-speed)[](#title-create-a-covering-array-design-of-experiments-doe-with-four-categorical-factors-web-browser-operating-system-ram-and-connection-speed "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Software Data.jmp");
// DOE Dialog
DOE(
    Covering Array,
    {
    Add Factor(
        Categorical,
        {"Safari", "IE", "Firefox",
        "Chrome", "Other"},
        "Web Browser",
        0
    ),
    Add Factor(
        Categorical,
        {"Macintosh", "Windows"},
        "Operating System",
        0
    ),
    Add Factor(
        Categorical,
        {"16 MB", "4 MB", "8 MB"},
        "RAM",
        0
    ),
    Add Factor(
        Categorical,
        {"0-1 Mbps", "1-5 Mbps",
        ">5 Mbps"},
        "Connection Speed",
        0
    ), Set Strength( 3 )}
);
```

### [Create a custom experimental design using the MIDI DOE platform, including mixture components and specified constraints.](#create-a-custom-experimental-design-using-the-midi-doe-platform-including-mixture-components-and-specified-constraints)[](#create-a-custom-experimental-design-using-the-midi-doe-platform-including-mixture-components-and-specified-constraints "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Functional Data/Formulation For Homogeneity DOE.jmp");
// DOE Dialog
DOE(
    Custom Design,
    {
    Add Response(
        Maximize, "Y", ., ., .
    ),
    Add Factor(
        Mixture, 0.26, 0.8, "Solvent", 0
    ),
    Add Factor(
        Mixture, 0.18, 0.4, "Active", 0
    ),
    Add Factor(
        Mixture, 0.02, 0.56, "Water", 0
    ), Set Random Seed( 625641159 ),
    Number of Starts( 6371 ),
    Add Constraint(
        [-1 1.4 0 0, 0 0.1 -1 0]
    ), Add Term( {1, 1} ),
    Add Term( {2, 1} ),
    Add Term( {3, 1} ),
    Add Term( {1, 1}, {2, 1} ),
    Add Term( {1, 1}, {3, 1} ),
    Add Term( {2, 1}, {3, 1} ),
    Add Term( {1, 1}, {2, 1}, {3, 1} ),
    Add Term( {1, 1}, {2, 1} ),
    Add Term( {1, 1}, {3, 1} ),
    Add Term( {2, 1}, {3, 1} ),
    Set Sample Size( 16 ),
    Simulate Responses( 0 ),
    Save X Matrix( 0 ), Make Design}
);
```

### [Design an experiment using a custom mixture design with specified factors, responses, and constraints.](#design-an-experiment-using-a-custom-mixture-design-with-specified-factors-responses-and-constraints)[](#design-an-experiment-using-a-custom-mixture-design-with-specified-factors-responses-and-constraints "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Potato Chip Responses.jmp");
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

### [Perform Response Surface Methodology (RSM) analysis for four responses using the Fit Model platform with specified effects, Standard Least Squares personality, and Profiler for scaled estimates and actual by predicted plots.](#perform-response-surface-methodology-rsm-analysis-for-four-responses-using-the-fit-model-platform-with-specified-effects-standard-least-squares-personality-and-profiler-for-scaled-estimates-and-actual-by-predicted-plots)[](#perform-response-surface-methodology-rsm-analysis-for-four-responses-using-the-fit-model-platform-with-specified-effects-standard-least-squares-personality-and-profiler-for-scaled-estimates-and-actual-by-predicted-plots "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Tiretread.jmp");
// RSM for 4 Responses
Fit Model(
    Y(
        :ABRASION, :MODULUS, :ELONG,
        :HARDNESS
    ),
    Effects(
        :SILICA & RS, :SILANE & RS,
        :SULFUR & RS, :SILICA * :SILICA,
        :SILANE * :SILICA,
        :SILANE * :SILANE,
        :SULFUR * :SILICA,
        :SULFUR * :SILANE,
        :SULFUR * :SULFUR
    ),
    Personality(
        "Standard Least Squares"
    ),
    Run(
        Profiler(
            Confidence Intervals( 1 )
        ),
        :ABRASION <<
        {Scaled Estimates( 1 ),
        Plot Actual by Predicted( 1 )},
        :MODULUS <<
        {Scaled Estimates( 1 ),
        Plot Actual by Predicted( 1 )},
        :ELONG << {Scaled Estimates( 1 ),
        Plot Actual by Predicted( 1 )},
        :HARDNESS <<
        {Scaled Estimates( 1 ),
        Plot Actual by Predicted( 1 )}
    )
);
```

### [Generate a space filling design by loading factors from a table](#generate-a-space-filling-design-by-loading-factors-from-a-table)[](#generate-a-space-filling-design-by-loading-factors-from-a-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Algorithm Factors.jmp");
// Load and Edit in Space Filling Design
DOE(
    Space Filling Design,
    Load Factors( Current Data Table() )
);
```

### [Generate a custom design by loading factors from a table](#generate-a-custom-design-by-loading-factors-from-a-table)[](#generate-a-custom-design-by-loading-factors-from-a-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Algorithm Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Use evaluate design on a mixed model design](#use-evaluate-design-on-a-mixed-model-design)[](#use-evaluate-design-on-a-mixed-model-design "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Battery Data.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Whole Plots, :Subplots, :A1, :A2,
        :A3, :A4, :C1, :C2
    )
);
```

### [Perform a screening analysis with the OCV as the response variable and A1, A2, A3, A4, C1, and C2 as the factors.](#perform-a-screening-analysis-with-the-ocv-as-the-response-variable-and-a1-a2-a3-a4-c1-and-c2-as-the-factors)[](#perform-a-screening-analysis-with-the-ocv-as-the-response-variable-and-a1-a2-a3-a4-c1-and-c2-as-the-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Battery Data.jmp");
// Screening
Screening(
    Y( :OCV ),
    X( :A1, :A2, :A3, :A4, :C1, :C2 )
);
```

### [Open and edit an existing data table in a space-filling design using the DOE function .](#open-and-edit-an-existing-data-table-in-a-space-filling-design-using-the-doe-function)[](#open-and-edit-an-existing-data-table-in-a-space-filling-design-using-the-doe-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Borehole Factors.jmp");
// Load and Edit in Space Filling Design
DOE(
    Space Filling Design,
    Load Factors( Current Data Table() )
);
```

### [Open and edit the current data table in the Custom Design platform.](#open-and-edit-the-current-data-table-in-the-custom-design-platform)[](#open-and-edit-the-current-data-table-in-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Borehole Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Evaluate the design using the DOE platform, focusing on the factors Silica, Sulfur, and Silane.](#evaluate-the-design-using-the-doe-platform-focusing-on-the-factors-silica-sulfur-and-silane)[](#evaluate-the-design-using-the-doe-platform-focusing-on-the-factors-silica-sulfur-and-silane "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Bounce Data.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X( :Silica, :Sulfur, :Silane )
);
```

### [Load existing data from a Response Surface Design experiment and edit its factors.](#load-existing-data-from-a-response-surface-design-experiment-and-edit-its-factors)[](#load-existing-data-from-a-response-surface-design-experiment-and-edit-its-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Bounce Factors.jmp");
// Load and Edit in Response Surface Design
DOE(
    Response Surface Design,
    Load Factors( Current Data Table() )
);
```

### [Load an existing data table and modify it in a custom design experiment.](#load-an-existing-data-table-and-modify-it-in-a-custom-design-experiment)[](#load-an-existing-data-table-and-modify-it-in-a-custom-design-experiment "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Bounce Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Load and Edit in Response Surface Design using DOE and Load Responses functions.](#load-and-edit-in-response-surface-design-using-doe-and-load-responses-functions)[](#load-and-edit-in-response-surface-design-using-doe-and-load-responses-functions "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Bounce Response.jmp");
// Load and Edit in Response Surface Design
DOE(
    Response Surface Design,
    Load Responses(
        Current Data Table()
    )
);
```

### [Evaluate the design of a Box Corrosion Split-Plot experiment using the DOE platform, focusing on the factors: Whole Plots, Furnace Temp, and Coating.](#evaluate-the-design-of-a-box-corrosion-split-plot-experiment-using-the-doe-platform-focusing-on-the-factors-whole-plots-furnace-temp-and-coating)[](#evaluate-the-design-of-a-box-corrosion-split-plot-experiment-using-the-doe-platform-focusing-on-the-factors-whole-plots-furnace-temp-and-coating "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Box Corrosion Split-Plot.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Whole Plots, :Furnace Temp,
        :Coating
    )
);
```

### [Evaluate the design of a cake experiment using the specified factors: Cocoa, Sugar, Flour, Butter, Milk, and Eggs.](#evaluate-the-design-of-a-cake-experiment-using-the-specified-factors-cocoa-sugar-flour-butter-milk-and-eggs)[](#evaluate-the-design-of-a-cake-experiment-using-the-specified-factors-cocoa-sugar-flour-butter-milk-and-eggs "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Cake Data.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Cocoa, :Sugar, :Flour, :Butter,
        :Milk, :Eggs
    )
);
```

### [Apply linear constraints to regression analysis. Use the Fit Model function to create a linear regression model with constraints on the coefficients of the predictors.](#apply-linear-constraints-to-regression-analysis-use-the-fit-model-function-to-create-a-linear-regression-model-with-constraints-on-the-coefficients-of-the-predictors)[](#apply-linear-constraints-to-regression-analysis-use-the-fit-model-function-to-create-a-linear-regression-model-with-constraints-on-the-coefficients-of-the-predictors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Cake Data.jmp");
// Constraint
{1 * :Cocoa + 1 * :Sugar + 1 * :Flour <=
0.45, -1 * :Cocoa + -1 * :Sugar + -1 *
:Flour <= -0.45};
```

### [Perform MaxDiff analysis using a Firth bias-adjusted logistic regression model to analyze multiple-choice data with profile effects.](#perform-maxdiff-analysis-using-a-firth-bias-adjusted-logistic-regression-model-to-analyze-multiple-choice-data-with-profile-effects)[](#perform-maxdiff-analysis-using-a-firth-bias-adjusted-logistic-regression-model-to-analyze-multiple-choice-data-with-profile-effects "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Candy Survey.jmp");
// MaxDiff
MaxDiff(
    One Table( 1 ),
    Response Subject ID( :Subject ),
    Profile ID( :Choice ),
    Profile Grouping(
        :Subject, :Choice Set
    ),
    Profile Effects( :Candy ),
    "Firth Bias-adjusted Estimates"n( 1 )
);
```

### [Generate a MaxDiff Design for a Candy Survey using the DOE Dialog function.](#generate-a-maxdiff-design-for-a-candy-survey-using-the-doe-dialog-function)[](#generate-a-maxdiff-design-for-a-candy-survey-using-the-doe-dialog-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Candy Survey.jmp");
// DOE Dialog
DOE(
    MaxDiff Design,
    X( :Candy ),
    {Set Number of Profiles( 4 ),
    Set Number of Choice Sets( 7 ),
    Make Design, Simulate Responses( 0 )}
);
```

### [Evaluate the design of an experiment involving temperature, time, and catalyst in a DOE platform using Whole Plots and Subplots.](#evaluate-the-design-of-an-experiment-involving-temperature-time-and-catalyst-in-a-doe-platform-using-whole-plots-and-subplots)[](#evaluate-the-design-of-an-experiment-involving-temperature-time-and-catalyst-in-a-doe-platform-using-whole-plots-and-subplots "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Catalyst Design.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        Whole Plots, Subplots,
        :Temperature, :Time, :Catalyst
    )
);
```

### [Perform data loading and editing operations within the Custom Design platform.](#perform-data-loading-and-editing-operations-within-the-custom-design-platform)[](#perform-data-loading-and-editing-operations-within-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Cheese Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Load and edit design factors in the Choice Design platform.](#load-and-edit-design-factors-in-the-choice-design-platform)[](#load-and-edit-design-factors-in-the-choice-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Coffee Choice Factors.jmp");
// Load and Edit in Choice Design
DOE(
    Choice Design,
    Load Factors( Current Data Table() )
);
```

### [Load and edit an existing dataset in the Custom Design platform.](#load-and-edit-an-existing-dataset-in-the-custom-design-platform)[](#load-and-edit-an-existing-dataset-in-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Coffee Choice Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Load data table Coffee Factors and open Custom Design window pre-populated with factors from the current data table.](#load-data-table-coffee-factors-and-open-custom-design-window-pre-populated-with-factors-from-the-current-data-table)[](#load-data-table-coffee-factors-and-open-custom-design-window-pre-populated-with-factors-from-the-current-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Coffee Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Evaluate the design of an experiment using the specified factors in DOE platform.](#evaluate-the-design-of-an-experiment-using-the-specified-factors-in-doe-platform)[](#evaluate-the-design-of-an-experiment-using-the-specified-factors-in-doe-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Custom RSM.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X( :X1, :X2, :X3 )
);
```

### [Perform screening analysis on the response variable Y using predictors X1, X2, and X3 from a specific dataset.](#perform-screening-analysis-on-the-response-variable-y-using-predictors-x1-x2-and-x3-from-a-specific-dataset)[](#perform-screening-analysis-on-the-response-variable-y-using-predictors-x1-x2-and-x3-from-a-specific-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Custom RSM.jmp");
// Screening
Screening( Y( :Y ), X( :X1, :X2, :X3 ) );
```

### [Evaluate the design of an experiment using the DOE platform with the specified factors.](#evaluate-the-design-of-an-experiment-using-the-doe-platform-with-the-specified-factors)[](#evaluate-the-design-of-an-experiment-using-the-doe-platform-with-the-specified-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/DOE Example 1.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X( :Operator, :Speed, :Current )
);
```

### [Perform Two-Level Screening Analysis on Design Experiment Data Using the Fit Two Level Screening Function](#perform-two-level-screening-analysis-on-design-experiment-data-using-the-fit-two-level-screening-function)[](#perform-two-level-screening-analysis-on-design-experiment-data-using-the-fit-two-level-screening-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/DOE Example 1.jmp");
// Screening
Fit Two Level Screening(
    Y( :Depth ),
    X( :Operator, :Speed, :Current )
);
```

### [Fit a Definitive Screening model to analyze the effects of six process variables on yield.](#fit-a-definitive-screening-model-to-analyze-the-effects-of-six-process-variables-on-yield)[](#fit-a-definitive-screening-model-to-analyze-the-effects-of-six-process-variables-on-yield "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Extraction Data.jmp");
// Fit Definitive Screening
Fit Definitive Screening(
    X(
        :Methanol, :Ethanol, :Propanol,
        :Butanol, :pH, :Time
    ),
    Y( :Yield )
);
```

### [Evaluate the design of an experiment focusing on the response variables associated with Methanol, Ethanol, Propanol, Butanol, pH, and Time.](#evaluate-the-design-of-an-experiment-focusing-on-the-response-variables-associated-with-methanol-ethanol-propanol-butanol-ph-and-time)[](#evaluate-the-design-of-an-experiment-focusing-on-the-response-variables-associated-with-methanol-ethanol-propanol-butanol-ph-and-time "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Extraction Data.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Methanol, :Ethanol, :Propanol,
        :Butanol, :pH, :Time
    )
);
```

### [Load and edit data in the Definitive Screening Design platform using the current data table.](#load-and-edit-data-in-the-definitive-screening-design-platform-using-the-current-data-table)[](#load-and-edit-data-in-the-definitive-screening-design-platform-using-the-current-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Extraction Factors.jmp");
// Load and Edit in Definitive Screening Design
DOE(
    Definitive Screening Design,
    Load Factors( Current Data Table() )
);
```

### [Load an existing data table from the sample data folder into the Custom Design platform for further experimentation and analysis using DOE and Load Factors functions.](#load-an-existing-data-table-from-the-sample-data-folder-into-the-custom-design-platform-for-further-experimentation-and-analysis-using-doe-and-load-factors-functions)[](#load-an-existing-data-table-from-the-sample-data-folder-into-the-custom-design-platform-for-further-experimentation-and-analysis-using-doe-and-load-factors-functions "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Extraction Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Evaluate the experimental design by assessing the selected factors for optimization.](#evaluate-the-experimental-design-by-assessing-the-selected-factors-for-optimization)[](#evaluate-the-experimental-design-by-assessing-the-selected-factors-for-optimization "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Extraction2 Data.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Lot, :Methanol, :Ethanol,
        :Propanol, :Butanol, :pH, :Time
    )
);
```

### [Evaluate the experimental design for the Extraction3 Data using the Design of Experiments (DOE) platform with the specified factors.](#evaluate-the-experimental-design-for-the-extraction3-data-using-the-design-of-experiments-doe-platform-with-the-specified-factors)[](#evaluate-the-experimental-design-for-the-extraction3-data-using-the-design-of-experiments-doe-platform-with-the-specified-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Extraction3 Data.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Lot, :Methanol, :Ethanol,
        :Propanol, :Butanol, :pH, :Time
    )
);
```

### [Load data from a specified file and open it in the Choice Design platform.](#load-data-from-a-specified-file-and-open-it-in-the-choice-design-platform)[](#load-data-from-a-specified-file-and-open-it-in-the-choice-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Laptop Factors.jmp");
// Load and Edit in Choice Design
DOE(
    Choice Design,
    Load Factors( Current Data Table() )
);
```

### [Evaluate the design of the experiment using the Dichloromethane, Methanol, and Sample Volume factors in the DOE platform.](#evaluate-the-design-of-the-experiment-using-the-dichloromethane-methanol-and-sample-volume-factors-in-the-doe-platform)[](#evaluate-the-design-of-the-experiment-using-the-dichloromethane-methanol-and-sample-volume-factors-in-the-doe-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Metacrate Limit Of Detection DOE.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Dichloromethane, :Methanol,
        :Sample Volume
    )
);
```

### [Evaluate the design using the variables pH, Water Temp, Extraction Time, Ratio, Agitation Speed, Hydrolyze, and Pre-Soak.](#evaluate-the-design-using-the-variables-ph-water-temp-extraction-time-ratio-agitation-speed-hydrolyze-and-pre-soak)[](#evaluate-the-design-using-the-variables-ph-water-temp-extraction-time-ratio-agitation-speed-hydrolyze-and-pre-soak "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Peanut Data.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :pH, :Water Temp,
        :Extraction TIme, :Ratio,
        :Agitation Speed, :Hydrolyze,
        :"Pre-Soak"n
    )
);
```

### [Load and edit a Definitive Screening Design from an existing data table.](#load-and-edit-a-definitive-screening-design-from-an-existing-data-table)[](#load-and-edit-a-definitive-screening-design-from-an-existing-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Peanut Factors.jmp");
// Load and Edit in Definitive Screening Design
DOE(
    Definitive Screening Design,
    Load Factors( Current Data Table() )
);
```

### [Load a data table and edit it using the Custom Design platform .](#load-a-data-table-and-edit-it-using-the-custom-design-platform)[](#load-a-data-table-and-edit-it-using-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Peanut Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Identify and filter out disallowed combinations in data table by specifying conditions on categorical variables . The script uses the Open and Data Filter functions to accomplish this task.](#identify-and-filter-out-disallowed-combinations-in-data-table-by-specifying-conditions-on-categorical-variables-the-script-uses-the-open-and-data-filter-functions-to-accomplish-this-task)[](#identify-and-filter-out-disallowed-combinations-in-data-table-by-specifying-conditions-on-categorical-variables-the-script-uses-the-open-and-data-filter-functions-to-accomplish-this-task "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Phone Data.jmp");
// Disallowed Combinations
Near Phone == "ISDN" & Near Interface ==
"A" | Far Phone == "ISDN" & Far Interface
 == "A" | Near Phone == "Bus" &
Near Interface == "B" | Near Phone ==
"Res" & Near Interface == "B";
```

### [Load and edit experimental factors in a Covering Array design.](#load-and-edit-experimental-factors-in-a-covering-array-design)[](#load-and-edit-experimental-factors-in-a-covering-array-design "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Phone Factors.jmp");
// Load and Edit in Covering Array
DOE(
    Covering Array,
    Load Factors( Current Data Table() )
);
```

### [Load a factor experiment data table and edit it in the Custom Design platform.](#load-a-factor-experiment-data-table-and-edit-it-in-the-custom-design-platform)[](#load-a-factor-experiment-data-table-and-edit-it-in-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Phone Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Apply linear constraints to a dataset.](#apply-linear-constraints-to-a-dataset)[](#apply-linear-constraints-to-a-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Piepel.jmp");
// Constraint
{-85 * :X1 + -90 * :X2 + -100 * :X3 - (
-90), 85 * :X1 + 90 * :X2 + 100 * :X3
-95, -0.7 * :X1 + -1 * :X3 - (-0.4)};
```

### [Perform screening analysis using the Screening function to identify significant factors affecting the Percent Reacted.](#perform-screening-analysis-using-the-screening-function-to-identify-significant-factors-affecting-the-percent-reacted)[](#perform-screening-analysis-using-the-screening-function-to-identify-significant-factors-affecting-the-percent-reacted "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Plackett-Burman.jmp");
// Screening
Screening(
    Y( :Percent Reacted ),
    X(
        :Feed Rate, :Catalyst, :Stir Rate,
        :Temperature, :Concentration
    )
);
```

### [Evaluate Design: Assess experimental factors in a Plackett-Burman design using the DOE platform.](#evaluate-design-assess-experimental-factors-in-a-plackett-burman-design-using-the-doe-platform)[](#evaluate-design-assess-experimental-factors-in-a-plackett-burman-design-using-the-doe-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Plackett-Burman.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Feed Rate, :Catalyst, :Stir Rate,
        :Temperature, :Concentration
    )
);
```

### [Load sample data from the Plastifactors dataset and apply the mixture design to the current data table using the DOE platform.](#load-sample-data-from-the-plastifactors-dataset-and-apply-the-mixture-design-to-the-current-data-table-using-the-doe-platform)[](#load-sample-data-from-the-plastifactors-dataset-and-apply-the-mixture-design-to-the-current-data-table-using-the-doe-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Plastifactors.jmp");
// Load and Edit in Mixture Design
DOE(
    Mixture Design,
    Load Factors( Current Data Table() )
);
```

### [Load an existing data table and edit it within the Custom Design platform .](#load-an-existing-data-table-and-edit-it-within-the-custom-design-platform)[](#load-an-existing-data-table-and-edit-it-within-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Plastifactors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Perform a screening analysis for the response variables 'Number Popped' and 'Total Kernels' against the predictor variables 'Brand', 'Time', and 'Power'.](#perform-a-screening-analysis-for-the-response-variables-number-popped-and-total-kernels-against-the-predictor-variables-brand-time-and-power)[](#perform-a-screening-analysis-for-the-response-variables-number-popped-and-total-kernels-against-the-predictor-variables-brand-time-and-power "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Popcorn DOE Results.jmp");
// Screening
Screening(
    Y( :Number Popped, :Total Kernels ),
    X( :Brand, :Time, :Power )
);
```

### [Apply constraints to the factors in a DOE analysis.](#apply-constraints-to-the-factors-in-a-doe-analysis)[](#apply-constraints-to-the-factors-in-a-doe-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Popcorn DOE Results.jmp");
// Constraint
{1 * :Time + 1 * :Power <= 13, 1 * :Time
 + 1 * :Power >= 10};
```

### [Perform a screening analysis with Percent Reacted as the response variable and Feed Rate, Catalyst, Stir Rate, Temperature, and Concentration as the explanatory variables.](#perform-a-screening-analysis-with-percent-reacted-as-the-response-variable-and-feed-rate-catalyst-stir-rate-temperature-and-concentration-as-the-explanatory-variables)[](#perform-a-screening-analysis-with-percent-reacted-as-the-response-variable-and-feed-rate-catalyst-stir-rate-temperature-and-concentration-as-the-explanatory-variables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor 20 Custom.jmp");
// Screening
Screening(
    Y( :Percent Reacted ),
    X(
        :Feed Rate, :Catalyst, :Stir Rate,
        :Temperature, :Concentration
    )
);
```

### [Perform a two-level screening analysis on a design experiment data table using the Fit Two Level Screening function.](#perform-a-two-level-screening-analysis-on-a-design-experiment-data-table-using-the-fit-two-level-screening-function)[](#perform-a-two-level-screening-analysis-on-a-design-experiment-data-table-using-the-fit-two-level-screening-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor 8 Runs.jmp");
// Screening
Fit Two Level Screening(
    Y( :Percent Reacted ),
    X(
        :Feed Rate, :Catalyst, :Stir Rate,
        :Temperature, :Concentration
    )
);
```

### [Evaluate the Design of a Reactor Experiment Using DOE Function](#evaluate-the-design-of-a-reactor-experiment-using-doe-function)[](#evaluate-the-design-of-a-reactor-experiment-using-doe-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor 32 Runs.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Feed Rate, :Catalyst, :Stir Rate,
        :Temperature, :Concentration
    )
);
```

### [Perform two-level screening analysis on a reactor experiment dataset to identify significant factors affecting percent reacted](#perform-two-level-screening-analysis-on-a-reactor-experiment-dataset-to-identify-significant-factors-affecting-percent-reacted)[](#perform-two-level-screening-analysis-on-a-reactor-experiment-dataset-to-identify-significant-factors-affecting-percent-reacted "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor 32 Runs.jmp");
// Screening
Fit Two Level Screening(
    Y( :Percent Reacted ),
    X(
        :Feed Rate, :Catalyst, :Stir Rate,
        :Temperature, :Concentration
    )
);
```

### [Evaluate the statistical properties of a designed experiment using the Evaluate Design function in the DOE platform.](#evaluate-the-statistical-properties-of-a-designed-experiment-using-the-evaluate-design-function-in-the-doe-platform)[](#evaluate-the-statistical-properties-of-a-designed-experiment-using-the-evaluate-design-function-in-the-doe-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor 8 Runs.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Feed Rate, :Catalyst, :Stir Rate,
        :Temperature, :Concentration
    )
);
```

### [Evaluate the design of an experiment with multiple factors in DOE (Design of Experiments) platform.](#evaluate-the-design-of-an-experiment-with-multiple-factors-in-doe-design-of-experiments-platform)[](#evaluate-the-design-of-an-experiment-with-multiple-factors-in-doe-design-of-experiments-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor Augment Data.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X(
        :Feed Rate, :Catalyst, :Stir Rate,
        :Temperature, :Concentration
    )
);
```

### [Load and Edit a Screening Design using current data table.](#load-and-edit-a-screening-design-using-current-data-table)[](#load-and-edit-a-screening-design-using-current-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor Factors.jmp");
// Load and Edit in Screening Design
DOE(
    Screening Design,
    Load Factors( Current Data Table() )
);
```

### [Open and edit the existing factors in a custom design from the specified data table.](#open-and-edit-the-existing-factors-in-a-custom-design-from-the-specified-data-table)[](#open-and-edit-the-existing-factors-in-a-custom-design-from-the-specified-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Load and edit data in a screening design using DOE and Load Responses functions.](#load-and-edit-data-in-a-screening-design-using-doe-and-load-responses-functions)[](#load-and-edit-data-in-a-screening-design-using-doe-and-load-responses-functions "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor Response.jmp");
// Load and Edit in Screening Design
DOE(
    Screening Design,
    Load Responses(
        Current Data Table()
    )
);
```

### [Load and Edit Responses in a Custom Design Experiment](#load-and-edit-responses-in-a-custom-design-experiment)[](#load-and-edit-responses-in-a-custom-design-experiment "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Reactor Response.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Responses(
        Current Data Table()
    )
);
```

### [Load factors from an existing data table and edit them in the Covering Array platform.](#load-factors-from-an-existing-data-table-and-edit-them-in-the-covering-array-platform)[](#load-factors-from-an-existing-data-table-and-edit-them-in-the-covering-array-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Software Factors.jmp");
// Load and Edit in Covering Array
DOE(
    Covering Array,
    Load Factors( Current Data Table() )
);
```

### [Load data from the Vinyl Factors file and edit it in the Custom Design platform.](#load-data-from-the-vinyl-factors-file-and-edit-it-in-the-custom-design-platform)[](#load-data-from-the-vinyl-factors-file-and-edit-it-in-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Vinyl Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Load and edit an existing response data table in the Custom Design platform.](#load-and-edit-an-existing-response-data-table-in-the-custom-design-platform)[](#load-and-edit-an-existing-response-data-table-in-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Vinyl Responses.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Responses(
        Current Data Table()
    )
);
```

### [Load data table and Edit in Screening Design using Load Factors function.](#load-data-table-and-edit-in-screening-design-using-load-factors-function)[](#load-data-table-and-edit-in-screening-design-using-load-factors-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Weld Factors.jmp");
// Load and Edit in Screening Design
DOE(
    Screening Design,
    Load Factors( Current Data Table() )
);
```

### [Load data from the Weld Factors sample dataset and edit the design experiment using the Custom Design platform.](#load-data-from-the-weld-factors-sample-dataset-and-edit-the-design-experiment-using-the-custom-design-platform)[](#load-data-from-the-weld-factors-sample-dataset-and-edit-the-design-experiment-using-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Weld Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Load factors from a specified data table and edit them in the Custom Design platform.](#load-factors-from-a-specified-data-table-and-edit-them-in-the-custom-design-platform)[](#load-factors-from-a-specified-data-table-and-edit-them-in-the-custom-design-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Wine Factors.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Factors( Current Data Table() )
);
```

### [Apply constraint to ensure positive levels of active ingredient and sufficient water relative to solvent in formulation.](#apply-constraint-to-ensure-positive-levels-of-active-ingredient-and-sufficient-water-relative-to-solvent-in-formulation)[](#apply-constraint-to-ensure-positive-levels-of-active-ingredient-and-sufficient-water-relative-to-solvent-in-formulation "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Functional Data/Formulation For Homogeneity DOE.jmp");
// Constraint
{1 * :Solvent + -1.4 * :Active >= 0, -0.1
 * :Active + 1 * :Water >= 0};
```

### [Evaluate the experimental design with the variables Solvent, Active, and Water.](#evaluate-the-experimental-design-with-the-variables-solvent-active-and-water)[](#evaluate-the-experimental-design-with-the-variables-solvent-active-and-water "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Functional Data/Formulation For Homogeneity DOE.jmp");
// Evaluate Design
DOE(
    Evaluate Design,
    X( :Solvent, :Active, :Water )
);
```

### [Perform variable screening using the Screening platform on a dataset containing 18 predictors and one response variable.](#perform-variable-screening-using-the-screening-platform-on-a-dataset-containing-18-predictors-and-one-response-variable)[](#perform-variable-screening-using-the-screening-platform-on-a-dataset-containing-18-predictors-and-one-response-variable "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Supersaturated.jmp");
// Screening
Screening(
    Y( :Y ),
    X(
        :X1, :X2, :X3, :X4, :X5, :X6, :X7,
        :X8, :X9, :X10, :X11, :X12, :X13,
        :X14, :X15, :X16, :X17, :X18
    )
);
```

[ Previous](Control%20Charts.html "Control Charts") [Next ](Data%20Table.html "Data Table")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
