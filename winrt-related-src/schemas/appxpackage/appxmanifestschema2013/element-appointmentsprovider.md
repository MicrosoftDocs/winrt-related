---
Description: Declares an app extensibility point of type windows.appointmentsProvider.
Search.Product: eADQiWindows 10XVcnh
title: AppointmentsProvider
ms.assetid: 12e4d422-dbbc-41c0-8511-b87eb343b2cf
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# AppointmentsProvider




Declares an app extensibility point of type **windows.appointmentsProvider**.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;AppointmentsProvider&gt;</b></dd>
</dl>

## Syntax

``` syntax
<AppointmentsProvider>

  <!-- Child elements -->
  AppointmentsProviderLaunchActions?

</AppointmentsProvider>
```

### Key

`?`   optional (zero or one)

## Attributes and Elements


### Attributes

None.

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
<td>[AppointmentsProviderLaunchActions](element-appointmentsproviderlaunchactions.md)</td>
<td><p>Declares actions to take when a appointment is launched.</p></td>
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
<td>[Extension](element-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For info about appointments and the appointments provider, see [**Windows.ApplicationModel.Appointments**](https://msdn.microsoft.com/library/windows/apps/dn263359) and [**Windows.ApplicationModel.Appointments.AppointmentsProvider**](https://msdn.microsoft.com/library/windows/apps/dn297284).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2013/manifest</p></td>
</tr>
</tbody>
</table>

 

 



