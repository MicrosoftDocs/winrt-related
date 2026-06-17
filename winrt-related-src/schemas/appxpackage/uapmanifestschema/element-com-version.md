---
title: com:Version
description: Version number and additional information about the type library  (in ComInterface/TypeLib).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com:Extension, com:ComInterface, com:TypeLib, com:Version]
---

# com:Version

Version number and additional information about the type library.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:ComInterface>`](element-com-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:TypeLib>`](element-com-interface-typelib.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:Version>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:ComInterface>`](element-com-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:TypeLib>`](element-com-interface-typelib.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:Version>`**  


## Syntax

```xml
<com:Version
  VersionNumber = 'A required one to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a'
  LocaleId = 'An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).'
  LibraryFlag = 'An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).'
  HelpDirectory = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.' >

  <!-- Child elements -->
  com:Win32Path?
  com:Win64Path?

</com:Version>
```

### Key

`?` optional (zero or one)


## Attributes
| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|**VersionNumber**| The name of the version number. |A one to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a|Yes||
|**LocaleId**| An Id representing geographic location. |An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).|No|0|
|**LibraryFlag**| An integer value from the [LIBFLAGS](/windows/win32/api/oaidl/ne-oaidl-libflags) enumeration. |An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).|No||
|**HelpDirectory**| The HELPDIR subkey. |An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.|No||
| **DisplayName** | <!-- TODO: Add description --> | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |

## Child elements
| Child element | Description |
|-|-|
| [com:Win32Path](element-com-win32path.md) | A path to the 32-bit type library. |
| [com:Win64Path](element-com-win64path.md) | A path to the 64-bit type library. |

## Parent elements

| Parent element | Description |
|-|-|
| [com:TypeLib](element-com-interface-typelib.md) | <!-- TODO: Add description --> |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |


## Remarks

You must specify either a Win32Path or a Win64Path, and can specify both. Generating and registering both 32-bit and 64-bit formats for a type library can improve performance if its interfaces are used from client processes of both 32-bit and 64-bit architectures.

For more information about type libraries and the attributes on this page, see [Registering a Type Library](/previous-versions/windows/desktop/automat/registering-a-type-library).

## Examples

<!-- Author content goes here -->
