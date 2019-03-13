---
Description: Declares an app extensibility point of type windows.protocol.
Search.Product: eADQiWindows 10XVcnh
title: uap:Protocol (Windows 10)
ms.assetid: b92c542e-d4a4-4d6d-8a1b-257c4a43aecc
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:Protocol (Windows 10)


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
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd><b>&lt;uap:Protocol&gt;</b></dd>
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
<Protocol Name           = A string between 2 and 39 characters in length that contains numbers, lowercased letters, dots ('.'), pluses('+'), or hyphens ('-'). The string can't start with a dot ('.').

              DesiredView?   = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum"
              ReturnResults? = "none" | "always" | "optional" >

  <!-- Child elements -->
  ( uap:Logo?
  & uap:DisplayName?
  )

</uap:Protocol>
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
<td><strong>DesiredView</strong></td>
<td><p>The desired amount of screen space to use when the appointment launches.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>default</li>
<li>useLess</li>
<li>useHalf</li>
<li>useMore</li>
<li>useMinimum</li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td><p>The name of the URI scheme, such as &quot;mailto&quot;. This name must be unique for the package.</p></td>
<td>A string between 2 and 39 characters in length that contains numbers, lowercased letters, dots ('.'), pluses('+'), or hyphens ('-'). The string can't start with a dot ('.').</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ReturnResults</strong></td>
<td><p>Specifies whether the app returns a value when invoked via a URI activation.</p>
<ul>
<li>None: does not return a value.</li>
<li>Always: URI activation with this protocol will always return a result.</li>
<li>Optional: URI activation with this protocol will return a result if it is activated for results (using [<strong>LaunchUriForResultsAndContinueAsync</strong>](https://msdn.microsoft.com/library/windows/apps/dn904655)). However, this protocol activation endpoint can also handle activation when results are not required.</li>
</ul></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>none</li>
<li>always</li>
<li>optional</li>
</ul></td>
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
<td><a href="element-1-uap-displayname.md">uap:DisplayName</a> </td>
<td><p>A friendly name that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-uap-logo.md">uap:Logo</a> </td>
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
<td><a href="element-uap-extension.md">uap:Extension</a> </td>
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
      <uap:Extension Category="windows.protocol">
        <uap:Protocol Name="alsdk" />
      </uap:Extension>
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
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10</p></td>
</tr>
</tbody>
</table>

 

 



