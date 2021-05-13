---
description: Defines the maximum transmission unit (MTU) for an IPv6 link.
Search.Product: eADQiWindows 10XVcnh
title: IPv6LinkMTU
ms.assetid: 9d7ca5ab-9be7-466f-bef9-48a84b0e7e7b

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# IPv6LinkMTU


Defines the maximum transmission unit (MTU) for an IPv6 link. It must be a positive integer between 1280 and 1500.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-carriernetworkmetadata.md">&lt;CarrierNetworkMetadata&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-networksettings.md">&lt;NetworkSettings&gt;</a></dt>
<dd><b>&lt;IPv6LinkMTU&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<IPv6LinkMTU>

  Defines a simple type for the maximum transmission unit (MTU).

</IPv6LinkMTU>
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
<td><a href="element-networksettings.md">NetworkSettings</a> </td>
<td><p>Defines the network settings in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This setting is applied to all the profiles defined in a subscriber's carrier provisioning file.

## See also


[CarrierControlSchema schema](../carriercontrolschema/schema-root.md)

[CarrierControlSchema\_v2 schema](schema-root.md)

[**NetworkSettings**](element-networksettings.md)

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v2` |

 

 
