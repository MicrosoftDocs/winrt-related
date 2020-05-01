---
Description: Defines the Access Point Name (APN) or dial string to be used to establish a data connection. 
Search.Product: eADQiWindows 10XVcnh
title: AccessString
ms.assetid: 86cd5d68-ef31-4a85-b3e2-3132c39f6bc4

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# AccessString


Defines the Access Point Name (APN) or dial string to be used to establish a data connection. Must be less than 100 characters.

## Element hierarchy

<dl>
<dt><a href="element-defaultprofile.md">&lt;DefaultProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-context.md">&lt;Context&gt;</a></dt>
<dd><b>&lt;AccessString&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-purchaseprofile.md">&lt;PurchaseProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-context.md">&lt;Context&gt;</a></dt>
<dd><b>&lt;AccessString&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<AccessString>

  token

</AccessString>
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
<td><a href="element-1-context.md">Context</a> </td>
<td><p>Defines the parameters required to setup a data connection.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



