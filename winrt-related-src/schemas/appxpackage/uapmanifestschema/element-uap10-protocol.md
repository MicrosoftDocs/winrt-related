---
title: uap10:Protocol
description: Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, uap10:Extension, uap10:Protocol]
---

# uap10:Protocol

Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap10:Extension>`](element-uap10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:Protocol>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap10:Extension>`](element-uap10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:Protocol>`**  

## Syntax

```xml
<uap10:Protocol
  Name = 'A required string with a value between 2 and 2048 characters in length.'
  DesiredView = 'An optional string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".'
  ReturnResults = 'An optional string that can have one of the following values: "none", "always", or "optional".'
  Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  uap10:Logo?
  uap10:DisplayName?
  uap10:MigrationProgIds?
  uap10:ProgId?

</uap10:Protocol>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | A user-friendly display name for the media content. | A string with a value between 2 and 2048 characters in length. | Yes |  |
| **DesiredView** | A user-friendly description for the media content. | An optional string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, *useMinimum*. | No |  |
| **ReturnResults** | Defines the key systems used to encrypt and decrypt media content. | An optional string that can have one of the following values: *none*, *always*, *optional*. | No |  |
| **Parameters** | The class ID associated with this media content. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap10:Logo](element-uap10-logo.md) | A path to a file that contains an image. |
| [uap10:DisplayName](element-uap10-displayname.md) | A friendly name that can be displayed to users. |
| [rescap3:MigrationProgIds](element-rescap3-migrationprogids.md) | Contains [programmatic identifier (ProgID)](/windows/win32/shell/fa-progids) values that describes the application, component, and version of each desktop application from which you want to inherit file associations. |
| [previewappcompat:ProgId](element-previewappcompat-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap10:Extension](element-uap10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
