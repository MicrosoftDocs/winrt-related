---
title: com2:ComInterface
description: Declares a package extension point of type windows.comInterface (com2:ComInterface).
ms.date: 04/20/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com2:ComInterface

Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com2:Extension\>](element-com2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com2:ComInterface\>**

## Syntax

```xml
<com2:ComInterface>

  <!-- Child elements -->
  com:ProxyStub{0,1000},
  com:Interface{0,10000},
  com:TypeLib{0,1000}

</com2:ComInterface>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [ProxyStub](element-com-proxystub.md) | Registers a proxy stub. |
| [Interface](element-com-interface.md) | Registers new COM Interfaces. |
| [TypeLib](element-com-typelib.md) | Registers a type library. |

### Parent elements

| Parent element | Description |
|-|-|
| [com2:Extension](element-com2-extension.md) | Provides functionality to expose COM registrations to clients outside of the app package. |

## Remarks

The **comInterface** extension can be under the Application/Extensions/Extension manifest element, or under the Package/Extensions/Extension manifest element. There is no functional difference between these two options, but both placements have different advantages.

If the extension is under Application/Extensions/Extension, you can improve the readability of the manifest by keeping interface registrations near the class registrations that implement them. However, if you place the extension under Package/Extensions/Extension, you won't need to determine which Application to use for each interface. It's possible to use multiple **comInterface** extensions in either Application/Extensions/Extension or Package/Extensions/Extension, but this is neither recommended nor necessary.

> [!NOTE]
> Any registrations in **comInterface** that depend on another registration (e.g. an **Interface** references a **ProxyStub** and/or a **TypeLib**) must be in the same **comInterface** extension.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/2` |
| Minimum OS Version | Windows 10 version 1709 (Build 16299) |
