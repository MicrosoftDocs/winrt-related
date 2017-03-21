---
Description: Declares actions to take when a appointment is launched.
Search.Product: eADQiWindows 10XVcnh
title: AppointmentsProviderLaunchActions
ms.assetid: 5e9b44b6-94b5-4cab-91ff-df8ae15c0978
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# AppointmentsProviderLaunchActions




Declares actions to take when a appointment is launched.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-appointmentsprovider.md">&lt;AppointmentsProvider&gt;</a></dt>
<dd><b>&lt;AppointmentsProviderLaunchActions&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<AppointmentsProviderLaunchActions DesiredView? = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum" >

  <!-- Child elements -->
  LaunchAction{0,10}

</AppointmentsProviderLaunchActions>
```

### Key

`?`   optional (zero or one)
`{}`   specific range of occurrences
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
<td><strong>DesiredView</strong></td>
<td><p>The desired amount of screen space to use when the appointment launches.</p>
<p><strong>Windows Phone:  DesiredView</strong> isn't supported for Windows Phone.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>default</li>
<li>useLess</li>
<li>useHalf</li>
<li>useMore</li>
<li>useMinimum</li>
</ul></td>
<td>No</td>
<td></td>
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
<td>[LaunchAction (in AppointmentsProviderLaunchActions)](element-1-launchaction.md)</td>
<td><p>Describes an [<strong>AppointmentsProviderLaunchActions</strong>](element-appointmentsproviderlaunchactions.md) content action.</p></td>
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
<td>[AppointmentsProvider](element-appointmentsprovider.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.appointmentsProvider</strong>.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For more info, see [**ViewSizePreference**](https://msdn.microsoft.com/library/windows/apps/dn281132) and [**DesiredRemainingView**](https://msdn.microsoft.com/library/windows/apps/dn298314).

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

 

 



