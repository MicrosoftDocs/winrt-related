---
description: The background task associated with the app extensibility point (extensions schema for Windows 8.1).
Search.Product: eADQiWindows 10XVcnh
title: Task (Windows 8.1 extensions schema)
ms.assetid: 4662ec1d-c245-4c60-b966-e27d5ce0699d


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Task (extensions schema for Windows 8.1)

The background task associated with the app extensibility point.

## Element hierarchy

**&lt;Task&gt;**

## Syntax

``` syntax
<Task Type = "audio" | "controlChannel" | "systemEvent" | "timer" | "pushNotification" />
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
<td><p>The task type.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>audio</li>
<li>controlChannel</li>
<li>systemEvent</li>
<li>timer</li>
<li>pushNotification</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|               |        Value                                                     |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



