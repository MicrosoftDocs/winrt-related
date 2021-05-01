---
description: Defines the name of the Home Provider for a given SIM/Device.
Search.Product: eADQiWindows 10XVcnh
title: HomeProviderName (child of DefaultProfile)
ms.assetid: 8c80386f-a778-49ec-9439-990220d17d13

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# HomeProviderName (child of DefaultProfile)


Defines the name of the Home Provider for a given SIM/Device.

## Element hierarchy

<dl>
<dt><a href="element-defaultprofile.md">&lt;DefaultProfile&gt;</a></dt>
<dd><b>&lt;HomeProviderName&gt;</b></dd>
</dl>

## Syntax

``` syntax
<HomeProviderName>

  ProviderNameType

</HomeProviderName>
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
<td><a href="element-defaultprofile.md">DefaultProfile</a> </td>
<td><p>Defines the default connection profile used by a subscriber to connect to a MNO. The Mobile Broadband service will use these connection settings without prompting the user for details.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This element is optional and is set by the Mobile Broadband service for internal use. An application should not set this field while creating or updating a profile.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



