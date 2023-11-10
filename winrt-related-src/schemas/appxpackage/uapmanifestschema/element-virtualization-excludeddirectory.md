---
description: Specifies a directory that is excluded from file system virtualization.
title: virtualization:ExcludedDirectory
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/18/2022
ms.custom: 
---

# virtualization:ExcludedDirectory

Specifies a directory that is excluded from file system virtualization. 

> [!NOTE]
> This element requires the  **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<virtualization:FileSystemWriteVirtualization\>](element-virtualization-filesystemwritevirtualization.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<virtualization:ExcludedDirectories\>](element-virtualization-excludeddirectories.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<virtualization:ExcludedDirectory\>**

## Syntax

```xml
<virtualization:ExcludedDirectory>
  This element is a case-insensitive string that must start with "$(KnownFolder:<known folder name>)<path to excluded directory>" where "known folder name" specifies one of the known folders under the AppData directory. The rest of the string is the relative path to the excluded directory. For example, "$(KnownFolder:LocalAppData)\Fabrikam\Shared".
</virtualization:ExcludedDirectory>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [virtualization:ExcludedDirectories](element-virtualization-excludeddirectories.md) | Specifies the list of directories that are excluded from file system virtualization.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

For the list of known directories that can be specified for this element, see [KNOWNFOLDERID](/windows/win32/shell/knownfolderid). The folder name specified in the schema syntax is the constant value with the `FOLDERID_` token removed from the string. For example, for the constant `FOLDERID_AccountPictures`, the known folder name is *AccountPictures*.

The following list contains the list of allowed known folder names, current as of this writing.

- AccountPictures
- AdminTools
- AppDataDesktop
- AppDataDocuments
- AppDataFavorites
- AppDataProgramData
- ApplicationShortcuts
- CDBurning
- Cookies
- GameTasks
- History
- ImplicitAppShortcuts
- InternetCache
- Libraries
- LocalAppData
- LocalAppDataLow
- NetHood
- OriginalImages
- PrintHood
- Programs
- QuickLaunch
- Recent
- Ringtones
- RoamingAppData
- RoamedTileImages
- RoamingTiles
- SearchHistory
- SearchTemplates
- SendTo
- SidebarParts
- StartMenu
- Startup
- Templates
- UserPinned
- UserProgramFiles
- UserProgramFilesCommon

## Requirements

| Item | Value |
|--|--|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
