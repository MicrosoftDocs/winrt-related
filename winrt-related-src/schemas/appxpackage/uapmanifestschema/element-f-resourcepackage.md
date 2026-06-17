---
title: ResourcePackage
description: Indicates whether the package is a resource package (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Properties, ResourcePackage]
---

# ResourcePackage

Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a resource.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<ResourcePackage>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <ResourcePackage>
      <!-- TODO: Add value description -->
  </ResourcePackage>
</Package>
```

## Value

<!-- TODO: Add value description -->

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Defines additional metadata about the package including attributes that describe how the package appears to users. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package. Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

If **ResourcePackage** is set to **true**, the manifest performs these semantic checks, which aren't enforced in the schema. A manifest that violates these semantic checks will just fail to validate via the [Packaging APIs](/windows/win32/appxpkg/interfaces).

- A resource package can't define the [Dependencies](element-f-dependencies.md), [Capabilities](element-f-capabilities.md), [Applications](element-f-applications.md), [Extensions (type: CT_PackageExtensions)](element-f-package-extensions.md), and [Framework](element-f-framework.md) elements.
- A resource package can't define [Package\\Identity\\@ProcessorArchitecture](element-f-identity.md), so it always defaults to **neutral**.
- [Resources\\Resource](element-f-resource.md) elements for a resource package can only define one type of attribute, for example, only **Language** or **Scale**.

## Examples

<!-- Author content goes here -->
