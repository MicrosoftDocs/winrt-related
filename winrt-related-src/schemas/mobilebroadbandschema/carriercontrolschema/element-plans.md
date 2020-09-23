---
Description: Defines information for a subscriber's connection plans to a Mobile Network Operator's (MNO) network.
Search.Product: eADQiWindows 10XVcnh
title: Plans
ms.assetid: f6bdcd56-748b-4d9e-86fd-10467df0e7f3

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Plans


Defines information for a subscriber's connection plans to a Mobile Network Operator's (MNO) network.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd><b>&lt;Plans&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Plans>

  <!-- Child elements -->
  Plan+

</Plans>
```

### Key

`+`   required (one or more)

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
<td><a href="element-plan.md">Plan</a> </td>
<td><p>Defines an instance of the <a href="/uwp/schemas/mobilebroadbandschema/plans/element-plan"><strong>Plan</strong></a>  element from the <a href="/uwp/schemas/mobilebroadbandschema/plans/schema-root"><strong>Plans</strong></a> schema.</p></td>
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
<td><a href="element-carrierprovisioning.md">CarrierProvisioning</a> </td>
<td><p>Defines the properties and settings in a subscriber's carrier provisioning file. <a href="element-carrierprovisioning.md"><strong>CarrierProvisioning</strong></a>  is the unique root element of the provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v1` |

 

 