---
title: Folder
description: Specifies a folder that the package shares with other packages from the same publisher.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, PublisherCacheFolders, Folder]
---

# Folder

Specifies a folder that the package shares with other packages from the same publisher.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<PublisherCacheFolders>`](element-f-publishercachefolders.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Folder>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Folder
    Name = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", /, \, &#124;, ?, or *.' />
</Package>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The folder name, which must be string valid for a folder name. Sub-folders in the folder name are not allowed. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | Yes |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [PublisherCacheFolders](element-f-publishercachefolders.md) | Declares a package extensibility point of type **windows.publisherCacheFolders**. This specifies one or more folders that the package shares with other packages from the same publisher. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

```xml
    <Extension Category="windows.publisherCacheFolders">
        <Folder Name="Folder1"/>
        <Folder Name="Folder2"/>
    </Extension>
```
