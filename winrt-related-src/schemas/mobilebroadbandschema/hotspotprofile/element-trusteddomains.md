---
Description: TrustedDomains
MS-HAID: HotSpotProfile.element\_TrustedDomains
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: TrustedDomains
ms.assetid: 5da7e270-ed7b-4441-ae73-274ce5323f4b
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# TrustedDomains


Contains a set of one or more host names that are trusted for providing credentials over HTTPS. Can be either a fully qualified name (such as *hotspot.contoso.com*) or a wildcard to refer to all hosts under the given domain name (such as *.contoso.com*).

## Element hierarchy

<dl>
<dt><a href="element-hotspotprofile.md">&lt;HotspotProfile&gt;</a></dt>
<dd><b>&lt;TrustedDomains&gt;</b></dd>
</dl>

## Syntax

``` syntax
<TrustedDomains>

  <!-- Child elements -->
  TrustedDomain+

</TrustedDomains>
```

### Key

`+`   required (one or more)

## Attributes and Elements


### Attributes

None.

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[TrustedDomain](element-trusteddomain.md)</td>
<td><p>A host name that is trusted for providing credentials over HTTPS. Can be either a fully qualified name (such as <em>hotspot.contoso.com</em>) or a wildcard to refer to all hosts under the given domain name (such as <em>.contoso.com</em>).</p></td>
</tr>
</tbody>
</table>

 

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
<td>[HotspotProfile](element-hotspotprofile.md)</td>
<td><p>Defines the properties and login credentials for a Wi-Fi hotspot. [<strong>HotspotProfile</strong>](element-hotspotprofile.md) is the unique root element of a Wi-Fi hotspot profile that uses the Wireless Internet Service Provider roaming (WISPr) protocol.</p></td>
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
<td><p>http://www.microsoft.com/networking/WLAN/HotspotProfile/v1</p></td>
</tr>
</tbody>
</table>

 

 



