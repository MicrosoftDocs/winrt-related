---
description: Defines an attribute of the class that is stored in the Windows Runtime property store (Windows 10, descendant of InProcessServer).
Search.Product: eADQiWindows 10XVcnh
title: ActivatableClassAttribute (Windows 10, descendant of InProcessServer)
ms.assetid: 6070f277-74ae-4cf8-9467-9109c4983f9d
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# ActivatableClassAttribute (Windows 10, descendant of InProcessServer)

Defines an attribute of the class that is stored in the Windows Runtime property store.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<InProcessServer\>](element-inprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<ActivatableClass\>](element-activatableclass.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<ActivatableClassAttribute\>**

## Syntax

```xml
<ActivatableClassAttribute
  Name  = 'An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  Type  = 'A string that can be one of the following values: "string" or "integer".'
  Value = 'A string with a value between 1 and 255 characters in length.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| Name | The name of the attribute. | An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | Yes |  |
| Type | The type of the attribute. | A string that can be one of the following values: *string* or *integer*. | Yes |  |
| Value | The value of the attribute. | A string with a value between 1 and 255 characters in length. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [ActivatableClass (type: *CT_InProcessActivatableClass*)](element-activatableclass.md) | Declares a runtime class associated with the extensibility point. |
| [ActivatableClass (type: *CT_OutOfProcessActivatableClass*)](element-1-activatableclass.md)] | Declares a runtime class associated with the extensibility point. |

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
