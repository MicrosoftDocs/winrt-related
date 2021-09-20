---
description: Defines a globally unique identifier for a package Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Identity (Windows 10)
ms.assetid: 45524773-3b61-44ac-a417-cfaac92af0a0


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 03/09/2017
---

# Identity (Windows 10)


Defines a globally unique identifier for a package. A package identity is represented as a tuple of attributes of the package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Identity&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Identity Name                   = A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
          ProcessorArchitecture? = "x86" | "x64" | "arm" | "arm64" | "neutral"
          Publisher              = A string between 1 and 8192 characters in length that fits the regular expression  of a distinguished name : "(CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+="<>#;])+ | ".*")(, ((CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+="<>#;])+ | ".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.
          Version                = A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0". 
          ResourceId?            = An ASCII string between 1 and 30 characters in length. />
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
<td><strong>Name</strong></td>
<td><p>Describes the contents of the package. The <strong>Name</strong> attribute is case-sensitive.</p>
<p>Use the <a href="element-displayname.md">DisplayName</a> attribute to display a package name to users.</p>
<p>This string cannot end with a period and cannot be one of these strings: &quot;CON&quot;, &quot;PRN&quot;, &quot;AUX&quot;, &quot;NUL&quot;, &quot;COM1&quot;, &quot;COM2&quot;, &quot;COM3&quot;, &quot;COM4&quot;, &quot;COM5&quot;, &quot;COM6&quot;, &quot;COM7&quot;, &quot;COM8&quot;, &quot;COM9&quot;, &quot;LPT1&quot;, &quot;LPT2&quot;, &quot;LPT3&quot;, &quot;LPT4&quot;, &quot;LPT5&quot;, &quot;LPT6&quot;, &quot;LPT7&quot;, &quot;LPT8&quot;, and &quot;LPT9&quot;.</p></td>
<td>A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.</td>
<td>Yes</td>
</tr>
<tr class="even">
<td><strong>ProcessorArchitecture</strong></td>
<td><p>Describes the architecture of the code contained in the package. A package that includes executable code must include this attribute. Defaults to &quot;neutral&quot;.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>x86</li>
<li>x64</li>
<li>arm</li>
<li>arm64</li>
<li>neutral</li>
</ul></td>
<td>No</td>
</tr>
<tr class="odd">
<td><strong>Publisher</strong></td>
<td><p>Describes the publisher information. The <strong>Publisher</strong> attribute must match the publisher subject information of the certificate used to sign a package. For more information see <a href="/windows/uwp/packaging/index">Packaging apps</a>.</p></td>
<td>A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name : &quot;(CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+ | &quot;.*&quot;)(, ((CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+ | &quot;.*&quot;)))*&quot;. Further, semantic validation ensures that the string is compliant with <a href="/windows/win32/api/wincrypt/nf-wincrypt-certnametostrw">CertNameToStr</a> Windows API implementation of X.500 rules.</td>
<td>Yes</td>
</tr>
<tr class="even">
<td><strong>ResourceId</strong></td>
<td><p>Describes the type of UI resources contained in the package. The <strong>ResourceId</strong> is a publisher-specified string.</p>
<p>This string cannot end with a period and cannot be one of these strings: &quot;CON&quot;, &quot;PRN&quot;, &quot;AUX&quot;, &quot;NUL&quot;, &quot;COM1&quot;, &quot;COM2&quot;, &quot;COM3&quot;, &quot;COM4&quot;, &quot;COM5&quot;, &quot;COM6&quot;, &quot;COM7&quot;, &quot;COM8&quot;, &quot;COM9&quot;, &quot;LPT1&quot;, &quot;LPT2&quot;, &quot;LPT3&quot;, &quot;LPT4&quot;, &quot;LPT5&quot;, &quot;LPT6&quot;, &quot;LPT7&quot;, &quot;LPT8&quot;, and &quot;LPT9&quot;.</p></td>
<td>An ASCII string between 1 and 30 characters in length.</td>
<td>No</td>
</tr>
<tr class="odd">
<td><strong>Version</strong></td>
<td><p>The version number of the package.</p></td>
<td>A version string in quad notation, &quot;Major.Minor.Build.Revision&quot; where Major cannot be "0".</td>
<td>Yes</td>
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
<td><a href="element-package.md">Package</a> </td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
</tbody>
</table>

### Example
This example is from the app manifest file of the [App package information](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/Package) sample on GitHub.

```xml
  <Identity Name="Microsoft.SDKSamples.PackageSample.CS" 
            Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" 
            Version="1.0.1.0" />
```
 

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |


 

 



