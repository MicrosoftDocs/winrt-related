---
description: A host name that is trusted for providing credentials over HTTPS.
Search.Product: eADQiWindows 10XVcnh
title: TrustedDomain
ms.assetid: e2dc8d60-cddd-4fd7-8092-ee34815a2cc5

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# TrustedDomain


A host name that is trusted for providing credentials over HTTPS. Can be either a fully qualified name (such as *hotspot.contoso.com*) or a wildcard to refer to all hosts under the given domain name (such as *.contoso.com*).

## Element hierarchy

<dl>
<dt><a href="element-hotspotprofile.md">&lt;HotspotProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-trusteddomains.md">&lt;TrustedDomains&gt;</a></dt>
<dd><b>&lt;TrustedDomain&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TrustedDomain>

  token

</TrustedDomain>
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
<td><a href="element-trusteddomains.md">TrustedDomains</a> </td>
<td><p>Contains a set of one or more host names that are trusted for providing credentials over HTTPS. Can be either a fully qualified name (such as <em>hotspot.contoso.com</em>) or a wildcard to refer to all hosts under the given domain name (such as <em>.contoso.com</em>).</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/WLAN/HotspotProfile/v1` |

 

 



