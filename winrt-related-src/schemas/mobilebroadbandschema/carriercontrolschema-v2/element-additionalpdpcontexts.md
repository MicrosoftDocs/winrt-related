---
Description: Defines additional Packet Data Protocol (PDP) contexts in a subscriber's carrier provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: AdditionalPDPContexts
ms.assetid: 4f4a4b43-e475-4d21-b847-0de7282c4f08
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# AdditionalPDPContexts


Defines additional Packet Data Protocol (PDP) contexts in a subscriber's carrier provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd><b>&lt;AdditionalPDPContexts&gt;</b></dd>
</dl>

## Syntax

``` syntax
<AdditionalPDPContexts>

  <!-- Child elements -->
  MultiplePDPContextPolicies?,
  TetheringSettings?

</AdditionalPDPContexts>
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
<td><a href="element-multiplepdpcontextpolicies.md">MultiplePDPContextPolicies</a> </td>
<td><p>Defines multiple Packet Data Protocol (PDP) context policies in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td><a href="element-tetheringsettings.md">TetheringSettings</a> </td>
<td><p>Defines the tethering settings in a subscriber's carrier provisioning file.</p></td>
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
<td><a href="element-extensions-v2.md">Extensions_v2</a> </td>
<td><p>Defines additional properties and settings in a subscriber's carrier provisioning file. <a href="element-extensions-v2.md"><strong>Extensions_v2</strong></a>  is the unique root element of the [CarrierControlSchema_v2](schema-root.md) provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## See also


[CarrierControlSchema schema](https://msdn.microsoft.com/library/windows/apps/hh868312)

[CarrierControlSchema\_v2 schema](schema-root.md)

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

 

 



