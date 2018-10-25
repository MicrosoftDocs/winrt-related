---
Description: Defines whether Federal Information Processing Standards (FIPS) mode is enabled.
Search.Product: eADQiWindows 10XVcnh
title: FIPSMode
ms.assetid: 0544cc73-0636-494c-a205-9831e43bd16f
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# FIPSMode


Defines whether Federal Information Processing Standards (FIPS) mode is enabled.

## Element hierarchy

**&lt;FIPSMode&gt;**

## Syntax

``` syntax
<FIPSMode>

  boolean

</FIPSMode>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

When a wireless connection is operating in FIPS mode, the security level of the connection complies with the FIPS 140-2 standard. For more information about FIPS, see the [FIPS Home Page](http://go.microsoft.com/fwlink/p/?linkid=86229).

This element is optional. If this element is not specified in a profile, then FIPS mode is not enabled.

**FIPSMode** can be enabled only when the following conditions are met:

-   The [**authentication**](https://msdn.microsoft.com/library/windows/apps/hh868402) element has a value of `WPA2` or `WPA2PSK`.
-   The [**encryption**](https://msdn.microsoft.com/library/windows/apps/hh868403) element has a value of `AES`.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/WLAN/v2</p></td>
</tr>
</tbody>
</table>

 

 



