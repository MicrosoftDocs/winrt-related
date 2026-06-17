---
title: uap2:WebAccountProvider
description: Declares an app extensibility point of the type windows.webAccountProvider.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package, manifest
no-loc: [Package, Applications, Application, Extensions, uap2:Extension, uap2:WebAccountProvider]
---

# uap2:WebAccountProvider

Declares an app extensibility point of the type windows.webAccountProvider.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap2:Extension>`](element-uap2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap2:WebAccountProvider>`**  

## Syntax

```xml
<uap2:WebAccountProvider
  Url = 'A required string between 1 and 32767 characters in length in the form of a valid web URL.'
  BackgroundEntryPoint = 'A required string between 1 and 256 characters in length that cannot start or end with a whitespace character.'
  DisplayName = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DisplayPurpose = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  Square44x44Logo = 'An optional string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both.' >

  <!-- Child elements -->
  uap2:ManagedUrls?

</uap2:WebAccountProvider>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Url** | Specifies a URL to which a plugin may send cookies. | A string between 1 and 32767 characters in length in the form of a valid web URL. | Yes |  |
| **BackgroundEntryPoint** | The activatable class ID. | A string between 1 and 256 characters in length that cannot start or end with a whitespace character. | Yes |  |
| **DisplayName** | A friendly name that can be displayed to users | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **DisplayPurpose** | Represents the purpose for the account provider. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **Square44x44Logo** | A path to a file that contains an image | An optional string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `&#124;`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap2:ManagedUrls](element-uap2-managedurls.md) | Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap2:Extension](element-uap2-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
