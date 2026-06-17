---
title: uap17:UpdateWhileInUse
description: TBD
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Extensions, uap17:Package, uap17:Properties, uap17:UpdateWhileInUse]
---

# uap17:UpdateWhileInUse

Specifies whether the OS should close the app for app updates, or if the update should be deferred until the next time the app is restarted by the user or a system reboot. The OS will still force-close the app for required OS updates and system reboots.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap17:UpdateWhileInUse>`**  

## Syntax

```xml
<uap17:UpdateWhileInUse>
    <!-- TODO: Add value description -->
</uap17:UpdateWhileInUse>
```

## Value

<!-- TODO: Add value description -->

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/17` |
| **Minimum OS Version** | Windows 11 version 24H2 (Build 26100) |

## Remarks

If the value of this element is set to "defer", then any force update options specified with [AddPackageOptions.ForceTargetAppShutdown](/uwp/api/windows.management.deployment.addpackageoptions.forcetargetappshutdown), [RegisterPackageOptions.ForceTargetAppShutdown](/uwp/api/windows.management.deployment.registerpackageoptions.forcetargetappshutdown), or [DeploymentOptions.ForceApplicationShutdown](/uwp/api/windows.management.deployment.deploymentoptions) will be ignored.

## Examples

<!-- Author content goes here -->
