---

title: uap5:ActivatableClass
description: Declares a runtime class associated with the extensibility point.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:ActivatableClass

## Description
Declares a runtime class associated with the extensibility point.

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
<dt><a href="element-uap5-outofprocessserver.md">&lt;uap5:OutOfProcessServer&gt;</a></dt>
<dd><b>&lt;uap5:ActivatableClass&gt;</b></dd>
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
<uap5:ActivatableClass  ActivatableClassId = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *. >

  <!-- Child elements -->
  ActivatableClassAttribute{0,1000}

</uap5:ActivatableClass>
```


## Attrbutes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ActivatableClassId | The identifier of the runtime class in the operating system. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, &quot;, /, &#92;, &#124;, ?, or *. | Yes |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [ActivatableClassAttribute](element-uap5-ActivatableClassAttribute.md) | Defines an attribute of the class that is stored in the Windows Runtime property store. |

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