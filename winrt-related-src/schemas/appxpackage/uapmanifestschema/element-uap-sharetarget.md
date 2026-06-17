---
title: uap:ShareTarget
description: Declares an app extension point of type windows.shareTarget (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:ShareTarget]
---

# uap:ShareTarget

Declares an app extension point of type *windows.shareTarget*. The app can share the specified types of files.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:ShareTarget>`**  

## Syntax

```xml
<uap:ShareTarget
  Description = 'An optional string with a value between 1 and 256 characters in length.'
  uap10:DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.' >

  <!-- Child elements -->
  uap:SupportedFileTypes?
  uap:DataFormat{0,10000}

</uap:ShareTarget>
```

### Key

`?` optional (zero or one)
`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Description** | The description of the share target. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **uap10:DisplayName** | <!-- TODO: Add description --> | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap:SupportedFileTypes](element-uap-sharetarget-supportedfiletypes.md) | Defines the file types that the app can share. |
| [uap:DataFormat](element-uap-dataformat.md) | Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |

## Remarks

The Share feature provides access to a list of target apps that can receive data that the user wants to share. This extensibility point enables your app to be included in the list of share targets.

[ShareTarget](../appxmanifestschema/element-sharetarget.md) must specify either [SupportedFileTypes](../appxmanifestschema/element-supportedfiletypes.md) element, or at least one [DataFormat](../appxmanifestschema/element-dataformat.md) element. It cannot omit both. The schema allows omitting both, but semantic validation will fail.

## Examples

```xml
<uap:Extension
  Category="windows.shareTarget">
  <uap:ShareTarget>
    <uap:SupportedFileTypes>
      <uap:SupportsAnyFileType />
    </uap:SupportedFileTypes>
    <uap:DataFormat>Text</uap:DataFormat>
    <uap:DataFormat>Uri</uap:DataFormat>
    <uap:DataFormat>Bitmap</uap:DataFormat>
    <uap:DataFormat>Html</uap:DataFormat>
    <uap:DataFormat>http://schema.org/Book</DataFormat>
  </uap:ShareTarget>
</uap:Extension>
```

## See also
**Tasks**
[Adding share](/previous-versions/windows/apps/hh758314(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))
