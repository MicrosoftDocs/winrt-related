---
description: Specifies which pages in the web context have access to the system's geolocation devices and access to the clipboard.
Search.Product: eADQiWindows 10XVcnh
title: Rule
ms.assetid: c78c8c62-df95-4202-b3f0-75ddbb7e0e46


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Rule

Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.

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
<dt><a href="element-applicationcontenturirules.md">&lt;ApplicationContentUriRules&gt;</a></dt>
<dd><b>&lt;Rule&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Rule Type  = "include" | "exclude"
      Match = A string between 1 and 2084 characters in length. />
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
<td><strong>Match</strong></td>
<td><p>The IRI to use in the rule. See RFC 3987 - Internationalized Resource Identifiers (IRIs) for details. It is unique per application in the package and is case sensitive.</p></td>
<td>A string between 1 and 2084 characters in length.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Type</strong></td>
<td><p>A string that specifies whether the rule is an inclusion or exclusion rule.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>include</li>
<li>exclude</li>
</ul></td>
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
<td><a href="element-applicationcontenturirules.md">ApplicationContentUriRules</a> </td>
<td><p>Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

If more than one rule is defined, then the order of the rules is important.

To define the **Match** attribute with an IRI for a web resource, you can specify only secure "https:" sites - unsecure "http:" sites aren't allowed. If you specify a "http:" site, you get a schema semantic check validation error.

For any values that have a [scheme](/windows/uwp/launch-resume/launch-maps-app) in Windows 8.1 (version 6.3.0), the manifest only permits secure "https:" scheme. The manifest fails any other scheme. This rule doesn't apply on Windows 8 apps for backward compatibility.

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
