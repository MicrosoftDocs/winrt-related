---
description: Declares actions to take when a contact is launched.
Search.Product: eADQiWindows 10XVcnh
title: ContactLaunchActions
ms.assetid: da094c1d-bd52-492f-81a6-23676802c15f


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# ContactLaunchActions




Declares actions to take when a contact is launched.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-contact.md">&lt;Contact&gt;</a></dt>
<dd><b>&lt;ContactLaunchActions&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<ContactLaunchActions DesiredView? = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum" >

  <!-- Child elements -->
  LaunchAction{1,50}

</ContactLaunchActions>
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
<td><p>The desired amount of screen space to use when the contact launches.</p>
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
<td><a href="element-launchaction.md">LaunchAction (in ContactLaunchActions)</a> </td>
<td><p>Describes a <a href="element-contactlaunchactions.md"><strong>ContactLaunchActions</strong></a>  content action.</p></td>
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
<td><a href="element-contact.md">Contact</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.contact</strong>.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For more info, see [**ViewSizePreference**](/uwp/api/Windows.UI.ViewManagement.ViewSizePreference) and [**DesiredRemainingView**](/uwp/api/Windows.System.LauncherOptions).

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 
