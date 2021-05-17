---

title: com2:ProxyStubDll
description: Specifies the path and processor architecture of a ProxyStub DLL.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:ProxyStubDll

## Description
Specifies the path and processor architecture of a ProxyStub DLL.

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
<dt><a href="element-com-proxystub.md">&lt;com:ProxyStub&gt;</a></dt>
<dd><b>&lt;com:ProxyStubDll&gt;</b></dd>
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
|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/2` |