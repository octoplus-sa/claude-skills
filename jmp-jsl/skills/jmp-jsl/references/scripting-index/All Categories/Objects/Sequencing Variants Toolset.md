# Sequencing Variants Toolset

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Sequencing%20Variants%20Toolset.html](https://jsl.jmp.com/All%20Categories/Objects/Sequencing%20Variants%20Toolset.html)*

---

# [Sequencing Variants Toolset](#sequencing-variants-toolset)[](#sequencing-variants-toolset "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Sequencing Variants Toolset](#sequencing-variants-toolset_1)[](#sequencing-variants-toolset_1 "Click to copy url")

**Syntax:** Sequencing Variants Toolset

**Description:** Provides a framework to process and analyze high-throughput sequencing data with SamTools and BcfTools.

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Arguments](#arguments)[](#arguments "Click to copy url")

**Syntax:** obj \<\< Arguments

**Description:** Enables specification of options to run the platform from the scripting window.

### [Run Cmd](#run-cmd)[](#run-cmd "Click to copy url")

**Syntax:** obj \<\< Run Cmd

**Description:** Determines the sequencing variants toolset task to be run from the scripting window.

### [Run Spec](#run-spec)[](#run-spec "Click to copy url")

**Syntax:** obj \<\< Run Spec

**Description:** Determines the sequencing variants toolset task to be run from the interface window.

### [Specification](#specification)[](#specification "Click to copy url")

**Syntax:** obj \<\< Specification

**Description:** Enables specification of a task.

## [Shared Item Messages](#shared-item-messages)[](#shared-item-messages "Click to copy url")

### [Action](#action)[](#action "Click to copy url")

**Syntax:** obj \<\< Action

**Description:** All-purpose trapdoor within a platform to insert expressions to evaluate. Temporarily sets the DisplayBox and DataTable contexts to the Platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Bivariate(
    Y( :height ),
    X( :weight ),
    Action( Distribution( Y( :height, :weight ), Histograms Only ) )
);
```

### [Apply Preset](#apply-preset)[](#apply-preset "Click to copy url")

**Syntax:** Apply Preset( preset ); Apply Preset( source, label, \<Folder( folder {, folder2, ...} )\> )

**Description:** Apply a previously created preset to the object, updating the options and customizations to match the saved settings.

**JMP Version Added:** 18

#### [Anonymous preset](#anonymous-preset)[](#anonymous-preset "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
dt2 = Open( "$SAMPLE_DATA/Dogs.jmp" );
obj2 = dt2 << Oneway( Y( :LogHist0 ), X( :drug ) );
Wait( 1 );
obj2 << Apply Preset( preset );
```

#### [Search by name](#search-by-name)[](#search-by-name "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "Compare Distributions" );
```

#### [Search within folder(s)](#search-within-folders)[](#search-within-folders "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "t-Tests", Folder( "Compare Means" ) );
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
obj << Copy Script;
```

### [Get By Levels](#get-by-levels)[](#get-by-levels "Click to copy url")

**Syntax:** obj \<\< Get By Levels

**Description:** Returns an associative array mapping the by group columns to their values.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv << Get By Levels;
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
t = obj << Get Container;
Show( (t << XPath( "//OutlineBox" )) << Get Title );
```

#### [Platform with Filter](#platform-with-filter)[](#platform-with-filter "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) ),
    Local Data Filter(
        Add Filter(
            columns( :age, :sex, :height ),
            Where( :age == {12, 13, 14} ),
            Where( :sex == "F" ),
            Where( :height >= 55 ),
            Display( :age, N Items( 6 ) )
        )
    )
);
New Window( "platform boxes",
    H List Box(
        Outline Box( "Report(platform)", Report( gb ) << Get Picture ),
        Outline Box( "platform << Get Container", (gb << Get Container) << Get Picture )
    )
);
```

### [Get Data Table](#get-data-table)[](#get-data-table "Click to copy url")

**Syntax:** obj \<\< Get Data Table

**Description:** Returns a reference to the data table.

``` jsl
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
t = obj << Get Timing;
Show( t );
```

### [Get Web Support](#get-web-support)[](#get-web-support "Click to copy url")

**Syntax:** obj \<\< Get Web Support

**Description:** Return a number indicating the level of Interactive HTML support for the display object. 1 means some or all elements are supported. 0 means no support.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
s = obj << Get Web Support();
Show( s );
```

### [Get Where Expr](#get-where-expr)[](#get-where-expr "Click to copy url")

**Syntax:** obj \<\< Get Where Expr

**Description:** Returns the Where expression for the data subset, if the platform was launched with By() or Where(). Otherwise, returns Empty()

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv2 = dt << Bivariate( X( :height ), Y( :weight ), Where( :age < 14 & :height > 60 ) );
Show( biv[1] << Get Where Expr, biv2 << Get Where Expr );
```

### [Ignore Platform Preferences](#ignore-platform-preferences)[](#ignore-platform-preferences "Click to copy url")

**Syntax:** Ignore Platform Preferences( state=0\|1 )

**Description:** Ignores the current settings of the platform's preferences. The message is ignored when sent to the platform after creation.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Bivariate(
    Ignore Platform Preferences( 1 ),
    Y( :height ),
    X( :weight ),
    Action( Distribution( Y( :height, :weight ), Histograms Only ) )
);
```

### [New Preset](#new-preset)[](#new-preset "Click to copy url")

**Syntax:** obj = New Preset()

**Description:** Create an anonymous preset representing the options and customizations applied to the object. This object can be passed to Apply Preset to copy the settings to another object of the same type.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
```

