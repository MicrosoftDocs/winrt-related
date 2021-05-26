---
title: LaunchAction (in AppointmentsProviderLaunchActions)
description: Describes an AppointmentsProviderLaunchActions content action.
Search.Product: eADQiWindows 10XVcnh
ms.assetid: 074c2f73-dcdd-4660-9d70-5bcee7b63199


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# LaunchAction (in AppointmentsProviderLaunchActions)




Describes an [**AppointmentsProviderLaunchActions**](element-appointmentsproviderlaunchactions.md) content action.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-appointmentsprovider.md">&lt;AppointmentsProvider&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-appointmentsproviderlaunchactions.md">&lt;AppointmentsProviderLaunchActions&gt;</a></dt>
<dd><b>&lt;LaunchAction&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<LaunchAction Verb         = "addAppointment" | "removeAppointment" | "replaceAppointment" | "showTimeFrame"
              DesiredView? = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum" />
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
<tr class="even">
<td><strong>Verb</strong></td>
<td><p>A unique identifier that is passed to the app when it is launched. The app can use this string to determine which <a href="element-appointmentsproviderlaunchactions.md"><strong>AppointmentsProviderLaunchActions</strong></a>  handler triggered its launch. It is unique per application in the package and is case sensitive.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>addAppointment</li>
<li>removeAppointment</li>
<li>replaceAppointment</li>
<li>showTimeFrame</li>
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
<td><a href="element-appointmentsproviderlaunchactions.md">AppointmentsProviderLaunchActions</a> </td>
<td><p>Declares actions to take when a appointment is launched.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[LaunchAction (in ContactLaunchActions)](element-launchaction.md)**

## Remarks

For more info about launch actions that an appointments provider takes, see [**AppointmentsProviderLaunchActionVerbs**](/uwp/api/Windows.ApplicationModel.Appointments.AppointmentsProvider.AppointmentsProviderLaunchActionVerbs).

The **LaunchAction (in AppointmentsProviderLaunchActions)** definition has these statements:

``` syntax
            <xs:element name="LaunchAction" minOccurs="0" maxOccurs="10">
              <xs:complexType>
                <xs:attribute name="Verb" type="ST_AppointmentsProviderLaunchActionVerbs" use="required"/>
                <xs:attribute name="DesiredView" type="ST_DesiredView" use="optional"/>
                <xs:attributeGroup ref="m:ExtensionBaseAttributes"/>
              </xs:complexType>
            </xs:element>
```

The preceding 'ref' statement indicates that **LaunchAction (in AppointmentsProviderLaunchActions)** inherits and all of these [**Extension**](../appxmanifestschema2010-v2/element-extension.md) base attributes:

``` syntax
  <xs:attributeGroup name="ExtensionBaseAttributes">
    <xs:attribute name="Executable" type="ST_Executable" use="optional"/>
    <xs:attribute name="EntryPoint" type="ST_EntryPoint" use="optional"/>
    <xs:attribute name="RuntimeType" type="ST_ActivatableClassId" use="optional"/>
    <xs:attribute name="StartPage" type="ST_FileName" use="optional"/>
  </xs:attributeGroup>
```

Because **LaunchAction (in AppointmentsProviderLaunchActions)** allows the [**Extension**](../appxmanifestschema2010-v2/element-extension.md) base attributes, it has these semantic validations that aren't covered by the XSD manifest schema:

-   [**Extension**](../appxmanifestschema2010-v2/element-extension.md) base attributes must follow these rules:

    -   If the **StartPage** attribute is specified, fail if the **EntryPoint**, **Executable**, or **RuntimeType** attribute is specified.
    -   Otherwise, fail if the **Executable** or **RuntimeType** attribute is specified without an **EntryPoint** specified.

-   If **LaunchAction** defines the **EntryPoint** attribute, either this **LaunchAction** or the parent [**Extension**](../appxmanifestschema2010-v2/element-extension.md) or [**Application**](../appxmanifestschema2010-v2/element-application.md) element must specify an **Executable** attribute.

## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 
