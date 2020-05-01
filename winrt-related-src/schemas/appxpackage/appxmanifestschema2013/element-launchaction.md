---
Description: Describes a ContactLaunchActions content action.
Search.Product: eADQiWindows 10XVcnh
title: LaunchAction (in ContactLaunchActions)
ms.assetid: 3561ba0c-690c-4c09-b383-b2c1e95f26d6


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# LaunchAction (in ContactLaunchActions)

Describes a [**ContactLaunchActions**](element-contactlaunchactions.md) content action.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-contact.md">&lt;Contact&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-contactlaunchactions.md">&lt;ContactLaunchActions&gt;</a></dt>
<dd><b>&lt;LaunchAction&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<LaunchAction Verb         = "call" | "map" | "message" | "post" | "videoCall"
              DesiredView? = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum" >

  <!-- Child elements -->
  ServiceId{0,100}

</LaunchAction>
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
<tr class="even">
<td><strong>Verb</strong></td>
<td><p>A unique identifier that is passed to the app when it is launched. The app can use this string to determine which <a href="element-contactlaunchactions.md"><strong>ContactLaunchActions</strong></a>  handler triggered its launch. It is unique per application in the package and is case sensitive.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>call</li>
<li>map</li>
<li>message</li>
<li>post</li>
<li>videoCall</li>
</ul></td>
<td>Yes</td>
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
<td><a href="element-serviceid.md">ServiceId</a> </td>
<td><p>Identifies the service for a contact action.</p></td>
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
<td><a href="element-contactlaunchactions.md">ContactLaunchActions</a> </td>
<td><p>Declares actions to take when a contact is launched.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[LaunchAction (in AppointmentsProviderLaunchActions)](element-1-launchaction.md)**

## Remarks

For more info about launch actions that a contacts provider takes, see [**ContactLaunchActionVerbs**](https://msdn.microsoft.com/library/windows/apps/dn263363).

The manifest enforces these semantic checks for the **Verb** attribute for a [**ContactLaunchActions**](element-contactlaunchactions.md) content action.

-   If **Verb** is set to **map**, it must not declare any [**ServiceId**](element-serviceid.md) elements. All other values for **Verb** must declare a **ServiceId**.
-   Only if **Verb** is set to **call** or **message**, can it specify [**ServiceId**](element-serviceid.md) as the well-known value 'telephone.'

The **LaunchAction (in ContactLaunchActions)** definition has these statements:

``` syntax
            <xs:element name="LaunchAction" maxOccurs="50">
              <xs:complexType>
                <xs:sequence>
                  <xs:element name="ServiceId" type="CT_ServiceId" minOccurs="0" maxOccurs="100"/>
                </xs:sequence>
                <xs:attribute name="Verb" type="ST_ContactLaunchActionVerbs" use="required"/>
                <xs:attribute name="DesiredView" type="ST_DesiredView" use="optional"/>
                <xs:attributeGroup ref="m:ExtensionBaseAttributes"/>
              </xs:complexType>
              <xs:unique name="Service_Id">
                <xs:selector xpath="m2:ServiceId"/>
                <xs:field xpath="."/>
              </xs:unique>
            </xs:element>
```

The preceding 'ref' statement indicates that **LaunchAction (in ContactLaunchActions)** inherits all of these [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270) base attributes:

``` syntax
  <xs:attributeGroup name="ExtensionBaseAttributes">
    <xs:attribute name="Executable" type="ST_Executable" use="optional"/>
    <xs:attribute name="EntryPoint" type="ST_EntryPoint" use="optional"/>
    <xs:attribute name="RuntimeType" type="ST_ActivatableClassId" use="optional"/>
    <xs:attribute name="StartPage" type="ST_FileName" use="optional"/>
  </xs:attributeGroup>
```

Because **LaunchAction (in ContactLaunchActions)** allows the [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270) base attributes, it has these semantic validations that aren't covered by the XSD manifest schema:

-   [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270) base attributes must follow these rules:

    -   If the **StartPage** attribute is specified, fail if the **EntryPoint**, **Executable**, or **RuntimeType** attribute is specified.
    -   Otherwise, fail if the **Executable** or **RuntimeType** attribute is specified without an **EntryPoint** specified.

-   If **LaunchAction** defines the **EntryPoint** attribute, either this **LaunchAction** or the parent [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270) or [**Application**](https://msdn.microsoft.com/library/windows/apps/dn423250) element must specify an **Executable** attribute.

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 



