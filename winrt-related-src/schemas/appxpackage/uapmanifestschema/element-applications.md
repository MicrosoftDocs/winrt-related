---
description: Represents one or more apps that comprise the package Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Applications (Windows 10)
ms.assetid: ad9e07fc-ba58-4465-b3fa-b330ba149f92
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Applications (Windows 10)

Represents one or more apps that comprise the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<Applications\>**

## Syntax

```xml
<Applications>

  <!-- Child elements -->
  Application{1,100}

</Applications>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Application](element-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

### Parent elements

| Parent element | Description |
|-|-|
| [Package](element-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Remarks

You can use the **Applications** element to specify one or more apps for the package.

> [!NOTE]
> Although each package can contain one or more apps, packages that contain multiple apps won't pass the Store certification process.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
