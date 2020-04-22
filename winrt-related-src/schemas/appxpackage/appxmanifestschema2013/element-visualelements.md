---
Description: Describes the visual aspects of the UWP app. 
Search.Product: eADQiWindows 10XVcnh
title: VisualElements
ms.assetid: f0db5141-8aba-4ac4-939f-4fe3debcc761


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# VisualElements

Describes the visual aspects of the UWP app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.

## Element hierarchy

**&lt;VisualElements&gt;**

## Syntax

``` syntax
<VisualElements Square150x150Logo = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
                Square30x30Logo   = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both. >

  <!-- Child elements -->
  ( DefaultTile?
  & LockScreen?
  & SplashScreen
  & InitialRotationPreference?
  & ApplicationView?
  )

</VisualElements>
```

### Key

`?`   optional (zero or one) 

`&`   interleave connector (may occur in any order)

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
<td><strong>Square150x150Logo</strong></td>
<td><p>A 150x150 image used as the app's square tile. For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Square30x30Logo</strong></td>
<td><p>A 30x30 image used as the app's square tile. For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-applicationview.md">ApplicationView</a> </td>
<td><p>Describes how the app is viewed on the screen.</p></td>
</tr>
<tr class="even">
<td><a href="element-defaulttile.md">DefaultTile</a> </td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
<tr class="odd">
<td><a href="element-initialrotationpreference.md">InitialRotationPreference</a> </td>
<td><p>Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.</p>
<p>Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.</p>
<p>These orientation preference choices apply to both the [<strong>splash screen</strong>](element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [<strong>AutoRotationPreferences</strong>](https://msdn.microsoft.com/library/windows/apps/dn264259) property.</p></td>
</tr>
<tr class="even">
<td><a href="element-lockscreen.md">LockScreen</a> </td>
<td><p>Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.</p></td>
</tr>
<tr class="odd">
<td><a href="element-splashscreen.md">SplashScreen</a> </td>
<td><p>Defines the appearance of the splash screen, which is displayed by the app during launch.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

For more info about visual aspects for apps, see [**VisualElements**](https://msdn.microsoft.com/library/windows/apps/dn423310).

The manifest performs these semantic checks for **VisualElements**, which aren't enforced in the schema.

-   If [**DefaultTile\\Square310x310Logo**](element-defaulttile.md) is specified, **DefaultTile\\Wide310x150Logo** must also be specified.
-   If [**DefaultTile\\DefaultSize**](element-defaulttile.md) or [**ShowNameOnTiles**](element-shownameontiles.md) specify a certain image size value, that image size must have been declared in the manifest.
-   If [**LockScreen\\Notification**](https://msdn.microsoft.com/library/windows/apps/dn423284) is set to **badgeAndTileText**, [**DefaultTile\\Wide310x150Logo**](element-defaulttile.md) must be specified.

**Square150x150Logo** and **Square30x30Logo** images can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply localized images to match different UI languages. For more info, see the [Globalization](https://msdn.microsoft.com/library/windows/apps/hh831183) topic.

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 



