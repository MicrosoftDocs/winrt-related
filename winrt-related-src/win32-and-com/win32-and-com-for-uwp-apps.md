---
author: msatranjr
description: A Universal Windows Platform (UWP) app (or a Windows Runtime component) written in C++/CX has access to the Win32 and COM APIs that are part of the Universal Windows Platform (UWP).
title: Win32 and COM APIs for UWP apps
ms.author: misatran
ms.topic: article


keywords: windows 10, uwp, win32, COM
ms.date: 04/05/2017
ms.assetid: BB6F6100-85F3-4B35-A2AB-FA677671AADA
---

# Win32 and COM APIs for UWP apps
A Universal Windows Platform (UWP) app (or a [Windows Runtime component](https://docs.microsoft.com/en-us/windows/uwp/winrt-components/)) written in C++/CX has access to the Win32 and COM APIs that are part of the Universal Windows Platform (UWP).

Most of these APIs are implemented by all Windows 10 devices, and that set is listed first (in two forms: grouped by module, and listed in alphabetical order of name). Then, additional APIs that are part of the UWP but that are not present on all Windows 10 devices, are listed.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[APIs present on all Windows 10 devices](win32-apis.md)</p></td>
<td><p>This topic lists the Win32 APIs that are part of the UWP and that are implemented by all Windows 10 devices. For convenience, an umbrella library named WindowsApp.lib is provided in the Microsoft Windows Software Development Kit (SDK), which provides the exports for this set of Win32 APIs. Link your app with WindowsApp.lib (and no other libraries) to access these APIs.</p></td>
</tr>
<tr class="even">
<td><p>[Extension APIs for Windows 10 devices](win32-extension-apis.md)</p></td>
<td><p>This topic lists the Win32 and COM APIs that are part of the UWP and that are implemented by some Windows 10 devices, so your calls to these APIs must be guarded with conditions that first confirm the presence of the API on the device your app is running on. The union of [APIs present on all Windows 10 devices](win32-apis.md) and the APIs listed in this topic make up the entire Win32 and COM surface area of UWP.</p></td>
</tr>
<tr class="odd">
<td><p>[Alternatives to Windows APIs in Windows 10 UWP apps](alternatives-to-windows-apis-uwp.md)</p></td>
<td><p>Learn which features of the Windows API can be used in a UWP app and which APIs to use as alternatives for those that cannot.</p></td>
</tr>
</tbody>
</table>

 

 

 



