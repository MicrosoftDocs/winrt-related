---
description: Defines the name and provider ID of a cellular network.
Search.Product: eADQiWindows 10XVcnh
title: Provider
ms.assetid: 349e3c3c-3533-4ec5-ae1d-fad2e3c7e542

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Provider


Defines the name and provider ID of a cellular network.

## Element hierarchy

<dl>
<dt><a href="element-defaultprofile.md">&lt;DefaultProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dataroamingpartners.md">&lt;DataRoamingPartners&gt;</a></dt>
<dd><b>&lt;Provider&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-purchaseprofile.md">&lt;PurchaseProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-dataroamingpartners.md">&lt;DataRoamingPartners&gt;</a></dt>
<dd><b>&lt;Provider&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Provider>

  ProviderType

</Provider>
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
<td><a href="element-1-dataroamingpartners.md">DataRoamingPartners</a> </td>
<td><p>Defines the list of preferred network providers for roaming.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



