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

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-virtualization-filesystemwritevirtualization.md">&lt;virtualization:FileSystemWriteVirtualization&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-virtualization-excludeddirectories.md">&lt;virtualization:ExcludedDirectories&gt;</a></dt>
<dd><b>&lt;virtualization:ExcludedDirectory&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` xml
<virtualization:ExcludedDirectory>$(KnownFolder:[known folder name])\[path to excluded directory]</virtualization:ExcludedDirectory>
```

## Value

This element is a case-insensitive string that must start with "$(KnownFolder:&lt;known folder name&gt;)\\&lt;path to excluded directory&gt;" where *known folder name* specifies one of the known folders under the AppData directory. The rest of the string is the relative path to the excluded directory. For example, "\$(KnownFolder:LocalAppData)\Fabrikam\Shared".

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [virtualization:ExcludedDirectories](element-virtualization-excludeddirectories.md) | Specifies the list of directories that are excluded from file system virtualization.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

For the list of known directories that can be specified for this element, see [KNOWNFOLDERID](/windows/win32/shell/knownfolderid). The folder name specified in the schema syntax is the constant value with the "FOLDERID_" token removed from the string. For example, for the constant **FOLDERID_AccountPictures**, the known folder name is "AccountPictures".

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

| Namespace | Manifest Path | 
|---------------|-------------------------------------------------------------|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |

 

 
