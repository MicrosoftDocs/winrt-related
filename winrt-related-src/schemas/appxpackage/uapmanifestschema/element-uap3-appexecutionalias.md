---
title: uap3:AppExecutionAlias
description: Specifies the application's execution alias to determine the executable of the app to be activated (uap3:AppExecutionAlias).
ms.date: 04/04/2004
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap3:AppExecutionAlias

## Description
Specifies the application's execution alias to determine the executable of the app to be activated.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap3-extension-manual.md">&lt;uap3:Extension&gt;</a></dt>
<dd><b>&lt;uap3:AppExecutionAlias&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap3:AppExecutionAlias desktop4:Subsystem? = String value. Can be one of the following: "console", "windows" >   
    uap3:ExecutionAlias{0,1000}
</uap3:AppExecutionAlias>
```

### Key
`{}`   specific range of occurrences


## Attributes and Elements
### Attributes
## Attributes

None.

### Child Elements
| Child Element | Description |
|---------------|-------------|
| [desktop:ExecutionAlias](element-desktop-executionalias.md) | The executable of a UWP app to be activated from a command prompt. |
| [uap8:ExecutionAlias](element-uap8-executionalias.md) | The executable of a UWP app to be activated from a command prompt. |


## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
