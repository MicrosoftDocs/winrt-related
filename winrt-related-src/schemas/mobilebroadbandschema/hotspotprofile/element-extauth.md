---
Description: ExtAuth
MS-HAID: HotSpotProfile.element\_ExtAuth
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: ExtAuth
ms.assetid: b8189ab7-f090-4175-8d5b-d311e7e040fe
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# ExtAuth


Contains the parameters for handling WISPr authentication through an app (rather than specifying a static user name and password via [**BasicAuth**](element-basicauth.md)).

## Element hierarchy

<dl>
<dt><a href="element-hotspotprofile.md">&lt;HotspotProfile&gt;</a></dt>
<dd><b>&lt;ExtAuth&gt;</b></dd>
</dl>

## Syntax

``` syntax
<ExtAuth>

  <!-- Child elements -->
  ExtensionId

</ExtAuth>
```

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
<td>[ExtensionId](element-extensionid.md)</td>
<td><p>The package family name of the app that will be invoked to handle the WISPr authentication.</p></td>
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
<td>[HotspotProfile](element-hotspotprofile.md)</td>
<td><p>Defines the properties and login credentials for a Wi-Fi hotspot. [<strong>HotspotProfile</strong>](element-hotspotprofile.md) is the unique root element of a Wi-Fi hotspot profile that uses the Wireless Internet Service Provider roaming (WISPr) protocol.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/WLAN/HotspotProfile/v1</p></td>
</tr>
</tbody>
</table>

 

 



