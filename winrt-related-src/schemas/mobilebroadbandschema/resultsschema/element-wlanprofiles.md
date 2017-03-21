---
Description: Contains any errors from processing the WLANProfile elements from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: WLANProfiles
ms.assetid: ca31898f-b3c9-4f87-9a8e-8adc30875413
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# WLANProfiles


Contains any errors from processing the [**WLANProfile**](https://msdn.microsoft.com/library/windows/apps/hh868422) elements from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd><b>&lt;WLANProfiles&gt;</b></dd>
</dl>

## Syntax

``` syntax
<WLANProfiles errorCode? = token >

  <!-- Child elements -->
  WLANProfile+

</WLANProfiles>
```

### Key

`?`   optional (zero or one)
`+`   required (one or more)

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
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td>[WLANProfile](element-wlanprofile.md)</td>
<td><p>Contains any errors from processing a [<strong>WLANProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868422) element from the last provisioning attempt.</p></td>
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
<td>[CarrierProvisioningResult](element-carrierprovisioningresult.md)</td>
<td><p>Contains any errors from processing the [<strong>CarrierProvisioning</strong>](https://msdn.microsoft.com/library/windows/apps/hh868289) element from the last provisioning attempt. [<strong>CarrierProvisioningResult</strong>](element-carrierprovisioningresult.md) is the unique root element for the provisioning results.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

If processing all WLAN profiles failed with the same error, this error will be shown as **ErrorCode**. If different profiles failed for different reasons, then each profile will be enumerated and have individual **ErrorCode** attributes.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControlResults/v1</p></td>
</tr>
</tbody>
</table>

 

 



