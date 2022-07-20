---
title: com4:InProcessServerDll
description: Specifies the path and processor architecture of an in-process server DLL. (com4:InProcessServerDll)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessServerDll



## Description
Specifies the path and processor architecture of an in-process server DLL.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-inprocessserver.md">&lt;com4:InProcessServer&gt;</a></dt>
<dd>
<b>&lt;com4:InProcessServerDll&gt;</b>
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
<com4:InProcessServerDll     Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".
    ProcessorArchitecture = "x86" | "x64" | "arm" | "arm64" | "x86a64"
></com4:InProcessServerDll>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | The full path to the in-process server DLL. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *, ending with the case-insensitive file extension ".dll".| Yes |
| ProcessorArchitecture | The processor architecture of the in-process server DLL. | One of the following values: "x86" , "x64" , "arm" , "arm64" , "x86a64"| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
