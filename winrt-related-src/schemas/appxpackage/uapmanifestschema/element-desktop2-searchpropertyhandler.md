---
title: desktop2:SearchPropertyHandler
description: Enables Windows Desktop Bridge apps to install property handlers on your system. These handlers are used to read properties from files for indexing and search.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop2:Extension, desktop2:SearchPropertyHandler]
---

# desktop2:SearchPropertyHandler

Enables Windows Desktop Bridge apps to install property handlers on your system. These handlers are used to read properties from files for indexing and search.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:SearchPropertyHandler>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:SearchPropertyHandler>`**

## Syntax

```xml
<desktop2:SearchPropertyHandler
  Clsid = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  Path = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".'
  ProcessorArchitecture = 'A required string that can have one of the following values: "x86", "x64", "arm", "arm64", or "neutral".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Clsid** | <!-- TODO: Add description --> | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **Path** | Path relative to the binary that implements the CLSID. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension ".dll". | Yes |  |
| **ProcessorArchitecture** | <!-- TODO: Add description --> | A string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, *neutral*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop2:Extension](element-desktop2-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

Starting with Windows 10 Version 1809 and Windows 11 Version 22H2, this app extension will no longer work for desktop apps packaged as UWP apps using Windows Desktop Bridge. Including this extension in the package manifest for Desktop Bridge apps will have no effect.

## Examples

<!-- Author content goes here -->
