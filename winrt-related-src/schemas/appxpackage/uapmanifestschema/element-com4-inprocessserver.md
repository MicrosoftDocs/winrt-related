---
title: com4:InProcessServer
description: Declares a package extensibility point of type windows.activatableClass.inProcessServer (com4:InProcessServer).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessServer



## Description
Declares a package extensibility point of type windows.activatableClass.inProcessServer.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:InProcessServer&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:InProcessServer     Path? = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".
>
<!-- Child elements -->
  Class
  InProcessServerDll
  ClassReference
</com4:InProcessServer>
```

## Key
`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | The path to the DLL. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *, ending with the case-insensitive file extension ".dll".| No |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-inprocessserver-class.md) | TBD |
| [InProcessServerDll](element-com4-inprocessserverdll.md) | TBD |
| [ClassReference](element-com4-inprocessserver-classreference.md) | TBD |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
