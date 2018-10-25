---
Description: Describes an AutoPlay device action.
Search.Product: eADQiWindows 10XVcnh
title: uap:LaunchAction (in uap:AutoPlayDevice) (Windows 10)
ms.assetid: 9b7d9e7a-4f85-4525-9a6b-683b3b78c23d
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:LaunchAction (in uap:AutoPlayDevice) (Windows 10)


Describes an AutoPlay device action.

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
<dt><a href="element-uap-autoplaydevice.md">&lt;uap:AutoPlayDevice&gt;</a></dt>
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
                  DeviceEvent       = A string between 1 and 255 characters in length. Backward slashes ('\') are not allowed. />
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
<td><strong>DeviceEvent</strong></td>
<td><p>The name of a device-related event that the extensibility point handles. For more info, see Remarks.</p></td>
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
<td>[uap:AutoPlayDevice](element-uap-autoplaydevice.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.autoPlayDevice</strong>. The app provides the specified AutoPlay device actions.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[uap:LaunchAction (in type: CT_AutoPlayContent)](element-uap-launchaction.md)**
-   **[uap:LaunchAction (global)](element-2-uap-launchaction.md)**

## Remarks

**ContentEvent** can be a custom event defined for the device. For WPD devices, **ContentEvent** can be one of the following well-known events:

-   **WPD\\AudioSource**
-   **WPD\\ImageSource**
-   **WPD\\VideoSource**

## Examples

```XML
<uap:Extension Category="windows.autoPlayDevice">
  <uap:AutoPlayContent>
    <uap:LaunchAction Verb="import" ActionDisplayName="Import" ContentEvent="WPD\ImageSource"/>
  </uap:AutoPlayContent>
</uap:Extension>
```

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

 

 



