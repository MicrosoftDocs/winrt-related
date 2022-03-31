---
title: com4:ProxyStubDll
description: TBD
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ProxyStubDll



## Description
Specifies the path and processor architecture of a ProxyStub DLL.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-proxystub.md">&lt;com4:ProxyStub&gt;</a></dt>
<dd>
<b>&lt;com4:ProxyStubDll&gt;</b>
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
<com4:ProxyStubDll     Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
    ProcessorArchitecture = "x86" | "x64" | "arm" | "arm64" | "x86a64"
></com4:ProxyStubDll>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | A relative path to the .dll file in the app package. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| ProcessorArchitecture | The processor architecture of the ProxyStub registration. | One of the following values: "x86" , "x64" , "arm" , "arm64" , "x86a64"| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
