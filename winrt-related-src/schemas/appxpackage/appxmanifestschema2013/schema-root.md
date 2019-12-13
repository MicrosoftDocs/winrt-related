---
Description: Provides details for each element, attribute, and data type of each feature extension that defines the schema for the app package manifest for Windows 8.1 apps.
Search.Product: eADQiWindows 10XVcnh
title: Windows 8.1 feature extensions manifest schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c

keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Windows 8.1 feature extensions manifest schema


This reference provides details for each element, attribute, and data type of each feature extension that defines the schema for the app package manifest for Windows 8.1 apps. The schema definition file is AppxManifestSchema2013.xsd. The AppxManifestSchema2013.xsd file imports the AppxManifestSchema2010\_v2.xsd file. The Windows 8 schema is AppxManifestSchema.xsd.

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
<td><a href="element-applicationview.md">ApplicationView</a> </td>
<td><p>Describes how the app is viewed on the screen.</p></td>
</tr>
<tr class="even">
<td><a href="element-appointmentsprovider.md">AppointmentsProvider</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.appointmentsProvider</strong>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-appointmentsproviderlaunchactions.md">AppointmentsProviderLaunchActions</a> </td>
<td><p>Declares actions to take when a appointment is launched.</p></td>
</tr>
<tr class="even">
<td><a href="element-contact.md">Contact</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.contact</strong>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-contactlaunchactions.md">ContactLaunchActions</a> </td>
<td><p>Declares actions to take when a contact is launched.</p></td>
</tr>
<tr class="even">
<td><a href="element-defaulttile.md">DefaultTile</a> </td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
<tr class="odd">
<td><a href="element-device.md">Device</a> </td>
<td><p>Declares a function for a device that is associated with the <a href="element-devicecapability.md"><strong>DeviceCapability</strong></a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-devicecapability.md">DeviceCapability</a> </td>
<td><p>Declares a device capability required by a package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-extension.md">Extension</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
<tr class="even">
<td><a href="element-function.md">Function</a> </td>
<td><p>Declares the function for the device.</p></td>
</tr>
<tr class="odd">
<td><a href="element-initialrotationpreference.md">InitialRotationPreference</a> </td>
<td><p>Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.</p>
<p>Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.</p>
<p>These orientation preference choices apply to both the [<strong>splash screen</strong>](element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [<strong>AutoRotationPreferences</strong>](https://msdn.microsoft.com/library/windows/apps/dn264259) property.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-launchaction.md">LaunchAction (in AppointmentsProviderLaunchActions)</a> </td>
<td><p>Describes an <a href="element-appointmentsproviderlaunchactions.md"><strong>AppointmentsProviderLaunchActions</strong></a>  content action.</p></td>
</tr>
<tr class="odd">
<td><a href="element-launchaction.md">LaunchAction (in ContactLaunchActions)</a> </td>
<td><p>Describes a <a href="element-contactlaunchactions.md"><strong>ContactLaunchActions</strong></a>  content action.</p></td>
</tr>
<tr class="even">
<td><a href="element-lockscreen.md">LockScreen</a> </td>
<td><p>Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.</p></td>
</tr>
<tr class="odd">
<td><a href="element-resourcepackage.md">ResourcePackage</a> </td>
<td><p>Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is <strong>false</strong> by default. You should not specify a value for it unless you are creating a resource.</p></td>
</tr>
<tr class="even">
<td><a href="element-rotation.md">Rotation</a> </td>
<td><p>Specifies a single rotational orientation in which an app will display.</p></td>
</tr>
<tr class="odd">
<td><a href="element-serviceid.md">ServiceId</a> </td>
<td><p>Identifies the service for a contact action.</p></td>
</tr>
<tr class="even">
<td><a href="element-shownameontiles.md">ShowNameOnTiles</a> </td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.</p></td>
</tr>
<tr class="odd">
<td><a href="element-showon.md">ShowOn</a> </td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen.</p></td>
</tr>
<tr class="even">
<td><a href="element-splashscreen.md">SplashScreen</a> </td>
<td><p>Defines the appearance of the splash screen, which is displayed by the app during launch.</p></td>
</tr>
<tr class="odd">
<td><a href="element-task.md">Task</a> </td>
<td><p>The background task associated with the app extensibility point.</p></td>
</tr>
<tr class="even">
<td><a href="element-tileupdate.md">TileUpdate</a> </td>
<td><p>Describes how the app tile receives update notifications.</p></td>
</tr>
<tr class="odd">
<td><a href="element-visualelements.md">VisualElements</a> </td>
<td><p>Describes the visual aspects of the UWP app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
</tbody>
</table>

 

 

 



