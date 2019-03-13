---
Description: Defines carrier specific branding information for a subscriber's connection to the Mobile Network Operator (MNO).
Search.Product: eADQiWindows 10XVcnh
title: Branding
ms.assetid: fdbfff1d-4109-4c4e-b996-e53ab04d03cf
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Branding


Defines carrier specific branding information for a subscriber's connection to the Mobile Network Operator (MNO).

## Element hierarchy

**&lt;Branding&gt;**

## Syntax

``` syntax
<Branding>

  <!-- Child elements -->
  Logo?,
  Name?,
  any element in a non-schema namespace*

</Branding>
```

### Key

`?`   optional (zero or one)
`*`   optional (zero or more)

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
<td><a href="element-logo.md">Logo</a> </td>
<td><p>Defines a 32x32 bitmap (.bmp) or portable network graphics (.png) type image of the MNO's logo.</p></td>
</tr>
<tr class="even">
<td><a href="element-name.md">Name (in type: Branding)</a> </td>
<td><p>Defines a carrier specific branding name for the MNO. Maximum length is 20 characters.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/WWAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



