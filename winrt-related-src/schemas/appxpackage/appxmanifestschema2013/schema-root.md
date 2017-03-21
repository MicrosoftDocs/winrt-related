---
Description: Provides details for each element, attribute, and data type of each feature extension that defines the schema for the app package manifest for Windows 8.1 Windows Store apps.
Search.Product: eADQiWindows 10XVcnh
title: Package manifest schema with feature extensions reference
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, package manifest
---

# Package manifest schema with feature extensions reference


This reference provides details for each element, attribute, and data type of each feature extension that defines the schema for the app package manifest for Windows 8.1 Windows Store apps. The schema definition file is AppxManifestSchema2013.xsd. The AppxManifestSchema2013.xsd file imports the AppxManifestSchema2010\_v2.xsd file. The Windows 8 schema is AppxManifestSchema.xsd.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[ApplicationView](element-applicationview.md)</td>
<td><p>Describes how the app is viewed on the screen.</p></td>
</tr>
<tr class="even">
<td>[AppointmentsProvider](element-appointmentsprovider.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.appointmentsProvider</strong>.</p></td>
</tr>
<tr class="odd">
<td>[AppointmentsProviderLaunchActions](element-appointmentsproviderlaunchactions.md)</td>
<td><p>Declares actions to take when a appointment is launched.</p></td>
</tr>
<tr class="even">
<td>[Contact](element-contact.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.contact</strong>.</p></td>
</tr>
<tr class="odd">
<td>[ContactLaunchActions](element-contactlaunchactions.md)</td>
<td><p>Declares actions to take when a contact is launched.</p></td>
</tr>
<tr class="even">
<td>[DefaultTile](element-defaulttile.md)</td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
<tr class="odd">
<td>[Device](element-device.md)</td>
<td><p>Declares a function for a device that is associated with the [<strong>DeviceCapability</strong>](element-devicecapability.md).</p></td>
</tr>
<tr class="even">
<td>[DeviceCapability](element-devicecapability.md)</td>
<td><p>Declares a device capability required by a package.</p></td>
</tr>
<tr class="odd">
<td>[Extension](element-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
<tr class="even">
<td>[Function](element-function.md)</td>
<td><p>Declares the function for the device.</p></td>
</tr>
<tr class="odd">
<td>[InitialRotationPreference](element-initialrotationpreference.md)</td>
<td><p>Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.</p>
<p>Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.</p>
<p>These orientation preference choices apply to both the [<strong>splash screen</strong>](element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [<strong>AutoRotationPreferences</strong>](https://msdn.microsoft.com/library/windows/apps/dn264259) property.</p></td>
</tr>
<tr class="even">
<td>[LaunchAction (in AppointmentsProviderLaunchActions)](element-1-launchaction.md)</td>
<td><p>Describes an [<strong>AppointmentsProviderLaunchActions</strong>](element-appointmentsproviderlaunchactions.md) content action.</p></td>
</tr>
<tr class="odd">
<td>[LaunchAction (in ContactLaunchActions)](element-launchaction.md)</td>
<td><p>Describes a [<strong>ContactLaunchActions</strong>](element-contactlaunchactions.md) content action.</p></td>
</tr>
<tr class="even">
<td>[LockScreen](element-lockscreen.md)</td>
<td><p>Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.</p></td>
</tr>
<tr class="odd">
<td>[ResourcePackage](element-resourcepackage.md)</td>
<td><p>Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is <strong>false</strong> by default. You should not specify a value for it unless you are creating a resource.</p></td>
</tr>
<tr class="even">
<td>[Rotation](element-rotation.md)</td>
<td><p>Specifies a single rotational orientation in which an app will display.</p></td>
</tr>
<tr class="odd">
<td>[ServiceId](element-serviceid.md)</td>
<td><p>Identifies the service for a contact action.</p></td>
</tr>
<tr class="even">
<td>[ShowNameOnTiles](element-shownameontiles.md)</td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.</p></td>
</tr>
<tr class="odd">
<td>[ShowOn](element-showon.md)</td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen.</p></td>
</tr>
<tr class="even">
<td>[SplashScreen](element-splashscreen.md)</td>
<td><p>Defines the appearance of the splash screen, which is displayed by the app during launch.</p></td>
</tr>
<tr class="odd">
<td>[Task](element-task.md)</td>
<td><p>The background task associated with the app extensibility point.</p></td>
</tr>
<tr class="even">
<td>[TileUpdate](element-tileupdate.md)</td>
<td><p>Describes how the app tile receives update notifications.</p></td>
</tr>
<tr class="odd">
<td>[VisualElements](element-visualelements.md)</td>
<td><p>Describes the visual aspects of the Windows Store app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
</tbody>
</table>

 

 

 



