---
Description: Defines timing information used to activate the subscriber's account on the Mobile Broadband Network (MNO) for a reconnect activation type.
Search.Product: eADQiWindows 10XVcnh
title: ReconnectToNetwork
ms.assetid: ae345c7f-83c1-4194-b577-515d07c70c8c

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# ReconnectToNetwork


Defines timing information used to activate the subscriber's account on the Mobile Broadband Network (MNO) for a reconnect activation type.

## Element hierarchy

**&lt;ReconnectToNetwork&gt;**

## Syntax

``` syntax
<ReconnectToNetwork Delay?         = P[n]Y[n]M[n]DT[n]H[n]M[n]S duration : "PT0S"
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

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/WWAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



