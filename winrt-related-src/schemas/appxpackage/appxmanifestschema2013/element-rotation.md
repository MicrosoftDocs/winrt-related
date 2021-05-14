---
description: Specifies a single rotational orientation in which an app will display.
Search.Product: eADQiWindows 10XVcnh
title: Rotation (Windows 8.1 feature extensions schema)
ms.assetid: 0e351d87-2ff0-4e9e-b3ea-6a6254d4c1c4


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Rotation (feature extensions schema for Windows 8.1)

Specifies a single rotational orientation in which an app will display.

## Element hierarchy

<dl>
<dt><a href="element-visualelements.md">&lt;VisualElements&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-initialrotationpreference.md">&lt;InitialRotationPreference&gt;</a></dt>
<dd><b>&lt;Rotation&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Rotation Preference = "portrait" | "landscape" | "portraitFlipped" | "landscapeFlipped" />
```

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
<td><strong>Preference</strong></td>
<td><p>The rotational orientation.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>portrait</li>
<li>landscape</li>
<li>portraitFlipped</li>
<li>landscapeFlipped</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-initialrotationpreference.md">InitialRotationPreference</a> </td>
<td><p>Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.</p>
<p>Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.</p>
<p>These orientation preference choices apply to both the [<strong>splash screen</strong>](element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [<strong>AutoRotationPreferences</strong>](/uwp/api/Windows.Graphics.Display.DisplayInformation) property.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

To specify more than one preferred orientation, include multiple [**Rotation**](../appxmanifestschema2010-v2/element-rotation.md) elements in your [**InitialRotationPreference**](../appxmanifestschema2010-v2/element-initialrotationpreference.md) element.

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 
