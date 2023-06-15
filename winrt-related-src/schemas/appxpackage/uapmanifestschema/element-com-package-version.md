---
ms.assetid: 4aaee0da-1eff-4a8f-972e-0f8706ab2ca0
title: com:Version (in Package/Extensions)
description: Version number and additional information about the type library (in Package/Extensions).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:Version (in Package/Extensions)

Version number and additional information about the type library.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-package-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Interface\>](element-com-package-interface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:TypeLib\>](element-com-package-typelib.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Version\>**

## Syntax

```xml
<com:Version
    VersionNumber = 'A string with a value between one to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters (for example, 1.5a).'
    LocaleId = 'An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case).'
    LibraryFlag = 'An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case).'
    HelpDirectory = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  Win32Path?,
  Win64Path?

</com:Version>
```

## Key

`?`    optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **VersionNumber** | The name of the version number. | A string with a value between one to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters (for example, 1.5a). | Yes |  |
| **LocaleId** | An Id representing geographic location. | An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case). | No |  |
| **LibraryFlag** | An integer value from the [LIBFLAGS](/windows/win32/api/oaidl/ne-oaidl-libflags) enumeration. | An optional string in hexadecimal format containing numbers or the letters a, b, c, d, e, or f (capital or lower case). | No |  |
| **HelpDirectory** | The HELPDIR subkey. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Win32Path](element-com-package-win32path.md) | A path to the 32-bit type library. |
| [Win64Path](element-com-package-win64path.md) | A path to the 64-bit type library. |

### Parent elements

| Parent element | Description |
|-|-|
| [com:TypeLib](element-com-package-typelib.md) | Registers a type library. |

## Remarks

For more information about type libraries and the attributes on this page, see [Registering a Type Library](/previous-versions/windows/desktop/automat/registering-a-type-library).

> [!NOTE]  
> You must specify both a Win32Path and a Win64Path.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
