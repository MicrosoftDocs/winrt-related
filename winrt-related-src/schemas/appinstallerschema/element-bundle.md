---
author: laurenhughes
ms.author: lahugh
title: Bundle
description: The Bundle element specifies the information about the bundle package. 
ms.topic: reference
ms.date: 10/10/2017


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# Bundle

The Bundle element specifies the information about the bundle package. 

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt><a href="element-optional-packages.md">&lt;OptionalPackages&gt;</a></dt>
            <dd><b>&lt;Bundle&gt;</b></dd>
    </dl>
    <dl>
        <dt><a href="element-related-packages.md">&lt;RelatedPackages&gt;</a></dt>
            <dd><b>&lt;Bundle&gt;</b></dd>
    </dl>
    <dl>
        <dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
            <dd><b>&lt;Bundle&gt;</b></dd>
    </dl>
</dd>
</dl>

## Syntax
``` xml
<Bundle 
    Name        = A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
    Publisher   = A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name: "(CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")(, ((CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.
    Version     = A version string in quad notation, "Major.Minor.Build.Revision".
    Uri         = Uri to the app package location />

```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name          |   Name as specified in the identity element in the bundle manifest. The Name attribute is case-insensitive.   | A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.        |  Yes        |
| Publisher    |   Publisher as specified in the identity element in the bundle manifest.     |   A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name. Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.    |   Yes |
| Version   |  Version as specified in the identity element in the bundle manifest.  |     A version string in quad notation, "Major.Minor.Build.Revision". |   Yes |
| Uri          | Uri to the app package location   |  URI as a string between 1 and 2084 characters in length.      |  Yes        |

### Parent Elements

| Parent Elements | Description |
|----------------|-------------|
| [OptionalPackages](element-optional-packages.md)           | Specifies the optional pacakges               |
| [RelatedPackages](element-related-packages.md)           | Specifies the related packages. These packages won't be installed.             |
| [Dependencies](element-dependencies.md)           | These are dependencies that will be installed if required.            |

## Requirements
<table>
    <tbody>
        <tr>
            <td>Namespace</td>
            <td> http://schemas.microsoft.com/appx/appinstaller/2017 </td>
        </tr>
    </tbody>
</table>