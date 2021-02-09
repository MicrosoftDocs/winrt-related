---
description: Defines the properties and login credentials for a Wi-Fi hotspot.
Search.Product: eADQiWindows 10XVcnh
title: HotspotProfile
ms.assetid: 7106b831-ef8c-4660-9b8b-4b13a8379ffd

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# HotspotProfile


Defines the properties and login credentials for a Wi-Fi hotspot. [**HotspotProfile**](element-hotspotprofile.md) is the unique root element of a Wi-Fi hotspot profile that uses the Wireless Internet Service Provider roaming (WISPr) protocol.

## Element hierarchy

**&lt;HotspotProfile&gt;**

## Syntax

``` syntax
<HotspotProfile>

  <!-- Child elements -->
  ( ( BasicAuth,
      TrustedDomains
    )
  | ( ExtAuth,
      TrustedDomains?
    )
  ),
  UserAgent?,
  SSIDConfig?,
  any element in a non-schema namespace*

</HotspotProfile>
```

### Key

`?`   optional (zero or one)
`*`   optional (zero or more)

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
<td><a href="element-basicauth.md">BasicAuth</a> </td>
<td><p>Contains the user name and password required for WISPr authentication. Using <a href="element-basicauth.md"><strong>BasicAuth</strong></a>  allows a static set of credentials to be used; use <a href="element-extauth.md"><strong>ExtAuth</strong></a> to have an app generate credentials for WISPr authentication.</p></td>
</tr>
<tr class="even">
<td><a href="element-extauth.md">ExtAuth</a> </td>
<td><p>Contains the parameters for handling WISPr authentication through an app (rather than specifying a static user name and password via <a href="element-basicauth.md"><strong>BasicAuth</strong></a> ).</p></td>
</tr>
<tr class="odd">
<td><a href="element-ssidconfig.md">SSIDConfig</a> </td>
<td><p>Contains a set of additional SSIDs that are handled by this profile to reduce the number of SSIDs in the WLAN profile store. Windows will not connect to these SSIDs until a user manually connects once. The newly-created profile will inherit the HotspotAuth settings from this profile.</p></td>
</tr>
<tr class="even">
<td><a href="element-trusteddomains.md">TrustedDomains</a> </td>
<td><p>Contains a set of one or more host names that are trusted for providing credentials over HTTPS. Can be either a fully qualified name (such as <em>hotspot.contoso.com</em>) or a wildcard to refer to all hosts under the given domain name (such as <em>.contoso.com</em>).</p></td>
</tr>
<tr class="odd">
<td><a href="element-useragent.md">UserAgent</a> </td>
<td><p>Customized HTTP user agent string to support operator-specific user agent filtering. This element is optional.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/WLAN/HotspotProfile/v1` |

 

 



