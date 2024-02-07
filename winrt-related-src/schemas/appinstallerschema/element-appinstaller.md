---


title: AppInstaller
description: Defines the root element of an appinstaller file.
ms.topic: reference
ms.date: 04/03/2017


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# AppInstaller

This element defines the root element of an appinstaller file. The appinstaller file describes the structure and defines the packages that will be installed as part of the deployment operation. 

## Element hierarchy

<b>&lt;AppInstaller&gt;</b>

## Syntax
``` xml

<?xml version="1.0" encoding="UTF-8"?>

<AppInstaller 
    xmlns="http://schemas.microsoft.com/appx/appinstaller/2017/2"
    Version= A version string in quad notation, "Major.Minor.Build.Revision".
    Uri= Web Uri to the redirected appinstaller file >

  <!-- Child elements -->
  ( MainPackage
  & MainBundle?
  & Dependencies?
  & OptionalPackages?
  & RelatedPackages?
  & UpdateSettings?
  & s4:UpdateUris?
  & s4:RepairUris?
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
| xmlns | The namespace definition of the appinstaller schema. For a list of the namespaces, see the [Requirements](#requirements) section in this article. | URI as a string between 1 and 2084 characters in length. |  Yes |
| Version | The version of appinstaller file |   A version string in quad notation, "Major.Minor.Build.Revision". | Yes |
| Uri | Web URI to the redirected appinstaller file. When the Uri specified in the field differs from the current file, the deployment operation will redirect to the Uri instead of the current file. The appinstaller file can only be redirected a max of three times. Query strings with multiple key/value pairs are currently not supported. | Web URI as a string between 1 and 2084 characters in length.| Yes |


### Child Elements

Child elements must appear in the specified order

| Child Elements | Description |
|----------------|-------------|
| [MainPackage](element-main-package.md) | Specifies the main package that will be installed. |
| [MainBundle](element-main-bundle.md) | Specifies the main bundle that will be installed. |
| [OptionalPackages](element-optional-packages.md) | Specifies the optional packages. |
| [RelatedPackages](element-related-packages.md) | Specifies the related packages. These packages won't be installed. |
| [Dependencies](element-dependencies.md) | These are dependencies that will be installed if required. |
| [UpdateSettings](element-update-settings.md) | Use the updatesettings element to toggle auto update of installed packages. |
| [s4:UpdateUris](element-s4-updateuris.md) | Specifies a list of Uris pointing to App Installer files for updating an installation. |
| [s4:RepairUris](element-s4-repairuris.md) | Specifies a list of Uris pointing to App Installer files for repairing an installation. |

### Parent Elements

This outermost element may not be contained by any other elements.

## Remarks

`<AppInstaller>` can have either a `<MainPackage>` or `<MainBundle>` element. The deployment operation will fail if more than one of either are included.
Only `encoding="UTF-8"` with no escape characters, and no non-ascii characters is accepted.

## Requirements

| Namespace | Description |
|----------------|-------------|
| `http://schemas.microsoft.com/appx/appinstaller/2018` | This namespace is required for features introduced in Windows 10, version 1809. |
| `http://schemas.microsoft.com/appx/appinstaller/2017/2` | This namespace is required for features introduced in Windows 10, version 1803. |
| `http://schemas.microsoft.com/appx/appinstaller/2017` | This namespace is required for features introduced in Windows 10, version 1709. |
