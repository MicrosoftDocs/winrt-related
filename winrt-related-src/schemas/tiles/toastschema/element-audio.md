---
Description: Specifies a sound to play when a toast notification is displayed.
Search.Product: eADQiWindows 10XVcnh
title: audio
ms.assetid: 13e5fe05-383b-4615-81ce-20d8b020350f
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, toast notifications
---

# audio


Specifies a sound to play when a toast notification is displayed. This element also allows you to mute any toast notification audio.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd><b>&lt;audio&gt;</b></dd>
</dl>

## Syntax

``` syntax
<audio src?    = string
       loop?   = boolean
       silent? = boolean />
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
<td><strong>loop</strong></td>
<td><p>Set to <strong>true</strong> if the sound should repeat as long as the toast is shown; <strong>false</strong> to play only once. If this attribute is set to <strong>true</strong>, the <em>duration</em> attribute in the [<strong>toast</strong>](element-toast.md) element must also be set. There are specific sounds provided to be used when looping. Note that UWP apps support neither looping audio nor long-duration toasts.</p></td>
<td>boolean</td>
<td>No</td>
<td>false</td>
</tr>
<tr class="even">
<td><strong>silent</strong></td>
<td><p><strong>True</strong> to mute the sound; <strong>false</strong> to allow the toast notification sound to play.</p></td>
<td>boolean</td>
<td>No</td>
<td>false</td>
</tr>
<tr class="odd">
<td><strong>src</strong></td>
<td><p>The media file to play in place of the default sound. On Windows, this attribute can have one of the following string values:</p>
<ul>
<li>ms-winsoundevent:Notification.Default</li>
<li>ms-winsoundevent:Notification.IM</li>
<li>ms-winsoundevent:Notification.Mail</li>
<li>ms-winsoundevent:Notification.Reminder</li>
<li>ms-winsoundevent:Notification.SMS</li>
<li>ms-winsoundevent:Notification.Looping.Alarm</li>
<li>ms-winsoundevent:Notification.Looping.Alarm2</li>
<li>ms-winsoundevent:Notification.Looping.Alarm3</li>
<li>ms-winsoundevent:Notification.Looping.Alarm4</li>
<li>ms-winsoundevent:Notification.Looping.Alarm5</li>
<li>ms-winsoundevent:Notification.Looping.Alarm6</li>
<li>ms-winsoundevent:Notification.Looping.Alarm7</li>
<li>ms-winsoundevent:Notification.Looping.Alarm8</li>
<li>ms-winsoundevent:Notification.Looping.Alarm9</li>
<li>ms-winsoundevent:Notification.Looping.Alarm10</li>
<li>ms-winsoundevent:Notification.Looping.Call</li>
<li>ms-winsoundevent:Notification.Looping.Call2</li>
<li>ms-winsoundevent:Notification.Looping.Call3</li>
<li>ms-winsoundevent:Notification.Looping.Call4</li>
<li>ms-winsoundevent:Notification.Looping.Call5</li>
<li>ms-winsoundevent:Notification.Looping.Call6</li>
<li>ms-winsoundevent:Notification.Looping.Call7</li>
<li>ms-winsoundevent:Notification.Looping.Call8</li>
<li>ms-winsoundevent:Notification.Looping.Call9</li>
<li>ms-winsoundevent:Notification.Looping.Call10</li>
</ul>
<p>On Windows Phone 8.1, this attribute can also contain the path to a local audio file, with one of the following prefixes:</p>
<ul>
<li>ms-appx:///</li>
<li>ms-appdata:///</li>
</ul></td>
<td>string</td>
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
<td>[toast](element-toast.md)</td>
<td><p>Base toast element, which contains at least a single [<strong>visual</strong>](element-visual.md) element.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

UWP apps that target the desktop platform don't currently support custom sounds; instead, you can choose from the list of winsoundevents.

If you specify a custom file path in the app payload, the default sound (notification, call, alarm, or reminder) will be played based on the specified scenario.

## Examples

The following code shows an example of this tag.

```XML
<audio src="ms-winsoundevent:Notification.Mail" loop="false"/>
                
```

The following code shows this tag used to mute toast notification audio.

```XML
<audio silent="true"/>
                
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/notifications/2012/toast.xsd</p></td>
</tr>
</tbody>
</table>

 

 



