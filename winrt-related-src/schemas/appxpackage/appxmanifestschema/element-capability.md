---
description: Declares a capability required by a package (Windows 8).
Search.Product: eADQiWindows 10XVcnh
title: Capability (package schema for Windows 8)
ms.assetid: ee6bf220-f139-4ad9-a7a7-e621c189b907


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Capability (package schema for Windows 8)




Declares a capability required by a package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd><b>&lt;Capability&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Capability Name = "internetClient" | "internetClientServer" | "privateNetworkClientServer" | "documentsLibrary" | "picturesLibrary" | ... />
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
<td><p>The name of the capability.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>internetClient</li>
<li>internetClientServer</li>
<li>privateNetworkClientServer</li>
<li>documentsLibrary</li>
<li>picturesLibrary</li>
<li>videosLibrary</li>
<li>musicLibrary</li>
<li>enterpriseAuthentication</li>
<li>sharedUserCertificates</li>
<li>removableStorage</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

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
<td><a href="element-capabilities.md">Capabilities</a> </td>
<td><p>Declares the access to protected user resources that the package requires.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The following table describes the capability values.

| Capability                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **internetClient**             | On Windows, this provides access to your Internet connection for outgoing connections to the Internet. On Windows Phone, provides full local and internet access and can act as a server, but inbound access to critical ports is always blocked.                                                                                                                                                                               |
| **internetClientServer**       | On Windows, this provides access to your Internet connection, including incoming unsolicited connections from the Internet – the app can send information to or from your computer through a firewall. You do not need to declare **internetClient** if this capability is declared. On Windows Phone, provides full local and internet access and can act as a server, but inbound access to critical ports is always blocked. |
| **privateNetworkClientServer** | On Windows, this provides access to a home or work network – the app can send information to or from your computer and other computers on the same network. On Windows Phone, provides the same access as **internetClient** or **internetClientServer**.                                                                                                                                                                       |
| **documentsLibrary**           | Your documents library, including the capability to add, change, or delete files. The package can only access file types that it has declared in the manifest. The app cannot access document libraries on HomeGroup computers.                                                                                                                                                                                                 |
| **picturesLibrary**            | Your pictures library, including the capability to add, change, or delete files. This capability also includes pictures libraries on HomeGroup computers, along with picture file types on locally connected media servers.                                                                                                                                                                                                     |
| **videosLibrary**              | Your videos library, including the capability to add, change, or delete files. This capability also includes videos libraries on HomeGroup computers, along with video file types on locally connected media servers.                                                                                                                                                                                                           |
| **musicLibrary**               | Your music library and playlists, including the capability to add, change, or delete files. This capability also includes music libraries and playlists in the music library on HomeGroup computers, plus music file types on locally connected media servers.                                                                                                                                                                  |
| **enterpriseAuthentication**   | Your Windows credentials, for access to a corporate intranet. This application can impersonate you on the network.                                                                                                                                                                                                                                                                                                              |
| **sharedUserCertificates**     | Software and hardware certificates or a smart card – used to identify you in the app. This capability may be used by your employer, bank, or government services to identify you.                                                                                                                                                                                                                                               |
| **removableStorage**           | Removable storage, such as an external hard drive or USB flash drive, or MTP portable device, including the capability to add, change, or delete specific files. This package can only access file types that it has declared in the manifest.                                                                                                                                                                                  |

 

## Examples

Here's an example of a [**Capabilities**](element-capabilities.md) node.

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


[App capability declarations](/previous-versions/windows/apps/hh464936(v=win.10))

[Guidelines for app settings](/windows/uwp/design/app-settings/guidelines-for-app-settings)

## Requirements

|               |   Value                                                          |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
