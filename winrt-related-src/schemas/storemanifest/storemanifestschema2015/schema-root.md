---
title: StoreManifest schema (Windows 10)
Description: StoreManifest schema (Windows 10)
Search.Product: eADQiWindows 10XVcnh
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, storemanifest
---

# StoreManifest schema (Windows 10)


StoreManifest.xml is an optional configuration file that may be included in a UWP package. Its purpose is to enable features, such as declaring your app as a Windows Store device app, that the AppxManifest.xml file does not cover. StoreManifest.xml is submitted with the application package and must be in the root folder of your app's main project.

**Note**  This section describes StoreManifest.xml for UWP packages targeting Windows 10. For packages targeting Windows 8.1 and earlier, see [StoreManifest schema (Windows 8.1 and earlier)](https://msdn.microsoft.com/library/windows/apps/jj730526).

 

To validate your StoreManifest.xml, create a new xml document in Microsoft Visual Studio and add the following declaration:

`http://schemas.microsoft.com/appx/2015/StoreManifest namespace`

See the samples instance document in [StoreManifest XML example (Windows 10)](storemanifest-xml-example-windows-10.md).

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
<td>[Dependencies](element-dependencies.md)</td>
<td><p>Declares requirements that a package depends on to be applicable to a device.</p></td>
</tr>
<tr class="even">
<td>[DeviceCompanionApplication](element-devicecompanionapplication.md)</td>
<td><p>The DeviceCompanionApplication element contains all the configuration required to declare your app as a Windows Store device app.</p></td>
</tr>
<tr class="odd">
<td>[DirectXDependency](element-directxdependency.md)</td>
<td><p>Identifies the minimum DirectX level that a device must support in order for your package to run properly.</p></td>
</tr>
<tr class="even">
<td>[ExperienceId](element-experienceid.md)</td>
<td><p>The ExperienceId element specifies a GUID that links the device metadata to a device app that can be automatically acquired when the device is first connected. Each ExperienceId GUID corresponds to the ExperienceId element of a device metadata package.</p></td>
</tr>
<tr class="odd">
<td>[MemoryDependency](element-memorydependency.md)</td>
<td><p>Identifies the minimum memory that a device must have in order for your package to run properly.</p>
<p>For desktop devices, the value indicates the requirement for installed memory. Available memory is not considered.</p>
<p>For mobile devices, the value indicates the requirements for available memory. The equivalent requirements for installed memory on mobile devices are as follows:</p>
<ul>
<li>300MB = device must have at least 1 GB of installed memory</li>
<li>750MB = device must have at least 2 GB of installed memory</li>
<li>1000MB = device must have at least 3 GB of installed memory</li>
<li>2000MB = device must have at least 4 GB of installed memory</li>
</ul>
<p>For example, if you specify that your UWP app requires 300 MB to run properly, it will only be able to be installed on mobile devices with &gt;1 GB of RAM or on desktop devices with &gt;300 MB of RAM.</p></td>
</tr>
<tr class="even">
<td>[StoreManifest](element-storemanifest.md)</td>
<td><p>Root node for the StoreManifest schema (for Windows 10).</p></td>
</tr>
<tr class="odd">
<td>[TargetDeviceFamily](element-targetdevicefamily.md)</td>
<td><p>Identifies the device family that your package targets.</p>
<div class="alert">
<strong>Important</strong>  In most cases, you should simply specify your device families in the [<strong>TargetDeviceFamily</strong>](https://msdn.microsoft.com/library/windows/apps/dn986903) element of your AppxManifest. Values here should only be used if you need to override that info (using a subset of the values provided there).
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

 

 



