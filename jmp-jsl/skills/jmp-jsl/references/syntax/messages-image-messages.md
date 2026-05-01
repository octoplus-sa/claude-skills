# Image Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 467-469).

## Index (line numbers in this file)

- `<< Crop` — L67
- `<< Filter` — L69
- `<< Flip Both` — L108
- `<< Flip Horizontal` — L110
- `<< Flip Vertical` — L112
- `<< Get EXIF` — L114
- `<< Get N Frames` — L117
- `<< Get Size` — L131
- `<< Rotate` — L134
- `<< Save Image` — L136
- `<< Set Current Frame` — L128
- `<< Size` — L132
- `AutoDeclare()` — L40
---

JSL Messages
Image Messages

467

description is an optional, quoted string that contains a description of the structure

for reference.
dll object<<Get Declaration JSL
Sends the declaration JSL from the DLL object to log.
dll object<<Load DLL(path, <AutoDeclare(Boolean|"Quiet"|"Verbose")>)
dll object<<Load DLL(path, <"Quiet"|"Verbose">)
Description

Loads the DLL from the specified path.
Required Argument
path A quoted path that specifies where to load the DLL.
Optional Named Arguments
AutoDeclare(Boolean|"Quiet"|"Verbose") AutoDeclare(1) and
AutoDeclare("Verbose") write verbose messages to the log. AutoDeclare("Quiet")

turns off log window messages. If you omit this option, verbose messages are written to
the log.
Quiet|Verbose When you use Declare Function, this option turns off log window
messaging ("Quiet") or turns on log window messaging ("Verbose").
dll object<<Show Functions
Sends the declared functions for the DLL object to the log.
dll object<<Unload DLL
Unloads the DLL.

Image Messages
This section contains JSL messages that apply to images.
Related Information
•

The Scripting Index provides examples for processing images. In JMP, select Help >
Scripting Index to view this interactive resource.

•

Additional resources are available from the JMP File Exchange at
https://community.jmp.com/community/file-exchange.

Image Messages

img<<Crop(Left(pix), Right(pix), Top(pix), Bottom(pix))
Creates a new image from an existing image to the specified dimensions (in pixels).
img<<Filter(name, <n>)
Filters the image based on the specified algorithm. Filtering is useful for cleaning up noise
in the image.
Note: All of the JMP image filters are supported at the operating system level. Images that are
processed on Windows might differ from images processed on Apple macOS.
Argument
name Specifies the quoted name of a JMP image filter. The following filters are available:

– "Despeckle" removes defects (that is, speckles) from a scanned or captured image (for
example, scratches, dust, etc.).
– "Edge" identifies pixels in an image where the brightness changes sharply and darkens
pixels with no sharp change. Edge detection is used to detect changes in surface, depth,
material, and lighting.
– "Enhance" reduces the contrast between pixels in a noisy image.
– "Median" reduces noise (that is, the random variation) and smooths an image by
comparing each pixel’s brightness with its neighbors’ and, if the value is very different,
replaces it with the average of the neighbors’ values.
– "Negate" creates the negative of the color or gray-scale image by changing each pixel
color to its complementary color.
– "Normalize" changes a color image’s pixels to use the full range of the file format’s
number system. Normalization will make the image’s colors more intense.
– "Sharpen" reduces blur by sharpening edges of an image.
– "Contrast", n brightens or darkens an image. A higher number (>0.0) brightens an
image; a lower number (<0.0) darkens an image.
– "Gamma", n corrects the image visual display (brightness and intensity) to account for
differences in monitor hardware. A higher number (> 1.0) lightens the image; a lower
number (< 1.0) darkens the image.
– "Reduce Noise", n reduces the random variation (or noise) that occurs with higher
ISO sensitivity or longer exposure times.
– "Gaussian Blur", radius, sigma reduces image noise and detail creating a
smoother image. Radius is equal to the blur radius around each pixel and sigma is the
standard deviation of the Gaussian distribution. Gaussian blur is commonly used
when resizing or performing edge detection.

JSL Messages
Image Messages

469

img<<Flip Both
Flips the image from left to right and top to bottom.
img<<Flip Horizontal
Flips the image from left to right.
img<<Flip Vertical
Flips the image from top to bottom.
img<<Get EXIF
Returns EXIF data from the image (such as the shutter speed and aperture value) in an
associative array.
img<<Get N Frames
Description

Returns the number of frames in a multi-frame TIF or animated GIF file, where the
number of frames begins with frame 0.
Example

The following example places a four-frame TIF file in a new window and shows the image
that is in the first frame.
img = New Image( "$DOWNLOADS/Multiframe.tif" );
nframes = img << Get N Frames(); // return 4
img << Set Current Frame( 1 ); // show image 1
win = New Window( "Multi-Frame TIFF", img );

img<<Get Size
img<<Size
Returns a list containing the width and height (in pixels) of the image.
img<<Rotate(degrees)
Rotates the image by the specified number of degrees.
img<<Save Image(path)
Saves the image to the quoted path.
