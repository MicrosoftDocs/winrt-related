---
title: s2:AppInstaller
description: Defines the root element of an AppInstaller file. (s2:AppInstaller)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:AppInstaller



## Description

Defines the root element of an AppInstaller file. (s2:AppInstaller)

## Element Hierarchy

&lt;s2:AppInstaller&gt;

## Syntax
```syntax
<s2:AppInstaller     Uri = Web URI as a string between 1 and 2084 characters in length.
    Version = A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".
    IgnorableNamespaces? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
>
<!-- Child elements -->
  ( s4:UpdateUris?
  & s4:RepairUris?
  & MainPackage?
  & MainBundle?
  & OptionalPackages?
  & RelatedPackages?
  & Dependencies?
  & UpdateSettings?)
</s2:AppInstaller>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Uri | Web URI to the redirected App Installer file. When the Uri specified in the field differs from the current file, the deployment operation will redirect to the Uri instead of the current file. The App Installer file can only be redirected a max of three times. Query strings with multiple key/value pairs are currently not supported. | Web URI as a string between 1 and 2084 characters in length. | Web URI as a string between 1 and 2084 characters in length.| Yes |
| Version | The version of App Installer file. | A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".| Yes |
| IgnorableNamespaces | Declares namespaces used in the app installer file that should be ignored. Ignored namespace elements are not validated and should be considered untrusted. Multiple namespaces are specified with a space between each namespace. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| No |


## Child Elements

| Element | Description |
| -----------| -------------|
| [s4:UpdateUris](element-s4-updateuris.md) | Specifies a list of Uris pointing to App Installer files for updating an installation. |
| [s4:RepairUris](element-s4-repairuris.md) | Specifies a list of Uris pointing to App Installer files for repairing an installation. |
| [s2:MainPackage](element-s2-mainpackage.md) | Specifies the information about the main package which includes name, publisher, version and uri.  |
| [s2:MainBundle](element-s2-mainbundle.md) | Specifies the information about the main bundle package. |
| [s2:OptionalPackages](element-s2-optionalpackages.md) | Specifies the optional packages that will be installed along with the main package. |
| [s2:RelatedPackages](element-s2-relatedpackages.md) | Specifies the related packages. These packages won't be installed as part of the deployment operation. |
| [s2:Dependencies](element-s2-dependencies.md) | These are dependencies that will be installed if required. |
| [s2:UpdateSettings](element-s2-updatesettings.md) | Toggles the auto update setting of installed packages. |

## Remarks

`<AppInstaller>` can have either a `<MainPackage>` or `<MainBundle>` element. The deployment operation will fail if more than one of either are included.
Only `encoding="UTF-8"` with no escape characters, and no non-ascii characters is accepted.

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s2) | `http://schemas.microsoft.com/appx/appinstaller/2017/2` |
| Namespace (s4) | `http://schemas.microsoft.com/appx/appinstaller/2021` |
| Minimum OS version | Windows 10 version 1803 build 17134 |
