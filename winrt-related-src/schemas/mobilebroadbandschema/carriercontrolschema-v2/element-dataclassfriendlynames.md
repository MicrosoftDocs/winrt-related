---
Description: DataClassFriendlyNames
MS-HAID: CarrierControlSchema\_v2.element\_DataClassFriendlyNames
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: DataClassFriendlyNames
ms.assetid: 14e6fa1b-991e-4420-a675-52f4c120f5e4
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# DataClassFriendlyNames


Defines class friendly names for the standard or protocol used for mobile network data in a subscriber's carrier provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-carriernetworkmetadata.md">&lt;CarrierNetworkMetadata&gt;</a></dt>
<dd><b>&lt;DataClassFriendlyNames&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DataClassFriendlyNames>

  <!-- Child elements -->
  NONE?,
  GPRS?,
  EDGE?,
  UMTS?,
  HSDPA?,
  HSUPA?,
  LTE?,
  ONEXRTT?,
  ONEXEVDO?,
  ONEXEVDO_REVA?,
  ONEXEVDV?,
  THREEXRTT?,
  ONEXEVDO_REVB?,
  UMB?,
  CUSTOM?

</DataClassFriendlyNames>
```

### Key

`?`   optional (zero or one)

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
<td>[CUSTOM](element-custom.md)</td>
<td><p>Defines a custom protocol used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[EDGE](element-edge.md)</td>
<td><p>Defines the Enhanced Data rates for the GSM Evolution (EDGE) protocol used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[GPRS](element-gprs.md)</td>
<td><p>Defines the general packet radio service (GPRS) protocol used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[HSDPA](element-hsdpa.md)</td>
<td><p>Defines the High-Speed Downlink Packet Access (HSDPA) protocol used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[HSUPA](element-hsupa.md)</td>
<td><p>Defines the High-Speed Uplink Packet Access (HSUPA) protocol used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[LTE](element-lte.md)</td>
<td><p>Defines the Long Term Evolution (LTE) standard used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[NONE](element-none.md)</td>
<td><p>No mobile broadband network Data Class is available.</p></td>
</tr>
<tr class="even">
<td>[ONEXEVDO](element-onexevdo.md)</td>
<td><p>Defines the Enhanced Voice-Data Optimized (EVDO) standard used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[ONEXEVDO_REVA](element-onexevdo-reva.md)</td>
<td><p>Defines the Enhanced Voice-Data Optimized (EVDO) Revision A (Rev. A) standard used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[ONEXEVDO_REVB](element-onexevdo-revb.md)</td>
<td><p>Defines the Enhanced Voice-Data Optimized (EVDO) Revision B (Rev. B) standard used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[ONEXEVDV](element-onexevdv.md)</td>
<td><p>Defines the 1x Evolution-Data and Voice (1xEV-DV) standards used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[ONEXRTT](element-onexrtt.md)</td>
<td><p>Defines the 1x Radio Transmission Technology (1xRTT) standards used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[THREEXRTT](element-threexrtt.md)</td>
<td><p>Defines the 3X Radio Transmission Technology (3xRTT) standard used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[UMB](element-umb.md)</td>
<td><p>Defines the Ultra Mobile Broadband (UMB) system used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[UMTS](element-umts.md)</td>
<td><p>Defines the Universal Mobile Telecommunications System (UMTS) protocol used for mobile network data based on the GSM standard.</p></td>
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
<td>[CarrierNetworkMetadata](element-carriernetworkmetadata.md)</td>
<td><p>Defines the network properties and settings in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## See also


[CarrierControlSchema schema](https://msdn.microsoft.com/library/windows/apps/hh868312)

[CarrierControlSchema\_v2 schema](schema-root.md)

[**CarrierNetworkMetadata**](element-carriernetworkmetadata.md)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/v2</p></td>
</tr>
</tbody>
</table>

 

 



