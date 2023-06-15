---
ms.assetid: b0bb03e0-67c6-484c-bf7b-de21ef24df66
title: com:Interface (descendant of com:Extension)
description: Registers new COM Interfaces (descendant of com:Extension).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:Interface (descendant of com:Extension)

Registers new COM Interfaces.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Interface\>**

## Syntax

```xml
<com:Interface
    Id = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
    UseUniversalMarshaler = 'An optional boolean value.'
    ProxyStubClsid = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    SynchronousInterface = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    AsynchronousInterface = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

  <!-- Child elements -->
  TypeLib?

</com:Interface>
```

## Key

`?`    optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | An interface Id (IID). | An alphanumeric string separated by a period between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **UseUniversalMarshaler** | Set this to true to use the OLE Universal Marshaler as the proxy stub. | An optional boolean value. | No |  |
| **ProxyStubClsid** | Corresponds to the [ProxyStubClsid32](/windows/win32/com/proxystubclsid32) registry value. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **SynchronousInterface** | The Id of another interface registration containing AsynchronousInterface that references this registration. The other interface must be in the same comInterface extension. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **AsynchronousInterface** | The Id of another interface registration containing SynchronousInterface that references this registration. The other interface must be in the same comInterface extension. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [com:TypeLib](element-com-interface-typelib.md) | A type library for an interface. |

### Parent elements

| Parent element | Description |
|-|-|
| [com:ComInterface](element-com-cominterface.md) | Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*. |

## Remarks

The **ProxyStubClsid** attribute must reference the Id of a [ProxyStub](element-com-proxystub.md) in the same [comInterface](element-com-cominterface.md) extension. **ProxyStubClsid** can only be used for proxy stubs with an implementation as part of the package. To use the OLE Universal Marshaler as the proxy stub, use **UseUniversalMarshaler** instead.

If **UseUniversalMarshaler** is true, the Interface registration must include **TypeLib**.

> [!NOTE]
> **ProxyStubClsid** and **UseUniversalMarshaler** are mutually exclusive.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
