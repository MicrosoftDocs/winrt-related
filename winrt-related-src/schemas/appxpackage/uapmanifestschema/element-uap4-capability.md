---
title: uap4:Capability
description: Declares a capability required by a package.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Extensions, uap4:Package, uap4:Capabilities, uap4:Capability]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap4:Capability

Declares a capability required by a package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap4:Capability>`**

## Syntax

```xml
<uap4:Capability
  Name = 'A required string that can have one of the following values: "offlineMapsManagement", or "userDataTasks".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *offlineMapsManagement*, *userDataTasks*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
