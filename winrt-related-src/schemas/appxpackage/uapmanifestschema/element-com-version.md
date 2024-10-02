---
ms.assetid: 85160560-7b79-45ad-904e-15b998d12c1b
title: com:Version
description: Version number and additional information about the type library  (in ComInterface/TypeLib).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:Version

Version number and additional information about the type library.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:TypeLib\>](element-com-typelib.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Version\>**

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Interface\>](element-com-interface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:TypeLib\>](element-com-typelib.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Version\>**

## Syntax

```xml
<com:Version
  VersionNumber = 'One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters (for example, 1.5a).'
  LocaleId = 'An optional string with a value in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case)'.
  LibraryFlag = 'An optional string with a value in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case).'
  HelpDirectory = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  Win32Path,
  Win64Path

</com:Version>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **VersionNumber** | The name of the version number. | One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters (for example, 1.5a). | Yes |  |
| **LocaleId** | An Id representing geographic location. | An optional string with a value in hexadecimal format containing numbers or the letters `a`, `b`, `c`, `d`, `e`, or `f` (capital or lower case) | No |  |
| **LibraryFlag** | An integer value from the [LIBFLAGS](/windows/win32/api/oaidl/ne-oaidl-libflags) enumeration. | An optional string with a value in hexadecimal format containing numbers or the letters `a`, `b`, `c`, `d`, `e`, or `f` (capital or lower case) | No |  |
| **HelpDirectory** | The HELPDIR subkey. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child Element | Description |
|-|-|
| [Win32Path](element-com-win32path.md) | A path to the 32-bit type library. |
| [Win64Path](element-com-win64path.md) | A path to the 64-bit type library. |

### Parent elements

| Parent Element | Description |
|-|-|
| [com:TypeLib](element-com-typelib.md) | Registers a type library. |

## Remarks

You must specify either a Win32Path or a Win64Path, and can specify both. Generating and registering both 32-bit and 64-bit formats for a type library can improve performance if its interfaces are used from client processes of both 32-bit and 64-bit architectures.

For more information about type libraries and the attributes on this page, see [Registering a Type Library](/previous-versions/windows/desktop/automat/registering-a-type-library).

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
