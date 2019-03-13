---
Description: Specifies the tile template.
Search.Product: eADQiWindows 10XVcnh
title: binding
ms.assetid: c88c9e7a-d929-4d1b-95e4-65df88cf9844
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, tiles


ms.topic: reference
ms.date: 04/05/2017
---

# binding




Specifies the tile template. Every notification should include one binding element for each supported tile size.

## Element hierarchy

<dl>
<dt><a href="element-tile.md">&lt;tile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-visual.md">&lt;visual&gt;</a></dt>
<dd><b>&lt;binding&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<binding template       = tileTemplateNameV2
         fallback?      = tileTemplateNameV1
         lang?          = string
         baseUri?       = anyURI
         branding?      = "none" | "logo" | "name"
         addImageQuery? = boolean
         contentId?     = string >

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
<td>logo</td>
</tr>
<tr class="even">
<td><strong>contentId</strong></td>
<td><p>Set to a sender-defined string that uniquely identifies the content of the notification. This prevents duplicates in the situation where a large tile template is displaying the last three wide tile notifications.</p></td>
<td>string</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>fallback</strong></td>
<td><p>A template to use if the primary template name is not recognized by the recipient, for use with Windows 8 compatibility. This value is the Windows 8 name of the value in the <em>template</em> attribute. New templates introduced after Windows 8 do not have a fallback.</p></td>
<td>tileTemplateNameV1 (see Remarks)</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>lang</strong></td>
<td><p>The target locale of the XML payload, specified as a <a href="https://go.microsoft.com/fwlink/p/?linkid=227302">BCP-47 language tags</a>  such as &quot;en-US&quot; or &quot;fr-FR&quot;. The locale specified here overrides that in [<strong>visual</strong>](element-visual.md), but can be overriden by that in [<strong>text</strong>](element-text.md). If this value is a literal string, this attribute defaults to the user's UI language. If this value is a string reference, this attribute defaults to the locale chosen by Windows Runtime in resolving the string. See Remarks for when this value isn't specified.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="odd">
<td><strong>template</strong></td>
<td><p>One of the provided templates on which to base the tile. Typically, a developer should supply both a square and a wide format, each as a separate <a href="element-binding.md"><strong>binding</strong></a>  element. Valid entries are members of the [<strong>tileTemplateType</strong>](https://msdn.microsoft.com/library/windows/apps/br208621) enumeration.</p></td>
<td>tileTemplateNameV2 (see Remarks)</td>
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
<td><p>Specifies an image used in the tile template. The supplied image should match the size and shape requirements for the specific template or image within that template.</p></td>
</tr>
<tr class="even">
<td><a href="element-text.md">text</a> </td>
<td><p>Specifies text used in the tile template.</p></td>
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
<td><p>Contains multiple <a href="element-binding.md"><strong>binding</strong></a>  child elements, each of which defines a tile.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **tileTemplateNameV2** value used in the *template* attribute can be one of the following string values. For details on each template, see [The tile template catalog](https://msdn.microsoft.com/library/windows/apps/hh761491).

-   TileSquare150x150Block
-   TileSquare150x150Image
-   TileSquare150x150PeekImageAndText01
-   TileSquare150x150PeekImageAndText02
-   TileSquare150x150PeekImageAndText03
-   TileSquare150x150PeekImageAndText04
-   TileSquare150x150Text01
-   TileSquare150x150Text02
-   TileSquare150x150Text03
-   TileSquare150x150Text04
-   TileSquare310x310BlockAndText01
-   TileSquare310x310BlockAndText02
-   TileSquare310x310Image
-   TileSquare310x310ImageAndText01
-   TileSquare310x310ImageAndText02
-   TileSquare310x310ImageAndTextOverlay01
-   TileSquare310x310ImageAndTextOverlay02
-   TileSquare310x310ImageAndTextOverlay03
-   TileSquare310x310ImageCollection
-   TileSquare310x310ImageCollectionAndText01
-   TileSquare310x310ImageCollectionAndText02
-   TileSquare310x310SmallImagesAndTextList01
-   TileSquare310x310SmallImagesAndTextList02
-   TileSquare310x310SmallImagesAndTextList03
-   TileSquare310x310SmallImagesAndTextList04
-   TileSquare310x310Text01
-   TileSquare310x310Text02
-   TileSquare310x310Text03
-   TileSquare310x310Text04
-   TileSquare310x310Text05
-   TileSquare310x310Text06
-   TileSquare310x310Text07
-   TileSquare310x310Text08
-   TileSquare310x310TextList01
-   TileSquare310x310TextList02
-   TileSquare310x310TextList03
-   TileWide310x150BlockAndText01
-   TileWide310x150BlockAndText02
-   TileWide310x150Image
-   TileWide310x150ImageAndText01
-   TileWide310x150ImageAndText02
-   TileWide310x150ImageCollection
-   TileWide310x150PeekImage01
-   TileWide310x150PeekImage02
-   TileWide310x150PeekImage03
-   TileWide310x150PeekImage04
-   TileWide310x150PeekImage05
-   TileWide310x150PeekImage06
-   TileWide310x150PeekImageAndText01
-   TileWide310x150PeekImageAndText02
-   TileWide310x150PeekImageCollection01
-   TileWide310x150PeekImageCollection02
-   TileWide310x150PeekImageCollection03
-   TileWide310x150PeekImageCollection04
-   TileWide310x150PeekImageCollection05
-   TileWide310x150PeekImageCollection06
-   TileWide310x150SmallImageAndText01
-   TileWide310x150SmallImageAndText02
-   TileWide310x150SmallImageAndText03
-   TileWide310x150SmallImageAndText04
-   TileWide310x150SmallImageAndText05
-   TileWide310x150Text01
-   TileWide310x150Text02
-   TileWide310x150Text03
-   TileWide310x150Text04
-   TileWide310x150Text05
-   TileWide310x150Text06
-   TileWide310x150Text07
-   TileWide310x150Text08
-   TileWide310x150Text09
-   TileWide310x150Text10
-   TileWide310x150Text11

The **tileTemplateNameV1** value used in the *fallback* attribute can be one of the following string values. These are the Windows 8 template names. For details on each template, see [The tile template catalog](https://msdn.microsoft.com/library/windows/apps/hh761491).

-   TileSquareBlock
-   TileSquareImage
-   TileSquarePeekImageAndText01
-   TileSquarePeekImageAndText02
-   TileSquarePeekImageAndText03
-   TileSquarePeekImageAndText04
-   TileSquareText01
-   TileSquareText02
-   TileSquareText03
-   TileSquareText04
-   TileWideBlockAndText01
-   TileWideBlockAndText02
-   TileWideImage
-   TileWideImageAndText01
-   TileWideImageAndText02
-   TileWideImageCollection
-   TileWidePeekImage01
-   TileWidePeekImage02
-   TileWidePeekImage03
-   TileWidePeekImage04
-   TileWidePeekImage05
-   TileWidePeekImage06
-   TileWidePeekImageAndText01
-   TileWidePeekImageAndText02
-   TileWidePeekImageCollection01
-   TileWidePeekImageCollection02
-   TileWidePeekImageCollection03
-   TileWidePeekImageCollection04
-   TileWidePeekImageCollection05
-   TileWidePeekImageCollection06
-   TileWideSmallImageAndText01
-   TileWideSmallImageAndText02
-   TileWideSmallImageAndText03
-   TileWideSmallImageAndText04
-   TileWideSmallImageAndText05
-   TileWideText01
-   TileWideText02
-   TileWideText03
-   TileWideText04
-   TileWideText05
-   TileWideText06
-   TileWideText07
-   TileWideText08
-   TileWideText09
-   TileWideText10
-   TileWideText11

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

 

 



