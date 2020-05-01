---
Description: Defines if the packet header and data transferred over the connection is compressed.
Search.Product: eADQiWindows 10XVcnh
title: Compression
ms.assetid: 7ef80c21-07a1-46d7-b6fe-e276fde61e39

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Compression


If **ENABLE**, the packet header and data transferred over the connection is compressed. Otherwise, **DISABLE**.

## Element hierarchy

<dl>
<dt><a href="element-defaultprofile.md">&lt;DefaultProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-context.md">&lt;Context&gt;</a></dt>
<dd><b>&lt;Compression&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-purchaseprofile.md">&lt;PurchaseProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-context.md">&lt;Context&gt;</a></dt>
<dd><b>&lt;Compression&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Compression>

  "DISABLE" | "ENABLE"

</Compression>
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
<td><a href="element-context.md">Context</a> </td>
<td><p>Defines the parameters required to setup a data connection.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



