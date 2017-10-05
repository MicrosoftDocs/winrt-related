---
author: laurenhughes
ms.author: lahugh
title: AppInstaller
description: Defines the root element of an appinstaller file.
ms.topic: reference
ms.date: 10/10/2017
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# AppInstaller

Defines the root element of an appinstaller file. The file describes the structure and defines the packages that will be installed as part of the deployment operation. 

## Element hierarchy

<b>&lt;AppInstaller&gt;</b>

## Syntax
```syntax
<AppInstaller 
    xmlns="http://schemas.microsoft.com/appx/appinstaller/2017"
    Version= A version string in quad notation, "Major.Minor.Build.Revision".
    Uri= Web Uri to the redirected appinstaller file >

  <!-- Child elements -->
  ( MainPackage
  & MainBundle?
  & Dependencies?
  & OptionalPackages?
  & RelatedPackages?
  & UpdateSettings?
  )

</AppInstaller>
```

### Key
`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| xmlns | The namespace definition of the appinstaller schema | URI as a string between 1 and 2084 characters in length. |  Yes |
| Version | The version of appinstaller file |   A version string in quad notation, "Major.Minor.Build.Revision". | Yes |
| Uri | Web URI to the redirected appinstaller file. When the Uri specified in the field differs from the current file, the deployment operation will redirect to the Uri instead of the current file. The appinstaller file can only be redirected a max of three times. | Web URI as a string between 1 and 2084 characters in length.| Yes |


### Child Elements

| Child Elements | Description |
|----------------|-------------|
| [MainPackage](element-main-package.md) | Specifies the main package that will be installed. |
| [MainBundle](element-main-bundle.md) | Specifies the main bundle that will be installed. |
| [OptionalPackages](element-optional-packages.md) | Specifies the optional pacakges. |
| [RelatedPackages](element-related-packages.md) | Specifies the related packages. These packages won't be installed. |
| [Dependencies](element-dependencies.md) | These are dependencies that will be installed if required. |
| [UpdateSettings](element-update-settings.md) | Use the updatesettings element to toggle auto update of installed packages. |

### Parent Elements

This outermost element may not be contained by any other elements.

## Remarks
`<AppInstaller>` can have either a `<MainPackage>` or `<MainBundle>` element. The deployment operation will fail if more than one of either are included.

## Requirements
<table>
    <tbody>
        <tr>
            <td>Namespace</td>
            <td> http://schemas.microsoft.com/appx/appinstaller/2017 </td>
        </tr>
    </tbody>
</table>