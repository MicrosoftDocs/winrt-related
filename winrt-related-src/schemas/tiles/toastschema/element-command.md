---
description: Specifies a scenario-associated button shown in a toast.
Search.Product: eADQiWindows 10XVcnh
title: command
ms.assetid: dc3cf502-fdf8-42ab-96b6-f0fb4e84e08c

keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 04/05/2017
---

# command




Specifies a scenario-associated button shown in a toast. The scenario is specified in the parent [**commands**](element-commands.md) element.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-commands.md">&lt;commands&gt;</a></dt>
<dd><b>&lt;command&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<command id?        = "snooze" | "dismiss" | "video" | "voice" | "decline"
         arguments? = string />
```

### Key

`?`   optional (zero or one)

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
<td><strong>arguments</strong></td>
<td><p>An argument string that can be passed to the associated app to provide specifics about the action that it should execute in response to the user action.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>id</strong></td>
<td><p>Specifies one command from the system-defined command list. These values correspond to available actions that the user can take. Two scenarios are available through the <a href="element-commands.md"><strong>commands</strong></a>  element. Only certain commands are used with a given scenario, as shown here:</p>
<ul>
<li><strong>alarm</strong>
<ul>
<li>snooze</li>
<li>dismiss</li>
</ul></li>
<li><strong>incomingCall</strong>
<ul>
<li>video</li>
<li>voice</li>
<li>decline</li>
</ul></li>
</ul></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>snooze</li>
<li>dismiss</li>
<li>video</li>
<li>voice</li>
<li>decline</li>
</ul></td>
<td>No</td>
<td>None</td>
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
<td><a href="element-commands.md">commands</a> </td>
<td><p>Specifies that the toast notification is being used to indicate an incoming call or an alarm, with appropriate commands associated with each scenario.</p></td>
</tr>
</tbody>
</table>

 

## See also


[Alarm notifications sample](/samples/browse/)

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/notifications/2012/toast.xsd` |

 

 
