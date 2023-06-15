---
title: com4:DataFormats
description: Specifies the default and main data formats supported by an application. (com4:DataFormats)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:DataFormats

Specifies the default and main data formats supported by an application.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Class\>](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:DataFormats\>**

## Syntax

```xml
<com4:DataFormats
  DefaultFormatName = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DefaultStandardFormat = 'A string in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case).' />

<!-- Child elements -->
  DataFormat
</com4:DataFormats>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DefaultFormatName** | The string value of the format name. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **DefaultStandardFormat** | The hexadecimal value of the format name. | A string in hexadecimal format containing numbers or the letters `a`, `b`, `c`, `d`, `e`, or `f` (capital or lower case). | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [DataFormat](element-com4-dataformat.md) | The data format supported by an application. |

### Parent elements

| Parent element | Description |
|-|-|
| [com4:Class](element-com4-class.md) | Specifies properties of a CLSID registered by the package that can be shared by one or more concrete registrations of the CLSID for different class contexts. |

## Remarks

**DefaultFormatName** is the string value, and **DefaultStandardFormat** is the integer value of the supported data formats. These values are mutually exclusive.

This element corresponds to the [DataFormats](/windows/win32/com/dataformats) subkey.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
