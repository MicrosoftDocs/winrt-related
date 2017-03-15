---
Description: MaxDownloadFileSizeInMegabytes
MS-HAID: DUSM.element\_MaxDownloadFileSizeInMegabytes
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: MaxDownloadFileSizeInMegabytes
ms.assetid: 6574bdc7-2d0a-472c-aac3-e0001c4b9073
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# MaxDownloadFileSizeInMegabytes


Defines a value representing the maximum suggested download size in MB of the subscriber's connection. Must be a value from 0 to 2<sup>32nd</sup>.

## Element hierarchy

<dl>
<dt><a href="element-cost.md">&lt;Cost&gt;</a></dt>
<dd><b>&lt;MaxDownloadFileSizeInMegabytes&gt;</b></dd>
</dl>

## Syntax

``` syntax
<MaxDownloadFileSizeInMegabytes>

  positiveInteger : "25"

</MaxDownloadFileSizeInMegabytes>
```

### Key

`:`   default value
## Attributes and Elements


### Attributes

None.

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
<td>[Cost](element-cost.md)</td>
<td><p>Defines a set of meter cost information that specifies the metered state of a subscriber's connection to a Mobile Network Operator (MNO). [<strong>Cost</strong>](element-cost.md) is the unique root element for DUSM cost information.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/DUSM/v1</p></td>
</tr>
</tbody>
</table>

 

 



