---
Description: Defines the network settings for DNS retries in a subscriber's carrier provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: DNSRetrySettings
ms.assetid: 2749204f-5d80-4b44-9c65-b0d62931e269
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# DNSRetrySettings


Defines the network settings for DNS retries in a subscriber's carrier provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-carriernetworkmetadata.md">&lt;CarrierNetworkMetadata&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-networksettings.md">&lt;NetworkSettings&gt;</a></dt>
<dd><b>&lt;DNSRetrySettings&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DNSRetrySettings>

  <!-- Child elements -->
  DNSRetryIntervalInSeconds,
  DNSRetryCount

</DNSRetrySettings>
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
<td>[DNSRetryCount](element-dnsretrycount.md)</td>
<td><p>Defines the DNS retry count. It must be a positive integer between 1 and 4.</p></td>
</tr>
<tr class="even">
<td>[DNSRetryIntervalInSeconds](element-dnsretryintervalinseconds.md)</td>
<td><p>Defines the DNS retry interval in seconds. It must be a positive integer between 1 and 4.</p></td>
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
<td>[NetworkSettings](element-networksettings.md)</td>
<td><p>Defines the network settings in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## See also


[CarrierControlSchema schema](https://msdn.microsoft.com/library/windows/apps/hh868312)

[CarrierControlSchema\_v2 schema](schema-root.md)

[**NetworkSettings**](element-networksettings.md)

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

 

 



