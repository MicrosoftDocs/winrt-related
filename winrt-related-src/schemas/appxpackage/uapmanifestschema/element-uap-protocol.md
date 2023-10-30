---
description: Declares an app extensibility point of type windows.protocol (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:Protocol (Windows 10)
ms.assetid: b92c542e-d4a4-4d6d-8a1b-257c4a43aecc
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:Protocol (Windows 10)

Declares an app extensibility point of type *windows.protocol*. A URI association indicates that the app is registered to handle URIs with the specified scheme.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:Protocol\>**

## Syntax

```xml
<uap:Protocol
  Name = 'A string with a value between 2 and 39 characters in length that contains numbers, lowercase letters, periods ("."), plus signs ("+"), or dashes ("-"). The string cannot start with a period (".").'
  DesiredView = 'A string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".'
  ReturnResults = 'An optional string that can have one of the following values: "none", "always", "optional".' >

  <!-- Child elements -->
  uap:Logo?
  & uap:DisplayName?
  & desktop7:ProgId
</uap:Protocol>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the URI scheme (such as `mailto`). This name must be unique for the package. | A string with a value between 2 and 39 characters in length that contains numbers, lowercase letters, periods (`.`), plus signs (`+`), or dashes (`-`). The string cannot start with a period (`.`). | Yes |  |
| **DesiredView** | The desired amount of screen space to use when the appointment launches. | A string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, or *useMinimum*. | No |  |
| **ReturnResults** | Specifies whether the app returns a value when invoked via a URI activation. | An optional string that can have one of the following values: "none" (does not return a value), "always" (URI activation will always return a result), "optional" (URI activation will return a result if it is activated for results using [LaunchUriForResultsAndContinueAsync](/previous-versions/windows/dn904655(v=win.10))). | No |  |

### Child elements

| Child element | Description |
|-|-|
| [uap:DisplayName](element-1-uap-displayname.md) | A friendly name that can be displayed to users. |
| [uap:Logo](element-1-uap-logo.md) | A path to a file that contains an image. |
| [desktop7:ProgId](element-desktop7-progId.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
