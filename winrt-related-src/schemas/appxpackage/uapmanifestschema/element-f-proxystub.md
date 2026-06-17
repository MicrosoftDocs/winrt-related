---
title: ProxyStub
description: Declares a package extensibility point of type windows.activatableClass.proxyStub (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, ProxyStub]
---

# ProxyStub

Declares a package extensibility point of type **windows.activatableClass.proxyStub**. A proxy can be composed of one or more interfaces.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<ProxyStub>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <ProxyStub
    ClassId = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

    <!-- Child elements -->
    Path
    Interface{1,65535}

  </ProxyStub>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ClassId** | The unique ID of the proxy. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| **Path** | The path to the DLL. |
| [Interface](element-f-interface.md) | Declares an interface associated with the proxy. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-f-package-extension.md) | Declares an extensibility point for the package. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

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
