---
author: laurenhughes
title: com2:ProxyStubDll
description: Specifies the path and processor architecture of a ProxyStub DLL.
ms.author: lahugh
ms.date: 10/10/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, com
---


# com2:ProxyStubDll (in Package/Extensions)

## Description
Specifies the path and processor architecture of a ProxyStub DLL.

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
<dt><a href="element-com-package-proxystub.md">&lt;com:ProxyStub&gt;</a></dt>
<dd><b>&lt;com2:ProxyStubDll&gt;</b></dd>
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
<com2:ProxyStubDll Path                  = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
                   ProcessorArchitecture = A string value, one of the following: x86 or x64 >
```

## Key
`?`    optional (zero or one)  

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Path | A relative path to the .dll file in the app package. | A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, ", &#124;, ?, or *. | Yes |
| ProcessorArchitecture | The processor architecture of the ProxyStub registration. | A string value, one of the following: x86 or x64 | No |

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
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10/2</p></td>
</tr>
</tbody>
</table>