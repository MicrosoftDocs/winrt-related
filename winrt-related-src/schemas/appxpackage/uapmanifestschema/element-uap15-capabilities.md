---
title: uap15:Capabilities
description: Declares the access to protected user resources that a package requires. This element can be used by framework packages.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap15:Package, uap15:Capabilities]
---

# uap15:Capabilities

Declares the access to protected user resources that a package requires. This element can be used by framework packages.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ **`<Capabilities>`**  

## Syntax

```xml
<uap15:Capabilities>

  <!-- Child elements -->
  uap15:CapabilityChoice{0,100}
  uap15:CustomCapabilityChoice{0,1000}
  uap15:DeviceCapability{0,1000}

</uap15:Capabilities>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [DeviceCapability](element-f-devicecapability.md) | Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 [Device](element-f-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples). |

## Parent elements

| Parent element | Description |
|-|-|
| [Package](element-f-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/15` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |

## Remarks

This element has the same format and provides the same behavior as the [Capabilities](element-f-capabilities.md) element. The only difference is that while the original **Capabilities** element could only be used for main packages, **uap15:Capabilities** can be used for non-main packages. The usage of this element is restricted to framework packages.

## Examples

<!-- Author content goes here -->

## See also
[App capability declarations](/windows/uwp/packaging/app-capability-declarations)
[MSIX framework packages and dynamic dependencies](/windows/apps/desktop/modernize/framework-packages/framework-packages-overview)
