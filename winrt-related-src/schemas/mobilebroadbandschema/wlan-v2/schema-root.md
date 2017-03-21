---
title: WLAN_v2 schema
description: The WLAN_v2 schema defines additional elements that are used to describe a subscriber's connection to a Wireless Local Area Network (WLAN).
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# WLAN\ schema


The WLAN\_v2 schema defines additional elements that are used to describe a subscriber's connection to a Wireless Local Area Network (WLAN).

All of the elements of the WLAN\_v2 schema are defined in the *http://www.microsoft.com/networking/CarrierControl/WLAN/v2* namespace.

The WLAN\_v2 schema elements are additions to the [WLAN](https://msdn.microsoft.com/library/windows/apps/hh868424) version 1 schema defined in the *http://www.microsoft.com/networking/CarrierControl/WLAN/v1* namespace.

The WLAN\_v2 schema is supported on Windows 8.1, Windows Server 2012 R2, and later.

The [**SSIDConfig**](https://msdn.microsoft.com/library/windows/apps/hh868420) element in the [WLAN](https://msdn.microsoft.com/library/windows/apps/hh868424) schema supports up to 25 SSIDs in the v1 namespace and up to additional 10,000 SSIDs in the v2 namespace. The v2 namespace also supports [**SSIDPrefix**](element-ssidprefix.md) elements.

Not all elements are in every profile, as some elements are optional.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[FIPSMode](element-fipsmode.md)</td>
<td><p>Defines whether Federal Information Processing Standards (FIPS) mode is enabled.</p></td>
</tr>
<tr class="even">
<td>[SSID](element-ssid.md)</td>
<td><p>Contains the SSID for a WLAN.</p></td>
</tr>
<tr class="odd">
<td>[SSIDPrefix](element-ssidprefix.md)</td>
<td><p>Contains the SSIDPrefix for a WLAN.</p></td>
</tr>
<tr class="even">
<td>[hex (in SSID)](element-hex.md)</td>
<td><p>Defines the SSID of a wireless LAN in hexadecimal format.</p></td>
</tr>
<tr class="odd">
<td>[hex (in SSIDPrefix)](element-1-hex.md)</td>
<td><p>Defines the SSIDPrefix of a wireless LAN in hexadecimal format.</p></td>
</tr>
<tr class="even">
<td>[name (in SSID)](element-name.md)</td>
<td><p>Defines the SSID of a wireless LAN in alphanumeric format.</p></td>
</tr>
<tr class="odd">
<td>[name (in SSIDPrefix)](element-1-name.md)</td>
<td><p>Defines the SSIDPrefix of a wireless LAN in alphanumeric format.</p></td>
</tr>
</tbody>
</table>

 

## Related topics


[**SSIDConfig**](https://msdn.microsoft.com/library/windows/apps/hh868420)

[WLAN schema](https://msdn.microsoft.com/library/windows/apps/hh868424)

 

 



