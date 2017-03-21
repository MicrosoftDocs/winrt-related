---
Description: Defines a MNO formatted message that contains the parsing rules necessary for Windows 8 to parse the message.
Search.Product: eADQiWindows 10XVcnh
title: Message
ms.assetid: b4f7969d-5251-4536-b782-ded76f385550
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# Message


Defines a MNO formatted message that contains the parsing rules necessary for Windows 8 to parse the message.

## Element hierarchy

<dl>
<dt><a href="element-messages.md">&lt;Messages&gt;</a></dt>
<dd><b>&lt;Message&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Message Silent? = boolean : "true"
         RuleId? = token >

  <!-- Child elements -->
  ( ( SMSBearer+,
      USSDBearer?
    )
  | USSDBearer
  ),
  Pattern,
  Locale?,
  Units?,
  Fields?

</Message>
```

### Key

`?`   optional (zero or one)
`:`   default value
`+`   required (one or more)

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
<td><strong>RuleId</strong></td>
<td><p>The MNO defined rule ID for this message that is passed back within a [<strong>NetworkOperatorNotificationEventDetails</strong>](https://msdn.microsoft.com/library/windows/apps/br207377) event for message identification.</p></td>
<td>token</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Silent</strong></td>
<td><p>If <strong>true</strong>, the message is relayed only to the MNO application. Otherwise, <strong>false</strong>, the message is relayed to SMS clients and visible to the user.</p></td>
<td>boolean</td>
<td>No</td>
<td>true</td>
</tr>
</tbody>
</table>

 

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
<td>[Fields](element-fields.md)</td>
<td><p>Defines values that describe the subscriber's plan and data usage.</p></td>
</tr>
<tr class="even">
<td>[Locale](element-locale.md)</td>
<td><p>Defines the message country code in the form &quot;en-us&quot; using ISO-3166.</p></td>
</tr>
<tr class="odd">
<td>[Pattern](element-pattern.md)</td>
<td><p>Defines a regular expression describing the contents of the decoded human-readable message.</p></td>
</tr>
<tr class="even">
<td>[SMSBearer](element-smsbearer.md)</td>
<td><p>Defines bearer types allowed for SMS messages.</p></td>
</tr>
<tr class="odd">
<td>[USSDBearer](element-ussdbearer.md)</td>
<td><p>Defines bearer types allowed for USSD messages.</p></td>
</tr>
<tr class="even">
<td>[Units](element-units.md)</td>
<td><p>Defines how to interpret the unit fields corresponding to each number field. Carriers may specify a whitespace-delimited list of tokens corresponding to each of the supported multipliers.</p></td>
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
<td>[Messages](element-messages.md)</td>
<td><p>Contains a set of MNO messages that are parsed by Windows 8 and may be signaled to the user.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Must be at least one bearer of either type, but multiple SMS bearers permitted.

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

 

 



