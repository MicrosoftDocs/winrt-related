---
Description: Declares a device capability required by a package.
Search.Product: eADQiWindows 10XVcnh
title: DeviceCapability (Windows 10)
ms.assetid: 4353c4fd-f038-4986-81ed-d2ec0c6235ef
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# DeviceCapability (Windows 10)


Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 [**Device**](element-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples).

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd><b>&lt;DeviceCapability&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DeviceCapability Name = A string between 1 and 50 characters in length or a GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >

  <!-- Child elements -->
  Device{0,1000}

</DeviceCapability>
```

### Key

`{}`   specific range of occurrences
## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><p>The name of the device capability, either specified as a friendly name or a device interface class GUID.</p></td>
<td>A string between 1 and 50 characters in length or a GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Device](element-device.md)</td>
<td><p>Declares a function for a device that is associated with the [<strong>DeviceCapability</strong>](element-devicecapability.md). On Windows 10.0.10240.0, a <strong>DeviceCapability</strong> can contain up to 100 <strong>Device</strong> elements. On Windows 10.0.10586.0, it can contain up to 1000 (for more details, see <strong>DeviceCapability</strong>).</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Capabilities](element-capabilities.md)</td>
<td><p>Declares the access to protected user resources that the package requires.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

If the *Name* attribute is specified as a GUID, then it is validated as GUID.

Apps are granted access to some devices by default. To access other types of devices, you must specify them using a **DeviceCapability** element. Some device capabilities must be added to the package manifest manually. For more info, see [How to specify device capabilities in a package manifest](../how-to-specify-device-capabilities-in-a-package-manifest.md).

For more info about capability declarations, see [App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936).

The following device capabilities require child elements.

| Device capability                     | Description                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **usb**                               | Provides access to APIs in the [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) namespace. This capability requires child elements. For more info, see [Updating the app manifest package for a USB device](http://go.microsoft.com/fwlink/p/?LinkId=302259).                                                                                            |
| **humaninterfacedevice**              | Provides access to APIs in the [**Windows.Devices.HumanInterfaceDevice**](https://msdn.microsoft.com/library/windows/apps/dn264174) namespace. This capability requires child elements. For more info, see [How to specify device capabilities for HID](../how-to-specify-device-capabilities-for-hid.md).                                             |
| **bluetooth.genericAttributeProfile** | Provides access to APIs in the [**Windows.Devices.Bluetooth.GenericAttributeProfile**](https://msdn.microsoft.com/library/windows/apps/dn297685) namespace. This capability requires child elements. For more info, see [How to specify device capabilities for Bluetooth](../how-to-specify-device-capabilities-for-bluetooth.md). |
| **bluetooth.rfcomm**                  | Provides access to APIs in the [**Windows.Devices.Bluetooth.Rfcomm**](https://msdn.microsoft.com/library/windows/apps/dn263529) namespace. This capability requires child elements. For more info, see [How to specify device capabilities for Bluetooth](../how-to-specify-device-capabilities-for-bluetooth.md).                                 |

 

## Examples

Here's an example of a [**Capabilities**](element-capabilities.md) node that will work on both Windows 10.0.10240.0 and 10.0.10586.0 (although, Windows 10.0.10240.0 will only parse the &lt;Device&gt; elements). Windows 10.0.10586.0, on the other hand, supports up to 100 &lt;Device&gt; elements plus &lt;f2:Device&gt; elements for a total complement of 1000.

```XML
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

If you only want to support Windows 10.0.10240.0, then you only need the &lt;Device&gt; element. If you only want to support Windows 10.0.10586.0, then you only need the &lt;f2:Device&gt; element.

For more examples, see [How to specify device capabilities in a package manifest](../how-to-specify-device-capabilities-in-a-package-manifest.md).

## See also


[App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936)

[How to specify device capabilities in a package manifest](../how-to-specify-device-capabilities-in-a-package-manifest.md)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>

 

 



