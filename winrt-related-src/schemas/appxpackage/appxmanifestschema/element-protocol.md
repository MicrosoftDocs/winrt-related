---
Description: Protocol
Search.Product: eADQiWindows 10XVcnh
title: Protocol
ms.assetid: ac911c85-02eb-408c-8c4b-24a4e172df8b
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# Protocol


Declares an app extensibility point of type **windows.protocol**. A URI association indicates that the app is registered to handle URIs with the specified scheme.

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
<dt><a href="element-1-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;Protocol&gt;</b></dd>
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
<Protocol Name = A string between 3 and 39 characters in length that contains numbers, lowercased letters, or a hyphen ('-'). >

  <!-- Child elements -->
  ( Logo?
  & DisplayName?
  )

</Protocol>
```

### Key

`?`   optional (zero or one)

`&`   interleave connector (may occur in any order)

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
<td><strong>Name</strong></td>
<td><p>The name of the URI scheme, such as &quot;mailto&quot;. This name must be unique for the package.</p></td>
<td>A string between 3 and 39 characters in length that contains numbers, lowercased letters, or a hyphen ('-').</td>
<td>Yes</td>
<td></td>
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
<td>[DisplayName](element-2-displayname.md)</td>
<td><p>A friendly name that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td>[Logo](element-2-logo.md)</td>
<td><p>A path to a file that contains an image.</p></td>
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
<td>[Extension (in type: CT_ApplicationExtensions)](element-1-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```XML
<Applications>
  <Application Id="App" StartPage="default.html">
    <Extensions>
      <Extension Category="windows.protocol">
        <Protocol Name="alsdk" />
      </Extension>
    </Extensions>
  </Application>
</Applications>
```

## See also


**Tasks**
[How to handle URI activation](https://msdn.microsoft.com/library/windows/apps/hh452686)

**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



