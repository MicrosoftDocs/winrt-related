---

title: uap5:InputType
description: Specifies media input sub-types.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:InputType

## Description
Specifies media input sub-types.

## Element Hierarchy
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
<dt><a href="element-uap5-VideoRendererEffect.md">&lt;uap5:VideoRendererEffect&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-InputTypes.md">&lt;uap5:InputTypes&gt;</a></dt>
<dd><b>&lt;uap5:InputType&gt;</b></dd>
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
```syntax
<uap5:InputType SubType = Either a GUID or a 4 character alphanumeric code. Cannot contain whitespace.
                MkvCodecId = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. />
```

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| SubType | A custom or existing media subtype. | Either a GUID or a 4 character alphanumeric code. Cannot contain whitespace. | Yes |
| MkvCodecId | A string representing a valid MKV codec ID. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |

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