---
description: Specifies a URL to which a plugin may send cookies.
Search.Product: eADQiWindows 10XVcnh
title: uap:Url (Windows 10)
ms.assetid: d552c065-2697-49d0-936e-f93dca38caad


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:Url (Windows 10)


Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL.

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
<dt><a href="element-uap-webaccountprovider.md">&lt;uap:WebAccountProvider&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-managedurls.md">&lt;uap:ManagedUrls&gt;</a></dt>
<dd><b>&lt;uap:Url&gt;</b></dd>
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
</dd>
</dl>

## Syntax

``` syntax
<Url>

  A string between 1 and 32767 characters in length in the form of a valid web url.

</uap:Url>
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
<td><a href="element-uap-managedurls.md">uap:ManagedUrls</a> </td>
<td><p>Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|   |   |
|--|--|
| Namespace | `	http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 



