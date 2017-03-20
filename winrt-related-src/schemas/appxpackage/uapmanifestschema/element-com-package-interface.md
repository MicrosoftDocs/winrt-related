---
author: laurenhughes
ms.assetid: b7261b8b-2979-4961-b521-7e5c290170a8
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
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-package-cominterface.md">&lt;ComInterface&gt;</a></dt>
<dd><b>&lt;Interface&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>



## -syntax
```syntax
<Interface
    Id = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    UseUniversalMarshaler? = Boolean.
    ProxyStubClsid? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    SynchronousInterface? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    AsynchronousInterface? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >

  <!-- Child elements -->
  TypeLib?  
</Interface>
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
| [TypeLib](element-com-package-interface-typelib.md) | A type library for an interface. | 

## -remarks

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