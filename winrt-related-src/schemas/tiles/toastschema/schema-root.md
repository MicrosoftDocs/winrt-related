---
Description: Toast schema
MS-HAID: toast.Schema\_Root
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Toast schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, toast notifications
---

# Toast schema


These elements are used to define a toast notification, and specify the template, images, audio, and text that compose the toast content, branding specifics, and language information.

These elements and their attributes are manipulated through Document Object Model (DOM) manipulation functions to customize the toast content.

To define the content for a toast, you can use [**ToastNotificationManager.getTemplateContent**](https://msdn.microsoft.com/library/windows/apps/br208646) to get a toast template that can be modified.

To examine the content of an existing toast, use [**ToastNotification.content**](https://msdn.microsoft.com/library/windows/apps/br208648) to get the current contents.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[audio](element-audio.md)</td>
<td><p>Specifies a sound to play when a toast notification is displayed. This element also allows you to mute any toast notification audio.</p></td>
</tr>
<tr class="even">
<td>[binding](element-binding.md)</td>
<td><p>Specifies the toast template. Note that only one binding element can be included in a toast notification.</p></td>
</tr>
<tr class="odd">
<td>[command](element-command.md)</td>
<td><p>Specifies a scenario-associated button shown in a toast. The scenario is specified in the parent [<strong>commands</strong>](element-commands.md) element.</p></td>
</tr>
<tr class="even">
<td>[commands](element-commands.md)</td>
<td><p>Specifies that the toast notification is being used to indicate an incoming call or an alarm, with appropriate commands associated with each scenario.</p></td>
</tr>
<tr class="odd">
<td>[image](element-image.md)</td>
<td><p>Specifies an image used in the toast template.</p></td>
</tr>
<tr class="even">
<td>[text](element-text.md)</td>
<td><p>Specifies text used in the toast template.</p></td>
</tr>
<tr class="odd">
<td>[toast](element-toast.md)</td>
<td><p>Base toast element, which contains at least a single [<strong>visual</strong>](element-visual.md) element.</p></td>
</tr>
<tr class="even">
<td>[visual](element-visual.md)</td>
<td><p>Contains a single [<strong>binding</strong>](https://msdn.microsoft.com/library/windows/apps/br212854) element that defines a toast.</p></td>
</tr>
</tbody>
</table>

 

 

 



