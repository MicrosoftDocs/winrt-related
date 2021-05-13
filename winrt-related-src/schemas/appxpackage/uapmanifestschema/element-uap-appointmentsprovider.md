---
description: Declares an app extensibility point of type windows.appointmentsProvider.
Search.Product: eADQiWindows 10XVcnh
title: uap:AppointmentsProvider (Windows 10)
ms.assetid: 017359a9-e1c5-4b47-8598-bc8c49a67e4a


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:AppointmentsProvider (Windows 10)


Declares an app extensibility point of type **windows.appointmentsProvider**.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd><b>&lt;uap:AppointmentsProvider&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<AppointmentsProvider>

  <!-- Child elements -->
  uap:AppointmentsProviderLaunchActions?

</uap:AppointmentsProvider>
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
<td><a href="element-uap-appointmentsproviderlaunchactions.md">uap:AppointmentsProviderLaunchActions</a> </td>
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
<td><a href="element-uap-extension.md">uap:Extension</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For info about appointments and the appointments provider, see [**Windows.ApplicationModel.Appointments**](/uwp/api/Windows.ApplicationModel.Appointments) and [**Windows.ApplicationModel.Appointments.AppointmentsProvider**](/uwp/api/Windows.ApplicationModel.Appointments.AppointmentsProvider).

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 
