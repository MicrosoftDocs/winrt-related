---
Description: Indicates whether...
title: rescap6:ModificationPackage


keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/19/2019
ms.custom: 19H1
---

# rescap6:ModificationPackage
Declares that the current package is a [modification package](https://docs.microsoft.com/windows/msix/modification-packages) for an enterprise application.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;rescap6:ModificationPackage&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` xml
<rescap6:ModificationPackage>true</rescap6:ModificationPackage>
```

## Attributes and Elements

### Attributes

None.

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |  

## Remarks

This element represents a restricted property that is only supported in [optional packages](https://docs.microsoft.com/windows/uwp/packaging/optional-packages). This element is currently intended to be used only for enterprise applications. We don't recommend that you declare this capability in applications that you submit to the Microsoft Store. In most cases, the use of this element won't be approved.

For more information, see [Modification packages](https://docs.microsoft.com/windows/msix/modification-packages).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/6</p></td>
</tr>
</tbody>
</table>

 

 



