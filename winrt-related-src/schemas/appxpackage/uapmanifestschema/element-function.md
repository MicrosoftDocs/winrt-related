---
Description: Declares the function for the device.
Search.Product: eADQiWindows 10XVcnh
title: Function (Windows 10)
ms.assetid: d53133f1-6017-4c20-bbff-f2370c5fc39d


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Function (Windows 10)


Declares the function for the device.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-devicecapability.md">&lt;DeviceCapability&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-device.md">&lt;Device&gt;</a></dt>
<dd><b>&lt;Function&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Function Type = A string between 1 and 100 characters in length. Where appropriate, the string may begin with "classId:" | "winUsbId:" | "serviceId:" | "serviceId:" | "usage:" | "interfaceId:". />
```

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
<td><strong>Type</strong></td>
<td><p>The type of function for the device.</p></td>
<td>A string between 1 and 100 characters in length. Where appropriate, the string may begin with &quot;classId:&quot; | &quot;winUsbId:&quot; | &quot;serviceId:&quot; | &quot;serviceId:&quot; | &quot;usage:&quot; | &quot;interfaceId:&quot;.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

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
<td><a href="element-device.md">Device</a> </td>
<td><p>Declares a function for a device that is associated with the <a href="element-devicecapability.md"><strong>DeviceCapability</strong></a> . On Windows 10.0.10240.0, a <strong>DeviceCapability</strong> can contain up to 100 <strong>Device</strong> elements. On Windows 10.0.10586.0, it can contain up to 1000 (for more details, see <strong>DeviceCapability</strong>).</p></td>
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

 

 



