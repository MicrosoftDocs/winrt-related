---
description: Contains any errors from processing a WLANProfile element from the last provisioning attempt (ResultsSchema_v2 schema).

Search.Product: eADQiWindows 10XVcnh
title: WLANProfile (ResultsSchema_v2 schema)
ms.assetid: adafca95-23be-417f-8c3f-7c340222ecfd

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# WLANProfile (ResultsSchema_v2 schema)


Contains any errors from processing a [**WLANProfile**](../wlan/element-wlanprofile.md) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-wlanprofiles.md">&lt;WLANProfiles&gt;</a></dt>
<dd><b>&lt;WLANProfile&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<WLANProfile errorCode = token
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
<td><p>Defines the case sensitive <a href="/uwp/schemas/mobilebroadbandschema/wlan/element-name"><strong>name</strong></a>  of the wireless LAN profile.</p></td>
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
<td><a href="element-wlanprofiles.md">WLANProfiles</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/wlan/element-wlanprofile"><strong>WLANProfile</strong></a>  elements from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v2` |

 

 
