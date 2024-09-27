---
ms.assetid: ffb76b68-b2c2-424f-8785-10da06294fb7
title: com:ComInterface
description: Declares a package extension point of type windows.comInterface (com:ComInterface).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:ComInterface

Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:ComInterface\>**

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:ComInterface\>**

## Syntax

```xml
<com:ComInterface>

  <!-- Child elements -->
  com:ProxyStub{0,1000},
  com:Interface{0,10000},
  com:TypeLib{0,1000}

</com:ComInterface>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [com:ProxyStub](element-com-proxystub.md) | Registers a proxy stub. |
| [com:Interface](element-com-interface.md) | Registers new COM Interfaces. |
| [com:TypeLib](element-com-typelib.md) | Registers a type library. |

### Parent elements

| Parent element | Description |
|-|-|
| [com:Extension](element-com-extension.md) | Provides functionality to expose COM registrations to clients outside of the app package. |

## Remarks

The **comInterface** extension can be under the Application/Extensions/Extension manifest element, or under the Package/Extensions/Extension manifest element. There is no functional difference between these two options, but both placements have different advantages.

If the extension is under Application/Extensions/Extension, you can improve the readability of the manifest by keeping interface registrations near the class registrations that implement them. However, if you place the extension under Package/Extensions/Extension, you won't need to determine which Application to use for each interface. It's possible to use multiple **comInterface** extensions in either Application/Extensions/Extension or Package/Extensions/Extension, but this is neither recommended nor necessary.

> [!NOTE]
> Any registrations in **comInterface** that depend on another registration (e.g. an *Interface* references a *ProxyStub* and/or a *TypeLib*) must be in the same **comInterface** extension.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
