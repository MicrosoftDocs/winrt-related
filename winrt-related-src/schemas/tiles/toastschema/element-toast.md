---
Description: Base toast element, which contains at least a single visual element.
Search.Product: eADQiWindows 10XVcnh
title: toast
ms.assetid: 78359fce-826c-4c1c-9afb-9651ac34cdfa

keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 04/05/2017
---

# toast




Base toast element, which contains at least a single [**visual**](element-visual.md) element.

## Element hierarchy

**&lt;toast&gt;**

## Syntax

``` syntax
<toast launch?   = string
       duration? = "long" | "short" >

  <!-- Child elements -->
  visual,
  audio?,
  commands?

</toast>
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
<td><strong>duration</strong></td>
<td><p>The amount of time the toast should display.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>long</li>
<li>short</li>
</ul></td>
<td>No</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>launch</strong></td>
<td><p>A string that is passed to the application when it is activated by the toast. The format and contents of this string are defined by the app for its own use. When the user taps or clicks the toast to launch its associated app, the launch string provides the context to the app that allows it to show the user a view relevant to the toast content, rather than launching in its default way.</p></td>
<td>string</td>
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
<td><a href="element-audio.md">audio</a> </td>
<td><p>Specifies a sound to play when a toast notification is displayed. This element also allows you to mute any toast notification audio.</p></td>
</tr>
<tr class="even">
<td><a href="element-commands.md">commands</a> </td>
<td><p>Specifies that the toast notification is being used to indicate an incoming call or an alarm, with appropriate commands associated with each scenario.</p></td>
</tr>
<tr class="odd">
<td><a href="element-visual.md">visual</a> </td>
<td><p>Contains a single <a href="/uwp/schemas/tiles/tilesschema/element-binding"><strong>binding</strong></a>  element that defines a toast.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/notifications/2012/toast.xsd` |

 

 