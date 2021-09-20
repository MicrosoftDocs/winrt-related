---
description: Defines the access string for a context in the Packet Data Protocol (PDP) context policy (descendant of PDPContextPolicy).
Search.Product: eADQiWindows 10XVcnh
title: AccessString (CarrierControlSchema_v2 schema, descendant of PDPContextPolicy)
ms.assetid: 10801ce9-abca-4eb4-95ae-0865961e3d2b

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# AccessString (CarrierControlSchema_v2 schema, descendant of PDPContextPolicy)


Defines the access string for a context in the Packet Data Protocol (PDP) context policy.

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
<dd><b>&lt;AccessString&gt;</b></dd>
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
<td><a href="element-context.md">Context</a> </td>
<td><p>Defines the context of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**AdditionalPDPContexts**](element-additionalpdpcontexts.md)

[CarrierControlSchema schema](../carriercontrolschema/schema-root.md)

[CarrierControlSchema\_v2 schema](schema-root.md)

[**Context**](element-context.md)

[**MultiplePDPContextPolicies**](element-multiplepdpcontextpolicies.md)

[**PDPContextPolicy**](element-pdpcontextpolicy.md)

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v2` |

 

 
