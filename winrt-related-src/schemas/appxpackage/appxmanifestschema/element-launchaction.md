---
description: Describes an AutoPlay content action (Windows 8).
Search.Product: eADQiWindows 10XVcnh
title: 'LaunchAction (Windows 8 package schema, child of AutoPlayContent)'
ms.assetid: 3561ba0c-690c-4c09-b383-b2c1e95f26d6


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# LaunchAction (package schema for Windows 8, child of AutoPlayContent)


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
<dt><a href="element-1-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-autoplaycontent.md">&lt;AutoPlayContent&gt;</a></dt>
<dd><b>&lt;LaunchAction&gt;</b></dd>
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
              ActionDisplayName = A string between 1 and 256 characters in length.
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
<p>This string is localizable.</p></td>
<td>A string between 1 and 256 characters in length.</td>
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
<td><a href="element-autoplaycontent.md">AutoPlayContent</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.autoPlayContent</strong>. The app provides the specified AutoPlay content actions.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[LaunchAction (in type: CT_AutoPlayDevice)](element-1-launchaction.md)**

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
<Extension Category="windows.autoPlayContent">
  <AutoPlayContent>
    <LaunchAction Verb="open" ActionDisplayName="Display" ContentEvent="ShowPicturesOnArrival"/>
  </AutoPlayContent>
</Extension>
```

## See also


[Supporting AutoPlay](/previous-versions/windows/apps/hh452731(v=win.10))

## Requirements

|               |   Value                                                          |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
