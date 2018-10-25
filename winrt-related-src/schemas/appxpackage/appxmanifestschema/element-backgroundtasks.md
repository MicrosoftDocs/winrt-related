---
Description: Defines an app extensibility point of type windows.backgroundTasks.
Search.Product: eADQiWindows 10XVcnh
title: BackgroundTasks
ms.assetid: 0e9cbbc5-3852-4158-87e7-12ea87be62e7
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# BackgroundTasks


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
<BackgroundTasks ServerName? = A string between 1 and 255 characters in length. >

  <!-- Child elements -->
  Task{1,5}

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
<td>A string between 1 and 255 characters in length.</td>
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
<td>[Task](element-task.md)</td>
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
<td>[Extension (in type: CT_ApplicationExtensions)](element-1-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Extensions of type "windows.backgroundTask" must specify either a StartPage or EntryPoint attribute in the Extension element. For more info (and an example) see [**How to declare background tasks in the application manifest (JavaScript and HTML)**](https://msdn.microsoft.com/library/windows/apps/hh977042) or [**How to declare background tasks in the application manifest (C#/VB/C++ and XAML)**](https://msdn.microsoft.com/library/windows/apps/xaml/hh977049).

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

 

 



