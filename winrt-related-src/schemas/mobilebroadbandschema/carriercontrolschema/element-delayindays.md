---
Description: DelayInDays
MS-HAID: CarrierControlSchema.element\_DelayInDays
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: DelayInDays
ms.assetid: e72b05f8-62c0-4d86-9112-35616e9f78ef
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# DelayInDays


Defines the number of days until the next refresh. It must be a positive integer less than 732.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-provisioning.md">&lt;Provisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-refreshparameters.md">&lt;RefreshParameters&gt;</a></dt>
<dd><b>&lt;DelayInDays&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DelayInDays>

  integer

</DelayInDays>
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
<td>[RefreshParameters](element-refreshparameters.md)</td>
<td><p>Defines parameters to be used when refreshing the provisioning file contents.</p></td>
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

 

 



