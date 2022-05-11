---
title: com4:Aspect
description: Specifies the desired data or view aspect of the object when drawing or getting data. (com4:Aspect)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Aspect



## Description
Specifies the desired data or view aspect of the object when drawing or getting data.



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
<dl><dt><a href = "element-com4-miscstatus.md">&lt;com4:MiscStatus&gt;</a></dt>
<dd>
<b>&lt;com4:Aspect&gt;</b>
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
<com4:Aspect     Type = "Content" | "Thumbnail" | "Icon" | "DocPrint"
    OleMiscFlag = An integer value in the range of 0-4194303.
></com4:Aspect>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Type | The string value for the view aspect of the object. | One of the following values: "Content" , "Thumbnail" , "Icon" , "DocPrint"| Yes |
| OleMiscFlag | The integer value for the view aspect of the object. | An integer value in the range of 0-4194303.| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
