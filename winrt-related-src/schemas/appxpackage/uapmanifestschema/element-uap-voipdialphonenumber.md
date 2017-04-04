---
Description: Indicates that the app supports dialing phone numbers.
Search.Product: eADQiWindows 10XVcnh
title: uap:VoipDialPhoneNumber
ms.assetid: 89161194-e351-4dee-a5b8-07aa4a429d0b
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# uap:VoipDialPhoneNumber


Indicates that the app supports dialing phone numbers.

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
<dd><b>&lt;uap:VoipDialPhoneNumber&gt;</b></dd>
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
<VoipDialPhoneNumber>

  xs:anyType

</uap:VoipDialPhoneNumber>
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
<td>[uap:VoipCall](element-uap-voipcall.md)</td>
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

 

 



