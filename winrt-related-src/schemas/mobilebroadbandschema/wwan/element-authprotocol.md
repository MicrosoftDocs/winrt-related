---
description: Defines the authentication protocol to be used for activating a Packet Data Protocol (PDP) context.
Search.Product: eADQiWindows 10XVcnh
title: AuthProtocol (descendant of DefaultProfile)
ms.assetid: 1cb2fe6e-48b1-4314-b7b7-17d6ab7e0f46

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# AuthProtocol (descendant of DefaultProfile)


Defines the authentication protocol to be used for activating a Packet Data Protocol (PDP) context:

-   **NONE** - No authentication protocol.
-   **PAP** - Unencrypted password authentication.
-   **CHAP** - Challenge Handshake Authentication Protocol(CHAP).
-   **MsCHAPv2** - Microsoft’s Challenge Handshake Authentication Protocol(CHAP) v2.0.

## Element hierarchy

<dl>
<dt><a href="element-defaultprofile.md">&lt;DefaultProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-context.md">&lt;Context&gt;</a></dt>
<dd><b>&lt;AuthProtocol&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<AuthProtocol>

  "NONE" | "PAP" | "CHAP" | "MsCHAPv2"

</AuthProtocol>
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
<td><a href="element-context.md">Context</a> </td>
<td><p>Defines the parameters required to setup a data connection.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This element is optional and is used only for GSM profiles. If the element is not specified and the profile is for a GSM device, then the Mobile Broadband service will use **NONE**.

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



