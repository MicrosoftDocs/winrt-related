---
title: com4:InProcessServerDll
description: Specifies the path and processor architecture of an in-process server DLL. (com4:InProcessServerDll)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessServerDll

Specifies the path and processor architecture of an in-process server DLL.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:InProcessServer\>](element-com4-inprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:InProcessServerDll\>**

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:InProcessServer\>](element-com4-inprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:InProcessServerDll\>**

## Syntax

```xml
<com4:InProcessServerDll
    Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".'
    ProcessorArchitecture = 'A string that can have one of the following values: "x86", "x64", "arm", "arm64", or "x86a64".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The full path to the in-process server DLL. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`, ending with the case-insensitive file extension `.dll`. | Yes |  |
| **ProcessorArchitecture** | The processor architecture of the in-process server DLL. | A string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, or *x86a64*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:InProcessServer](element-com4-inprocessserver.md) | Registers an in-process server with one or many class registrations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
