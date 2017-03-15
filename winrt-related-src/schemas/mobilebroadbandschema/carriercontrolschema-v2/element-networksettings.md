---
Description: NetworkSettings
MS-HAID: CarrierControlSchema\_v2.element\_NetworkSettings
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: NetworkSettings
ms.assetid: 82e8282b-5405-4fcf-b835-83fe6ec9a460
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# NetworkSettings


Defines the network settings in a subscriber's carrier provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-carriernetworkmetadata.md">&lt;CarrierNetworkMetadata&gt;</a></dt>
<dd><b>&lt;NetworkSettings&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<NetworkSettings>

  <!-- Child elements -->
  IPv4LinkMTU?,
  IPv6LinkMTU?,
  DNSRetrySettings?

</NetworkSettings>
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
<td>[DNSRetrySettings](element-dnsretrysettings.md)</td>
<td><p>Defines the network settings for DNS retries in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td>[IPv4LinkMTU](element-ipv4linkmtu.md)</td>
<td><p>Defines the maximum transmission unit (MTU) for an IPv4 link. It must be a positive integer between 1280 and 1500.</p></td>
</tr>
<tr class="odd">
<td>[IPv6LinkMTU](element-ipv6linkmtu.md)</td>
<td><p>Defines the maximum transmission unit (MTU) for an IPv6 link. It must be a positive integer between 1280 and 1500.</p></td>
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
<td>[CarrierNetworkMetadata](element-carriernetworkmetadata.md)</td>
<td><p>Defines the network properties and settings in a subscriber's carrier provisioning file.</p></td>
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

 

 



