---
Description: Defines an attribute of the class that is stored in the Windows Runtime property store.
title: uap5:ActivatableClassAttribute 
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 10/10/2017
---

# uap5:ActivatableClassAttribute 

Defines an attribute of the class that is stored in the Windows Runtime property store.

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
<dt><a href="element-uap5-extension.md">&lt;uap5:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-outofprocessserver.md">&lt;uap5:OutOfProcessServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-activatableclass.md">&lt;uap5:ActivatableClass&gt;</a></dt>
<dd><b>&lt;uap5:ActivatableClassAttribute&gt;</b></dd>
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
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | The attribute name. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | Yes |
| Type | The attribute type. | "string" | "integer" | Yes |
| Value | The attribute value. | A string between 1 and 255 characters in length. | Yes |

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
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/5</p></td>
</tr>
</tbody>
</table>

 

 



