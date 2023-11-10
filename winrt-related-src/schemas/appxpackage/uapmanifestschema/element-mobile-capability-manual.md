---
description: Declares a capability required by a package (mobile:Capability).
Search.Product: eADQiWindows 10XVcnh
title: mobile:Capability (Windows 10)
ms.assetid: c3074580-c334-4578-93e1-e7eb2c58c8ea
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# mobile:Capability 

Declares a capability required by a package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<mobile:Capability\>**

## Syntax

```xml
<mobile:Capability
  Name = 'A string that can have one of the following values: "recordedCallsFolder".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: "recordedCallsFolder". | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/mobile/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
