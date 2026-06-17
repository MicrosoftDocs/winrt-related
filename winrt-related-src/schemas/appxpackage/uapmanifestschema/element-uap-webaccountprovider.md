---
title: uap:WebAccountProvider
description: Declares an app extensibility point of type windows.webAccountProvider.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:WebAccountProvider]
---

# uap:WebAccountProvider

Declares an app extensibility point of type *windows.webAccountProvider*.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:WebAccountProvider>`**  

## Syntax

```xml
<uap:WebAccountProvider
  Url = 'A required string between 1 and 32767 characters in length in the form of a valid web URL.'
  BackgroundEntryPoint = 'A required string between 1 and 256 characters in length that cannot start or end with a whitespace character.' >

  <!-- Child elements -->
  uap:ManagedUrls?

</uap:WebAccountProvider>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Url** | The Web Account provider identifier (URL). Should be a valid HTTPS URL. Used to uniquely identify the provider when called from an app. | A string between 1 and 32767 characters in length in the form of a valid web URL. | Yes |  |
| **BackgroundEntryPoint** | Entry Point for UI-less get token request. | A string between 1 and 256 characters in length that cannot start or end with a whitespace character. | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| [uap:ManagedUrls](element-uap-managedurls.md) | Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<Extension
    Category="windows.webAccountProvider">
    <WebAccountProvider
        Url="https://login.live.com"
        BackgroundEntryPoint="MSA.WebAccountProviderTask"/>
</Extension>
```
