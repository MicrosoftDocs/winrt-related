---
Description: Task
MS-HAID: AppxManifestSchema2013.element\_Task
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Task
ms.assetid: 4662ec1d-c245-4c60-b966-e27d5ce0699d
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# Task

The background task associated with the app extensibility point.

## Element hierarchy

**&lt;Task&gt;**

## Syntax

``` syntax
<Task Type = "location" | "deviceUse" | "deviceServicing" />
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
<li>location</li>
<li>deviceUse</li>
<li>deviceServicing</li>
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

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2013/manifest</p></td>
</tr>
</tbody>
</table>

 

 



