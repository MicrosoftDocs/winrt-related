---
title: Device (in DeviceCapability)
description: Declares a function for a device that is associated with the DeviceCapability (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Capabilities, DeviceCapability, Device]
---

# Device (in DeviceCapability)

Declares a function for a device that is associated with the [DeviceCapability](element-f-devicecapability.md). On Windows 10.0.10240.0, a **DeviceCapability** can contain up to 100 **Device** elements. On Windows 10.0.10586.0, it can contain up to 1000 (for more details, see **DeviceCapability**).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<DeviceCapability>`](element-f-devicecapability.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Device>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Device
    Id = 'A required value. <!-- TODO: Add description for t:ST_DeviceId -->' >

    <!-- Child elements -->
    Function{1,100}

  </Device>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The identifier of the device. | A value. <!-- TODO: Add data type for t:ST_DeviceId --> | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| [Function](element-f-function.md) | Declares the function for the device. |

## Parent elements

| Parent element | Description |
|-|-|
| [DeviceCapability](element-f-devicecapability.md) | Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 [Device](element-f-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples). |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
