---
title: uap17:PackageExtension
description: Declares an app extensibility point of type windows.packageExtension.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, uap17:Extension, uap17:PackageExtension]
---

# uap17:PackageExtension

Declares an app extensibility point of type windows.packageExtension.

Declares an app extensibility point of type *windows.packageExtension*. This element indicates which categories of extensions the package intends to consume and/or host.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap17:Extension>`](element-uap17-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap17:PackageExtension>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap17:Extension>`](element-uap17-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap17:PackageExtension>`**  

## Syntax

```xml
<uap17:PackageExtension
  Name = 'A required string with a value between 2 and 65519 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.'
  Id = 'A required string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.'
  PublicFolder = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  DisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  Description = 'An optional string between 1 and 2048 characters in length.' >

  <!-- Child elements -->
  uap17:Properties?

</uap17:PackageExtension>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | <!-- TODO: Add description --> | A string with a value between 2 and 65519 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | Yes |  |
| **Id** | <!-- TODO: Add description --> | A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | Yes |  |
| **PublicFolder** | <!-- TODO: Add description --> | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **DisplayName** | <!-- TODO: Add description --> | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Description** | <!-- TODO: Add description --> | An optional string between 1 and 2048 characters in length. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap17:Properties](element-uap17-properties.md) | Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system. The information is only read by the host app. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap17:Extension](element-uap17-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/17` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
