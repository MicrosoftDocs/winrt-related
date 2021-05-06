---
description: Defines optional user name credentials to be presented using HTTP-Auth to log on to the Mobile Network Operator's network when retrieving the provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: UserName (CarrierControlSchema schema)
ms.assetid: 5c377a0a-ca24-4a24-85c0-79d5bc6af8ef

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# UserName (CarrierControlSchema schema)


Defines optional user name credentials to be presented using HTTP-Auth to log on to the Mobile Network Operator's network when retrieving the provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-provisioning.md">&lt;Provisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-refreshparameters.md">&lt;RefreshParameters&gt;</a></dt>
<dd><b>&lt;UserName&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<UserName>

  token

</UserName>
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
<td><a href="element-refreshparameters.md">RefreshParameters</a> </td>
<td><p>Defines parameters to be used when refreshing the provisioning file contents.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v1` |

 

 



