---
title: uap6:LoaderSearchPathOverride
description: An extension that allows an app developer to declare a path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap6:Extension, uap6:LoaderSearchPathOverride]
---

# uap6:LoaderSearchPathOverride

An extension that allows an app developer to declare a path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap6:Extension>`](element-uap6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:LoaderSearchPathOverride>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap6:Extension>`](element-uap6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:LoaderSearchPathOverride>`**  

## Syntax

```xml
<uap6:LoaderSearchPathOverride>

  <!-- Child elements -->
  uap6:LoaderSearchPathEntry{0,5}

</uap6:LoaderSearchPathOverride>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap6:LoaderSearchPathEntry](element-uap6-loadersearchpathentry.md) | A path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap6:Extension](element-uap6-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->