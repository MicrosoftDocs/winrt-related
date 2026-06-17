---
title: uap6:LoaderSearchPathEntry
description: A relative path used specify where to load content from an app package.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap6:Extension, uap6:LoaderSearchPathOverride, uap6:LoaderSearchPathEntry]
---

# uap6:LoaderSearchPathEntry

A path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap6:Extension>`](element-uap6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap6:LoaderSearchPathOverride>`](element-uap6-loadersearchpathoverride.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:LoaderSearchPathEntry>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap6:Extension>`](element-uap6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap6:LoaderSearchPathOverride>`](element-uap6-loadersearchpathoverride.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:LoaderSearchPathEntry>`**  

## Syntax

```xml
<uap6:LoaderSearchPathEntry
  FolderPath = 'A path relative to the package root. Paths cannot contain a leading or trailing slash or backslash ("\"). This value can also be an empty string.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **FolderPath** | A relative path used specify where to load content from an app package. | A path relative to the package root. Paths cannot contain a leading or trailing slash or backslash (`\`). This value can also be an empty string. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap6:LoaderSearchPathOverride](element-uap6-loadersearchpathoverride.md) | An extension that allows an app developer to declare a path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

Note that a *LoaderSearchPathEntry* can contain an empty *FolderPath*, which has a different behavior than omitting the *LoaderSearchPathEntry*. If the *LoaderSearchPathEntry* is omitted, the default path is the app package root path. Duplicate paths are not permitted.

Main app packages, related set package, optional packages, and framework packages can all declare a *LoaderSearchPathEntry*.

## Examples

<!-- Author content goes here -->