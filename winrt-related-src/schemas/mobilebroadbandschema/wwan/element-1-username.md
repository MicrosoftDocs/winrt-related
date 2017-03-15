---
Description: UserName
MS-HAID: WWAN.element\_1\_UserName
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: UserName
ms.assetid: fb4913e1-095c-421d-af9a-40529f9bcd42
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# UserName


Defines the user name for logon. Must be less than 256 characters.

## Element hierarchy

<dl>
<dt><a href="element-defaultprofile.md">&lt;DefaultProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-context.md">&lt;Context&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-userlogoncred.md">&lt;UserLogonCred&gt;</a></dt>
<dd><b>&lt;UserName&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-purchaseprofile.md">&lt;PurchaseProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-context.md">&lt;Context&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-userlogoncred.md">&lt;UserLogonCred&gt;</a></dt>
<dd><b>&lt;UserName&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<UserName>

  NameType

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
<td>[UserLogonCred](element-1-userlogoncred.md)</td>
<td><p>Defines logon credentials for a connection.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/WWAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



