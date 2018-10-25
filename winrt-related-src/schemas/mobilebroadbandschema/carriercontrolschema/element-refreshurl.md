---
Description: Defines the HTTPS URL where the client can find the updated copy of this provisioning file in the future. 
Search.Product: eADQiWindows 10XVcnh
title: RefreshURL
ms.assetid: 615de7ad-9070-4ed1-b6b8-5c5770e47153
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# RefreshURL


Defines the HTTPS URL where the client can find the updated copy of this provisioning file in the future. This URL will be accessed upon receipt of an SMS/USSD trigger or after the specified [**DelayInDays**](element-delayindays.md). It must be formatted as **https://.+**

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-provisioning.md">&lt;Provisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-refreshparameters.md">&lt;RefreshParameters&gt;</a></dt>
<dd><b>&lt;RefreshURL&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<RefreshURL>

  anyURI

</RefreshURL>
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
<td>[RefreshParameters](element-refreshparameters.md)</td>
<td><p>Defines parameters to be used when refreshing the provisioning file contents.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/v1</p></td>
</tr>
</tbody>
</table>

 

 



