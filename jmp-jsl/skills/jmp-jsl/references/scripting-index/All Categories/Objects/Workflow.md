# Workflow

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Workflow.html](https://jsl.jmp.com/All%20Categories/Objects/Workflow.html)*

---

# [Workflow](#workflow)[](#workflow "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Close](#close)[](#close "Click to copy url")

**Syntax:** workflow \<\< Close()

**Description:** Close the workflow.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Close();
```

### [Execute Next](#execute-next)[](#execute-next "Click to copy url")

**Syntax:** workflow \<\< Execute Next()

**Description:** Execute the current step in the workflow, and move the execution pointer to the following step.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Execute Next();
```

### [Get Execution Info](#get-execution-info)[](#get-execution-info "Click to copy url")

**Syntax:** workflow \<\< Get Execution Info(\<index\>)

**Description:** Return a structure containing information about the steps of the workflow that have been executed.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Resume;
wf << Get Execution Info( 1 );
```

### [Get Step Count](#get-step-count)[](#get-step-count "Click to copy url")

**Syntax:** workflow \<\< Get Step Count

**Description:** Return the number of steps in the workflow.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Get Step Count;
```

### [Get Step JSL](#get-step-jsl)[](#get-step-jsl "Click to copy url")

**Syntax:** workflow \<\< Get Step JSL(\<index\>)

**Description:** Return the JSL code of the given step in the workflow.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Get Step JSL( 1 );
```

### [Get Step Name](#get-step-name)[](#get-step-name "Click to copy url")

**Syntax:** workflow \<\< Get Step Name(\<index\>)

**Description:** Return the name of the given step in the workflow.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Get Step Name( 1 );
```

### [Log Executed Steps](#log-executed-steps)[](#log-executed-steps "Click to copy url")

**Syntax:** obj \<\< Log Executed Steps( state=0\|1 )

**Description:** Log the JSL script for each step that is executed.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Log Executed Steps( 1 );
wf << Resume();
```

### [Presentation Mode](#presentation-mode)[](#presentation-mode "Click to copy url")

**Syntax:** obj \<\< Presentation Mode( state=0\|1 )

**Description:** Presentation mode removes editing options and unnecessary support interfaces.

**JMP Version Added:** 17

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Presentation Mode( 1 );
```

### [Resume](#resume)[](#resume "Click to copy url")

**Syntax:** workflow \<\< Resume()

**Description:** Execute or resume execution of the workflow.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Resume();
```

### [Set Execution Callback](#set-execution-callback)[](#set-execution-callback "Click to copy url")

**Syntax:** workflow \<\< Set Execution Callback(\<callback\>)

**Description:** Set a callback on the workflow that will be notified each time a step finishes executing with associated information.

**JMP Version Added:** 18

``` jsl
//The callback function receives two arguments; the Workflow scriptable and a structure containing information about what step has just been executed and the reason if stopped.
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Set Execution Callback( Function( {wfb, data}, Show( data ) ) );
wf << Resume;
```

### [Set Next Step To Execute](#set-next-step-to-execute)[](#set-next-step-to-execute "Click to copy url")

**Syntax:** workflow \<\< Set Next Step To Execute(\<index\>)

**Description:** Move the execution cursor to a step in the workflow.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Set Next Step To Execute( 2 );
```

### [Start Over](#start-over)[](#start-over "Click to copy url")

**Syntax:** workflow \<\< Start Over()

**Description:** Reset the workflow back to the beginning, closing all tables and other windows opened by the workflow.

**JMP Version Added:** 18

``` jsl
wf = Open( "$SAMPLE_WORKFLOWS/WorkflowBuilder.jmpflow" );
wf << Start Over();
```

[ Previous](Window%20Object.html "Window Object") [Next ](XGBoost.html "XGBoost")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
