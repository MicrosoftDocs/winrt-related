---
author: laurenhughes
ms.assetid: 85160560-7b79-45ad-904e-15b998d12c1b
title: com:Version
description: Version number and additional information about the type library.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, com
---


# com:Version

## Description
Version number and additional information about the type library.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-extension.md">&lt;com:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-cominterface.md">&lt;com:ComInterface&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-typelib.md">&lt;com:TypeLib&gt;</a></dt>
<dd><b>&lt;com:Version&gt;</b></dd>
</dl>
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
</dd>
</dl>

## Syntax
```syntax
<com:Version
    VersionNumber = One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a
    LocaleId? = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).
    LibraryFlag? = An integer value in the range of 0 to 15.
    HelpDirectory? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >

  <!-- Child elements -->
  ( Win32Path,
    Win64Path )  
</com:Version>
```

## Key
`?`    optional (zero or one) 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| VersionNumber | The name of the version number. | One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a | Yes |
| LocaleId | An Id representing geographic location. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). | No |
| LibraryFlag | An integer value from the [LIBFLAGS](https://msdn.microsoft.com/library/windows/desktop/ms221149.aspx) enumeration. | An integer value in the range of 0 to 15. | No |
| HelpDirectory | The HELPDIR subkey. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |

## Child Elements
 
| Child Element | Description |
|---------------|-------------|
| [Win32Path](element-com-win32path.md) | A path to the 32-bit type library. |
| [Win64Path](element-com-win64path.md) | A path to the 64-bit type library. |

## Remarks
> [!NOTE]  
> You must specify both a Win32Path and a Win64Path.

## Examples

## Requirements
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>