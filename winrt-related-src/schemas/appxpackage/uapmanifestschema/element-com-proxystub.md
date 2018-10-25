---
author: laurenhughes
ms.assetid: 0fe5d00f-4ade-440a-a13d-cb8e9c9b7e3c
title: com:ProxyStub
description: Registers a proxy stub. 
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:ProxyStub

## Description
Registers a proxy stub.

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
<dd><b>&lt;com:ProxyStub&gt;</b></dd>
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
<com:ProxyStub
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    DisplayName? = A string between 1 and 256 characters in length. This string is localizable.
    Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. >

      <!-- Child elements -->
    com2:ProxyStubDll

</com:ProxyStub>
```

## Key
`?`    optional (zero or one)  

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | The proxy stub's CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| DisplayName | A localizable string corresponding to the default value of the proxy stub's CLSID key. | A string between 1 and 256 characters in length. This string is localizable. | No |
| Path | The path relative to the package root. Path must reference a file in the package. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [com2:ProxyStubDll](element-com2-proxystubdll.md) | Specifies the path and processor architecture of a ProxyStub DLL. |

## Remarks
A proxy stub element must have either a Path attribute or one or more ProxyStubDll child elements, but not both.

## Examples

## Requirements
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>