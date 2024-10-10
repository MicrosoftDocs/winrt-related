---
title: com4:Win64Path
description: A path to the 64-bit type library. (com4:Win64Path)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Win64Path

A path to the 64-bit type library.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:TypeLib\>](element-com4-typelib.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Version\>](element-com4-version.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Win32Path\>**

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:TypeLib\>](element-com4-typelib.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Version\>](element-com4-version.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Win32Path\>**

## Syntax

```xml
<com4:Win64Path
    Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
    ResourceId = 'An optional non-negative integer value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | A path to the 32-bit TypeLib relative to the package root. Path must reference a file in the package. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **ResourceId** | The integer at the end of the default value of the Win32Path, separated from the path by a backslash (for example, C:\Foo\Bar\Baz.exe\5). | An optional non-negative integer value. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:Version](element-com4-version.md) | Version number and additional information about the type library. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
