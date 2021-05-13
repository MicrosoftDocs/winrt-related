---
description: Contains a set of MNO messages that are parsed by Windows 8 and may be signaled to the user.
Search.Product: eADQiWindows 10XVcnh
title: Messages (WWAN schema)
ms.assetid: 08283c2b-d44e-4d03-8a0f-f213397cb93d

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Messages (WWAN schema)


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
<td><a href="element-message.md">Message</a> </td>
<td><p>Defines a MNO formatted message that contains the parsing rules necessary for Windows 8 to parse the message.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



