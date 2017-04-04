---
Description: StoreManifest schema for Windows 8.1 and earlier
Search.Product: eADQiWindows 10XVcnh
title: StoreManifest
ms.assetid: 01d2ebcb-9da0-4bcc-9eb4-c284810f894b
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, storemanifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# StoreManifest


Root node for the StoreManifest schema (for Windows 8.1 and earlier).

## Element hierarchy

**&lt;StoreManifest&gt;**

## Syntax

``` syntax
<StoreManifest>

  <!-- Child elements -->
  ProductFeatures?

</StoreManifest>
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
<td>[ProductFeatures](element-productfeatures.md)</td>
<td><p>The ProductFeatures element is the container for all existing and future product features that will be configured through the StoreManifest XML file.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

For UWP apps, see [StoreManifest schema](https://msdn.microsoft.com/library/windows/apps/mt617335).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/StoreManifest</p></td>
</tr>
</tbody>
</table>

 

 



