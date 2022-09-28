---
ms.assetid: 6997bc14-c33f-4a88-aec1-21c1ddd5a8f2
title: uap4:Capability
description: Declares a capability required by a package.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:Capability

Declares a capability required by a package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap4:Capability\>**

## Syntax

```xml
<uap4:Capability
  Name = 'A string that can have one of the following values: "offlineMapsManagement" or "userDataTasks".' />
```

## Attributes and elements

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *offlineMapsManagement* or *userDataTasks*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Capability](element-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
