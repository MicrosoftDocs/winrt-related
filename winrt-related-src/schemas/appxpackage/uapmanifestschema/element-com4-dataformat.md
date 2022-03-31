---
title: com4:DataFormat
description: The data format supported by an application. (com4:DataFormat)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:DataFormat



## Description
The data format supported by an application.



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
<dl><dt><a href = "element-com4-dataformats.md">&lt;com4:DataFormats&gt;</a></dt>
<dd>
<b>&lt;com4:DataFormat&gt;</b>
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
</dd>
</dl>

## Syntax
```syntax
<com4:DataFormat     FormatName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    StandardFormat = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).
    AspectFlag = An integer between -1 and 15.
    MediumFlag = An integer between 0 and 127.
    Direction = "Get" | "Set" | "GetAndSet"
></com4:DataFormat>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| FormatName | The name of the data format. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| StandardFormat | The integer value of the data format. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).| Yes |
| AspectFlag | Represents a [DVASPECT](/windows/win32/api/wtypes/ne-wtypes-dvaspect) enumeration value for the desired data or view aspect. | An integer between -1 and 15.| Yes |
| MediumFlag | The type of storage medium used for data transfer. This corresponds to the [TYMED](/windows/win32/api/objidl/ne-objidl-tymed) enumeration. | An integer between 0 and 127.| Yes |
| Direction | This represents the [DATADIR](/windows/win32/api/objidl/ne-objidl-datadir) enumeration which corresponds to the direction of the data flow. | One of the following values: "Get" , "Set" , "GetAndSet"| Yes |

## Remarks
Note that **FormatName** and **StandardFormat** are mutually exclusive attributes and are [Standard Clipboard Formats](/windows/win32/dataxchg/standard-clipboard-formats).

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
