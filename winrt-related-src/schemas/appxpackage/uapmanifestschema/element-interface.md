---
description: Declares an interface associated with the proxy (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Interface (Windows 10)
ms.assetid: 5b5c6b0c-a9d1-4e0c-a71c-40744a12c4e7
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Interface (Windows 10)

Declares an interface associated with the proxy.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<ProxyStub\>](element-proxystub.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Interface\>**

## Syntax

```xml
<Interface
  Name = 'A string with a value between 1 and 255 characters in length that consists of alphanumeric, period, and underscore characters.'
  InterfaceId = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the interface. | A string with a value between 1 and 255 characters in length that consists of alpha-numeric, period, and underscore characters. | Yes |  |
| **InterfaceId** | The interface ID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [ProxyStub](element-proxystub.md) | Declares a package extensibility point of type **windows.activatableClass.proxyStub**. A proxy can be composed of one or more interfaces. |

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
