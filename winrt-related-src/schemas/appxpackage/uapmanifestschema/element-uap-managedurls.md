---
description: Provides support for multiple URLs.
Search.Product: eADQiWindows 10XVcnh
title: uap:ManagedUrls (Windows 10)
ms.assetid: 9b4709ea-cce3-472c-a799-96039241fd0b
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:ManagedUrls (Windows 10)

Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:WebAccountProvider\>](element-uap-webaccountprovider.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:ManagedUrls\>**

## Syntax

```xml
<uap:ManagedUrls>

  <!-- Child elements -->
  uap:Url{1,200}

</uap:ManagedUrls>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap:Url](element-uap-url.md) | Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:WebAccountProvider](element-uap-webaccountprovider.md) | Declares an app extensibility point of type *windows.webAccountProvider*. |

## Examples

```xml
<Extension
    Category="windows.webAccountProvider">
    <WebAccountProvider
        Url="https://login.live.com"
        BackgroundEntryPoint="MSA.WebAccountProviderTask">
        <uap:ManagedUrls>
            <uap:Url>https://login.windows.cn</uap:Url>
            <uap:Url>https://login.windows.us</uap:Url>
        </uap:ManagedUrls>
    </WebAccountProvider>
</Extension>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
