---
title: com4:MiscStatus
description: Specifies how to create and display an object. (com4:MiscStatus)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:MiscStatus

Specifies how to create and display an object.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Class\>](element-com4-managedinprocessserver-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:MiscStatus\>**

## Syntax

```xml
<com4:MiscStatus
  OleMiscFlag = 'An integer with a value between 0 and 4194303.' >

  <!-- Child elements -->
  Aspect

</com4:MiscStatus>
```

## Attributes and elements

### Attributs

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **OleMiscFlag** | The integer value for the view aspect of the object. | An integer with a value between 0 and 4194303. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [Aspect](element-com4-aspect.md) | Specifies the desired data or view aspect of the object when drawing or getting data. |

### Parent element

| Parent element | Description |
|-|-|
| [com4:class](element-com4-managedinprocessserver-class.md) | Specifies the class with which the managed in-process server is associated and sets registration details. |

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
