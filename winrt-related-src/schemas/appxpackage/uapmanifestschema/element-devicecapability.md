---
description: Declares a device capability required by a package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: DeviceCapability (Windows 10)
ms.assetid: 4353c4fd-f038-4986-81ed-d2ec0c6235ef
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# DeviceCapability (Windows 10)

Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 [Device](element-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<DeviceCapability\>**

## Syntax

```xml
<DeviceCapability
    Name = 'A string with a value between 1 and 50 characters in length or a GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

  <!-- Child elements -->
  Device{0,1000}

</DeviceCapability>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the device capability, either specified as a friendly name or a device interface class GUID. | A string with a value between 1 and 50 characters in length or a GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [Device](element-device.md) | Declares a function for a device that is associated with the [DeviceCapability](element-devicecapability.md). On Windows 10.0.10240.0, a **DeviceCapability** can contain up to 100 **Device** elements. On Windows 10.0.10586.0, it can contain up to 1000 (for more details, see **DeviceCapability**). |

### Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-capabilities.md) | Declares the access to protected user resources that the package requires. You can have multiple **DeviceCapability** and **Capability** elements in the **Capabilities** element, but all **DeviceCapability** elements must come after the **Capability** elements. |

## Remarks

If the *Name* attribute is specified as a GUID, then it is validated as GUID.

Apps are granted access to some devices by default. To access other types of devices, you must specify them using a **DeviceCapability** element. Some device capabilities must be added to the package manifest manually. For more info, see [How to specify device capabilities in a package manifest](../how-to-specify-device-capabilities-in-a-package-manifest.md).

For more info about capability declarations, see [App capability declarations](/previous-versions/windows/apps/hh464936(v=win.10)).

The following device capabilities require child elements.

| Device capability | Description |
|-|-|
| **usb** | Provides access to APIs in the [Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb) namespace. This capability requires child elements. For more info, see [Updating the app manifest package for a USB device](/windows-hardware/drivers/usbcon/). |
| **humaninterfacedevice** | Provides access to APIs in the [Windows.Devices.HumanInterfaceDevice](/uwp/api/Windows.Devices.HumanInterfaceDevice) namespace. This capability requires child elements. For more info, see [How to specify device capabilities for HID](../how-to-specify-device-capabilities-for-hid.md). |
| **bluetooth.genericAttributeProfile** | Provides access to APIs in the [Windows.Devices.Bluetooth.GenericAttributeProfile](/uwp/api/Windows.Devices.Bluetooth.GenericAttributeProfile) namespace. This capability requires child elements. For more info, see [How to specify device capabilities for Bluetooth](../how-to-specify-device-capabilities-for-bluetooth.md). |
| **bluetooth.rfcomm** | Provides access to APIs in the [Windows.Devices.Bluetooth.Rfcomm](/uwp/api/Windows.Devices.Bluetooth.Rfcomm) namespace. This capability requires child elements. For more info, see [How to specify device capabilities for Bluetooth](../how-to-specify-device-capabilities-for-bluetooth.md). |

## Examples

Here's an example of a [Capabilities](element-capabilities.md) node that will work on both Windows 10.0.10240.0 and 10.0.10586.0 (although, Windows 10.0.10240.0 will only parse the \<Device\> elements). Windows 10.0.10586.0, on the other hand, supports up to 100 \<Device\> elements plus \<f2:Device\> elements for a total complement of 1000.

```xml
<Package
    xmlns:f2="http://schemas.microsoft.com/appx/manifest/foundation/windows10/2">
...
<Dependencies>
    <TargetDeviceFamily Name="Windows.Universal" MinVersion="10.0.10240.0" MaxVersionTested="10.0.10586.0"/>
</Dependencies>
...
<Capabilities>
    <DeviceCapability Name="microphone"/>
    <DeviceCapability Name="webcam"/>
    <DeviceCapability Name="<name>">
        <Device Id="id_000" ... />
        ...
        <Device Id="id_099" ... />
        <f2:Device Id="id_100" ... />
        ...
        <f2:Device Id="id_999" ... />
    </DeviceCapability>
</Capabilities>
```

If you only want to support Windows 10.0.10240.0, then you only need the \<Device\> element. If you only want to support Windows 10.0.10586.0, then you only need the \<f2:Device\> element.

For more examples, see [How to specify device capabilities in a package manifest](../how-to-specify-device-capabilities-in-a-package-manifest.md).

## See also

[App capability declarations](/previous-versions/windows/apps/hh464936(v=win.10))

[How to specify device capabilities in a package manifest](../how-to-specify-device-capabilities-in-a-package-manifest.md)

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
