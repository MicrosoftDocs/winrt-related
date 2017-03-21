---
Description: Specifies text used in the tile template.
Search.Product: eADQiWindows 10XVcnh
title: text
ms.assetid: dac874d1-0a30-4d85-a63d-0ddfa88783d1
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, tiles
---

# text

Specifies text used in the tile template.

## Element hierarchy

<dl>
<dt><a href="element-tile.md">&lt;tile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-visual.md">&lt;visual&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-binding.md">&lt;binding&gt;</a></dt>
<dd><b>&lt;text&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<text id    = integer
      lang? = string />
```

### Key

`?`   optional (zero or one)

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
<td><strong>id</strong></td>
<td><p>The text element in the tile template that this text is intended for. If a template has only one text element, then this value is 1. The number of available text positions is based on the template definition.</p></td>
<td>integer</td>
<td>Yes</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>lang</strong></td>
<td><p>The target locale of the XML payload, specified as a [BCP-47 language tags](http://go.microsoft.com/fwlink/p/?linkid=227302) such as &quot;en-US&quot; or &quot;fr-FR&quot;. The locale specified here overrides any other specified locale, such as that in [<strong>binding</strong>](element-binding.md) or [<strong>visual</strong>](element-visual.md). If this value is a literal string, this attribute defaults to the user's UI language. If this value is a string reference, this attribute defaults to the locale chosen by Windows Runtime in resolving the string.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
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
<td>[binding](element-binding.md)</td>
<td><p>Specifies the tile template. Every notification should include one binding element for each supported tile size.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The body of the text element can be expressed in two ways:

-   As a literal string; for instance, &lt;text id="1"&gt;Hello world!&lt;/text&gt;.
-   As a string reference, using the "ms-resource" prefix; for instance, &lt;text id="1"&gt; ms-resource:hello&lt;/text&gt;. When using the "ms-resource" prefix, the string identifier is referenced in the app's Resources.resjson (Windows app using JavaScript) or Resources.resw file (C#/C++).

For more information, see [Globalizing your tile: localization, scaling, and accessibility](https://msdn.microsoft.com/library/windows/apps/hh831183).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/notifications/2012/tile.xsd</p></td>
</tr>
</tbody>
</table>

 

 



