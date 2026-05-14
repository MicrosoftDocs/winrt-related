---
description: Declares a capability required by a package (uap6:Capability).
title: uap6:Capability
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/10/2018
no-loc: [Package, Capabilities, uap6:Capability]
---

# uap6:Capability

Declares a capability required by a package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:Capability>`**  

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
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |

## See also

[App capability declarations](/windows/uwp/packaging/app-capability-declarations)

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |
