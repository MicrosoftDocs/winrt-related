---
Description: Defines a regular expression describing the contents of the decoded human-readable message.
Search.Product: eADQiWindows 10XVcnh
title: Pattern
ms.assetid: 873958b1-2344-46ce-b5b4-d0139156389d
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Pattern


Defines a regular expression describing the contents of the decoded human-readable message.

## Element hierarchy

<dl>
<dt><a href="element-messages.md">&lt;Messages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-message.md">&lt;Message&gt;</a></dt>
<dd><b>&lt;Pattern&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Pattern>

  string

</Pattern>
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
<td>[Message](element-message.md)</td>
<td><p>Defines a MNO formatted message that contains the parsing rules necessary for Windows 8 to parse the message.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This regular expression must match an incoming message for further parsing to proceed. The regular expression may also specify one or more capturing groups to be processed by subsequent rules. The class of messages described by a RegEx must not overlap with the class described by any other RegEx in the provisioning file.

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

 

 



