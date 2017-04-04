---
Description: Defines the password used for the Packet Data Protocol (PDP) context activation.
Search.Product: eADQiWindows 10XVcnh
title: Password
ms.assetid: a7a63a7c-31d7-42bb-8e04-557306980baf
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# Password


Defines the password used for the Packet Data Protocol (PDP) context activation.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-additionalpdpcontexts.md">&lt;AdditionalPDPContexts&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-multiplepdpcontextpolicies.md">&lt;MultiplePDPContextPolicies&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-pdpcontextpolicy.md">&lt;PDPContextPolicy&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-context.md">&lt;Context&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-userlogoncred.md">&lt;UserLogonCred&gt;</a></dt>
<dd><b>&lt;Password&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-tetheringsettings.md">&lt;TetheringSettings&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-tetheringprofile.md">&lt;TetheringProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-context.md">&lt;Context&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-userlogoncred.md">&lt;UserLogonCred&gt;</a></dt>
<dd><b>&lt;Password&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Password>

  string

</Password>
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
<td>[UserLogonCred](element-userlogoncred.md)</td>
<td><p>Defines the user login credentials for a context in the Packet Data Protocol (PDP) context policy.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**AdditionalPDPContexts**](element-additionalpdpcontexts.md)

[CarrierControlSchema schema](https://msdn.microsoft.com/library/windows/apps/hh868312)

[CarrierControlSchema\_v2 schema](schema-root.md)

[**Context**](element-context.md)

[**MultiplePDPContextPolicies**](element-multiplepdpcontextpolicies.md)

[**PDPContextPolicy**](element-pdpcontextpolicy.md)

[**UserLogonCred**](element-userlogoncred.md)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/v2</p></td>
</tr>
</tbody>
</table>

 

 



