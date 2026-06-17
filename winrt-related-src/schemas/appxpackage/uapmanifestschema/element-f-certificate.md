---
title: Certificate
description: A certificate for use with the package and placed in the system certificate stores (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, Certificates, Certificate]
---

# Certificate

A certificate for use with the package and placed in the system certificate stores.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Certificates>`](element-f-certificates.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Certificate>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Certificate
    StoreName = 'A required value. <!-- TODO: Add description for t:ST_CertificateStoreName -->'
    Content = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.' />
</Package>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **StoreName** | The store name in which the certificate should be placed. | A value. <!-- TODO: Add data type for t:ST_CertificateStoreName --> | Yes |  |
| **Content** | The path to the certificate content to place in the store. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |

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
