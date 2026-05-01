# Compatibility Notes

Source: JMP 19 Scripting Guide (PDF pages 931-932).

---

Appendix A
Compatibility Notes
Changes in JMP 18.0
Application Data Folder Location
The location where preferences and add-ins are stored changed in JMP 18.0 on Windows. The
location on Apple macOS did not change. This change has particular relevance for add-ins.
On Windows, prior to JMP 18, all add-ins for all versions of JMP were stored in:
C:\Users\<username>\AppData\Roaming\SAS\JMP\Addins

In JMP 18 that location changed to:
C:\Users\<username>\AppData\Roaming\JMP\JMP\Addins

When JMP 18 is first launched on Windows, add-ins from JMP 17 and earlier are copied to the
new JMP 18 location.
Because add-ins are copied to a different location, changes made to an add-in at JMP 18 do not
effect the original add-in installation at JMP 17 (or earlier). For example, a recent file list is not
shared with earlier versions, and uninstalling an add-in at JMP 18 will not uninstall it for prior
versions.

932

Compatibility Notes

Appendix A
