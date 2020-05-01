---
Description: Defines the number of days until the next refresh.
Search.Product: eADQiWindows 10XVcnh
title: DelayInDays
ms.assetid: e72b05f8-62c0-4d86-9112-35616e9f78ef

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
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
<td><a href="element-refreshparameters.md">RefreshParameters</a> </td>
<td><p>Defines parameters to be used when refreshing the provisioning file contents.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v1` |

 

 



