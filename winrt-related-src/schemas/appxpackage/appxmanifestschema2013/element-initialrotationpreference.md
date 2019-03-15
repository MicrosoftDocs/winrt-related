---
Description: Describes the orientations in which the app would prefer to be shown for the best user experience. 
Search.Product: eADQiWindows 10XVcnh
title: InitialRotationPreference
ms.assetid: 0f03085b-0bbc-4e1c-adda-565bb6287b15
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# InitialRotationPreference

Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.

Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.

These orientation preference choices apply to both the [**splash screen**](element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [**AutoRotationPreferences**](https://msdn.microsoft.com/library/windows/apps/dn264259) property.

## Element hierarchy

<dl>
<dt><a href="element-visualelements.md">&lt;VisualElements&gt;</a></dt>
<dd><b>&lt;InitialRotationPreference&gt;</b></dd>
</dl>

## Syntax

``` syntax
<InitialRotationPreference>

  <!-- Child elements -->
  Rotation{1,4}

</InitialRotationPreference>
```

### Key

`{}`   specific range of occurrences
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
<td><a href="element-rotation.md">Rotation</a> </td>
<td><p>Specifies a single rotational orientation in which an app will display.</p></td>
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
<td><a href="element-visualelements.md">VisualElements</a> </td>
<td><p>Describes the visual aspects of the UWP app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2013/manifest</p></td>
</tr>
</tbody>
</table>

 

 



