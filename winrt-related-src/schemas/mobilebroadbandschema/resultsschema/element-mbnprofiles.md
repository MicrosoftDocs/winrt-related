---
Description: Contains any errors from processing the MBNProfiles element from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: MBNProfiles
ms.assetid: 10f5eab7-7e8c-4162-95e5-f1b5b793e0d8
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# MBNProfiles


Contains any errors from processing the [**MBNProfiles**](https://msdn.microsoft.com/library/windows/apps/hh868295) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd><b>&lt;MBNProfiles&gt;</b></dd>
</dl>

## Syntax

``` syntax
<MBNProfiles errorCode? = token >

  <!-- Child elements -->
  DefaultProfile?,
  PurchaseProfile?

</MBNProfiles>
```

### Key

`?`   optional (zero or one)

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
<td>[DefaultProfile](element-defaultprofile.md)</td>
<td><p>Contains any errors from processing the [<strong>DefaultProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868453) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[PurchaseProfile](element-purchaseprofile.md)</td>
<td><p>Contains any errors from processing the [<strong>PurchaseProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868470) element from the last provisioning attempt.</p></td>
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

If processing all MBN profiles failed with the same error, this error will be shown as **ErrorCode**. If different profiles failed for different reasons, then each profile will be enumerated and have individual **ErrorCode** attributes.

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

 

 



