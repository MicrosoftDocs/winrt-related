---
Description: The ProductFeatures element is the container for all existing and future product features that will be configured through the StoreManifest XML file.
Search.Product: eADQiWindows 10XVcnh
title: ProductFeatures
ms.assetid: 95f2ec1b-e3d1-490d-a5dc-367e385f7fc5


keywords: windows 10, uwp, schema, storemanifest


ms.topic: reference
ms.date: 04/05/2017
---

# ProductFeatures


The ProductFeatures element is the container for all existing and future product features that will be configured through the StoreManifest XML file.

## Element hierarchy

<dl>
<dt><a href="element-storemanifest.md">&lt;StoreManifest&gt;</a></dt>
<dd><b>&lt;ProductFeatures&gt;</b></dd>
</dl>

## Syntax

``` syntax
<ProductFeatures>

  <!-- Child elements -->
  ( DeviceCompanionApplication?
  & ExclusiveOptOut?
  & PreinstallOptOut?
  )

</ProductFeatures>
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
<td><a href="element-devicecompanionapplication.md">DeviceCompanionApplication</a> </td>
<td><p>The DeviceCompanionApplication element contains all the configuration required to declare your app as a Microsoft Store device app.</p></td>
</tr>
<tr class="even">
<td><a href="element-exclusiveoptout.md">ExclusiveOptOut</a> </td>
<td><p>Do not use. The ExclusiveOptOut element is no longer read by the Microsoft Store.</p></td>
</tr>
<tr class="odd">
<td><a href="element-preinstalloptout.md">PreinstallOptOut</a> </td>
<td><p>Do not use. The PreinstallOptOut element is no longer read by the Microsoft Store.</p></td>
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
<td><a href="element-storemanifest.md">StoreManifest</a> </td>
<td><p>Root node for the StoreManifest schema (for Windows 8.1 and earlier).</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The StoreManifest schema allows the ProductFeatures element to be empty. If so, the StoreManifest.xml will have no effect at app onboarding (as if no StoreManifest.xml was submitted with the app).

## Examples

The following is an example of the ProductFeatures element that declares the app as a device app.

```XML
<ProductFeatures>     
    <DeviceCompanionApplication>
        <ExperienceIds>
            <ExperienceId>aeabdaa8-3bcd-4f03-a7f5-54647fd574c2</ExperienceId>
        </ExperienceIds>
    </DeviceCompanionApplication>   
</ProductFeatures>
```

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/StoreManifest` |

 

 



