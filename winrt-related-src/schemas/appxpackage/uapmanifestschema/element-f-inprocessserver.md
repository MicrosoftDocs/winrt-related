---
title: InProcessServer
description: Declares a package extensibility point of type windows.activatableClass.inProcessServer (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, InProcessServer]
---

# InProcessServer

Declares a package extensibility point of type **windows.activatableClass.inProcessServer**. The app uses a dynamic link library (DLL) that exposes one or more activatable classes.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<InProcessServer>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <InProcessServer>

    <!-- Child elements -->
    Path
    ActivatableClass{1,65535}

  </InProcessServer>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | <!-- TODO: Add description --> |  |  |  |
|  | <!-- TODO: Add description --> |  |  |  |
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
| **Path** | The path to the DLL. |
| **ActivatableClass** | Declares a runtime class associated with the extensibility point. |

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

```xml
<Extension
  Category="windows.activatableClass.inProcessServer">
    <InProcessServer>
      <Path>Microsoft.Samples.DllServerAuthoring.dll</Path>
      <ActivatableClass
        ActivatableClassId="Microsoft.Samples.DllServerAuthoring.Toaster" ThreadingModel="both" />
    </InProcessServer>
</Extension>
```
