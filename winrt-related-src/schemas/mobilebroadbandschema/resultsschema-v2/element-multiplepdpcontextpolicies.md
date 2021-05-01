---
description: Contains any errors from processing the MultiplePDPContextPolicies element from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: MultiplePDPContextPolicies (ResultsSchema_v2 schema)
ms.assetid: c6a17067-5f76-41bd-8df5-39ca71cab5b9

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# MultiplePDPContextPolicies (ResultsSchema_v2 schema)


Contains any errors from processing the [**MultiplePDPContextPolicies**](../carriercontrolschema-v2/element-multiplepdpcontextpolicies.md) element from the last provisioning attempt.

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
<td><p>Contains any errors from processing a <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema-v2/element-pdpcontextpolicy"><strong>PDPContextPolicy</strong></a>  element from the last provisioning attempt.</p></td>
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
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema-v2/element-additionalpdpcontexts"><strong>AdditionalPDPContexts</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v2` |

 

 
