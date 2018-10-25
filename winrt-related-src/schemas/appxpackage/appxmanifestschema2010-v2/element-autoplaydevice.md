---
Description: Declares an app extensibility point of type windows.autoPlayDevice.
Search.Product: eADQiWindows 10XVcnh
title: AutoPlayDevice
ms.assetid: f01934d7-ad54-455d-bfb9-ef2560bb02ad
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# AutoPlayDevice




Declares an app extensibility point of type **windows.autoPlayDevice**. The app provides the specified AutoPlay device actions.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;AutoPlayDevice&gt;</b></dd>
</dl>

## Syntax

``` syntax
<AutoPlayDevice>

  <!-- Child elements -->
  LaunchAction{1,1000}

</AutoPlayDevice>
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
<td>[LaunchAction (in type: CT_AutoPlayDevice)](element-1-launchaction.md)</td>
<td><p>Describes an AutoPlay device action.</p></td>
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
<td>[Extension (type: CT_ApplicationExtension)](element-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

When a device that is not volume-based is connected to a computer, the system raises an AutoPlay device event. This extensibility point enables your app to be listed as an AutoPlay choice for one or more AutoPlay device events. Because these devices are not volume-based, the system provides the app with device information rather than a file folder.

## Examples

```XML
<Extension Category="windows.autoPlayDevice">
  <AutoPlayDevice>
    <LaunchAction Verb="startDeviceApp" ActionDisplayName="Start my device app" DeviceEvent="CustomDeviceEvent"/>
  </AutoPlayDevice>
</Extension>
```

## See also


**Tasks**
[Auto-launching with AutoPlay](https://msdn.microsoft.com/library/windows/apps/hh452731)

**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



