---


title: App Installer file
description: An App Installer file is an XML document (*.appinstaller) that contains app package and bundle information for defining the packages that are part of a related set.
ms.topic: reference
ms.date: 10/10/2017


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# App Installer file

## Purpose

An App Installer file is an XML document (*.appinstaller) that contains app package and bundle information for defining the packages that are part of a related set.

## Developer audience

The App Installer file can be created manually or through the use of the AppInstaller file builder available in the [MSIX Toolkit](https://aka.ms/msixtoolkit).

For more information on how to create an App Installer file manually, see [Install a related set using an App Installer file](/windows/uwp/packaging/install-related-set).

## App Installer file versioning

Features are added to the app installer file by adding new schemas. The namespace associated with each new version is unique. The following versions of the schema are currently supported:

| Schema namespace | Introduced in OS Version |
|------------------|--------------------------|
| `xmlns=http://schemas.microsoft.com/appx/appinstaller/2017` | Windows 10, version 1709. |
| `xmlns:s2=http://schemas.microsoft.com/appx/appinstaller/2017/2` | Windows 10, version 1803. |
| `xmlns:s3=http://schemas.microsoft.com/appx/appinstaller/2018` | Windows 10, version 1809. |
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | Windows version 21H2 build 22000 |

Note that earlier versions of the schema may support elements introduced in later schemas using namespace references.

## In this section

-   [App Installer file (.appinstaller) schema reference](schema-root.md)

## Related topics
[App Installer features](/windows/uwp/packaging/appinstaller-root)
