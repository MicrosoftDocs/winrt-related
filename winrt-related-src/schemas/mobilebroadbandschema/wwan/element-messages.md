---
Description: Messages
MS-HAID: WWAN.element\_Messages
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Messages
ms.assetid: 08283c2b-d44e-4d03-8a0f-f213397cb93d
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# Messages


Contains a set of MNO messages that are parsed by Windows 8 and may be signaled to the user.

## Element hierarchy

**&lt;Messages&gt;**

## Syntax

``` syntax
<Messages>

  <!-- Child elements -->
  Message+

</Messages>
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
<td>[Message](element-message.md)</td>
<td><p>Defines a MNO formatted message that contains the parsing rules necessary for Windows 8 to parse the message.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/WWAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



