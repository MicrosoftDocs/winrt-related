---
Description: Defines the mobile broadband Purchase and Internet profiles to be used for the mobile network.
Search.Product: eADQiWindows 10XVcnh
title: MobileBroadbandProfiles
ms.assetid: 4d95a695-e120-4de3-acac-b5d44d16da1a
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# MobileBroadbandProfiles

**Note**  The **MobileBroadbandProfiles** element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Internet and Purchase APN information.

Defines the mobile broadband Purchase and Internet profiles to be used for the mobile network.

## Element hierarchy

<dl>
<dt><a href="element-mobilebroadbandinfo.md">&lt;MobileBroadbandInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-networkconfiguration.md">&lt;NetworkConfiguration&gt;</a></dt>
<dd><b>&lt;MobileBroadbandProfiles&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<MobileBroadbandProfiles>

  <!-- Child elements -->
  Purchase?,
  Internet?,
  any element in a non-schema namespace*

</MobileBroadbandProfiles>
```

### Key

`?`   optional (zero or one)
`*`   optional (zero or more)

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
<td>[Internet](element-internet.md)</td>
<td><div class="alert">
<strong>Note</strong>  The <strong>Internet</strong> element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Internet APN information.
</div>
<div>
 
</div>
<p>Defines the mobile broadband Internet profile to be used for the mobile network.</p></td>
</tr>
<tr class="even">
<td>[Purchase](element-purchase.md)</td>
<td><div class="alert">
<strong>Note</strong>  The <strong>Purchase</strong> element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Purchase APN information.
</div>
<div>
 
</div>
<p>Defines the mobile broadband Purchase profile to be used for the mobile network.</p></td>
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
<td>[NetworkConfiguration](element-networkconfiguration.md)</td>
<td><div class="alert">
<strong>Note</strong>  The <strong>NetworkConfiguration</strong> element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Purchase and Internet APN information.
</div>
<div>
 
</div>
<p>Defines the network configuration for the mobile broadband Purchase and Internet profiles to be used for mobile network.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**MobileBroadbandInfo**](element-mobilebroadbandinfo.md)

[**NetworkConfiguration**](element-networkconfiguration.md)

[MBAE schema](schema-root.md)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo</p></td>
</tr>
</tbody>
</table>

 

 



