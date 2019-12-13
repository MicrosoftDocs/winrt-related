---
Description: Defines information for a subscriber's WLAN profiles on a Mobile Network Operator's (MNO) network.
Search.Product: eADQiWindows 10XVcnh
title: WLANProfiles
ms.assetid: ca31898f-b3c9-4f87-9a8e-8adc30875413

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
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
<td><a href="element-wlanprofile.md">WLANProfile</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868422"><strong>WLANProfile</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868424"><strong>WLAN</strong></a> schema.</p></td>
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
<td><a href="element-carrierprovisioning.md">CarrierProvisioning</a> </td>
<td><p>Defines the properties and settings in a subscriber's carrier provisioning file. <a href="element-carrierprovisioning.md"><strong>CarrierProvisioning</strong></a>  is the unique root element of the provisioning file.</p></td>
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

 

 



