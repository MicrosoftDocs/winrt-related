---
Description: ActivatableClassAttribute (Windows 10)
MS-HAID: UapManifestSchema.element\_1\_ActivatableClassAttribute
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: ActivatableClassAttribute (Windows 10)
ms.assetid: 74ca4fd4-1a67-4e1f-b933-89b2ffa2fa17
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# ActivatableClassAttribute (Windows 10)


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
<dt><a href="element-inprocessserver.md">&lt;InProcessServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-activatableclass.md">&lt;ActivatableClass&gt;</a></dt>
<dd><b>&lt;ActivatableClassAttribute&gt;</b></dd>
</dl>
</dd>
</dl>
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
<ActivatableClassAttribute Name  = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
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
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
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
<td>[ActivatableClass (type: CT_InProcessActivatableClass)](element-activatableclass.md)</td>
<td><p>Declares a runtime class associated with the extensibility point.</p></td>
</tr>
<tr class="even">
<td>[ActivatableClass (type: CT_OutOfProcessActivatableClass)](element-1-activatableclass.md)</td>
<td><p>Declares a runtime class associated with the extensibility point.</p></td>
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

 

 



