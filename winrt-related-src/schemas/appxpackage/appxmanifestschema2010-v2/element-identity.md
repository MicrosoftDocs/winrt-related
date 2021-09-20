---
description: Defines a globally unique identifier for a package (Windows 8.1).
Search.Product: eADQiWindows 10XVcnh
title: Identity (Windows 8.1 extensions schema)
ms.assetid: 45524773-3b61-44ac-a417-cfaac92af0a0


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Identity (extensions schema for Windows 8.1)




Defines a globally unique identifier for a package. A package identity is represented as a tuple of attributes of the package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Identity&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Identity Name                   = A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
          ProcessorArchitecture? = "x86" | "x64" | "arm" | "neutral"
          Publisher              = A string between 1 and 8192 characters in length that fits the regular expression  of a distinguished name : "(CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|Description|PostalCode|POBox|Phone|X21Address|dnQualifier|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")(, ((CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|Description|PostalCode|POBox|Phone|X21Address|dnQualifier|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.

          Version                = A version string in quad notation, "Major.Minor.Build.Revision".
          ResourceId?            = A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters. />
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
<td><strong>Name</strong></td>
<td><p>Describes the contents of the package. The <strong>Name</strong> attribute is case-insensitive.</p>
<p>Use the [<strong>DisplayName</strong>](../appxmanifestschema/element-displayname.md) attribute to display a package name to users.</p>
<p>This string cannot end with a period and cannot be one of these strings: &quot;CON&quot;, &quot;PRN&quot;, &quot;AUX&quot;, &quot;NUL&quot;, &quot;COM1&quot;, &quot;COM2&quot;, &quot;COM3&quot;, &quot;COM4&quot;, &quot;COM5&quot;, &quot;COM6&quot;, &quot;COM7&quot;, &quot;COM8&quot;, &quot;COM9&quot;, &quot;LPT1&quot;, &quot;LPT2&quot;, &quot;LPT3&quot;, &quot;LPT4&quot;, &quot;LPT5&quot;, &quot;LPT6&quot;, &quot;LPT7&quot;, &quot;LPT8&quot;, and &quot;LPT9&quot;.</p></td>
<td>A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ProcessorArchitecture</strong></td>
<td><p>Describes the architecture of the code contained in the package. A package that includes executable code must include this attribute.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>x86</li>
<li>x64</li>
<li>arm</li>
<li>neutral</li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Publisher</strong></td>
<td><p>Describes the publisher information. The <strong>Publisher</strong> attribute must match the publisher subject information of the certificate used to sign a package.  For more information see <a href="/windows/uwp/packaging/index">Packaging apps</a> .</p></td>
<td>A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name : &quot;(CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|Description|PostalCode|POBox|Phone|X21Address|dnQualifier|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+|&quot;.*&quot;)(, ((CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|Description|PostalCode|POBox|Phone|X21Address|dnQualifier|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+|&quot;.*&quot;)))*&quot;. Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ResourceId</strong></td>
<td><p>Describes the type of UI resources contained in the package. The <strong>ResourceId</strong> is a publisher-specified string.</p>
<p>This string cannot end with a period and cannot be one of these strings: &quot;CON&quot;, &quot;PRN&quot;, &quot;AUX&quot;, &quot;NUL&quot;, &quot;COM1&quot;, &quot;COM2&quot;, &quot;COM3&quot;, &quot;COM4&quot;, &quot;COM5&quot;, &quot;COM6&quot;, &quot;COM7&quot;, &quot;COM8&quot;, &quot;COM9&quot;, &quot;LPT1&quot;, &quot;LPT2&quot;, &quot;LPT3&quot;, &quot;LPT4&quot;, &quot;LPT5&quot;, &quot;LPT6&quot;, &quot;LPT7&quot;, &quot;LPT8&quot;, and &quot;LPT9&quot;.</p></td>
<td>A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Version</strong></td>
<td><p>The version number of the package.</p></td>
<td>A version string in quad notation, &quot;Major.Minor.Build.Revision&quot;.</td>
<td>Yes</td>
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
<td><a href="element-package.md">Package</a> </td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **Name** attribute is used by the operating system and developers to identify packages. The **Name** attribute is not intended to be displayed to end users.

When an app is based on different resource packages, the **ResourceId** attribute must be unique across the user account for a given package name. Main package variants based on resource IDs are not allowed to be installed simultaneously. However, multiple simultaneous variants of a resource-only package are allowed. Examples of possible **ResoureId** attributes include:

-   North America
-   Asia
-   European Languages

The **Publisher** attribute is validated against the subject name of the signing certificate when signed packages are opened. If the **Publisher** attribute doesn't exactly match the subject name, the package is invalid. You can construct multiple semantically-equivalent string representations from the subject name that is stored in the certificate. Use these canonicalization rules to match the **Publisher** attribute value to that subject name:

-   Unicode values can be UTF-8 encoded.
-   If the name contains the legacy e-mail component, the [Internationalized Domain Name (IDN)](/windows/win32/intl/handling-internationalized-domain-names--idns) is represented in Unicode form.
-   Object identifiers (OIDs) with X.500 key names must use the X.500 key name (for example, CN, not 2.5.4.3).
-   OIDs without X.500 key names are identified with the "OID." prefix (for example, OID.2.5.4.34).
-   OID key names are separated from their values by an equal sign without extra spaces (for example, CN=JohnSmith).
-   Multiple [relative distinguished name (RDN)](/previous-versions/windows/desktop/ldap/distinguished-names) entries are separated by a comma followed by a space (for example, CN=JohnSmith, O=Contoso).
-   The RDN value has quotes around it only if it contains leading or trailing white space or one of the following characters (for example, CN=" JohnSmith", O="C++ Inc."):

    -   Comma (,)
    -   Plus sign (+)
    -   Equal sign (=)
    -   Inch mark (")
    -   Backslash followed by the letter n (\\n)
    -   Less than sign (&lt;)
    -   Greater than sign (&gt;)
    -   Number sign (\#)
    -   Semicolon (;)

-   The quotation character is an inch mark ("). If the RDN value contains an inch mark, the inch mark must have double quotes ("") in addition to being enclosed in quotes (for example, CN="William ""Bill"" Smith").
-   Multivalued RDN are not allowed (for example, CN=JohnSmith + O=Contoso).

These rules follow the behavior of the [**CertNameToStr**](/windows/win32/api/wincrypt/nf-wincrypt-certnametostra) function, which can be used to determine the expected **Publisher** attribute value from a certificate.

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```XML
<Identity Name="Microsoft.SDKSamples.ApplicationDataSample" 
          Version="1.0.0.0" 
          Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" />
```

## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
