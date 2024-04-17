---


title: Package (App installer schema)
description: The Package element specifies the information about the package which includes name, publisher, version and uri. ProcessorArchitecture is an optional attribute of the Package.
ms.topic: reference
ms.date: 10/10/2017


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# Package (App installer schema)

The Package element specifies the information about the package which includes name, publisher, version and uri. ProcessorArchitecture is an optional attribute of the Package. 

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt><a href="element-optional-packages.md">&lt;OptionalPackages&gt;</a></dt>
            <dd><b>&lt;Package&gt;</b></dd>
    </dl>
    <dl>
        <dt><a href="element-related-packages.md">&lt;RelatedPackages&gt;</a></dt>
            <dd><b>&lt;Package&gt;</b></dd>
    </dl>
    <dl>
        <dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
            <dd><b>&lt;Package&gt;</b></dd>
    </dl>
</dd>
</dl>

## Syntax
``` xml
<Package 
    Name                    = A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
    Publisher               = A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name : "(CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")(, ((CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.
    Version                 = A version string in quad notation, "Major.Minor.Build.Revision".
    ProcessorArchitecture?  = "x86" | "x64" | "arm" | "neutral"
    Uri                     = Uri to the app package location />

```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name          |   Name as specified in the identity element in the Package manifest. The Name attribute is case-insensitive.   | A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.        |  Yes        |
| Publisher    |   Publisher as specified in the identity element in the Package manifest.     |   A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name. Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.   |   Yes |
| Version   |  Version as specified in the identity element in the Package manifest.  |     A version string in quad notation, "Major.Minor.Build.Revision". |   Yes |
| ProcessorArchitecture | Describes the architecture of the code contained in the package. A package that includes executable code must include this attribute. | "x86" or "x64"or "arm" or "neutral" | No |
| Uri          | Uri to the app package location   |  URI       |  Yes        |

### Parent Elements

| Parent Elements | Description |
|----------------|-------------|
| [OptionalPackages](element-optional-packages.md)           | Specifies the optional pacakges               |
| [RelatedPackages](element-related-packages.md)           | Specifies the related packages. These packages won't be installed.             |
| [Dependencies](element-dependencies.md)           | These are dependencies that will be installed if required.            |

## Requirements

| Requirement | Description |
|----------------|-------------|
| `xmlns=http://schemas.microsoft.com/appx/appinstaller/2017` | This namespace is required for features introduced in Windows 10, version 1709. |
| Minimum OS version | Windows 10, version 1709 |