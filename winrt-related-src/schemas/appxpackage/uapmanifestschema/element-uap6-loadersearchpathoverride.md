---
Description: An extension that allows an app developer to declare a path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes.
title: uap6:LoaderSearchPathOverride


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/10/2018
---

# uap6:LoaderSearchPathOverride
An extension that allows an app developer to declare a path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;uap6:LoaderSearchPathOverride&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<uap6:LoaderSearchPathOverride>

  <!-- Child elements -->
  LoaderSearchPathEntry{0,5}

</uap6:LoaderSearchPathOverride>
```

### Key
`{}`   specific range of occurrences

## Attributes and Elements

### Attributes
None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [uap6:LoaderSearchPathEntry](element-uap6-loadersearchpathentry.md) | A relative path used specify where to load content from an app package. |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/6</p></td>
</tr>
</tbody>
</table>

 

 



