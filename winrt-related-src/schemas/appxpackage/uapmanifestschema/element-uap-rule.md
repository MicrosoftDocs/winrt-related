---
description: Specifies which pages in the web context have access to the system's geolocation devices and access to the clipboard (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:Rule (Windows 10)
ms.assetid: 99bea1bd-db33-4dc9-bdf5-299f413d5c00


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 11/01/2017
---

# uap:Rule (Windows 10)


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
<dt><a href="element-uap-applicationcontenturirules.md">&lt;uap:ApplicationContentUriRules&gt;</a></dt>
<dd><b>&lt;uap:Rule&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Rule Type                  = "include" | "exclude"
      Match                 = A string between 1 and 2084 characters in length.
      WindowsRuntimeAccess? = "allowForWebOnly" | "all" | "none" 
      uap5:ServiceWorker?   = Boolean />
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
<td><strong>Match</strong></td>
<td><p>The IRI to use in the rule. See RFC 3987 - Internationalized Resource Identifiers (IRIs) for details. It is unique per application in the package and is case sensitive. For example, values of Match can be: https://www.microsoft.com/, or *.pdf</p></td>
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
<tr class="odd">
<td><strong>WindowsRuntimeAccess</strong></td>
<td><p>Declares UWP (Windows Runtime) access from remote sites. This attribute gives control to a developer to specify the set of URIs that can access UWP APIs from their website.</p>
<p>The value &quot;allowForWebOnly&quot; indicates that only UWP APIs created by the developer and included inside the app package will be exposed. Note that the UWP Windows Runtime class that is intended to be exposed to JavaScript must be decorated with the [AllowForWeb] attribute where it is declared.</p>
<p>The value &quot;all&quot; indicates all allowed UWP APIs will be available.</p>
<p>The value &quot;none&quot; (the default value) explicitly states that no UWP APIs will be exposed.</p>
<p>This attribute is not allowed if Type is set to &quot;exclude&quot;.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>allowForWebOnly</li>
<li>all</li>
<li>none</li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap5:ServiceWorker</strong></td>
<td><p>This represents the registration of a service worker from a web page (a Progressive Web App) to run as a UWP app. If true, it will be determined whether a URL the app navigates to has the permission required to register the app as a service worker.</p></td>
<td><p>Boolean</p></td>
<td>No</td>
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
<td><a href="element-uap-applicationcontenturirules.md">uap:ApplicationContentUriRules</a> </td>
<td><p>Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

If more than one rule is defined, then the order of the rules is important.

To define the **Match** attribute with an IRI for a web resource, you can specify only secure "https:" sites - unsecure "http:" sites aren't allowed. If you specify a "http:" site, you get a schema semantic check validation error.

For any values that have a [scheme](/windows/uwp/launch-resume/launch-maps-app) in Windows 8.1 (version 6.3.0), the manifest only permits secure "https:" scheme. The manifest fails any other scheme. This rule doesn't apply on Windows 8 apps for backward compatibility.

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 
