---
Description: The background task associated with the app extensibility point.
Search.Product: eADQiWindows 10XVcnh
title: Task (Windows 10)
ms.assetid: 4662ec1d-c245-4c60-b966-e27d5ce0699d


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Task (Windows 10)


The background task associated with the app extensibility point.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-backgroundtasks.md">&lt;BackgroundTasks&gt;</a></dt>
<dd><b>&lt;Task&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Task Type = "general" | "audio" | "controlChannel" | "systemEvent" | "timer" | ... />
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
<li>general</li>
<li>audio</li>
<li>controlChannel</li>
<li>systemEvent</li>
<li>timer</li>
<li>pushNotification</li>
<li>location</li>
<li>deviceUse</li>
<li>deviceServicing</li>
<li>deviceConnectionChange</li>
<li>bluetooth</li>
</ul></td>
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
<td><a href="element-backgroundtasks.md">BackgroundTasks</a> </td>
<td><p>Defines an app extensibility point of type <strong>windows.backgroundTasks</strong>. Background tasks run in a dedicated background host; that is, without a UI.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |


 

 



