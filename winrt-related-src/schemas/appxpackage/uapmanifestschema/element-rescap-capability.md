---
description: Declares a restricted capability required by a package (rescap:Capability).
Search.Product: eADQiWindows 10XVcnh
title: rescap:Capability (Windows 10)
ms.assetid: 1a5d687b-4e1f-479a-a24e-eeda24afc560
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# rescap:Capability (Windows 10)

Declares a restricted capability required by a package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<rescap:Capability\>**

## Syntax

```xml
<rescap:Capability
    Name = 'A string that is between 3 and 128 characters that can contain alphanumeric characters and underscores.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that is between 3 and 128 characters that can contain alphanumeric characters and underscores. | Yes |  |

### Child elements

None.

### Parent elements

| Parent Element | Description |
|-|-|
| [Capabilities](element-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Examples



## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
