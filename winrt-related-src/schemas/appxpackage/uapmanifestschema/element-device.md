---
Description: Declares a function for a device that is associated with the DeviceCapability.
Search.Product: eADQiWindows 10XVcnh
title: Device (Windows 10)
ms.assetid: 1e9e699f-bbd9-4d15-95ea-207ec495c46e
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Device (Windows 10)


Declares a function for a device that is associated with the [**DeviceCapability**](element-devicecapability.md). On Windows 10.0.10240.0, a **DeviceCapability** can contain up to 100 **Device** elements. On Windows 10.0.10586.0, it can contain up to 1000 (for more details, see **DeviceCapability**).

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-devicecapability.md">&lt;DeviceCapability&gt;</a></dt>
<dd><b>&lt;Device&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Device Id = A string between 1 and 512 characters in length. >

  <!-- Child elements -->
  Function{1,100}

</Device>
```

### Key

`{}`   specific range of occurrences
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
<td><strong>Id</strong></td>
<td><p>The identifier of the device.</p></td>
<td>A string between 1 and 512 characters in length.</td>
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
<td><a href="element-function.md">Function</a> </td>
<td><p>Declares the function for the device.</p></td>
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
<td><a href="element-devicecapability.md">DeviceCapability</a> </td>
<td><p>Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 <a href="element-device.md"><strong>Device</strong></a>  elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples).</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>

 

 



