---

title: App Installer file (.appinstaller) reference
description: This reference provides details for each element, attribute, and data type that defines the schema for appinstaller file that defines the packages that are part of a related set. 

ms.date: 1/4/2018
ms.topic: reference


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---


# App Installer file (.appinstaller) schema reference

This reference provides details for each element, attribute, and data type that defines the schema for an .appinstaller file that defines the packages that are part of a related set. 

The following table lists all of the elements in this schema.


| Element | Description |
|---------|-------------|
| [AppInstaller](element-appinstaller.md) | The root element of the appinstaller document. |
| [Bundle](element-bundle.md)| Element that includes information about the app bundle. The child elements of this element requires an exact match of the name, publisher and version from the identity element in the app package bundle manifest.  |
| [Dependencies](element-dependencies.md) | These are dependencies that will be installed if required. |
| [MainBundle](element-main-bundle.md)| Element that includes information about the main bundle that will installed. The child elements of this element requires an exact match of the name, publisher and version from the identity element in the app package bundle manifest. |
| [MainPackage](element-main-package.md)| Element that includes information about the main package that will installed. The child elements of this element requires an exact match of the name, publisher and version from the identity element in the app package manifest. ProcessorArchitecture is an optional element.  |
| [OptionalPackages](element-optional-packages.md) | Specifies the optional packages. |
| [Package](element-package.md)| Element that includes information about the  package. This elements requires an exact match of the name, publisher and version from the identity element in the app package manifest. ProcessorArchitecture is an optional element.  |
| [RelatedPackages](element-related-packages.md) | Specifies the related packages. These packages won't be installed. |
| [UpdateSettings](element-update-settings.md) | Use the UpdateSettings element to toggle auto update of installed packages and set an interval for update checks. |
| [OnLaunch](element-onlaunch.md)  |  Signifies that the deployment service will check for an update to the appinstaller file on the app launch. |
| [s4:AutomaticBackgroundTask](element-s4-automaticbackgroundtask.md)  | Checks for updates in the background. A check is made every 8 hours independently of whether the user launched the app. This type of update cannot show UI.  |
| [s4:ForceUpdateFromAnyVersion](element-s4-forceupdatefromanyversion.md)  | A boolean that allows the app's version to be incremented or decremented. Without this element, the app can only move to a higher version.  |
| [s4:MainPackageType](element-s4-mainpackagetype.md)  | Checks for updates in the background. A check is made every 8 hours independently of whether the user launched the app. This type of update cannot show UI.  |
| [s4:RepairUris](element-s4-repairuris.md)  | A boolean that allows the app's version to be incremented or decremented. Without this element, the app can only move to a higher version.  |
| [s4:RepairUri](element-s4-repairuri.md)  | A boolean that allows the app's version to be incremented or decremented. Without this element, the app can only move to a higher version.  |
| [s4:UpdateUris](element-s4-updateuris.md)  | A boolean that allows the app's version to be incremented or decremented. Without this element, the app can only move to a higher version.  |
| [s4:UpdateUri](element-s4-updateuri.md)  | A boolean that allows the app's version to be incremented or decremented. Without this element, the app can only move to a higher version.  |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns=http://schemas.microsoft.com/appx/appinstaller/2017/2` | This namespace is required for features introduced in Windows 10, version 1803. |
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows 10 version 1803 build 17134 |
