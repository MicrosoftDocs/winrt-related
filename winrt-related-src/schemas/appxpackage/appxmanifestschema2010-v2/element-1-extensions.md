---
Description: Defines one or more extensibility points for the app.
Search.Product: eADQiWindows 10XVcnh
title: 'Extensions (type: CT\_ApplicationExtensions)'
ms.assetid: 267051e3-b09c-467c-b5bd-4575cc31cb36


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Extensions (type: CT\_ApplicationExtensions)




Defines one or more extensibility points for the app.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd><b>&lt;Extension&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Extensions>

  <!-- Child elements -->
  ApplicationExtensionChoice{1,10000}

</Extensions>
```

### Key

`{}`   specific range of occurrences

## Attributes and Elements


### Attributes

None.

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
<td><a href="element-applicationextensionchoice.md">ApplicationExtensionChoice</a> </td>
<td><p>The abstract application extension choice element for the XSD substitution group. This can't be declared in the XML.</p></td>
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
<td><a href="element-application.md">Application</a> </td>
<td><p>Represents an app that comprises part of or all of the functionality delivered in the package.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[Extensions (type: CT\_PackageExtensions)](element-extensions.md)**

## Remarks

Extensibility points are a mechanism by which an app can add functionality in a manner defined by the operating system. An example of an app extensibility point is the ability to create a file type association and enable your app to be the default handler for files with a specific file name extension.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><pre>http://schemas.microsoft.com/appx/2010/manifest</pre></td>
</tr>
</tbody>
</table>

 

 