### [Report](#report)[](#report "Click to copy url")

**Syntax:** obj \<\< Report; Report( obj )

**Description:** Returns a reference to the report object.

``` jsl
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
obj << Save Script to Script Window;
```

### [SendToByGroup](#sendtobygroup)[](#sendtobygroup "Click to copy url")

**Syntax:** SendToByGroup( {":Column == level"}, command );

**Description:** Sends platform commands or display customization commands to each level of a by-group.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Distribution(
    By( :Sex ),
    SendToByGroup(
        {:sex == "F"},
        Continuous Distribution( Column( :weight ), Normal Quantile Plot( 1 ) )
    ),
    SendToByGroup( {:sex == "M"}, Continuous Distribution( Column( :weight ) ) )
);
```

### [SendToEmbeddedScriptable](#sendtoembeddedscriptable)[](#sendtoembeddedscriptable "Click to copy url")

**Syntax:** SendToEmbeddedScriptable( Dispatch( "Outline name", "Element name", command );

**Description:** SendToEmbeddedScriptable restores settings of embedded scriptable objects.

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    Censor Code( 1 ),
    <<Fit Weibull,
    SendToEmbeddedScriptable(
        Dispatch(
            {"Statistics", "Parametric Estimate - Weibull", "Profilers", "Density Profiler"},
            {1, Confidence Intervals( 0 ), Term Value( Time( 6000, Lock( 0 ), Show( 1 ) ) )}
        )
    )
);
```

### [SendToReport](#sendtoreport)[](#sendtoreport "Click to copy url")

