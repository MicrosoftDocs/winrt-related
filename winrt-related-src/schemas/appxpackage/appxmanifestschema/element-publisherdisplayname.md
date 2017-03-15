---
Description: PublisherDisplayName
MS-HAID: AppxManifestSchema.element\_PublisherDisplayName
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: PublisherDisplayName
ms.assetid: 8df2d218-e62d-4b2e-8db5-3436c67aa04c
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# PublisherDisplayName


A friendly name for the publisher that can be displayed to users.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;PublisherDisplayName&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<PublisherDisplayName>

  A string between 1 and 256 characters in length.

</PublisherDisplayName>
```

## Attributes and Elements


### Attributes

None.

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
<td>[Properties](element-properties.md)</td>
<td><p>Defines additional metadata about the package including attributes that describe how the package appears to users.</p>
<div class="alert">
<strong>Note</strong>  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “|” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](https://msdn.microsoft.com/library/windows/desktop/hh973484) if you get an error.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

## Remarks

This string is localizable. 

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

 

 



