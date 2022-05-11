---
title: com4:DataFormats
description: Specifies the default and main data formats supported by an application. (com4:DataFormats)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:DataFormats



## Description
Specifies the default and main data formats supported by an application.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-class.md">&lt;com4:Class&gt;</a></dt>
<dd>
<b>&lt;com4:DataFormats&gt;</b>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:DataFormats     DefaultFormatName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    DefaultStandardFormat = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).
>
<!-- Child elements -->
  DataFormat
</com4:DataFormats>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| DefaultFormatName | The string value of the format name. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| DefaultStandardFormat | The hexadecimal value of the format name. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [DataFormat](element-com4-dataformat.md) | The data format supported by an application. |

## Remarks
**DefaultFormatName** is the string value, and **DefaultStandardFormat** is the integer value of the supported data formats. These values are mutually exclusive.

This element corresponds to the [DataFormats](/windows/win32/com/dataformats) subkey.

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
