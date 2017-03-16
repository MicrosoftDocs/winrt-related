---
Description: SSIDConfig
MS-HAID: WLAN.element\_SSIDConfig
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: SSIDConfig
ms.assetid: a58e4178-4a15-46c0-951d-93aef9fec5e6
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# SSIDConfig


Defines one or more service set identifiers (SSID) for a wireless LAN.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd><b>&lt;SSIDConfig&gt;</b></dd>
</dl>

## Syntax

``` syntax
<SSIDConfig>

  <!-- Child elements -->
  SSID{1,25},
  any element in a non-schema namespace*

</SSIDConfig>
```

### Key

`*`   optional (zero or more)
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
<td>[SSID](element-ssid.md)</td>
<td><p>Contains the SSID for a WLAN.</p></td>
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
<td>[WLANProfile](element-wlanprofile.md)</td>
<td><p>Defines the properties and security settings of a subscriber's WLAN connection profile. [<strong>WLANProfile</strong>](element-wlanprofile.md) is the unique root element of a wireless profile.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **SSIDConfig** element in te [WLAN](schema-root.md) schema supports up to 25 SSIDs in the v1 namespace and up to additional 10,000 SSIDs in the [WLAN\_v2 schema](https://msdn.microsoft.com/library/windows/apps/dn297323) in the v2 namespace. The v2 namespace also supports [**SSIDPrefix**](https://msdn.microsoft.com/library/windows/apps/dn297316) elements.

## See also


[**SSIDPrefix**](https://msdn.microsoft.com/library/windows/apps/dn297316)

[WLAN\_v2 schema](https://msdn.microsoft.com/library/windows/apps/dn297323)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/WLAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



