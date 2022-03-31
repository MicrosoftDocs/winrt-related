---
title: com4:Interface
description: Registers new COM Interfaces (com4:Interface).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Interface



## Description
Registers new COM Interfaces.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:Interface&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:Interface     Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    UseUniversalMarshaler = Boolean.
    ProxyStubClsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    SynchronousInterface = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    AsynchronousInterface = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
>
<!-- Child elements -->
  TypeLib
</com4:Interface>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Id | An interface Id (IID). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| UseUniversalMarshaler | Set this to true to use the OLE Universal Marshaler as the proxy stub. | Boolean.| Yes |
| ProxyStubClsid | Corresponds to the [ProxyStubClsid32](/windows/win32/com/proxystubclsid32) registry value. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| SynchronousInterface | The Id of another interface registration containing AsynchronousInterface that references this registration. The other interface must be in the same comInterface registration. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| AsynchronousInterface | The Id of another interface registration containing SynchronousInterface that references this registration. The other interface must be in the same comInterface registration. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [TypeLib](element-com4-interface-typelib.md) | A type library for an interface. |

## Remarks
The **ProxyStubClsid** attribute must reference the Id of a [ProxyStub](element-com4-proxystub.md) in the same [comInterface](element-com4-cominterface.md) extension. **ProxyStubClsid** can only be used for proxy stubs with an implementation as part of the package. To use the OLE Universal Marshaler as the proxy stub, use **UseUniversalMarshaler** instead.

If **UseUniversalMarshaler** is true, the Interface registration must include **TypeLib**.

> [!NOTE]
> **ProxyStubClsid** and **UseUniversalMarshaler** are mutually exclusive.

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
