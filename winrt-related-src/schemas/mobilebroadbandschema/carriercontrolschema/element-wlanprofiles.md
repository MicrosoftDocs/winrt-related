---
Description: WLANProfiles
MS-HAID: CarrierControlSchema.element\_WLANProfiles
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: WLANProfiles
ms.assetid: ca31898f-b3c9-4f87-9a8e-8adc30875413
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# WLANProfiles


Defines information for a subscriber's WLAN profiles on a Mobile Network Operator's (MNO) network.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd><b>&lt;WLANProfiles&gt;</b></dd>
</dl>

## Syntax

``` syntax
<WLANProfiles>

  <!-- Child elements -->
  WLANProfile*

</WLANProfiles>
```

### Key

`*`   optional (zero or more)

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
<td>[WLANProfile](element-wlanprofile.md)</td>
<td><p>Defines an instance of the [<strong>WLANProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868422) element from the [<strong>WLAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868424) schema.</p></td>
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
<td>[CarrierProvisioning](element-carrierprovisioning.md)</td>
<td><p>Defines the properties and settings in a subscriber's carrier provisioning file. [<strong>CarrierProvisioning</strong>](element-carrierprovisioning.md) is the unique root element of the provisioning file.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/v1</p></td>
</tr>
</tbody>
</table>

 

 



