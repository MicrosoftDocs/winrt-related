---


title: MainPackage
description: The MainPackage element specifies the information about the package which includes name, publisher, version and uri. ProcessorArchitecture and ResourceId are optional attributes of the MainPackage. 
ms.topic: reference
ms.date: 10/10/2017


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# MainPackage

The MainPackage element specifies the information about the package which includes name, publisher, version and uri. ProcessorArchitecture and ResourceId are optional attributes of the MainPackage. 

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt>**MainPackage**</dt>
    </dl>
</dd>
</dl>

## Syntax
``` xml
<MainPackage 
    Name        = A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
    Publisher   = A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name: "(CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")(, ((CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+="<>#;])+|".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.
    Version     = A version string in quad notation, "Major.Minor.Build.Revision".
    ProcessorArchitecture  = "x86" | "x64" | "arm" | "neutral"
    Uri         = Uri to the app package location 
    ResourceId? = An ASCII string between 1 and 30 characters in length. />
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name          |   Name as specified in the identity element in the bundle manifest. The Name attribute is case-insensitive.   | A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.        |  Yes        |
| Publisher    |   Publisher as specified in the identity element in the bundle manifest.     |   A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name. Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.   |   Yes |
| Version   |  Version as specified in the identity element in the bundle manifest.  |     A version string in quad notation, "Major.Minor.Build.Revision". |   Yes |
| ProcessorArchitecture | Describes the architecture of the code contained in the package. A package that includes executable code must include this attribute. | "x86" or "x64"or "arm" or "neutral" | Yes |
| Uri          | Uri to the app package location   |  URI as a string between 1 and 2084 characters in length. |  Yes        |
| ResourceId   | Describes the type of UI resources contained in the package. The ResourceId is a publisher-specified string. This string cannot end with a period and cannot be one of these strings: "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", and "LPT9". | An ASCII string between 1 and 30 characters in length. | No |

### Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [AppInstaller](element-appinstaller.md) | The root element of the appinstaller document. |

## Remarks
Only one of either `<MainPackage>` or `<MainBundle>` can be declared in the `<AppInstaller>` element. 

The `<MainPackage>` element should only be used for app packages (.appx).

> [!NOTE]
> The Name, Publisher, Version, ProcessorArchitecture, and ResourceId **must** match the values in the AppxManifest.xml file specified in the app package Uri. 

## Requirements
|               |      Object                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/appinstaller/2017` |