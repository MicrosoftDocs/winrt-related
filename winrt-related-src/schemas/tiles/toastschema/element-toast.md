---
description: Base toast element, which contains at least a single visual element.
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
      duration? = "long" | "short" 
      displayTimeStamp? = tbd
      scenario? = "reminder" | "alarm" | "incomingCall" | "urgent" 
      useButtonStyle? = boolean>

  <!-- Child elements -->
  visual,
  audio?,
  commands?
  actions?
  header?
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
<tr class="odd">
<td><strong>displayTimestamp</strong></td>
<td><p>Introduced in Creators Update: Overrides the default timestamp with a custom timestamp representing when your notification content was actually delivered, rather than the time the notification was received by the Windows platform.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>scenario</strong></td>
<td><p>The scenario your toast is used for, like an alarm or reminder. <ul><li>"reminder" - A reminder notification. This will be displayed pre-expanded and stay on the user's screen till dismissed.</li><li>"alarm" - An alarm notification. This will be displayed pre-expanded and stay on the user's screen till dismissed. Audio will loop by default and will use alarm audio.</li><li>"incomingCall" - An incoming call notification. This will be displayed pre-expanded in a special call format and stay on the user's screen till dismissed. Audio will loop by default and will use ringtone audio.</li><li>"urgent" - TBD.</li></ul></li>
</ul></p></td>
<td>string</td>
<td>No</td>
<td>"default" tbd - This is not listed in the email, but is mentioned in https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/toast-schema#toastheader</td>
</tr>
<tr class="odd">
<td><strong>useButtonStyle</strong></td>
<td><p>Specifies whether styled buttons should be used. The styling of the button is determined by the **hint-buttonStyle** attribute of the [action](element-action.md) element.</p></td>
<td>boolean</td>
<td>No</td>
<td>false</td>
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
</tr>
<tr class="even">
<td><a href="element-actions.md">actions</a> </td>
<td><p>Container element for declaring up to five inputs and up to five button actions for the toast notification.</p></td>
</tr>
</tr>
<tr class="odd">
<td><a href="element-header.md">visual</a> </td>
<td><p>Introduced in Creators Update. Specifies a custom header that groups multiple notifications together within Action Center.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## See also

[Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
[Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/notifications/2012/toast.xsd` |

 

 
