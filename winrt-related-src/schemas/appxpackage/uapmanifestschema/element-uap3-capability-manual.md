---
description: Declares a capability required by a package (uap3:Capability).
Search.Product: eADQiWindows 10XVcnh
title: uap3:Capability (Windows 10)
ms.assetid: 1a5d687b-4e1f-479a-a24e-eeda24afc560
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:Capability (Windows 10)

Declares a capability required by a package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:Capability\>**

## Syntax

```xml
<uap3:Capability
    Name = 'A string that can have one of the following values: "backgroundMediaPlayback" or "userNotificationListener".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *backgroundMediaPlayback* or *userNotificationListener*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent Element | Description |
|-|-|
| [Capabilities](element-capabilities.md) | Declares the access to protected user resources that the package requires. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
