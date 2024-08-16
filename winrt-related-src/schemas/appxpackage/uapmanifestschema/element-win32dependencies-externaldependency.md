---
description: Specifies an external dependency that is not included in the MSIX but will be chain installed as part of the app installation. 
Search.Product: eADQiWindows 10XVcnh
title: win32dependencies:ExternalDependency (Windows 10, Windows 11)
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/26/2021
---

# win32dependencies:ExternalDependency (Windows 10, Windows 11)

Specifies an external dependency that is not included in the MSIX but will be chain installed as part of the app installation. If the specified minimum version of the external dependency is not already installed on the OS, the Microsoft App Installer app will retrieve the minimum version from an external repository and install the dependency. Microsoft maintains a list of dependencies that can be installed using this method. See the [Remarks](#remarks) section for the current list of allowed packages.

> [!IMPORTANT]
> **win32dependencies:ExternalDependency** only applies to installations that use the Microsoft App Installer app. If a package is installed using any other mechanism, such as the [PackageManager](/uwp/api/windows.management.deployment.packagemanager) API, a Powershell cmdlet, Intune or any other mechanism other than via the App Installer app, then **win32dependencies:ExternalDependency** is ignored.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Dependencies\>]

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<win32dependencies:ExternalDependency\>**

## Syntax

```xml
<win32dependencies:ExternalDependency
    Name = 'A string between 3 and 50 characters in length that consists of alpha-numeric characters, periods, and dashes only.' 
    Publisher = 'A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.'
    MinVersion = 'A version string in quad notation, ("Major.Minor.Build.Revision") where "Major" is not "0".'
    Optional = 'A boolean value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The dependency package name. For the list of allowed dependency packages, see the Remarks section below. | A string between 3 and 50 characters in length that consists of alpha-numeric characters, periods, and dashes only. | Yes |  |
| **Publisher** | The publisher of the dependency package. | A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name. | Yes |  |
| **MinVersion**  | The minimum version of the external dependency. If the OS already has the minimum version installed, the installation will not be triggered. | A version string in quad notation, (`Major.Minor.Build.Revision`) where `Major` is not `0`. | Yes |  |
| **Optional**  | When the installation is performed without an internet connection and this value is false, the installation will complete without installing the external dependency. If this value is true, an installation with no internet connection will fail. | A boolean value. | Yes |  |

### Child elements

None.

### Parent elements

| Parent Element | Description |
|-|-|
| [Dependencies](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Examples

```xml
<Package
    xmlns:win32dependencies="http://schemas.microsoft.com/appx/manifest/externaldependencies"  
    IgnorableNamespaces="... win32dependencies">
    <Dependencies>  
        <TargetDeviceFamily
            Name="Windows.Universal"
            MinVersion="11.0.0.0" 
            MaxVersionTested="12.0.0.0"/>  
        <uap4:MainPackageDependency
            Name="MyApp"
            Publisher="CN=DianCert, O=Contoso Corporation, C=US" />  
        <win32dependencies:ExternalDependency
            Name="Microsoft.WebView2"
            Publisher="CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
            MinVersion="1.1.1.1"
            Optional="true"/>
    </Dependencies>  
</Package>
```

## Remarks

This feature requires that Microsoft App Installer version 1.16.12651.0 or later be installed on the target machine. The app can be obtained from the [Microsoft Store](https://www.microsoft.com/en-us/store/apps/windows).

### Allowed external dependencies

The following table lists the external dependencies that are currently allowed in the **ExternalDependency** element.

| Package | Name attribute value | Publisher attribute value |
|-|-|-|
| **Webview2** | "Microsoft.WebView2" | "CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" |

## Requirements

| Item | Value |
|--|--|
| virtualization | `http://schemas.microsoft.com/appx/manifest/externaldependencies` |
