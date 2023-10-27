---
description: Declares the access to protected user resources that a package requires. This element can be used by framework packages.
title: uap15:Capabilities
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 09/22/2022
---

# uap15:Capabilities

Declares the access to protected user resources that a package requires. This element can be used by framework packages.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<uap15:Capabilities\>**

## Syntax

```xml
<uap15:Capabilities>

  <!-- Child elements -->
  Capability{0,100},
  uap:Capability{0,100},
  DeviceCapability{0,100},
  mobile:Capability{0,100},
  rescap:Capability{0,100},
  uap:Capability{0,100},
  uap2:Capability{0,100},
  uap3:Capability{0,100},
  uap4:Capability{0,100},
  uap4:CustomCapability{0,100},
  uap7:Capability{0,100},
  uap11:Capability{0,100}

</uap15:Capabilities>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Capability](element-capability.md) | Declares a capability required by a package. |
| [DeviceCapability](element-devicecapability.md) | Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 **[Device]**(element-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples). |
| [mobile:Capability](element-mobile-capability-manual.md) | Declares a capability required by a package. (mobile)|
| [rescap:Capability](element-rescap-capability.md) | Declares a restricted capability required by a package.|
| [uap2:Capability](element-uap2-capability.md) | Declares a capability required by a package. (uap2)|
| [uap3:Capability](element-uap3-capability-manual.md) | Declares a capability required by a package. (uap3)|
| [uap4:Capability](element-uap4-capability.md) | Declares a capability required by a package. (uap4)|
| [uap4:CustomCapability](element-uap4-customcapability.md) | Declares a custom capability required by a package. (uap4) |
| [uap11:Capability](element-uap11-capability.md) | Declares a capability required by a package. (uap11)|

### Parent elements

| Parent element | Description |
|-|-|
| Package | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Remarks

This element has the same format and provides the same behavior as the [Capabilities](element-capabilities.md) element. The only difference is that while the original **Capabilities** element could only be used for main packages, **uap15:Capabilities** can be used for non-main packages. The usage of this element is restricted to framework packages.



## See also

[App capability declarations](/windows/uwp/packaging/app-capability-declarations)
[MSIX framework packages and dynamic dependencies](/windows/apps/desktop/modernize/framework-packages/framework-packages-overview)

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/15` |
| Minimum OS Version | Windows 11 version 22H2 (Build 22621) |
