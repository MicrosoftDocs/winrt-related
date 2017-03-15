---
Description: pm:PhoneIdentity (Windows 10)
MS-HAID: UapManifestSchema.element\_pm\_PhoneIdentity
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: pm:PhoneIdentity (Windows 10)
ms.assetid: 817d5865-3838-4554-b751-2af09d84c8ad
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# pm:PhoneIdentity (Windows 10)


If your app is an update to an app previously made available on Windows Phone, ensure that this element matches what is in the app manifest of your previous app. Use the same GUIDs that were assigned to the app by the Store. This ensures that users of your app who are upgrading to Windows 10 will receive your new app as an update, and not as a duplicate.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;pm:PhoneIdentity&gt;</b></dd>
</dl>

## Syntax

``` syntax
<PhoneIdentity PhoneProductId   = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
                  PhonePublisherId = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. />
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
<td><strong>PhoneProductId</strong></td>
<td><p>Describes the product information.</p></td>
<td>A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>PhonePublisherId</strong></td>
<td><p>Describes the publisher information.</p></td>
<td>A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.</td>
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
<td>[Package](element-package.md)</td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2014/phone/manifest</p></td>
</tr>
</tbody>
</table>

 

 



