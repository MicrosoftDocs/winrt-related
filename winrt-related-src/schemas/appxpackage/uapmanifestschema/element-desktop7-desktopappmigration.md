---
title: desktop7:DesktopAppMigration
description: Specifies a set of app migration entries for tiles and pins.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:DesktopAppMigration

Specifies a set of app migration entries for tiles and pins.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Extension\>](element-desktop7-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Shortcut\>](element-desktop7-shortcut.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop7:DesktopAppMigration\>**

## Syntax

```xml
<desktop7:DesktopAppMigration>

    desktop7:DesktopApp{0,1000}

</desktop7:DesktopAppMigration>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop7:DesktopApp](element-desktop7-desktopapp.md) | Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration. |  

### Parent elements

| Parent element | Description |
|-|-|
| [desktop7:Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  

## Remarks

This element requires the [runFullTrust](/windows/uwp/packaging/app-capability-declarations) capability.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **Minimum OS Version** | Windows 10 (Build 19645) |
