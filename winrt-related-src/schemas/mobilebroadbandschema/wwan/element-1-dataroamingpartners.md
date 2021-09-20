---
description: Defines the list of preferred network providers for roaming (in PurchaseProfile/DataRoamingPartners).
Search.Product: eADQiWindows 10XVcnh
title: DataRoamingPartners (child of PurchaseProfile)
ms.assetid: 68a5d75a-bbd5-45cb-8bee-ccb3b0cc0a39

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# DataRoamingPartners (child of PurchaseProfile)


Defines the list of preferred network providers for roaming.

## Element hierarchy

<dl>
<dt><a href="element-purchaseprofile.md">&lt;PurchaseProfile&gt;</a></dt>
<dd><b>&lt;DataRoamingPartners&gt;</b></dd>
</dl>

## Syntax

``` syntax
<DataRoamingPartners>

  <!-- Child elements -->
  Provider+

</DataRoamingPartners>
```

### Key

`+`   required (one or more)

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
<td><a href="element-1-provider.md">Provider</a> </td>
<td><p>Defines the name and provider ID of a cellular network.</p></td>
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
<td><a href="element-purchaseprofile.md">PurchaseProfile</a> </td>
<td><p>Defines a purchase connection profile used by a subscriber to connect to a MNO.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



