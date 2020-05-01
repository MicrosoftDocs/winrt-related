---

ms.assetid: 33e5b0ce-9b38-4524-a11d-3909c6b85826
title: OptionalBundle
description:

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, optional bundle 
---

# OptionalBundle

## Description
Defines optional bundles relative to the main bundle. Optional bundles contain additional packages that apply to the main app package or bundle.

## Element Hierarchy
<dl>
<dt><a href="element-bundle.md">&lt;Bundle&gt;</a></dt>
<dd><b>&lt;OptionalBundle&gt;</b></dd>
</dl>


## Syntax
```syntax
<OptionalBundle Name      = A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
                Publisher = A string between 1 and 8192 characters in length that fits the regular expression  of a distinguished name : "(CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|Description|PostalCode|POBox|Phone|X21Address|dnQualifier|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")(, ((CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|Description|PostalCode|POBox|Phone|X21Address|dnQualifier|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.
                Version?  = A version string in quad notation, "Major.Minor.Build.Revision".
                FileName? = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. >

    <!-- Child elements -->
    Package{1,10000}
</OptionalBundle>
```


### Key
`?`   optional (zero or one)  
`{}`  specific range of occurrences

## Attributes

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td><p>Describes the contents of the bundle. The <strong>Name</strong> attribute is case-sensitive.</p></td>
<td>A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Publisher</td>
<td><p>Describes info about the publisher of the bundle.</p></td>
<td>A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name : &quot;(CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|Description|PostalCode|POBox|Phone|X21Address|dnQualifier|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+|&quot;.*&quot;)(, ((CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|Description|PostalCode|POBox|Phone|X21Address|dnQualifier|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+|&quot;.*&quot;)))*&quot;. Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>Version</td>
<td><p>The version number of the bundle.</p></td>
<td>A version string in quad notation, &quot;Major.Minor.Build.Revision&quot;.</td>
<td>No</td>
</tr>
<tr class="even">
<td>FileName</td>
<td><p>The file name of the bundle.</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *.</td>
<td>No</td>
</tr>
</tbody>
</table>

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [Package](element-optionalbundle-package.md) | Defines one of the app packages or resource packages in the optional bundle. |

## Remarks


## Examples

## Requirements
|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2016/bundle` |
