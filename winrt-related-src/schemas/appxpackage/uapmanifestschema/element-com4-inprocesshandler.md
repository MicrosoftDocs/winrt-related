---
title: com4:InProcessHandler
description: TBD
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessHandler



## Description
TBD



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:InProcessHandler&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:InProcessHandler     Path? = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".
>
<!-- Child elements -->
  Class
  InProcessHandlerDll
  ClassReference
</com4:InProcessHandler>
```

## Key
`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | TBD | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *, ending with the case-insensitive file extension ".dll".| No |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-inprocesshandler-class.md) | TBD |
| [InProcessHandlerDll](element-com4-inprocesshandlerdll.md) | TBD |
| [ClassReference](element-com4-inprocesshandler-classreference.md) | TBD |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
