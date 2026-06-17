---
title: ActivatableClassAttribute
description: Defines an attribute of the class that is stored in the Windows Runtime property store.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, InProcessServer, ActivatableClass, ActivatableClassAttribute, OutOfProcessServer]
---

# ActivatableClassAttribute

Defines an attribute of the class that is stored in the Windows Runtime property store.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<InProcessServer>`](element-f-inprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<ActivatableClass>`](element-f-outofprocessserver-activatableclass.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<ActivatableClassAttribute>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<OutOfProcessServer>`](element-f-outofprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<ActivatableClass>`](element-f-outofprocessserver-activatableclass.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<ActivatableClassAttribute>`**

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <ActivatableClassAttribute
    Name = 'A required alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
    Type = 'A required string that can have one of the following values: "string", or "integer".'
    Value = 'A required string between 1 and 32767 characters in length.' />
</Package>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the attribute. | A alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | Yes |  |
| **Type** | The type of the attribute. | A string that can have one of the following values: *string*, *integer*. | Yes |  |
| **Value** | The value of the attribute. | A string between 1 and 32767 characters in length. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| **ActivatableClass** | <!-- TODO: Add description --> |
| [ActivatableClass](element-f-outofprocessserver-activatableclass.md) | Declares a runtime class associated with the extensibility point. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
