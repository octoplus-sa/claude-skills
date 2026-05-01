# Notebook

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Notebook.html](https://jsl.jmp.com/All%20Categories/Objects/Notebook.html)*

---

# [Notebook](#notebook)[](#notebook "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Notebook](#notebook_1)[](#notebook_1 "Click to copy url")

**Syntax:** nb = Notebook( name\|number )

**Description:** Creates a new notebook, or returns the notebook with the provided name or index.

``` jsl

nb = Notebook();
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Enable Inline Logging](#enable-inline-logging)[](#enable-inline-logging "Click to copy url")

**Syntax:** obj \<\< Enable Inline Logging( 0\|1 )

**Description:** Enables/disables the logging of output in notebook blocks.

``` jsl


nb = Notebook();

nb << Enable Inline Logging( 0 );
```

### [Export to a Workflow](#export-to-a-workflow)[](#export-to-a-workflow "Click to copy url")

**Syntax:** obj \<\< Export to a Workflow( \<Create(wfb name)\>\|\<AddTo(wfb name)\> )

**Description:** Exports the blocks of the notebook to a workflow.

``` jsl


nb = Notebook();

nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );
nb << Add New Block(
    "JSL", "Data Table ( \!"Big Class\!" ) << Distribution ( Y(:age, :sex) )"
);
nb << Export to a Workflow;
```

### [Get Window](#get-window)[](#get-window "Click to copy url")

**Syntax:** obj \<\< Get Window

**Description:** Returns the window of this notebook.

``` jsl


nb = Notebook();

nb << Get Window;
```

### [Import .ipynb File](#import-ipynb-file)[](#import-ipynb-file "Click to copy url")

**Syntax:** obj \<\< Import .ipynb File( file path )

**Description:** Loads the provided .ipynb file as blocks in the notebook.

``` jsl


nb = Notebook();

nb << Import .ipynb File( NOTEBOOKPATH );
```

### [Run All Scripts](#run-all-scripts)[](#run-all-scripts "Click to copy url")

**Syntax:** obj \<\< Run All Scripts

**Description:** Runs the full notebook.

``` jsl


nb = Notebook();

nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );
nb << Add New Block(
    "JSL", "Data Table ( \!"Big Class\!" ) << Distribution ( Y(:age, :sex) )"
);
Wait( 1 );
nb << Run All Scripts;
```

### [Show Embedded Log](#show-embedded-log)[](#show-embedded-log "Click to copy url")

**Syntax:** obj \<\< Show Embedded Log( 0\|1 )

**Description:** Enables/disables the embedded log in the notebook.

``` jsl


nb = Notebook();

nb << Show Embedded Log( 1 );
```

### [Title](#title)[](#title "Click to copy url")

**Syntax:** obj \<\< Title( title )

**Description:** Sets the title of this notebook.

``` jsl


nb = Notebook();

nb << Title( "Example Title" );
Show( nb << Title );
```

## [Block](#block)[](#block "Click to copy url")

### [Associated Constructors](#associated-constructors_1)[](#associated-constructors_1 "Click to copy url")

#### [Block](#block_1)[](#block_1 "Click to copy url")

**Syntax:** Block

``` jsl

nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );
```

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Block Name](#block-name)[](#block-name "Click to copy url")

**Syntax:** obj \<\< Block Name( name )

**Description:** Sets/gets the title of this block.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

block << Block Name( "Test Block Name" );
```

#### [Duplicate Block](#duplicate-block)[](#duplicate-block "Click to copy url")

**Syntax:** obj \<\< Duplicate Block

**Description:** Duplicates this block and adds the new block as its sibling.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

block << Duplicate Block;
```

#### [Get Content](#get-content)[](#get-content "Click to copy url")

**Syntax:** obj \<\< Get Content

**Description:** Gets the content of the block.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

Show( block << Get Content );
```

#### [Get Output](#get-output)[](#get-output "Click to copy url")

**Syntax:** obj \<\< Get Output

**Description:** Gets the display tree output of the block.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

block2 = nb << Add New Block(
    "JSL", "Data Table ( \!"Big Class\!" ) << Distribution ( Y(:age, :sex) )"
);
Wait( 1 );
nb << Run All Scripts;
block2 << Get Output;
```

#### [Import .ipynb File](#import-ipynb-file_1)[](#import-ipynb-file_1 "Click to copy url")

**Syntax:** obj \<\< Import .ipynb File( file path )

**Description:** Loads the provided .ipynb file as blocks added to this section.

``` jsl

nb = Notebook();
section = nb << Add New Block( "Section" );
section << Import .ipynb File( NOTEBOOKPATH );
```

#### [Line Count](#line-count)[](#line-count "Click to copy url")

**Syntax:** obj \<\< Line Count( number )

**Description:** Sets the maximum number of lines shown in this block before enabling scrolling. Set to zero to enable auto-sizing.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

block << Line Count( 1 );
```

#### [Move Block Down](#move-block-down)[](#move-block-down "Click to copy url")

**Syntax:** obj \<\< Move Block Down

**Description:** Moves this block down by one in the list.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

block2 = nb << Add New Block(
    "JSL", "Data Table ( \!"Big Class\!" ) << Distribution ( Y(:age, :sex) )"
);
block << Move Block Down;
```

#### [Move Block Up](#move-block-up)[](#move-block-up "Click to copy url")

**Syntax:** obj \<\< Move Block Up

**Description:** Moves this block up by one in the list.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

block2 = nb << Add New Block(
    "JSL", "Data Table ( \!"Big Class\!" ) << Distribution ( Y(:age, :sex) )"
);
block2 << Move Block Up;
```

#### [Popout Results](#popout-results)[](#popout-results "Click to copy url")

**Syntax:** obj \<\< Popout Results

**Description:** Sends the current output of this block to a new window.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

block2 = nb << Add New Block(
    "JSL", "Data Table ( \!"Big Class\!" ) << Distribution ( Y(:age, :sex) )"
);
Wait( 1 );
nb << Run All Scripts;
block2 << Popout Results;
```

#### [Remove Block](#remove-block)[](#remove-block "Click to copy url")

**Syntax:** obj \<\< Remove Block

**Description:** Removes this block from its parent.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

block << Remove Block;
```

#### [Remove Section](#remove-section)[](#remove-section "Click to copy url")

**Syntax:** obj \<\< Remove Section

**Description:** Removes this section from its parent.

``` jsl

nb = Notebook();
section = nb << Add New Block( "Section" );
section << Remove Section;
```

#### [Run Script](#run-script)[](#run-script "Click to copy url")

**Syntax:** obj \<\< Run Script

**Description:** Executes the contents of the current block.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

Wait( 1 );
block << Run Script;
```

#### [Run Section](#run-section)[](#run-section "Click to copy url")

**Syntax:** obj \<\< Run Section

**Description:** Runs the children of this section in order.

``` jsl

nb = Notebook();
section = nb << Add New Block( "Section" );
section << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );
Wait( 1 );
section << Run Section;
```

#### [Set Content](#set-content)[](#set-content "Click to copy url")

**Syntax:** obj \<\< Set Content( content )

**Description:** Sets the content of the block.

``` jsl


nb = Notebook();
block = nb << Add New Block( "JSL", "Open (\!"$SAMPLE_DATA/Big Class.jmp\!")" );

block << Set Content( "Print(Char(Pi(), 10))" );
```

[ Previous](Normalization.html "Normalization") [Next ](NumberEditableBox.html "NumberEditableBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
