---
title: Certificates
description: Declares a package extensibility point of type windows.certificates (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, Certificates]
---

# Certificates

Declares a package extensibility point of type **windows.certificates**. The app requires one or more certificates from the specified certificate stores.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Certificates>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Certificates>

    <!-- Child elements -->
    Certificate{0,100}
    TrustFlags?
    SelectionCriteria?

  </Certificates>
</Package>
```

### Key

`?` optional (zero or one)
`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | A certificate for use with the package and placed in the system certificate stores. |  |  |  |
|  | Indicates whether the certificates for the package are exclusive to the package. |  |  |  |
|  | Defines selection criteria for the certificates defined for the package. |  |  |  |
|  | Description |  |  |  |
|  | - |  |  |  |
|  | Declares an extensibility point for the package. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

| Child element | Description |
|-|-|
| [Certificate](element-f-certificate.md) | A certificate for use with the package and placed in the system certificate stores. |
| [TrustFlags](element-f-trustflags.md) | Indicates whether the certificates for the package are exclusive to the package. |
| [SelectionCriteria](element-f-selectioncriteria.md) | Defines selection criteria for the certificates defined for the package. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-f-package-extension.md) | Declares an extensibility point for the package. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->

## See also

**Tasks**
[Working with certificates](/previous-versions/windows/apps/hh465044(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))
