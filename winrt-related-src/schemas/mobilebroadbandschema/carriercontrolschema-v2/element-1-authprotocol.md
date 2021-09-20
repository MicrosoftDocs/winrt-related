---
description: Defines the authentication protocol to use for a context in the Packet Data Protocol (PDP) context policy (descendant of TetheringProfile).
Search.Product: eADQiWindows 10XVcnh
title: AuthProtocol (descendant of TetheringProfile)
ms.assetid: 24272c9d-966a-4f02-a64b-6e7116131ba7

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# AuthProtocol (descendant of TetheringProfile)


Defines the authentication protocol to use for a context in the Packet Data Protocol (PDP) context policy.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-additionalpdpcontexts.md">&lt;AdditionalPDPContexts&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-tetheringsettings.md">&lt;TetheringSettings&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-tetheringprofile.md">&lt;TetheringProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-context.md">&lt;Context&gt;</a></dt>
<dd><b>&lt;AuthProtocol&gt;</b></dd>
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
<td><a href="element-1-context.md">Context</a> </td>
<td><p>Defines the context of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v2` |

 

 



