---
description: Defines one or more extensibility points for the package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Extensions (in Package) (Windows 10)
ms.assetid: 837ae066-b590-4f58-b552-2e9d608f0fac
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Extensions (in Package) (Windows 10)

Defines one or more extensibility points for the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<Extensions\>**

## Syntax

```xml
<Extensions>

  <!-- Child elements -->
  Extension{1,10000}

</Extensions>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Extension (in type: CT_PackageExtensions)](element-extension.md) | Declares an extensibility point for the package. |

### Parent elements

| Parent element | Description |
|-|-|
| [Package](element-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md)

## Remarks

Extensibility points are a mechanism by which an app can add functionality in a manner defined by the operating system. An example of a package extensibility point is the ability to specify a dynamic-link library or executable that contains activatable classes that your code uses.

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```xml
<Package>
  <Extensions>
    <Extension Category="windows.activatableClass.proxyStub">
      <ProxyStub ClassId="332fd2f1-1c69-4c91-949e-4bb67a85bdc5">
        <Path>Microsoft.Samples.DllServerAuthoring.Proxies.dll</Path>
        <Interface Name="IToaster" InterfaceId="6a112353-4f87-4460-a908-2944e92686f3" />
        <Interface Name="IToast" InterfaceId="699b1394-3ceb-4a14-ae23-efec518b088b" />
        <Interface Name="IAppliance" InterfaceId="332fd2f1-1c69-4c91-949e-4bb67a85bdc5" />
      </ProxyStub>
    </Extension>
    <Extension Category="windows.activatableClass.inProcessServer">
      <InProcessServer>
        <Path>Microsoft.Samples.DllServerAuthoring.dll</Path>
        <ActivatableClass ActivatableClassId="Microsoft.Samples.DllServerAuthoring.Toaster" ThreadingModel="both" />
      </InProcessServer>
    </Extension>
  </Extensions>
</Package>
```

## See also

- [App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
