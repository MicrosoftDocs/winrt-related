---
ms.assetid: 706cd678-5620-4733-880b-72641a308c3c
title: desktop2:SearchFilterHandler
description: Enables Windows Desktop Bridge apps to register IFilters to extract file properties for searching.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:SearchFilterHandler

Enables Windows Desktop Bridge apps to register IFilters to extract file properties for searching.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:Extension\>](element-desktop2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:SearchFilterHandler\>**

## Syntax

```xml
<desktop2:SearchFilterHandler
  Clsid = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  Path  = 'An optional string with a value between 1 and 256 characters in length, ending with ".dll" and cannot contain these characters: <, >, :, ", |, ?, or *.'
  ProcessorArchitecture = 'An optional string that can have one of the following values: "x86", "x64", "arm", "arm64", or "neutral".' />

  <!-- Child elements -->
  desktop2:FilterExtension{0,10000}

</desktop2:SearchFilterHandler>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Clsid** | The ID of the class that will be activated to handle requests for files. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **Path** | The path to the binary in the app's package. | An optional string with a value between 1 and 256 characters in length, ending with `.dll`, that cannot contain the following characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |
| **ProcessorArchitecture** | The processor architecture. | One of the following: *x86*, *x64*, *arm*, *arm64*, or *neutral*. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [FilterExtension](element-desktop2-FilterExtension.md) | Specifies the file type to be registered by the app. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
