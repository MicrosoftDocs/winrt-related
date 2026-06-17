---
title: uap3:Protocol
description: Declares an app extensibility point of type windows.protocol. A URI association indicates the app is registered to handle URIs with the specified scheme.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap3:Extension, uap3:Protocol]
keywords: windows 10, uwp, schema, manifest, extension
---

# uap3:Protocol

Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:Extension>`](element-uap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:Protocol>`**

## Syntax

```xml
<uap3:Protocol
  Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  Name = 'A required string with a value between 2 and 2048 characters in length.'
  DesiredView = 'An optional string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".'
  ReturnResults = 'An optional string that can have one of the following values: "none", "always", or "optional".' >

  <!-- Child elements -->
  uap3:Logo?
  uap3:DisplayName?
  uap3:MigrationProgIds?
  uap3:ProgId?
  uap3:ProgId?

</uap3:Protocol>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Parameters** | The class ID associated with this media content. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **Name** | <!-- TODO: Add description --> | A string with a value between 2 and 2048 characters in length. | Yes |  |
| **DesiredView** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, *useMinimum*. | No |  |
| **ReturnResults** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *none*, *always*, *optional*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap:Logo](element-uap-logo.md) | A path to a file that contains an image. |
| [uap:DisplayName](element-uap-displayname.md) | A friendly name that can be displayed to users. |
| [rescap3:MigrationProgIds](element-rescap3-migrationprogids.md) | Contains [programmatic identifier (ProgID)](/windows/win32/shell/fa-progids) values that describes the application, component, and version of each desktop application from which you want to inherit file associations. |
| [previewappcompat:ProgId](element-previewappcompat-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique. |
| [desktop7:ProgId](element-desktop7-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
