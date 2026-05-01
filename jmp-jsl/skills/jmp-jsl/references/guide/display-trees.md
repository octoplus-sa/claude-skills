# Display Trees

Source: JMP 19 Scripting Guide (PDF pages 521-634).

---

Display Trees
Create and Interact with Windows
After you learn the basics of scripting, you’re ready to manipulate JMP reports and create new
JMP windows. This chapter focuses on the following topics:
•

navigating JMP display trees to manipulate items in report windows

•

building new windows with custom results

•

building modal windows

•

interacting with the script editor

•

converting deprecated Dialog() scripts to New Window() scripts

Display Tree Compatibility Issues
JMP platforms are generally stable from release to release. However, sometimes the structure
of reports changes in major releases. When this happens, old scripts can fail because of the
new structure. To avoid the continual updating of old scripts, write scripts so that they avoid
dependence on the report structure. Using a string to index a box, followed by a numbered
subscript to pick a specific child box, is most reliable across releases. See “Create a Reference
by Subscripting”. See “Compatibility Notes” for compatibility issues in JMP 19.
Note: This chapter shows how to create and use the most common display boxes. All display
boxes are documented in the JMP Scripting Index, which is available in the Help menu.

522

Display Trees
