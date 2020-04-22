---

ms.assetid: 4e586752-228a-4165-9f8d-699634c4ad33
title: com:Win32Path (in ComInterface/TypeLib)
description: A path to the 32-bit type library. 

ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:Win32Path (in ComInterface/TypeLib)

## Description
A path to the 32-bit type library. 

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
<dd>
<dl>
<dt><a href="element-com-version.md">&lt;com:Version&gt;</a></dt>
<dd><b>&lt;com:Win32Path&gt;</b></dd>
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
</dd>
</dl>



## Syntax
```syntax
<com:Win32Path
    Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, %, ", |, ?, or *.
    ResourceId? = An integer type. >
</com:Win32Path>
```

## Key
`?`    optional (zero or one) 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Path | A path to the 32-bit TypeLib relative to the package root. Path must reference a file in the package. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, %, ", &#124;, ?, or *. | Yes |
| ResourceId | The integer at the end of the default value of the Win32Path, separated from the path by a backslash, e.g., C:\Foo\Bar\Baz.exe\5. | An integer type. | No |

## Remarks
> [!NOTE]  
> You must specify both a Win32Path and a Win64Path in the [Version](element-com-version.md).

## Examples

## Requirements
|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |