---
ms.assetid: 6bca24cd-9433-4cbd-a701-9356f0a4b418
title: com:DataFormats (in ExeServer/Class)
description: Specifies the default and main data formats supported by an application (in ExeServer/Class).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:DataFormats (in ExeServer/Class)

Specifies the default and main data formats supported by an application.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComServer\>](element-com-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ExeServer\>](element-com-exeserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Class\>](element-com-exeserver-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:DataFormats\>**

## Syntax

```xml
<com:DataFormats
  DefaultFormatName = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DefaultStandardFormat = 'A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case)'. >

  <!-- Child elements -->
  DataFormat{0,1000}

</com:DataFormats>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

## Attributes

| Attribute | Description | Data type | Required |
|-|-|-|-|
| DefaultFormatName | The string value of the format name. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| DefaultStandardFormat | The hexadecimal value of the format name. | A string in hexadecimal format containing numbers or the letters `a`, `b`, `c`, `d`, `e`, or `f` (capital or lower case). | Yes |

## Child elements

| Child Element | Description |
|-|-|
| [DataFormat](element-com-exe-dataformat.md) | The data format supported by an application. |

## Parent elements

| Parent Element | Description |
|-|-|
| [com:Class](element-com-exeserver-class.md) | Defines an ExeServer class registration. |

## Remarks

**DefaultFormatName** is the string value, and **DefaultStandardFormat** is the integer value of the supported data formats. These values are mutually exclusive.

This element corresponds to the [DataFormats](/windows/win32/com/dataformats) subkey.

## Examples

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
