---
description: Describes the orientations in which the app would prefer to be shown for the best user experience (extensions schema for Windows 8.1).
Search.Product: eADQiWindows 10XVcnh
title: InitialRotationPreference (Windows 8.1 extensions schema)
ms.assetid: 0f03085b-0bbc-4e1c-adda-565bb6287b15


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# InitialRotationPreference (extensions schema for Windows 8.1)




Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.

Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.

These orientation preference choices apply to both the [**splash screen**](element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [**AutoRotationPreferences**](/uwp/api/Windows.Graphics.Display.DisplayInformation) property.

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

 

## Remarks

This element is part of your app manifest file (package.appxmanifest). In the Microsoft Visual Studio manifest editor, this setting is found under the **Application UI** tab as "Supported Initial Rotations". By default, none of the options are selected. This means that all rotation orientations are supported. Selecting either none of the rotations or all of the rotations gives the same result.

Because your app can be run on different device types—desktop PCs, tablets, laptops, or phones—you cannot be guaranteed advance knowledge of the orientation of the device at the time that your app is launched, nor that the device won't be rotated while the app is active. Therefore, we recommend that you develop your app with the ability to be displayed in any orientation. That said, your app can use this element to ask Windows to restrict the display of your app to its ideal rotations. However, Windows cannot always honor the request. Because not all devices can be rotated or detect rotation, orientation preferences cannot always be honored by Windows. For instance, if you state that your app should be displayed in Portrait but the app is run on a standard landscape-oriented desktop monitor or on a television, the preference will be ignored because showing the app on its side would be a poor user experience. For this reason, you should consider supporting all orientations so that your app looks good regardless of the device rotation.

**Note**  Because at this time desktop PCs and notebooks remain the statistically predominant devices that your app is likely to be run on, and because those devices are almost all fixed in a landscape orientation and do not detect rotation, it is required that an app support at least the Landscape rotation. However, while it must be supported, you are not required to declare Landscape as a preferred rotation.

 

This element contains up to 4 [**Rotation**](element-rotation.md) elements, each of which specifies an orientation in which the app prefers to be viewed. If you include no **Rotation** elements, it has the same effect as including all four.

The following example shows an app that will display in Landscape and LandscapeFlipped, but will not change its orientation for a device held in Portrait or PortraitFlipped.

```XML
                        
<InitialRotationPreference>
    <Rotation Preference="landscape"/>
    <Rotation Preference="landscapeFlipped"/>
</InitialRotationPreference>
                    
```

When your app is initially launched, Windows receives its rotation preferences. These preferences remain in place until that app is terminated, with one important exception: if a call is made to [**Windows.Graphics.Display.DisplayInformation.autoRotationPreferences**](/uwp/api/Windows.Graphics.Display.DisplayInformation) to change those preferences. That API is used to inform Windows of a change in your app's rotational preferences, and can be called at any time. Note that this API call does not affect the contents of the **InitialRotationPreference** element in the app's manifest file, which remain as you set them in the manifest editor. Therefore, whenever you relaunch your app, it takes the rotation preferences that you originally specified in your app's manifest.

For instance, consider a game app that is best viewed in Landscape, but that has a certain page that displays a map that is more readable in Portrait. The following series of events could take place on a device that supports rotation. A familiarity with [app lifecycle](/previous-versions/windows/apps/hh464925(v=win.10)) terms will be helpful to you here.

1.  The developer specifies Landscape and/or LandscapeFlipped rotation preferences for the app in the manifest editor.
2.  The game is installed and launched. The preferences specified in the manifest editor apply and the game will not rotate into Portrait.
3.  The game detects that the user is accessing the map. It calls [**AutoRotationPreferences**](/uwp/api/Windows.Graphics.Display.DisplayInformation) to tell Windows to change the app's rotational preferences to Portrait and/or PortraitFlipped.
4.  Windows rotates the app to the new preferred orientation.
5.  The user switches to another app to check their mail.
6.  The user switches back to the game app to continue where they left off. Windows knows that the app's last stated preference was for Portrait and brings the app onscreen in that orientation. Note that it did not refer to the **InitialRotationPreference** settings because the current session is still active.
7.  The game detects that the user is closing the map page. It calls [**AutoRotationPreferences**](/uwp/api/Windows.Graphics.Display.DisplayInformation) to change its rotational preferences back to its original Landscape settings to continue the game.
8.  The user finishes the game and the app is suspended after the user navigates away for some period of time.
9.  The user resumes the app to play another game. Because the app has not been relaunched, the last preferences declared by the [**AutoRotationPreferences**](/uwp/api/Windows.Graphics.Display.DisplayInformation) API still apply.
10. The game is closed (terminated).
11. The game is restarted. Because it is again starting from an initial launch, the **InitialRotationPreference** settings once again apply.

The key point to note is that once you've called [**AutoRotationPreferences**](/uwp/api/Windows.Graphics.Display.DisplayInformation), it is your responsibility to handle the rotational preferences through that API until the game is terminated (not merely suspended).

When an app rotates, Windows rotates with it. If you close the app in Portrait, the Start screen is shown in Portrait. If an app has stated a rotation preference for a different rotation than the device is currently displaying, the rotation of the system occurs while the app's splash screen is displayed. The main app UI will not be shown until the system rotation is complete behind it.

## See also


[**VisualElements**](../appxmanifestschema/element-visualelements.md)

[Quickstart: Creating a default tile using the Visual Studio manifest editor](/previous-versions/windows/apps/hh465437(v=win.10))

[**Windows.Graphics.Display.DisplayInformation.AutoRotationPreferences**](/uwp/api/Windows.Graphics.Display.DisplayInformation)

## Requirements

|               |    Value                                                         |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
