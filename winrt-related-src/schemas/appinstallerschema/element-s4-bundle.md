---
title: s4:Bundle
description: Specifies the information about the bundle package. (s4:Bundle)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:Bundle

## Description

Specifies the information about the bundle package. (s4:Bundle)

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s4:OptionalPackages](element-s4-optionalpackages.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s4:Bundle&gt;

&nbsp;&nbsp;&nbsp;&nbsp; [s4:RelatedPackages](element-s4-relatedpackages.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s4:Bundle&gt;

&nbsp;&nbsp;&nbsp;&nbsp; [s4:Dependencies](element-s4-dependencies.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s4:Bundle&gt;

## Syntax

```syntax
<s4:Bundle     Name = A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
    Publisher = A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.
    Version = A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".
    Uri = Web URI as a string between 1 and 2084 characters in length.
></s4:Bundle>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Name | The bundle name, as specified in the identity element in the bundle manifest. The *Name* attribute is case-insensitive. | A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.| Yes |
| Publisher | The publisher, as specified in the identity element in the bundle manifest. | A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.| Yes |
| Version | The version, as specified in the identity element in the bundle manifest. | A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".| Yes |
| Uri | Uri to the app package location. | Web URI as a string between 1 and 2084 characters in length. | Yes |


## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:OptionalPackages](element-s4-optionalpackages.md) | Specifies the optional packages that will be installed along with the main package. |
| [s4:RelatedPackages](element-s4-relatedpackages.md) | Specifies the related packages. These packages won't be installed as part of the deployment operation. |
| [s4:Dependencies](element-s4-dependencies.md) | These are dependencies that will be installed if required. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s4) | `http://schemas.microsoft.com/appx/appinstaller/2021` |
| Minimum OS version | Windows version 21H2 build 22000 |
