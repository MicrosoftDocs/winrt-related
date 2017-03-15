---
Description: RefreshParameters
MS-HAID: CarrierControlSchema.element\_RefreshParameters
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: RefreshParameters
ms.assetid: 138e7caf-6eeb-4f3d-8e53-13a3ecfacfeb
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# RefreshParameters


Defines parameters to be used when refreshing the provisioning file contents.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-provisioning.md">&lt;Provisioning&gt;</a></dt>
<dd><b>&lt;RefreshParameters&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<RefreshParameters>

  <!-- Child elements -->
  DelayInDays?,
  RefreshURL,
  UserName?,
  Password?

</RefreshParameters>
```

### Key

`?`   optional (zero or one)

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
<td>[DelayInDays](element-delayindays.md)</td>
<td><p>Defines the number of days until the next refresh. It must be a positive integer less than 732.</p></td>
</tr>
<tr class="even">
<td>[Password](element-password.md)</td>
<td><p>Defines optional password credentials to be presented using HTTP-Auth to log on to the Mobile Network Operator's network when retrieving the provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[RefreshURL](element-refreshurl.md)</td>
<td><p>Defines the HTTPS URL where the client can find the updated copy of this provisioning file in the future. This URL will be accessed upon receipt of an SMS/USSD trigger or after the specified [<strong>DelayInDays</strong>](element-delayindays.md). It must be formatted as <strong>https://.+</strong></p></td>
</tr>
<tr class="even">
<td>[UserName](element-username.md)</td>
<td><p>Defines optional user name credentials to be presented using HTTP-Auth to log on to the Mobile Network Operator's network when retrieving the provisioning file.</p></td>
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
<td>[Provisioning](element-provisioning.md)</td>
<td><p>Defines parameters used to establish trust and refresh settings for future provisioning attempts.</p></td>
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

 

 



