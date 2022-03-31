---
title: com4:ManagedInProcessServer
description: TBD
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ManagedInProcessServer



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
<dd><b>&lt;com4:ManagedInProcessServer&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:ManagedInProcessServer     Assembly = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    RuntimeVersion = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
>
<!-- Child elements -->
  Class
  ClassReference
</com4:ManagedInProcessServer>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Assembly | TBD | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| RuntimeVersion | TBD | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-managedinprocessserver-class.md) | TBD |
| [ClassReference](element-com4-managedinprocessserver-classreference.md) | TBD |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
