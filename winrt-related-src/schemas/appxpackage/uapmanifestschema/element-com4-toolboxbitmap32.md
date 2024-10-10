---
title: com4:ToolboxBitmap32
description: Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. (com4:ToolboxBitmap32)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ToolboxBitmap32

Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:SurrogateServer\>](element-com4-surrogateserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Class\>](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ToolboxBitmap32\>**

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:SurrogateServer\>](element-com4-surrogateserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Class\>](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ToolboxBitmap32\>**

## Syntax

```xml
<com4:ToolboxBitmap32
    Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
    ResourceId = 'A non-negative integer value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The path to the bitmap.  | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **ResourceId** | The resource ID of the bitmap. | A non-negative integer value. | Yes |  |

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
