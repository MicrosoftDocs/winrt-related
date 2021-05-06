---
description: Contains a single binding element that defines a toast.
Search.Product: eADQiWindows 10XVcnh
title: visual (Toast schema)
ms.assetid: f8de9ed6-53d4-4ba5-a4e5-df540c93bd89

keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 04/05/2017
---

# visual (Toast schema)




Contains a single [**binding**](../tilesschema/element-binding.md) element that defines a toast.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd><b>&lt;visual&gt;</b></dd>
</dl>

## Syntax

``` syntax
<visual version?       = integer
        lang?          = string
        baseUri?       = anyURI
        branding?      = "none" | "logo" | "name"
        addImageQuery? = boolean >

  <!-- Child elements -->
  binding+

</visual>
```

### Key

`?`   optional (zero or one)
`+`   required (one or more)

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
<td><strong>addImageQuery</strong></td>
<td><p>Set to &quot;true&quot; to allow Windows to append a query string to the image URI supplied in the toast notification. Use this attribute if your server hosts images and can handle query strings, either by retrieving an image variant based on the query strings or by ignoring the query string and returning the image as specified without the query string. This query string specifies scale, contrast setting, and language; for instance, a value of</p>
<p>&quot;www.website.com/images/hello.png&quot;</p>
<p>given in the notification becomes</p>
<p>&quot;www.website.com/images/hello.png?ms-scale=100&amp;ms-contrast=standard&amp;ms-lang=en-us&quot;</p></td>
<td>boolean</td>
<td>No</td>
<td>false</td>
</tr>
<tr class="even">
<td><strong>baseUri</strong></td>
<td><p>A default base URI that is combined with relative URIs in image source attributes.</p></td>
<td>anyURI</td>
<td>No</td>
<td>ms-appx:///</td>
</tr>
<tr class="odd">
<td><strong>branding</strong></td>
<td><p>Not used.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>none</li>
<li>logo</li>
<li>name</li>
</ul></td>
<td>No</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>lang</strong></td>
<td><p>The target locale of the XML payload, specified as <a href="https://go.microsoft.com/fwlink/p/?linkid=227302">BCP-47 language tags</a>  such as &quot;en-US&quot; or &quot;fr-FR&quot;. This locale is overridden by any locale specified in <a href="element-binding.md"><strong>binding</strong></a> or <a href="element-text.md"><strong>text</strong></a>. If this value is a literal string, this attribute defaults to the user's UI language. If this value is a string reference, this attribute defaults to the locale chosen by Windows Runtime in resolving the string.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="odd">
<td><strong>version</strong></td>
<td><p>The version of the toast XML schema this particular payload was developed for.</p></td>
<td>integer</td>
<td>No</td>
<td>1</td>
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
<td><a href="element-binding.md">binding</a> </td>
<td><p>Specifies the toast template. Note that only one binding element can be included in a toast notification.</p></td>
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
<td><a href="element-toast.md">toast</a> </td>
<td><p>Base toast element, which contains at least a single <a href="element-visual.md"><strong>visual</strong></a>  element.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/notifications/2012/toast.xsd` |

 

 
