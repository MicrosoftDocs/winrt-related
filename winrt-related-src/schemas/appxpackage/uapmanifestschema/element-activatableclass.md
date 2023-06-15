---
description: Declares a runtime class associated with the extensibility point in InProcessServer).
Search.Product: eADQiWindows 10XVcnh
title: ActivatableClass (in InProcessServer) (Windows 10)
ms.assetid: c75a7a4d-1864-4bff-95e6-67cd007ee192
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# ActivatableClass (in InProcessServer) (Windows 10)

Declares a runtime class associated with the extensibility point.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<InProcessServer\>](element-inprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<ActivatableClass\>**

## Syntax

```xml
<ActivatableClass 
  ActivatableClassId = 'A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
  ThreadingModel = 'A string that can be one of the following values: "both", "STA", or "MTA".' >

  <!-- Child elements -->
  ActivatableClassAttribute{0,1000}

</ActivatableClass>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ActivatableClassId** | The identifier of the runtime class in the operating system. | A string with a value between 1 and 255 characters in length that cannot start or end with a period (`.`) or contain these characters: `<`, `>`, `:`, `&`, `"`, `/`, `\`, `|`, `?`, or `*`. | Yes |  |
| **ThreadingModel** | The type of threading model supported by the runtime class. | A string that can be one of the following values: *both*, *STA*, or *MTA*. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [ActivatableClassAttribute](element-activatableclassattribute.md) | Defines an attribute of the class that is stored in the Windows Runtime property store. |

### Parent elements

| Parent element | Description |
|-|-|
| [InProcessServer](element-inprocessserver.md) | Declares a package extensibility point of type **windows.activatableClass.inProcessServer**. The app uses a dynamic link library (DLL) that exposes one or more activatable classes. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[ActivatableClass (type: CT_OutOfProcessActivatableClass)](element-1-activatableclass.md)**

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
