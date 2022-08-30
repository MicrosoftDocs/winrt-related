---
ms.assetid: b9fbedc4-6f3f-45ae-807a-aa4c53abd9be
title: com:Win32Path (in Package/Extensions)
description: A path to the 32-bit type library (in Package/Extensions).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:Win32Path (in Package/Extensions)

A path to the 32-bit type library.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-package-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Interface\>](element-com-package-interface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:TypeLib\>](element-com-package-typelib.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Version\>](element-com-package-version.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Win32Path\>**

## Syntax

```xml
<com:Win32Path
    Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, %, ", |, ?, or *.'
    ResourceId = 'An optional integer value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | A path to the 32-bit TypeLib relative to the package root. Path must reference a file in the package. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `%`, `"`, `|`, `?`, or `*`. | Yes |  |
| **ResourceId** | The integer at the end of the default value of the Win32Path, separated from the path by a backslash (for example, C:\Foo\Bar\Baz.exe\5). | An optional integer value. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com:Version](element-com-package-version.md) | Version number and additional information about the type library. |

## Remarks

> [!NOTE]  
> You must specify both a Win32Path and a Win64Path in the [Version](element-com-package-version.md).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
