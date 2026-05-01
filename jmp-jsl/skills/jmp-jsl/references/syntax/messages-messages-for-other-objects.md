# Messages for Other Objects

Source: JMP 19 JSL Syntax Reference (PDF pages 501-504).

## Index (line numbers in this file)

- `<< Save` — L32
- `<< Save As` — L35
- `<< Save HTML` — L67
- `<< Save PDF` — L88
- `<< Save RTF` — L75
- `Run Foreground()` — L20
---

JSL Messages
Messages for Other Objects

501

Run Foreground(<OnRunComplete(script), <"Private"|"Invisible">>,
<OnRunCanceled(script)>, <OnError(script)>)
Description

Runs the SQL query in the foreground.
Returns

A data table that opens when the query is finished.
See Also

“Run Background(<OnRunComplete(script), <ʺPrivateʺ|ʺInvisibleʺ>>,
<OnRunCanceled(script)>, <OnError(script)>)”
obj<<Save
Saves the query to its associated file. The save fails if the query does not yet have an
associated file.
obj<<Save As(path, <Replace Existing(Boolean))
Saves the query to the specified file. If the file already exists, the save fails unless Replace
Existing is true.

Messages for Other Objects
This section contains JSL messages that apply to other objects, such as zip archives and
journals.

Zip Archives
This section contains JSL messages that apply to zip archives.
list = za<<Dir
Returns a list of member names
data = za<<Read(member name, <Format("blob")>)
Returns a quoted string that contains the entire quoted member name. A zip file consists of
file names, also called “member names”.
Notes

For remote files, JMP copies the URL data to the local disk. When the zip archive is no
longer accessible, the local data file is deleted.

Messages for Other Objects

actualname = za<<Write(member name, member data, <"replace">)
Writes a quoted string or quoted blob to a zip archive member file. If the quoted member
name isn’t in the current zip file, the returned actualname is the same as member name.
This member name will be changed to prevent overwriting an existing member; the name
actually used is returned. The quoted member data argument is the data to write into the
zip file’s member of that name. replace creates the file with a temporary name, deletes
the old file, and renames the temporary file to the existing name.

Journals
This section contains JSL messages that apply to JMP journals.
jnl<<Save HTML(<path>, <format>)
Saves the journal as HTML.
Optional Arguments
"path" Specifies the quoted path for the saved HTML file (for example,
"C:\myFile.html").
format Specifies the quoted graphic file format. JPG, PNG, and TIFF formats are
supported. The graphics are saved in a subdirectory named gfx.

jnl<<Save RTF(<path>, <format>)
Saves the journal as an RTF file.
Optional Arguments
"path" Specifies the quoted path for the saved RTF file (for example, "C:\myFile.rtf").
"format" Specifies the quoted file format for the embedded graphics. "JPG", "PNG", and
"EMF" formats are supported on Windows. All journals are saved as PDF files by

default on Apple macOS.
Notes

If no path or format are provided, you are prompted to name the file and specify the
format on Windows. On Apple macOS, you are prompted to name the file. The file is
saved as a PDF file by default.
jnl<<Save PDF(<path>, <Show Page Setup(Boolean)>, <Portrait(Boolean)>)
Saves the journal as a PDF file.
Optional Arguments
"path" The quoted path for the saved PDF file (for example, "C:\myFile.pdf").
Show Page Setup If set to true, opens the Page Setup window to let the user change the

margin, magnification level, and other page layout options.

JSL Messages
Messages for Other Objects

503

Portrait Determines whether the page orientation is portrait or landscape. Overrides

the user’s selection in the Show Page Setup window.

Messages for Other Objects
