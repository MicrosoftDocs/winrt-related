---
title: s2:MainPackage
description: Specifies the information about the main package which includes name, publisher, version and uri. ProcessorArchitecture and ResourceId are optional attributes of the MainPackage. (s2:MainPackage)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:MainPackage

## Description

Specifies the information about the main package which includes name, publisher, version and uri. ProcessorArchitecture and ResourceId are optional attributes of the MainPackage. (s2:MainPackage)

## Element Hierarchy

[s2:AppInstaller](element-s2-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s2:MainPackage&gt;

## Syntax
```syntax
<s2:MainPackage     Name = A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
    Publisher = A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.
    Version = A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".
    Uri = Web URI as a string between 1 and 2084 characters in length.
    ProcessorArchitecture? = "x86" | "x64" | "arm" | "arm64" | "neutral"
    ResourceId? = An ASCII string between 1 and 30 characters in length.
></s2:MainPackage>
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
| [s2:AppInstaller](element-s2-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s2) | `http://schemas.microsoft.com/appx/appinstaller/2017/2` |
| Minimum OS version | Windows 10 version 1803 build 17134 |
