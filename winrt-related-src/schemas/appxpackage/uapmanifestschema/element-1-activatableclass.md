---
description: Declares a runtime class associated with the extensibility point (in OutOfProcessServer).
Search.Product: eADQiWindows 10XVcnh
title: ActivatableClass (in OutOfProcessServer) (Windows 10)
ms.assetid: b2994883-87f9-4aa5-aff8-9c846606c462
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# ActivatableClass (in OutOfProcessServer) (Windows 10)

Declares a runtime class associated with the extensibility point.

## Element hierarchy

> [\<Package\>](element-package.md)
> > [\<Extensions\>](element-extensions.md)
> > > [\<Extension\>](element-extension.md)
> > > > [\<OutOfProcessServer\>](element-outofprocessserver.md)
> > > > > **\<ActivatableClass\>**

## Syntax

```xml
<ActivatableClass
  ActivatableClassId = 'A string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.' >

  <!-- Child elements -->
  ActivatableClassAttribute{0,1000}

</ActivatableClass>
```

### Key

`{}`   specific range of occurrences

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| ActivatableClassId | The identifier of the runtime class in the operating system. | A string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, or `*`. | Yes |  |

### Child Elements

| Child element | Description |
|-|-|
| [ActivatableClassAttribute](element-1-activatableclassattribute.md) | Defines an attribute of the class that is stored in the Windows Runtime property store. |

### Parent Elements

| Parent element | Description |
|-|-|
| [OutOfProcessServer](element-outofprocessserver.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (EXE) that exposes one or more activatable classes. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[ActivatableClass (*type: CT_InProcessActivatableClass*)](element-activatableclass.md)**

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
