---
Description: Specifies the toast template.
Search.Product: eADQiWindows 10XVcnh
title: binding
ms.assetid: c88c9e7a-d929-4d1b-95e4-65df88cf9844

keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 04/05/2017
---

# binding




Specifies the toast template. Note that only one binding element can be included in a toast notification.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-visual.md">&lt;visual&gt;</a></dt>
<dd><b>&lt;binding&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<binding template       = "ToastImageAndText01" | "ToastImageAndText02" | "ToastImageAndText03" | ...
         fallback?      = string
         lang?          = string
         addImageQuery? = boolean
         baseUri?       = anyURI
         branding?      = string >

  <!-- Child elements -->
  ( image
  | text
  )*

</binding>
```

### Key

`?`   optional (zero or one)
`*`   optional (zero or more)

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
<td><strong>fallback</strong></td>
<td><p>A template to use if the primary template cannot be found, for use with backward compatibility.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="odd">
<td><strong>lang</strong></td>
<td><p>The target locale of the XML payload, specified as a <a href="https://go.microsoft.com/fwlink/p/?linkid=227302">BCP-47 language tags</a>  such as &quot;en-US&quot; or &quot;fr-FR&quot;. The locale specified here overrides that in <a href="element-visual.md"><strong>visual</strong></a>, but can be overriden by that in <a href="element-text.md"><strong>text</strong></a>. If this value is a literal string, this attribute defaults to the user's UI language. If this value is a string reference, this attribute defaults to the locale chosen by Windows Runtime in resolving the string.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>template</strong></td>
<td><p>One of the provided templates on which to base the toast. Values are given in the <a href="https://msdn.microsoft.com/library/windows/apps/br208660"><strong>toastTemplateType</strong></a>  enumeration.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>ToastImageAndText01</li>
<li>ToastImageAndText02</li>
<li>ToastImageAndText03</li>
<li>ToastImageAndText04</li>
<li>ToastText01</li>
<li>ToastText02</li>
<li>ToastText03</li>
<li>ToastText04</li>
</ul></td>
<td>Yes</td>
<td>None</td>
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
<td><a href="element-image.md">image</a> </td>
<td><p>Specifies an image used in the toast template.</p></td>
</tr>
<tr class="even">
<td><a href="element-text.md">text</a> </td>
<td><p>Specifies text used in the toast template.</p></td>
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
<td><a href="element-visual.md">visual</a> </td>
<td><p>Contains a single <a href="https://msdn.microsoft.com/library/windows/apps/br212854"><strong>binding</strong></a>  element that defines a toast.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

To see examples of each of the toast templates, see the [toast template catalog](https://msdn.microsoft.com/library/windows/apps/hh761494).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/notifications/2012/toast.xsd</p></td>
</tr>
</tbody>
</table>

 

 



