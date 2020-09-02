---
Description: Declares the access to protected user resources that the package requires.
Search.Product: eADQiWindows 10XVcnh
title: Capabilities (Windows 10)
ms.assetid: 508b9a46-3dd4-4bce-875b-fb7cadadceb1


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Capabilities (Windows 10)


Declares the access to protected user resources that the package requires.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Capabilities&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Capabilities>

  <!-- Child elements -->
  Capability{0,100},
  uap:Capability{0,100},
  DeviceCapability{0,100}

</Capabilities>
```

### Key

`{}`   specific range of occurrences
## Attributes and Elements


### Attributes

None.

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
<td><a href="element-capability.md">Capability</a> </td>
<td><p>Declares a capability required by a package.</p></td>
</tr>
<tr class="even">
<td><a href="element-devicecapability.md">DeviceCapability</a> </td>
<td><p>Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 <a href="element-device.md"><strong>Device</strong></a>  elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples).</p></td>
</tr>
<tr class="odd">
<td><a href="element-uap-capability.md">uap:Capability</a> </td>
<td><p>Declares a capability required by a package.</p></td>
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
<td><a href="element-package.md">Package</a> </td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

If you don't explicitly declare the capabilities required for your app to access user resources, your app can't access that resource. However, even if you declare a capability, your app still won't have access to the user resource if it doesn't exist on the system or there are other security policies in place that limit access to the resource.

## Examples

Here's an example [**Capabilities**](https://msdn.microsoft.com/library/windows/apps/dn423258) node.

```XML
<Capabilities>
    <Capability Name="internetClient"/>
    <Capability Name="internetClientServer"/>
    <Capability Name="privateNetworkClientServer"/>
    <Capability Name="allJoyn"/>
    <uap:Capability Name="documentsLibrary"/>
    <uap:Capability Name="picturesLibrary"/>
    <uap:Capability Name="videosLibrary"/>
    <uap:Capability Name="musicLibrary"/>
    <uap:Capability Name="enterpriseAuthentication"/>
    <uap:Capability Name="sharedUserCertificates"/>
    <uap:Capability Name="userAccountInformation"/>
    <uap:Capability Name="removableStorage"/>
    <uap:Capability Name="appointments"/>
    <uap:Capability Name="contacts"/>
    <uap:Capability Name="phoneCall"/>
    <uap:Capability Name="blockedChatMessages"/>
    <uap:Capability Name="objects3D"/>
    <mobile:Capability Name="recordedCallsFolder"/>
</Capabilities>
```

## See also


[App capability declarations](/previous-versions/windows/apps/hh464936(v=win.10))

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |


 

 