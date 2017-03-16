---
Description: Capability (Windows 10)
MS-HAID: UapManifestSchema.element\_Capability
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Capability (Windows 10)
ms.assetid: ee6bf220-f139-4ad9-a7a7-e621c189b907
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
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
<td>[Capabilities](element-capabilities.md)</td>
<td><p>Declares the access to protected user resources that the package requires.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The [App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936) topic describes the capability values.

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


[App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936)

[Guidelines for app settings](https://msdn.microsoft.com/library/windows/apps/hh770544)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>

 

 



