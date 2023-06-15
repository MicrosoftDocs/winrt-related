---
title: com4:Interface
description: Registers new COM interface (com4:Interface).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Interface

Registers new COM Interfaces.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Interface\>**

## Syntax

```xml
<com4:Interface
  Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  UseUniversalMarshaler = 'A boolean value.'
  ProxyStubClsid = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  SynchronousInterface = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  AsynchronousInterface = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

  <!-- Child elements -->
  TypeLib

</com4:Interface>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | An interface Id (IID). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| UseUniversalMarshaler | Set this to true to use the OLE Universal Marshaler as the proxy stub. | A boolean value. | Yes |  |
| **ProxyStubClsid** | Corresponds to the [ProxyStubClsid32](/windows/win32/com/proxystubclsid32) registry value. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **SynchronousInterface** | The Id of another interface registration containing AsynchronousInterface that references this registration. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **AsynchronousInterface** | The Id of another interface registration containing SynchronousInterface that references this registration. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [TypeLib](element-com4-interface-typelib.md) | A type library for an interface. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Remarks

**ProxyStubClsid** can only be used for proxy stubs with an implementation as part of the package. To use the OLE Universal Marshaler as the proxy stub, use **UseUniversalMarshaler** instead.

If **UseUniversalMarshaler** is true, the Interface registration must include **TypeLib**.

> [!NOTE]
> **ProxyStubClsid** and **UseUniversalMarshaler** are mutually exclusive.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
