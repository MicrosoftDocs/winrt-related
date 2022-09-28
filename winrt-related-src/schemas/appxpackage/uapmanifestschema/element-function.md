---
description: Declares the function for the device (in Package/Capabilities).
Search.Product: eADQiWindows 10XVcnh
title: Function (Windows 10)
ms.assetid: d53133f1-6017-4c20-bbff-f2370c5fc39d
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Function (Windows 10)

Declares the function for the device.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<DeviceCapability\>](element-devicecapability.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Device\>](element-device.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Function\>**

## Syntax

```xml
<Function
  Type = 'A string with a value between 1 and 100 characters in length. Where appropriate, it may begin with "classId:", "winUsbId:", "serviceId:", "usage:", or "interfaceId:".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | The type of function for the device. | A string with a value between 1 and 100 characters in length. Where appropriate, it may begin with *classId:*, *winUsbId:*, *serviceId:*, *usage:*, or *interfaceId:*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Device](element-device.md) | Declares a function for a device that is associated with the **DeviceCapability**. On Windows 10.0.10240.0, a **DeviceCapability** can contain up to 100 **Device** elements. On Windows 10.0.10586.0, it can contain up to 1000 (for more details, see [DeviceCapability](element-devicecapability.md)). |

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
