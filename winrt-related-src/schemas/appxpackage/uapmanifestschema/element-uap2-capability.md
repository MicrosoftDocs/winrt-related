---
description: Declares a capability required by a package (uap2:Capability).
Search.Product: eADQiWindows 10XVcnh
title: uap2:Capability (Windows 10)
ms.assetid: 1a5d687b-4e1f-479a-a24e-eeda24afc560
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap2:Capability (Windows 10)

Declares a capability required by a package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap2:Capability\>**

## Syntax

```xml
<uap2:Capability
    Name = 'A string that can have one of the following values: "phoneCallHistoryPublic" or "spatialPerception".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *phoneCallHistoryPublic* or *spatialPerception*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent Element | Description |
|-|-|
| [Capabilities](element-capabilities.md) | Declares the access to protected user resources that the package requires. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
