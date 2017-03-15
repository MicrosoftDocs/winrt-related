---
Description: DeviceCapability
MS-HAID: AppxManifestSchema2010\_v2.element\_DeviceCapability
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: DeviceCapability
ms.assetid: 4353c4fd-f038-4986-81ed-d2ec0c6235ef
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# DeviceCapability




Declares a device capability required by a package.

## Element hierarchy

**&lt;DeviceCapability&gt;**

## Syntax

``` syntax
<DeviceCapability Name = A string between 1 and 50 characters in length or a GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. />
```

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

None.

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

If the *Name* attribute is specified as a GUID, then it is validated as GUID.

Apps are granted access to some devices by default. For Windows Store apps, this includes access to print and scanner devices. To access other types of devices, you must specify them using a **DeviceCapability** element. Some device capabilities must be added to the package manifest manually. For more info, see [How to specify device capabilities in a package manifest](https://msdn.microsoft.com/library/windows/apps/dn263092).

For more info about capability declarations, see [App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936).

Some device capabilities require child elements. This table lists device capabilities by name or GUID and specifies if any child elements are required.

| Device capability                     | Description                                                                                                                                                                                                                                                                                                                                               |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **location**                          | Provides access to the user's current location.                                                                                                                                                                                                                                                                                                           |
| **microphone**                        | Provides access to the microphone's audio feed.                                                                                                                                                                                                                                                                                                           |
| **proximity**                         | Required for near-field communication (NFC) between devices in close proximity. Near-field proximity may be used to send files or connect with an app on a proximate device.                                                                                                                                                                              |
| **webcam**                            | Provides access to the camera's video feed.                                                                                                                                                                                                                                                                                                               |
| **usb**                               | Provides access to APIs in the [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) namespace. This capability requires child elements. For more info, see [Updating the app manifest package for a USB device](http://go.microsoft.com/fwlink/p/?LinkId=302259).                                                                                     |
| **humaninterfacedevice**              | Provides access to APIs in the [**Windows.Devices.HumanInterfaceDevice**](https://msdn.microsoft.com/library/windows/apps/dn264174) namespace. This capability requires child elements. For more info, see [How to specify device capabilities for HID](https://msdn.microsoft.com/library/windows/apps/dn263091).                                             |
| **bluetooth.genericAttributeProfile** | Provides access to APIs in the [**Windows.Devices.Bluetooth.GenericAttributeProfile**](https://msdn.microsoft.com/library/windows/apps/dn297685) namespace. This capability requires child elements. For more info, see [How to specify device capabilities for Bluetooth](https://msdn.microsoft.com/library/windows/apps/dn263090). |
| **bluetooth.rfcomm**                  | Provides access to APIs in the [**Windows.Devices.Bluetooth.Rfcomm**](https://msdn.microsoft.com/library/windows/apps/dn263529) namespace. This capability requires child elements. For more info, see [How to specify device capabilities for Bluetooth](https://msdn.microsoft.com/library/windows/apps/dn263090).                                 |
| **pointOfService**                    | Provides access to Point of Service (POS) barcode scanners and magnetic stripe readers, via the [**Windows.Devices.PointOfService**](https://msdn.microsoft.com/library/windows/apps/dn298071) namespace. These APIs are not supported on Windows Phone.                                                                                                                  |
| Other devices (represented by GUIDs)  | Includes specialized devices and Windows Portable Devices.                                                                                                                                                                                                                                                                                                |

 

## Examples

Here's an example of a [**Capabilities**](element-capabilities.md) node. For more examples, see [How to specify device capabilities in a package manifest](https://msdn.microsoft.com/library/windows/apps/dn263092).

```XML
<Capabilities>
  <Capability Name="internetClient"/>
  <Capability Name="musicLibrary"/>
  <Capability Name="videosLibrary"/>
  <DeviceCapability Name="microphone"/>
  <DeviceCapability Name="webcam"/>
</Capabilities>
```

## See also


[App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936)

[How to specify device capabilities in a package manifest](https://msdn.microsoft.com/library/windows/apps/dn263092)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



