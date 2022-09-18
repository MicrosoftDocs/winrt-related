---
description: Indicates whether the package is a resource package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: ResourcePackage (Windows 10)
ms.assetid: 51cabad7-a2eb-4fa3-ab52-59298555aefb
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# ResourcePackage (Windows 10)

Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a resource.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<ResourcePackage\>**

## Syntax

```xml
<ResourcePackage>
  A boolean value.
</ResourcePackage>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package. Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

## Remarks

If **ResourcePackage** is set to **true**, the manifest performs these semantic checks, which aren't enforced in the schema. A manifest that violates these semantic checks will just fail to validate via the [Packaging APIs](/windows/win32/appxpkg/interfaces).

- A resource package can't define the [Dependencies](element-dependencies.md), [Capabilities](element-capabilities.md), [Applications](element-applications.md), [Extensions (type: CT_PackageExtensions)](element-extensions.md), and [Framework](element-framework.md) elements.
- A resource package can't define [Package\\Identity\\@ProcessorArchitecture](element-identity.md), so it always defaults to **neutral**.
- [Resources\\Resource](element-resource.md) elements for a resource package can only define one type of attribute, for example, only **Language** or **Scale**.

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
