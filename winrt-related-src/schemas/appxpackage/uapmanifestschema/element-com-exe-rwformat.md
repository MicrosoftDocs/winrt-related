---
ms.assetid: 65f3026d-b53f-448e-abb3-5f8826a01af5
title: com:Format (in ExeServer/Class)
description: Specifies the file format an application can read and write (activate as) (in ExeServer/Class).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:Format (in ExeServer/Class)

Specifies the file format an application can read and write (activate as).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComServer\>](element-com-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ExeServer\>](element-com-exeserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Class\>](element-com-exeserver-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Conversion\>](element-com-exe-conversion.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Readwritable\>](element-com-exe-readwritable.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Format\>**

## Syntax

```xml
<com:Format
    FormatName = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    StandardFormat = 'An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case).' >
</com:Format>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **FormatName** | The string file format name. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **StandardFormat** | The hexadecimal file format name. | An optional string in hexadecimal format containing numbers or the letters `a`, `b`, `c`, `d`, `e`, or `f` (capital or lower case). | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com:Readwritable](element-com-exe-readwritable.md) | Specifies that an application can read and write files. |

## Remarks

> [!NOTE]
> **FormatName** and **StandardFormat** are mutually exclusive.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
