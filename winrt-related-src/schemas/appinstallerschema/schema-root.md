---
author: laurenhughes
title: App Installer file (.appinstaller) reference
description: This reference provides details for each element, attribute, and data type that defines the schema for appinstaller file that defines the packages that are part of a related set. 
ms.author: lahugh
ms.date: 1/4/2018
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
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
| [OptionalPackages](element-optional-packages.md) | Specifies the optional pacakges. |
| [Package](element-package.md)| Element that includes information about the  package. This elements requires an exact match of the name, publisher and version from the identity element in the app package manifest. ProcessorArchitecture is an optional element.  |
| [RelatedPackages](element-related-packages.md) | Specifies the related packages. These packages won't be installed. |
| [UpdateSettings](element-update-settings.md) | Use the UpdateSettings element to toggle auto update of installed packages and set an interval for update checks. |
