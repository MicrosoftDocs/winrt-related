---
Description: Defines information for a subscriber's activation method on a Mobile Network Operator's (MNO) network.
Search.Product: eADQiWindows 10XVcnh
title: Activation
ms.assetid: d01c586b-a738-4506-a18e-a8c6475d77cd

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
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
<td><a href="element-activationmethod.md">ActivationMethod</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868442"><strong>ActivationMethod</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868486"><strong>WWAN</strong></a> schema.</p></td>
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

 

 



