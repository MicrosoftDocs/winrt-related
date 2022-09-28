---
title: rescap4:ClassicAppCompatKeys
description: Contains registry keys for discovering classic app installations and launching executables.
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap4:ClassicAppCompatKeys

Contains registry keys for discovering classic app installations and launching executables.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<rescap4:Extension\>](element-rescap4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<rescap4:ClassicAppCompatKeys\>**

## Syntax

```xml
<rescap4:ClassicAppCompatKeys>

  <!-- Child elements -->
  rescap4:ClassicAppCompatKey{1,10000}

</rescap4:ClassicAppCompatKeys>
```

### Key

`{}` specific range of occurrences  

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [ClassicAppCompatKey](element-rescap4-classicappcompatkey.md) | Registry keys for discovering classic app installations and launching executables. |

### Parent elements

| Parent element | Description |
|-|-|
| [rescap4:Extension](element-rescap4-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/4` |
