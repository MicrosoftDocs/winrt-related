---
description: Defines a dependency on a host app package for the current app package.
title: uap10:HostRuntimeDependency
keywords: windows 10, uwp, schema, package manifest, host app, hosted app
ms.topic: reference
ms.date: 04/20/2020
---

# uap10:HostRuntimeDependency

Defines a dependency on a host app for the current app. For more information, see [Create hosted apps](/windows/uwp/launch-resume/hosted-apps).

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;uuap10:HostRuntimeDependency&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<uap10:HostRuntimeDependency Name       = An alphanumeric string. May contain period and dash characters.
                             Publisher  =  A string between 1 and 8192 characters in length that fits the regular expression  of a distinguished name : "(CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+="<>#;])+ | ".*")(, ((CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+="<>#;])+ | ".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.
                             MinVersion = A version string in quad notation, "Major.Minor.Build.Revision".  />
```

## Attributes and Elements
### Attributes

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
<td><strong>Name</strong></td>
<td>The name of the host app.</td>
<td>An alphanumeric string. May contain period and dash characters./td>
<td>Yes</td>
</tr>
<tr class="odd">
<td><strong>Publisher</strong></td>
<td><p>The publisher of the host app.</p></td>
<td>A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name : &quot;(CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+ | &quot;.*&quot;)(, ((CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+ | &quot;.*&quot;)))*&quot;. Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.</td>
<td>Yes</td>
</tr>
<tr class="even">
<td><strong>MinVersion</strong></td>
<td>The minimum version of the host app that the current app depends on.</td>
<td>A version string in quad notation, "Major.Minor.Build.Revision". </td>
<td>Yes</td>
</tr>
</tbody>
</table>

### Child Elements

None

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
