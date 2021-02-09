---
description: Defines additional properties and settings in a subscriber's carrier provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: Extensions\_v2
ms.assetid: 698df4b4-94ce-4516-bcbc-92cae505c405

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Extensions\_v2


Defines additional properties and settings in a subscriber's carrier provisioning file. [**Extensions\_v2**](element-extensions-v2.md) is the unique root element of the [CarrierControlSchema\_v2](schema-root.md) provisioning file.

## Element hierarchy

**&lt;Extensions\_v2&gt;**

## Syntax

``` syntax
<Extensions_v2>

  <!-- Child elements -->
  CarrierNetworkMetadata?,
  AdditionalPDPContexts?

</Extensions_v2>
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
<td><a href="element-additionalpdpcontexts.md">AdditionalPDPContexts</a> </td>
<td><p>Defines additional Packet Data Protocol (PDP) contexts in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td><a href="element-carriernetworkmetadata.md">CarrierNetworkMetadata</a> </td>
<td><p>Defines the network properties and settings in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## See also


[CarrierControlSchema schema](../carriercontrolschema/schema-root.md)

[CarrierControlSchema\_v2 schema](schema-root.md)

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v2` |

 

 
