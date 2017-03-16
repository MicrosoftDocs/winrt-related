---
Description: TetheringSettings
MS-HAID: ResultsSchema\_v2.element\_TetheringSettings
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: TetheringSettings
ms.assetid: 0bf2129c-0589-437a-8cfa-834b16ce42a2
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# TetheringSettings


Contains any errors from processing the [**TetheringSettings**](https://msdn.microsoft.com/library/windows/apps/dn394030) element from the last provisioning attempt.

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
<td>[TetheringProfile](element-tetheringprofile.md)</td>
<td><p>Contains any errors from processing a [<strong>TetheringProfile</strong>](https://msdn.microsoft.com/library/windows/apps/dn394029) element from the last provisioning attempt.</p></td>
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
<td>[AdditionalPDPContexts](element-additionalpdpcontexts.md)</td>
<td><p>Contains any errors from processing the [<strong>AdditionalPDPContexts</strong>](https://msdn.microsoft.com/library/windows/apps/dn393994) element from the last provisioning attempt.</p></td>
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

 

 



