---
Description: Indicates that the app supports video upgrade
Search.Product: eADQiWindows 10XVcnh
title: uap:VoipCallUpgrade
ms.assetid: e2566775-a4fa-476b-af65-ab252dec514d
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:VoipCallUpgrade


Indicates that the app supports video upgrade. Video upgrade is a feature on some mobile devices such that, when a user is on a cellular call, the user can upgrade that call to a VoIP video call if there is an app installed that can service such a request. These upgrades can be non-seamless (we must drop the cellular call before starting the video call through the app) or seamless (the cellular call remains connected until the app tells us the video call is established).

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
<dt><a href="element-uap-voipcall.md">&lt;uap:VoipCall&gt;</a></dt>
<dd><b>&lt;uap:VoipCallUpgrade&gt;</b></dd>
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
<VoipCallUpgrade SeamlessCallUpgrade? = boolean />
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
<td><strong>SeamlessCallUpgrade</strong></td>
<td><p>Indicates whether or not the app supports a seamless video upgrade.</p></td>
<td>boolean</td>
<td>No</td>
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
<td><a href="element-uap-voipcall.md">uap:VoipCall</a> </td>
<td><p>Declares an app extensibility point of type <strong>voipCall</strong> so that your app can declare that it can perform an upgrade from a cellular call to a VoIP video call, and/or whether it is a VoIP app that supports dialing phone numbers directly.</p></td>
</tr>
</tbody>
</table>

 

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

 

 



