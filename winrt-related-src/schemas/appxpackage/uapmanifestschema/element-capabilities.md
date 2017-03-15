---
Description: Capabilities (Windows 10)
MS-HAID: UapManifestSchema.element\_Capabilities
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Capabilities (Windows 10)
ms.assetid: 508b9a46-3dd4-4bce-875b-fb7cadadceb1
author: laurenhughes
ms.author: lahugh
keywords: windows 10
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
<td>[Capability](element-capability.md)</td>
<td><p>Declares a capability required by a package.</p></td>
</tr>
<tr class="even">
<td>[DeviceCapability](element-devicecapability.md)</td>
<td><p>Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 [<strong>Device</strong>](element-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples).</p></td>
</tr>
<tr class="odd">
<td>[uap:Capability](element-uap-capability.md)</td>
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
<td>[Package](element-package.md)</td>
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


[App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936)

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

 

 



