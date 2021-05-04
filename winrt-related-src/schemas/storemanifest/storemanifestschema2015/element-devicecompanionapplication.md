---
description: The DeviceCompanionApplication element contains all the configuration required to declare your app as a Microsoft Store device app.
Search.Product: eADQiWindows 10XVcnh
title: DeviceCompanionApplication (StoreManifest schema for Windows 10)
ms.assetid: 302f6805-4684-4061-bb60-c0fcff710758


keywords: windows 10, uwp, schema, storemanifest


ms.topic: reference
ms.date: 04/05/2017
---

# DeviceCompanionApplication (StoreManifest schema for Windows 10)


The DeviceCompanionApplication element contains all the configuration required to declare your app as a Microsoft Store device app.

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
<td><a href="element-experienceid.md">ExperienceId</a> </td>
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
<td><a href="element-storemanifest.md">StoreManifest</a> </td>
<td><p>Root node for the StoreManifest schema (for Windows 10).</p></td>
</tr>
</tbody>
</table>

 

## Remarks

When present, the DeviceCompanionApplication element must contain an ExperienceId element, which is described below.

**Important**  Using the DeviceCompanionApplication element in StoreManifest.xml and submitting it with your app will declare your app as a device app in the Microsoft Store. This action cannot be undone in the same product release. If you wish to release this app without the features and constraints that are applied to device apps, you will need to create and submit a new release with an updated StoreManifest.xml file. For more info, see [Microsoft Store device apps](/windows-hardware/drivers/devapps/).

 

## Examples

The following is an example of the DeviceCompanionApplication element that declares the app as a device app.

```XML
       <DeviceCompanionApplication>
            <ExperienceId>aeabdaa8-3bcd-4f03-a7f5-54647fd574c2</ExperienceId>
    </DeviceCompanionApplication>   
</ProductFeatures>
```

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2015/StoreManifest` |

 

 
