---
title: uap2:Url
description: Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package, manifest
no-loc: [Package, Applications, Application, Extensions, uap2:Extension, uap2:WebAccountProvider, uap2:ManagedUrls, uap2:Url]
---

# uap2:Url

Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap2:Extension>`](element-uap2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap2:WebAccountProvider>`](element-uap2-webaccountprovider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap2:ManagedUrls>`](element-uap2-managedurls.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap2:Url>`**  

## Syntax

```xml
<uap2:Url>
    <!-- TODO: Add value description -->
</uap2:Url>
```

## Value

<!-- TODO: Add value description -->

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap2:ManagedUrls](element-uap2-managedurls.md) | Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
