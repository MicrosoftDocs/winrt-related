---
title: AppointmentsProvider
description: Declares an app extensibility point of type windows.appointmentsProvider.
Search.Product: eADQiWindows 10XVcnh
ms.assetid: 12e4d422-dbbc-41c0-8511-b87eb343b2cf


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
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
<td><a href="element-appointmentsproviderlaunchactions.md">AppointmentsProviderLaunchActions</a> </td>
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
<td><a href="element-extension.md">Extension</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For info about appointments and the appointments provider, see [**Windows.ApplicationModel.Appointments**](/uwp/api/Windows.ApplicationModel.Appointments) and [**Windows.ApplicationModel.Appointments.AppointmentsProvider**](/uwp/api/Windows.ApplicationModel.Appointments.AppointmentsProvider).

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 
