---
title: com5:Format
description: Specifies the file format an application can read from or write to. (com5:Format)
ms.date: 06/22/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com5:Format



## Description

Specifies the file format an application can read from or write to.

## Element Hierarchy
[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp; [\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Conversion\>](element-com5-conversion.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Readable\>](element-com5-readable.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **&lt;com5:Format&gt;**

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<ReadWritable\>](element-com5-readwritable.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **&lt;com5:Format&gt;**


## Syntax
```syntax
<com5:Format     FormatName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    StandardFormat = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).
></com5:Format>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| FormatName | The string value of the format name. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| StandardFormat | The hexadecimal value of the format name. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).| Yes |

### Parent elements

| Parent element | Description |
|-|-|
| [com5:Readable](element-com5-readable.md) | Specifies that an application can only read files. |
| [com5:Readwritable](element-com5-readwritable.md) | Specifies that an application can read and write files. |


## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com5 | http://schemas.microsoft.com/appx/manifest/com/windows10/5 |
