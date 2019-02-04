---
Description: Contains multiple binding child elements, each of which defines a tile.
Search.Product: eADQiWindows 10XVcnh
title: visual
ms.assetid: f8de9ed6-53d4-4ba5-a4e5-df540c93bd89
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, tiles


ms.topic: reference
ms.date: 04/05/2017
---

# visual




Contains multiple [**binding**](element-binding.md) child elements, each of which defines a tile.

## Element hierarchy

<dl>
<dt><a href="element-tile.md">&lt;tile&gt;</a></dt>
<dd><b>&lt;visual&gt;</b></dd>
</dl>

## Syntax

``` syntax
<visual version?       = integer
        lang?          = string
        baseUri?       = anyURI
        branding?      = "none" | "logo" | "name"
        addImageQuery? = boolean
        contentId?     = string >

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
<td><p>Set to <strong>true</strong> to allow Windows to append a query string to the image URI supplied in the tile notification. Use this attribute if your server hosts images and can handle query strings, either by retrieving an image variant based on the query strings or by ignoring the query string and returning the image as specified without the query string. This query string specifies scale, contrast setting, and language; for instance, a value of</p>
<p>&quot;www.website.com/images/hello.png&quot;</p>
<p>included in the notification becomes</p>
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
<td><p>The form that the tile should use to display the app's brand.</p></td>
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
<td><strong>contentId</strong></td>
<td><p>Set to a sender-defined string that uniquely identifies the content of the notification. This prevents duplicates in the situation where a large tile template is displaying the last three wide tile notifications.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="odd">
<td><strong>lang</strong></td>
<td><p>The target locale of the XML payload, specified as a [BCP-47 language tags](https://go.microsoft.com/fwlink/p/?linkid=227302) such as &quot;en-US&quot; or &quot;fr-FR&quot;. This locale is overridden by any locale specified in [<strong>binding</strong>](element-binding.md) or [<strong>text</strong>](element-text.md). If this value is a literal string, this attribute defaults to the user's UI language. If this value is a string reference, this attribute defaults to the locale chosen by Windows Runtime in resolving the string. See Remarks for when this value isn't specified.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>version</strong></td>
<td><p>The version of the tile XML schema this particular payload was developed for. It can have two values, 1 or 2. Version 1 requires a valid payload under the Windows 8 schema. Version 2 recognizes the new large tile templates, the new Windows 8.1 template names for existing templates, and the <em>fallback</em> attribute of the [<strong>binding</strong>](element-binding.md) element.</p></td>
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
<td>[binding](element-binding.md)</td>
<td><p>Specifies the tile template. Every notification should include one binding element for each supported tile size.</p></td>
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
<td>[tile](element-tile.md)</td>
<td><p>Base tile element, which contains a single [<strong>visual</strong>](https://msdn.microsoft.com/library/windows/apps/br230847) element.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The following table explains how the system responds when lang is not specified.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>For...</th>
<th>The system response</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The language for the notification</td>
<td><ul>
<li>If set explicitly, use visual.lang or binding.lang</li>
<li>Else the app specific language setting (the language, if any, that the [Resource Management System](https://msdn.microsoft.com/library/windows/apps/jj552947) determines the app will run in given the current language profile)</li>
<li>Else the language of the display name on the tile as resolved by Windows Runtime</li>
<li>Else the Shell's UI language (MUI language)</li>
</ul>
<p>This language primarily influences the layout of columns in templates that feature columns.</p></td>
</tr>
<tr class="even">
<td>Text elements with literal text</td>
<td><ul>
<li>If set explicitly, use visual.lang or binding.lang</li>
<li>Else the app specific language setting (the language, if any, that the [Resource Management System](https://msdn.microsoft.com/library/windows/apps/jj552947) determines the app will run in given the current language profile)</li>
<li>Else the language of the display name on the tile as resolved by Windows Runtime</li>
<li>Else the shell's UI language (MUI language)</li>
</ul></td>
</tr>
<tr class="odd">
<td>Text elements with ms-resource content</td>
<td><ul>
<li>If set explicitly, use visual.lang or binding.lang, and the explicit language is prepended to the language list the Resource Management System's [ResourceContext](https://msdn.microsoft.com/library/windows/apps/jj552947#resourcecontext) used to resolve the string</li>
<li>Else the [ResourceContext](https://msdn.microsoft.com/library/windows/apps/jj552947#resourcecontext) used as initialized with the user's language profile</li>
</ul>
<p>After the string is resolved, the language for the resolved string is assigned to the text element. This language shapes the text alignment (LTR vs. RTL) and font selection for UI.</p></td>
</tr>
<tr class="even">
<td>ms-appx:/// image</td>
<td><ul>
<li>If set explicitly, use visual.lang or binding.lang, the explicit language is prepended to the language list the Resource Management System's [ResourceContext](https://msdn.microsoft.com/library/windows/apps/jj552947#resourcecontext) used to resolve the string</li>
<li>Else the [ResourceContext](https://msdn.microsoft.com/library/windows/apps/jj552947#resourcecontext) us used as initialized with the user's language profile</li>
</ul></td>
</tr>
<tr class="odd">
<td>Cloud images</td>
<td><ul>
<li>If set explicitly, use visual.lang or binding.lang</li>
<li>Else the app-specific language setting (the language, if any, that the [Resource Management System](https://msdn.microsoft.com/library/windows/apps/jj552947) determines the app will run in given the current language profile)</li>
<li>Else the language of the display name on the tile as resolved by Windows Runtime (might not be set if the name is language-neutral)</li>
<li>Else the Shell's UI language (MUI language)</li>
</ul>
<p>This language is included in the query string if addImageQuery is true.</p></td>
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
<td><p>http://schemas.microsoft.com/notifications/2012/tile.xsd</p></td>
</tr>
</tbody>
</table>

 

 



