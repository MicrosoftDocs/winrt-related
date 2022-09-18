---
description: Declares a package extensibility point of type windows.activatableClass.proxyStub (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: ProxyStub (Windows 10)
ms.assetid: d902d2b6-4694-4158-9c1f-4b3511150ee5
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# ProxyStub (Windows 10)

Declares a package extensibility point of type **windows.activatableClass.proxyStub**. A proxy can be composed of one or more interfaces.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<ProxyStub\>**

## Syntax

```xml
<ProxyStub
  ClassId = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

  <!-- Child elements -->
  Path,
  Interface{1,65535}

</ProxyStub>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ClassId** | The unique ID of the proxy. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [Interface](element-interface.md) | Declares an interface associated with the proxy. |
| [Path (type: ST_FileName)](element-2-path.md) | The path to the DLL. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extension (in type: CT_PackageExtensions)](element-extension.md) | Declares an extensibility point for the package. |

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```xml
<Extension
  Category="windows.activatableClass.proxyStub">
  <ProxyStub
    ClassId="332fd2f1-1c69-4c91-949e-4bb67a85bdc5">
    <Path>Microsoft.Samples.DllServerAuthoring.Proxies.dll</Path>
    <Interface
      Name="IToaster" InterfaceId="6a112353-4f87-4460-a908-2944e92686f3" />
    <Interface
      Name="IToast" InterfaceId="699b1394-3ceb-4a14-ae23-efec518b088b" />
    <Interface
      Name="IAppliance" InterfaceId="332fd2f1-1c69-4c91-949e-4bb67a85bdc5" />
  </ProxyStub>
</Extension>

```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
