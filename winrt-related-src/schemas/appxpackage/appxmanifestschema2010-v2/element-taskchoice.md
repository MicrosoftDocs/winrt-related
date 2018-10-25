---
Description: The abstract task choice element for the XSD substitution group.
Search.Product: eADQiWindows 10XVcnh
title: TaskChoice
ms.assetid: 349bb88f-fe2c-4d5e-9082-c708a24a0c9b
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# TaskChoice

The abstract task choice element for the XSD substitution group. This can't be declared in the XML.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-backgroundtasks.md">&lt;BackgroundTasks&gt;</a></dt>
<dd><b>&lt;TaskChoice&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TaskChoice>

  xs:anyType

</TaskChoice>
```

## Attributes and Elements


### Attributes

None.

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
<td>[BackgroundTasks](element-backgroundtasks.md)</td>
<td><p>Defines an app extensibility point of type <strong>windows.backgroundTasks</strong>. Background tasks run in a dedicated background host; that is, without a UI.</p></td>
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
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



