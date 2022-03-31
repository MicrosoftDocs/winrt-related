---
title: com4:InProcessHandlerDll
description: Specifies the path and processor architecture of an in-process handler DLL. (com4:InProcessHandlerDll)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessHandlerDll



## Description
Specifies the path and processor architecture of an in-process handler DLL.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-inprocesshandler.md">&lt;com4:InProcessHandler&gt;</a></dt>
<dd>
<b>&lt;com4:InProcessHandlerDll&gt;</b>
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
<com4:InProcessHandlerDll     Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".
    ProcessorArchitecture = "x86" | "x64" | "arm" | "arm64" | "x86a64"
></com4:InProcessHandlerDll>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path |  The full path to the in-process handler DLL. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *, ending with the case-insensitive file extension ".dll".| Yes |
| ProcessorArchitecture | The processor architecture of the in-process handler DLL. | One of the following values: "x86" , "x64" , "arm" , "arm64" , "x86a64"| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
