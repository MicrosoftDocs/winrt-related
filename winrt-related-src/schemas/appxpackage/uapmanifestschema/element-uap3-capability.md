---
title: uap3:Capability
description: Declares a capability required by a package (uap3:Capability).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap3:Package, uap3:Capabilities, uap3:Capability]
---

# uap3:Capability

Declares a capability required by a package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:Capability>`**  

## Syntax

```xml
<uap3:Capability
  Name = 'A required string that can have one of the following values: "backgroundMediaPlayback", "userNotificationListener", or "remoteSystem".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *backgroundMediaPlayback*, *userNotificationListener*, *remoteSystem*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<Package
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="uap3">
    <Capabilities>
        <uap3:Capability
            Name="backgroundMediaPlayback"/>  
        <uap3:Capability
            Name="userNotificationListener"/>  
    </Capabilities>
</Package>
```
