---
description: Declares a function for a device that is associated with the DeviceCapability (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Device (Windows 10)
ms.assetid: 1e9e699f-bbd9-4d15-95ea-207ec495c46e
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Device (Windows 10)

Declares a function for a device that is associated with the [DeviceCapability](element-devicecapability.md). On Windows 10.0.10240.0, a **DeviceCapability** can contain up to 100 **Device** elements. On Windows 10.0.10586.0, it can contain up to 1000 (for more details, see **DeviceCapability**).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<DeviceCapability\>](element-devicecapability.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Device\>**

## Syntax

```xml
<Device
  Id = 'A string with a value between 1 and 512 characters in length.' >

  <!-- Child elements -->
  Function{1,100}

</Device>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The identifier of the device. | A string between 1 and 512 characters in length. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [Function](element-function.md) | Declares the function for the device. |

### Parent elements

| Parent element | Description |
|-|-|
| [DeviceCapability](element-devicecapability.md) | Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 [Device](element-device.md)  elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples). |

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
