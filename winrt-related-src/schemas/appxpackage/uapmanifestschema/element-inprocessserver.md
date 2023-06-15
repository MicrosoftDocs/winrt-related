---
description: Declares a package extensibility point of type windows.activatableClass.inProcessServer (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: InProcessServer (Windows 10)
ms.assetid: 47e3c888-76eb-4d12-977c-ebd947a2b63c
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# InProcessServer (Windows 10)

Declares a package extensibility point of type **windows.activatableClass.inProcessServer**. The app uses a dynamic link library (DLL) that exposes one or more activatable classes.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<InProcessServer\>**

## Syntax

```xml
<InProcessServer>

  <!-- Child elements -->
  Path
  ActivatableClass{1,65535}

</InProcessServer>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child Elements

| Child element | Description |
|-|-|
| [ActivatableClass (type: CT_InProcessActivatableClass)](element-activatableclass.md) | Declares a runtime class associated with the extensibility point. |
| [Path (type: ST_FileName)](element-path.md) | The path to the DLL. |

### Parent Elements

| Parent element | Description |
|-|-|
| [Extension (in type: CT_PackageExtensions)](element-extension.md) | Declares an extensibility point for the package. |

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

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
