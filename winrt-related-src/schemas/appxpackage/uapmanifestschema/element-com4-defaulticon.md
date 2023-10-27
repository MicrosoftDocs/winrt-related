---
title: com4:DefaultIcon
description: Provides default icon information for iconic presentations of objects. (com4:DefaultIcon)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:DefaultIcon

## Description

Provides default icon information for iconic presentations of objects.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Class\>](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:DefaultIcon\>**

## Syntax

```xml
<com4:DefaultIcon
    Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
    ResourceIndex = 'An optional integer value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The full path to the executable name of the server application. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **ResourceIndex** | The integer at the end of the path, separated from the path by a comma  (for example, `C:\Foo\Bar\Baz.exe,5`). See the `nIconIndex` parameter in [ExtractIcon](/windows/win32/api/shellapi/nf-shellapi-extracticona) for more details. | An optional integer value. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:Class](element-com4-class.md) | Specifies properties of a CLSID registered by the package that can be shared by one or more concrete registrations of the CLSID for different class contexts. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
