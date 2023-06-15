---
description: Indicates whether the certificates for the package are exclusive to the package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: TrustFlags (Windows 10)
ms.assetid: 44ea0d79-4774-4152-8f69-c5d9ff9287aa
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# TrustFlags (Windows 10)

Indicates whether the certificates for the package are exclusive to the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Certificates\>](element-certificates.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<TrustFlags\>**

## Syntax

```xml
<TrustFlags
  ExclusiveTrust = 'A boolean value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ExclusiveTrust** | Indicates whether the declared certificates are exclusive to the package. *true* if they are exclusive to the package, otherwise *false*. | A boolean value. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Certificates](element-certificates.md) | Declares a package extensibility point of type *windows.certificates*. The app requires one or more certificates from the specified certificate stores. |

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
