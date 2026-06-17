---
title: ActivatableClass (in OutOfProcessServer)
description: Declares a runtime class associated with the extensibility point (in OutOfProcessServer).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, OutOfProcessServer, ActivatableClass]
---

# ActivatableClass (in OutOfProcessServer)

Declares a runtime class associated with the extensibility point.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<OutOfProcessServer>`](element-f-outofprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<ActivatableClass>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <ActivatableClass
    ActivatableClassId = 'A required string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.' >

    <!-- Child elements -->
    ActivatableClassAttribute{0,1000}

  </ActivatableClass>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ActivatableClassId** | The identifier of the runtime class in the operating system. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | Yes |

## Child elements

| Child element | Description |
|-|-|
| [ActivatableClassAttribute](element-f-activatableclassattribute.md) | Defines an attribute of the class that is stored in the Windows Runtime property store. |

## Parent elements

| Parent element | Description |
|-|-|
| [OutOfProcessServer](element-f-outofprocessserver.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (`.exe`) that exposes one or more activatable classes. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->

## See also
The following elements have the same name as this one, but different content or attributes:

- **[ActivatableClass (type: CT_InProcessActivatableClass)](element-f-outofprocessserver-activatableclass.md)**
