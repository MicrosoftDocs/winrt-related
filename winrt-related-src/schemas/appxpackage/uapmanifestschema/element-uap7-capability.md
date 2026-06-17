---
title: uap7:Capability
description: Declares a capability.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Extensions, uap7:Package, uap7:Capabilities, uap7:Capability]
---

# uap7:Capability

Declares a capability required by a package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap7:Capability>`**  

## Syntax

```xml
<uap7:Capability
  Name = 'A required string that can have one of the following values: "globalMediaControl", or "gazeInput".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *globalMediaControl*, *gazeInput*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->