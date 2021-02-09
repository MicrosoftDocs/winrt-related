---
description: Defines whether Federal Information Processing Standards (FIPS) mode is enabled.
Search.Product: eADQiWindows 10XVcnh
title: FIPSMode
ms.assetid: 0544cc73-0636-494c-a205-9831e43bd16f

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

When a wireless connection is operating in FIPS mode, the security level of the connection complies with the FIPS 140-2 standard. For more information about FIPS, see the [FIPS Home Page](https://go.microsoft.com/fwlink/p/?linkid=86229).

This element is optional. If this element is not specified in a profile, then FIPS mode is not enabled.

**FIPSMode** can be enabled only when the following conditions are met:

-   The [**authentication**](../wlan/element-authentication.md) element has a value of `WPA2` or `WPA2PSK`.
-   The [**encryption**](../wlan/element-encryption.md) element has a value of `AES`.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WLAN/v2` |

 

 
