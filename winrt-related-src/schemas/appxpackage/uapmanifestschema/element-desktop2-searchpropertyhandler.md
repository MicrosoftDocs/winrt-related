---
ms.assetid: 92f81548-6524-4d3f-8e9c-5a671fa72813
title: desktop2:SearchPropertyHandler
description: Enables Windows Desktop Bridge apps to install property handlers on your system. These handlers are used to read properties from files for indexing and search.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:SearchPropertyHandler

Enables Windows Desktop Bridge apps to install property handlers on your system. These handlers are used to read properties from files for indexing and search.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:Extension\>](element-desktop2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:SearchPropertyHandler\>**

## Syntax

```xml
<desktop2:SearchPropertyHandler Clsid = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
                                Path  = 'A string with a value between 1 and 256 characters in length, ending with ".dll", that cannot contain the following characters: <, >, :, ", |, ?, or *.'
                                ProcessorArchitecture = 'A string that can have one of the following values: "x86", "x64", "arm", "arm64", or "neutral".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Clsid** | The ID of the class in the app's package. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| **Path** | Path relative to the binary that implements the CLSID. | A string with a value between 1 and 256 characters in length, ending with `.dll`, that cannot contain the following characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |
| **ProcessorArchitecture** | The processor architecture. | A string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, or *neutral*. | Yes |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop2:Extension](element-desktop2-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| Minimum OS Version | Windows 10 version 1703 (Build 15063) |
