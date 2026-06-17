---
title: uap2:Capability
description: Declares a capability required by a package (uap2:Capability).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap2:Package, uap2:Capabilities, uap2:Capability]
---

# uap2:Capability

Declares a capability required by a package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap2:Capability>`**  

## Syntax

```xml
<uap2:Capability
  Name = 'A required string that can have one of the following values: "phoneCallHistoryPublic", or "spatialPerception".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *phoneCallHistoryPublic*, *spatialPerception*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<Package
    xmlns:uap2="http://schemas.microsoft.com/appx/manifest/uap/windows10/2"  
    IgnorableNamespaces="uap2">
    <Capabilities>
        <uap2:Capability
            Name="phoneCallHistoryPublic"/>  
        <uap2:Capability
            Name="spatialPerception"/>  
    </Capabilities>
</Package>
```
