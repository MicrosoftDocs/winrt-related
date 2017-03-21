---
Description: Defines the DNS retry interval in seconds. 
Search.Product: eADQiWindows 10XVcnh
title: DNSRetryIntervalInSeconds
ms.assetid: 0240b016-78a5-4512-8c26-9bc3713a2e59
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# DNSRetryIntervalInSeconds


Defines the DNS retry interval in seconds. It must be a positive integer between 1 and 4.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-carriernetworkmetadata.md">&lt;CarrierNetworkMetadata&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-networksettings.md">&lt;NetworkSettings&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dnsretrysettings.md">&lt;DNSRetrySettings&gt;</a></dt>
<dd><b>&lt;DNSRetryIntervalInSeconds&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DNSRetryIntervalInSeconds>

  Defines a simple type for the DNS retry interval.

</DNSRetryIntervalInSeconds>
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
<td>[DNSRetrySettings](element-dnsretrysettings.md)</td>
<td><p>Defines the network settings for DNS retries in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This setting is applied to all the profiles defined in a subscriber's carrier provisioning file.

## See also


[CarrierControlSchema schema](https://msdn.microsoft.com/library/windows/apps/hh868312)

[CarrierControlSchema\_v2 schema](schema-root.md)

[**DNSRetrySettings**](element-dnsretrysettings.md)

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

 

 



