---
title: com4:DefaultIcon
description: Provides default icon information for iconic presentations of objects. (com4:DefaultIcon)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:DefaultIcon



## Description
Provides default icon information for iconic presentations of objects.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-class.md">&lt;com4:Class&gt;</a></dt>
<dd>
<b>&lt;com4:DefaultIcon&gt;</b>
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
<com4:DefaultIcon     Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
    ResourceIndex = Integer.
></com4:DefaultIcon>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | The full path to the executable name of the server application. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| ResourceIndex | The integer at the end of the path, separated from the path by a comma, e.g., C:\Foo\Bar\Baz.exe,5. See the nIconIndex parameter in [ExtractIcon](/windows/win32/api/shellapi/nf-shellapi-extracticona) for more details. | Integer.| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
