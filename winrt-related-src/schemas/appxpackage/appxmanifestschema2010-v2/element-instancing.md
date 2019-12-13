---
Description: Specifies whether the executable runs as a single instance or can run as multiple instances.
Search.Product: eADQiWindows 10XVcnh
title: Instancing
ms.assetid: 26533f27-2470-4083-91a0-4e4b03f8479a


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Instancing




Specifies whether the executable runs as a single instance or can run as multiple instances.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-outofprocessserver.md">&lt;OutOfProcessServer&gt;</a></dt>
<dd><b>&lt;Instancing&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
## Syntax

``` syntax
<Instancing>

  "singleInstance" | "multipleInstances"

</Instancing>
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
<td><a href="element-outofprocessserver.md">OutOfProcessServer</a> </td>
<td><p>Declares a package extension point of type <strong>windows.activatableClass.outOfProcessServer</strong>. The app uses an executable (EXE) that exposes one or more activatable classes.</p></td>
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
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



