---
Description: PurchaseProfile
MS-HAID: ResultsSchema\_v2.element\_PurchaseProfile
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: PurchaseProfile
ms.assetid: 66b0d844-5469-4e94-b364-72638ac4212a
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# PurchaseProfile


Contains any errors from processing the [**PurchaseProfile**](https://msdn.microsoft.com/library/windows/apps/hh868470) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-mbnprofiles.md">&lt;MBNProfiles&gt;</a></dt>
<dd><b>&lt;PurchaseProfile&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<PurchaseProfile errorCode = token
                 name      = string />
```

## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>errorCode</strong></td>
<td><p>S_OK if schema processed successfully. Otherwise, the HRESULT returned during the provisioning attempt formatted as eight hexadecimal characters [0-9a-f].</p></td>
<td>token</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>name</strong></td>
<td><p>Defines the case-sensitive name of the purchased profile.</p></td>
<td>string</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td>[MBNProfiles](element-mbnprofiles.md)</td>
<td><p>Contains any errors from processing the [<strong>MBNProfiles</strong>](https://msdn.microsoft.com/library/windows/apps/hh868295) element from the last provisioning attempt.</p></td>
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

 

 



