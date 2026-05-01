# Image

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Image.html](https://jsl.jmp.com/All%20Categories/Objects/Image.html)*

---

# [Image](#image)[](#image "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [New Image](#new-image)[](#new-image "Click to copy url")

**Syntax:** img = Open( filepath, jpg\|png\|gif\|bmp\|tif ) New Image(\<width, height\>, \<existing image\> )

**Description:** A picture object, which can be used for adding a picture to a frame or a display box.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
```

### [Open](#open)[](#open "Click to copy url")

**Syntax:** Open( filePath, \<data table options \| Excel import options \| text import options \| SAS import options \| HTML import options \| esriShapeFile import options \| PDF import options \| other file options \> )

**Description:** Returns a reference to a data table or other JMP file or object created from a file. If no path is specified, the Open dialog appears. If a folder path is specified, the system file browser is opened and no object is returned. Refer to the Syntax Reference for a complete description of available options.

``` jsl
/* Data tables, other JMP files, external files:
   Open( filePath,
     <Invisible | Private>,
     <Select Columns( "col", ... )>,
     <Ignore Columns( "col", ... )>,
     <Add to Recent Files(bool)>,
     <Quarantine Action("Allow Scripts"|"Block Scripts"|"Do Not Open"|"Show Dialog")>
     <Force Refresh>,
     <Enable Filter Views(bool)>,
     <"file type">
   )
*/
//Basic data table open
dt1 = Open( "$SAMPLE_DATA/Big Class.jmp" );
//Data table open with some options
dt2 = Open( "$SAMPLE_DATA/Fitness.jmp", Select Columns( "Name", "Sex", "Age", "Weight" ) );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Add Frame](#add-frame)[](#add-frame "Click to copy url")

**Syntax:** obj \<\< Add Frame

**Description:** Adds a new frame to an animated image. The frame will not contain any content until Set Pixels is used. An optional duration argument can be specified, which indicates the frame duration in milliseconds. If the duration argument is omitted, the duration of the current frame will be used as the duration of the added frame. If there are no other frames, a default duration of 100 milliseconds is used.

**JMP Version Added:** 16

``` jsl
dim = 100;
mat0 = J( dim, dim, 0 );
mat1 = J( dim, dim, 1 );
multiImage = New Image( "rgb", {mat1, mat0, mat0} );
multiImage << Add Frame( 2000 );
multiImage << Set Pixels( "rgb", {mat0, mat1, mat0} );
multiImage << Add Frame( 1000 );
multiImage << Set Pixels( "rgb", {mat0, mat0, mat1} );
win = New Window( "Multi-Frame Image", multiImage );
durs = multiImage << Get Frame Durations();
For( i = 0, i < 3, i++,
    multiImage << Set Current Frame( i );
    win << reshow();
    dur = durs[i + 1] / 1000.0;
    Wait( dur );
);
win << Close Window();
```

### [Crop](#crop)[](#crop "Click to copy url")

**Syntax:** obj \<\< Crop( Left( number ), Right( number ), Top( number ), Bottom( number ) )

**Description:** Modifies the image to be the sub-image at the specified pixel coordinates within the existing image.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
Wait( 1 );
img << Crop( Left( 50 ), Right( 300 ), Top( 20 ), Bottom( 200 ) );
obj2 = New Window( "Cropped", img );
```

### [Filter](#filter)[](#filter "Click to copy url")

**Syntax:** obj \<\< Filter( despeckle\|edge\|enhance\|median\|negate\|normalize\|sharpen\|contrast\|gamma\|reduce noise\|gaussian blur\|canny, \<number\> )

**Description:** Filters the image based on the specified algorithm. Filtering is useful for cleaning up noise in the image. Contrast, gamma and reduce noise require one additional (numeric) parameter. Gaussian blur requires two: radius and sigma.

**Example 1**

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
New Window( "tile(40,40)", New Image( img ) );
Wait( 1 );
img << Filter( "negate" );
New Window( "Neg filter", img ); 
//contrast filter example 
img2 = Open( "$SAMPLE_IMAGES/black rhino footprint.jpg", jpg );
obj = New Window( "Black Rhino", New Image( img2 ) );
Wait( 1 );
img3 = New Image( img2 );/*save a copy for later*/ img2 << Filter( "Contrast", 4 );
New Window( "Contrast filter", New Image( img2 ) );
```

**Example 2**

``` jsl
/* http://en.wikipedia.org/wiki/Canny_edge_detector */ 
radius = 1;
sigma = 3;
smallThreshold = .01;
largeThreshold = .3;
file = Pick File(
    "pick picture",
    "$SAMPLE_IMAGES",
    {"pictures|png;jpg", "All Files|*"},
    1,
    0,
    "black rhino footprint.jpg"
);
original = New Image( file );
edges = New Image( original );
New Window( "canny",
    H List Box(
        Slider Box(
            0,
            10,
            radius,
            refilter();
            hb << reshow;
            t1 << settext( Char( Floor( radius ) ) );,
            <<setwidth( 100 )
        ),
        Text Box( "radius of smoothing filter=" ),
        t1 = Text Box( Char( Floor( radius ) ) )
    ),
    H List Box(
        Slider Box(
            1,
            5,
            sigma,
            refilter();
            hb << reshow;
            t2 << settext( Char( Floor( sigma ) ) );,
            <<setwidth( 100 )
        ),
        Text Box( "smoothing repeat=" ),
        t2 = Text Box( Char( Floor( sigma ) ) )
    ),
    H List Box(
        sb1 = Slider Box(
            .0001,
            1,
            largeThreshold,
            If( smallThreshold >= largeThreshold,
                sb0 << set( largeThreshold / 2 )
            );
            refilter();
            hb << reshow;
            t3 << settext( Char( largeThreshold ) );
            t4 << settext( Char( smallThreshold ) );,
            <<setwidth( 300 )
        ),
        Text Box( "large (start) threshold=" ),
        t3 = Text Box( Char( largeThreshold ) )
    ),
    H List Box(
        sb0 = Slider Box(
            .0001,
            1,
            smallThreshold,
            If( smallThreshold >= largeThreshold,
                sb1 << set( smallThreshold + .1 )
            );
            refilter();
            hb << reshow;
            t4 << settext( Char( smallThreshold ) );
            t3 << settext( Char( largeThreshold ) );,
            <<setwidth( 300 )
        ),
        Text Box( "small (stop) threshold=" ),
        t4 = Text Box( Char( smallThreshold ) )
    ),
    Spacer Box( size( 10, 20 ) ),
    hb = H List Box( original, edges )
);
refilter = Function( {},
    edges << setpixels( original << getpixels );
    //edges << filter( "gaussian blur", radius, sigma ); //you could use the gaussian blur filter by setting radius(0), below
    edges << filter(
        "canny"/* here it is! */,
        largeThreshold( largeThreshold )/*tracing begins when a large-value edge is found*/,
        smallThreshold( smallThreshold )/*tracing stops when the edge value gets too small*/,
        radius( radius )/*a blur-filter, use 0 for no blurring*/,
        Repeat( sigma )/* number of repeats of a box-blur; 3 approximates a gaussian-blur filter */
    );
    edges << filter( "negate" );/*black on white*/
);
refilter();
```

### [Flip Both](#flip-both)[](#flip-both "Click to copy url")

**Syntax:** obj \<\< Flip Both

**Description:** Flips the image both horizontally and vertically.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
Wait( 1 );
img << Flip Both;
obj2 = New Window( "Diagonal Flip", img );
```

### [Flip Horizontal](#flip-horizontal)[](#flip-horizontal "Click to copy url")

**Syntax:** obj \<\< Flip Horizontal

**Description:** Flips the image horizontally.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
Wait( 1 );
img << Flip Horizontal;
obj2 = New Window( "Horizontal Flip", img );
```

### [Flip Vertical](#flip-vertical)[](#flip-vertical "Click to copy url")

**Syntax:** obj \<\< Flip Vertical

**Description:** Flips the image upside down.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
Wait( 1 );
img << Flip Vertical;
obj2 = New Window( "Vertical Flip", img );
```

### [Get Current Frame](#get-current-frame)[](#get-current-frame "Click to copy url")

**Syntax:** obj \<\< Get Current Frame

**Description:** Returns the current frame number. For most images, the value is 0. For animated GIF files, the value can be between 0 and one less than the number of frames. Actions, such as getPixels and setPixels, will act on the current frame.

``` jsl
img = New Image( "$SAMPLE_IMAGES/progress.gif" );
num = img << Get Current Frame();
```

### [Get EXIF](#get-exif)[](#get-exif "Click to copy url")

**Syntax:** obj \<\< Get EXIF

**Description:** Gets EXIF data that is stored internally with the image. An array of key/value pairs will be returned.

**JMP Version Added:** 14

``` jsl
img = New Image( "$SAMPLE_IMAGES/tile.jpg" );
exifData = img << getEXIF();
key = exifData << first;
While( !Is Empty( key ),
    v = exifData << getValue( key );
    Show( key, v );
    key = exifData << next( key );
);
```

### [Get Frame Durations](#get-frame-durations)[](#get-frame-durations "Click to copy url")

**Syntax:** obj \<\< Get Frame Durations

**Description:** Returns a matrix of the pause duration between each frame. The time is specified in milliseconds.

``` jsl
img = New Image( "$SAMPLE_IMAGES/progress.gif" );
durs = img << Get Frame Durations();
```

### [Get N Frames](#get-n-frames)[](#get-n-frames "Click to copy url")

**Syntax:** obj \<\< Get N Frames

**Description:** Returns the number of frames in the image. For most images this will be one. For animated GIF files this could be more than one.

``` jsl
img = New Image( "$SAMPLE_IMAGES/progress.gif" );
num = img << Get N Frames();
```

### [Get N Loops](#get-n-loops)[](#get-n-loops "Click to copy url")

**Syntax:** obj \<\< Get N Loops

**Description:** Returns the number of times an animated image should loop through its sequence. A value of zero indicates it should loop indefinitely.

``` jsl
img = New Image( "$SAMPLE_IMAGES/progress.gif" );
loops = img << Get N Loops();
```

### [Get Path](#get-path)[](#get-path "Click to copy url")

**Syntax:** obj \<\< Get Path

### [Get Pixels](#get-pixels)[](#get-pixels "Click to copy url")

**Syntax:** mat = img \<\< Get Pixels(); {r, g, b} = img \<\< Get Pixels("rgb"); {r, g, b, a} = img \<\< Get Pixels("rgba")

**Description:** If no color designator is specified, a matrix of JSL colors representing the pixel values is returned. A color designator of rgb will return a list of three matrices, red, green, and blue, respectively. Specifying rgba will return the alpha (transparency) channel as well as the red, green, and blue.

**Example 1**

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
win = New Window( "tile(40,40)", img );
m = img << Get Pixels;
Show( m );
```

**Example 2**

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
win = New Window( "tile(40,40)", img );
{r, g, b} = img << Get Pixels( "rgb" );
```

**Example 3**

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
win = New Window( "tile(40,40)", img );
{r, g, b, a} = img << Get Pixels( "rgba" );
```

### [GetSize](#getsize)[](#getsize "Click to copy url")

**Syntax:** {w,h} = pic \<\< Get Size {w,h} = pic \<\< Size

**Description:** Returns a list containing the width and height of the image.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
s = {w, h} = img << Get Size;
Show( s );
```

### [Remove Frame](#remove-frame)[](#remove-frame "Click to copy url")

**Syntax:** obj \<\< Remove Frame

**Description:** Removes a frame from an animated image. The index of the frame to remove is passed.

``` jsl
img = New Image( "$SAMPLE_IMAGES/progress.gif" );
img << Remove Frame( 0 );
```

### [Rotate](#rotate)[](#rotate "Click to copy url")

**Syntax:** obj \<\< Rotate( angle )

**Description:** Rotates the image by the specified angle of rotation.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
Wait( 1 );
img << Rotate( 45 );
obj2 = New Window( "Rotated", img );
```

### [Save Image](#save-image)[](#save-image "Click to copy url")

**Syntax:** obj \<\< Save Image( filePath, image type )

**Description:** Saves the image in the specified location and file name. The second parameter indicates what type of image to save, regardless of the extension used in the file name. Valid image types include PNG, JPG, GIF, TIFF, BMP, and PDF. If no image type is specified, or the specified image type is not understood, the image is saved as a PNG file.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
img << Save Image( "$TEMP/Mediterranean.jpg", "jpg" );
```

### [Scale](#scale)[](#scale "Click to copy url")

**Syntax:** obj \<\< Scale( scale \| xscale, yscale )

**Description:** Applies a scale factor to the width and height of the image or scales the width (xscale) and height (yscale) independently.

**Example 1**

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
img << scale( 0.5 );
obj2 = New Window( "Tile scaled by 0.5", img );
```

**Example 2**

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
img << scale( 2, 0.5 );
obj2 = New Window( "Tile scaled by 2 vertically and by 0.5 horizontally", img );
```

### [Set Blob](#set-blob)[](#set-blob "Click to copy url")

**Syntax:** obj \<\< Set Blob

**Description:** Sets the image from a blob.

### [Set Current Frame](#set-current-frame)[](#set-current-frame "Click to copy url")

**Syntax:** obj \<\< Set Current Frame( frame )

**Description:** Sets the current frame number. For most images this will be 0. For animated GIF files, this can be between 0 and one less than the number of frames. Actions, such as getPixels and setPixels, will act on the current frame.

``` jsl
img = New Image( "$SAMPLE_IMAGES/progress.gif" );
num = img << Get N Frames();
win = New Window( "Progress", img );
For( i = 0, i < num, i++,
    img << Set Current Frame( i );
    win << reshow();
    Wait( 1 );
);
win << Close Window();
```

### [Set Frame Duration](#set-frame-duration)[](#set-frame-duration "Click to copy url")

**Syntax:** obj \<\< Set Frame Duration( duration )

**Description:** Set the duration of the current frame in an animated image. The time is specified in milliseconds.

``` jsl
img = New Image( "$SAMPLE_IMAGES/progress.gif" );
img << Set Frame Duration( 1000 );
durs = img << Get Frame Durations();
```

### [Set N Loops](#set-n-loops)[](#set-n-loops "Click to copy url")

**Syntax:** obj \<\< Set N Loops( loops )

**Description:** Sets the number of times an animated image should loop through its sequence. A value of 0 indicates that the image should loop indefinitely.

``` jsl
img = New Image( "$SAMPLE_IMAGES/progress.gif" );
img << Set N Loops( 3 );
loops = img << Get N Loops();
```

### [Set Pixels](#set-pixels)[](#set-pixels "Click to copy url")

**Syntax:** img \<\< Set Pixels(jslmat); img \<\< Set Pixels ("rgb", {r, g, b})

**Description:** Sets the pixel matrix, or matrices, for the image. If one matrix is specified with no color designator, the matrix is treated as a matrix of JSL colors. A color designator can be specified, such as rgb, to indicate the following matrices are red, green, and blue, respectively. In this case, the size of all the specified matrices should be the same.

**Example 1**

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
win = New Window( "tile(40,40)", img );
m = img << Get Pixels;
Wait( 1 );
n = m`;
img << Set Pixels( n );
win2 = New Window( "Transformed", img );
```

**Example 2**

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
win = New Window( "tile(40,40)", img );
{r, g, b} = img << Get Pixels( "rgb" );
Wait( 1 );
i = .30 * r + .59 * g + .11 * b;
img << Set Pixels( "rgb", {i, i, i} );
win2 = New Window( "Gray Scale", img );
```

### [SetSize](#setsize)[](#setsize "Click to copy url")

**Syntax:** obj \<\< SetSize( {width, height} )

**Description:** Sets the image size based on the specified width and height.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
img << Set Size( {600, 600} );
obj2 = New Window( "Larger tile(40,40)", img );
```

### [Size](#size)[](#size "Click to copy url")

**Syntax:** {w,h} = pic \<\< Get Size {w,h} = pic \<\< Size

**Description:** Returns a list containing the width and height of the image.

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
obj = New Window( "tile(40,40)", img );
s = {w, h} = img << Get Size;
Show( s );
```

### [Transparency](#transparency)[](#transparency "Click to copy url")

**Syntax:** obj \<\< Transparency( fraction )

**Description:** Applies transparency to an image. Valid values are between 0.0 (transparent) and 1.0 (opaque)

``` jsl
img = Open( "$SAMPLE_IMAGES/tile.jpg", jpg );
win = New Window( "tile(40,40)", img );
Wait( 1 );
img << Transparency( 0.5 );
win << reshow;
```

[ Previous](IP.21%20Server.html "IP.21 Server") [Next ](Item%20Analysis.html "Item Analysis")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
