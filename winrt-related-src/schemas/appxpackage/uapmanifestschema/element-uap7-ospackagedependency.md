---
Description: OS package dependency information.
title: uap7:OSPackageDependency
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest, driver dependency
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 10/03/18
---

# uap7:OSPackageDependency
Defines a package dependency for a UWP app.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;uap7:OSPackageDependency&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<uap7:OSPackageDependency Name    = An alphanumeric string. May contain period and dash characters.
                          Version =  A version string in quad notation, "Major.Minor.Build.Revision". />
```

## Attributes and Elements
### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name      | The name of the package dependency. | An alphanumeric string. May contain period and dash characters. | Yes |
| Version   | The version of the package dependency. | A version string in quad notation, "Major.Minor.Build.Revision". | Yes |

### Child Elements
None


## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/7</p></td>
</tr>
</tbody>
</table>