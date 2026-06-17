---
title: rescap:Capability
description: Declares a restricted capability required by a package (rescap:Capability).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, rescap:Package, rescap:Capabilities, rescap:Capability]
---

# rescap:Capability

Declares a restricted capability required by a package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap:Capability>`**  

## Syntax

```xml
<rescap:Capability
  Name = 'A required value. <!-- TODO: Add description for t:ST_Capability_Windows_Restricted_Party -->' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A value. <!-- TODO: Add data type for t:ST_Capability_Windows_Restricted_Party --> | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
