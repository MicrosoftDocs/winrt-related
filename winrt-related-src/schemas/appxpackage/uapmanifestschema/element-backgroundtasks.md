---
Description: Defines an app extensibility point of type windows.backgroundTasks.
Search.Product: eADQiWindows 10XVcnh
title: BackgroundTasks (Windows 10)
ms.assetid: 0e9cbbc5-3852-4158-87e7-12ea87be62e7


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# BackgroundTasks (Windows 10)


Defines an app extensibility point of type **windows.backgroundTasks**. Background tasks run in a dedicated background host; that is, without a UI.

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
<dd><b>&lt;BackgroundTasks&gt;</b></dd>
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
<BackgroundTasks ServerName? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. 
                 uap4:SupportsMultipleInstances = Boolean. >

  <!-- Child elements -->
  Task{1,17},
  uap:Task{1,17}

</BackgroundTasks>
```

### Key

`?`   optional (zero or one)
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
<td><strong>ServerName</strong></td>
<td><p>The server name. Ensures that only one instance of the server exists at runtime.</p></td>
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap4:SupportsMultipleInstances</strong></td>
<td><p>Supports multiple, separate instances of background tasks.</p></td>
<td>Boolean.</td>
<td>No</td>
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
<td><a href="element-task.md">Task</a> </td>
<td><p>The background task associated with the app extensibility point.</p></td>
</tr>
<tr class="even">
<td><a href="element-uap-task.md">uap:Task</a> </td>
<td><p>The background task associated with the app extensibility point.</p></td>
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
<td><a href="element-1-extension.md">Extension (global)</a> </td>
<td><p>Declares an extensibility point for the package.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Extensions of type "windows.backgroundTask" must specify either a StartPage or EntryPoint attribute in the Extension element. For more info (and an example) see [Declare background tasks in the application manifest](https://docs.microsoft.com/windows/uwp/launch-resume/declare-background-tasks-in-the-application-manifest).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10</p></td>
</tr>
</tbody>
</table>

 

 



