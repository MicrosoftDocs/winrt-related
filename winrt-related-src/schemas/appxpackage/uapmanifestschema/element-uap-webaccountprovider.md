---
description: Declares an app extensibility point of type windows.webAccountProvider.
Search.Product: eADQiWindows 10XVcnh
title: uap:WebAccountProvider (Windows 10)
ms.assetid: 9e38d699-4a07-46ac-88d4-70109fbaa892
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:WebAccountProvider (Windows 10)

Declares an app extensibility point of type *windows.webAccountProvider*.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:WebAccountProvider\>**

## Syntax

```xml
<uap:WebAccountProvider
    Url = 'A string with a value between 1 and 32767 characters in length in the form of a valid web url.'
    BackgroundEntryPoint = 'A string with a value between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type.'
 >

  <!-- Child elements -->
  uap:ManagedUrls?

</uap:WebAccountProvider>
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Url** | The Web Account provider identifier (URL). Should be a valid HTTPS URL. Used to uniquely identify the provider when called from an app. | A string between 1 and 32767 characters in length in the form of a valid web url. | Yes |  |
| **BackgroundEntryPoint** | Entry Point for UI-less get token request. | A string with a value between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [uap:ManagedUrls](element-uap-managedurls.md) | Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Examples

```xml
<Extension
    Category="windows.webAccountProvider">
    <WebAccountProvider
        Url="https://login.live.com"
        BackgroundEntryPoint="MSA.WebAccountProviderTask"/>
</Extension>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
