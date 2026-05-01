# Data Tables

Source: JMP 19 Scripting Guide (PDF pages 325-474).

---

Data Tables
Work with Data Table Objects
Before you can work with a data table or with objects in a data table, you must first open the
data table and assign a reference to it. In the Scripting Guide, dt represents a reference to a data
table object.
To manipulate an object in JSL, you send a message to the reference that represents the object,
asking the object to perform one of its tasks. Messages are commands that can be understood
only in context by a particular type of object. For example, messages for data table objects
include Save, New Column, Sort, and so on. Most of these messages would not make sense for
another object, such as a platform object.
In this chapter, you can learn the following:
•

How to assign a reference to a data table

•

How to send messages to the reference, resulting in specific actions

•

About the different types of messages that data table objects can understand

Most of this chapter focuses on the different types of messages that you can send to data table
objects, such as data tables, columns, rows, and values.
Tip: This chapter contains most, but not all of the JSL commands that you can use with data
tables. For an exhaustive list, see the JMP Scripting Index. Select Help > Scripting Index. Select
Objects from the menu, and then select Data Table.

326

Data Tables
