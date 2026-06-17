---
title: Applications
description: Represents one or more apps that comprise the package Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Applications]
---

# Applications

Represents one or more apps that comprise the package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ **`<Applications>`**

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Applications>

    <!-- Child elements -->
    Application{1,100}

  </Applications>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [Application](element-f-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## Parent elements

| Parent element | Description |
|-|-|
| [Package](element-f-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |

## Remarks

You can use the **Applications** element to specify one or more apps for the package.

> [!NOTE]
> Although each package can contain one or more apps, packages that contain multiple apps won't pass the Store certification process.

## Examples

<!-- Author content goes here -->
