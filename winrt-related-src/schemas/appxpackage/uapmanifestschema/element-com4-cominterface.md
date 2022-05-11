---
title: com4:ComInterface
description: Declares a package extension point of type **windows.comInterface** (com4:ComInterface).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ComInterface



## Description
Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: **Interface**, **ProxyStub**, or **TypeLib**.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-extension.md">&lt;com4:Extension&gt;</a></dt>
<dd>
<b>&lt;com4:ComInterface&gt;</b>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:ComInterface>
<!-- Child elements -->
  ProxyStub{0,1}
  Interface{0,1}
  TypeLib{0,1}
</com4:ComInterface>
```

## Key
`{}`   specific range of occurrences




## Child Elements

| Element | Description |
| -----------| -------------|
| [ProxyStub](element-com4-proxystub.md) | Registers a proxy stub. |
| [Interface](element-com4-interface.md) | Registers new COM interfaces |
| [TypeLib](element-com4-typelib.md) | Registers a type library.  |

## Remarks

The **comInterface** extension can be under the Application/Extensions/Extension manifest element, or under the Package/Extensions/Extension manifest element. There is no functional difference between these two options, but both placements have different advantages.

If the extension is under Application/Extensions/Extension, you can improve the readability of the manifest by keeping interface registrations near the class registrations that implement them. However, if you place the extension under Package/Extensions/Extension, you won't need to determine which Application to use for each interface. It's possible to use multiple **comInterface** extensions in either Application/Extensions/Extension or Package/Extensions/Extension, but this is neither recommended nor necessary.

> [!NOTE]
> Any registrations in **comInterface** that depend on another registration (e.g. an **Interface** references a **ProxyStub** and/or a **TypeLib**) must be in the same **comInterface** extension. 

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
