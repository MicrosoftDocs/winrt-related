---
Description: Defines a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: PDPContextPolicy
ms.assetid: 2f17fea0-fb18-416d-9bb2-f70f1b53157e
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# PDPContextPolicy


Defines a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-additionalpdpcontexts.md">&lt;AdditionalPDPContexts&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-multiplepdpcontextpolicies.md">&lt;MultiplePDPContextPolicies&gt;</a></dt>
<dd><b>&lt;PDPContextPolicy&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<PDPContextPolicy>

  <!-- Child elements -->
  Name,
  Context,
  AppIDList

</PDPContextPolicy>
```

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
<td>[AppIDList](element-appidlist.md)</td>
<td><p>Defines the list of applications that are part of the Packet Data Protocol (PDP) context allowed list.</p></td>
</tr>
<tr class="even">
<td>[Context](element-context.md)</td>
<td><p>Defines the context of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[Name](element-name.md)</td>
<td><p>Defines the name of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
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
<td>[MultiplePDPContextPolicies](element-multiplepdpcontextpolicies.md)</td>
<td><p>Defines multiple Packet Data Protocol (PDP) context policies in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**AdditionalPDPContexts**](element-additionalpdpcontexts.md)

[CarrierControlSchema schema](https://msdn.microsoft.com/library/windows/apps/hh868312)

[CarrierControlSchema\_v2 schema](schema-root.md)

[**MultiplePDPContextPolicies**](element-multiplepdpcontextpolicies.md)

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

 

 



