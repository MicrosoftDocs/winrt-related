---
title: uap13:HostRuntimeDependency
description: Declares publisher information for the app.
keywords: windows 10, uwp, schema, manifest, extension

ms.date: 05/03/2022
ms.topic: reference
---

# uap13:HostRuntimeDependency

## Description

Declares publisher information for the app.

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><strong>&lt;uap13:HostRuntimeDependency&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` XML
<uap13:HostRuntimeDependency
  Name = An alphanumeric string value between 1 and 32767 characters that may also contain the following characters: "." and "-".
  Publisher = A string between 1 and 8192 characters in length that fits the regular expression  of a distinguished name: "(CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+="<>#;])+ | ".*")(, ((CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+="<>#;])+ | ".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.
  MinVersion = A version string in quad notation, "Major.Minor.Build.Revision".
  >

</uap13:HostRuntimeDependency>
```

## Attributes & Elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|:-:|
| Name | The name of the application. | An alphanumeric string value between 1 and 32767 characters that may also contain the following characters: "." and "-". | Yes |
| Publisher | The publisher of the application | A string between 1 and 8192 characters in length that fits the regular expression  of a distinguished name. Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules. | Yes |
| MinVersion | The minimum Windows version required to install the application. | A version string in quad notation, e.g. "Major.Minor.Build.Revision". | Yes |

### Child Elements

**None.**

### Parent Elements

| Parent Element | Description |
|-|-|
| [Extension (in Package/Applications)](element-extension.md) | Declares an extensibility point for the app. |

### Requirements

| Namespace | Path |
|-|-|
| **UAP12** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/13` |