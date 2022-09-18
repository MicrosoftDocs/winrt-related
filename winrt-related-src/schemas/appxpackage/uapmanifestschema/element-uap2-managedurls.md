---
title: uap2:ManagedUrls
description: Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies.
keywords: windows 10, uwp, schema, package, manifest
ms.topic: reference
ms.date: 03/28/2022
---

# uap2:ManagedUrls

Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap2:Extension\>](element-uap2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap2:WebAccountProvider\>](element-uap2-webaccountprovider.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap2:ManagedUrls\>**

## Syntax

```xml
<uap2:ManagedUrls>

  <!-- Child Elements -->
  uap2:Url

</uap2:ManagedUrls>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap2:Url](element-uap2-url.md) | Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap2:WebAccountProvider](element-uap2-webaccountprovider.md) | Declares an app extensibility point of the type windows.webAccountProvider. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2` |