**Syntax:** SendToReport( Dispatch( "Outline name", "Element name", Element type, command );

**Description:** Send To Report is used in tandem with the Dispatch command to customize the appearance of a report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Distribution(
    Nominal Distribution( Column( :age ) ),
    Continuous Distribution( Column( :weight ) ),
    SendToReport( Dispatch( "age", "Distrib Nom Hist", FrameBox, {Frame Size( 178, 318 )} ) )
);
```

### [Title](#title)[](#title "Click to copy url")

**Syntax:** obj \<\< Title( "new title" )

**Description:** Sets the title of the platform.

``` jsl
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
r = obj << Top Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [View Web XML](#view-web-xml)[](#view-web-xml "Click to copy url")

**Syntax:** obj \<\< View Web XML

**Description:** Returns the XML code that is used to create the interactive HTML report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
xml = obj << View Web XML;
```

## [Sequencing Variants Toolset Run](#sequencing-variants-toolset-run)[](#sequencing-variants-toolset-run "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Auto Send Output to Files List](#auto-send-output-to-files-list)[](#auto-send-output-to-files-list "Click to copy url")

**Syntax:** obj \<\< Auto Send Output to Files List( state=0\|1 )

**Description:** Sends output files to the files list panel.

#### [Bam Files](#bam-files)[](#bam-files "Click to copy url")

**Syntax:** obj \<\< Bam Files

**Description:** Specifies BAM files.

#### [Bcf Files](#bcf-files)[](#bcf-files "Click to copy url")

**Syntax:** obj \<\< Bcf Files

**Description:** Specifies BCF files.

#### [Caller](#caller)[](#caller "Click to copy url")

**Syntax:** obj \<\< Caller( "Multiallelic"\|"Consensus"="Multiallelic" )

**Description:** "Multiallelic" by default.

#### [Copy Task Specification](#copy-task-specification)[](#copy-task-specification "Click to copy url")

**Syntax:** obj \<\< Copy Task Specification

**Description:** Copies the current sequencing variants toolset specifications to the clipboard.

**JMP Version Added:** 19

#### [Files](#files)[](#files "Click to copy url")

**Syntax:** obj \<\< Files

**Description:** Load input files to be run in samtools.

#### [Ploidy](#ploidy)[](#ploidy "Click to copy url")

**Syntax:** obj \<\< Ploidy( number=2 )

**Description:** "2" by default.

#### [Recall in Task Specification](#recall-in-task-specification)[](#recall-in-task-specification "Click to copy url")

**Syntax:** obj \<\< Recall in Task Specification

**Description:** Sets the task specification in the Task Specification report to the specified model.

#### [Ref Files](#ref-files)[](#ref-files "Click to copy url")

**Syntax:** obj \<\< Ref Files

**Description:** Specifies Reference Genome files.

#### [Remove Run](#remove-run)[](#remove-run "Click to copy url")

**Syntax:** obj \<\< ( Run\[number\] \<\< Remove Run( state=0\|1 ) )

**Description:** Removes the specified run report from the report window.

#### [Results Folder](#results-folder)[](#results-folder "Click to copy url")

**Syntax:** obj \<\< Results Folder

**Description:** Specifies the result folder.

#### [Sam Files](#sam-files)[](#sam-files "Click to copy url")

**Syntax:** obj \<\< Sam Files

**Description:** Specifies SAM files.

#### [Send Output to Files List](#send-output-to-files-list)[](#send-output-to-files-list "Click to copy url")

**Syntax:** obj \<\< Send Output to Files List( state=0\|1 )

**Description:** Sends output files to the file list panel.

#### [Sort Reads By](#sort-reads-by)[](#sort-reads-by "Click to copy url")

**Syntax:** obj \<\< Sort Reads By( "Coordinates"\|"Alpha-numeric"\|"Lexicographical"="Coordinates" )

**Description:** "Coordinates" by default.

#### [Summary](#summary)[](#summary "Click to copy url")

**Syntax:** obj \<\< Summary( state=0\|1 )

**Description:** Shows or hides a report that contains details of the run. On by default.

#### [Target Regions](#target-regions)[](#target-regions "Click to copy url")

**Syntax:** obj \<\< Target Regions

**Description:** Sets target regions. The specification of regions requires that the BAM file be coordinate-sorted and indexed.

#### [Task](#task)[](#task "Click to copy url")

**Syntax:** obj \<\< Task( "Index Fasta"\|"Convert SAM to BAM"\|"Sort Reads"\|"Add Mate Coordinates"\|"Remove Duplicates"\|"Merge Files"\|"Index BAM"\|"Convert BAM To SAM"\|"Extract Mapped Reads"\|"Extract Unmapped Reads"\|"Extract Target Regions"\|"Extract Properly Aligned"\|"Extract First Read"\|"Tag Mismatches and Insertions"\|"Count Alignment"\|"Count Alignment By Flag"\|"Count Alignment By Reference"\|"Generate Statistics"\|"Generate Base Alignment Quality"\|"Generate Read Depth"\|"Bgzip Compress"\|"Bgzip Decompress"\|"Generate Genotype Likelihoods"\|"Generate Genotype Calls"\|"Convert Bcf to Vcf"\|"Convert Vcf to Bcf" )

**Description:** Determines the task to run.

#### [Title](#title_1)[](#title_1 "Click to copy url")

**Syntax:** obj \<\< Title

**Description:** Sets a title.

#### [Unthreaded](#unthreaded)[](#unthreaded "Click to copy url")

**Syntax:** obj \<\< Unthreaded( state=0\|1 )

**Description:** Use only the main thread for calculations

#### [Vcf Files](#vcf-files)[](#vcf-files "Click to copy url")

**Syntax:** obj \<\< Vcf Files

**Description:** Specifies VCF files.

## [Sequencing Variants Toolset Specification](#sequencing-variants-toolset-specification)[](#sequencing-variants-toolset-specification "Click to copy url")

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Auto Send Output to Files List](#auto-send-output-to-files-list_1)[](#auto-send-output-to-files-list_1 "Click to copy url")

**Syntax:** obj \<\< Auto Send Output to Files List( state=0\|1 )

**Description:** Sends output files to the files list panel.

#### [Bam Files](#bam-files_1)[](#bam-files_1 "Click to copy url")

**Syntax:** obj \<\< Bam Files

**Description:** Specifies BAM files.

#### [Bcf Files](#bcf-files_1)[](#bcf-files_1 "Click to copy url")

**Syntax:** obj \<\< Bcf Files

**Description:** Specifies BCF files.

#### [Caller](#caller_1)[](#caller_1 "Click to copy url")

**Syntax:** obj \<\< Caller( "Multiallelic"\|"Consensus"="Multiallelic" )

**Description:** "Multiallelic" by default.

#### [Files](#files_1)[](#files_1 "Click to copy url")

**Syntax:** obj \<\< Files

**Description:** Load input files to be run in samtools.

#### [Ploidy](#ploidy_1)[](#ploidy_1 "Click to copy url")

**Syntax:** obj \<\< Ploidy( number=2 )

**Description:** Specifies a positive number that indicates the ploidy level. "2" by default.

#### [Ref Files](#ref-files_1)[](#ref-files_1 "Click to copy url")

**Syntax:** obj \<\< Ref Files

**Description:** Specifies Reference Genome files.

#### [Results Folder](#results-folder_1)[](#results-folder_1 "Click to copy url")

**Syntax:** obj \<\< Results Folder

**Description:** Specifies the result folder.

#### [Sam Files](#sam-files_1)[](#sam-files_1 "Click to copy url")

**Syntax:** obj \<\< Sam Files

**Description:** Specifies SAM files.

#### [Sort Reads By](#sort-reads-by_1)[](#sort-reads-by_1 "Click to copy url")

**Syntax:** obj \<\< Sort Reads By( "Coordinates"\|"Alpha-numeric"\|"Lexicographical"="Coordinates" )

**Description:** "Coordinates" by default.

#### [Target Regions](#target-regions_1)[](#target-regions_1 "Click to copy url")

**Syntax:** obj \<\< Target Regions

**Description:** Sets target regions. The specification of regions requires that the BAM file be coordinate-sorted and indexed.

#### [Task](#task_1)[](#task_1 "Click to copy url")

**Syntax:** obj \<\< Task( "Index Fasta"\|"Convert SAM to BAM"\|"Sort Reads"\|"Add Mate Coordinates"\|"Remove Duplicates"\|"Merge Files"\|"Index BAM"\|"Convert BAM To SAM"\|"Extract Mapped Reads"\|"Extract Unmapped Reads"\|"Extract Target Regions"\|"Extract Properly Aligned"\|"Extract First Read"\|"Tag Mismatches and Insertions"\|"Count Alignment"\|"Count Alignment By Flag"\|"Count Alignment By Reference"\|"Generate Statistics"\|"Generate Base Alignment Quality"\|"Generate Read Depth"\|"Bgzip Compress"\|"Bgzip Decompress"\|"Generate Genotype Likelihoods"\|"Generate Genotype Calls"\|"Convert Bcf to Vcf"\|"Convert Vcf to Bcf"="Index Fasta" )

**Description:** Determines the task to run. "Index Fasta" by default.

#### [Title](#title_2)[](#title_2 "Click to copy url")

**Syntax:** obj \<\< Title

**Description:** Sets a title.

#### [Unthreaded](#unthreaded_1)[](#unthreaded_1 "Click to copy url")

**Syntax:** obj \<\< Unthreaded( state=0\|1 )

**Description:** Use only the main thread for calculations

#### [Vcf Files](#vcf-files_1)[](#vcf-files_1 "Click to copy url")

**Syntax:** obj \<\< Vcf Files

**Description:** Specifies VCF files.

[ Previous](Score%20Ellipse%20Coverage.html "Score Ellipse Coverage") [Next ](Socket.html "Socket")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
