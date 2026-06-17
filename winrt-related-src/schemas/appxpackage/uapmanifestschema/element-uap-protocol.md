---
title: uap:Protocol
description: Declares an app extensibility point of type windows.protocol (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:Protocol]
---

# uap:Protocol

Declares an app extensibility point of type *windows.protocol*. A URI association indicates that the app is registered to handle URIs with the specified scheme.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:Protocol>`**  

## Syntax

```xml
<uap:Protocol
  Name = 'A required string with a value between 2 and 2048 characters in length.'
  DesiredView = 'An optional string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".'
  ReturnResults = 'An optional string that can have one of the following values: "none", "always", or "optional".' >

  <!-- Child elements -->
  uap:Logo?
  uap:DisplayName?
  uap:MigrationProgIds?
  uap:ProgId?
  uap:ProgId?

</uap:Protocol>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the URI scheme (such as `mailto`). This name must be unique for the package. | A string with a value between 2 and 2048 characters in length. | Yes |  |
| **DesiredView** | The desired amount of screen space to use when the appointment launches. | An optional string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, *useMinimum*. | No |  |
| **ReturnResults** | Specifies whether the app returns a value when invoked via a URI activation. | An optional string that can have one of the following values: *none*, *always*, *optional*. | No |  |

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
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```xml
<Applications>
  <Application
    Id="App"
    StartPage="default.html">
    <Extensions>
      <uap:Extension
        Category="windows.protocol">
        <uap:Protocol
          Name="alsdk" />
      </uap:Extension>
    </Extensions>
  </Application>
</Applications>
```

## See also
**Tasks**
[How to handle URI activation](/previous-versions/windows/apps/hh452686(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))
