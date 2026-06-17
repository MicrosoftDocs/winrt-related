---
title: uap2:ManagedUrls
description: Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package, manifest
no-loc: [Package, Applications, Application, Extensions, uap2:Extension, uap2:WebAccountProvider, uap2:ManagedUrls]
---

# uap2:ManagedUrls

Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap2:Extension>`](element-uap2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap2:WebAccountProvider>`](element-uap2-webaccountprovider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap2:ManagedUrls>`**  

## Syntax

```xml
<uap2:ManagedUrls>

  <!-- Child elements -->
  uap2:Url{1,200}

</uap2:ManagedUrls>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap2:Url](element-uap2-url.md) | Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap2:WebAccountProvider](element-uap2-webaccountprovider.md) | Declares an app extensibility point of the type windows.webAccountProvider. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
