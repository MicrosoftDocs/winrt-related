---
description: Specifies a folder that the package shares with other packages from the same publisher.
Search.Product: eADQiWindows 10XVcnh
title: Folder (Windows 10)
ms.assetid: b412b98e-130a-4152-a264-49a42ef2d97c
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Folder (Windows 10)

Specifies a folder that the package shares with other packages from the same publisher.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<PublisherCacheFolders\>](element-publishercachefolders.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Folder\>**

## Syntax

```xml
<Folder
    Name = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \, /, |, ?, or *.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The folder name, which must be string valid for a folder name. Sub-folders in the folder name are not allowed. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `\`, `/`, `|`, `?`, or `*`. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [PublisherCacheFolders](element-publishercachefolders.md) | Declares a package extensibility point of type **windows.publisherCacheFolders**. This specifies one or more folders that the package shares with other packages from the same publisher. |

## Examples

```xml
    <Extension Category="windows.publisherCacheFolders">
        <Folder Name="Folder1"/>
        <Folder Name="Folder2"/>
    </Extension>
```

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
