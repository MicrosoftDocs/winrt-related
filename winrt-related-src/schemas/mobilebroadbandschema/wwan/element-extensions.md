---
description: Defines a schema extension point container for future additions.
Search.Product: eADQiWindows 10XVcnh
title: Extensions (WWAN schema, child of DefaultProfile)
ms.assetid: 837ae066-b590-4f58-b552-2e9d608f0fac


keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Extensions (WWAN schema, child of DefaultProfile)


Defines a schema extension point container for future additions.

## Element hierarchy

<dl>
<dt><a href="element-defaultprofile.md">&lt;DefaultProfile&gt;</a></dt>
<dd><b>&lt;Extensions&gt;</b></dd>
</dl>
<dl>
<dt><a href="element-purchaseprofile.md">&lt;PurchaseProfile&gt;</a></dt>
<dd><b>&lt;Extensions&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Extensions>

  <!-- Child elements -->
  any element in a non-schema namespace*

</Extensions>
```

### Key

`*`   optional (zero or more)

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
<td><a href="element-defaultprofile.md">DefaultProfile</a> </td>
<td><p>Defines the default connection profile used by a subscriber to connect to a MNO. The Mobile Broadband service will use these connection settings without prompting the user for details.</p></td>
</tr>
<tr class="even">
<td><a href="element-purchaseprofile.md">PurchaseProfile</a> </td>
<td><p>Defines a purchase connection profile used by a subscriber to connect to a MNO.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



