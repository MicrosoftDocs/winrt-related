---
author: laurenhughes
ms.assetid: b0bb03e0-67c6-484c-bf7b-de21ef24df66
title: com:Interface
description: Registers new COM Interfaces.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, schema, manifest, com
---


# com:Interface

## -description
Registers new COM Interfaces.

## -element-hierarchy
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
<dd><b>&lt;com:Interface&gt;</b></dd>
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

## -syntax
```syntax
<com:Interface
    Id = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    UseUniversalMarshaler? = Boolean.
    ProxyStubClsid? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    SynchronousInterface? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    AsynchronousInterface? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >

  <!-- Child elements -->
  TypeLib?  
</com:Interface>
```

## -key
`?`    optional (zero or one) 

## -attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id      | An interface Id (IID). | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | Yes |
| UseUniversalMarshaler | Set this to true to use the OLE Universal Marshaler as the proxy stub. | Boolean. | No |
| ProxyStubClsid | Corresponds to the [ProxyStubClsid32](https://msdn.microsoft.com/library/windows/desktop/ms688573.aspx) registry value. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |
| SynchronousInterface | The Id of another interface registration containing AsynchronousInterface that references this registration. The other interface must be in the same comInterface registration. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |
| AsynchronousInterface | The Id of another interface registration containing SynchronousInterface that references this registration. The other interface must be in the same comInterface registration. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |

## -child-elements

| Child Element | Description |
|---------------|-------------|
| [TypeLib](element-com-interface-typelib.md) | A type library for an interface. |

## -remarks
The **ProxyStubClsid** attribute must reference the Id of a [ProxyStub](element-com-proxystub.md) in the same [comInterface](element-com-cominterface.md) extension. **ProxyStubClsid** can only be used for proxy stubs with an implementation as part of the package. To use the OLE Universal Marshaler as the proxy stub, use **UseUniversalMarshaler** instead.

If **UseUniversalMarshaler** is true, the Interface registration must include **TypeLib**.

> [!NOTE]
> **ProxyStubClsid** and **UseUniversalMarshaler** are mutually exclusive.

## -examples

## -requirements
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