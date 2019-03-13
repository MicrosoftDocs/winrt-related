---
Description: Contains any errors from processing the MultiplePDPContextPolicies element from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: MultiplePDPContextPolicies
ms.assetid: c6a17067-5f76-41bd-8df5-39ca71cab5b9
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# MultiplePDPContextPolicies


Contains any errors from processing the [**MultiplePDPContextPolicies**](https://msdn.microsoft.com/library/windows/apps/dn394018) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-additionalpdpcontexts.md">&lt;AdditionalPDPContexts&gt;</a></dt>
<dd><b>&lt;MultiplePDPContextPolicies&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<MultiplePDPContextPolicies>

  <!-- Child elements -->
  PDPContextPolicy+

</MultiplePDPContextPolicies>
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
<td><a href="element-pdpcontextpolicy.md">PDPContextPolicy</a> </td>
<td><p>Contains any errors from processing a <a href="https://msdn.microsoft.com/library/windows/apps/dn394028"><strong>PDPContextPolicy</strong></a>  element from the last provisioning attempt.</p></td>
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
<td><a href="element-additionalpdpcontexts.md">AdditionalPDPContexts</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn393994"><strong>AdditionalPDPContexts</strong></a>  element from the last provisioning attempt.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControlResults/v2</p></td>
</tr>
</tbody>
</table>

 

 



