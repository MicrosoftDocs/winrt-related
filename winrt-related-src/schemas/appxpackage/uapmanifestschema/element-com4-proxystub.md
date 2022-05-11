---
title: com4:ProxyStub
description: Registers a proxy stub. (com4:ProxyStub)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ProxyStub



## Description
Registers a proxy stub 



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:ProxyStub&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:ProxyStub     Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
    ProcessorArchitecture = "x86" | "x64" | "arm" | "arm64" | "x86a64"
    Path? = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
>
<!-- Child elements -->
  ProxyStubDll
</com4:ProxyStub>
```

## Key
`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | The path relative to the package root. Path must reference a file in the package. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| Id | The proxy stub's CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| DisplayName | A localizable string corresponding to the default value of the proxy stub's CLSID key. | A string between 1 and 256 characters in length. This string is localizable.| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [ProxyStubDll](element-com4-proxystubdll.md) | Specifies the path and processor architecture of a ProxyStub DLL. |

## Remarks
A proxy stub element must have either a Path attribute or one or more ProxyStubDll child elements, but not both.

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
