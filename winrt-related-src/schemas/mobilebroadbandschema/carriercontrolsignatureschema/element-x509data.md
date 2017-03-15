---
Description: X509Data
MS-HAID: CarrierControlSignatureSchema.element\_X509Data
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: X509Data
ms.assetid: 1e3356cf-1c4d-45da-bb08-11329c586529
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# X509Data


Defines one or more X.509 compliant signatures as defined in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-keyinfo.md">&lt;KeyInfo&gt;</a></dt>
<dd><b>&lt;X509Data&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<X509Data>

  <!-- Child elements -->
  X509Certificate+

</X509Data>
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
<td>[X509Certificate](element-x509certificate.md)</td>
<td><p>Defines an X.509 compliant signature as defined in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
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
<td>[KeyInfo](element-keyinfo.md)</td>
<td><p>Defines all key information used to validate the signature as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
</tbody>
</table>

 

## Remarks

**X509Data** contains only [**X509Certificate**](element-x509certificate.md) elements. All other child elements defined in [XML DSIG](http://www.w3.org/TR/xmldsig-core/) are disallowed.

[**KeyInfo**](element-keyinfo.md) may contain only one **X509Data** element.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.w3.org/2000/09/xmldsig#</p></td>
</tr>
</tbody>
</table>

 

 



