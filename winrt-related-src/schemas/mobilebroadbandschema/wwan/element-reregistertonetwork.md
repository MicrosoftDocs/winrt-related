---
Description: Defines timing information used to activate the subscriber's account on the Mobile Broadband Network (MNO) for a reregister activation type.
Search.Product: eADQiWindows 10XVcnh
title: ReregisterToNetwork
ms.assetid: 623c7f6a-64d7-4634-990f-ff0f0ccc4994
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# ReregisterToNetwork


Defines timing information used to activate the subscriber's account on the Mobile Broadband Network (MNO) for a reregister activation type.

## Element hierarchy

**&lt;ReregisterToNetwork&gt;**

## Syntax

``` syntax
<ReregisterToNetwork Delay?         = P[n]Y[n]M[n]DT[n]H[n]M[n]S duration : "PT0S"
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
<td><p>Defines the time until the next activation attempt. Duration time format is defined by [ISO 8601](http://www.iso.org/iso/catalogue_detail?csnumber=40874).</p></td>
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
<td><p>Defines the time between activation attempts. Duration time format is defined by [ISO 8601](http://www.iso.org/iso/catalogue_detail?csnumber=40874).</p></td>
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

 

 



