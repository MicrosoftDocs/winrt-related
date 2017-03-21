---
Description: The ExperienceIds element contains a list of one or more individual ExperienceId elements.
Search.Product: eADQiWindows 10XVcnh
title: ExperienceIds
ms.assetid: 83a574da-fcdc-4655-bd37-4d942d8c988b
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, storemanifest
---

# ExperienceIds


The ExperienceIds element contains a list of one or more individual ExperienceId elements.

## Element hierarchy

<dl>
<dt><a href="element-storemanifest.md">&lt;StoreManifest&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-productfeatures.md">&lt;ProductFeatures&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-devicecompanionapplication.md">&lt;DeviceCompanionApplication&gt;</a></dt>
<dd><b>&lt;ExperienceIds&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<ExperienceIds>

  <!-- Child elements -->
  ExperienceId{1,500}

</ExperienceIds>
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
<td>[DeviceCompanionApplication](element-devicecompanionapplication.md)</td>
<td><p>The DeviceCompanionApplication element contains all the configuration required to declare your app as a Windows Store device app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The ExperienceIds element must contain at least one ExperienceId element and a maximum of 500.

## Examples

The following is an example of the ExperienceIds element with three ExperienceId children.

```XML
<ExperienceIds>
    <ExperienceId>aeabdaa8-3bcd-4f03-a7f5-54647fd574c2</ExperienceId>
    <ExperienceId>30292909-c6ba-402e-a41a-7f1ad570c795</ExperienceId>
    <ExperienceId>730f4ea7-c6e3-4778-9662-c7c1a6e826aa</ExperienceId>
</ExperienceIds>
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
<td><p>http://schemas.microsoft.com/appx/2010/StoreManifest</p></td>
</tr>
</tbody>
</table>

 

 



