---
title: com4:ComInterface
description: Declares a package extension point of type **windows.comInterface** (com4:ComInterface).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ComInterface

Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Extension\>](element-com4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ComInterface\>**

## Syntax

```xml
<com4:ComInterface>

<!-- Child elements -->
  ProxyStub{0,1}
  Interface{0,1}
  TypeLib{0,1}

</com4:ComInterface>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [ProxyStub](element-com4-proxystub.md) | Registers a proxy stub. |
| [Interface](element-com4-interface.md) | Registers new COM interfaces |
| [TypeLib](element-com4-typelib.md) | Registers a type library.  |

### Parent elements

| Parent element | Description |
|-|-|
| [com4:Extension](element-com4-extension.md) | Provides functionality to expose COM registrations to clients outside of the app package. The com4 extension is a new version that is a superset of and replacement for the previous COM schema versions. See the Remarks section for more information. |

## Remarks

The **comInterface** extension can be under the Application/Extensions/Extension manifest element, or under the Package/Extensions/Extension manifest element. There is no functional difference between these two options, but both placements have different advantages.

If the extension is under Application/Extensions/Extension, you can improve the readability of the manifest by keeping interface registrations near the class registrations that implement them. However, if you place the extension under Package/Extensions/Extension, you won't need to determine which Application to use for each interface.

It is possible to have multiple **comInterface** extensions under the Applications/Application element, but in most cases this is neither necessary nor recommended. An example of an edge case where multiple **comInterface** extensions are needed is if a package needs some of the registrations to have CompatMode="classic" while others have CompatMode="modern", the only way to do this is to split them between extensions.

> [!NOTE]
> Any registrations in **comInterface** that depend on another registration (e.g. an **Interface** references a **ProxyStub** and/or a **TypeLib**) must be in the same **comInterface** extension.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
