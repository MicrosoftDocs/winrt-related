---
Description: Contains the name of the subscriber's data plan.
Search.Product: eADQiWindows 10XVcnh
title: AssociatedPlan
ms.assetid: 982defaf-4870-4bca-bbc9-6d780d61ebf7
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# AssociatedPlan


Contains the name of the subscriber's data plan. It must match the **Name** attribute of a [**Plan**](https://msdn.microsoft.com/library/windows/apps/hh868373) in the same XML document.

## Element hierarchy

<dl>
<dt><a href="element-defaultprofile.md">&lt;DefaultProfile&gt;</a></dt>
<dd><b>&lt;AssociatedPlan&gt;</b></dd>
</dl>
<dl>
<dt><a href="element-purchaseprofile.md">&lt;PurchaseProfile&gt;</a></dt>
<dd><b>&lt;AssociatedPlan&gt;</b></dd>
</dl>

## Syntax

``` syntax
<AssociatedPlan>

  string

</AssociatedPlan>
```

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
<td>[DefaultProfile](element-defaultprofile.md)</td>
<td><p>Defines the default connection profile used by a subscriber to connect to a MNO. The Mobile Broadband service will use these connection settings without prompting the user for details.</p></td>
</tr>
<tr class="even">
<td>[PurchaseProfile](element-purchaseprofile.md)</td>
<td><p>Defines a purchase connection profile used by a subscriber to connect to a MNO.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/WWAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



