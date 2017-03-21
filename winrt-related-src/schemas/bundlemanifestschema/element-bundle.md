---
Description: Defines the root element of a bundle manifest.
Search.Product: eADQiWindows 10XVcnh
title: Bundle
ms.assetid: 34dfa061-f42f-40f2-bf36-ee9c21ecd096
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# Bundle

Defines the root element of a bundle manifest. The manifest describes the structure and capabilities of the software to the system.

## Element hierarchy

**&lt;Bundle&gt;**

## Syntax

``` syntax
<Bundle IgnorableNamespaces? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
        SchemaVersion        = A version string in duo notation (major.minor) or trio notation (major.minor.appversion). >

  <!-- Child elements -->
  ( Identity
  & Packages
  & OptionalBundle{0,10000}
  )

</Bundle>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)
`{}`  specific range of occurrences

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
<td><strong>IgnorableNamespaces</strong></td>
<td><p>Declares namespace elements to ignore. Ignored namespace elements aren't validated and are considered untrusted. Multiple namespace elements are specified with a space between each namespace.</p></td>
<td>A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>SchemaVersion</strong></td>
<td><p>The version number of the bundle manifest schema.</p></td>
<td>A version string in duo notation (major.minor) or trio notation (major.minor.appversion).</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

<table>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Identity](element-identity.md)</td>
<td><p>Defines a globally unique identifier for a bundle. A bundle identity is represented as a tuple of attributes of the bundle.</p></td>
</tr>
<tr class="even">
<td>[Packages](element-packages.md)</td>
<td><p>Defines the app packages and resource packages that are contained in the bundle.</p></td>
</tr>
<tr class="odd">
<td>[OptionalBundle](element-optionalbundle.md)</td>
<td><p>Defines optional bundles relative to the main bundle.</p></td>
</tr>
</tbody>
</table>

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2013/bundle</p></td>
</tr>
</tbody>
</table>

 

 



