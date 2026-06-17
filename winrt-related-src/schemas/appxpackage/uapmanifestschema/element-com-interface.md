---
title: com:Interface
description: Registers new COM Interfaces (descendant of com:Extension).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com:Extension, com:ComInterface, com:Interface]
---

# com:Interface

Registers new COM Interfaces.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:ComInterface>`](element-com-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:Interface>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:ComInterface>`](element-com-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:Interface>`**  


## Syntax

```xml
<com:Interface
  Id = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  UseUniversalMarshaler = 'An optional boolean value.'
  ProxyStubClsid = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  SynchronousInterface = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  AsynchronousInterface = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

  <!-- Child elements -->
  com:TypeLib?

</com:Interface>
```

### Key

`?` optional (zero or one)


## Attributes
| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|**Id**| An interface Id (IID). |A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.|Yes||
|**UseUniversalMarshaler**| Set this to true to use the OLE Universal Marshaler as the proxy stub. |An optional boolean value.|No||
|**ProxyStubClsid**| Corresponds to the [ProxyStubClsid32](/windows/win32/com/proxystubclsid32) registry value. |An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.|No||
|**SynchronousInterface**| The Id of another interface registration containing AsynchronousInterface that references this registration. The other interface must be in the same comInterface extension. |An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.|No||
|**AsynchronousInterface**| The Id of another interface registration containing SynchronousInterface that references this registration. The other interface must be in the same comInterface extension. |An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.|No||

## Child elements
| Child element | Description |
|-|-|
| [com:TypeLib](element-com-interface-typelib.md) | A type library for an interface. |

## Parent elements

| Parent element | Description |
|-|-|
| [com:ComInterface](element-com-cominterface.md) | Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*. |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |


## Remarks

The **ProxyStubClsid** attribute must reference the Id of a [ProxyStub](element-com-proxystub.md) in the same [comInterface](element-com-cominterface.md) extension. **ProxyStubClsid** can only be used for proxy stubs with an implementation as part of the package. To use the OLE Universal Marshaler as the proxy stub, use **UseUniversalMarshaler** instead.

If **UseUniversalMarshaler** is true, the Interface registration must include **TypeLib**.

> [!NOTE]
> **ProxyStubClsid** and **UseUniversalMarshaler** are mutually exclusive.

## Examples

<!-- Author content goes here -->
