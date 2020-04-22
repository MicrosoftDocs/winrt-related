---
Description: Declares an extensibility point for the package.
Search.Product: eADQiWindows 10XVcnh
title: Extension (in Package/Extensions) (Windows 10)
ms.assetid: 72f0d1ae-15a4-4eba-a3ca-990f4de2b697
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/10/2018
---

# Extension (in Package/Extensions) (Windows 10)


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
<Extension Category = "windows.activatableClass.inProcessServer" | "windows.activatableClass.outOfProcessServer" | "windows.activatableClass.proxyStub" | "windows.certificates" | "windows.publisherCacheFolders" | "windows.comInterface" | "windows.loaderSearchPathOverride"
           uap10:TrustLevel?       = String value. Can be one of the following: "appContainer", "mediumIL".
           uap10:RuntimeBehavior?  = String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".
           uap10:HostId?           = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
           uap10:Parameters?       = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >

  <!-- Child elements -->
  ( InProcessServer
  | OutOfProcessServer
  | ProxyStub
  | Certificates
  | PublisherCacheFolders
  | com:ComInterface
  | uap6:LoaderSearchPathOverride
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
<li>windows.certificates</li>
<li>windows.publisherCacheFolders</li>
<li>windows.comInterface</li>
<li>windows.loaderSearchPathOverride</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap10:TrustLevel</strong></td>
<td><p>Specifies the trust level of the extension. </p></td>
<td>String value. Can be one of the following: "appContainer", "mediumIL". </td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap10:RuntimeBehavior</strong></td>
<td><p>Specifies the run time behavior of the extension. </p></td>
<td>String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App". </td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap10:HostId</strong></td>
<td><p>This value specifies the app ID of the host app for the extension. </p></td>
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap10:Parameters</strong></td>
<td><p>Contains command line parameters for the extension.</p></td>
<td>A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. </td>
<td>No</td>
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
<td><a href="element-inprocessserver.md">InProcessServer</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.inProcessServer</strong>. The app uses a dynamic link library (DLL) that exposes one or more activatable classes.</p></td>
</tr>
<tr class="odd">
<td><a href="element-outofprocessserver.md">OutOfProcessServer</a> </td>
<td><p>Declares a package extension point of type <strong>windows.activatableClass.outOfProcessServer</strong>. The app uses an executable (EXE) that exposes one or more activatable classes.</p></td>
</tr>
<tr class="even">
<td><a href="element-proxystub.md">ProxyStub</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.proxyStub</strong>. A proxy can be composed of one or more interfaces.</p></td>
</tr>
<tr class="odd">
<td><a href="element-publishercachefolders.md">PublisherCacheFolders</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.publisherCacheFolders</strong>. This specifies one or more folders that the package shares with other packages from the same publisher.</p></td>
</tr>
<tr class="even">
<td><a href="element-com-package-interface.md">com:ComInterface</a> </td>
<td><p>Declares a package extension point of type <strong>windows.comInterface.</strong></p></td>
</tr>
<tr class="odd">
<td><a href="element-uap6-LoaderSearchPathOverride.md">uap6:LoaderSearchPathOverride</a> </td>
<td><p>Declares a package extension point of type <strong>windows.loaderSearchPathOverride.</strong></p></td>
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

-   **[Extension (global)](element-1-extension.md)**

## Remarks

Extensibility points are a mechanism by which a package can add functionality in a manner defined by the operating system. An extensibility point is a location where an app can register to execute code or use resources of the current package. To add functionality for a particular app, use the [**Application**](element-application.md) child element of the [**Applications**](element-applications.md) element.

The **windows.certificates** extensibility point can't be declared multiple times in a manifest.

## See also


**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10`<br/><br/>`http://schemas.microsoft.com/appx/manifest/uap/windows10/10` (for the **uap10** attributes) |
