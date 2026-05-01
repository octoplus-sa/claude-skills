# Scripting Platforms

Source: JMP 19 Scripting Guide (PDF pages 475-520).

---

Scripting Platforms
Create, Repeat, and Modify Analyses
If you run the same analysis frequently, you can script it to automate the process. Anyone can
then run the script, ensuring the same results every time. To get started, perform your analysis
interactively as you normally would with JMP, and then save a script that re-creates that
analysis. You can modify the script to further customize it.
Figure 10.1 Typical Workflow for Scripting Platforms
Perform an
interactive analysis

Save the script for
the analysis

Add a platform
object reference

Send messages to
the platform object
This chapter is about scripting platforms, not reports. Platform object references and report
object references receive different types of JSL messages. Platforms can run tests, draw plots,
and so on. Reports can copy pictures, select display boxes, or close outline nodes. To learn
about scripting reports, see the section “Structure of JMP Reports”.
Tip: For additional scripting help, see the JMP Scripting Index (select Help > Scripting Index)
and the JSL Syntax Reference.

476

Scripting Platforms
