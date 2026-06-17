---
title: SelectionCriteria
description: Defines selection criteria for the certificates defined for the package (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, Certificates, SelectionCriteria]
---

# SelectionCriteria

Defines selection criteria for the certificates defined for the package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Certificates>`](element-f-certificates.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<SelectionCriteria>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <SelectionCriteria
    HardwareOnly = 'An optional boolean value.'
    AutoSelect = 'An optional boolean value.' />
</Package>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **HardwareOnly** | Indicates whether specified certificates are hardware-specific. *True* if they are hardware-specific, otherwise *false*. | An optional boolean value. | No |  |
| **AutoSelect** | Indicates whether the certificates are selected automatically. *True* if they are selected automatically, otherwise *false*. | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Certificates](element-f-certificates.md) | Declares a package extensibility point of type **windows.certificates**. The app requires one or more certificates from the specified certificate stores. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
