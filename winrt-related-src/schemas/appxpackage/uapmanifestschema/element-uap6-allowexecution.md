---
description: Indicates whether the contents of the package will be allowed to execute.
title: uap6:AllowExecution
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/07/2018
---

# uap6:AllowExecution

Indicates whether the contents of the package will be allowed to execute.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap6:AllowExecution\>**

## Syntax

```xml
<uap6:AllowExecution>
  boolean
</uap6:AllowExecution>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |
