---
title: rescap4:ClassicAppCompatKeys
description: Contains registry keys for discovering classic app installations and launching executables.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, rescap4:Extension, rescap4:ClassicAppCompatKeys]
---

# rescap4:ClassicAppCompatKeys

Contains registry keys for discovering classic app installations and launching executables.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap4:Extension>`](element-rescap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap4:ClassicAppCompatKeys>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap4:Extension>`](element-rescap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap4:ClassicAppCompatKeys>`**  

## Syntax

```xml
<rescap4:ClassicAppCompatKeys>

  <!-- Child elements -->
  rescap4:ClassicAppCompatKey{0,100000000}
  rescap4:ClassicAppCompatKey{0,100000000}

</rescap4:ClassicAppCompatKeys>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [rescap4:ClassicAppCompatKey](element-rescap4-classicappcompatkey.md) | Registry keys for discovering classic app installations and launching executables. |
| **desktop10:ClassicAppCompatKey** | Registry keys for discovering classic app installations and launching executables. |

## Parent elements

| Parent element | Description |
|-|-|
| [rescap4:Extension](element-rescap4-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/4` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
