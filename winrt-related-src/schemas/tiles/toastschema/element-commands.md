---
description: Specifies that the toast notification is being used to indicate an incoming call or an alarm, with appropriate commands associated with each scenario.
Search.Product: eADQiWindows 10XVcnh
title: commands
ms.assetid: 34e5b696-bc5c-40d1-abe0-42b10a0a6611

keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 04/05/2017
---

# commands




Specifies that the toast notification is being used to indicate an incoming call or an alarm, with appropriate commands associated with each scenario.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd><b>&lt;commands&gt;</b></dd>
</dl>

## Syntax

``` syntax
<commands scenario? = "alarm" | "incomingCall" >

  <!-- Child elements -->
  command*

</commands>
```

### Key

`?`   optional (zero or one)
`*`   optional (zero or more)

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
<td><strong>scenario</strong></td>
<td><p>The intended use of the notification.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>alarm</li>
<li>incomingCall</li>
</ul></td>
<td>No</td>
<td>None</td>
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
<td><a href="element-command.md">command</a> </td>
<td><p>Specifies a scenario-associated button shown in a toast. The scenario is specified in the parent <a href="element-commands.md"><strong>commands</strong></a>  element.</p></td>
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
<td><a href="element-toast.md">toast</a> </td>
<td><p>Base toast element, which contains at least a single <a href="element-visual.md"><strong>visual</strong></a>  element.</p></td>
</tr>
</tbody>
</table>

 

## See also

* [Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
* [Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)



 

 
