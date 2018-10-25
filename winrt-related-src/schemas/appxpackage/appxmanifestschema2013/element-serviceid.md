---
Description: Identifies the service for a contact action.
Search.Product: eADQiWindows 10XVcnh
title: ServiceId
ms.assetid: 1ddf4438-cfe4-4be1-9ca3-f734d7729d92
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# ServiceId




Identifies the service for a contact action.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-contact.md">&lt;Contact&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-contactlaunchactions.md">&lt;ContactLaunchActions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-launchaction.md">&lt;LaunchAction&gt;</a></dt>
<dd><b>&lt;ServiceId&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<ServiceId>

  Identifies the service for a contact.

</ServiceId>
```

## Attributes and Elements


### Attributes

None.

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
<td>[LaunchAction (in ContactLaunchActions)](element-launchaction.md)</td>
<td><p>Describes a [<strong>ContactLaunchActions</strong>](element-contactlaunchactions.md) content action.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **ServiceId** definition has these statements:

``` syntax
  <xs:complexType name="CT_ServiceId" mixed="true">
    <xs:simpleContent>
      <xs:extension base="ST_ServiceId">
        <xs:attributeGroup ref="m:ExtensionBaseAttributes"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
```

The preceding 'ref' statement indicates that **ServiceId** inherits all of these [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270) base attributes:

``` syntax
  <xs:attributeGroup name="ExtensionBaseAttributes">
    <xs:attribute name="Executable" type="ST_Executable" use="optional"/>
    <xs:attribute name="EntryPoint" type="ST_EntryPoint" use="optional"/>
    <xs:attribute name="RuntimeType" type="ST_ActivatableClassId" use="optional"/>
    <xs:attribute name="StartPage" type="ST_FileName" use="optional"/>
  </xs:attributeGroup>
```

Because **ServiceId** allows the [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270) base attributes, it has these semantic validations that aren't covered by the XSD manifest schema:

-   [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270) base attributes must follow these rules:

    -   If the **StartPage** attribute is specified, fail if the **EntryPoint**, **Executable**, or **RuntimeType** attribute is specified.
    -   Otherwise, fail if the **Executable** or **RuntimeType** attribute is specified without an **EntryPoint** specified.

-   If **ServiceId** defines the **EntryPoint** attribute, either this **ServiceId** or the parent [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270) or [**Application**](https://msdn.microsoft.com/library/windows/apps/dn423250) element must specify an **Executable** attribute.

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

 

 



