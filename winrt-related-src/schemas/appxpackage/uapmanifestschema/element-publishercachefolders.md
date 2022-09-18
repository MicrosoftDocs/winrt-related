---
description: Declares a package extensibility point of type windows.publisherCacheFolders.
Search.Product: eADQiWindows 10XVcnh
title: PublisherCacheFolders (Windows 10)
ms.assetid: 71425cb8-5f6b-415a-9791-28c7407869dc
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# PublisherCacheFolders (Windows 10)

Declares a package extensibility point of type **windows.publisherCacheFolders**. This specifies one or more folders that the package shares with other packages from the same publisher.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<PublisherCacheFolder\>**

## Syntax

```xml
<PublisherCacheFolders>

  <!-- Child elements -->
  Folder{1,100}

</PublisherCacheFolders>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Folder](element-folder.md) | Specifies a folder that the package shares with other packages from the same publisher. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extension (in type: CT_PackageExtensions)](element-extension.md) | Declares an extensibility point for the package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
