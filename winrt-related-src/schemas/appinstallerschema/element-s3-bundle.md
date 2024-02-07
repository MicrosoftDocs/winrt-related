---
title: s3:Bundle
description: Specifies the information about the bundle package. (s3:Bundle)
ms.date: 02/05/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s3:Bundle

## Description

Specifies the information about the bundle package. (s3:Bundle)


## Element Hierarchy

[s3:AppInstaller](element-s3-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s3:OptionalPackages](element-s3-optionalpackages.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s3:Bundle&gt;

&nbsp;&nbsp;&nbsp;&nbsp; [s3:RelatedPackages](element-s3-relatedpackages.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s3:Bundle&gt;

&nbsp;&nbsp;&nbsp;&nbsp; [s3:Dependencies](element-s3-dependencies.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s3:Bundle&gt;

## Syntax

```syntax
<s3:Bundle     Name = A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
    Publisher = A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.
    Version = A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".
    Uri = Web URI as a string between 1 and 2084 characters in length.
></s3:Bundle>
```

## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Name | The bundle name, as specified in the identity element in the bundle manifest. The *Name* attribute is case-insensitive. | A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.| Yes |
| Publisher | The publisher, as specified in the identity element in the bundle manifest. | A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name. | Yes |
| Version | The version, as specified in the identity element in the bundle manifest. | A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0". | A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".| Yes |
| Uri | Uri to the app package location. | Web URI as a string between 1 and 2084 characters in length.| Yes |


## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s3:OptionalPackages](element-s3-optionalpackages.md) | Specifies the optional packages that will be installed along with the main package. |
| [s3:RelatedPackages](element-s3-relatedpackages.md) | Specifies the related packages. These packages won't be installed as part of the deployment operation. |
| [s3:Dependencies](element-s3-dependencies.md) | These are dependencies that will be installed if required. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s3) | `http://schemas.microsoft.com/appx/appinstaller/2018` |
| Minimum OS version | Windows version 1809 build 17763 |
