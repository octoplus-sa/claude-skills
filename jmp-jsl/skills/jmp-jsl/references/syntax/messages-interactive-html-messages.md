# Interactive HTML Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 470-471).

## Index (line numbers in this file)

- `<< Add Image` — L82
- `<< Publish` — L66
- `<< Scale` — L24
- `<< Set Current Frame` — L40
- `<< Set Size` — L49
- `<< Transparency` — L53
- `Data()` — L70
- `File()` — L81
- `New Window()` — L31
- `Public()` — L86
- `Publish Data()` — L96
- `Reports()` — L67
- `Title()` — L83
---

Interactive HTML Messages

img<<Scale(scale|xscale, yscale)
Resizes the image by the specified dimensions. Provide one argument to resize both the
width and height. Provide two arguments to resize the width and height separately.
Examples
img = New Image( "$SAMPLE_IMAGES/tile.jpg" );
xs = 2;
img << Scale( xs );
New Window( "Tilex 2", img );
img = New Image( "$SAMPLE_IMAGES/tile.jpg" );
img << Scale( 2, 0.5 ); // scale image width by 2 and height by 1/2
New Window( "Tile squished", img );

Notes

Using Scale is an alternative to getting the size of the image, multiplying by the scale
factor, and then setting the size.
img<<Set Current Frame
Description

Sets the frame that shows in a multi-frame TIFF or animated GIF file. Specify 0 through the
number of frames minus 1. For example, with four frames, you can specify frame 0
through frame 3.
See Also

“img<<Get N Frames”
img<<Set Size(width, height)
Resizes the image to the specified dimensions (in pixels). To scale the image
proportionally, specify a width and height that correspond to the aspect ratio in the
original image.
img<<Transparency(fraction)
Sets the transparency for the image where the fraction is between 0.0 (full transparency) to
1.0 (no transparency).

Interactive HTML Messages
This section contains JSL messages for interactive HTML web reports.

JSL Messages
Interactive HTML Messages

471

Web Report Messages
webreport<<Publish(<Add Image(...)>, <Add Report(...)>, <Add
Reports(...)>, <Public(Boolean)>, <Index(...), <User Name(...)>,
<Password(...)|password function)>,
<Prompt("IfNeeded"|"Always"|"Never")>, <URL(...)>, <Publish
Data(Boolean)>, Replace(<id>, Prompt("IfNeeded"|"Always"|"Never"))>)
Description

Publishes the web report to the JMP server.
Returns

On success, the URL of the published report is returned.
Optional Arguments
Add Image Inserts an image at the top of the index page. Valid formats are "png", "bmp",
"jpeg", "jpg", "tiff", and "tif". Title and Description are optional. Title
appears above the image. Description appears below the image. Use
File(filepath) or just a quoted string. Here is an example:
webrpt << Add Image( File( "C:\Users\Public\JMP\Projects\WebJMP\atlas.jpg" ),
Title( "Atlas" ), Description( "Holding up the world as always." ) );

Add Report Adds a report to publish within the web report.
Public(Boolean) Specifies whether the public has access to the report. By default, the

report is private.
Index The name of the index page for multiple reports. You can also specify the
description.
User Name Specifies the user name registered on the JMP server.
Password Specifies the user’s password. You can also define a password function.
Prompt Displays a window in which the user types the server URL, user name, and
password.
URL The location that you are publishing to.
Publish Data(Boolean) Includes the data in the HTML. Reports contains static rather
than interactive images. In a public report, you might not want to share the data.
Replace Replaces the report. Get the URL from the address field in the browser where
the page is displayed.
