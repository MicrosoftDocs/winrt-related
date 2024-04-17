---
title: s4:Package
description: Specifies the information about a package, including name, publisher, version and uri. (s4:Package)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:Package



## Description

Specifies the information about a package, including name, publisher, version and uri. (s4:Package)

*ProcessorArchitecture* and *ResourceId** are optional attributes of the **Package**.

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s4:OptionalPackages](element-s4-optionalpackages.md);

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s4:Package&gt;

&nbsp;&nbsp;&nbsp;&nbsp; [s4:RelatedPackages](element-s4-relatedpackages.md);

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s4:Package&gt;

&nbsp;&nbsp;&nbsp;&nbsp; [s4:Dependencies](element-s4-dependencies.md);

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s4:Package&gt;



## Syntax

```syntax
<s4:Package     Name = A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
    Publisher = A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.
    Version = A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".
    Uri = Web URI as a string between 1 and 2084 characters in length.
    ProcessorArchitecture? = "x86" | "x64" | "arm" | "arm64" | "neutral"
    ResourceId? = An ASCII string between 1 and 30 characters in length.
></s4:Package>
```

## Key

`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Name | The package name as specified in the identity element in the package manifest. The *Name* attribute is case-insensitive. | A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.| Yes |
| Publisher | The publisher, as specified in the identity element in the package manifest. | A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.| Yes |
| Version | The version, as specified in the identity element in the package manifest. | A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".| Yes |
| Uri | The Uri to the app package location. | Web URI as a string between 1 and 2084 characters in length.| Yes |
| ProcessorArchitecture | Describes the architecture of the code contained in the package. A package that includes executable code must include this attribute. | One of the following values: "x86" , "x64" , "arm" , "arm64" , "neutral"| No |
| ResourceId | Describes the type of UI resources contained in the package. The **ResourceId** is a publisher-specified string. This string cannot end with a period and cannot be one of these strings: "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", and "LPT9". | An ASCII string between 1 and 30 characters in length.| No |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:OptionalPackages](element-s4-optionalpackages.md) | Specifies the optional packages that will be installed along with the main package. |
| [s4:RelatedPackages](element-s4-relatedpackages.md) | Specifies the related packages. These packages won't be installed as part of the deployment operation. |
| [s4:Dependencies](element-s4-dependencies.md) | These are dependencies that will be installed if required. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows version 21H2 build 22000 |
