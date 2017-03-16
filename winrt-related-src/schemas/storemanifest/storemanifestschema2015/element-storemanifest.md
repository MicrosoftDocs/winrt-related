---
Description: StoreManifest
MS-HAID: StoreManifestSchema2015.element\_StoreManifest
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: StoreManifest
ms.assetid: 01d2ebcb-9da0-4bcc-9eb4-c284810f894b
author: laurenhughes
ms.author: lahugh
windows 10, uwp, schema, storemanifest
---

# StoreManifest


Root node for the StoreManifest schema (for Windows 10).

## Element hierarchy

**&lt;StoreManifest&gt;**

## Syntax

``` syntax
<StoreManifest>

  <!-- Child elements -->
  ( DeviceCompanionApplication?
  & Dependencies?
  )

</StoreManifest>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

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
<td>[Dependencies](element-dependencies.md)</td>
<td><p>Declares requirements that a package depends on to be applicable to a device.</p></td>
</tr>
<tr class="even">
<td>[DeviceCompanionApplication](element-devicecompanionapplication.md)</td>
<td><p>The DeviceCompanionApplication element contains all the configuration required to declare your app as a Windows Store device app.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

For apps targeting earlier OS versions, see [StoreManifest schema (Windows 8.1 and earlier)](https://msdn.microsoft.com/library/windows/apps/jj730526).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2015/StoreManifest</p></td>
</tr>
</tbody>
</table>

 

 



