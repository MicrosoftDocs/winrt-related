---
description: Defines the abstract base element for ReconnectToNetwork, ReregisterToNetwork, and ServiceActivation.
Search.Product: eADQiWindows 10XVcnh
title: ActivationMethod (WWAN schema)
ms.assetid: bd57da53-5b6a-47e7-a240-5e300ad9d133

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# ActivationMethod (WWAN schema)


Defines the abstract base element for [**ReconnectToNetwork**](element-reconnecttonetwork.md), [**ReregisterToNetwork**](element-reregistertonetwork.md), and [**ServiceActivation**](element-serviceactivation.md).

## Element hierarchy

**&lt;ActivationMethod&gt;**

## Syntax

``` syntax
<ActivationMethod Delay?         = P[n]Y[n]M[n]DT[n]H[n]M[n]S duration : "PT0S"
                  RetryCount?    = positive integer : "0"
                  RetryInterval? = P[n]Y[n]M[n]DT[n]H[n]M[n]S duration : "PT1M" />
```

### Key

`?`   optional (zero or one)
`:`   default value
## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Delay</strong></td>
<td><p>Defines the time until the next activation attempt. Duration time format is defined by <a href="https://www.iso.org/iso/catalogue_detail?csnumber=40874">ISO 8601</a> .</p></td>
<td>P[n]Y[n]M[n]DT[n]H[n]M[n]S duration</td>
<td>No</td>
<td>PT0S</td>
</tr>
<tr class="even">
<td><strong>RetryCount</strong></td>
<td><p>Defines the number of activation attempts.</p></td>
<td>positive integer</td>
<td>No</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>RetryInterval</strong></td>
<td><p>Defines the time between activation attempts. Duration time format is defined by <a href="https://www.iso.org/iso/catalogue_detail?csnumber=40874">ISO 8601</a> .</p></td>
<td>P[n]Y[n]M[n]DT[n]H[n]M[n]S duration</td>
<td>No</td>
<td>PT1M</td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



