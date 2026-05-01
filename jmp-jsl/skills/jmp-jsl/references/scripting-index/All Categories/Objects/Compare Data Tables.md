# Compare Data Tables

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Compare%20Data%20Tables.html](https://jsl.jmp.com/All%20Categories/Objects/Compare%20Data%20Tables.html)*

---

# [Compare Data Tables](#compare-data-tables)[](#compare-data-tables "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Compare Data Tables](#compare-data-tables_1)[](#compare-data-tables_1 "Click to copy url")

**Syntax:** Compare Data Tables( \<Compare with( Data Table( name ))\>, \<show window(0 \| 1)\>, \<limit(integer)\>, \<Compare table properties(0 \| 1)\>, \<Compare column attributes and properties(0 \| 1)\>, \<Compare data(0 \| 1)\>, \<Fuzzy compare( \<0 \| 1\>, \<Relative Error(number)\>)\>, \<Show difference summary(0 \| 1)\>, \<Show difference plot(0 \| 1)\> )

**Description:** Compares two open data tables and reports differences between data, as well as metadata.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Are Data Different](#are-data-different)[](#are-data-different "Click to copy url")

**Syntax:** obj \<\< Are Data Different

**Description:** Returns true or false depending on whether the data of the two tables are different or not.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
how = (obj << Are Data Different);
```

### [Auto compare](#auto-compare)[](#auto-compare "Click to copy url")

**Syntax:** Auto Compare(0\|1)

**Description:** Perform comparisons as soon as any setting is changed

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Auto Compare( 1 );
```

### [Close](#close)[](#close "Click to copy url")

**Syntax:** obj \<\< Close

**Description:** Close the Compare Data Table object

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << close;
```

### [Compare](#compare)[](#compare "Click to copy url")

**Syntax:** Compare()

**Description:** Perform comparisons now

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Compare();
```

### [Compare Column Attributes and Properties](#compare-column-attributes-and-properties)[](#compare-column-attributes-and-properties "Click to copy url")

**Syntax:** obj \<\< Compare Column Attributes and Properties( state=0\|1 )

**Description:** Set or clear the flag to compare the columns attributes and properties. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << compare column attributes and properties( 1 );
```

### [Compare Data](#compare-data)[](#compare-data "Click to copy url")

**Syntax:** obj \<\< Compare Data( state=0\|1 )

**Description:** Set or clear the flag to compare the columns data. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << compare data( 0 );
```

### [Compare Table Properties](#compare-table-properties)[](#compare-table-properties "Click to copy url")

**Syntax:** obj \<\< Compare Table Properties( state=0\|1 )

**Description:** Set or clear the flag to compare the table variables and scripts. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << compare table properties;
```

### [Compare With](#compare-with)[](#compare-with "Click to copy url")

**Syntax:** obj \<\< Compare With( Data Table( name ) )

**Description:** Compare the first table with this table. Returns true or false.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
obj = dt << Compare Data Tables();
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
same = obj << compare with( dt2 );
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Put the Compare Data Tables script on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Copy Script;
```

### [Fuzzy Compare](#fuzzy-compare)[](#fuzzy-compare "Click to copy url")

**Syntax:** obj \<\< Fuzzy Compare( \<(state= 1 \| 0)\>, \<Relative Error (number)\> )

**Description:** Set or clear the flag to compare the columns data.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << fuzzy compare( relative error( 0.0001 ) );
```

### [Get column attributes differences](#get-column-attributes-differences)[](#get-column-attributes-differences "Click to copy url")

**Syntax:** obj \<\< Get column attributes differences( columns( column) )

**Description:** Get the list of column attributes which are different for the compared columns.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
attribDiff = (obj << Get columns attributes differences( :name ));
```

### [Get column properties differences](#get-column-properties-differences)[](#get-column-properties-differences "Click to copy url")

**Syntax:** obj \<\< Get column properties differences( columns( column) )

**Description:** Get the list of column properties which are different for the compared columns.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
propDiff = (obj << Get columns properties differences( :name ));
```

### [Get columns list](#get-columns-list)[](#get-columns-list "Click to copy url")

**Syntax:** obj \<\< Get columns list( ( \<differed in data\> \| \<differed in properties\> \| \<mismatched data type\> \| \<differed in attributes\>) )

**Description:** Get the list of columns that differ in data, column properties, data type, or other column attributes.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
colDiff = (obj << Get columns list( differed in attributes ));
Show( colDiff );
```

### [Get difference summary matrix](#get-difference-summary-matrix)[](#get-difference-summary-matrix "Click to copy url")

**Syntax:** obj \<\< Get difference summary matrix

**Description:** Gets the difference summary as a matrix. The matrix columns correspond to the columns in the difference summary. The first column, action, is represented in the matrix with -1 for Delete, 0 for Replace, and 1 for Add.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
mtx = (obj << Get Difference Summary matrix);
```

### [Get table scripts difference list](#get-table-scripts-difference-list)[](#get-table-scripts-difference-list "Click to copy url")

**Syntax:** obj \<\< Get table scripts difference list

**Description:** Get the list of table scripts that are different or missing.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
scriptDiff = (obj << Get table scripts difference list);
```

### [Get table variables difference list](#get-table-variables-difference-list)[](#get-table-variables-difference-list "Click to copy url")

**Syntax:** obj \<\< Get table variables difference list

**Description:** Get the list of table variables which are different or missing.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
tvdiff = (obj << Get table variables difference list);
```

### [Get unmatched columns list](#get-unmatched-columns-list)[](#get-unmatched-columns-list "Click to copy url")

**Syntax:** obj \<\< Get unmatched columns list

**Description:** Get the list of unmatched columns, those that do not have corresponding columns to be compared

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
colDiff = (obj << Get unmatched columns list);
```

### [Hide column properties with no differences](#hide-column-properties-with-no-differences)[](#hide-column-properties-with-no-differences "Click to copy url")

**Syntax:** Hide column properties with no differences(0\|1)

**Description:** Hide properties that are the same when comparing column properties.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Hide column properties with no differences( 0 );
```

### [Hide columns with no differences](#hide-columns-with-no-differences)[](#hide-columns-with-no-differences "Click to copy url")

**Syntax:** Hide columns with no differences(0\|1)

**Description:** Hide columns that are the same when comparing table data.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Hide columns with no differences( 0 );
```

### [Hide rows with no differences](#hide-rows-with-no-differences)[](#hide-rows-with-no-differences "Click to copy url")

**Syntax:** Hide rows with no differences(0\|1)

**Description:** Hide rows that are the same when comparing table data.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Hide rows with no differences( 0 );
```

### [Hide table properties with no differences](#hide-table-properties-with-no-differences)[](#hide-table-properties-with-no-differences "Click to copy url")

**Syntax:** Hide table properties with no differences(0\|1)

**Description:** Hide items that are the same when comparing table metadata.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Hide table properties with no differences( 0 );
```

### [Ignore case](#ignore-case)[](#ignore-case "Click to copy url")

**Syntax:** Ignore Case(0\|1)

**Description:** Ignore character case during data comparison

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Ignore Case( 1 );
```

### [Ignore missing](#ignore-missing)[](#ignore-missing "Click to copy url")

**Syntax:** Ignore Missing(0\|1)

**Description:** Ignore missing values during data comparison

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Ignore Missing( 1 );
```

### [Ignore whitespace](#ignore-whitespace)[](#ignore-whitespace "Click to copy url")

**Syntax:** Ignore Whitespce(0\|1)

**Description:** Ignore whitespace characters during data comparison

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Ignore Whitespace( 1 );
```

### [Limit](#limit)[](#limit "Click to copy url")

**Syntax:** obj \<\< Limit( integer )

**Description:** Set the limit for the number of difference. Compare will stop when the limit is reached.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << limit( 100 );
```

### [Link](#link)[](#link "Click to copy url")

**Syntax:** Link({"col1", "col2", \<ID(0\|1)\>, \<No Compare(0\|1)\>, \<Fuzzy Compare(\<Ignore Case(0\|1)\>, \<Ignore Whitespace(0\|1)\>, \<Ignore Missing(0\|1)\>, \<Relative Error(\<amount\>)\>)\>

**Description:** Specify column pairs to compare and other comparison options.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Link( {:age, :weight}, );
```

### [Relative Error](#relative-error)[](#relative-error "Click to copy url")

**Syntax:** obj \<\< Relative Error( integer )

**Description:** Set the relative error for fuzzy compare.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Relative Error( 0.00001 );
```

### [Report](#report)[](#report "Click to copy url")

**Syntax:** obj \<\< Report

**Description:** Returns a reference to the report object.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Row Alignment](#row-alignment)[](#row-alignment "Click to copy url")

**Syntax:** obj \<\< Row Alignment (Flexible by Row\|By Row\|Use ID Columns)

**Description:** Set how the rows are aligned for comparison.

Flexible By Row: attempt to find as many matching rows as possible in order by skipping over blocks of non-matching rows.

By Row: compare each row by line number.

Use ID Columns: the ID columns specified are used to create a key for each row. This key is used to match rows.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Row Alignment( "By Row" );
```

### [Save Difference Summary](#save-difference-summary)[](#save-difference-summary "Click to copy url")

**Syntax:** obj \<\< Save Difference Summary( \<invisible(0 \| 1)\> )

**Description:** Save the difference summary in a data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
summaryDT = (obj << save difference summary( invisible ));
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script to Data Table

**Description:** Save the Compare Data Tables script as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Save Script to Data Table;
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Add a Button to the journal containing the Compare Data Tables script.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Save Script to Journal;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Append the Compare Data Tables script to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Save Script to Script Window;
```

### [Show Window](#show-window)[](#show-window "Click to copy url")

**Syntax:** obj \<\< Show Window( Show window( 0\|1) )

**Description:** Show or hide the window for Compare Data Table

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << show window( 1 );
```

### [Show fuzzy differences](#show-fuzzy-differences)[](#show-fuzzy-differences "Click to copy url")

**Syntax:** Show Fuzzy Differences(0\|1)

**Description:** Hilite differences in data comparison for values that are equal only because of fuzzy comparison settings

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Show Fuzzy Differences( 1 );
```

### [Unlink](#unlink)[](#unlink "Click to copy url")

**Syntax:** Unlink(\<column name 1\>, \<column name 2\>)

**Description:** Remove the column comparison.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Unlink( {"a", "b"} );
```

### [Unlink All](#unlink-all)[](#unlink-all "Click to copy url")

**Syntax:** Unlink All

**Description:** Remove all column comparisons.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Students1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Students2.jmp" );
obj = dt << Compare Data Tables( compare With( Data Table( "Students2" ) ) );
obj << Unlink All;
```

[ Previous](Columns%20Manager.html "Columns Manager") [Next ](Constant%20Stress%20ALT%20Design.html "Constant Stress ALT Design")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
