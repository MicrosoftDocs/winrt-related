---
title: com4:DataFormat
description: The data format supported by an application. (com4:DataFormat)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:DataFormat

The data format supported by an application.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Class\>](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:DataFormats\>](element-com4-dataformats.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:DataFormat\>**

## Syntax

```xml
<com4:DataFormat
    FormatName = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    StandardFormat = 'A string in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case).'
    AspectFlag = 'An integer with a value between -1 and 15.'
    MediumFlag = 'An integer between 0 and 127.'
    Direction = 'A string with one of the following values: "Get", "Set", or "GetAndSet".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **FormatName** | The name of the data format. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **StandardFormat** | The integer value of the data format. | A string in hexadecimal format containing numbers or the letters `a`, `b`, `c`, `d`, `e`, or `f` (capital or lower case). | Yes |  |
| **AspectFlag** | Represents a [DVASPECT](/windows/win32/api/wtypes/ne-wtypes-dvaspect) enumeration value for the desired data or view aspect. | An integer with a value between -1 and 15. | Yes |  |
| **MediumFlag** | The type of storage medium used for data transfer. This corresponds to the [TYMED](/windows/win32/api/objidl/ne-objidl-tymed) enumeration. | An integer between 0 and 127.| Yes |  |
| **Direction** | This represents the [DATADIR](/windows/win32/api/objidl/ne-objidl-datadir) enumeration which corresponds to the direction of the data flow. | A string with one of the following values: *Get*, *Set*, or *GetAndSet*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:DataFormats](element-com4-dataformats.md) | Specifies the default and main data formats supported by an application. |

## Remarks

Note that **FormatName** and **StandardFormat** are mutually exclusive attributes and are [Standard Clipboard Formats](/windows/win32/dataxchg/standard-clipboard-formats).

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
