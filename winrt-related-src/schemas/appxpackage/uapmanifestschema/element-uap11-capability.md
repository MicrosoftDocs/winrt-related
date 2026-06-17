---
title: uap11:Capability
description: Declares a capability required by a package (uap11:Capability).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap11:Package, uap11:Capabilities, uap11:Capability]
---

# uap11:Capability

Declares a capability required by a package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap11:Capability>`**  

## Syntax

```xml
<uap11:Capability
  Name = 'A required string that can have one of the following values: "graphicsCaptureProgrammatic", or "graphicsCaptureWithoutBorder".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *graphicsCaptureProgrammatic*, *graphicsCaptureWithoutBorder*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| **Minimum OS Version** | Windows 10 (Build 19645) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<Package
    xmlns:uap11="http://schemas.microsoft.com/appx/manifest/uap/windows10/11"  
    IgnorableNamespaces="uap11">
    <Capabilities>
        <uap11:Capability
            Name="graphicsCaptureProgrammatic"/>  
        <uap11:Capability
            Name="graphicsCaptureWithoutBorder"/>  
    </Capabilities>
</Package>
```
