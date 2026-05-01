# Text Analysis

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Text%20Analysis.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Text%20Analysis.html)*

---

# [Text Analysis](#text-analysis)[](#text-analysis "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Conduct Latent Semantic Analysis (LSA) on the Reported Term for the Adverse Event column and identify key terms related to intracranial pressure, hepatic function, and urinary tract infection using the Text Explorer platform.](#conduct-latent-semantic-analysis-lsa-on-the-reported-term-for-the-adverse-event-column-and-identify-key-terms-related-to-intracranial-pressure-hepatic-function-and-urinary-tract-infection-using-the-text-explorer-platform)[](#conduct-latent-semantic-analysis-lsa-on-the-reported-term-for-the-adverse-event-column-and-identify-key-terms-related-to-intracranial-pressure-hepatic-function-and-urinary-tract-infection-using-the-text-explorer-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Nicardipine.jmp");
// Text Explorer: Adverse Event
_te =
Text Explorer(
    Text Columns(
        :
        Reported Term for the Adverse Event
    ),
    Tokenizing( "Basic Words" ),
    Latent Semantic Analysis(
        1,
        Maximum Number of Terms( 92 ),
        Minimum Term Frequency( 10 ),
        Weighting( "TF IDF" ),
        Number of Singular Vectors( 5 ),
        Centering and Scaling(
            "Centered and Scaled"
        )
    )
);
_lst = Report( _te )[
"Term and Phrase Lists"][
String Col Box( 1 )] << get;
_rowvec =
Contains( _lst, "intracranial" ) |/
Contains( _lst, "pressure" ) |/
Contains( _lst, "increased" ) |/
Contains( _lst, "hepatic" ) |/
Contains( _lst, "function" ) |/
Contains( _lst, "abnormal" ) |/
Contains( _lst, "urinary" ) |/
Contains( _lst, "tract" ) |/
Contains( _lst, "infection" );
Report( _te )["Term and Phrase Lists"][
String Col Box( 1 )] <<
set selected rows( _rowvec );
```

### [Perform Latent Semantic Analysis and generate SVD plots for text exploration in the Pet Survey dataset.](#perform-latent-semantic-analysis-and-generate-svd-plots-for-text-exploration-in-the-pet-survey-dataset)[](#perform-latent-semantic-analysis-and-generate-svd-plots-for-text-exploration-in-the-pet-survey-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Pet Survey.jmp");
// Text Explorer with SVD Plots
Text Explorer(
    Text Columns( :Survey Response ),
    Set Regex( Library( "Words" ) ),
    Latent Semantic Analysis(
        1,
        Maximum Number of Terms( 143 ),
        Minimum Term Frequency( 2 ),
        Weighting( "TF IDF" ),
        Number of Singular Vectors( 100 ),
        Centering and Scaling(
            "Centered and Scaled"
        )
    )
);
```

[ Previous](Statistical%20Analysis.html "Statistical Analysis") [Next ](Time%20Series.html "Time Series")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
