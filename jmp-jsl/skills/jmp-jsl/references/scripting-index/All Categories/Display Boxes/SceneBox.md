# SceneBox

*Source: [https://jsl.jmp.com/All%20Categories/Display%20Boxes/SceneBox.html](https://jsl.jmp.com/All%20Categories/Display%20Boxes/SceneBox.html)*

---

# [SceneBox](#scenebox)[](#scenebox "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Scene Box](#scene-box)[](#scene-box "Click to copy url")

**Syntax:** box = Scene Box( xsize, ysize )

**Description:** Returns a display box that can execute OpenGL commands.

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [ArcBall](#arcball)[](#arcball "Click to copy url")

**Syntax:** obj \<\< ArcBall( list,radius )

**Description:** Draws the objects in the specified list which allow rotation by left clicking and dragging.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << color( 0, 0, 1 );
shape << Text( center, baseline, 0.2, "Hello, World." );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << ArcBall( shape, 1 );
scene << Update;
```

### [Background Color](#background-color)[](#background-color "Click to copy url")

**Syntax:** obj \<\< Background Color( red, green, blue )

**Description:** Sets the background color of the Scene Box.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << color( 0, 0, 1 );
scene << Text( center, baseline, 0.2, "Hello, World." );
scene << Background Color( 0, 0, 0 );
```

### [Begin](#begin)[](#begin "Click to copy url")

**Syntax:** obj \<\< Begin

**Description:** Specifies the starting point of a primitive. Uses the OpenGL command glBegin.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Begin( POLYGON );
shape << Color( 1, 0, 0 );
shape << Vertex( -1, 0.75, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -0.75, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -0.75, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 0.75, 0 );
shape << End();
scene = Scene Box( 200, 200 );
scene << CallList( shape );
New Window( "Example", scene );
```

### [BlendFunc](#blendfunc)[](#blendfunc "Click to copy url")

**Syntax:** obj \<\< BlendFunc( source factor,destination factor )

**Description:** Sets the functions used for blending. Uses the OpenGL command glBlendFunc.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Enable( Blend );
shape << BlendFunc( SRC_ALPHA, ONE_MINUS_SRC_ALPHA );
shape << Begin( POLYGON );
shape << Color( 1, 0, 0, 0 );
shape << Vertex( -1, 0.75, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -0.75, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -0.75, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 0.75, 0 );
shape << End();
shape << Disable( Blend );
scene = Scene Box( 200, 200 );
scene << CallList( shape );
New Window( "Example", scene );
```

### [CallList](#calllist)[](#calllist "Click to copy url")

**Syntax:** obj \<\< CallList( list )

**Description:** Draws the objects in the specified list. Uses the OpenGL command glCallList.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color( 0, 0.48, 0.72 );
shape << Disk( .5, 1, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << CallList( shape );
scene << update;
```

### [Clear](#clear)[](#clear "Click to copy url")

**Syntax:** obj \<\< Clear

**Description:** Clears the scene to the background color.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 500, 500 );
fps = Scene Display List();
window = New Window( "Frames Per Second", scene );
lastTime = 0;
frameCount = 0;
framesPerSecond = "Frames Per Second: ";
While( 1,
    time = Today();
    frameCount++;
    If( time != lastTime,
        framesPerSecond = Char( frameCount );
        frameCount = 0;
        lastTime = time;
    );
    fps << Clear;
    fps << Translate( -1, 0, 0 );
    fps << Color( 1, 0, 0 );
    fps << Text( left, baseline, .1, "Frames Per Second: " || framesPerSecond );
    scene << Clear;
    scene << CallList( fps );
    scene << Update;
    Wait( 0 );
);
```

### [ClipPlane](#clipplane)[](#clipplane "Click to copy url")

**Syntax:** obj \<\< ClipPlane( clip_plane0\|clip_plane1\|clip_plane2\|clip_plane3\|clip_plane4\|clip_plane5,x,y,z,d )

**Description:** Creates a clipping plane. Uses the OpenGL command glClipPlane.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Color( 0, 0.48, 0.72 );
shape << Cylinder( 0.5, 0.5, 2, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << enable( CLIP_PLANE0 );
scene << ClipPlane( CLIP_PLANE0, 1, 1, 0, 0 );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << ArcBall( shape, 2 );
scene << Disable( CLIP_PLANE0 );
scene << Update;
```

### [Color](#color)[](#color "Click to copy url")

**Syntax:** obj \<\< Color( r,g,b,\<a\> )

**Description:** Sets the color. For the alpha layer to work, blending must be enabled. Uses the OpenGL command glColor.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Enable( Blend );
shape << BlendFunc( SRC_ALPHA, ONE_MINUS_SRC_ALPHA );
shape << Begin( POLYGON );
shape << Color( 1, 0, 0, 0 );
shape << Vertex( -1, 0.75, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -0.75, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -0.75, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 0.75, 0 );
shape << End();
shape << Disable( Blend );
scene = Scene Box( 200, 200 );
scene << CallList( shape );
New Window( "Example", scene );
```

### [ColorMask](#colormask)[](#colormask "Click to copy url")

**Syntax:** obj \<\< ColorMask( red=0\|1,green=0\|1,blue=0\|1,alpha=0\|1 )

**Description:** Applies a color mask to the succeeding objects. Uses the OpenGL command glColorMask.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.0, 0.0 );
shape << Material( Front, Ambient, 0, 1, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << ColorMask( 1, 1, 0, 0 );
shape << Begin( POLYGON );
shape << Color( 1, 0, 0 );
shape << Vertex( -1, 1.5, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -1.5, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -1.5, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 1.5, 0 );
shape << End();
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 2 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [ColorMaterial](#colormaterial)[](#colormaterial "Click to copy url")

**Syntax:** obj \<\< ColorMaterial( Front\|Back\|Front_And_Back,Emission\|Ambient\|Diffuse\|Specular\|Ambient_And_Diffuse )

**Description:** Applies a color material to the succeeding objects. Uses the OpenGL command glColorMaterial.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color Material( Front_And_Back, Ambient );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [CullFace](#cullface)[](#cullface "Click to copy url")

**Syntax:** obj \<\< CullFace( front\|back\|front_and_back )

**Description:** Sets where culling should be enabled. Uses the OpenGL command glCullFace.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( CULL_FACE );
shape << CullFace( Front );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
shape << Disable( CULL_FACE );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [Cylinder](#cylinder)[](#cylinder "Click to copy url")

**Syntax:** obj \<\< Cylinder( base radius,top radius,height,slices,stacks )

**Description:** Creates a cylinder. Uses the OpenGL Utility command gluCylinder.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Color( 0, 0.48, 0.72 );
shape << Cylinder( 0.5, 0.5, 2, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << ArcBall( shape, 2 );
scene << Update;
```

### [DepthFunc](#depthfunc)[](#depthfunc "Click to copy url")

**Syntax:** obj \<\< DepthFunc( nevert\|lesst\|equalt\|lequalt\|greatert\|notequalt\|gequalt\|always )

**Description:** Sets the depth function to use for depth buffer comparisons. Uses the OpenGL command glDepthFunc.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( DEPTH_TEST );
shape << DepthFunc( never );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
shape << Disable( DEPTH_TEST );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [DepthMask](#depthmask)[](#depthmask "Click to copy url")

**Syntax:** obj \<\< DepthMask( state=0\|1 )

**Description:** Sets whether or not the depth buffer can be written to. Uses the OpenGL command glDepthMask.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( DEPTH_TEST );
shape << DepthMask( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
shape << Disable( DEPTH_TEST );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [DepthRange](#depthrange)[](#depthrange "Click to copy url")

**Syntax:** obj \<\< DepthRange( near,far )

**Description:** Sets the near and far depth range. Anything outside of this range will not be drawn. Uses the OpenGL command glDepthRange.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( DEPTH_TEST );
shape << DepthRange( 1, 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
shape << Disable( DEPTH_TEST );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [Disable](#disable)[](#disable "Click to copy url")

**Syntax:** obj \<\< Disable

**Description:** Disables various OpenGL capabilities. Uses the OpenGL command glDisable.

**JMP Version Added:** 16

``` jsl
showfog = 1;
scene = Scene Box( 600, 600 );
New Window( "Example",
    scene,
    box = Button Box( "Disable Fog",
        showfog = !showfog;
        refresh();
    )
);
refresh = Function( {},
    scene << clear;
    scene << perspective( 50, .5, 5 );
    scene << translate( 0, 0, -2 );
    scene << backgroundcolor( "Black" );
    If( showfog,
        scene << enable( FOG );
        scene << fog( FOG_END, 3 );
        scene << fog( FOG_START, 1 );
        scene << fog( FOG_COLOR, 0, 0, 0 );
        scene << fog( FOG_MODE, LINEAR );
        box << SetButtonName( "Disable Fog" );
    ,
        scene << disable( FOG );
        box << SetButtonName( "Enable Fog" );
    );
    scene << color( 0, 1, 0 );
    scene << rotate( 180, 1, 0, 0 );
    object = Scene Display List();
    object << cylinder( .8, .4, 1, 40, 10 );
    scene << calllist( object );
    scene << update;
);
refresh();
```

### [Disk](#disk)[](#disk "Click to copy url")

**Syntax:** obj \<\< Disk( inner radius,outer radius,slices,rings )

**Description:** Creates a disk. Uses the OpenGL Utility command gluDisk.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Color( 0, 0.48, 0.72 );
shape << Disk( .5, 1, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << ArcBall( shape, 2 );
scene << Update;
```

### [Enable](#enable)[](#enable "Click to copy url")

**Syntax:** obj \<\< Enable

**Description:** Enables various OpenGL capabilities. Uses the OpenGL command glEnable.

**JMP Version Added:** 16

``` jsl
showfog = 1;
scene = Scene Box( 600, 600 );
New Window( "Example",
    scene,
    box = Button Box( "Disable Fog",
        showfog = !showfog;
        refresh();
    )
);
refresh = Function( {},
    scene << clear;
    scene << perspective( 50, .5, 5 );
    scene << translate( 0, 0, -2 );
    scene << backgroundcolor( "Black" );
    If( showfog,
        scene << enable( FOG );
        scene << fog( FOG_END, 3 );
        scene << fog( FOG_START, 1 );
        scene << fog( FOG_COLOR, 0, 0, 0 );
        scene << fog( FOG_MODE, LINEAR );
        box << SetButtonName( "Disable Fog" );
    ,
        scene << disable( FOG );
        box << SetButtonName( "Enable Fog" );
    );
    scene << color( 0, 1, 0 );
    scene << rotate( 180, 1, 0, 0 );
    object = Scene Display List();
    object << cylinder( .8, .4, 1, 40, 10 );
    scene << calllist( object );
    scene << update;
);
refresh();
```

### [End](#end)[](#end "Click to copy url")

**Syntax:** obj \<\< End

**Description:** Specifies the ending point of a primitive. Uses the OpenGL command glEnd.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Begin( POLYGON );
shape << Color( 1, 0, 0 );
shape << Vertex( -1, 0.75, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -0.75, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -0.75, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 0.75, 0 );
shape << End();
scene = Scene Box( 200, 200 );
scene << CallList( shape );
New Window( "Example", scene );
```

### [EvalCoord1](#evalcoord1)[](#evalcoord1 "Click to copy url")

**Syntax:** obj \<\< EvalCoord1( u )

**Description:** Evaluates the one dimensional map. Uses the OpenGL command glEvalCoord1d.

**JMP Version Added:** 16

``` jsl
NPOINTS = 4;
points = J( NPOINTS, 3, 0 );
For( x = 1, x <= NPOINTS, x++,
    points[x, 1] = Random Uniform() - .5;
    points[x, 2] = Random Uniform() - .5;
    points[x, 3] = 0;
);
curve = Scene Box( 500, 400 );
curve << Map1( MAP1_VERTEX_3, 0, 1, 3, NPOINTS, points );
curve << Enable( MAP1_VERTEX_3 );
curve << Ortho2D( -.6, .6, -.6, .6 );
curve << Color( 0, 0, 1 );
curve << Begin( line_strip );
For( i = 0, i <= 30, i++,
    curve << EvalCoord1( i / 30 )
);
curve << End();
curve << Disable( MAP1_VERTEX_3 );
New Window( "Example", curve );
```

### [EvalCoord2](#evalcoord2)[](#evalcoord2 "Click to copy url")

**Syntax:** obj \<\< EvalCoord2( u,v )

**Description:** Evaluates the two dimensional map. Uses the OpenGL command glEvalCoord2d.

**JMP Version Added:** 16

``` jsl
gridsize = 10;
npoints = 16;
imax = 8;
jmax = 20;
points = J( npoints, 3, 0 );
For( i = 0, i < npoints, i++,
    points[i, 1] = Random Uniform() - .5;
    points[i, 2] = Random Uniform() - .5;
    points[i, 3] = Random Uniform() - .5;
);
surface = Scene Display List();
surface << Enable( MAP2_VERTEX_3 );
surface << Enable( Auto_Normal );
surface << Map2( MAP2_VERTEX_3, 0, 1, 3, 4, 0, 1, 12, 4, points );
surface << color( 0, 0, 1 );
For( i = 0, i <= imax, i++,
    surface << begin( LINE_STRIP );
    For( j = 0, j <= jmax, j++,
        surface << EvalCoord2( j / jmax, i / imax )
    );
    surface << End();
    surface << Begin( LINE_STRIP );
    For( j = 0, j < jmax, j++,
        surface << EvalCoord2( i / imax, j / jmax )
    );
    surface << End();
);
sb = Scene Box( 500, 400 );
sb << Ortho( -.75, .75, -.75, .75, -1, 1 );
sb << CallList( surface );
sb << backgroundcolor( "white" );
New Window( "Example", sb );
```

### [EvalMesh1](#evalmesh1)[](#evalmesh1 "Click to copy url")

**Syntax:** obj \<\< EvalMesh1( mode,i1,i2 )

**Description:** Evaluates the one dimensional mesh. Uses the OpenGL command glEvalMesh1.

**JMP Version Added:** 16

``` jsl
gridsize = 100;
NPOINTS = 4;
points = J( NPOINTS, 3, 0 );
For( x = 1, x <= NPOINTS, x++,
    points[x, 1] = (x - 1) / (NPOINTS - 1) - .5;
    points[x, 2] = Random Uniform() - .5;
    points[x, 3] = 0;
);
spline = Scene Box( 500, 400 );
spline << Ortho2D( -.6, .6, -.6, .6 );
spline << Enable( MAP1_VERTEX_3 );
spline << MapGrid1( gridsize, 0, 1 );
spline << color( .2, .2, 1 );
spline << Map1( MAP1_VERTEX_3, 0, 1, 3, NPOINTS, points );
spline << EvalMesh1( LINE, 0, gridsize );
New Window( "Example", spline );
```

### [EvalMesh2](#evalmesh2)[](#evalmesh2 "Click to copy url")

**Syntax:** obj \<\< EvalMesh2( mode,i1,i2,j1,j2 )

**Description:** Evaluates the two dimensional mesh. Uses the OpenGL command glEvalMesh2.

**JMP Version Added:** 16

``` jsl
gridsize = 10;
npoints = 32;
points = J( npoints, 3, 0 );
For( i = 0, i < npoints, i++,
    points[i, 1] = Random Uniform() - .5;
    points[i, 2] = Random Uniform() - .5;
    points[i, 3] = Random Uniform() - .5;
);
surface = Scene Display List();
surface << Enable( MAP2_VERTEX_3 );
surface << Enable( Auto_Normal );
surface << MapGrid2( gridsize, 0, 1, gridsize, 0, 1 );
surface << color( 0, 0, 1 );
surface << Map2( MAP2_VERTEX_3, 0, 1, 3, 4, 0, 1, 12, 4, points );
surface << EvalMesh2( LINE, 0, gridsize, 0, gridsize );
sb = Scene Box( 500, 400 );
sb << Ortho( -.75, .75, -.75, .75, -1, 1 );
sb << ArcBall( surface, 1 );
New Window( "Example", sb );
```

### [EvalPoint1](#evalpoint1)[](#evalpoint1 "Click to copy url")

**Syntax:** obj \<\< EvalPoint1( i )

**Description:** Evaluates a single point in the one dimensional mesh. Uses the OpenGL command glEvalPoint1.

**JMP Version Added:** 16

``` jsl
NPOINTS = 4;
points = J( NPOINTS, 3, 0 );
For( x = 1, x <= NPOINTS, x++,
    points[x, 1] = Random Uniform() - .5;
    points[x, 2] = Random Uniform() - .5;
    points[x, 3] = 0;
);
curve = Scene Box( 500, 400 );
curve << Map1( MAP1_VERTEX_3, 0, 1, 3, NPOINTS, points );
curve << Enable( MAP1_VERTEX_3 );
curve << Ortho2D( -.6, .6, -.6, .6 );
curve << Color( 0, 0, 1 );
curve << Begin( line_strip );
For( i = 0, i <= 60, i++,
    curve << EvalPoint1( i )
);
curve << End();
curve << Disable( MAP1_VERTEX_3 );
New Window( "Example", curve );
```

### [EvalPoint2](#evalpoint2)[](#evalpoint2 "Click to copy url")

**Syntax:** obj \<\< EvalPoint2( i,j )

**Description:** Evaluates a single point in the two dimensional mesh. Uses the OpenGL command glEvalPoint2.

**JMP Version Added:** 16

``` jsl
gridsize = 10;
npoints = 16;
imax = 8;
jmax = 20;
points = J( npoints, 3, 0 );
For( i = 0, i < npoints, i++,
    points[i, 1] = Random Uniform() - .5;
    points[i, 2] = Random Uniform() - .5;
    points[i, 3] = Random Uniform() - .5;
);
curves = Scene Display List();
curves << Enable( MAP2_VERTEX_3 );
curves << Enable( Auto_Normal );
curves << Map2( MAP2_VERTEX_3, 0, 1, 3, 4, 0, 1, 12, 4, points );
curves << color( 0, 0, 1 );
For( i = 0, i <= imax, i++,
    curves << begin( LINE_STRIP );
    For( j = 0, j <= jmax, j++,
        curves << EvalCoord2( j / jmax, i / imax )
    );
    curves << End();
    curves << Begin( LINE_STRIP );
    For( j = 0, j < jmax, j++,
        curves << EvalPoint2( i, j )
    );
    curves << End();
);
sb = Scene Box( 500, 400 );
sb << Ortho( -.75, .75, -.75, .75, -1, 1 );
sb << CallList( curves );
sb << backgroundcolor( "white" );
New Window( "Example", sb );
```

### [Fog](#fog)[](#fog "Click to copy url")

**Syntax:** obj \<\< Fog( fog_mode\|fog_density\|fog_start\|fog_end\|fog_index\|fog_color,p1,\<p2\>,\<p3\>,\<p4\> )

**Description:** Creates fog. Uses the OpenGL command glFog.

**JMP Version Added:** 16

``` jsl
showfog = 1;
scene = Scene Box( 600, 600 );
New Window( "Example",
    scene,
    box = Button Box( "Disable Fog",
        showfog = !showfog;
        refresh();
    )
);
refresh = Function( {},
    scene << clear;
    scene << perspective( 50, .5, 5 );
    scene << translate( 0, 0, -2 );
    scene << backgroundcolor( "Black" );
    If( showfog,
        scene << enable( FOG );
        scene << fog( FOG_END, 3 );
        scene << fog( FOG_START, 1 );
        scene << fog( FOG_COLOR, 0, 0, 0 );
        scene << fog( FOG_MODE, LINEAR );
        box << SetButtonName( "Disable Fog" );
    ,
        scene << disable( FOG );
        box << SetButtonName( "Enable Fog" );
    );
    scene << color( 0, 1, 0 );
    scene << rotate( 180, 1, 0, 0 );
    object = Scene Display List();
    object << cylinder( .8, .4, 1, 40, 10 );
    scene << calllist( object );
    scene << update;
);
refresh();
```

### [Frame](#frame)[](#frame "Click to copy url")

**Syntax:** obj \<\< Frame( x0,x1,y0,y1,z0,z1,farside )

**Description:** Draws a frame.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 200, 200 );
New Window( "Example", scene );
scene << frame( -0.2, 0.2, -0.2, 0.2, 0.0, 0.0, 1 );
scene << frame( -0.4, 0.4, -0.4, 0.4, 0.0, 0.0, 1 );
scene << frame( -0.6, 0.6, -0.6, 0.6, 0.0, 0.0, 1 );
scene << frame( -0.8, 0.8, -0.8, 0.8, 0.0, 0.0, 1 );
```

### [FrontFace](#frontface)[](#frontface "Click to copy url")

**Syntax:** obj \<\< FrontFace( cw\|ccw )

**Description:** Sets which polygons are front or back facing. This is used with object culling. Uses the OpenGL command glFrontFace.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( CULL_FACE );
shape << CullFace( Front );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
shape << Disable( CULL_FACE );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << frontface( cw );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [Frustum](#frustum)[](#frustum "Click to copy url")

**Syntax:** obj \<\< Frustum( left,right,bottom,top,near,far )

**Description:** Sets the parameters used by the camera. Uses the OpenGL command glFrustum.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << Frustum( -3, 1, -1, 1, 2, 9 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [Get Background Color](#get-background-color)[](#get-background-color "Click to copy url")

**Syntax:** color = obj \<\< Get Background Color

**Description:** Returns the background color of the Scene Box.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << color( 0, 0, 1 );
scene << Text( center, baseline, 0.2, "Hello, World." );
scene << Background Color( 0, 0, 0 );
scene << Get Background Color();
```

### [Get Show ArcBall](#get-show-arcball)[](#get-show-arcball "Click to copy url")

**Syntax:** obj \<\< Get Show ArcBall

**Description:** Returns the display state of the ArcBall.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << color( 0, 0, 1 );
shape << Text( center, baseline, 0.2, "Hello, World." );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << ArcBall( shape, 1 );
scene << Show ArcBall( always );
scene << Update;
scene << Get Show ArcBall();
```

### [Get Width](#get-width)[](#get-width "Click to copy url")

**Syntax:** pixels = obj \<\< Get Width

**Description:** Returns the width of the box.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
scene << Get Width();
```

### [Height](#height)[](#height "Click to copy url")

**Syntax:** obj \<\< Height( pixels )

**Description:** Sets the height of the box.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
scene << Height( 150 );
```

### [Light](#light)[](#light "Click to copy url")

**Syntax:** obj \<\< Light( light0\|light1\|light2\|light3\|light4\|light5\|light6\|light7,ambient\|diffuse\|specular\|position,x\|r,y\|g,z\|b,\<a\> )

**Description:** Creates a light source with the specified parameters. Uses the OpenGL command glLight.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color( 0, 0.48, 0.72 );
shape << Sphere( 1.5, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << Light( Light0, Ambient, 0, 0, 1, 1 );
scene << Light( Light0, Diffuse, 0, 1, 1, 1 );
scene << Light( Light0, Specular, 1, 1, 0, 1 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [LightModel](#lightmodel)[](#lightmodel "Click to copy url")

**Syntax:** obj \<\< LightModel( light_model_ambient\|light_model_local_viewer\|light_model_two_side,r,g,b,a )

**Description:** Sets the parameters used for the light model. Uses the OpenGL command glLightModel.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << Light Model( light_model_ambient, 0.2, 0, 0.5, 1 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [LineStipple](#linestipple)[](#linestipple "Click to copy url")

**Syntax:** obj \<\< LineStipple( factor,pattern )

**Description:** Sets the line stipple pattern. Uses the OpenGL command glLineStipple.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 200, 200 );
New Window( "Example", scene );
scene << LineWidth( 4 );
scene << color( 0, 0, 0 );
scene << Enable( LINE_STIPPLE );
scene << LineStipple( 2, 01101010 );
scene << Begin( LINES );
scene << Vertex( -.8, 0, 0 );
scene << Vertex( .8, 0, 0 );
scene << End();
scene << Disable( LINE_STIPPLE );
```

### [LineWidth](#linewidth)[](#linewidth "Click to copy url")

**Syntax:** obj \<\< LineWidth( width )

**Description:** Sets the width of the line. Uses the OpenGL command glLineWidth.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 200, 200 );
New Window( "Example", scene );
scene << LineWidth( 1 );
scene << Begin( LINES );
scene << color( 0, 0, 0 );
scene << Vertex( -.4, 0.04, 0 );
scene << Vertex( .4, 0.04, 0 );
scene << End();
scene << LineWidth( 4 );
scene << Begin( LINES );
scene << Vertex( -.4, -0.04, 0 );
scene << Vertex( .4, -0.04, 0 );
scene << End();
```

### [LoadIdentity](#loadidentity)[](#loadidentity "Click to copy url")

**Syntax:** obj \<\< LoadIdentity

**Description:** Sets the current matrix to the identity matrix. Uses the OpenGL command glLoadIdentity.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color( 0, 0.48, 0.72 );
shape << Sphere( 0.5, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 1.0, 0.0, -5 );
scene << CallList( shape );
scene << LoadIdentity;
scene << Perspective( 90, 1, 10 );
scene << Translate( -1.0, 0.0, -5 );
scene << CallList( shape );
scene << update;
```

### [LoadMatrix](#loadmatrix)[](#loadmatrix "Click to copy url")

**Syntax:** obj \<\< LoadMatrix( matrix )

**Description:** Sets the current matrix to the specified matrix. Uses the OpenGL command glLoadMatrix.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color( 0, 0.48, 0.72 );
shape << Sphere( 0.5, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 1.0, 0.0, -5 );
scene << CallList( shape );
identitymatrix = [1 0 0 0, 0 1 0 0, 0 0 1 0, 0 0 0 1];
scene << LoadMatrix( identitymatrix );
scene << Perspective( 90, 1, 10 );
scene << Translate( -1.0, 0.0, -5 );
scene << CallList( shape );
scene << update;
```

### [LoadName](#loadname)[](#loadname "Click to copy url")

**Syntax:** obj \<\< LoadName( i )

**Description:** Use with picker, load the integer that identifies the succeeding object. Uses the OpenGL command glLoadName.

**JMP Version Added:** 16

``` jsl
spheres = Scene Display List();
spheres << Point Size( 50 );
Spheres << PushName( 0 );
For( i = 0, i < 3, i++,
    spheres << LoadName( (i + 1) );
    spheres << PushMatrix;
    spheres << Translate( (i * 0.75 - .75), 0, 0 );
    spheres << color( 1, 0, 0 );
    spheres << Begin( POINTS );
    spheres << Vertex( 0, 0, -.0001 );
    spheres << End;
    spheres << color( 0, 0, 0 );
    spheres << Text( center, middle, 0.2, Char( (i + 1) ) );
    spheres << PopMatrix;
);
spheres << PopName;
view = Scene Box( 500, 400 );
view << Ortho( -1, 1, -1, 1, -2, 2 );
view << CallList( spheres );
view << update;
New Window( "Example", view );
Print( view << Pick( 50, 200, 1, 1, 4, 1 ) );
```

### [LookAt](#lookat)[](#lookat "Click to copy url")

**Syntax:** obj \<\< LookAt( eye x,eye y,eye z,center x,center y,center z,up x,up y,up z )

**Description:** Sets the location that the camera should be looking. Uses the OpenGL Utility command gluLookAt.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Cylinder( 0.5, 0.5, 2, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 20 );
scene << LookAt( 1, 0, 7, 0, 0, 0, 0, 1, 0 );
scene << ArcBall( shape, 2 );
scene << Update;
```

### [Map1](#map1)[](#map1 "Click to copy url")

**Syntax:** obj \<\< Map1( target,u1,u2,stride,order,points )

**Description:** Defines a one dimensional evaluator. Uses the OpenGL command glMap1d.

**JMP Version Added:** 16

``` jsl
gridsize = 100;
NPOINTS = 4;
points = J( NPOINTS, 3, 0 );
For( x = 1, x <= NPOINTS, x++,
    points[x, 1] = (x - 1) / (NPOINTS - 1) - .5;
    points[x, 2] = Random Uniform() - .5;
    points[x, 3] = 0;
);
spline = Scene Box( 500, 400 );
spline << Ortho2D( -.6, .6, -.6, .6 );
spline << Enable( MAP1_VERTEX_3 );
spline << MapGrid1( gridsize, 0, 1 );
spline << color( .2, .2, 1 );
spline << Map1( MAP1_VERTEX_3, 0, 1, 3, NPOINTS, points );
spline << EvalMesh1( LINE, 0, gridsize );
New Window( "Example", spline );
```

### [Map2](#map2)[](#map2 "Click to copy url")

**Syntax:** obj \<\< Map2( target,u1,u2,ustride,uorder,v1,v2,vstride,vorder,points )

**Description:** Defines a two dimensional evaluator. Uses the OpenGL command glMap2d.

**JMP Version Added:** 16

``` jsl
gridsize = 10;
npoints = 32;
points = J( npoints, 3, 0 );
For( i = 0, i < npoints, i++,
    points[i, 1] = Random Uniform() - .5;
    points[i, 2] = Random Uniform() - .5;
    points[i, 3] = Random Uniform() - .5;
);
surface = Scene Display List();
surface << Enable( MAP2_VERTEX_3 );
surface << Enable( Auto_Normal );
surface << MapGrid2( gridsize, 0, 1, gridsize, 0, 1 );
surface << color( 0, 0, 1 );
surface << Map2( MAP2_VERTEX_3, 0, 1, 3, 4, 0, 1, 12, 4, points );
surface << EvalMesh2( LINE, 0, gridsize, 0, gridsize );
sb = Scene Box( 500, 400 );
sb << Ortho( -.75, .75, -.75, .75, -1, 1 );
sb << ArcBall( surface, 1 );
New Window( "Example", sb );
```

### [MapGrid1](#mapgrid1)[](#mapgrid1 "Click to copy url")

**Syntax:** obj \<\< MapGrid1( un,u1,u2 )

**Description:** Defines a one dimensional mesh. Uses the OpenGL command glMapGrid1d.

**JMP Version Added:** 16

``` jsl
gridsize = 100;
NPOINTS = 4;
points = J( NPOINTS, 3, 0 );
For( x = 1, x <= NPOINTS, x++,
    points[x, 1] = (x - 1) / (NPOINTS - 1) - .5;
    points[x, 2] = Random Uniform() - .5;
    points[x, 3] = 0;
);
spline = Scene Box( 500, 400 );
spline << Ortho2D( -.6, .6, -.6, .6 );
spline << Enable( MAP1_VERTEX_3 );
spline << MapGrid1( gridsize, 0, 1 );
spline << color( .2, .2, 1 );
spline << Map1( MAP1_VERTEX_3, 0, 1, 3, NPOINTS, points );
spline << EvalMesh1( LINE, 0, gridsize );
New Window( "Example", spline );
```

### [MapGrid2](#mapgrid2)[](#mapgrid2 "Click to copy url")

**Syntax:** obj \<\< MapGrid2( un,u1,u2,vn,v1,v2 )

**Description:** Defines a two dimensional mesh. Uses the OpenGL command glMapGrid2d.

**JMP Version Added:** 16

``` jsl
gridsize = 10;
npoints = 32;
points = J( npoints, 3, 0 );
For( i = 0, i < npoints, i++,
    points[i, 1] = Random Uniform() - .5;
    points[i, 2] = Random Uniform() - .5;
    points[i, 3] = Random Uniform() - .5;
);
surface = Scene Display List();
surface << Enable( MAP2_VERTEX_3 );
surface << Enable( Auto_Normal );
surface << MapGrid2( gridsize, 0, 1, gridsize, 0, 1 );
surface << color( 0, 0, 1 );
surface << Map2( MAP2_VERTEX_3, 0, 1, 3, 4, 0, 1, 12, 4, points );
surface << EvalMesh2( LINE, 0, gridsize, 0, gridsize );
sb = Scene Box( 500, 400 );
sb << Ortho( -.75, .75, -.75, .75, -1, 1 );
sb << ArcBall( surface, 1 );
New Window( "Example", sb );
```

### [Material](#material)[](#material "Click to copy url")

**Syntax:** obj \<\< Material

**Description:** Specifies the type of material to use for the succeeding objects. Uses the OpenGL command glMaterial.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << update;
```

### [MatrixMode](#matrixmode)[](#matrixmode "Click to copy url")

**Syntax:** obj \<\< MatrixMode( modelview\|projection\|texture )

**Description:** Sets which matrix to operate on. Uses the OpenGL command glMatrixMode.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color( 0, 0.48, 0.72 );
shape << Sphere( 0.5, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 1.0, 0.0, -5 );
scene << CallList( shape );
scene << MatrixMode( projection );
scene << LoadIdentity;
scene << Perspective( 90, 1, 10 );
scene << Translate( -1.0, 0.0, -5 );
scene << CallList( shape );
scene << update;
```

### [MultMatrix](#multmatrix)[](#multmatrix "Click to copy url")

**Syntax:** obj \<\< MultMatrix( matrix )

**Description:** Multiplies the current matrix by the specified matrix. Uses the OpenGL command glMultMatrix.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color( 0, 0.48, 0.72 );
shape << Sphere( 1.0, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
matrix = [1.5 0 0 0, 0 1 0 0, 0 0 1 0, 0 0 0 1];
scene << MultMatrix( matrix );
scene << CallList( shape );
scene << update;
```

### [Normal](#normal)[](#normal "Click to copy url")

**Syntax:** obj \<\< Normal( x,y,z )

**Description:** Sets the current normal. Uses the OpenGL command glNormal.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << LightModel( LIGHT_MODEL_TWO_SIDE, 1 );
shape << Color( 0, 0.0, 0.0 );
shape << Material( Front_and_back, Ambient, 0, 1, 1, 1 );
shape << Material( Front_and_back, Diffuse, 0, 1, 1, 1 );
shape << Material( Front_and_back, Specular, 0, 1, 0, 1 );
shape << Material( Front_and_back, Emission, 0, 0, 0, 1 );
shape << Material( Front_and_back, Shininess, 100 );
shape << Begin( POLYGON );
shape << Normal( 0, 0, 1 );
shape << Color( 1, 0, 0 );
shape << Vertex( -1, 1.5, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -1.5, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -1.5, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 1.5, 0 );
shape << End();
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 2 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [Ortho](#ortho)[](#ortho "Click to copy url")

**Syntax:** obj \<\< Ortho( left,right,bottom,top,near,far )

**Description:** Sets the scene to an orthogonal view. Uses the OpenGL command glOrtho.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Begin( POLYGON );
shape << Color( 1, 0, 0 );
shape << Vertex( -1, 1.5, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -1.5, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -1.5, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 1.5, 0 );
shape << End();
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Ortho( -2, 2, -2, 2, -0.5, 0.5 );
scene << ArcBall( shape, 2 );
scene << update;
```

### [Ortho2D](#ortho2d)[](#ortho2d "Click to copy url")

**Syntax:** obj \<\< Ortho2D( left,right,bottom,top )

**Description:** Sets the scene to a 2D orthogonal view. Uses the OpenGL Utility command gluOrtho2d.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 200, 200 );
New Window( "Example", scene );
scene << Ortho2D( -1, 1, -1, 1 );
scene << Shade Model( SMOOTH );
scene << Begin( TRIANGLES );
scene << color( 1, 0, 0 );
scene << Vertex( -1, -1, 0 );
scene << Color( 0, 1, 0 );
scene << Vertex( 0, 1, 0 );
scene << Color( 0, 0, 1 );
scene << Vertex( 1, -1, 0 );
scene << End();
scene << Update;
```

### [PartialDisk](#partialdisk)[](#partialdisk "Click to copy url")

**Syntax:** obj \<\< PartialDisk( inner radius,outer radius,slices,rings,start angle,sweep angle )

**Description:** Creates a partial disk. Uses the OpenGL Utility command gluPartialDisk.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Color( 0, 0.48, 0.72 );
shape << PartialDisk( 0.5, 1, 2, 3, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << ArcBall( shape, 2 );
scene << Update;
```

### [Perspective](#perspective)[](#perspective "Click to copy url")

**Syntax:** obj \<\< Perspective( angle,z near,z far )

**Description:** Sets the perspective of the view. Uses the OpenGL Utility command gluPerspective.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << color( 0, 0, 1 );
scene << Text( center, baseline, 0.2, "Hello, World." );
```

### [Pick](#pick)[](#pick "Click to copy url")

**Syntax:** name = obj \<\< Pick( x center,y center,pick width,pick height,buffer size,only return the names=0\|1 )

**Description:** Returns the named object that is located under the 2D coordinates of the mouse.

**JMP Version Added:** 16

``` jsl
spheres = Scene Display List();
spheres << Point Size( 50 );
Spheres << PushName( 0 );
For( i = 0, i < 3, i++,
    spheres << LoadName( (i + 1) );
    spheres << PushMatrix;
    spheres << Translate( (i * 0.75 - .75), 0, 0 );
    spheres << color( 1, 0, 0 );
    spheres << Begin( POINTS );
    spheres << Vertex( 0, 0, -.0001 );
    spheres << End;
    spheres << color( 0, 0, 0 );
    spheres << Text( center, middle, 0.2, Char( (i + 1) ) );
    spheres << PopMatrix;
);
spheres << PopName;
view = Scene Box( 500, 400 );
view << Ortho( -1, 1, -1, 1, -2, 2 );
view << CallList( spheres );
view << update;
New Window( "Example", view );
Print( view << Pick( 50, 200, 1, 1, 4, 1 ) );
```

### [PointSize](#pointsize)[](#pointsize "Click to copy url")

**Syntax:** obj \<\< PointSize( size )

**Description:** Sets the size of a point. Uses the OpenGL command glPointSize.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 200, 200 );
New Window( "Example", scene );
scene << pointsize( 1 );
scene << Begin( POINTS );
scene << color( 0, 0, 0 );
scene << Vertex( -.08, 0.04, 0 );
scene << Vertex( -.04, 0.04, 0 );
scene << Vertex( 0, 0.04, 0 );
scene << Vertex( .04, 0.04, 0 );
scene << Vertex( .08, 0.04, 0 );
scene << End();
scene << pointsize( 2 );
scene << Begin( POINTS );
scene << Vertex( -.08, -0.04, 0 );
scene << Vertex( -.04, -0.04, 0 );
scene << Vertex( 0, -0.04, 0 );
scene << Vertex( .04, -0.04, 0 );
scene << Vertex( .08, -0.04, 0 );
scene << End();
```

### [PolygonMode](#polygonmode)[](#polygonmode "Click to copy url")

**Syntax:** obj \<\< PolygonMode( front\|back\|front_and_back,point\|line\|fill )

**Description:** Sets the mode used in rasterization. Uses the OpenGL command glPolygonMode.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << PolygonMode( front, line );
shape << Begin( POLYGON );
shape << Color( 1, 0, 0 );
shape << Vertex( -1, 1.5, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -1.5, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -1.5, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 1.5, 0 );
shape << End();
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Ortho( -2, 2, -2, 2, -2, 2 );
scene << ArcBall( shape, 2 );
scene << update;
```

### [PolygonOffset](#polygonoffset)[](#polygonoffset "Click to copy url")

**Syntax:** obj \<\< PolygonOffset( factor,units )

**Description:** Sets the offset of the polygon. Uses the OpenGL command glPolygonOffset.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Begin( POLYGON );
shape << Color( 1, 0, 0 );
shape << Vertex( -1, 1.5, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -1.5, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -1.5, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 1.5, 1 );
shape << Color( 0, 0, 0 );
shape << Vertex( 1, 1.5, 0 );
shape << End();
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Ortho( -2, 2, -2, 2, -2, 2 );
scene << Enable( Polygon_offset_fill );
scene << PolygonMode( back, point );
scene << ArcBall( shape, 2 );
scene << Disable( Polygon_offset_line );
scene << update;
```

### [PopAttrib](#popattrib)[](#popattrib "Click to copy url")

**Syntax:** obj \<\< PopAttrib

**Description:** Pops the current attributes. Uses the OpenGL command glPopAttrib.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color( 0, 0, 1 );
shape << PushAttrib( GL_CURRENT_BIT );
shape << Color( 0, 0, 0 );
shape << Begin( POLYGON );
shape << Vertex( -1, 0, 0 );
shape << Vertex( 1, 0, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -2, 0 );
shape << Vertex( -1, -2, 0 );
shape << End;
shape << PopAttrib;
shape << Begin( TRIANGLES );
shape << Vertex( -1, 0, 0 );
shape << Vertex( 1, 0, 0 );
shape << Color( 1, 0, 0 );
shape << Vertex( 0, 2, 0 );
shape << End();
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0, 0, -5 );
scene << ArcBall( shape, 2 );
scene << update;
```

### [PopMatrix](#popmatrix)[](#popmatrix "Click to copy url")

**Syntax:** obj \<\< PopMatrix

**Description:** Pops the current matrix. Uses the OpenGL command glPopMatrix.

**JMP Version Added:** 16

``` jsl
object = Scene Display List();
object << PushMatrix;
object << Translate( 0, 0, .1 );
object << Color( 1, 0, 0 );
object << Cylinder( 1, .4, .4, 25, 5 );
object << PopMatrix;
object << PushMatrix;
object << Translate( 0, 0, -.1 );
object << Rotate( 180, 1, 0, 0 );
object << Color( 0, 1, 0 );
object << Cylinder( 1, .4, .4, 25, 5 );
object << PopMatrix;
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << Rotate( -85, 1, 0, 0 );
scene << CallList( object );
scene << Update;
```

### [PopName](#popname)[](#popname "Click to copy url")

**Syntax:** obj \<\< PopName

**Description:** Use with picker, pop the integer that identifies the succeeding object. Uses the OpenGL command glPopName.

**JMP Version Added:** 16

``` jsl
spheres = Scene Display List();
spheres << Point Size( 50 );
Spheres << PushName( 0 );
For( i = 0, i < 3, i++,
    spheres << LoadName( (i + 1) );
    spheres << PushMatrix;
    spheres << Translate( (i * 0.75 - .75), 0, 0 );
    spheres << color( 1, 0, 0 );
    spheres << Begin( POINTS );
    spheres << Vertex( 0, 0, -.0001 );
    spheres << End;
    spheres << color( 0, 0, 0 );
    spheres << Text( center, middle, 0.2, Char( (i + 1) ) );
    spheres << PopMatrix;
);
spheres << PopName;
view = Scene Box( 500, 400 );
view << Ortho( -1, 1, -1, 1, -2, 2 );
view << CallList( spheres );
view << update;
New Window( "Example", view );
Print( view << Pick( 50, 200, 1, 1, 4, 1 ) );
```

### [PushAttrib](#pushattrib)[](#pushattrib "Click to copy url")

**Syntax:** obj \<\< PushAttrib( mask )

**Description:** Pushes the current attributes. Uses the OpenGL command glPushAttrib.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color( 0, 0, 1 );
shape << PushAttrib( GL_CURRENT_BIT );
shape << Color( 0, 0, 0 );
shape << Begin( POLYGON );
shape << Vertex( -1, 0, 0 );
shape << Vertex( 1, 0, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -2, 0 );
shape << Vertex( -1, -2, 0 );
shape << End;
shape << PopAttrib;
shape << Begin( TRIANGLES );
shape << Vertex( -1, 0, 0 );
shape << Vertex( 1, 0, 0 );
shape << Color( 1, 0, 0 );
shape << Vertex( 0, 2, 0 );
shape << End();
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0, 0, -5 );
scene << ArcBall( shape, 2 );
scene << update;
```

### [PushMatrix](#pushmatrix)[](#pushmatrix "Click to copy url")

**Syntax:** obj \<\< PushMatrix

**Description:** Pushes the current matrix. Uses the OpenGL command glPushMatrix.

**JMP Version Added:** 16

``` jsl
object = Scene Display List();
object << PushMatrix;
object << Translate( 0, 0, .1 );
object << Color( 1, 0, 0 );
object << Cylinder( 1, .4, .4, 25, 5 );
object << PopMatrix;
object << PushMatrix;
object << Translate( 0, 0, -.1 );
object << Rotate( 180, 1, 0, 0 );
object << Color( 0, 1, 0 );
object << Cylinder( 1, .4, .4, 25, 5 );
object << PopMatrix;
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << Rotate( -85, 1, 0, 0 );
scene << CallList( object );
scene << Update;
```

### [PushName](#pushname)[](#pushname "Click to copy url")

**Syntax:** obj \<\< PushName( i )

**Description:** Use with picker, push the integer that identifies the succeeding object. Uses the OpenGL command glPushName.

**JMP Version Added:** 16

``` jsl
spheres = Scene Display List();
spheres << Point Size( 50 );
Spheres << PushName( 0 );
For( i = 0, i < 3, i++,
    spheres << LoadName( (i + 1) );
    spheres << PushMatrix;
    spheres << Translate( (i * 0.75 - .75), 0, 0 );
    spheres << color( 1, 0, 0 );
    spheres << Begin( POINTS );
    spheres << Vertex( 0, 0, -.0001 );
    spheres << End;
    spheres << color( 0, 0, 0 );
    spheres << Text( center, middle, 0.2, Char( (i + 1) ) );
    spheres << PopMatrix;
);
spheres << PopName;
view = Scene Box( 500, 400 );
view << Ortho( -1, 1, -1, 1, -2, 2 );
view << CallList( spheres );
view << update;
New Window( "Example", view );
Print( view << Pick( 50, 200, 1, 1, 4, 1 ) );
```

### [QuadricDrawStyle](#quadricdrawstyle)[](#quadricdrawstyle "Click to copy url")

**Syntax:** obj \<\< QuadricDrawStyle( point\|line\|silhouette\|fill )

**Description:** Sets the type of draw style to use for quadrics. Uses the OpenGL Utility command gluQuadricDrawStyle.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << QuadricDrawStyle( LINE );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << update;
```

### [QuadricNormals](#quadricnormals)[](#quadricnormals "Click to copy url")

**Syntax:** obj \<\< QuadricNormals( none\|flat\|smooth )

**Description:** Sets the type of normals to use for quadrics. Uses the OpenGL Utility command gluQuadricNormals.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << QuadricNormals( FLAT );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << update;
```

### [QuadricOrientation](#quadricorientation)[](#quadricorientation "Click to copy url")

**Syntax:** obj \<\< QuadricOrientation( outside\|inside )

**Description:** Sets the type of orientation to use for quadrics. Uses the OpenGL Utility command gluQuadricOrientation.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << QuadricOrientation( INSIDE );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Ambient, 0, 0, 1, 1 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << update;
```

### [QuadricTexture](#quadrictexture)[](#quadrictexture "Click to copy url")

**Syntax:** obj \<\< QuadricTexture

**JMP Version Added:** 16

### [Rect](#rect)[](#rect "Click to copy url")

**Syntax:** obj \<\< Rect( x1,y1,x2,y2 )

**Description:** Creates a rectangle. Uses the OpenGL command glRect.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Color( 0.5, 0, 0 );
shape << Rect( -0.75, -0.75, 0.5, 0.75 );
scene = Scene Box( 200, 200 );
New Window( "Example", scene );
scene << Ortho2D( -1, 1, -1, 1 );
scene << CallList( shape );
```

### [Rotate](#rotate)[](#rotate "Click to copy url")

**Syntax:** obj \<\< Rotate( angle,x,y,z )

**Description:** Multiplies the current matrix by the specified rotation angle in degrees. Uses the OpenGL command glRotate.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << color( 0, 0, 1 );
scene << Rotate( 15, 0, 0, 1 );
scene << Text( center, baseline, 0.2, "Hello, World." );
```

### [Scale](#scale)[](#scale "Click to copy url")

**Syntax:** obj \<\< Scale( x,y,z )

**Description:** Multiplies the current matrix by the specified scale. Uses the OpenGL command glScale.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << color( 0, 0, 1 );
scene << Scale( 2, 1, 1 );
scene << Text( center, baseline, 0.2, "Hello, World." );
```

### [Scissor](#scissor)[](#scissor "Click to copy url")

**Syntax:** obj \<\< Scissor( x,y,width,height )

**Description:** Only items that appear within the scissor view will be drawn. Uses the OpenGL command glScissor.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Color( 1, 0, 0 );
shape << Rect( -0.5, -0.5, 0.5, 0.5 );
scene = Scene Box( 200, 200 );
New Window( "Example", scene );
scene << Scissor( 0, 0, 100, 200 );
scene << Enable( scissor_test );
scene << CallList( shape );
scene << Disable( scissor_test );
```

### [ShadeModel](#shademodel)[](#shademodel "Click to copy url")

**Syntax:** obj \<\< ShadeModel( flat\|smooth )

**Description:** Specifies the type of shading to use for the succeeding objects. Uses the OpenGL command glShadeModel.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 200, 200 );
New Window( "Example", scene );
scene << Ortho2D( -1, 1, -1, 1 );
scene << Shade Model( SMOOTH );
scene << Begin( TRIANGLES );
scene << color( 1, 0, 0 );
scene << Vertex( -1, -1, 0 );
scene << Color( 0, 1, 0 );
scene << Vertex( 0, 1, 0 );
scene << Color( 0, 0, 1 );
scene << Vertex( 1, -1, 0 );
scene << End();
scene << Update;
```

### [Show ArcBall](#show-arcball)[](#show-arcball "Click to copy url")

**Syntax:** obj \<\< Show ArcBall( "During Drag"\|"Always"\|"Never" )

**Description:** Sets the display state of the ArcBall.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << color( 0, 0, 1 );
shape << Text( center, baseline, 0.2, "Hello, World." );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << ArcBall( shape, 1 );
scene << Show ArcBall( always );
scene << Update;
```

### [SortList](#sortlist)[](#sortlist "Click to copy url")

**Syntax:** obj \<\< SortList

**JMP Version Added:** 16

### [Sphere](#sphere)[](#sphere "Click to copy url")

**Syntax:** obj \<\< Sphere( radius,slices,stacks )

**Description:** Creates a sphere. Uses the OpenGL Utility command gluSphere.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
```

### [Suppress Context Menu](#suppress-context-menu)[](#suppress-context-menu "Click to copy url")

**Syntax:** obj \<\< Suppress Context Menu( state=0\|1 )

**Description:** Stops the Scene Box context menu from appearing.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << color( 0, 0, 1 );
shape << Text( center, baseline, 0.2, "Hello, World." );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << ArcBall( shape, 1 );
scene << Update;
scene << Suppress Context Menu( 1 );
```

### [Text](#text)[](#text "Click to copy url")

**Syntax:** obj \<\< Text( left\|center\|right,top\|middle\|baseline\|bottom,size,"string" )

**Description:** Creates text that can be shown in a SceneBox.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( 0.0, 0.0, -4.5 );
scene << color( 0, 0, 1 );
scene << Text( center, baseline, 0.2, "Hello, World." );
```

### [Translate](#translate)[](#translate "Click to copy url")

**Syntax:** obj \<\< Translate( x,y,z )

**Description:** Multiplies the current matrix by the specified translation. Uses the OpenGL command glTranslate.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << Perspective( 45, 3, 7 );
scene << Translate( -0.9, 1.5, -4.5 );
scene << color( 0, 0, 1 );
scene << Text( center, baseline, 0.2, "Hello, World." );
```

### [Update](#update)[](#update "Click to copy url")

**Syntax:** obj \<\< Update

**Description:** Renders the scene.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 500, 500 );
fps = Scene Display List();
window = New Window( "Frames Per Second", scene );
lastTime = 0;
frameCount = 0;
framesPerSecond = "Frames Per Second: ";
While( 1,
    time = Today();
    frameCount++;
    If( time != lastTime,
        framesPerSecond = Char( frameCount );
        frameCount = 0;
        lastTime = time;
    );
    fps << Clear;
    fps << Translate( -1, 0, 0 );
    fps << Color( 1, 0, 0 );
    fps << Text( left, baseline, .1, "Frames Per Second: " || framesPerSecond );
    scene << Clear;
    scene << CallList( fps );
    scene << Update;
    Wait( 0 );
);
```

### [Use Hardware Acceleration](#use-hardware-acceleration)[](#use-hardware-acceleration "Click to copy url")

**Syntax:** obj \<\< Use Hardware Acceleration( state=0\|1 )

**Description:** Hardware Acceleration might make the display faster. If it looks bad, new graphics drivers (from the hardware vendor) might be needed.

**JMP Version Added:** 16

``` jsl
scene = Scene Box( 500, 500 );
fps = Scene Display List();
window = New Window( "Frames Per Second",
    scene,
    accelButton = Button Box( "Turn Hardware Acceleration On", toggleHardwareAccel() )
);
hardwareAccel = 0;
lastTime = 0;
frameCount = 0;
framesPerSecond = "Frames Per Second: ";
toggleHardwareAccel = Function( {},
    hardwareAccel = !hardwareAccel;
    scene << Use Hardware Acceleration( hardwareAccel );
    If( hardwareAccel,
        accelButton << Set Button Name( "Turn Hardware Acceleration Off" ),
        accelButton << Set Button Name( "Turn Hardware Acceleration On" )
    );
);
While( 1,
    time = Today();
    frameCount++;
    If( time != lastTime,
        framesPerSecond = Char( frameCount );
        frameCount = 0;
        lastTime = time;
    );
    fps << Clear;
    fps << Translate( -1, 0, 0 );
    fps << Color( 1, 0, 0 );
    fps << Text( left, baseline, .1, "Frames Per Second: " || framesPerSecond );
    scene << Clear;
    scene << CallList( fps );
    scene << Update;
    Wait( 0 );
);
```

### [Vertex](#vertex)[](#vertex "Click to copy url")

**Syntax:** obj \<\< Vertex( x,y,z )

**Description:** Specifies the vertex of a primitive.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List();
shape << Begin( POLYGON );
shape << Color( 1, 0, 0 );
shape << Vertex( -1, 0.75, 0 );
shape << Color( 0, 0, 1 );
shape << Vertex( -1, -0.75, 0 );
shape << Color( 0, 1, 0 );
shape << Vertex( 1, -0.75, 0 );
shape << Color( 1, 1, 0 );
shape << Vertex( 1, 0.75, 0 );
shape << End();
scene = Scene Box( 200, 200 );
scene << CallList( shape );
New Window( "Example", scene );
```

### [Width](#width)[](#width "Click to copy url")

**Syntax:** obj \<\< Width( pixels )

**Description:** Sets the width of the box.

**JMP Version Added:** 16

``` jsl
shape = Scene Display List( 0 );
shape << Enable( COLOR_MATERIAL );
shape << Color( 0, 0.48, 0.72 );
shape << Material( Front, Diffuse, 0, 1, 1, 1 );
shape << Material( Front, Specular, 0, 1, 0, 1 );
shape << Material( Front, Emission, 0, 0, 0, 1 );
shape << Material( Front, Shininess, 100 );
shape << Sphere( 1.5, 50, 50 );
shape << Disable( COLOR_MATERIAL );
scene = Scene Box( 400, 400 );
New Window( "Example", scene );
scene << clear;
scene << Perspective( 45, 1, 10 );
scene << Translate( 0.0, 0.0, -5 );
scene << Enable( Lighting );
scene << Enable( Light0 );
scene << Light( Light0, Position, 1, 1, 1, 0 );
scene << ArcBall( shape, 3 );
scene << Disable( Light0 );
scene << Disable( Lighting );
scene << update;
scene << Width( 150 );
```

## [Shared Item Messages](#shared-item-messages)[](#shared-item-messages "Click to copy url")

### [Add Line Annotation](#add-line-annotation)[](#add-line-annotation "Click to copy url")

**Syntax:** obj \<\< Add Line Annotation

**Description:** Adds a line on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Line Annotation( Line( 160, 235, 240, 235 ) );
```

### [Add Pin Annotation](#add-pin-annotation)[](#add-pin-annotation "Click to copy url")

**Syntax:** obj \<\< Add Pin Annotation

**Description:** Adds a pinned annotation on top of a display box. Most attributes (such as Index Row, UniqueID and FoundPt) are designed for internal use only.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Bivariate(
    Y( :weight ),
    X( :height ),
    SendToReport(
        Dispatch( {}, "Bivar Plot", FrameBox,
            Add Pin Annotation(
                Seg( Marker Seg( 1 ) ),
                Index( 17 ),
                Index Row( 17 ),
                UniqueID( -960001792 ),
                FoundPt( {238, 219} ),
                Origin( {64.9765625, 142} ),
                Offset( {-174, -40} ),
                Tag Line( 1 ),
                Font( "Helvetica", 11, "Plain" )
            )
        )
    )
);
```

### [Add Polygon Annotation](#add-polygon-annotation)[](#add-polygon-annotation "Click to copy url")

**Syntax:** obj \<\< Add Polygon Annotation

**Description:** Adds a polygon on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Polygon Annotation(
    Points( {210, 80}, {230, 70}, {280, 115}, {240, 120} ),
    Color( "Red" ),
    Closed( 1 )
);
```

### [Add Simple Shape Annotation](#add-simple-shape-annotation)[](#add-simple-shape-annotation "Click to copy url")

**Syntax:** obj \<\< Add Simple Shape Annotation

**Description:** Adds a simple shape on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Simple Shape Annotation( Oval( 210, 100, 250, 75 ) );
rbiv << Add Simple Shape Annotation( Rectangle( 70, 180, 95, 215 ) );
```

### [Add Text Annotation](#add-text-annotation)[](#add-text-annotation "Click to copy url")

**Syntax:** obj \<\< Add Text Annotation

**Description:** Adds text on top of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Text Annotation(
    Text( "We need to discuss this at the next meeting." ),
    Text Box( {65, 35, 200, 77} )
);
```

### [Append](#append)[](#append "Click to copy url")

**Syntax:** obj \<\< Append( db2 )

**Description:** Add db2 to the display tree after db.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << append( Text Box( "=== below ===" ) );
```

### [Border](#border)[](#border "Click to copy url")

**Syntax:** obj \<\< Border( sides ); sides = obj \<\< Get Border

**Description:** Borders are solid lines drawn around the outside of a display box. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical borders.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Border );
Wait( 1 );
tb << Border( 1 );
```

### [Border Color](#border-color)[](#border-color "Click to copy url")

**Syntax:** obj \<\< Border Color( color ); color = obj \<\< Get Border Color

**Description:** Optional color to override the default color for box borders.

**JMP Version Added:** 19

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Wait( 2 );
tb << Border( 1 );
tb << Border Color( "Light Red" );
```

### [Bring Window To Front](#bring-window-to-front)[](#bring-window-to-front "Click to copy url")

**Syntax:** obj \<\< Bring Window To Front

**Description:** Brings the window to the front.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Run Script( "Bivariate" );
w << Bring Window To Front;
```

### [Child](#child)[](#child "Click to copy url")

**Syntax:** obj \<\< Child

**Description:** Returns the child of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisParent = axisbox << parent();
axisChild = axisParent << child();
Print( axisChild << Class Name() );
```

### [Class Name](#class-name)[](#class-name "Click to copy url")

**Syntax:** obj \<\< Class Name

**Description:** Returns the name of the display class for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisbox << Class Name();
```

### [Clone Box](#clone-box)[](#clone-box "Click to copy url")

**Syntax:** obj \<\< Clone Box

**Description:** Makes a new copy of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << append( Text Box( "=== below ===" ) );
clonedBox = rbiv << Clone Box();
rbiv << append( clonedBox );
```

### [Close Window](#close-window)[](#close-window "Click to copy url")

**Syntax:** obj \<\< Close Window( \<"NoSave"\> )

**Description:** Closes the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
w << Close Window;
```

### [Copy Data](#copy-data)[](#copy-data "Click to copy url")

**Syntax:** obj \<\< Copy Data

**Description:** copies the tab-delimited data from a matrix or table to the clip board.

``` jsl
New Window( "x", mat = Matrix Box( [1 2 3, 4 5 6, 7 8 9] ) );
mat << CopyData;
```

### [Copy Graph](#copy-graph)[](#copy-graph "Click to copy url")

**Syntax:** obj \<\< Copy Graph

**Description:** Puts a picture of the graph and axes on the clipboard.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
(rbiv[FrameBox( 1 )]) << Copy Graph();
"paste into a paint program";
```

### [Copy Picture](#copy-picture)[](#copy-picture "Click to copy url")

**Syntax:** obj \<\< Copy Picture

**Description:** Puts a picture of the display box on the clipboard.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Copy Picture();
```

### [Delete Box](#delete-box)[](#delete-box "Click to copy url")

**Syntax:** obj \<\< Delete Box

**Description:** Delete the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisbox << Delete Box();
```

### [Deselect](#deselect)[](#deselect "Click to copy url")

**Syntax:** obj \<\< Deselect

**Description:** Deselects this object for use by Edit menu commands.

``` jsl
//This message applies to all display box objects
selected = 0;
New Window( "Example",
    ex = Button Box( "Press Me",
        selected = !selected;
        refresh;
    )
);
refresh = Function( {},
    If( selected,
        ex << Select,
        ex << Deselect
    )
);
```

### [Dispatch](#dispatch)[](#dispatch "Click to copy url")

**Syntax:** obj \<\< Dispatch( {outline node, ...}, display element, display element type, command )

**Description:** Send command to a specific part of a display tree.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Dispatch( {}, "Bivar Plot", FrameBox, {Marker Size( 3 )} );
```

### [Enabled](#enabled)[](#enabled "Click to copy url")

**Syntax:** obj \<\< Enabled( state=0\|1 ); state = obj \<\< Get Enabled

**Description:** An object that is not enabled will not respond to keyboard or mouse input. This property is inherited by child objects, so a container object that is disabled will cause all descendent objects to be disabled.

``` jsl
//This message applies to all display objects
New Window( "enabled",
    V List Box(
        check = Check Box(
            {"Use Password"},
            ptext << Enabled( check << Get( 1 ) );
            pvalue << Enabled( check << Get( 1 ) );
        ),
        Lineup Box( N Col( 2 ),
            Text Box( "Username:" ),
            Text Edit Box( "", <<Set Width( 100 ) ),
            ptext = Text Box( "Password:", <<Enabled( 0 ) ),
            pvalue = Text Edit Box( "",
                <<Password Style( 1 ),
                <<Set Width( 20 ),
                <<Enabled( 0 )
            )
        )
    )
);
```

### [Find](#find)[](#find "Click to copy url")

**Syntax:** obj \<\< Find

**Description:** Returns a display box with the given argument.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv << Find( axis box( 1 ) );
axisbox << Delete();
```

### [Get Annotation](#get-annotation)[](#get-annotation "Click to copy url")

**Syntax:** obj \<\< Get Annotation

**Description:** Returns the first annotation that is anchored to this display box. Other annotations can be accessed by using Sib() on the result.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Add Text Annotation(
    Text( "We need to discuss this at the next meeting." ),
    Text Box( {65, 35, 200, 77} )
);
annotation = rbiv << Get Annotation;
annotation << delete;
```

### [Get Border](#get-border)[](#get-border "Click to copy url")

**Syntax:** obj \<\< Border( sides ); sides = obj \<\< Get Border

**Description:** Borders are solid lines drawn around the outside of a display box. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical borders.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Border );
Wait( 1 );
tb << Border( 1 );
```

### [Get Border Color](#get-border-color)[](#get-border-color "Click to copy url")

**Syntax:** obj \<\< Border Color( color ); color = obj \<\< Get Border Color

**Description:** Optional color to override the default color for box borders.

**JMP Version Added:** 19

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Wait( 2 );
tb << Border( 1 );
tb << Border Color( "Light Red" );
```

### [Get Content Size](#get-content-size)[](#get-content-size "Click to copy url")

**Syntax:** obj \<\< Get Content Size

**Description:** Returns the content size within the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
c = w << Get Content Size();
Show( c );
```

### [Get Display Path](#get-display-path)[](#get-display-path "Click to copy url")

**Syntax:** obj \<\< Get Display Path( parent box, \<receiver expr\>, \<Mode("XPath"\|"Subscript")\> )

**Description:** Gets a relatively robust expression to navigate between parent box and obj. This path is not guaranteed to be stable across JMP releases. The receiver expr is incorporated into the output expression if provided. If not, the expression provided for parent box is used instead. As shown in the example, this message is mainly useful for increasing the robustness of a path you already have available. The XPath mode is default.

#### [Basic](#basic)[](#basic "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
rpt = Report( biv );
xpath expr = rpt[Number Col Box( 9 )] << Get Display Path( rpt, Expr( Report( biv ) ) ); // Make Number Col Box(9) more robust
Show( xpath expr );
xpath expr << Select;
```

#### [Subscript Mode](#subscript-mode)[](#subscript-mode "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
rpt = Report( biv );
subscript expr = rpt[Number Col Box( 9 )] << Get Display Path( rpt, Mode( "Subscript" ) ); // Make Number Col Box(9) more robust
Show( subscript expr );
subscript expr << Select;
```

### [Get Enabled](#get-enabled)[](#get-enabled "Click to copy url")

**Syntax:** obj \<\< Enabled( state=0\|1 ); state = obj \<\< Get Enabled

**Description:** An object that is not enabled will not respond to keyboard or mouse input. This property is inherited by child objects, so a container object that is disabled will cause all descendent objects to be disabled.

``` jsl
//This message applies to all display objects
New Window( "enabled",
    V List Box(
        check = Check Box(
            {"Use Password"},
            ptext << Enabled( check << Get( 1 ) );
            pvalue << Enabled( check << Get( 1 ) );
        ),
        Lineup Box( N Col( 2 ),
            Text Box( "Username:" ),
            Text Edit Box( "", <<Set Width( 100 ) ),
            ptext = Text Box( "Password:", <<Enabled( 0 ) ),
            pvalue = Text Edit Box( "",
                <<Password Style( 1 ),
                <<Set Width( 20 ),
                <<Enabled( 0 )
            )
        )
    )
);
```

### [Get HTML](#get-html)[](#get-html "Click to copy url")

**Syntax:** obj \<\< Get HTML( \<format\> )

**Description:** Returns a string containing HTML source for the display box.

**Example 1**

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << Set Text( win << Get HTML );
```

**Example 2**

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), Means( 1 ), Mean Diamonds( 1 ) );
Save Text File( "$TEMP/Oneway.html", obj << Get HTML( "svg" ) ); // Prefer <<Save HTML
Web( "$TEMP/Oneway.html", JMPWindow );
```

### [Get Height](#get-height)[](#get-height "Click to copy url")

**Syntax:** width = obj \<\< Get Height

**Description:** Returns the height of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Height;
```

### [Get Horizontal Alignment](#get-horizontal-alignment)[](#get-horizontal-alignment "Click to copy url")

**Syntax:** obj \<\< Horizontal Alignment( "Default"\|"Left"\|"Center"\|"Right" ); "Default"\|"Left"\|"Center"\|"Right" = obj \<\< Get Horizontal Alignment

**Description:** Horizontal alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Border( 1 );
Wait( 2 );
lb << Horizontal Alignment( "Right" );
```

### [Get Journal](#get-journal)[](#get-journal "Click to copy url")

**Syntax:** obj \<\< Get Journal

**Description:** Returns a string containing journal source for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
Print( rbiv << Get Journal );
```

### [Get Margin](#get-margin)[](#get-margin "Click to copy url")

**Syntax:** obj \<\< Margin( sides ); sides = obj \<\< Get Margin

**Description:** Margin adds space between the border of the box and adjacent boxes. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical margins.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Margin );
tb << Border( 1 );
Wait( 2 );
tb << Margin( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Get Max Size](#get-max-size)[](#get-max-size "Click to copy url")

**Syntax:** width,height = obj \<\< Get Max Size

**Description:** Returns the maximum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Max Size;
```

### [Get Min Size](#get-min-size)[](#get-min-size "Click to copy url")

**Syntax:** width,height = obj \<\< Get Min Size

**Description:** Returns the minimum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Get Min Size;
```

### [Get Namespace](#get-namespace)[](#get-namespace "Click to copy url")

**Syntax:** obj \<\< Get Namespace

**Description:** Returns the namespace associated with this display object.

``` jsl
//This message applies to all display objects
x = 1;
w = New Window( "Test", b = Button Box( "Press me" ) );
b:x = 2;
ns = b << GetNamespace();
Show( ns:x, x );
```

### [Get On Close](#get-on-close)[](#get-on-close "Click to copy url")

**Syntax:** obj \<\< Get On Close

**Description:** Returns the script or function that will run when the window closes.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << On Close(
    // Modal dialogs return Button(1) if OK is pressed, Button(-1) if canceled
    New Window( "Are you sure?",
        <<modal,
        V List Box(
            Text Box( "Press OK to allow the window to close" ),
            H List Box( Button Box( "OK" ), Button Box( "Cancel" ) )
        )
    )["button"] == 1
);
Show( w << Get On Close );
```

### [Get Padding](#get-padding)[](#get-padding "Click to copy url")

**Syntax:** obj \<\< Padding( sides ); sides = obj \<\< Get Padding

**Description:** Padding adds space between the content and the border of the box. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical padding.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Padding );
tb << Border( 1 );
Wait( 1 );
tb << Padding( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Get Page Setup](#get-page-setup)[](#get-page-setup "Click to copy url")

**Syntax:** obj \<\< Get Page Setup

**Description:** Get page setup information for PDF

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Page Setup Test" ) );
w << get page setup();
```

### [Get Picture](#get-picture)[](#get-picture "Click to copy url")

**Syntax:** obj \<\< Get Picture( \<Scale(factor)\>, \<Type("Bitmap" \| "Scalable")\>, \<View("Picture" \| "Screen" \| "Print"), \<Appearance("Default" \| "Current")\>, \<SubRect(Left(number), Top(number), Right(number), Bottom(number))\> )

**Description:** Captures db as an Image Object. The optional Scale argument will render the image at a scaled resolution. Scaling requires that the display box be stretchable. The Type argument determines whether the result will be a scalable vector image or a bitmap. By default a scalable image is returned, which is suitable for saving to vector formats like PDF. The View option changes the behavior of some boxes. The default option of "Picture" draws the report as it would when exporting to an image format, with scrolled areas fully shown. View mode of "Screen" draws the report as seen on-screen, and "Print" draws the report as it does when printing, without any of the page setup features. The SubRect option will capture a portion of the resulting image rather than a full image. The Appearance option can change from the "Default" output colors to the "Current" colors as seen on-screen. The View, SubRect, and Appearance options are only supported for Type "Bitmap".

#### [Default](#default)[](#default "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
New Window( "Example", rbiv << Get Picture );
```

#### [Scale](#scale_1)[](#scale_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv[FrameBox( 1 )] << Set Stretch( "Window", "Window" );
New Window( "Example", rbiv << Get Picture( Scale( 1.5 ) ) );
```

#### [View and Appearance](#view-and-appearance)[](#view-and-appearance "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate(
    Y( :weight ),
    X( :height ),
    Fit Line( {Line Color( {212, 73, 88} )} ),
    Fit Polynomial( 3, {Line Color( {61, 174, 70} )} ),
    Kernel Smoother( 1, 1, 0.5, 0 )
);
rbiv = biv << report;
rbiv[FrameBox( 1 )] << Set Stretch( "Window", "Window" );
New Window( "Example",
    H List Box(
        rbiv << Get Picture( View( "Screen" ), Appearance( "Current" ) ),
        rbiv << Get Picture( View( "Print" ), Appearance( "Default" ) )
    )
);
```

### [Get Project](#get-project)[](#get-project "Click to copy url")

**Syntax:** project = obj \<\< Get Project()

**Description:** Returns the parent project of the window, or Empty() if it is not in a project.

**JMP Version Added:** 14

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
c = w << Get Project();
Show( c );
```

### [Get Properties](#get-properties)[](#get-properties "Click to copy url")

**Syntax:** obj \<\< Get Properties

**Description:** Returns an associative array that contains the display box's properties and their values.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Get Properties;
```

### [Get Property](#get-property)[](#get-property "Click to copy url")

**Syntax:** obj \<\< Get Property( "property" )

**Description:** Returns the current setting for the named property.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Get Property( "Enabled" );
```

### [Get Property List](#get-property-list)[](#get-property-list "Click to copy url")

**Syntax:** obj \<\< Get Property List

**Description:** Returns a list of properties the display box has.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Get Property List;
```

### [Get RTF](#get-rtf)[](#get-rtf "Click to copy url")

**Syntax:** obj \<\< Get RTF( \<format\> )

**Description:** Returns a string containing RTF source for the display box.

**Example 1**

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << Set Text( win << Get RTF );
```

**Example 2**

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), Means( 1 ), Mean Diamonds( 1 ) );
Save Text File( "$TEMP/Oneway.rtf", obj << Get RTF( "png" ) ); // Prefer <<Save RTF
Open( "$TEMP/Oneway.rtf" );
```

### [Get Row States](#get-row-states)[](#get-row-states "Click to copy url")

**Syntax:** rs = obj \<\< Get Row States( \<dt\> )

**Description:** Returns a vector containing the row state for every row in the given data table or the current data table. The row states can come from the table, or from the filter context of the box.

#### [Single table](#single-table)[](#single-table "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    Data Filter Context Box(
        H List Box(
            dt << Data Filter(
                Local,
                Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
                Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
            ),
            V List Box(
                t = Text Box( "0 Rows Excluded" ),
                Distribution(
                    Continuous Distribution( Column( :weight ) ),
                    Nominal Distribution( Column( :age ) )
                )
            )
        )
    )
);
updatetext = Function( {},
    rs = t << Get Row States( dt );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = t << Make Row State Handler( dt, rsupdate );
updatetext();
```

#### [Where subset](#where-subset)[](#where-subset "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    t = Text Box( "0 Rows Excluded" ),
    dist = Distribution(
        Continuous Distribution( Column( :weight ) ),
        Nominal Distribution( Column( :age ) ),
        Local Data Filter(
            Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
            Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
        ),
        Where( :sex == "F" )
    )
);
subset = dist << Get Data Table();
updatetext = Function( {},
    rs = Report( dist ) << Get Row States( subset );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = Report( dist ) << Make Row State Handler( subset, rsupdate );
updatetext();
```

### [Get Show Window](#get-show-window)[](#get-show-window "Click to copy url")

**Syntax:** obj \<\< Get Show Window

**Description:** Returns the visibility of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Show Window( 0 );
Wait( 2 );
Print( w << Get Show Window() );
```

### [Get Size](#get-size)[](#get-size "Click to copy url")

**Syntax:** width,height = obj \<\< Get Size

**Description:** Returns the size of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
Print( fb << Get Size );
```

### [Get Stretch](#get-stretch)[](#get-stretch "Click to copy url")

**Syntax:** x,y = obj \<\< Get Stretch

**Description:** Returns the stretching flags for this display box in the horizontal and vertical directions.

**JMP Version Added:** 16

``` jsl
//This message applies to all display box objects
New Window( "Stretch",
    V List Box(
        H List Box( Text Edit Box( "String1" ), Text Edit Box( "String2" ) ),
        spacer = Spacer Box(
            Size( 20, 20 ),
            Color( "Light Red" ),
            <<Set Stretch( "Fill", "Off" )
        )
    )
);
spacer << Get Stretch();
```

### [Get Text](#get-text)[](#get-text "Click to copy url")

**Syntax:** obj \<\< Get Text

**Description:** Returns a string containing the text of the display box.

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << Set Text( win << Get Text );
```

### [Get Text Color](#get-text-color)[](#get-text-color "Click to copy url")

**Syntax:** obj \<\< Text Color( color ); color = obj \<\< Get Text Color

**Description:** Text will be drawn using the text color if it has been set. If the property has not been set, the box will inherit the text color of the containing box.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Text Color );
Wait( 2 );
tb << Text Color( "Red" );
```

### [Get UI Only](#get-ui-only)[](#get-ui-only "Click to copy url")

**Syntax:** obj \<\< UI Only( state=0\|1 ); state = obj \<\< Get UI Only

### [Get Vertical Alignment](#get-vertical-alignment)[](#get-vertical-alignment "Click to copy url")

**Syntax:** obj \<\< Vertical Alignment( "Default"\|"Top"\|"Center"\|"Bottom" ); "Default"\|"Top"\|"Center"\|"Bottom" = obj \<\< Get Vertical Alignment

**Description:** Vertical alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Set Horizontal( 1 );
lb = r[List Box( 7 )];
lb << Border( 1 );
Wait( 2 );
lb << Vertical Alignment( "Bottom" );
```

### [Get Visibility](#get-visibility)[](#get-visibility "Click to copy url")

**Syntax:** obj \<\< Visibility( "Visible"\|"Hidden"\|"Collapse" ); "Visible"\|"Hidden"\|"Collapse" = obj \<\< Get Visibility

**Description:** Visibility determines whether a box is shown and whether it takes up space. The default value of "Visible" means that the object will be shown. A "Hidden" box is not shown but still takes up space, while a "Collapsed" box takes up no space in the layout.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Visibility );
Wait( 1 );
tb << Visibility( "Collapse" );
Show( tb << Get Visibility );
```

### [Get Web Support](#get-web-support)[](#get-web-support "Click to copy url")

**Syntax:** obj \<\< Get Web Support

**Description:** Return a number indicating the level of Interactive HTML support for the display object. 1 means some or all elements are supported. 0 means no support.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = Bivariate( Y( :Weight ), X( :Height ) );
s = obj << Get Web Support();
Show( s );
```

### [Get Window Icon](#get-window-icon)[](#get-window-icon "Click to copy url")

**Syntax:** obj \<\< Get Window Icon

**Description:** Returns the window icon.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
t = w << Get Window Icon;
Show( t );
```

### [Get Window Position](#get-window-position)[](#get-window-position "Click to copy url")

**Syntax:** obj \<\< Get Window Position

**Description:** Returns the position of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
p = w << Get Window Position();
Show( p );
```

### [Get Window Size](#get-window-size)[](#get-window-size "Click to copy url")

**Syntax:** obj \<\< Get Window Size

**Description:** Returns the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
s = w << Get Window Size();
Show( s );
```

### [Get Window Title](#get-window-title)[](#get-window-title "Click to copy url")

**Syntax:** obj \<\< Get Window Title

**Description:** Returns the window title.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
t = w << Get Window Title;
Show( t );
```

### [Get Window View](#get-window-view)[](#get-window-view "Click to copy url")

**Syntax:** obj \<\< Get Window View

**Description:** Returns the current window view. Windows can be "Visible", "Invisible", or "Private".

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Print( w << Get Window View() );
```

### [Get XML](#get-xml)[](#get-xml "Click to copy url")

**Syntax:** obj \<\< Get XML( \<English(0\|1)\>, \<NoData(0\|1)\> )

**Description:** Retrieves the display tree formatted as XML. By default, strings are returned in the local language, and the XML includes data values within some boxes. Use the English option to return English strings where available. Use the NoData option to omit the data values within boxes, which can be very large for some display trees.

``` jsl
//This message applies to all display box objects
win = New Window( "test", a = Text Box( "my test" ) );
a << set text( win << get xml );
```

### [GetOffset](#getoffset)[](#getoffset "Click to copy url")

**Syntax:** x,y = obj \<\< GetOffset

**Description:** Returns the offset of this display box relative to the parent box. You might need to use the \<\<parent message in a loop to accumulate several offsets.

``` jsl
New Window( "example",
    MouseBox(
        Graph Box(
            title( "title" ),
            Pen Size( 3 );
            Y Function( -3 + 100 / 2 * (1 + Sin( (2 * Pi() * (x + .3)) / 100 )), x );
        ),
        <<settrackenable( 1 ) // put the mouse box to work, watching "tracking"
    ,
        <<settrack( // events from the mouse (movement, with button up or down)
            Function( {this, pt}, // parameters: this is the mousebox, pt is mouse x,y
                {fb, offset, t, off, size}, // local variables
                // recalulate offset and size each time, the values can change
                fb = this[framebox( 1 )]; // the framebox in the graph 
                offset = [0, 0]; // accumulator to sum up the offset between framebox and mousebox
                t = fb; // a temporary box that starts at the frame 
                While( t != this, // and walks up to the mousebox
                    off = t << getOffset; // ask each box for its offset to the immediate parent
                    offset += Matrix( off ); // convert list answer to matrix so + will work
                    t = t << parent; // crawl up to the mousebox, one box at a time
                );
                size = Matrix( fb << getSize ); // the frame knows its size
                If( // over the frame box
                    offset[1] < pt[1] < offset[1] + size[1] & offset[2] < pt[2] < offset[2]
                     + size[2]
                ,
                    fb << setbackgroundcolor( "red" ),
                    fb << setbackgroundcolor( "blue" )
                );
            )
        )
    )
);
```

### [Horizontal Alignment](#horizontal-alignment)[](#horizontal-alignment "Click to copy url")

**Syntax:** obj \<\< Horizontal Alignment( "Default"\|"Left"\|"Center"\|"Right" ); "Default"\|"Left"\|"Center"\|"Right" = obj \<\< Get Horizontal Alignment

**Description:** Horizontal alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Border( 1 );
Wait( 2 );
lb << Horizontal Alignment( "Right" );
```

### [Inval](#inval)[](#inval "Click to copy url")

**Syntax:** obj \<\< Inval

**Description:** Invalidate the displaybox. The window will update when either the \<\<UpdateWindow message is sent or the operating system has time for the update.

``` jsl
//This message applies to all display box objects
color = "green"; /* initial color in a variable */
New Window( "Inval example",
    Button Box( "red",
        color = "red";
        g1 << inval; /* tell the oval to redraw */
        g2 << inval; /* tell the rectangle to redraw */
        g1 << updateWindow; /* tell the window to update immediately */
        // this is a busy-wait to help demonstrate the various behaviors...
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 /* delay without wait(.5) */ );
    ),
    Button Box( "blue",
        color = "blue";
        g1 << inval; /* same comments */
        g2 << inval;
        g1 << updateWindow;
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 );
    ),
    g1 = Graph Box(/* the graph does NOT watch for the color variable to change 
                      but will use the current value of color when it reshows */
        Fill Color( color );
        Oval( 10, 80, 70, 50, 1 );
    ),
    g2 = Graph Box(
        Fill Color( color );
        Rect( 10, 80, 70, 50, 1 );
    )
);
```

### [Is Dirty](#is-dirty)[](#is-dirty "Click to copy url")

**Syntax:** obj \<\< Is Dirty

**Description:** Gets the document's modified status. 1 means the document has been modified and will prompt for saving; 0 means the document is not modified.

**JMP Version Added:** 14

``` jsl

ww = New Window( "Test", <<Script, "Open(\!"$SAMPLE_DATA\Big Class.jmp\!");" );
Show( ww << Is Dirty );
ww << Set Dirty( 0 );
Show( ww << Is Dirty );
```

### [Is Modal Dialog](#is-modal-dialog)[](#is-modal-dialog "Click to copy url")

**Syntax:** obj \<\< Is Modal Dialog

**Description:** Returns true if the window is a modal dialog. Only useful when called from a window handler callback.

``` jsl
With Window Handler(
    New Window( "Modal Window", <<Modal ),
    Function( {win},
        Print( win << Is Modal Dialog() );
        win << close window();
    )
);
```

### [Journal](#journal)[](#journal "Click to copy url")

**Syntax:** obj \<\< Journal

**Description:** Makes a journal from the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << journal;
```

### [Journal Window](#journal-window)[](#journal-window "Click to copy url")

**Syntax:** obj \<\< Journal Window

**Description:** Opens a journal window of the window.

``` jsl
//This message applies to all display box objects
w = New Window( "Main Window", Text Box( "Main JMP Window" ) );
w << Journal Window;
```

### [Launch](#launch)[](#launch "Click to copy url")

**Syntax:** obj \<\< Launch

**Description:** Evaluates the given argument in the context of the display box.

``` jsl
//This message applies to all display box objects
Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "example",
    ob1 = Outline Box( "treemap launcher" ),
    ob2 = Outline Box( "bivariate partial" ),
    ob3 = Outline Box( "bivariate launched" )
);
ob1 << launch( Treemap() );
ob2 << launch( Bivariate( Y( :height ) ) );
ob3 << launch( Bivariate( Y( :height ), X( :weight ) ) );
```

### [Make RowState Handler](#make-rowstate-handler)[](#make-rowstate-handler "Click to copy url")

**Syntax:** rs = obj \<\< Make RowState Handler( \<dt\>, function(a) )

**Description:** Creates a row state handler for the given data table or the current data table. The function is called when the row states change in the filter context of the box. The argument of the function holds the rows numbers that have changed, or -1 if the row state filter has changed.

#### [Single table](#single-table_1)[](#single-table_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    Data Filter Context Box(
        H List Box(
            dt << Data Filter(
                Local,
                Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
                Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
            ),
            V List Box(
                t = Text Box( "0 Rows Excluded" ),
                Distribution(
                    Continuous Distribution( Column( :weight ) ),
                    Nominal Distribution( Column( :age ) )
                )
            )
        )
    )
);
updatetext = Function( {},
    rs = t << Get Row States( dt );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = t << Make Row State Handler( dt, rsupdate );
updatetext();
```

#### [Where subset](#where-subset_1)[](#where-subset_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
New Window( "filter test",
    t = Text Box( "0 Rows Excluded" ),
    dist = Distribution(
        Continuous Distribution( Column( :weight ) ),
        Nominal Distribution( Column( :age ) ),
        Local Data Filter(
            Add Filter( columns( :height ), Where( :height >= 51 & :height <= 62 ) ),
            Mode( Select( 0 ), Show( 1 ), Include( 1 ) )
        ),
        Where( :sex == "F" )
    )
);
subset = dist << Get Data Table();
updatetext = Function( {},
    rs = Report( dist ) << Get Row States( subset );
    n = 0;
    For( ii = 1, ii <= N Rows( rs ), ii++,
        If( Excluded( As Row State( rs[ii] ) ),
            n
            ++)
    );
    t << Set Text( Char( n ) || " Rows Excluded" );
);
rsupdate = Function( {a},
    If( Is Matrix( a ),
        updatetext()
    )
);
rsh = Report( dist ) << Make Row State Handler( subset, rsupdate );
updatetext();
```

### [Margin](#margin)[](#margin "Click to copy url")

**Syntax:** obj \<\< Margin( sides ); sides = obj \<\< Get Margin

**Description:** Margin adds space between the border of the box and adjacent boxes. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical margins.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Margin );
tb << Border( 1 );
Wait( 2 );
tb << Margin( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Maximize Window](#maximize-window)[](#maximize-window "Click to copy url")

**Syntax:** obj \<\< Maximize Window( \<state=0\|1\> )

**Description:** Maximizes the window. Default argument is 1.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Maximize Window( 1 );
Wait( 1 );
w << Maximize Window( 0 );
```

### [Minimize Window](#minimize-window)[](#minimize-window "Click to copy url")

**Syntax:** obj \<\< Minimize Window( \<state=0\|1\> )

**Description:** Minimizes the window. Default argument is 1.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Minimize Window( 1 );
Wait( 1 );
w << Minimize Window( 0 );
```

### [Move Window](#move-window)[](#move-window "Click to copy url")

**Syntax:** obj \<\< Move Window( x,y )

**Description:** Moves the window to the specified position.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 2 );
w << Move Window( 500, 500 );
```

### [Next](#next)[](#next "Click to copy url")

**Syntax:** obj \<\< Next

**Description:** Returns the display box after this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
next = rbiv << Next();
Print( next << Class Name() );
```

### [On Close](#on-close)[](#on-close "Click to copy url")

**Syntax:** obj \<\< On Close( script )

**Description:** Sets a script or function to run upon closing the window. This script should return 1 to allow the close, or 0 to prevent the window from closing.

#### [Close Function](#close-function)[](#close-function "Click to copy url")

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << On Close(
    Function( {this}, 
        // Modal dialogs return Button(1) if OK is pressed, Button(-1) if cancelled
        New Window( "Are you sure?",
            <<modal,
            V List Box(
                Text Box( "Press OK to allow " || (this << Get Window Title) || " to close" ),
                H List Box( Button Box( "OK" ), Button Box( "Cancel" ) )
            )
        )["button"] == 1
    )
);
```

#### [Close Script](#close-script)[](#close-script "Click to copy url")

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << On Close(
    // Modal dialogs return Button(1) if OK is pressed, Button(-1) if canceled
    New Window( "Are you sure?",
        <<modal,
        V List Box(
            Text Box( "Press OK to allow the window to close" ),
            H List Box( Button Box( "OK" ), Button Box( "Cancel" ) )
        )
    )["button"] == 1
);
```

### [Optimize Display](#optimize-display)[](#optimize-display "Click to copy url")

**Syntax:** obj \<\< Optimize Display

**Description:** Sets a data table's column widths and window to an optimum size.

**JMP Version Added:** 14

``` jsl
//This message applies to Data Table objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Optimize Display;
```

### [Pad Window](#pad-window)[](#pad-window "Click to copy url")

**Syntax:** obj \<\< Pad Window( bool )

**Description:** Turns window padding on or off.

``` jsl
//This message applies to all display box objects
Open( "$SAMPLE_DATA/Big Class.jmp" );
d = distribution( Column( :height ) );
r = d << report;
r << Pad Window( 0 );
```

### [Padding](#padding)[](#padding "Click to copy url")

**Syntax:** obj \<\< Padding( sides ); sides = obj \<\< Get Padding

**Description:** Padding adds space between the content and the border of the box. Use named arguments, or provide a list of values. If a single value is provided, it will be applied to all sides. If two values are specified, they will be applied to horizontal and vertical padding.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Padding );
tb << Border( 1 );
Wait( 1 );
tb << Padding( Left( 20 ), Top( 20 ), Right( 20 ), Bottom( 20 ) );
```

### [Page Break](#page-break)[](#page-break "Click to copy url")

**Syntax:** obj \<\< Page Break

**Description:** Inserts a page break before the display box.

``` jsl
//This message applies to all display box objects
New Window( "Example",
    ob = Outline Box( "Outline Box",
        V List Box(
            ob2 = Outline Box( "Outline Box 2",
                H List Box( Text Edit Box( "Top Left" ), Text Edit Box( "Top Right" ) )
            ),
            ob3 = Outline Box( "Outline Box",
                H List Box( Text Edit Box( "Bottom Left" ), Text Edit Box( "Bottom Right" ) )
            )
        )
    )
);
ob3 << Page Break;
```

### [Parent](#parent)[](#parent "Click to copy url")

**Syntax:** obj \<\< Parent

**Description:** Returns the parent of this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisParent = axisbox << parent();
Print( axisParent << Class Name() );
```

### [Prepend](#prepend)[](#prepend "Click to copy url")

**Syntax:** obj \<\< Prepend( db2 )

**Description:** Add db2 to the display tree before db.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << prepend( Text Box( "=== above ===" ) );
```

### [Prev Sib](#prev-sib)[](#prev-sib "Click to copy url")

**Syntax:** obj \<\< Prev Sib

**Description:** Returns the previous sibling of the display box.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 2 )];
axisSibling = axisbox << Prev Sib();
Print( axisSibling << Class Name() );
```

### [Print Window](#print-window)[](#print-window "Click to copy url")

**Syntax:** obj \<\< Print Window

**Description:** Prints the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Print Window;
```

### [Reshow](#reshow)[](#reshow "Click to copy url")

**Syntax:** obj \<\< Reshow

**Description:** Invalidate the displaybox and update the window with the new content. See \<\<Inval and \<\<UpdateWindow messages if more control over timing of the update is required.

``` jsl
//This message applies to all display box objects
color = "green"; /* initial color in a variable */
New Window( "Reshow example",
    Button Box( "red",
        color = "red";
        g << reshow/* tell the graph that something changed */;
    ),
    Button Box( "blue",
        color = "blue";
        g << reshow/* tell the graph that something changed */;
    ),
    g = Graph Box(/* the graph does NOT watch for the color variable to change
                     but will use the current value of color when it reshows */
        Fill Color( color );
        Oval( 10, 80, 70, 50, 1 );
    )
);
```

### [Save Capture](#save-capture)[](#save-capture "Click to copy url")

**Syntax:** obj \<\< Save Capture( \<"path"\>, \<format\>, \<Add Sibling(n)\> )

**Description:** Saves a screen capture of the display box at the specified path. If a path is not given, the Save As window appears.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Capture( "$TEMP/jmp_example.png", "png" );
```

### [Save HTML](#save-html)[](#save-html "Click to copy url")

**Syntax:** obj \<\< Save HTML( \<pathname\>, \<format\> )

**Description:** Saves HTML source and folder of graphics in format specified.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save HTML( "$TEMP/jmp_example.html" );
```

### [Save Interactive HTML](#save-interactive-html)[](#save-interactive-html "Click to copy url")

**Syntax:** obj \<\< Save Interactive HTML( \<pathname\>, \<Boolean\> )

**Description:** Saves Interactive HTML with Data to a file. The Boolean argument represents the report being static.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Interactive HTML( "$TEMP/jmp_example.html" );
```

### [Save Journal](#save-journal)[](#save-journal "Click to copy url")

**Syntax:** obj \<\< Save Journal( \<pathname\> )

**Description:** Saves journal source for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Journal( "$TEMP/jmp_example.jrn" );
```

### [Save MSWord](#save-msword)[](#save-msword "Click to copy url")

**Syntax:** obj \<\< Save MSWord( \<pathname\>, \<format\> )

**Description:** Saves the display box as a Microsoft Word document. (Windows Only)

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save MSWord( "$TEMP/jmp_example.doc" );
```

### [Save PDF](#save-pdf)[](#save-pdf "Click to copy url")

**Syntax:** obj \<\< Save PDF( \<pathname\>, \<Show Page Setup(0\|1)\>, \<Portrait(0\|1)\> )

**Description:** Saves a PDF of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save PDF( "$TEMP/jmp_example.pdf" );
```

### [Save Picture](#save-picture)[](#save-picture "Click to copy url")

**Syntax:** obj \<\< Save Picture( \<pathname\>, \<format\>, \<Scale(factor)\>, \<Type("Bitmap" \| "Scalable")\>, \<View("Picture" \| "Screen" \| "Print"), \<Appearance("Default" \| "Current")\>, \<SubRect(Left(number), Top(number), Right(number), Bottom(number))\> )

**Description:** Saves a picture of the display box. Supported formats are EMF(Windows), PICT(Macintosh), JPEG or JPG, GIF, or PNG. The optional Scale argument will render the image at a scaled resolution. Scaling requires that the display box be stretchable. The Type argument determines whether the result will be a scalable vector image or a bitmap. By default a scalable image is returned, which is suitable for saving to vector formats like PDF. The View option changes the behavior of some boxes. The default option of "Picture" draws the report as it would when exporting to an image format, with scrolled areas fully shown. View mode of "Screen" draws the report as seen on-screen, and "Print" draws the report as it does when printing, without any of the page setup features. The SubRect option will capture a portion of the resulting image rather than a full image. The Appearance option can change from the "Default" output colors to the "Current" colors as seen on-screen. The View, SubRect, and Appearance options are only supported for Type "Bitmap".

#### [Default](#default_1)[](#default_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Picture( "$TEMP/jmp_example.png", "png" );
```

#### [Scale](#scale_2)[](#scale_2 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv[FrameBox( 1 )] << Set Stretch( "Window", "Window" );
rbiv << Save Picture( "$TEMP/jmp_example_scale.png", "png", Scale( 1.5 ) );
New Window( "scaled image", New Image( "$TEMP/jmp_example_scale.png" ) );
```

#### [View and Appearance](#view-and-appearance_1)[](#view-and-appearance_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate(
    Y( :weight ),
    X( :height ),
    Fit Line( {Line Color( {212, 73, 88} )} ),
    Fit Polynomial( 3, {Line Color( {61, 174, 70} )} ),
    Kernel Smoother( 1, 1, 0.5, 0 )
);
rbiv = biv << report;
rbiv << Save Picture(
    "$TEMP/jmp_example_screen.png",
    "png",
    View( "Screen" ),
    Appearance( "Current" )
);
rbiv << Save Picture(
    "$TEMP/jmp_example_print.png",
    "png",
    View( "Print" ),
    Appearance( "Default" )
);
New Window( "Example",
    H List Box(
        New Image( "$TEMP/jmp_example_screen.png" ),
        New Image( "$TEMP/jmp_example_print.png" )
    )
);
```

### [Save Presentation](#save-presentation)[](#save-presentation "Click to copy url")

**Syntax:** obj \<\< Save Presentation( "filename.pptx", \<Template("path\to\my_template.pptx")\>, \<Insert(Begin\|End\|#) \| Replace(Begin\|End\|#) \| Append\>, \<Outline Titles(None\|Hide\|TopLeft\|TopRight\|BottomLeft\|BottomRight)\>, \<"EMF"\|"PNG"\|"JPG"\|"Native"\> )

**Description:** Saves the display box tables and graphs slides in a presentation. The presentation can be opened with Microsoft PowerPoint or other presentation software.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save Presentation( "$TEMP/jmp_example.pptx" );
Open( "$TEMP/jmp_example.pptx" );
```

### [Save RTF](#save-rtf)[](#save-rtf "Click to copy url")

**Syntax:** obj \<\< Save RTF( \<pathname\>, \<format\> )

**Description:** Saves RTF source with graphics in format specified.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Save RTF( "$TEMP/jmp_example.rtf", "png" );
```

### [Save Text](#save-text)[](#save-text "Click to copy url")

**Syntax:** obj \<\< Save Text( \<pathname\>, \<format\> )

**Description:** Saves a file containing the text of the display box.

``` jsl
//This message applies to all display box objects
win = New Window( "Example", a = Text Box( "Example Text" ) );
a << save text( "$TEMP/jmp_example.txt" );
```

### [Save Window Report](#save-window-report)[](#save-window-report "Click to copy url")

**Syntax:** obj \<\< Save Window Report( pathname, \<embed data(0\|1)\> )

**Description:** Saves the current report window to a JMP report file (.jrp).

**JMP Version Added:** 16

``` jsl
//This message can be sent to any display box object but will be applied to the report window
Open( "$SAMPLE_DATA/Big Class.jmp" );
d = distribution( Column( :height ) );
d << Save Window Report( "$DOCUMENTS/test.jrp", embed data( 1 ) );
```

### [Scroll Window](#scroll-window)[](#scroll-window "Click to copy url")

**Syntax:** obj \<\< Scroll Window( DisplayBox \| \<Relative(\<v\> \| \<h\>,\<v\>)\> \| \<Absolute(\<v\> \| \<h\>,\<v\>) )

**Description:** Adjust the window scrollbar to bring the given DisplayBox into view, or scroll a relative number of pixels, or scroll to an absolute pixel location. In place of a number of pixels the keywords "Start" or "End" can be used.

#### [Absolute](#absolute)[](#absolute "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
fm = Fit Model(
    Y( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    Effects( :Subject, :Dose ),
    Personality( "Manova" ),
    Run
);
fm << setwindowsize( 600, 600 ); // shrink the window
fm << scroll window( Absolute( "End", "End" ) );
Wait( 1 );
fm << scroll window( Absolute( 0, 300 ) );
Wait( 1 );
```

#### [Box](#box)[](#box "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
fm = Fit Model(
    Y( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    Effects( :Subject, :Dose ),
    Personality( "Manova" ),
    Run
);
fm << setwindowsize( 600, 600 ); // shrink the window
For( i = 1, i <= 5, i++, // repeatedly, bring each frame box into view for 1/2 second
    fm << scroll window( Report( fm )[framebox( 2 )] );
    Wait( .5 );
    fm << scroll window( Report( fm )[framebox( 3 )] );
    Wait( .5 );
    fm << scroll window( Report( fm )[framebox( 1 )] );
    Wait( .5 );
);
```

#### [Relative](#relative)[](#relative "Click to copy url")

``` jsl

Open( "$SAMPLE_DATA/Blood Pressure.jmp" );
fm = Fit Model(
    Y( :BP 8M, :BP 12M, :BP 6M, :BP 8W, :BP 12W, :BP 6W, :BP 8F, :BP 12F, :BP 6F ),
    Effects( :Subject, :Dose ),
    Personality( "Manova" ),
    Run
);
fm << setwindowsize( 600, 600 ); // shrink the window
fm << scroll window( Relative( 300 ) );
Wait( 1 );
fm << scroll window( Relative( -50 ) );
Wait( 1 );
fm << scroll window( Relative( "Start" ) );
Wait( 1 );
```

### [Select](#select)[](#select "Click to copy url")

**Syntax:** obj \<\< Select

**Description:** Selects this object for use by Edit menu commands.

``` jsl
//This message applies to all display box objects
New Window( "Example", ex = Button Box( "Press Me" ) );
ex << Select;
```

### [Set Content Size](#set-content-size)[](#set-content-size "Click to copy url")

**Syntax:** obj \<\< Set Content Size( x,y )

**Description:** Sets the content size within the window.

``` jsl
//This message applies to all display box objects
w = New Window( "Test",
    lb = List Box( {"a", "b", "c", "d"} ),
    Button Box( "Enable 2nd item",
        lb << enable item( 2, 1 );
        Show( lb << item enabled( 2 ) );
    ),
    Button Box( "Disable 2nd item",
        lb << enable item( 2, 0 );
        Show( lb << item enabled( 2 ) );
    )
);
Wait( 2 );
w << Set Content Size( 400, 300 );
```

### [Set Dirty](#set-dirty)[](#set-dirty "Click to copy url")

**Syntax:** obj \<\< Set Dirty

**Description:** Sets the document's modified status. 0 will not prompt for saving; 1 will prompt.

**JMP Version Added:** 14

``` jsl

ww = New Window( "Test", <<Script, "Open(\!"$SAMPLE_DATA\Big Class.jmp\!");" );
Show( ww << Is Dirty );
ww << Set Dirty( 0 );
Show( ww << Is Dirty );
```

### [Set Height](#set-height)[](#set-height "Click to copy url")

**Syntax:** obj \<\< Set Height( width )

**Description:** Sets the height of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Height( 150 );
```

### [Set Main Window](#set-main-window)[](#set-main-window "Click to copy url")

**Syntax:** obj \<\< Set Main Window

**Description:** Set the window to be the main window in JMP and sets the prior main window to be a normal window

``` jsl
//This message applies to all display box objects
w = New Window( "Main Window", Text Box( "Main JMP Window" ) );
w << Set Main Window;
```

### [Set Max Size](#set-max-size)[](#set-max-size "Click to copy url")

**Syntax:** obj \<\< Set Max Size( width,height )

**Description:** Sets the maximum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Max Size( 500, 500 );
fb << Get Max Size;
```

### [Set Min Size](#set-min-size)[](#set-min-size "Click to copy url")

**Syntax:** obj \<\< Set Min Size( width,height )

**Description:** Sets the minimum size of this display box for purposes of auto-stretching.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Min Size( 30, 30 );
fb << Get Min Size;
```

### [Set Page Setup](#set-page-setup)[](#set-page-setup "Click to copy url")

**Syntax:** obj \<\< Set Page Setup( \<margins(left, top, right, bottom)\>, \<scale(s)\>, \<portrait(0\|1)\>, \<paper size(p)\>, \<Table of Contents(always, never, default)\> )

**Description:** Sets the page setup information that is used during printing or saving as pdf. A Table of Contents can optionally be generated from Outline Boxes.

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Outline Box( "TOC", Text Box( "Page Setup Test" ) ) );
w << Set page setup(
    margins( 1, 1, 1, 1 ),
    scale( 1 ),
    portrait( 1 ),
    paper size( "Letter" ),
    Table of Contents( "always" )
);
w << Save pdf( "$DOCUMENTS\test.pdf" );
```

### [Set Print Footers](#set-print-footers)[](#set-print-footers "Click to copy url")

**Syntax:** obj \<\< Set Print Footers( left footer, center footer, right header )

**Description:** Sets the left, center, and right footers for printed output

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Footer Test" ) );
w << Set Print Footers(
    "Today is: &d;"/*left*/, "&wt;"/*center*/,
    "Page &pn; of &pc;"/*right*/
);
w << Print Window;
```

### [Set Print Headers](#set-print-headers)[](#set-print-headers "Click to copy url")

**Syntax:** obj \<\< Set Print Headers( left header, center header, right header )

**Description:** Sets the left, center, and right headers for printed output

``` jsl
//This message applies to all display box objects
w = New Window( "Window", Text Box( "Header Test" ) );
w << Set Print Headers(
    "Today is: &d;"/*left*/, "&wt;"/*center*/,
    "Page &pn; of &pc;"/*right*/
);
w << Print Window;
```

### [Set Property](#set-property)[](#set-property "Click to copy url")

**Syntax:** obj \<\< Set Property( "property", value )

**Description:** Sets the value for the named property for the display box.

``` jsl
New Window( "Example", bb = Button Box( "Press Me", Print( "Pressed" ) ) );
bb << Set Property( "Enabled", 0 );
```

### [Set Report Title](#set-report-title)[](#set-report-title "Click to copy url")

**Syntax:** obj \<\< Set Report Title( "string" )

**Description:** Changes the report title.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Set Report Title( "New Title" );
```

### [Set Stretch](#set-stretch)[](#set-stretch "Click to copy url")

**Syntax:** obj \<\< Set Stretch( x,y )

**Description:** Sets the horizontal and vertical stretching behavior of the box. Boxes that stretch with Window will resize as the window or splitter size changes. Boxes that stretch to Fill will stretch to fill available space in their container. Boxes with stretching turned Off generally will not stretch. Most boxes default to Neutral, which means that they will determine their behavior based on their child boxes.

**JMP Version Added:** 16

#### [Stretch to Fill](#stretch-to-fill)[](#stretch-to-fill "Click to copy url")

``` jsl
//This message applies to all display box objects
New Window( "Stretch",
    V List Box(
        H List Box( Text Edit Box( "String1" ), Text Edit Box( "String2" ) ),
        Spacer Box( Size( 20, 20 ), Color( "Light Red" ), <<Set Stretch( "Fill", "Off" ) )
    )
);
```

#### [Stretch with Window](#stretch-with-window)[](#stretch-with-window "Click to copy url")

``` jsl
//This message applies to all display box objects
New Window( "Example",
    H List Box(
        tv = Text Box( "V+V", <<rotate text( left ) ),
        V List Box(
            Text Box( "resize the containing window" ),
            th = Text Box( "H+H" ),
            ts = Spacer Box( <<Size( 10, 30 ), <<Color( "blue" ) )
        )
    )
);
tv << Vertical Alignment( "Center" );
th << Horizontal Alignment( "Center" );
th << Set Stretch( "Window", "Off" );
ts << Set Min Size( 5, 20 );
ts << Set Max Size( 100000, 100 );
ts << Set Stretch( "Window", "Window" );
```

### [Set Summary Behavior](#set-summary-behavior)[](#set-summary-behavior "Click to copy url")

**Syntax:** obj \<\< Set Summary Behavior( "Default"\|"Visible"\|"Collapse" )

**Description:** Sets the behavior of the box when a report is viewed in Summary mode.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
d << Report View( "Summary" );
r = d << Report;
tb = r[Table Box( 1 )];
tb << Set Summary Behavior( "Visible" );
```

### [Set Width](#set-width)[](#set-width "Click to copy url")

**Syntax:** obj \<\< Set Width( width )

**Description:** Sets the width of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << Set Width( 400 );
```

### [Set Window Icon](#set-window-icon)[](#set-window-icon "Click to copy url")

**Syntax:** obj \<\< Set Window Icon( icon name )

**Description:** Sets the window icon.

``` jsl
//This message applies to all display box objects
w = New Window( "Example", ex = Button Box( "New Analysis" ) );
w << Set Window Icon( "Scatter3D" );
```

### [Set Window Size](#set-window-size)[](#set-window-size "Click to copy url")

**Syntax:** obj \<\< Set Window Size( x,y )

**Description:** Sets the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Set Window Size( 800, 1200 );
```

### [Set Window Title](#set-window-title)[](#set-window-title "Click to copy url")

**Syntax:** obj \<\< Set Window Title( "string" )

**Description:** Changes the window title.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Set Window Title( "New Title" );
```

### [Show Properties](#show-properties)[](#show-properties "Click to copy url")

**Syntax:** obj \<\< Show Properties

**Description:** Displays a property editor for display boxes

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Show Properties();
```

### [Show Tree Structure](#show-tree-structure)[](#show-tree-structure "Click to copy url")

**Syntax:** obj \<\< Show Tree Structure

**Description:** Displays a hierarchical tree structure of the display box and its related nodes.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rbiv << Show Tree Structure();
```

### [Show Window](#show-window)[](#show-window "Click to copy url")

**Syntax:** obj \<\< Show Window( state=0\|1 )

**Description:** Shows or hides the window. This is useful for hiding windows temporarily. On by default.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
Wait( 1 );
w << Show Window( 0 );
Wait( 2 );
w << Show Window( 1 );
```

### [Sib](#sib)[](#sib "Click to copy url")

**Syntax:** obj \<\< Sib

**Description:** Returns the sibling of the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
axisbox = rbiv[axis box( 1 )];
axisSibling = axisbox << sib();
Print( axisSibling << Class Name() );
```

### [Sib Append](#sib-append)[](#sib-append "Click to copy url")

**Syntax:** obj \<\< Sib Append( Display box, Horizontal\|Vertical )

**Description:** Adds a display box immediately after this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r()[framebox( 1 )];
fb << sib append(
    Text Box( "============ after ==============", Rotate Text( "Right" ) ),
    "Horizontal"
);
fb << sib append( Text Box( "=== below ===" ), "Vertical" );
```

### [Sib Prepend](#sib-prepend)[](#sib-prepend "Click to copy url")

**Syntax:** obj \<\< Sib Prepend( Display box, Horizontal\|Vertical )

**Description:** Adds a display box immediately before this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/big class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
fb = r[framebox( 1 )];
fb << sib prepend(
    Text Box( "    ============ before ==============", Rotate Text( "Right" ) ),
    "Horizontal"
);
fb << sib prepend( Text Box( "=== above ===" ), "Vertical" );
```

### [Size Window](#size-window)[](#size-window "Click to copy url")

**Syntax:** obj \<\< Size Window( x,y )

**Description:** Sets the size of the window.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Size Window( 500, 500 );
```

### [Text Color](#text-color)[](#text-color "Click to copy url")

**Syntax:** obj \<\< Text Color( color ); color = obj \<\< Get Text Color

**Description:** Text will be drawn using the text color if it has been set. If the property has not been set, the box will inherit the text color of the containing box.

**JMP Version Added:** 15

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Text Color );
Wait( 2 );
tb << Text Color( "Red" );
```

### [Top Parent](#top-parent)[](#top-parent "Click to copy url")

**Syntax:** obj \<\< Top Parent

**Description:** Returns the root parent of this display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
rootParent = rbiv << Top Parent();
Print( rootParent << Class Name() );
```

### [UI Only](#ui-only)[](#ui-only "Click to copy url")

**Syntax:** obj \<\< UI Only( state=0\|1 ); state = obj \<\< Get UI Only

### [Update Window](#update-window)[](#update-window "Click to copy url")

**Syntax:** obj \<\< Update Window

**Description:** Update the window holding the displaybox if there are invalidated regions. The \<\<Inval message creates invalidated regions.

``` jsl
//This message applies to all display box objects
color = "green"; /* initial color in a variable */
New Window( "UpdateWindow example",
    Button Box( "red",
        color = "red";
        // try commenting out each of the 4 lines that follow, run the script,
        // click the buttons, and resize the windows (for example) to force a
        // redraw.  All 4 lines are important, though the last two may be
        // slightly different on Windows and Mac OSs.
        g1 << inval; /* tell the oval to redraw */
        g2 << inval; /* tell the rectangle to redraw */
        g1 << updateWindow; /* tell the oval window to update immediately */
        g2 << updateWindow; /* tell the rect window to update immediately */
        // this is a busy-wait to help demonstrate the various behaviors...
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 /* delay without wait(.5) */ );
    ),
    Button Box( "blue",
        color = "blue";
        g1 << inval; /* same comments */
        g2 << inval;
        g1 << updateWindow;
        g2 << updateWindow;
        x = Tick Seconds();
        While( Tick Seconds() - x < .5, 0 );
    )
);
New Window( "oval",
    g1 = Graph Box(/* the graph does NOT watch for the color variable to change
                      but will use the current value of color when it reshows */
        Fill Color( color );
        Oval( 10, 80, 70, 50, 1 );
    )
);
New Window( "rect",
    g2 = Graph Box(
        Fill Color( color );
        Rect( 10, 80, 70, 50, 1 );
    )
);
```

### [Vertical Alignment](#vertical-alignment)[](#vertical-alignment "Click to copy url")

**Syntax:** obj \<\< Vertical Alignment( "Default"\|"Top"\|"Center"\|"Bottom" ); "Default"\|"Top"\|"Center"\|"Bottom" = obj \<\< Get Vertical Alignment

**Description:** Vertical alignment controls the positioning of the box within a container if the box does not fill the entire space.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
lb = r[List Box( 6 )];
lb << Set Horizontal( 1 );
lb = r[List Box( 7 )];
lb << Border( 1 );
Wait( 2 );
lb << Vertical Alignment( "Bottom" );
```

### [Visibility](#visibility)[](#visibility "Click to copy url")

**Syntax:** obj \<\< Visibility( "Visible"\|"Hidden"\|"Collapse" ); "Visible"\|"Hidden"\|"Collapse" = obj \<\< Get Visibility

**Description:** Visibility determines whether a box is shown and whether it takes up space. The default value of "Visible" means that the object will be shown. A "Hidden" box is not shown but still takes up space, while a "Collapsed" box takes up no space in the layout.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
d = dt << Distribution( Column( :height ) );
r = d << report;
tb = r[Table Box( 1 )];
Show( tb << Get Visibility );
Wait( 1 );
tb << Visibility( "Collapse" );
Show( tb << Get Visibility );
```

### [Window Class Name](#window-class-name)[](#window-class-name "Click to copy url")

**Syntax:** obj \<\< Window Class Name

**Description:** Returns the name of the window class for the display box.

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( y( :weight ), x( :height ) );
rbiv = biv << report;
Show( biv << Window Class Name() );
Show( rbiv << Window Class Name() );
```

### [XPath](#xpath)[](#xpath "Click to copy url")

**Syntax:** obj \<\< XPath( XPath expression, \<English(0\|1)\>, \<NoData(0\|1)\> )

**Description:** Applies an XPath expression to the XML representation of the display tree and returns the results. By default, strings are returned in the local language, and the XML includes data values within some boxes. Use the English option to return English strings where available. Use the NoData option to omit the data values within boxes, which is useful for performance when your query is based only on box attributes.

#### [Attributes](#attributes)[](#attributes "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//OutlineBox[@isOpen='false']" )) << Close( 0 );
```

#### [Box type](#box-type)[](#box-type "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//TextEditBox" )) << Text Color( "Green" );
```

#### [Child box](#child-box)[](#child-box "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//OutlineBox[text()='Summary of Fit']/TableBox" )) <<
Make Into Data Table;
```

#### [Data](#data)[](#data "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//NumberColBoxItem[text()='40']/parent::*" )) <<
Text Color( "Green" );
```

#### [Display Seg](#display-seg)[](#display-seg "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//MarkerSeg" )) << Set Marker( "Square" );
```

#### [Text](#text_1)[](#text_1 "Click to copy url")

``` jsl
//This message applies to all display box objects
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Run Script( "Bivariate" );
(Report( biv ) << xpath( "//OutlineBox[text()='Parameter Estimates']" )) << Close;
```

### [Zoom Window](#zoom-window)[](#zoom-window "Click to copy url")

**Syntax:** obj \<\< Zoom Window

**Description:** Resizes the window to be large enough to show all of its contents.

``` jsl
//This message applies to all display box objects
w = Open( "$SAMPLE_DATA/Big Class.jmp" );
w << Set Window Size( 80, 120 );
Wait( 2 );
w << Zoom Window;
```

[ Previous](ScaleBox.html "ScaleBox") [Next ](ScriptBox.html "ScriptBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
