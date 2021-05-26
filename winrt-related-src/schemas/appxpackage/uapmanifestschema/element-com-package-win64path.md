---

ms.assetid: a79b9fa6-60bd-40d2-80b7-bac80d439e84
title: com:Win64Path (in Package/Extensions)
description: A path to the 64-bit type library.

ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:Win64Path (in Package/Extensions)

## Description
A path to the 64-bit type library.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-package-cominterface.md">&lt;ComInterface&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-package-typelib.md">&lt;TypeLib&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-package-version.md">&lt;Version&gt;</a></dt>
<dd><b>&lt;Win64Path&gt;</b></dd>
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
<Win64Path
    Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, %, ", |, ?, or *.
    ResourceId? = An integer type. >
</Win64Path>
```

## Key
`?`    optional (zero or one) 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Path | A path to the 64-bit TypeLib relative to the package root. Path must reference a file in the package. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, %, ", &#124;, ?, or *. | Yes |
| ResourceId | The integer at the end of the default value of the Win64Path, separated from the path by a backslash, e.g., C:\Foo\Bar\Baz.exe\5. | An integer type. | No |

## Remarks
> [!NOTE]  
> You must specify both a Win32Path and a Win64Path in the [Version](element-com-package-version.md).

## Examples

## Requirements
|               |    Value                                                         |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |