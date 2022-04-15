---
title: uap2:Url
description: Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL.

keywords: windows 10, uwp, schema, package, manifest
ms.topic: reference
ms.date: 03/28/2022

---

# uap2:Url

Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL.

## Element Hierarchy

[ < Package > ](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Applications > ](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Application > ](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Extensions > ](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP2:Extension > ](element-uap2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP2:WebAccountProvider > ](element-uap2-webaccountprovider.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP2:ManagedUrls > ](element-uap2-managedurls.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**< UAP2:Url >**

## Syntax

```syntax 
<uap2:Url>

  A string between 1 and 32767 characters in length in the form of a valid web url.

</uap2:Url>
```

## Attributes

None.

## Child Elements

None.

## Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [uap2:ManagedUrls](element-uap2-managedurls.md) | Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies. |

## Requirements

| Namespace | Manifest Path |
|-----------|---------------|
| **UAP2** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2`