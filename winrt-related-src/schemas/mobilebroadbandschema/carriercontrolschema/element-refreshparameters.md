---
description: Defines parameters to be used when refreshing the provisioning file contents.
Search.Product: eADQiWindows 10XVcnh
title: RefreshParameters
ms.assetid: 138e7caf-6eeb-4f3d-8e53-13a3ecfacfeb

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
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
<td><a href="element-delayindays.md">DelayInDays</a> </td>
<td><p>Defines the number of days until the next refresh. It must be a positive integer less than 732.</p></td>
</tr>
<tr class="even">
<td><a href="element-password.md">Password</a> </td>
<td><p>Defines optional password credentials to be presented using HTTP-Auth to log on to the Mobile Network Operator's network when retrieving the provisioning file.</p></td>
</tr>
<tr class="odd">
<td><a href="element-refreshurl.md">RefreshURL</a> </td>
<td><p>Defines the HTTPS URL where the client can find the updated copy of this provisioning file in the future. This URL will be accessed upon receipt of an SMS/USSD trigger or after the specified <a href="element-delayindays.md"><strong>DelayInDays</strong></a> . It must be formatted as <strong>https://.+</strong></p></td>
</tr>
<tr class="even">
<td><a href="element-username.md">UserName</a> </td>
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
<td><a href="element-provisioning.md">Provisioning</a> </td>
<td><p>Defines parameters used to establish trust and refresh settings for future provisioning attempts.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v1` |

 

 



