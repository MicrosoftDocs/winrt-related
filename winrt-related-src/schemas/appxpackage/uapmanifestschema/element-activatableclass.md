---
description: Declares a runtime class associated with the extensibility point.
Search.Product: eADQiWindows 10XVcnh
title: ActivatableClass (in InProcessServer) (Windows 10)
ms.assetid: c75a7a4d-1864-4bff-95e6-67cd007ee192


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# ActivatableClass (in InProcessServer) (Windows 10)


Declares a runtime class associated with the extensibility point.

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
<dt><a href="element-inprocessserver.md">&lt;InProcessServer&gt;</a></dt>
<dd><b>&lt;ActivatableClass&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<ActivatableClass ActivatableClassId = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
                  ThreadingModel     = "both" | "STA" | "MTA" >

  <!-- Child elements -->
  ActivatableClassAttribute{0,1000}

</ActivatableClass>
```

### Key

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
<td><strong>ActivatableClassId</strong></td>
<td><p>The identifier of the runtime class in the operating system.</p></td>
<td>A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, &quot;, /, \, |, ?, or *.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ThreadingModel</strong></td>
<td><p>The type of threading model supported by the runtime class.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>both</li>
<li>STA</li>
<li>MTA</li>
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
<td><a href="element-activatableclassattribute.md">ActivatableClassAttribute</a> </td>
<td><p>Defines an attribute of the class that is stored in the Windows Runtime property store.</p></td>
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
<td><a href="element-inprocessserver.md">InProcessServer</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.inProcessServer</strong>. The app uses a dynamic link library (DLL) that exposes one or more activatable classes.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[ActivatableClass (type: CT_OutOfProcessActivatableClass)](element-1-activatableclass.md)**

## Requirements

|   | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |


 

 



