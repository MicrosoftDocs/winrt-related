---
Description: Describes an uap:AppointmentsProviderLaunchActions content action.
Search.Product: eADQiWindows 10XVcnh
title: uap:LaunchAction (in AppointmentsProviderLaunchActions)
ms.assetid: 1058a98d-10a0-4ce2-8b10-84d5c8fb9da6
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:LaunchAction (in AppointmentsProviderLaunchActions)


Describes an [**uap:AppointmentsProviderLaunchActions**](element-uap-appointmentsproviderlaunchactions.md) content action.

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
<dd>
<dl>
<dt><a href="element-uap-appointmentsprovider.md">&lt;uap:AppointmentsProvider&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-appointmentsproviderlaunchactions.md">&lt;uap:AppointmentsProviderLaunchActions&gt;</a></dt>
<dd><b>&lt;uap:LaunchAction&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
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
<LaunchAction Verb           = "addAppointment" | "removeAppointment" | "replaceAppointment" | "showTimeFrame" | "showAppointmentDetails"
                  DesiredView?   = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum"
                  Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
                  EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type.
If EntryPoint is not specified, the EntryPoint defined for the app is used instead.

                  RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
                  StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
                  ResourceGroup? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. />
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
<td><strong>DesiredView</strong></td>
<td><p>The desired amount of screen space to use when the appointment launches.</p></td>
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
<tr class="even">
<td><strong>EntryPoint</strong></td>
<td><p>The activatable class ID.</p></td>
<td>A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Executable</strong></td>
<td><p>The default launch executable.</p></td>
<td>A string between 1 and 256 characters in length that must end with &quot;.exe&quot; and cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ResourceGroup</strong></td>
<td><p>A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [<strong>Application@ResourceGroup</strong>](element-application.md) and Remarks.</p></td>
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>RuntimeType</strong></td>
<td><p>The runtime provider. This attribute is used typically when there are mixed frameworks in an app.</p></td>
<td>A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, &quot;, /, \, |, ?, or *.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>StartPage</strong></td>
<td><p>The web page that handles the extensibility point.</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Verb</strong></td>
<td><p>A unique identifier that is passed to the app when it is launched. The app can use this string to determine which [<strong>uap:AppointmentsProviderLaunchActions</strong>](element-uap-appointmentsproviderlaunchactions.md) handler triggered its launch. It is unique per application in the package and is case sensitive.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>addAppointment</li>
<li>removeAppointment</li>
<li>replaceAppointment</li>
<li>showTimeFrame</li>
<li>showAppointmentDetails</li>
</ul></td>
<td>Yes</td>
<td></td>
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
<td>[uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md)</td>
<td><p>Declares actions to take when a appointment is launched.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[uap:LaunchAction (in type: CT_AutoPlayContent)](element-uap-launchaction.md)**
-   **[uap:LaunchAction (in type: CT_AutoPlayDevice)](element-1-uap-launchaction.md)**

## Remarks

For more info about launch actions that an appointments provider takes, see [**AppointmentsProviderLaunchActionVerbs**](https://msdn.microsoft.com/library/windows/apps/dn297211).

**LaunchAction (in AppointmentsProviderLaunchActions)** has these semantic validations:

-   [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270) base attributes must follow these rules:

    -   If the **StartPage** attribute is specified, fail if the **EntryPoint**, **Executable**, or **RuntimeType** attribute is specified.
    -   Otherwise, fail if the **Executable** or **RuntimeType** attribute is specified without an **EntryPoint** specified.

-   If **LaunchAction (in AppointmentsProviderLaunchActions)** defines the **EntryPoint** attribute, either this **LaunchAction (in AppointmentsProviderLaunchActions)** or the parent [**uap:Extension**](element-uap-extension.md) or [**Application**](element-application.md) element must specify an **Executable** attribute.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10</p></td>
</tr>
</tbody>
</table>

 

 



