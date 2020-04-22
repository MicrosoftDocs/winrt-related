---
Description: Specifies a badge's value or glyph.
Search.Product: eADQiWindows 10XVcnh
title: badge
ms.assetid: b16170df-5c92-4b03-8f4d-6d155d114725

keywords: windows 10, uwp, schema, badges


ms.topic: reference
ms.date: 04/05/2017
---

# badge

Specifies a badge's value or glyph.

## Element hierarchy

**&lt;badge&gt;**

## Syntax

``` syntax
<badge value    = "1-99" | "none" | "activity" | "alert" | "alarm" | "available" | ...
       version? = integer />
```

### Key

`?`   optional (zero or one)

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
<td><strong>value</strong></td>
<td><p>Either a numeric value or a string value that specifies a predefined badge glyph. Numerically, this value can accept any valid integer. A value of 0 clears the badge, values from 1-99 display as given, and any value greater than 99 displays as 99+.</p></td>
<td><p>This attribute can be set to an integer or have one of the following values:</p>
<ul>
<li>none</li>
<li>activity</li>
<li>alert</li>
<li>alarm</li>
<li>available</li>
<li>away</li>
<li>busy</li>
<li>newMessage</li>
<li>paused</li>
<li>playing</li>
<li>unavailable</li>
<li>error</li>
<li>attention</li>
</ul></td>
<td>Yes</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>version</strong></td>
<td><p>The version of the badge XML schema this particular payload was developed for.</p></td>
<td>integer</td>
<td>No</td>
<td>1</td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

This table shows the available status glyphs.


| Status      | Glyph                                                                   | XML                            |
|-------------|-------------------------------------------------------------------------|--------------------------------|
| none        | No badge shown                                                          | `<badge value="none"/>`        |
| activity    | ![the activity badge; two circling arrows](images/badge-4.png)          | `<badge value="activity"/>`    |
| alarm       | ![the alarm badge](images/badge-15.png)                                 | `<badge value="alarm"/>`       |
| alert       | ![the alert badge](images/badge-10.png)                                 | `<badge value="alert"/>`       |
| attention   | ![the attention badge; an exclamation point](images/attentionbadge.png) | `<badge value="attention"/>`   |
| available   | ![the available badge; a green dot](images/badge-11.png)                | `<badge value="available"/>`   |
| away        | ![the away badge; a yellow dot](images/badge-12.png)                    | `<badge value="away"/>`        |
| busy        | ![the busy badge; a red dot](images/badge-13.png)                       | `<badge value="busy"/>`        |
| error       | ![the error badge; an x](images/badge-9.png)                            | `<badge value="error"/>`       |
| newMessage  | ![the new mail badge; an envelope](images/badge-5.png)                  | `<badge value="newMessage"/>`  |
| paused      | ![the paused badge](images/badge-7.png)                                 | `<badge value="paused"/>`      |
| playing     | ![the playing badge](images/badge-6.png)                                | `<badge value="playing"/>`     |
| unavailable | ![the unavailable badge; a gray dot](images/badge-14.png)               | `<badge value="unavailable"/>` |

 

## See also


[Badge overview](https://msdn.microsoft.com/library/windows/apps/hh779719)

[App tiles and badges sample](https://go.microsoft.com/fwlink/p/?linkid=231469)

[How to send a glyph or numeric badge in a local notification](https://msdn.microsoft.com/library/windows/apps/hh700418)

[How to clear a badge](https://msdn.microsoft.com/library/windows/apps/hh700418)

[Guidelines and checklist for tiles and badges](https://msdn.microsoft.com/library/windows/apps/hh465403)

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/notifications/2012/badge.xsd` |

 

 



