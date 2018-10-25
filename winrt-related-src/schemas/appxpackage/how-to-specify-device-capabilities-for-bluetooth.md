---
Description: The package manifest is an XML document that contains the info the system needs to deploy, display, or update a Windows Runtime apps app.
Search.Product: eADQiWindows 10XVcnh
title: How to specify device capabilities for Bluetooth 
ms.assetid: 366676d5-187e-4e3d-bafa-33ee468efa64
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# How to specify device capabilities for Bluetooth


**Note**  For Windows 10, see [What's different in Windows 10.](uapmanifestschema/what-s-changed-in-windows-10.md)

 

The package manifest is an XML document that contains the info the system needs to deploy, display, or update a Windows Runtime apps app. This info includes package identity, package dependencies, required capabilities, visual elements, and extensibility points. Every app package must include one package manifest.

For detailed information about the package manifest, see [How to create a package manifest manually](how-to-create-a-package-manifest-manually.md).

A Windows Runtime app that accesses a Bluetooth device (via the Rfcomm or Gatt APIs) must include specific **DeviceCapability** data in the **Capabilities** node of its manifest. This data identifies the device and its purpose (or function). Note that some devices may have multiple functions.

The **Device Id** element corresponds to the device identifier. This element may specify a combination **Vendor Id** (vid) and **Product Id** (pid); or, it may specify a combination of **Manufacturer** and **Model**; or, it may specify a generic string ("any"). In addition, if the **Device Id** specifies a **Vendor Id** (vid) and **Product Id** (pid) then it may contain an optional provider string of "usb" or "bluetooth".

The **Function Type** element specifies the device function. This element may specify a Bluetooth **Service Name** (name) or **Service Id** (serviceId).

## Bluetooth DeviceCapability Usage


Your Bluetooth app must include certain device capabilities in its [App package manifest](appx-package-manifest.md) to specify key information about the device. Here are the required elements in hierarchical order:

[**&lt;DeviceCapability&gt;**](appxmanifestschema/element-devicecapability.md): The **Name** attribute must be "bluetooth.rfcomm" for accessing a Bluetooth RFCOMM device or "bluetooth.genericAttributeProfile" for accessing a Bluetooth GATT device.

**&lt;Device&gt;**: The **Id** attribute must specify the vendor/product Id, or the manufacturer/model, or can be "any" to allow access to any device that matches the function type.

**&lt;Function&gt;**: The **Type** attribute can specify the service name or the service Id.

**Note**  You cannot modify the Bluetooth device capability in Microsoft Visual Studio. You must right-click the Package.appxmanifest file in **Solution Explorer** and select **Open With...**, and then **XML (Text) Editor**. The file opens in plain XML.

 

## Defining Rfcomm DeviceCapabilities


Use the following layout to describe your app's Bluetooth RFCOMM capabilities:

``` syntax
<m2:DeviceCapability Name="bluetooth.rfcomm">
  <m2:Device Id="vidpid:xxxx xxxx bluetooth">
    <m2:Function Type="serviceId:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"/>
    <m2:Function Type="name:xxxxx"/>
  </m2:Device>
<m2:/DeviceCapability>
```

## Defining GenericAttributeProfile DeviceCapabilities


Use the following layout to describe your app's Bluetooth GATT capabilities:

``` syntax
<m2:DeviceCapability Name="bluetooth.genericAttributeProfile">
  <m2:Device Id="model:xxxx;xxxx">
    <m2:Function Type="serviceId:xxxxxxxx"/>
    <m2:Function Type="name:xxxxx"/>
  <m2:/Device>
<m2:/DeviceCapability>
```

##  How to Specify DeviceCapabilities Examples


The following entries illustrate different methods for defining **DeviceCapabilities** for a Bluetooth device.

The following snippet identifies the **DeviceCapabilities** for a Bluetooth RFCOMM device using the **Vendor Id** and **Product Id** combination, along with the optional provider:

``` syntax
<m2:DeviceCapability Name="bluetooth.rfcomm">
  <m2:Device Id="vidpid:0006 0001 bluetooth">
    <m2:Function Type="name:obexObjectPush"/>
  </m2:Device>
</m2:DeviceCapability>
```

Alternately, the following snippet identifies the **DeviceCapabilities** for a Bluetooth RFCOMM device using its full Id.

``` syntax
<m2:DeviceCapability Name="bluetooth.rfcomm">
  <m2:Device Id="any">
    <m2:Function Type="name:AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE" />
  </m2:Device>
</m2:DeviceCapability>
```

The following snippet identifies the **DeviceCapabilities** for a Bluetooth GATT device using the **Manufacturer** and **Model** combination:

``` syntax
<m2:DeviceCapability Name="bluetooth.genericAttributeProfile">
  <m2:Device Id="any">
    <m2:Function Type="name:heartRate" />
  </m2:Device>
</m2:DeviceCapability>
```

## Support for Bluetooth RFCOMM services


The following RFCOMM services are supported via the **name** value:

-   name:serialPort
-   name:obexObjectPush
-   name:obexFileTransfer
-   name:phoneBookAccessPce
-   name:phoneBookAccessPse
-   name:genericFileTransfer

The following RFCOMM services are not supported:

-   Service Discovery (0x1000)
-   Browse Group Descriptor (0x1001)
-   LAN Access Using PPP (0x1102)
-   Dialup Networking (0x1103)
-   Headset (0x1108, 0x1112)
-   Cordless Telephony (0x1109)
-   Audio Source (0x110A) and Sink (0x110B)
-   A/V Remote Control (0x110C, 0x110E, 0x110F)
-   Intercom (0x1110)
-   Fax (0x1111)
-   WAP (0x1113, 0x1114)
-   PANU (0x1115)
-   NAP (0x1116)
-   GN (0x1117)
-   Handsfree (0x111E, 0x111F)
-   Human Interface Device (0x1124)
-   HCR Print (0x1126) and Scan (0x1127)
-   Common ISDN Access (0x1128)
-   SIM Access (0x112D)
-   Headset – HS (0x1131)
-   GNSS Server (0x1136)
-   PnP Information (0x1200)
-   Generic Networking (0x1201)
-   Generic Audio (0x1203)
-   Generic Telephony (0x1204)
-   UPnP (0x1205, 0x1206)
-   ESDP UPnP IP (0x1300, 0x1301, 0x1302)
-   Video Source (0x1303) and Sink (0x1304)
-   Video Distribution (0x1305)
-   HDP Source (0x1401) and Sink (0x1402)

## Support for Bluetooth GATT services


The following GATT services are supported via the **name** value:

-   name:battery
-   name:bloodPressure
-   name:cyclingSpeedAndCadence
-   name:genericAccess
-   name:genericAttribute
-   name:glucose
-   name:healthThermometer
-   name:heartRate
-   name:runningSpeedAndCadence

The following GATT service is not supported:

-   Human Interface Device (0x1812)

 

 



