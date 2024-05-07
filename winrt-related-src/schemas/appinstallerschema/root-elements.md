---


title: Element Hierarchy (app installer file schema)
description: The following list summarizes the allowed hierarchies for the App Installer file schema, starting with the outermost element at the top.
ms.topic: reference
ms.date: 10/10/2017


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# Element Hierarchy (app installer file schema)

The following list summarizes the allowed hierarchies for the App Installer file schema, starting with the outermost element at the top.


* [AppInstaller](element-appinstaller.md)
  * [MainBundle](element-main-bundle.md)
  * [MainPackage](element-main-package.md)
  * [OptionalPackages](element-optional-packages.md)  
    * [Bundle](element-bundle.md)  
    * [Package](element-package.md)
  * [RelatedPackages](element-related-packages.md)  
    * [Bundle](element-bundle.md) 
    * [Package](element-package.md)
  * [Dependencies](element-dependencies.md)  
    * [Bundle](element-bundle.md)  
    * [Package](element-package.md)
  * [UpdateSettings](element-update-settings.md)
    * [OnLaunch](element-onlaunch.md)
    * [s4:AutomaticBackgroundTask](element-s4-automaticbackgroundtask.md)
    * [s4:ForceUpdateFromAnyVersion](element-s4-forceupdatefromanyversion.md)
  * [s4:RepairUris](element-s4-repairuris.md)
    * [s4:RepairUri](element-s4-repairuri.md)
  * [s4:UpdateUris](element-s4-updateuris.md)
    * [s4:UpdateUri](element-s4-updateuri.md)

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns=http://schemas.microsoft.com/appx/appinstaller/2017/2` | This namespace is required for features introduced in Windows 10, version 1803. |
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows 10 version 1803 build 17134 |
