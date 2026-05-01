# JMP App Module

*Source: [https://jsl.jmp.com/All%20Categories/Objects/JMP%20App%20Module.html](https://jsl.jmp.com/All%20Categories/Objects/JMP%20App%20Module.html)*

---

# [JMP App Module](#jmp-app-module)[](#jmp-app-module "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Create Instance](#create-instance)[](#create-instance "Click to copy url")

**Syntax:** instance = obj \<\< Create Instance( \<parameters\> )

**Description:** Create an instance of the module. The parameters are passed to the OnModuleLoad() function defined in the module script.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Run Application;
modules = app << Get Modules;
modules[1] << Create Instance;
```

### [Get Application](#get-application)[](#get-application "Click to copy url")

**Syntax:** app = obj \<\< Get Application

**Description:** Returns the application that owns the module.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Run Application;
modules = app << Get Modules;
modules[1] << Get Application;
```

[ Previous](JMP%20App%20Module%20Instance.html "JMP App Module Instance") [Next ](JMP%20App.html "JMP App")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
