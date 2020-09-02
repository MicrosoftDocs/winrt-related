---
Description: Contains any errors from processing the TetheringSettings element from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: TetheringSettings
ms.assetid: 0bf2129c-0589-437a-8cfa-834b16ce42a2

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# TetheringSettings


Contains any errors from processing the [**TetheringSettings**](../carriercontrolschema-v2/element-tetheringsettings.md) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-additionalpdpcontexts.md">&lt;AdditionalPDPContexts&gt;</a></dt>
<dd><b>&lt;TetheringSettings&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TetheringSettings>

  <!-- Child elements -->
  TetheringProfile+

</TetheringSettings>
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
<td><a href="element-tetheringprofile.md">TetheringProfile</a> </td>
<td><p>Contains any errors from processing a <a href="https://msdn.microsoft.com/library/windows/apps/dn394029"><strong>TetheringProfile</strong></a>  element from the last provisioning attempt.</p></td>
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

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v2` |

 

 