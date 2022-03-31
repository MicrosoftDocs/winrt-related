---
title: com4:TypeLib (in com4:ComInterface)
description: Registers a type library. (in com4:ComInterface)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:TypeLib



## Description
Registers a type library.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:TypeLib&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:TypeLib     Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
>
<!-- Child elements -->
  Version
</com4:TypeLib>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Id | The type library ID.  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Version](element-com4-version.md) | Version number and additional information about the type library. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
