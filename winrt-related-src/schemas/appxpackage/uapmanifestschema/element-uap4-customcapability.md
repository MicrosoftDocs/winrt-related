---
ms.assetid: 7c6136d7-780e-40a8-b374-f81998dac3f4
title: uap4:CustomCapability
description: Declares a custom capability required by a package.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:CustomCapability

Declares a custom capability required by a package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap4:CustomCapability\>**

## Syntax

```xml
<uap4:CustomCapability
  Name = 'An alphanumeric string in the form: "company.capabilitynamefromstore_publisherId".' >
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | An alphanumeric string in the form: company.capabilitynamefromstore_publisherId.  | Yes |  |

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
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
