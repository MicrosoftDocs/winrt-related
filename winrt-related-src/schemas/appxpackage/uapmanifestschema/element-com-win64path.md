---
title: com:Win64Path
description: A path to the 64-bit type library (in ComInterface/TypeLib).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com:Extension, com:ComInterface, com:TypeLib, com:Version, com:Win64Path]
---

# com:Win64Path

A path to the 64-bit type library.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:ComInterface>`](element-com-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:TypeLib>`](element-com-interface-typelib.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Version>`](element-com-version.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:Win64Path>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:ComInterface>`](element-com-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:TypeLib>`](element-com-interface-typelib.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Version>`](element-com-version.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:Win64Path>`**  


## Syntax

```xml
<com:Win64Path
  Path = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceId = 'An optional positive integer.' />
```


## Attributes
| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|**Path**| A path to the 32-bit TypeLib relative to the package root. Path must reference a file in the package. |A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *.|Yes||
|**ResourceId**| The integer at the end of the default value of the Win32Path, separated from the path by a backslash, e.g., C:\Foo\Bar\Baz.exe\5. |An optional positive integer.|No||

## Child elements

None.


## Parent elements

| Parent element | Description |
|-|-|
| [com:Version](element-com-version.md) | Version number and additional information about the type library. |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |


## Remarks

> [!NOTE]  
> You must specify both a Win32Path and a Win64Path in the [Version](element-com-version.md).

## Examples

<!-- Author content goes here -->
