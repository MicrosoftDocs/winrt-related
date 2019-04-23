---
Description: Defines the DNS retry count.
Search.Product: eADQiWindows 10XVcnh
title: DNSRetryCount
ms.assetid: 3fa80714-0ad9-4b7a-9c4a-3dd9fa96bf9a
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# DNSRetryCount


Defines the DNS retry count. It must be a positive integer between 1 and 4.

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
<dd><b>&lt;DNSRetryCount&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DNSRetryCount>

  Defines a simple type for the DNS retry count.

</DNSRetryCount>
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
<td><a href="element-dnsretrysettings.md">DNSRetrySettings</a> </td>
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

 

 



