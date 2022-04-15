---
title: com4:Version
description:  Version number and additional information about the type library. (com4:Version)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Version



## Description

 Version number and additional information about the type library.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-typelib.md">&lt;com4:TypeLib&gt;</a></dt>
<dd>
<b>&lt;com4:Version&gt;</b>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:Version     VersionNumber = One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a
    LocaleId = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).
    LibraryFlag = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).
    HelpDirectory = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
>
<!-- Child elements -->
  Win32Path{1,1000}
  Win64Path{1,1000}
</com4:Version>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| VersionNumber | The name of the version number. | One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a| Yes |
| LocaleId | An Id representing geographic location. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).| Yes |
| LibraryFlag | An integer value from the [LIBFLAGS](/windows/win32/api/oaidl/ne-oaidl-libflags) enumeration. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).| Yes |
| HelpDirectory | The HELPDIR subkey. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| DisplayName | The display name for the version number. | A string between 1 and 256 characters in length. This string is localizable.| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Win32Path](element-com4-win32path.md) | A path to the 32-bit type library. |
| [Win64Path](element-com4-win64path.md) | A path to the 64-bit type library. |

## Remarks

You must specify either a Win32Path or a Win64Path, and can specify both. Generating and registering both 32-bit and 64-bit formats for a type library can improve performance if its interfaces are used from client processes of both 32-bit and 64-bit architectures.

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
