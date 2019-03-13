---
Description: Defines the tethering settings in a subscriber's carrier provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: TetheringSettings
ms.assetid: 0bf2129c-0589-437a-8cfa-834b16ce42a2
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# TetheringSettings


Defines the tethering settings in a subscriber's carrier provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-additionalpdpcontexts.md">&lt;AdditionalPDPContexts&gt;</a></dt>
<dd><b>&lt;TetheringSettings&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TetheringSettings>

  <!-- Child elements -->
  TetheringProfile?,
  MaxNumberOfDevices?

</TetheringSettings>
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
<td><a href="element-maxnumberofdevices.md">MaxNumberOfDevices</a> </td>
<td><p>Defines the maximum number of tethered connections.</p></td>
</tr>
<tr class="even">
<td><a href="element-tetheringprofile.md">TetheringProfile</a> </td>
<td><p>Defines the tethering profile in a subscriber's carrier provisioning file.</p></td>
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


[**AdditionalPDPContexts**](element-additionalpdpcontexts.md)

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

 

 



