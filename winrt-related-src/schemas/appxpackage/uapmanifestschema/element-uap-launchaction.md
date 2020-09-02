---
Description: Describes an AutoPlay content action.
Search.Product: eADQiWindows 10XVcnh
title: uap:LaunchAction (in uap:AutoPlayContent) (Windows 10)
ms.assetid: 5d2c732f-08dd-4e7e-93b1-6bb122e2179f


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:LaunchAction (in uap:AutoPlayContent) (Windows 10)


Describes an AutoPlay content action.

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
<dd>
<dl>
<dt><a href="element-uap-autoplaycontent.md">&lt;uap:AutoPlayContent&gt;</a></dt>
<dd><b>&lt;uap:LaunchAction&gt;</b></dd>
</dl>
</dd>
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
<LaunchAction Verb              = A string between 1 and 64 characters in length that consists of alphanumeric, period, dash, and space characters only.
                  ActionDisplayName = A string between 1 and 256 characters in length. This string is localizable. 
                  ContentEvent      = A string between 1 and 255 characters in length. Backward slashes ('\') are not allowed. />
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
<td><strong>ActionDisplayName</strong></td>
<td><p>The name displayed to the user in the AutoPlay flyout for the handler.</p>
<p>This string is localizable. </p></td>
<td>A string between 1 and 256 characters in length. This string is localizable.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ContentEvent</strong></td>
<td><p>The name of a content-related event that the extensibility point handles. For more info, see Remarks.</p></td>
<td>A string between 1 and 255 characters in length. Backward slashes ('\') are not allowed.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Verb</strong></td>
<td><p>A unique identifier that is passed to the app when it is launched. The app can use this string to determine which AutoPlay handler triggered its launch. It is unique per application in the package and is case sensitive.</p></td>
<td>A string between 1 and 64 characters in length that consists of alphanumeric, period, dash, and space characters only.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

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
<td><a href="element-uap-autoplaycontent.md">uap:AutoPlayContent</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.autoPlayContent</strong>. The app provides the specified AutoPlay content actions.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[uap:LaunchAction (in type: CT_AutoPlayDevice)](element-1-uap-launchaction.md)**
-   **[uap:LaunchAction (global)](element-2-uap-launchaction.md)**

## Remarks

**ContentEvent** can be a custom event defined by the volume or one of the following well-known events:

-   **HandleCDBurningOnArrival**
-   **HandleDVDBurningOnArrival**
-   **MixedContentOnArrival**
-   **PlayBluRayOnArrival**
-   **PlayCDAudioOnArrival**
-   **PlayDVDAudioOnArrival**
-   **PlayDVDMovieOnArrival**
-   **PlayEnhancedCDOnArrival**
-   **PlayEnhancedDVDOnArrival**
-   **PlayMusicFilesOnArrival**
-   **PlaySuperVideoCDMovieOnArrival**
-   **PlayVideoCDMovieOnArrival**
-   **PlayVideoFilesOnArrival**
-   **ShowPicturesOnArrival**
-   **StorageOnArrival**
-   **UnknownContentOnArrival**

## Examples

```XML
<uap:Extension Category="windows.autoPlayContent">
  <uap:AutoPlayContent>
    <uap:LaunchAction Verb="open" ActionDisplayName="Display" ContentEvent="ShowPicturesOnArrival"/>
  </uap:AutoPlayContent>
</uap:Extension>
```

## See also


[Supporting AutoPlay](/previous-versions/windows/apps/hh452731(v=win.10))

## Requirements

|   |   |
|--|--|
| Namespace | `	http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 