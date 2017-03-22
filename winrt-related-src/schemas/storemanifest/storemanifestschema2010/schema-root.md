---
Description: StoreManifest schema (Windows 8.1 and earlier)
Search.Product: eADQiWindows 10XVcnh
title: StoreManifest schema (Windows 8.1 and earlier)
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, storemanifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# StoreManifest schema (Windows 8.1 and earlier)


StoreManifest.xml is an optional configuration file that may be included in the package of Windows Store app packages. Its purpose is to enable features, such as declaring your app as a Windows Store device app, that the AppxManifest.xml file does not cover. StoreManifest.xml is submitted with the application package and must be in the root folder of your app's main project.

**Note**  This section describes StoreManifest.xml for packages targeting Windows 8.1 and earlier. For Windows 10, see [StoreManifest schema (Windows 10)](https://msdn.microsoft.com/library/windows/apps/mt617335).

 

To validate your StoreManifest.xml, create a new xml document in Microsoft Visual Studio and add the following declaration:

`http://schemas.microsoft.com/appx/2010/StoreManifest namespace`

See the samples instance document in [StoreManifest XML example (Windows 8.1 and earlier)](https://msdn.microsoft.com/library/windows/apps/jj730527).

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
<td>[DeviceCompanionApplication](element-devicecompanionapplication.md)</td>
<td><p>The DeviceCompanionApplication element contains all the configuration required to declare your app as a Windows Store device app.</p></td>
</tr>
<tr class="even">
<td>[ExclusiveOptOut](element-exclusiveoptout.md)</td>
<td><p>Do not use. The ExclusiveOptOut element is no longer read by the Windows Store.</p></td>
</tr>
<tr class="odd">
<td>[ExperienceId](element-experienceid.md)</td>
<td><p>The ExperienceId element specifies a GUID that links the device metadata to a device app that can be automatically acquired when the device is first connected. Each ExperienceId GUID corresponds to the ExperienceId element of a device metadata package.</p></td>
</tr>
<tr class="even">
<td>[ExperienceIds](element-experienceids.md)</td>
<td><p>The ExperienceIds element contains a list of one or more individual ExperienceId elements.</p></td>
</tr>
<tr class="odd">
<td>[PreinstallOptOut](element-preinstalloptout.md)</td>
<td><p>Do not use. The PreinstallOptOut element is no longer read by the Windows Store.</p></td>
</tr>
<tr class="even">
<td>[ProductFeatures](element-productfeatures.md)</td>
<td><p>The ProductFeatures element is the container for all existing and future product features that will be configured through the StoreManifest XML file.</p></td>
</tr>
<tr class="odd">
<td>[StoreManifest](element-storemanifest.md)</td>
<td><p>Root node for the StoreManifest schema (for Windows 8.1 and earlier).</p></td>
</tr>
</tbody>
</table>

 

 

 



