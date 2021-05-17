---
description: Declares a capability required by a package.
Search.Product: eADQiWindows 10XVcnh
title: Capability (Windows 10)
ms.assetid: ee6bf220-f139-4ad9-a7a7-e621c189b907


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Capability (Windows 10)


Declares a capability required by a package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd><b>&lt;Capability&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Capability Name = "internetClient" | "internetClientServer" | "privateNetworkClientServer" | "allJoyn" | "codeGeneration" />
```

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
<td><strong>Name</strong></td>
<td><p>The name of the capability.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>internetClient</li>
<li>internetClientServer</li>
<li>privateNetworkClientServer</li>
<li>allJoyn</li>
<li>codeGeneration</li>
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
<td><a href="element-capabilities.md">Capabilities</a> </td>
<td><p>Declares the access to protected user resources that the package requires.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The [App capability declarations](/previous-versions/windows/apps/hh464936(v=win.10)) topic describes the capability values.

## Examples

Here's an example of a [**Capabilities**](element-capabilities.md) node.

```XML
<Capabilities>
    <Capability Name="internetClient"/>
    <Capability Name="internetClientServer"/>
    <Capability Name="privateNetworkClientServer"/>
    <Capability Name="allJoyn"/>
    <uap:Capability Name="documentsLibrary"/>
    <uap:Capability Name="picturesLibrary"/>
    <uap:Capability Name="videosLibrary"/>
    <uap:Capability Name="musicLibrary"/>
    <uap:Capability Name="enterpriseAuthentication"/>
    <uap:Capability Name="sharedUserCertificates"/>
    <uap:Capability Name="userAccountInformation"/>
    <uap:Capability Name="removableStorage"/>
    <uap:Capability Name="appointments"/>
    <uap:Capability Name="contacts"/>
    <uap:Capability Name="phoneCall"/>
    <uap:Capability Name="blockedChatMessages"/>
    <uap:Capability Name="objects3D"/>
</Capabilities>
```

## See also


[App capability declarations](/previous-versions/windows/apps/hh464936(v=win.10))

[Guidelines for app settings](/windows/uwp/design/app-settings/guidelines-for-app-settings)

## Requirements

|   |  Value |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |


 

 
