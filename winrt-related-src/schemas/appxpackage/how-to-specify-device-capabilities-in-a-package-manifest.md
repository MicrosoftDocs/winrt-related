---
description: To declare each device capability required by your Windows Runtime app, add a DeviceCapability element and applicable child elements to the package manifest.
Search.Product: eADQiWindows 10XVcnh
title: How to specify device capabilities in a package manifest
ms.assetid: 4e83e2b2-d80f-41e2-aa1f-436ffa389ccc


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# How to specify device capabilities in a package manifest


> [!NOTE]
> For Windows 10, see [What's different in Windows 10.](uapmanifestschema/what-s-changed-in-windows-10.md)

 

To declare each device capability required by your Windows Runtime app, add a [**DeviceCapability**](./uapmanifestschema/element-devicecapability.md) element and applicable child elements to the package manifest.

> [!IMPORTANT]
> Some device capabilities must be specified manually. For example, you must use the **XML (Text) Editor** to specify device capabilities for the USB, Human Interface Device (HID), Point of Service (POS), Bluetooth GATT, and Bluetooth RFCOMM APIs.

 

## Step 1:


Open the Package.appxmanifest file. In Microsoft Visual Studio, open the file with the **XML (Text) Editor**. To do that, in **Solution Explorer**, right-click the file and click **Open with**. Then select **XML (Text) Editor** and click **OK**.

## Step 2:


Add one **DeviceCapability** element per device capability. You can have multiple **DeviceCapability** and **Capability** elements in the **Capabilities** element, but all **DeviceCapability** elements must come after the **Capability** elements. Note that some device capabilities require multiple child elements. For more info, see [**DeviceCapability**](./uapmanifestschema/element-devicecapability.md).

> [!NOTE]
> Not all APIs are available for both UWP apps and Windows 8.x Phone apps. See the API reference documentation for more details about which devices are supported by each API.

 

### Webcam example

Here's an example of the **webcam** device capability. This device capability does not require child elements. For an example of how to use a webcam, see [How to record audio or video](/previous-versions/windows/apps/hh452798(v=win.10)).

```XML
<Capabilities>
  <Capability Name="internetClient"/>
  <Capability Name="musicLibrary"/>
  <Capability Name="videosLibrary"/>
  <DeviceCapability Name="microphone"/>
  <DeviceCapability Name="webcam"/>
</Capabilities>
```

### USB example

The **usb** device capability enables access to APIs in the [**Windows.Devices.Usb**](/uwp/api/Windows.Devices.Usb) namespace. For more info, see [Updating the app manifest package for a USB device](/windows-hardware/drivers/usbcon/).

```XML
<DeviceCapability Name="usb">
    <Device Id="vidpid:xxxx xxxx">
      <Function Type="classId:xx xx xx"/>
      <Function Type="name:xxxxx"/>
      <Function Type="winUsbId:xxxxx"/>
    </Device>
</DeviceCapability>
```

### Human Interface Device (HID) example

The **humaninterfacedevice** device capability enables access to APIs in the [**Windows.Devices.HumanInterfaceDevice**](/uwp/api/Windows.Devices.HumanInterfaceDevice) namespace. In this example, the capability enables access to any device of a specific function. For more info, see [How to specify device capabilities for HID](how-to-specify-device-capabilities-for-hid.md).

```XML
<DeviceCapability Name="humaninterfacedevice">
    <Device Id="any">
      <Function Type="usage:xxxx xxxx"/>
    </Device>
</DeviceCapability>
```

### Point of Service (POS) example

The **pointOfService** device capability enables access to APIs in the [**Windows.Devices.PointOfService**](/uwp/api/Windows.Devices.PointOfService) namespace. This device capability does not require child elements.

```XML
<Capabilities>
  <DeviceCapability Name="pointOfService"/>
</Capabilities>
```

### Bluetooth GATT example

The **bluetooth.genericAttributeProfile** device capability enables access to APIs in the [**Windows.Devices.Bluetooth.GenericAttributeProfile**](/uwp/api/Windows.Devices.Bluetooth.GenericAttributeProfile) namespace. In this example, the capability enables access to any device of a specific function. For more info, see [How to specify device capabilities for Bluetooth](how-to-specify-device-capabilities-for-bluetooth.md).

```XML
  <Capabilities>
    <m2:DeviceCapability Name="bluetooth.genericAttributeProfile">
      <m2:Device Id="any">
        <m2:Function Type="name:xxxxxx"/>
      </m2:Device>
    </m2:DeviceCapability>
  </Capabilities>
```

### Bluetooth RFCOMM example

The **bluetooth.rfcomm** device capability enables access to APIs in the [**Windows.Devices.Bluetooth.Rfcomm**](/uwp/api/Windows.Devices.Bluetooth.Rfcomm) namespace. In this example, the capability enables access to any device of a specific function. For more info, see [How to specify device capabilities for Bluetooth](how-to-specify-device-capabilities-for-bluetooth.md).

```XML
  <Capabilities>
    <m2:DeviceCapability Name="bluetooth.rfcomm">
      <m2:Device Id="any">
        <m2:Function Type="serviceId:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"/>
      </m2:Device>
    </m2:DeviceCapability>
  </Capabilities>
```

## Related topics


[Devices, sensors, and power](/windows/uwp/devices-sensors/)

[**DeviceCapability element reference**](./uapmanifestschema/element-devicecapability.md)

[App capability declarations](/windows/uwp/packaging/app-capability-declarations)

 

 
