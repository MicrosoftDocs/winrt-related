---
description: An extension that allows an app developer to declare a path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes.
title: uap6:LoaderSearchPathOverride
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/10/2018
---

# uap6:LoaderSearchPathOverride

An extension that allows an app developer to declare a path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap6:LoaderSearchPathOverride\>**

## Syntax

```xml
<uap6:LoaderSearchPathOverride>

  <!-- Child elements -->
  LoaderSearchPathEntry{0,5}

</uap6:LoaderSearchPathOverride>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap6:LoaderSearchPathEntry](element-uap6-loadersearchpathentry.md) | A relative path used specify where to load content from an app package. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-extension.md) | Declares an extensibility point for the package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |
