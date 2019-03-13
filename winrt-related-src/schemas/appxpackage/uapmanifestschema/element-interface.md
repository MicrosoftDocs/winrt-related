---
Description: Declares an interface associated with the proxy.
Search.Product: eADQiWindows 10XVcnh
title: Interface (Windows 10)
ms.assetid: 5b5c6b0c-a9d1-4e0c-a71c-40744a12c4e7
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Interface (Windows 10)


Declares an interface associated with the proxy.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-proxystub.md">&lt;ProxyStub&gt;</a></dt>
<dd><b>&lt;Interface&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Interface Name        = A string between 1 and 255 characters in length that consists of alpha-numeric, period, and underscore characters.
           InterfaceId = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. />
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
<td><strong>InterfaceId</strong></td>
<td><p>The interface ID.</p></td>
<td>A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td><p>The name of the interface.</p></td>
<td>A string between 1 and 255 characters in length that consists of alpha-numeric, period, and underscore characters.</td>
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
<td><a href="element-proxystub.md">ProxyStub</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.proxyStub</strong>. A proxy can be composed of one or more interfaces.</p></td>
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
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>

 

 



