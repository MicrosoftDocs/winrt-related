---
title: com4:Win32Path
description: A path to the 32-bit type library. (com4:Win32Path)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Win32Path



## Description
A path to the 32-bit type library.



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
<dl><dt><a href = "element-com4-version.md">&lt;com4:Version&gt;</a></dt>
<dd>
<b>&lt;com4:Win32Path&gt;</b>
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
<com4:Win32Path     Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
    ResourceId? = A positive integer.
></com4:Win32Path>
```

## Key
`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | A path to the 32-bit TypeLib relative to the package root. Path must reference a file in the package. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| ResourceId | The integer at the end of the default value of the Win32Path, separated from the path by a backslash, e.g., C:\Foo\Bar\Baz.exe\5. | A positive integer.| No |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
