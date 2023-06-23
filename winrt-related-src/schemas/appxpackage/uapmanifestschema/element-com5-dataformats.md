---
title: com5:DataFormats
description: Specifies the default and main data formats supported by an application. (com5:DataFormats)
ms.date: 06/22/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com5:DataFormats



## Description
TBD



## Element Hierarchy
[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp; [\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com5:Class\> (in InProcessServer)](element-com5-inprocessserver-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **&lt;com5:DataFormats&gt;**

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com5:Class\> (in InProcessHandler)](element-com5-inprocesshandler-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **&lt;com5:DataFormats&gt;**


## Syntax
```syntax
<com5:DataFormats     DefaultFormatName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    DefaultStandardFormat = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).
>
<!-- Child elements -->
  DataFormat
</com5:DataFormats>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| DefaultFormatName | The string value of the format name. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| DefaultStandardFormat | The hexadecimal value of the format name. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [DataFormat](element-com5-dataformat.md) | TBD |

## Parent elements

| Parent element | Description |
|-|-|
| [com5:Class (in InProcessServer)](element-com5-inprocessserver-class.md) | Specifies properties of a CLSID registered by the package that can be shared by one or more concrete registrations of the CLSID for different class contexts. |
| [com5:Class (in InProcessHandler)](element-com5-inprocesshandler-class.md) | Specifies properties of a CLSID registered by the package that can be shared by one or more concrete registrations of the CLSID for different class contexts. |

## Remarks

**DefaultFormatName** is the string value, and **DefaultStandardFormat** is the integer value of the supported data formats. These values are mutually exclusive.

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com5 | http://schemas.microsoft.com/appx/manifest/com/windows10/5 |
