---
title: com4:Version
description:  Version number and additional information about the type library. (com4:Version)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Version

Version number and additional information about the type library.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:TypeLib\>](element-com4-typelib.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Version\>**

## Syntax

```xml
<com4:Version
  VersionNumber = 'One to three alphanumeric characters, separated by a period, followed by one to three more alphanumeric characters (for example, 1.5a).'
  LocaleId = 'A string with a value in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case).'.
  LibraryFlag = 'A string with a value in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case).'
  HelpDirectory = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.' >

  <!-- Child elements -->
  Win32Path{1,1000}
  Win64Path{1,1000}

</com4:Version>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **VersionNumber** | The name of the version number. | One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a| Yes |  |
| **LocaleId** | An Id representing geographic location. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).| Yes |  |
| **LibraryFlag** | An integer value from the [LIBFLAGS](/windows/win32/api/oaidl/ne-oaidl-libflags) enumeration. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).| Yes |  |
| **HelpDirectory** | The HELPDIR subkey. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |  |
| **DisplayName** | The display name for the version number. | A string between 1 and 256 characters in length. This string is localizable.| Yes |  |

### Child Elements

| Child element | Description |
|-|-|
| [Win32Path](element-com4-win32path.md) | A path to the 32-bit type library. |
| [Win64Path](element-com4-win64path.md) | A path to the 64-bit type library. |

### Parent elements

| Parent element | Description |
|-|-|
| [com4:TypeLib](element-com4-typelib.md) | Registers a type library. |

## Remarks

You must specify either a Win32Path or a Win64Path, and can specify both. Generating and registering both 32-bit and 64-bit formats for a type library can improve performance if its interfaces are used from client processes of both 32-bit and 64-bit architectures.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
