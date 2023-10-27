---
description: Declares an app extensibility point of the type windows.webAccountProvider.
title: uap2:WebAccountProvider
keywords: windows 10, uwp, schema, package, manifest
ms.topic: reference
ms.date: 03/28/2022
---

# uap2:WebAccountProvider

Declares an app extensibility point of the type windows.webAccountProvider.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<uap2:Extension\>](element-uap2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<uap2:WebAccountProvider\>**

## Syntax

```xml
<uap2:WebAccountProvider
  Url = 'A string with a value between 1 and 32767 characters in length in the form of a valid web url.'
  BackgroundEntryPoint = 'A string with a value between 1 and 256 characters in length.'
  DisplayName = 'A string with a value between 1 and 256 characters in length.'
  DisplayPurpose = 'A string with a value between 1 and 2048 characters in length.'
  Square44x44Logo = 'A string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters.' >

  <!-- Child Elements -->
  uap2:managedUrls?

</uap2:webAccountProvider>

```

## Attributes and elements

### Attributes

| Attribute | Description | Data Type | Required | Default value |
|-|-|-|-|-|
| **Url** | Specifies a URL to which a plugin may send cookies. | A string with a value between 1 and 32767 characters in length in the form of a valid web url. | Yes |  |
| **BackgroundEntryPoint** | The activatable class ID. | A string with a value between 1 and 256 characters in length. | Yes |  |
| **DisplayName** | A friendly name that can be displayed to users | A string with a value between 1 and 256 characters in length. This string is localizable. | No |  |
| **DisplayPurpose** | Represents the purpose for the account provider. | A string between 1 and 2048 characters in length. | No |  |
| **Square44x44Logo** | A path to a file that contains an image | A string with a value between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters cannot be the first or last characters. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [uap2:ManagedUrls](element-uap2-managedurls.md) | Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap2:Extension](element-uap2-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2`
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
