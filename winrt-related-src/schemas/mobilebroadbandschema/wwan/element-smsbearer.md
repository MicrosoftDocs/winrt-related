---
Description: Defines bearer types allowed for SMS messages.
Search.Product: eADQiWindows 10XVcnh
title: SMSBearer
ms.assetid: 33e79977-cca7-400a-8d01-c3dc72670b3f
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# SMSBearer


Defines bearer types allowed for SMS messages.

## Element hierarchy

<dl>
<dt><a href="element-messages.md">&lt;Messages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-message.md">&lt;Message&gt;</a></dt>
<dd><b>&lt;SMSBearer&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<SMSBearer Sender?        = token
           ClassZeroOnly? = boolean : "true" />
```

### Key

`?`   optional (zero or one)
`:`   default value
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
<td><strong>ClassZeroOnly</strong></td>
<td><p>If <strong>true</strong>, non-class-0 messages should be ignored for matching purposes. Otherwise, if <strong>false</strong> or omitted, all messages will be parsed.</p></td>
<td>boolean</td>
<td>No</td>
<td>true</td>
</tr>
<tr class="even">
<td><strong>Sender</strong></td>
<td><p>Defines a numeric sender to expect on an incoming message. If omitted, any sender is allowed for these messages. Formatted as a string of digits to avoid internationalization / length issues.</p></td>
<td>token</td>
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
<td>[Message](element-message.md)</td>
<td><p>Defines a MNO formatted message that contains the parsing rules necessary for Windows 8 to parse the message.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/WWAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



