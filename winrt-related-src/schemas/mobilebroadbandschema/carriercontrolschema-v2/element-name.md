---
Description: Defines the name of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: Name
ms.assetid: 388d0dc5-d9a8-48f3-96ce-ebd5262894ed
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Name


Defines the name of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.

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
<dd><b>&lt;Name&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-tetheringsettings.md">&lt;TetheringSettings&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-tetheringprofile.md">&lt;TetheringProfile&gt;</a></dt>
<dd><b>&lt;Name&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Name>

  NameType

</Name>
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
<td>[PDPContextPolicy](element-pdpcontextpolicy.md)</td>
<td><p>Defines a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td>[TetheringProfile](element-tetheringprofile.md)</td>
<td><p>Defines the tethering profile in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**AdditionalPDPContexts**](element-additionalpdpcontexts.md)

[CarrierControlSchema schema](https://msdn.microsoft.com/library/windows/apps/hh868312)

[CarrierControlSchema\_v2 schema](schema-root.md)

[**MultiplePDPContextPolicies**](element-multiplepdpcontextpolicies.md)

[**PDPContextPolicy**](element-pdpcontextpolicy.md)

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

 

 



