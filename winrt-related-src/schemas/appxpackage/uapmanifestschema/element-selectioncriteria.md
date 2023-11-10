---
description: Defines selection criteria for the certificates defined for the package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: SelectionCriteria (Windows 10)
ms.assetid: 5f3d9db3-5b2d-44ec-9607-dcc15f0854b5
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# SelectionCriteria (Windows 10)

Defines selection criteria for the certificates defined for the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Certificates\>](element-certificates.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<SelectionCriteria\>**

## Syntax

```xml
<SelectionCriteria
  HardwareOnly = 'An optional boolean value.'
  AutoSelect = 'An optional boolean value.' />
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AutoSelect** | Indicates whether the certificates are selected automatically. *True* if they are selected automatically, otherwise *false*. | An optional boolean value. | No |  |
| **HardwareOnly** | Indicates whether specified certificates are hardware-specific. *True* if they are hardware-specific, otherwise *false*. | An optional boolean value. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Certificates](element-certificates.md) | Declares a package extensibility point of type *windows.certificates*. The app requires one or more certificates from the specified certificate stores. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
