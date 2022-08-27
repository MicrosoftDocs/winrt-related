---
description: A certificate for use with the package and placed in the system certificate stores (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Certificate (Windows 10)
ms.assetid: d3682c0f-fb91-466a-a612-a60c1e6025c9
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Certificate (Windows 10)

A certificate for use with the package and placed in the system certificate stores.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Certificates\>](element-certificates.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Certificate\>**

## Syntax

```xml
<Certificate
  StoreName = 'A string with a value between 1 and 50 characters in length that cannot contain these characters: <, >, :, ", /, \, |, ?, or *.'
  Content = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. />'
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| Content | The path to the certificate content to place in the store. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `&`, `"`, `/`, `\`, `|`, `?`, or `*`. | Yes |  |
| StoreName | The store name in which the certificate should be placed. | A string with a value between 1 and 50 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, or `*`. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Certificates](element-certificates.md) | Declares a package extensibility point of type **windows.certificates**. The app requires one or more certificates from the specified certificate stores. |

## Requirements

|   |  Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
