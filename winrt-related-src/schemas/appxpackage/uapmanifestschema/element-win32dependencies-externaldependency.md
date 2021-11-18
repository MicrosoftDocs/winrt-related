---
description: Specifies an external dependency that is not included in the MSIX but will be chain installed as part of the app installation. 
Search.Product: eADQiWindows 10XVcnh
title: win32dependencies:ExternalDependency (Windows 10, Windows 11)



keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 10/26/2021
---

# win32dependencies:ExternalDependency (Windows 10, Windows 11)


Specifies an external dependency that is not included in the MSIX but will be chain installed as part of the app installation. If the specified minimum version of the external dependency is not already installed on the OS, the Microsoft App Installer app will retrieve the minimum version from an external repository and install the dependency. Microsoft maintains a list of dependencies that can be installed using this method. See the remarks section for the current list of allowed packages.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;win32dependencies:ExternalDependency&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax


```
<win32dependencies:ExternalDependency Name = A string between 3 and 50 characters in
                                   length that consists of alpha-numeric, 
                                   period, and dash characters. 
                            Publisher = A string between 1 and 8192 characters in length that fits the regular expression  of a distinguished name : "(CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+="<>#;])+ | ".*")(, ((CN | L | O | OU | E | C | S | STREET | T | G | I | SN | DC | SERIALNUMBER | Description | PostalCode | POBox | Phone | X21Address | dnQualifier | (OID\.(0 | [1-9][0-9]*)(\.(0 | [1-9][0-9]*))+))=(([^,+="<>#;])+ | ".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.
                            MinVersion = A version string in quad notation, "Major.Minor.Build.Revision".
                            Optional = boolean>
</win32dependencies:ExternalDependency>
```

## Attributes and Elements


**Attributes**

| Attribute | Description                                                                                                                     | Data type                                                                                                   | Required | Default value |
|-----------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------|---------------|
| **Name**  | The dependency package name. For the list of allowed dependency packages, see TBD. | A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters. | Yes      |               |
| **Publisher**  | The publisher of the dependency package. |  A string between 1 and 8192 characters in length that fits the regular expression  of a distinguished name : "(CN \| L \| O \| OU \| E \| C \| S \| STREET \| T \| G \| I \| SN \| DC \| SERIALNUMBER \| Description \| PostalCode \| POBox \| Phone \| X21Address \| dnQualifier \| (OID\.(0 \| [1-9][0-9]*)(\.(0 \| [1-9][0-9]*))+))=(([^,+="<>#;])+ \| ".*")(, ((CN \| L \| O \| OU \| E \| C \| S \| STREET \| T \| G \| I \| SN \| DC \| SERIALNUMBER \| Description \| PostalCode \| POBox \| Phone \| X21Address \| dnQualifier \| (OID\.(0 \| [1-9][0-9]*)(\.(0 \| [1-9][0-9]*))+))=(([^,+="<>#;])+ \| ".*")))*". Further, semantic validation ensures that the string is compliant with CertNameToStr Windows API implementation of X.500 rules.  | Yes      |               |
| **MinVersion**  | The minimum version of the external dependency. If the OS already has the minimum version installed, the installation will not be triggered. | A version string in quad notation, "Major.Minor.Build.Revision". | Yes      |               |
| **Optional**  | When the installation is performed without an internet connection and this value is false, the installation will complete without installing the external dependency. If this value is true, an installation with no internet connection will fail. | A version string in quad notation, "Major.Minor.Build.Revision". | Yes      |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                               | Description                                                                 |
|----------------------------------------------|-----------------------------------------------------------------------------|
| [**Dependencies**](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |

 

## Examples


```XML
<Package ...
         xmlns:win32dependencies="http://schemas.microsoft.com/appx/manifest/externaldependencies"  
         IgnorableNamespaces="... win32dependencies">
    <Dependencies>  
        <TargetDeviceFamily Name="Windows.Universal" MinVersion="11.0.0.0" 
                            MaxVersionTested="12.0.0.0"/>  
        
        <uap4:MainPackageDependency Name="MyApp" Publisher="CN=DianCert, O=Contoso Corporation, C=US" />  
        <win32dependencies:ExternalDependency Name="Microsoft.WebView2" Publisher="CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" MinVersion="1.1.1.1" Optional="true"/>
    </Dependencies>  
</Package>
```

## Remarks

This feature requires that the latest version of the Microsoft App Installer app be installed on the target machine. The app can be obtained from the [Microsoft Store](https://www.microsoft.com/en-us/store/apps/windows).

## Requirements


|     Namespace | Value                                                       |
|---------------|-------------------------------------------------------------|
| win32dependencies | "http://schemas.microsoft.com/appx/manifest/externaldependencies" |

 

 

 



