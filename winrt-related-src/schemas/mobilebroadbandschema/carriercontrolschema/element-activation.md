---
Description: Activation
MS-HAID: CarrierControlSchema.element\_Activation
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Activation
ms.assetid: d01c586b-a738-4506-a18e-a8c6475d77cd
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# Activation


Defines information for a subscriber's activation method on a Mobile Network Operator's (MNO) network.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd><b>&lt;Activation&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Activation>

  <!-- Child elements -->
  ActivationMethod

</Activation>
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
<td>[ActivationMethod](element-activationmethod.md)</td>
<td><p>Defines an instance of the [<strong>ActivationMethod</strong>](https://msdn.microsoft.com/library/windows/apps/hh868442) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
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
<td>[CarrierProvisioning](element-carrierprovisioning.md)</td>
<td><p>Defines the properties and settings in a subscriber's carrier provisioning file. [<strong>CarrierProvisioning</strong>](element-carrierprovisioning.md) is the unique root element of the provisioning file.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/v1</p></td>
</tr>
</tbody>
</table>

 

 



