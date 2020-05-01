---
Description: Declares an extensibility point for the package.
Search.Product: eADQiWindows 10XVcnh
title: Extension (in Application/Extensions) (Windows 10)
ms.assetid: e25d664a-67e8-4a22-a666-1b11286b58f3
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Extension (in Application/Extensions) (Windows 10)


Declares an extensibility point for the package.

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
<dd><b>&lt;Extension&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Extension Category       = "windows.backgroundTasks" | "windows.preInstalledConfigTask" | "windows.updateTask" | "windows.restrictedLaunch"
           Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
           EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type.
If EntryPoint is not specified, the EntryPoint defined for the app is used instead.

           RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
           StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
           ResourceGroup? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
           uap10:TrustLevel?   = String value. Can be one of the following: "appContainer", "mediumIL".
           uap10:RuntimeBehavior?  = String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".
           uap10:HostId?       = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
           uap10:Parameters?   = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >

  <!-- Child elements -->
  BackgroundTasks?

</Extension>
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
<td><strong>Category</strong></td>
<td><p>The type of package extensibility point.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>windows.backgroundTasks</li>
<li>windows.preInstalledConfigTask</li>
<li>windows.updateTask</li>
<li>windows.restrictedLaunch</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>EntryPoint</strong></td>
<td><p>The activatable class ID.</p></td>
<td>A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Executable</strong></td>
<td><p>The default launch executable.</p></td>
<td>A string between 1 and 256 characters in length that must end with &quot;.exe&quot; and cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ResourceGroup</strong></td>
<td><p>A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See <a href="element-application.md"><strong>Application@ResourceGroup</strong></a>  and Remarks.</p></td>
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>RuntimeType</strong></td>
<td><p>The runtime provider. This attribute is used typically when there are mixed frameworks in an app.</p></td>
<td>A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, &quot;, /, \, |, ?, or *.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>StartPage</strong></td>
<td><p>The web page that handles the extensibility point.</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap10:TrustLevel</strong></td>
<td><p>Specifies the trust level of the extension.</p></td>
<td>String value. Can be one of the following: "appContainer", "mediumIL". </td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap10:RuntimeBehavior</strong></td>
<td><p>Specifies the run time behavior of the extension.</p></td>
<td>String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App". </td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap10:HostId</strong></td>
<td><p>This value specifies the app ID of the host app for the extension.</p></td>
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap10:Parameters</strong></td>
<td><p>Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity.</p></td>
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
<td><a href="element-backgroundtasks.md">BackgroundTasks</a> </td>
<td><p>Defines an app extensibility point of type <strong>windows.backgroundTasks</strong>. Background tasks run in a dedicated background host; that is, without a UI.</p></td>
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
<td><a href="element-1-extensions.md">Extensions (type: CT_ApplicationExtensions)</a> </td>
<td><p>Defines one or more extensibility points for the app.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[Extension (in type: CT_PackageExtensions)](element-extension.md)**

## Remarks

Extensibility points are a mechanism by which a package can add functionality in a manner defined by the operating system. An extensibility point is a location where an app can register to execute code or use resources of the current package. To add functionality for a particular app, use the [**Application**](element-application.md) child element of the [**Applications**](element-applications.md) element.

The **windows.certificates** extensibility point can't be declared multiple times in a manifest.

**Note**  Either the **EntryPoint** or **StartPage** attribute is required if the **Category** attribute is windows.UpdateTask or windows.preInstalledConfigTask for versions of Windows 10 before Windows 10, version 1607. Starting with Windows 10, version 1607, you no longer need to specify a value for **EntryPoint** or **StartPage** when **Category** is windows.UpdateTask or windows.preInstalledConfigTask and your application targets only devices that run Windows 10, version 1607 or later.

 

## See also


**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10`<br/><br/>`http://schemas.microsoft.com/appx/manifest/uap/windows10/10` (for the **uap10** attributes) |
