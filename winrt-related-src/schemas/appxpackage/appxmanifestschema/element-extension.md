---
Description: Declares an extensibility point for the package.
Search.Product: eADQiWindows 10XVcnh
title: 'Extension (in type: CT_PackageExtensions)'
ms.assetid: 72f0d1ae-15a4-4eba-a3ca-990f4de2b697
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Extension (in type: CT_PackageExtensions)


Declares an extensibility point for the package.

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
<Extension Category = "windows.activatableClass.inProcessServer" | "windows.activatableClass.outOfProcessServer" | "windows.activatableClass.proxyStub" | "windows.gameExplorer" | "windows.certificates" >

  <!-- Child elements -->
  ( InProcessServer
  | OutOfProcessServer
  | ProxyStub
  | GameExplorer
  | Certificates
  )

</Extension>
```

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
<td><strong>Category</strong></td>
<td><p>The type of package extensibility point.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>windows.activatableClass.inProcessServer</li>
<li>windows.activatableClass.outOfProcessServer</li>
<li>windows.activatableClass.proxyStub</li>
<li>windows.gameExplorer</li>
<li>windows.certificates</li>
</ul></td>
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
<td><a href="element-certificates.md">Certificates</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.certificates</strong>. The app requires one or more certificates from the specified certificate stores.</p></td>
</tr>
<tr class="even">
<td><a href="element-gameexplorer.md">GameExplorer</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.gameExplorer</strong>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-inprocessserver.md">InProcessServer</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.inProcessServer</strong>. The app uses a dynamic link library (DLL) that exposes one or more activatable classes.</p></td>
</tr>
<tr class="even">
<td><a href="element-outofprocessserver.md">OutOfProcessServer</a> </td>
<td><p>Declares a package extension point of type <strong>windows.activatableClass.outOfProcessServer</strong>. The app uses an executable (EXE) that exposes one or more activatable classes.</p></td>
</tr>
<tr class="odd">
<td><a href="element-proxystub.md">ProxyStub</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.proxyStub</strong>. A proxy can be composed of one or more interfaces.</p></td>
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
<td><a href="element-extensions.md">Extensions (type: CT_PackageExtensions)</a> </td>
<td><p>Defines one or more extensibility points for the package.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[Extension (in type: CT_ApplicationExtensions)](element-1-extension.md)**

## Remarks

Extensibility points are a mechanism by which a package can add functionality in a manner defined by the operating system. An extensibility point is a location where an app can register to execute code or use resources of the current package. To add functionality for a particular app, use the [**Application**](element-application.md) child element of the [**Applications**](element-applications.md) element.

These extensibility points can't be declared multiple times in a manifest:

-   **windows.certificates**
-   **windows.gameExplorer**

## See also


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

 

 



