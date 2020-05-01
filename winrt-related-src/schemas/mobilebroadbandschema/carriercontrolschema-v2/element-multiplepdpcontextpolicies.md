---
Description: Defines multiple Packet Data Protocol (PDP) context policies in a subscriber's carrier provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: MultiplePDPContextPolicies
ms.assetid: c6a17067-5f76-41bd-8df5-39ca71cab5b9

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# MultiplePDPContextPolicies


Defines multiple Packet Data Protocol (PDP) context policies in a subscriber's carrier provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-additionalpdpcontexts.md">&lt;AdditionalPDPContexts&gt;</a></dt>
<dd><b>&lt;MultiplePDPContextPolicies&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<MultiplePDPContextPolicies MultiplePDPContextSupport? = boolean : "true" >

  <!-- Child elements -->
  PDPContextPolicy*

</MultiplePDPContextPolicies>
```

### Key

`?`   optional (zero or one)
`:`   default value
`*`   optional (zero or more)

## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MultiplePDPContextSupport</strong></td>
<td><p>Defines whether multiple PDP context support is enabled.</p></td>
<td>boolean</td>
<td>No</td>
<td>true</td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-pdpcontextpolicy.md">PDPContextPolicy</a> </td>
<td><p>Defines a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
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
<td><a href="element-additionalpdpcontexts.md">AdditionalPDPContexts</a> </td>
<td><p>Defines additional Packet Data Protocol (PDP) contexts in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## See also


[CarrierControlSchema schema](https://msdn.microsoft.com/library/windows/apps/hh868312)

[CarrierControlSchema\_v2 schema](schema-root.md)

[**AdditionalPDPContexts**](element-additionalpdpcontexts.md)

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v2` |

 

 



