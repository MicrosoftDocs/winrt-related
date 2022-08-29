---
ms.assetid: b7261b8b-2979-4961-b521-7e5c290170a8
title: com:Interface (descendant of Extension)
description: Registers new COM Interfaces (descendant of Extension).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:Interface (descendant of Extension)

Registers new COM Interfaces.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-package-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Interface\>**

## Syntax

```xml
<com:Interface
  Id = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
  UseUniversalMarshaler = 'An optional boolean value.'
  ProxyStubClsid = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  SynchronousInterface = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  AsynchronousInterface = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'  >

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
| **Id** | An interface Id (IID). | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **UseUniversalMarshaler** | Set this to true to use the OLE Universal Marshaler as the proxy stub. | An optional boolean value. | No |  |
| **ProxyStubClsid** | Corresponds to the [ProxyStubClsid32](/windows/win32/com/proxystubclsid32) registry value. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **SynchronousInterface** | The Id of another interface registration containing AsynchronousInterface that references this registration. The other interface must be in the same comInterface extension. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **AsynchronousInterface** | The Id of another interface registration containing SynchronousInterface that references this registration. The other interface must be in the same comInterface extension. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [TypeLib](element-com-package-interface-typelib.md) | A type library for an interface. |

### Parent elements

| Parent element | Description |
|-|-|
| [com:ComInterface](element-com-package-cominterface.md) | Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
