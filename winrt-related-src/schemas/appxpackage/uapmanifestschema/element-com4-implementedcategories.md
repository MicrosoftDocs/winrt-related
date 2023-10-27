---
title: com4:ImplementedCategories
description: Specifies categories implemented by the class. (com4:ImplementedCategories)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ImplementedCategories

Specifies categories implemented by the class.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Class\>](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ImplementedCategories\>**

## Syntax

```xml
<com4:ImplementedCategories>

  <!-- Child elements -->
  ImplementedCategory

</com4:ImplementedCategories>
```

## Attributes and elements

### Attributes

None.

### Child Elements

| Child element | Description |
|-|-|
| [ImplementedCategory](element-com4-implementedcategory.md) | Indicates that the class has implemented the specified category. |

### Parent elements

| Parent element | Description |
|-|-|
| [com4:Class](element-com4-class.md) | Specifies properties of a CLSID registered by the package that can be shared by one or more concrete registrations of the CLSID for different class contexts. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| Minimum OS Version | Windows 10 (Build 20348) |
