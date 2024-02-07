---
title: s2:MainBundle
description: Specifies the information about the main bundle package. (s2:MainBundle)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:MainBundle

## Description

Specifies the information about the main bundle package. (s2:MainBundle)

## Element Hierarchy

[s2:AppInstaller](element-s2-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s2:MainBundle&gt;

## Syntax
```syntax
<s2:MainBundle     Name = A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
    Publisher = A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.
    Version = A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".
    Uri = Web URI as a string between 1 and 2084 characters in length.
></s2:MainBundle>
```

## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Name | The bundle name, as specified in the identity element in the bundle manifest. The *Name* attribute is case-insensitive. | A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.| Yes |
| Publisher | The publisher, as specified in the identity element in the bundle manifest.  | A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.| Yes |
| Version | The version, as specified in the identity element in the bundle manifest. | A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".| Yes |
| Uri | Uri to the app package location. | Web URI as a string between 1 and 2084 characters in length.| Yes |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s2:AppInstaller](element-s2-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s2) | `http://schemas.microsoft.com/appx/appinstaller/2017/2` |
| Minimum OS version | Windows 10 version 1803 build 17134 |
