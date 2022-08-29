---
description: Declares a package extensibility point of type windows.certificates (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Certificates (Windows 10)
ms.assetid: 378edcd3-b9ef-46db-9a56-94470451829e
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Certificates (Windows 10)

Declares a package extensibility point of type **windows.certificates**. The app requires one or more certificates from the specified certificate stores.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Certificates\>**

## Syntax

```xml
<Certificates>

  <!-- Child elements -->
  Certificate{0,100},
  TrustFlags?,
  SelectionCriteria?

</Certificates>
```

### Key

`?`   optional (zero or one)
`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Certificate](element-certificate.md) | A certificate for use with the package and placed in the system certificate stores. |
| [SelectionCriteria](element-selectioncriteria.md) | Defines selection criteria for the certificates defined for the package. |
| [TrustFlags](element-trustflags.md) | Indicates whether the certificates for the package are exclusive to the package. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extension (in type: CT_PackageExtensions)](element-extension.md) | Declares an extensibility point for the package. |

## See also

**Tasks**
[Working with certificates](/previous-versions/windows/apps/hh465044(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
