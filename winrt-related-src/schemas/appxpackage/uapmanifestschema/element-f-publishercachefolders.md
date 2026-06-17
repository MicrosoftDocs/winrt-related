---
title: PublisherCacheFolders
description: Declares a package extensibility point of type windows.publisherCacheFolders.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, PublisherCacheFolders]
---

# PublisherCacheFolders

Declares a package extensibility point of type **windows.publisherCacheFolders**. This specifies one or more folders that the package shares with other packages from the same publisher.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<PublisherCacheFolders>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <PublisherCacheFolders>

    <!-- Child elements -->
    Folder{1,100}

  </PublisherCacheFolders>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Specifies a folder that the package shares with other packages from the same publisher. |  |  |  |
|  | Description |  |  |  |
|  | - |  |  |  |
|  | Declares an extensibility point for the package. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

| Child element | Description |
|-|-|
| [Folder](element-f-folder.md) | Specifies a folder that the package shares with other packages from the same publisher. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-f-package-extension.md) | Declares an extensibility point for the package. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
