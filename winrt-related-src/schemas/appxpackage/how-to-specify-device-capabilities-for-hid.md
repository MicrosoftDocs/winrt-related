---
Description: The package manifest is an XML document that contains the info the system needs to deploy, display, or update a Windows Runtime app.
MS-HAID: AppxManifestSchema.how\_to\_specify\_device\_capabilities\_for\_hid
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: How to specify device capabilities for HID (Windows Runtime apps)
ms.assetid: 4c5c4ab6-e1d1-4631-ab8e-f0c33af8b464
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# How to specify device capabilities for HID (Windows Runtime apps)


**Note**  For Windows 10, see [What's different in Windows 10.](uapmanifestschema/what-s-changed-in-windows-10.md)

 

The package manifest is an XML document that contains the info the system needs to deploy, display, or update a Windows Runtime app. This info includes package identity, package dependencies, required capabilities, visual elements, and extensibility points. Every app package must include one package manifest.

A Windows Runtime app that accesses a HID device must include specific **DeviceCapability** data in the **Capabilities** node of its manifest. This data identifies the device and its purpose (or function). Note that some devices may have multiple functions.

The **Device Id** element corresponds to the device identifier. This element may specify a combination **Vendor Id** (vid) and **Product Id** (pid); or, it may specify a generic string ("any"). In addition, the **Device ID** may contain an optional provider string of "usb" or "bluetooth".

The **Function Type** element specifies the device function. This element contains one or more HID usage values. These values consist of a **Usage Page** and an optional **Usage Id**, each of which are 16-bit hexadecimal values.

## Example DeviceCapabilities


This section contains example **DeviceCapabilities** entries for three HID devices. The first two correspond to a vendor-defined usage on a HID device, the third to gaming device (in the Game Controls page), and the fourth to a joystick and a game pad.

In the following vendor-defined usage data, the device is identified by the **Vendor Id** and **Product Id** combination.

``` syntax
<!-- HID Device -->
<DeviceCapability Name="humaninterfacedevice">
    <Device Id="vidpid:0A81 0701">
      <Function Type="usage:ffa0 0001"/>
    </Device>
</DeviceCapability>
```

The following is identical to the first with the exception of the additional provider string ("usb") in the **Device Id** element.

``` syntax
<!-- HID Device -->
<DeviceCapability Name="humaninterfacedevice">
    <Device Id="vidpid:0A81 0701 usb">
      <Function Type="usage:ffa0 0001"/>
    </Device>
</DeviceCapability>
```

In the following gaming-device data there is no **Vendor Id** and **Product Id**.

``` syntax
<!-- Any gamepad device  -->
<DeviceCapability Name="humaninterfacedevice">
    <Device Id="any">
      <Function Type="usage:0005 *"/>
    </Device>
</DeviceCapability>
```

In the following joystick and game pad data there is no **Vendor Id** and **Product Id**

``` syntax
<!-- Any generic gaming device  -->
<DeviceCapability Name="humaninterfacedevice">
    <Device Id="any">
      <Function Type="usage:0004 *"/>
      <Function Type="usage:0005 *"/>
    </Device>
</DeviceCapability>
```

## Requirements for Windows Phone Store apps


Windows Phone Store apps can access the **Windows.Devices.HumanInterfaceDevice** API if the manufacturer supported the HID protocol for specific devices and provided corresponding device-data to app developers. Refer to your manufacturer’s documentation for a list of supported HID devices as well as the data that you’ll need to implement device discovery.

## Related topics


[**Windows.Devices.HumanInterfaceDevice**](https://msdn.microsoft.com/library/windows/apps/dn264174)

 

 



