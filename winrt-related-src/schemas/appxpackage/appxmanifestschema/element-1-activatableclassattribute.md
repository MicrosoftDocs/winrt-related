---
description: Defines an attribute of the class that is stored in the Windows Runtime property store.
Search.Product: eADQiWindows 10XVcnh
title: ActivatableClassAttribute (Windows 8, descendant of OutOfProcessServer)
ms.assetid: 74ca4fd4-1a67-4e1f-b933-89b2ffa2fa17


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# ActivatableClassAttribute (Windows 8, descendant of OutOfProcessServer)


Defines an attribute of the class that is stored in the Windows Runtime property store.

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
<dt><a href="element-outofprocessserver.md">&lt;OutOfProcessServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-activatableclass.md">&lt;ActivatableClass&gt;</a></dt>
<dd><b>&lt;ActivatableClassAttribute&gt;</b></dd>
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
<ActivatableClassAttribute Name  = A string between 1 and 255 characters in length that consists of alpha-numeric fields separated by periods. Each field must begin with an ASCII alphabetical character.
                           Type  = "string" | "integer"
                           Value = A string between 1 and 255 characters in length. />
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
<td><p>The attribute name.</p></td>
<td>A string between 1 and 255 characters in length that consists of alpha-numeric fields separated by periods. Each field must begin with an ASCII alphabetical character.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Type</strong></td>
<td><p>The attribute type.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>string</li>
<li>integer</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Value</strong></td>
<td><p>The attribute value.</p></td>
<td>A string between 1 and 255 characters in length.</td>
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
<td><a href="element-activatableclass.md">ActivatableClass (type: CT_InProcessActivatableClass)</a> </td>
<td><p>Declares a runtime class associated with the extensibility point.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-activatableclass.md">ActivatableClass (type: CT_OutOfProcessActivatableClass)</a> </td>
<td><p>Declares a runtime class associated with the extensibility point.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



