---
title: com4:Version
description: Version number and additional information about the type library. (com4:Version)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:Extension, com4:ComInterface, com4:TypeLib, com4:Version]
---

# com4:Version

Version number and additional information about the type library.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComInterface>`](element-com4-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:TypeLib>`](element-com4-class-typelib.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:Version>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComInterface>`](element-com4-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:TypeLib>`](element-com4-class-typelib.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:Version>`**

## Syntax

```xml
<com4:Version
  VersionNumber = 'A required one to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a'
  LocaleId = 'An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).'
  LibraryFlag = 'An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).'
  HelpDirectory = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.' >

  <!-- Child elements -->
  com4:Win32Path?
  com4:Win64Path?

</com4:Version>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **VersionNumber** | The name of the version number. | A one to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a | Yes |  |
| **LocaleId** | An Id representing geographic location. | An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). | No | 0 |
| **LibraryFlag** | An integer value from the [LIBFLAGS](/windows/win32/api/oaidl/ne-oaidl-libflags) enumeration. | An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). | No |  |
| **HelpDirectory** | The HELPDIR subkey. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **DisplayName** | The display name for the version number. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [com4:Win32Path](element-com4-win32path.md) | A path to the 32-bit type library. |
| [com4:Win64Path](element-com4-win64path.md) | A path to the 64-bit type library. |

## Parent elements

| Parent element | Description |
|-|-|
| **com4:TypeLib** | <!-- TODO: Add description --> |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

You must specify either a Win32Path or a Win64Path, and can specify both. Generating and registering both 32-bit and 64-bit formats for a type library can improve performance if its interfaces are used from client processes of both 32-bit and 64-bit architectures.

## Examples

<!-- Author content goes here -->
