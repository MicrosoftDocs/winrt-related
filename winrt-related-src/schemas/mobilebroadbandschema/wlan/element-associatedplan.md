---
Description: Contains the name of the subscriber's data plan.
Search.Product: eADQiWindows 10XVcnh
title: AssociatedPlan
ms.assetid: fdfc0657-a653-4fed-b0ae-b60e94af03ee
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
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
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
<td>[WLANProfile](element-wlanprofile.md)</td>
<td><p>Defines the properties and security settings of a subscriber's WLAN connection profile. [<strong>WLANProfile</strong>](element-wlanprofile.md) is the unique root element of a wireless profile.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/WLAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



