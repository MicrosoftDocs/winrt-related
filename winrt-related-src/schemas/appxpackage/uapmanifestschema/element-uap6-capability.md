---
description: Declares a capability required by a package (uap6:Capability).
title: uap6:Capability
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/10/2018
---

# uap6:Capability

Declares a capability required by a package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap6:Capability\>**

## Syntax

```xml
<uap6:Capability
  Name = 'A string that can have one of the following values: "graphicsCapture".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: "graphicsCapture". | Yes |  |  

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-capabilities.md) | Declares the access to protected user resources that the package requires. |

## See also

[App capability declarations](/previous-versions/windows/apps/hh464936(v=win.10))

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
