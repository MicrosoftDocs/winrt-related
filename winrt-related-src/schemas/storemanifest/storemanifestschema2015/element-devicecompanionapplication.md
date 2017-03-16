---
Description: DeviceCompanionApplication
MS-HAID: StoreManifestSchema2015.element\_DeviceCompanionApplication
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: DeviceCompanionApplication
ms.assetid: 302f6805-4684-4061-bb60-c0fcff710758
author: laurenhughes
ms.author: lahugh
windows 10, uwp, schema, storemanifest
---

# DeviceCompanionApplication


The DeviceCompanionApplication element contains all the configuration required to declare your app as a Windows Store device app.

## Element hierarchy

<dl>
<dt><a href="element-storemanifest.md">&lt;StoreManifest&gt;</a></dt>
<dd><b>&lt;DeviceCompanionApplication&gt;</b></dd>
</dl>

## Syntax

``` syntax
<DeviceCompanionApplication>

  <!-- Child elements -->
  ExperienceId{1,500}

</DeviceCompanionApplication>
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
<td>[ExperienceId](element-experienceid.md)</td>
<td><p>The ExperienceId element specifies a GUID that links the device metadata to a device app that can be automatically acquired when the device is first connected. Each ExperienceId GUID corresponds to the ExperienceId element of a device metadata package.</p></td>
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
<td>[StoreManifest](element-storemanifest.md)</td>
<td><p>Root node for the StoreManifest schema (for Windows 10).</p></td>
</tr>
</tbody>
</table>

 

## Remarks

When present, the DeviceCompanionApplication element must contain an ExperienceId element, which is described below.

**Important**  Using the DeviceCompanionApplication element in StoreManifest.xml and submitting it with your app will declare your app as a device app in the Windows Store. This action cannot be undone in the same product release. If you wish to release this app without the features and constraints that are applied to device apps, you will need to create and submit a new release with an updated StoreManifest.xml file. For more info, see [Windows Store device apps](http://go.microsoft.com/fwlink/?LinkID=301381).

 

## Examples

The following is an example of the DeviceCompanionApplication element that declares the app as a device app.

```XML
       <DeviceCompanionApplication>
            <ExperienceId>aeabdaa8-3bcd-4f03-a7f5-54647fd574c2</ExperienceId>
    </DeviceCompanionApplication>   
</ProductFeatures>
```

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

 

 



