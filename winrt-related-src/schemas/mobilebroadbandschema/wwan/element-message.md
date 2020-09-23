---
Description: Defines a MNO formatted message that contains the parsing rules necessary for Windows 8 to parse the message.
Search.Product: eADQiWindows 10XVcnh
title: Message
ms.assetid: b4f7969d-5251-4536-b782-ded76f385550

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
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
<td><p>The MNO defined rule ID for this message that is passed back within a <a href="/uwp/api/Windows.Networking.NetworkOperators.NetworkOperatorNotificationEventDetails"><strong>NetworkOperatorNotificationEventDetails</strong></a>  event for message identification.</p></td>
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
<td><a href="element-fields.md">Fields</a> </td>
<td><p>Defines values that describe the subscriber's plan and data usage.</p></td>
</tr>
<tr class="even">
<td><a href="element-locale.md">Locale</a> </td>
<td><p>Defines the message country code in the form &quot;en-us&quot; using ISO-3166.</p></td>
</tr>
<tr class="odd">
<td><a href="element-pattern.md">Pattern</a> </td>
<td><p>Defines a regular expression describing the contents of the decoded human-readable message.</p></td>
</tr>
<tr class="even">
<td><a href="element-smsbearer.md">SMSBearer</a> </td>
<td><p>Defines bearer types allowed for SMS messages.</p></td>
</tr>
<tr class="odd">
<td><a href="element-ussdbearer.md">USSDBearer</a> </td>
<td><p>Defines bearer types allowed for USSD messages.</p></td>
</tr>
<tr class="even">
<td><a href="element-units.md">Units</a> </td>
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
<td><a href="element-messages.md">Messages</a> </td>
<td><p>Contains a set of MNO messages that are parsed by Windows 8 and may be signaled to the user.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Must be at least one bearer of either type, but multiple SMS bearers permitted.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 