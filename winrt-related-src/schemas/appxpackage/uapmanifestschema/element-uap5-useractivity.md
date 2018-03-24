---
author: laurenhughes
title: uap5:UserActivity
description: Allows an app to opt out of engagement data tracking.
ms.author: lahugh
ms.date: 10/10/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:UserActivity

## Description
Allows an app to specify the web site associated with this application for cross platform UserActivity publishing.

## Element Hierarchy
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
<dt><a href="element-uap5-extension.md">&lt;uap5:Extension&gt;</a></dt>
<dd><b>&lt;uap5:UserActivity&gt;</b></dd>
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
```syntax
<uap5:UserActivity ActivitySourceHost = A string between 1 and 255 characters in length. />
```

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ActivitySourceHost | The fully-qualified domain name of the web site associated with the app. | A string between 1 and 255 characters in length. | Yes | 

### Child Elements
None

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/5</p></td>
</tr>
</tbody>
</table>
